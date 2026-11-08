#!/usr/bin/env python3
"""Chuẩn bị file để đẩy projects/<du-an>/ lên Google Drive và ghi ID/link vào projects/<du-an>/_drive.json.

Script KHÔNG gọi Drive (không có API key) — Claude gọi công cụ Google Drive (MCP) theo kế hoạch script in ra.
Thư mục trên Drive giống hệt git: "BA Projects/<du-an>/{docs,diagrams,ui,exports,input,_luu-tru}".

Cách dùng:
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an>                  # tài liệu (docs) — mặc định
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --diagrams       # + ảnh sơ đồ
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --ui             # + ảnh wireframe (trạng thái mặc định)
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --input          # + tài liệu khảo sát gốc
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --exports        # + file .docx/.csv gốc (≤ 3 MB)
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --only srs urd   # chỉ các key này
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --force          # coi mọi mục là đã đổi
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --folders root=<id> project=<id> docs=<id> …
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --record <key> <file_id> <url>
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --status

Tài liệu (thư mục docs/ trên Drive, chuyển thành Google Doc / Sheet):
    srs  docs/SRS.md -> exports/SRS.docx · urd docs/URD.md -> exports/URD.docx
    uc   docs/UC.md  -> exports/UC.docx  · backlog exports/backlog.csv -> Google Sheet
File .docx lớn hơn giới hạn upload (3,0 MB) được nén ảnh vào .tmp/drive/.
Kế hoạch đầy đủ ghi vào .tmp/drive/plan.json; màn hình chỉ in mục cần đẩy (create/replace) kèm file_ref.
Trạng thái: create · replace · skip (không đổi) · too_big · missing · error.
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
sys.path.insert(0, str(REPO / "tools"))
from ba_paths import SUBDIRS, Project, resolve  # noqa: E402

TO_DOCX = REPO / ".claude" / "skills" / "write-srs" / "scripts" / "to_docx.py"
LIMIT = 3_000_000  # giới hạn ~3,1 MB file mỗi lần gọi công cụ Drive, chừa biên
DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".pdf": "application/pdf",
        ".docx": DOCX_MIME, ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".csv": "text/csv", ".md": "text/markdown", ".txt": "text/plain"}
DOCS = [  # key, nguồn (so thay đổi), file upload, tiêu đề
    ("srs", "docs/SRS.md", "exports/SRS.docx", "SRS — {du_an}"),
    ("urd", "docs/URD.md", "exports/URD.docx", "URD — {du_an}"),
    ("uc", "docs/UC.md", "exports/UC.docx", "Use Case — {du_an}"),
    ("backlog", "exports/backlog.csv", "exports/backlog.csv", "Backlog — {du_an}"),
]
COMPACT_STEPS = [(1400, 128), (1200, 64), (1000, 32), (800, 16)]  # (chiều rộng tối đa, số màu)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def version_of(path: Path) -> str:
    if path.suffix != ".md":
        return ""
    m = re.search(r"^\|\s*Phiên bản\s*\|\s*([0-9][0-9.]*)", path.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else ""


def load_state(project: Project) -> dict:
    if project.drive_json.exists():
        return json.loads(project.drive_json.read_text(encoding="utf-8"))
    return {"folders": {}, "files": {}, "archived": []}


def save_state(project: Project, state: dict) -> None:
    project.drive_json.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_docx(project: Project, src: Path, docx: Path) -> str | None:
    """Xuất lại .docx khi chưa có hoặc cũ hơn nguồn. Trả về lỗi (nếu có)."""
    if docx.exists() and docx.stat().st_mtime >= src.stat().st_mtime:
        return None
    cmd = [sys.executable, str(TO_DOCX), project.slug] + ([] if src.name == "SRS.md" else ["--src", src.name])
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


def catalog(project: Project, groups: set[str]) -> list[dict]:
    """Mọi mục có thể đẩy: key, thư mục Drive, nguồn, file upload, tiêu đề, mime, có chuyển sang Google Doc/Sheet không."""
    du_an = project.slug
    items = []
    for key, src, up, title in DOCS:
        items.append({"key": key, "folder": "docs", "source": project.root / src, "upload": project.root / up,
                      "title": title.format(du_an=du_an), "convert": True,
                      "mime": "text/csv" if up.endswith(".csv") else DOCX_MIME})

    def files(folder: str, paths):
        for p in sorted(paths):
            if p.suffix.lower() in MIME:
                items.append({"key": f"{folder}/{p.relative_to(project.root / folder).as_posix()}", "folder": folder,
                              "source": p, "upload": p, "title": p.name, "mime": MIME[p.suffix.lower()],
                              "convert": p.suffix.lower() in (".md", ".txt")})

    if "diagrams" in groups:
        files("diagrams", project.diagrams.glob("*.png"))
    if "ui" in groups:
        files("ui", [p for p in project.png.glob("SCR-*.png") if "--" not in p.name])
    if "input" in groups:
        files("input", [p for p in project.input.rglob("*") if p.is_file()
                        and not any(part.startswith("_") for part in p.relative_to(project.input).parts)])
    if "exports" in groups:
        files("exports", project.exports.glob("*"))
    return items


def plan(project: Project, groups: set[str], only: list[str], force: bool) -> dict:
    state = load_state(project)
    out = []
    for it in catalog(project, groups):
        if only and it["key"] not in only:
            continue
        rec = {k: it[k] for k in ("key", "folder", "title", "mime", "convert")}
        src, up = it["source"], it["upload"]
        if not src.exists():
            out.append({**rec, "action": "missing"})
            continue
        if up.suffix == ".docx" and src.suffix == ".md":
            err = ensure_docx(project, src, up)
            if err:
                out.append({**rec, "action": "error", "error": err})
                continue
        upload = up
        if up.stat().st_size > LIMIT:
            if up.suffix != ".docx" or not it["convert"]:
                out.append({**rec, "action": "too_big", "size": up.stat().st_size,
                            "error": f"{up.name} {up.stat().st_size:,} byte > {LIMIT:,} (chỉ nén được docx chuyển thành Google Doc)"})
                continue
            dst = project.tmp / "drive" / up.name
            size = compact_docx(up, dst)
            if size > LIMIT:
                out.append({**rec, "action": "too_big", "size": size, "error": f"{up.name} nén rồi vẫn {size:,} byte"})
                continue
            upload = dst
        cur = state["files"].get(it["key"], {})
        src_sha = sha256(src)
        action = "create" if not cur.get("file_id") else ("replace" if force or cur.get("source_sha256") != src_sha else "skip")
        out.append({**rec, "action": action, "version": version_of(src), "size": upload.stat().st_size,
                    "compacted": upload != up, "parent_id": state.get("folders", {}).get(it["folder"], ""),
                    "file_ref": f"sha256:{sha256(upload)}:{upload.resolve().as_posix()}", "current": cur or None})
    return {"project": project.slug, "folders": state.get("folders", {}), "items": out}


def main(argv: list[str]) -> int:
    args = argv[1:]
    if not args or args[0].startswith("--"):
        print(__doc__)
        return 2
    project = resolve(args[0])
    state = load_state(project)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if "--folders" in args:
        pairs = [a.split("=", 1) for a in args[args.index("--folders") + 1:] if "=" in a]
        allowed = {"root", "project", "archive", *SUBDIRS}
        bad = [k for k, _ in pairs if k not in allowed]
        if not pairs or bad:
            print(f"ERROR: --folders key=id … với key thuộc {sorted(allowed)}")
            return 2
        state.setdefault("folders", {}).update(dict(pairs))
        save_state(project, state)
        print(f"drive_pack: đã lưu {len(pairs)} thư mục vào {project.rel(project.drive_json)}")
        return 0

    if "--record" in args:
        i = args.index("--record")
        key, file_id, url = (args[i + 1:i + 4] + ["", "", ""])[:3]
        spec = {it["key"]: it for it in catalog(project, {"diagrams", "ui", "input", "exports"})}.get(key)
        if not (spec and file_id and url):
            print("ERROR: --record <key> <file_id> <url> (key lấy từ kế hoạch, vd. srs, diagrams/uc-01.png)")
            return 2
        old = state["files"].get(key)
        if old and old.get("file_id") and old["file_id"] != file_id:
            state.setdefault("archived", []).append({**old, "key": key, "archived_at": now})
        src = spec["source"]
        state["files"][key] = {"file_id": file_id, "url": url, "folder": spec["folder"], "version": version_of(src),
                               "source_sha256": sha256(src) if src.exists() else "", "synced_at": now}
        save_state(project, state)
        print(f"drive_pack: {key} -> {url}")
        return 0

    if "--status" in args:
        files = state.get("files", {})
        print(f"{project.slug}: {len(files)} mục trên Drive, {len(state.get('archived', []))} bản lưu trữ")
        for k, v in sorted(files.items()):
            print(f"  {k:<40} v{v.get('version') or '-':<6} {v['url']}")
        return 0

    groups = {g for g in ("diagrams", "ui", "input", "exports") if f"--{g}" in args}
    only = [a for a in args[args.index("--only") + 1:] if not a.startswith("--")] if "--only" in args else []
    try:
        result = plan(project, groups, only, "--force" in args)
    except ImportError:
        print("ERROR: thiếu Pillow để nén ảnh (pip install pillow)")
        return 1
    project.tmp.joinpath("drive").mkdir(parents=True, exist_ok=True)
    plan_file = project.tmp / "drive" / "plan.json"
    plan_file.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    counts: dict[str, int] = {}
    for it in result["items"]:
        counts[it["action"]] = counts.get(it["action"], 0) + 1
        if it["action"] in ("create", "replace"):
            print(f"{it['action']:<7} {it['key']} -> {it['folder']}/ ({it['mime']}{', nén ảnh' if it.get('compacted') else ''})"
                  f" · parent={it['parent_id'] or 'CHƯA CÓ'} · {it['file_ref']}")
        elif it["action"] in ("error", "too_big"):
            print(f"{it['action']:<7} {it['key']} · {it['error']}")
    missing_folders = [f for f in ("root", "project", "archive", *SUBDIRS) if f not in result["folders"]]
    print(f"drive_pack: {', '.join(f'{k} {v}' for k, v in sorted(counts.items()))} · kế hoạch: {project.rel(plan_file)}"
          + (f" · thiếu ID thư mục: {', '.join(missing_folders)}" if missing_folders else ""))
    return 1 if any(it["action"] in ("error", "too_big") for it in result["items"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
