#!/usr/bin/env python3
"""Chuẩn bị file Word để đẩy lên Google Drive và ghi ID/link vào projects/<du-an>/_drive.json.

Quy tắc (CLAUDE.md):
- Mọi file đẩy lên Drive là **Word (.docx) nguyên bản** — không chuyển Google Doc (disableConversionToGoogleType=true).
- Thư mục Drive do **user tạo** và đưa link; **mỗi lần đẩy hỏi user** đẩy vào thư mục nào (script chỉ in gợi ý).
- Không tự tạo thư mục, không xoá, không chia sẻ, không di chuyển file trên Drive.
Script KHÔNG gọi Drive — Claude gọi công cụ Google Drive (MCP) theo kế hoạch in ra.

Cách dùng:
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an>                    # tài liệu Word — mặc định
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --only "FSD/Sprint 4/BBA-45…"   # chỉ các key này (key = đường dẫn trong Document/, bỏ .md và _vX.Y)
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --diagrams         # + ảnh sơ đồ (PNG)
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --wireframe        # + ảnh wireframe (PNG, trạng thái mặc định)
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --force            # coi mọi mục là đã đổi
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --record <key> <file_id> <url> --folder <id|link> [--folder-name "<tên>"]
    python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --status

Tài liệu được đẩy: URD.md, SRS.md, UC.md, backlog.md, test-cases.md, mọi .md trong Document/FSD/ và Document/Test_Case/
(kể cả thư mục Sprint <n>), cộng project.json › drive.docs. Không đẩy: Bien_Ban_Khao_Sat/, SRS/srs/, brainstorm.md.
Markdown → .docx bằng to_docx.py (định dạng dự án nếu có docx_style) vào .output/; > 3,0 MB thì nén ảnh vào .tmp/drive/.
Gợi ý thư mục cho mỗi mục: thư mục đã dùng cho chính key đó → project.json › drive.folder_hints (khớp tiền tố key)
→ thư mục đã dùng cho cùng loại tài liệu → drive.root_url. Trạng thái: create · replace · skip · too_big · missing · error.
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
from ba_paths import DOC_HOME, Project, resolve  # noqa: E402

TO_DOCX = REPO / ".claude" / "skills" / "write-srs" / "scripts" / "to_docx.py"
LIMIT = 3_000_000  # giới hạn ~3,1 MB file mỗi lần gọi công cụ Drive, chừa biên
DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
MAIN_DOCS = {"URD.md": "URD", "SRS.md": "SRS", "UC.md": "Use Case", "backlog.md": "Backlog", "test-cases.md": "Test case"}
LEGACY_KEYS = {"srs": "SRS/SRS", "urd": "URD/URD", "uc": "Use_Case/UC", "backlog": "Backlog/backlog", "tc": "Test_Case/test-cases",
               "workflow": "SRS/workflow", "tom-tat-fsd": "FSD/tom-tat-fsd"}
COMPACT_STEPS = [(1400, 128), (1200, 64), (1000, 32), (800, 16)]  # (chiều rộng tối đa, số màu)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def version_of(path: Path) -> str:
    if path.suffix != ".md" or not path.exists():
        return ""
    m = re.search(r"^\|\s*Phiên bản\s*\|\s*([0-9][0-9.]*)", path.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else ""


def load_state(project: Project) -> dict:
    state = json.loads(project.drive_json.read_text(encoding="utf-8")) if project.drive_json.exists() else {}
    state.setdefault("files", {})
    state.setdefault("folders_used", {})
    for old, new in LEGACY_KEYS.items():  # key kiểu cũ (srs, urd…) -> đường dẫn trong Document/
        if old in state["files"] and new not in state["files"]:
            state["files"][new] = state["files"].pop(old)
    return state


def save_state(project: Project, state: dict) -> None:
    project.drive_json.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_docx(project: Project, src: Path, docx: Path) -> str | None:
    """Xuất lại .docx khi chưa có hoặc cũ hơn nguồn. Trả về lỗi (nếu có)."""
    if docx.exists() and docx.stat().st_mtime >= src.stat().st_mtime:
        return None
    rel = src.relative_to(project.document).as_posix()
    cmd = [sys.executable, str(TO_DOCX), project.slug] + ([] if rel == "SRS/SRS.md" else ["--src", rel])
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


def doc_key(project: Project, src: Path) -> str:
    """Key ổn định của tài liệu: đường dẫn trong Document/, bỏ .md và hậu tố _vX.Y (bản mới thay bản cũ)."""
    rel = src.relative_to(project.document).with_suffix("").as_posix()
    return re.sub(r"_v\d+(?:\.\d+)*$", "", rel)


def doc_title(project: Project, src: Path, key: str) -> str:
    for prefix, pattern in project.config.get("drive", {}).get("titles", {}).items():
        if key.startswith(prefix):
            return pattern.format(stem=src.stem, du_an=project.slug)
    if src.name in MAIN_DOCS:
        v = version_of(src)
        return f"{MAIN_DOCS[src.name]} — {project.slug}{' v' + v if v else ''}.docx"
    return f"{src.stem}.docx"


def catalog(project: Project, groups: set[str]) -> list[dict]:
    """Mọi mục có thể đẩy: key, nguồn, file upload (.docx / .png), tiêu đề, mime."""
    srcs: list[Path] = [project.doc(n) for n in MAIN_DOCS]
    for kind in ("fsd", "tc"):
        srcs += sorted(p for p in project.doc_dir(kind).rglob("*.md") if not p.name.startswith("_"))
    for d in project.config.get("drive", {}).get("docs", []):
        srcs += sorted(project.root.glob(d["src"]))
    items, seen = [], set()
    for src in srcs:
        if src in seen:
            continue
        seen.add(src)
        key = doc_key(project, src)
        items.append({"key": key, "kind": key.split("/")[0], "source": src,
                      "upload": project.export(f"{src.stem}.docx"), "title": doc_title(project, src, key),
                      "mime": DOCX_MIME})

    def images(kind: str, paths):
        for p in sorted(paths):
            items.append({"key": f"{kind}/{p.name}", "kind": kind, "source": p, "upload": p, "title": p.name,
                          "mime": "image/png"})

    if "diagrams" in groups:
        images("Diagram/Flow", project.diagrams.glob("*.png"))
    if "wireframe" in groups:
        images("Diagram/Wireframe", [p for p in project.png.glob("SCR-*.png") if "--" not in p.name])
    return items


def folder_id(text: str) -> str:
    m = re.search(r"/folders/([\w-]+)", text) or re.search(r"[?&]id=([\w-]+)", text)
    return m.group(1) if m else text.strip()


def suggestions(project: Project, state: dict, key: str, kind: str) -> list[dict]:
    """Thư mục gợi ý (theo thứ tự) để hỏi user — không bao giờ tự chọn thay user."""
    used = state.get("folders_used", {})
    out: list[str] = []
    cur = state["files"].get(key, {})
    if cur.get("folder_id"):
        out.append(cur["folder_id"])
    cfg = project.config.get("drive", {})
    for prefix, link in sorted(cfg.get("folder_hints", {}).items(), key=lambda kv: -len(kv[0])):
        if key.startswith(prefix):
            out.append(folder_id(link))
    out += [fid for fid, v in sorted(used.items(), key=lambda kv: kv[1].get("last_used", ""), reverse=True)
            if kind in v.get("kinds", [])]
    if cfg.get("root_url"):
        out.append(folder_id(cfg["root_url"]))
    res, seen = [], set()
    for fid in out:
        if fid and fid not in seen:
            seen.add(fid)
            res.append({"id": fid, "name": used.get(fid, {}).get("name", ""),
                        "url": f"https://drive.google.com/drive/folders/{fid}"})
    return res[:3]


def plan(project: Project, groups: set[str], only: list[str], force: bool) -> dict:
    state = load_state(project)
    out = []
    for it in catalog(project, groups):
        if only and it["key"] not in only:
            continue
        rec = {k: it[k] for k in ("key", "kind", "title", "mime")}
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
            if up.suffix != ".docx":
                out.append({**rec, "action": "too_big", "size": up.stat().st_size,
                            "error": f"{up.name} {up.stat().st_size:,} byte > {LIMIT:,}"})
                continue
            dst = project.tmp / "drive" / up.name
            size = compact_docx(up, dst)
            if size > LIMIT:
                out.append({**rec, "action": "too_big", "size": size, "error": f"{up.name} nén ảnh rồi vẫn {size:,} byte"})
                continue
            upload = dst
        cur = state["files"].get(it["key"], {})
        src_sha = sha256(src)
        action = "create" if not cur.get("file_id") else ("replace" if force or cur.get("source_sha256") != src_sha else "skip")
        out.append({**rec, "action": action, "version": version_of(src), "size": upload.stat().st_size,
                    "compacted": upload != up, "suggest": suggestions(project, state, it["key"], it["kind"]),
                    "file_ref": f"sha256:{sha256(upload)}:{upload.resolve().as_posix()}", "current": cur or None})
    return {"project": project.slug, "root_url": project.config.get("drive", {}).get("root_url", ""), "items": out}


def main(argv: list[str]) -> int:
    args = argv[1:]
    if not args or args[0].startswith("--"):
        print(__doc__)
        return 2
    project = resolve(args[0])
    state = load_state(project)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if "--record" in args:
        i = args.index("--record")
        key, file_id, url = (args[i + 1:i + 4] + ["", "", ""])[:3]
        folder = folder_id(args[args.index("--folder") + 1]) if "--folder" in args else ""
        fname = args[args.index("--folder-name") + 1] if "--folder-name" in args else ""
        spec = {it["key"]: it for it in catalog(project, {"diagrams", "wireframe"})}.get(key)
        if not (spec and file_id and url and folder):
            print("ERROR: --record <key> <file_id> <url> --folder <id|link> [--folder-name <tên>] (key lấy từ kế hoạch)")
            return 2
        old = state["files"].get(key)
        if old and old.get("file_id") and old["file_id"] != file_id:
            state.setdefault("history", []).append({**old, "key": key, "replaced_at": now})
        src = spec["source"]
        state["files"][key] = {"file_id": file_id, "url": url, "folder_id": folder, "title": spec["title"],
                               "version": version_of(src), "source_sha256": sha256(src) if src.exists() else "",
                               "synced_at": now}
        fu = state["folders_used"].setdefault(folder, {"name": fname, "kinds": []})
        fu["name"] = fname or fu.get("name", "")
        fu["last_used"] = now
        if spec["kind"] not in fu["kinds"]:
            fu["kinds"].append(spec["kind"])
        save_state(project, state)
        print(f"drive_pack: {key} -> {url} (thư mục {fname or folder})")
        return 0

    if "--status" in args:
        files = state.get("files", {})
        print(f"{project.slug}: {len(files)} file trên Drive · thư mục gốc: {project.config.get('drive', {}).get('root_url') or 'chưa gắn'}")
        for k, v in sorted(files.items()):
            print(f"  {k:<50} v{v.get('version') or '-':<6} {v['url']}")
        return 0

    groups = {g for g in ("diagrams", "wireframe") if f"--{g}" in args}
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
            sug = " | ".join(f"{s['name'] or s['id']} {s['url']}" for s in it["suggest"]) or "chưa có — hỏi user dán link"
            print(f"{it['action']:<7} {it['key']} · \"{it['title']}\"{' (nén ảnh)' if it.get('compacted') else ''}"
                  f" · {it['file_ref']} · gợi ý thư mục: {sug}")
        elif it["action"] in ("error", "too_big"):
            print(f"{it['action']:<7} {it['key']} · {it['error']}")
    print(f"drive_pack: {', '.join(f'{k} {v}' for k, v in sorted(counts.items()))} · kế hoạch: {project.rel(plan_file)}"
          " · HỎI user thư mục đích trước khi upload (Word, disableConversionToGoogleType=true)")
    return 1 if any(it["action"] in ("error", "too_big") for it in result["items"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
