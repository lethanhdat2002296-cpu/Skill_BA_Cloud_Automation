#!/usr/bin/env python3
"""Điểm vào cho mọi việc theo dự án — tìm đúng dự án, xem nhanh trạng thái, tạo thẻ PROJECT.md.

Cách dùng:
    python tools/project.py list                 # tên dự án + phiên bản (1 dòng / dự án)
    python tools/project.py find "<tên>"         # tên gần đúng -> đúng 1 slug, hoặc danh sách gợi ý
    python tools/project.py status <du-an>       # tóm tắt ≤ 15 dòng: phiên bản, số mã, OQ mở, màn chờ vẽ, Drive
    python tools/project.py card <du-an>         # ghi projects/<du-an>/PROJECT.md (giữ phần "Ghi chú" viết tay)
    python tools/project.py new <du-an>          # tạo khung thư mục dự án mới

Quy tắc: mọi lệnh chỉ đọc trong projects/<du-an>/ của dự án được chọn, không quét dự án khác.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ba_paths import REPO, SUBDIRS, Project, all_projects, find, resolve, slugify  # noqa: E402

START, END = "<!-- card:start -->", "<!-- card:end -->"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def version(text: str) -> str:
    m = re.search(r"^\|\s*Phiên bản\s*\|\s*([0-9][0-9.]*)", text, re.M)
    return m.group(1) if m else ""


def ids(text: str, kind: str, head: bool = False) -> list[str]:
    pat = rf"^#{{3,4}} +({kind}-\d+(?:\.\d+)?)\b" if head else rf"^\|\s*({kind}-\d+)\s*\|"
    return list(dict.fromkeys(re.findall(pat, text, re.M)))


def open_oq(text: str) -> tuple[list[str], list[str]]:
    open_, partial = [], []
    for oid, cell in re.findall(r"^\|\s*(OQ-\d+)\s*\|\s*([^|]*)\|", text, re.M):
        if "Đã trả lời một phần" in cell:
            partial.append(oid)
        elif "Đã trả lời" not in cell:
            open_.append(oid)
    return open_, partial


def facts(p: Project) -> dict:
    srs, urd, uc, bl = (read(p.doc(n)) for n in ("SRS.md", "URD.md", "UC.md", "backlog.md"))
    main = srs or urd
    hist = re.findall(r"^\|\s*(\d+\.\d+(?:\.\d+)?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]*)\|", srs, re.M)
    pending = [r for r in re.findall(r"^\|\s*(SCR-\d+)\s*\|", read(p.ui / "_pending.md").split("## Đã xử lý")[0], re.M)]
    drive = json.loads(read(p.drive_json) or "{}")
    title = re.search(r"^# +(?:SRS|URD)\s*[—–-]\s*(.+)$", main, re.M)
    o, part = open_oq(main)
    log = subprocess.run(["git", "log", "-1", "--format=%cs %s", "--", p.rel(p.root)], cwd=REPO,
                         capture_output=True, text=True, encoding="utf-8").stdout.strip()
    return {
        "title": title.group(1).strip() if title else p.slug,
        "versions": {k: version(t) for k, t in (("SRS", srs), ("URD", urd), ("UC", uc), ("backlog", bl)) if t},
        "counts": {"US": len(ids(urd, "US", True)), "UC": len(ids(uc, "UC", True)), "FR": len(ids(srs, "FR", True)),
                   "NFR": len(ids(srs, "NFR", True)), "SCR": len(ids(srs, "SCR")), "AS": len(ids(main, "AS")),
                   "OQ": len(ids(main, "OQ"))},
        "oq_open": o, "oq_partial": part, "history": hist[-1] if hist else None, "pending": pending,
        "drive": drive, "last_commit": log,
        "files": {f: len(read(p.root / f).splitlines()) for f in
                  ("docs/SRS.md", "docs/URD.md", "docs/UC.md", "docs/backlog.md", "ui/flows.md") if (p.root / f).exists()},
        "srs_split": p.srs_dir.is_dir(),
    }


def status_lines(p: Project, f: dict) -> list[str]:
    c = f["counts"]
    out = [f"{p.slug} — {f['title']}",
           "Phiên bản: " + (" · ".join(f"{k} {v}" for k, v in f["versions"].items()) or "chưa có tài liệu"),
           f"Mã: {c['US']} US · {c['UC']} UC · {c['FR']} FR · {c['NFR']} NFR · {c['SCR']} SCR · {c['AS']} AS · {c['OQ']} OQ",
           f"OQ mở ({len(f['oq_open'])}): {', '.join(f['oq_open']) or 'không'}"
           + (f" · trả lời một phần: {', '.join(f['oq_partial'])}" if f["oq_partial"] else "")]
    if f["history"]:
        v, d, summary = f["history"]
        out.append(f"Lần cập nhật cuối: {v} ({d}) — {summary.strip()[:160]}")
    out.append(f"Màn chờ vẽ lại: {', '.join(f['pending']) or 'không'}")
    folders = f["drive"].get("folders", {})
    if folders.get("project"):
        out.append(f"Drive: https://drive.google.com/drive/folders/{folders['project']} ({len(f['drive'].get('files', {}))} mục)")
    out.append("File: " + ", ".join(f"{k} ({n} dòng)" for k, n in f["files"].items())
               + ("" if f["srs_split"] or not f["files"].get("docs/SRS.md") else " — SRS chưa tách srs/"))
    if f["last_commit"]:
        out.append(f"Commit cuối: {f['last_commit'][:120]}")
    return out


def card(p: Project) -> Path:
    f = facts(p)
    old = read(p.card)
    notes = old.split(END, 1)[1].strip() if END in old else "## Ghi chú (viết tay — giữ nguyên khi sinh lại thẻ)\n\n- "
    drive = f["drive"]
    links = [f"- Thư mục: https://drive.google.com/drive/folders/{drive['folders']['project']}"] if drive.get("folders", {}).get("project") else []
    links += [f"- {k}: {v['url']}" for k, v in sorted(drive.get("files", {}).items()) if "/" not in k]
    body = [f"# {f['title']} (`{p.slug}`)", "", START,
            "> Sinh bởi `python tools/project.py card " + p.slug + "` — không sửa tay đoạn này. Đọc thẻ này TRƯỚC khi mở tài liệu lớn.", "",
            *[f"- {ln}" for ln in status_lines(p, f)[1:]], "",
            "## Bản đồ file", "",
            "| Cần | Mở | Ghi chú |", "|---|---|---|",
            "| Yêu cầu hợp nhất mới nhất | `input/_tong-hop.md` | Nguồn ưu tiên khi có |",
            "| Lịch sử nạp / khác biệt | `input/_manifest.md`, `input/_changes/` | Đọc change report mới nhất, không đọc hết |",
            "| FR / NFR / SCR / AS / OQ | `docs/SRS.md` (hoặc `docs/srs/*.md`) | Tra mã → file: `build_srs.py <du-an> --index`; Read theo offset |",
            "| User story / Use case | `docs/URD.md`, `docs/UC.md` | `grep -n \"^#### US-07\"` rồi Read đoạn đó |",
            "| Backlog | `docs/backlog.md` → `exports/backlog.csv` | |",
            "| Màn hình | `ui/flows.md`, `ui/screens/SCR-xx-*.html` | Chỉ mở ảnh `ui/png/` khi cần review |",
            "| Sơ đồ | `diagrams/` (`swimlanes/*.json` là nguồn) | |",
            "| File giao khách | `exports/` | Sinh ra — không sửa tay |", ""]
    if links:
        body += ["## Google Drive", "", *links, ""]
    body += [END, "", notes, ""]
    p.card.write_text("\n".join(body), encoding="utf-8")
    return p.card


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, rest = argv[1], argv[2:]
    if cmd == "list":
        for n in all_projects():
            p = Project(n)
            v = version(read(p.doc("SRS.md")) or read(p.doc("URD.md")))
            print(f"{n:<30} {('v' + v) if v else '(chưa có tài liệu)'}")
        return 0
    if not rest:
        print(__doc__)
        return 2
    name = " ".join(rest)
    if cmd == "find":
        p, cands = find(name)
        print(p.slug if p else f"KHÔNG RÕ: '{name}' — gợi ý: {', '.join(cands) or '(chưa có dự án)'}")
        return 0 if p else 1
    if cmd == "new":
        p = Project(slugify(name))
        if p.exists():
            print(f"ERROR: đã có projects/{p.slug}/")
            return 1
        for sub in SUBDIRS:
            (p.root / sub).mkdir(parents=True, exist_ok=True)
            (p.root / sub / ".gitkeep").touch()
        card(p)
        print(f"project: đã tạo projects/{p.slug}/ ({', '.join(SUBDIRS)}) + PROJECT.md")
        return 0
    p = resolve(name)
    if cmd == "status":
        print("\n".join(status_lines(p, facts(p))))
        return 0
    if cmd == "card":
        print(f"project: {p.rel(card(p))}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
