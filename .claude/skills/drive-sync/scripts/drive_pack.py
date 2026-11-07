#!/usr/bin/env python3
"""Chuẩn bị file để đẩy outputs/<du-an>/ lên Google Drive và ghi lại ID/link vào outputs/<du-an>/_drive.json.

Script KHÔNG gọi Drive (không có API key) — Claude gọi công cụ Google Drive (MCP) theo kế hoạch script in ra.

Cách dùng:
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an>                 # in DRIVE_PLAN {json}
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --only srs urd  # chỉ một số tài liệu
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --force         # coi mọi tài liệu là đã đổi
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --folders <root_id> <project_id> <archive_id>
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --record <key> <file_id> <url>
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --status

Tài liệu (key):
    srs      SRS.md     -> SRS.docx      -> Google Doc "SRS — <du-an>"
    urd      URD.md     -> URD.docx      -> Google Doc "URD — <du-an>"
    uc       UC.md      -> UC.docx       -> Google Doc "Use Case — <du-an>"
    backlog  backlog.csv                 -> Google Sheet "Backlog — <du-an>"
File .docx lớn hơn giới hạn upload (3,0 MB) được nén ảnh (thu nhỏ, giảm màu) vào outputs/<du-an>/.tmp/drive/.
Trạng thái mỗi tài liệu trong kế hoạch: create (chưa có trên Drive), replace (nguồn đã đổi), skip (không đổi),
too_big (nén rồi vẫn quá giới hạn), missing (không có file nguồn).
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
import sys
import zipfile
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
TO_DOCX = REPO / ".claude" / "skills" / "write-srs" / "scripts" / "to_docx.py"
LIMIT = 3_000_000  # giới hạn ~3,1 MB file mỗi lần gọi công cụ Drive, chừa biên
DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
ARTIFACTS = [
    # key, nguồn, file upload, tiêu đề, mime upload
    ("srs", "SRS.md", "SRS.docx", "SRS — {du_an}", DOCX_MIME),
    ("urd", "URD.md", "URD.docx", "URD — {du_an}", DOCX_MIME),
    ("uc", "UC.md", "UC.docx", "Use Case — {du_an}", DOCX_MIME),
    ("backlog", "backlog.csv", "backlog.csv", "Backlog — {du_an}", "text/csv"),
]
# (chiều rộng tối đa, số màu) — thử lần lượt tới khi vừa giới hạn
COMPACT_STEPS = [(1400, 128), (1200, 64), (1000, 32), (800, 16)]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def version_of(md: Path) -> str:
    if md.suffix != ".md":
        return ""
    m = re.search(r"^\|\s*Phiên bản\s*\|\s*([0-9][0-9.]*)", md.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else ""


def load_state(project: Path) -> dict:
    p = project / "_drive.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"folders": {}, "files": {}, "archived": []}


def save_state(project: Path, state: dict) -> None:
    (project / "_drive.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_docx(du_an: str, src: Path, docx: Path) -> str | None:
    """Xuất lại .docx khi chưa có hoặc cũ hơn nguồn. Trả về lỗi (nếu có)."""
    if docx.exists() and docx.stat().st_mtime >= src.stat().st_mtime:
        return None
    cmd = [sys.executable, str(TO_DOCX), du_an] + ([] if src.name == "SRS.md" else ["--src", src.name])
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 or not docx.exists():
        return f"to_docx thất bại cho {src.name}: {(r.stdout + r.stderr)[-300:]}"
    return None


def compact_docx(src: Path, dst: Path) -> int:
    """Nén ảnh PNG/JPEG trong docx cho tới khi file <= LIMIT. Trả về kích thước cuối."""
    from PIL import Image  # Pillow có sẵn cùng Playwright; thiếu thì báo lỗi rõ ở main()

    data_in = zipfile.ZipFile(src)
    size = src.stat().st_size
    for width, colors in COMPACT_STEPS:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
            for info in data_in.infolist():
                data = data_in.read(info.filename)
                if info.filename.startswith("word/media/") and info.filename.lower().endswith((".png", ".jpg", ".jpeg")):
                    im = Image.open(io.BytesIO(data))
                    if im.width > width:
                        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
                    im = im.convert("RGB").quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
                    b = io.BytesIO()
                    # giữ nguyên tên/đuôi file để document.xml vẫn trỏ đúng; Word/Drive đọc theo nội dung
                    im.save(b, "PNG", optimize=True)
                    data = b.getvalue()
                # không truyền lại `info`: writestr sửa CRC/size của nó, lần nén sau sẽ đọc lỗi
                zout.writestr(info.filename, data)
        size = len(buf.getvalue())
        if size <= LIMIT:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(buf.getvalue())
            return size
    return size


def plan(du_an: str, project: Path, only: list[str], force: bool) -> dict:
    state = load_state(project)
    items = []
    for key, src_name, up_name, title, mime in ARTIFACTS:
        if only and key not in only:
            continue
        src = project / src_name
        item = {"key": key, "title": title.format(du_an=du_an), "source": src_name, "mime": mime,
                "google_type": "spreadsheet" if mime == "text/csv" else "document"}
        if not src.exists():
            items.append({**item, "action": "missing"})
            continue
        up = project / up_name
        if up_name.endswith(".docx"):
            err = ensure_docx(du_an, src, up)
            if err:
                items.append({**item, "action": "error", "error": err})
                continue
        upload = up
        if up.stat().st_size > LIMIT:
            dst = project / ".tmp" / "drive" / up_name
            size = compact_docx(up, dst)
            if size > LIMIT:
                items.append({**item, "action": "too_big", "size": size,
                              "error": f"{up_name} nén rồi vẫn {size:,} byte > {LIMIT:,}"})
                continue
            upload = dst
        src_sha = sha256(src)
        cur = state["files"].get(key, {})
        if not cur.get("file_id"):
            action = "create"
        elif force or cur.get("source_sha256") != src_sha:
            action = "replace"
        else:
            action = "skip"
        up_sha = sha256(upload)
        items.append({**item, "action": action, "version": version_of(src),
                      "upload_path": str(upload), "size": upload.stat().st_size,
                      "compacted": upload != up, "source_sha256": src_sha,
                      "file_ref": f"sha256:{up_sha}:{upload.resolve().as_posix()}",
                      "current": cur or None})
    return {"project": du_an, "folders": state.get("folders", {}), "items": items}


def main(argv: list[str]) -> int:
    args = argv[1:]
    if not args or args[0].startswith("--"):
        print(__doc__)
        return 2
    du_an = args[0].strip("/\\")
    project = REPO / "outputs" / du_an
    if not project.is_dir():
        print(f"ERROR: không có outputs/{du_an}/")
        return 1
    state = load_state(project)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if "--folders" in args:
        i = args.index("--folders")
        root, proj, arch = (args[i + 1:i + 4] + ["", "", ""])[:3]
        if not (root and proj and arch):
            print("ERROR: --folders cần 3 ID: <root_id> <project_id> <archive_id>")
            return 2
        state["folders"] = {"root": root, "project": proj, "archive": arch}
        save_state(project, state)
        print(f"drive_pack: đã lưu thư mục vào outputs/{du_an}/_drive.json")
        return 0

    if "--record" in args:
        i = args.index("--record")
        key, file_id, url = (args[i + 1:i + 4] + ["", "", ""])[:3]
        spec = {a[0]: a for a in ARTIFACTS}.get(key)
        if not (spec and file_id and url):
            print("ERROR: --record <key> <file_id> <url> (key: " + ", ".join(a[0] for a in ARTIFACTS) + ")")
            return 2
        src = project / spec[1]
        old = state["files"].get(key)
        if old and old.get("file_id") and old["file_id"] != file_id:
            state.setdefault("archived", []).append({**old, "key": key, "archived_at": now})
        state["files"][key] = {"file_id": file_id, "url": url, "version": version_of(src),
                               "source_sha256": sha256(src) if src.exists() else "", "synced_at": now}
        save_state(project, state)
        print(f"drive_pack: {key} -> {url}")
        return 0

    if "--status" in args:
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return 0

    only = []
    if "--only" in args:
        only = [a for a in args[args.index("--only") + 1:] if not a.startswith("--")]
    try:
        result = plan(du_an, project, only, "--force" in args)
    except ImportError:
        print("ERROR: thiếu Pillow để nén ảnh (pip install pillow)")
        return 1
    for it in result["items"]:
        extra = f" · {it['size']:,} byte" + (" (đã nén ảnh)" if it.get("compacted") else "") if "size" in it else ""
        print(f"{it['action']:<8} {it['key']:<8} {it['title']}{extra}" + (f" · {it['error']}" if it.get("error") else ""))
    print("DRIVE_PLAN " + json.dumps(result, ensure_ascii=False))
    return 1 if any(it["action"] in ("error", "too_big") for it in result["items"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
