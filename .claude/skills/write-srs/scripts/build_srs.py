#!/usr/bin/env python3
"""Ghép outputs/<du-an>/srs/*.md thành outputs/<du-an>/SRS.md + sinh ma trận truy vết + chỉ mục tra cứu.

Cách dùng:
    python .claude/skills/write-srs/scripts/build_srs.py <du-an>            # ghép SRS.md
    python .claude/skills/write-srs/scripts/build_srs.py <du-an> --index    # ghép + in chỉ mục FR/SCR/AS/OQ -> file

Cấu trúc srs/ (ghép theo thứ tự tên file; file bắt đầu bằng "_" bị bỏ qua):
    00-dau-trang.md          # SRS — Tên, bảng thuộc tính, Lịch sử phiên bản
    01-gioi-thieu.md         ## 1. Giới thiệu
    02-tong-quan.md          ## 2. Mô tả tổng quan
    03-00-chuc-nang.md       ## 3. Yêu cầu chức năng (+ mô hình trạng thái chung)
    03-01-<phan-he>.md       ### 3.1 <Phân hệ>  +  #### FR-xx — ... (mỗi phân hệ một file)
    04-phi-chuc-nang.md      ## 4. ...  (### NFR-xx)
    05-tich-hop.md           ## 5. ...
    06-man-hinh.md           ## 6. Screen Inventory (6.1 bảng + 6.2 ảnh wireframe)
    07-user-flow.md          ## 7. User flow
    09-gia-dinh-cau-hoi.md   ## 9. Assumptions & Open Questions
Mục 8 (Ma trận truy vết) được SINH TỰ ĐỘNG từ dòng "Truy vết:" của từng FR — không viết tay.
Chỉ khi có file 08-*.md thì dùng file đó thay vì tự sinh.

SRS.md là file sinh ra: sửa trong srs/, không sửa SRS.md.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
GENERATED_NOTE = "<!-- SRS.md được sinh tự động bởi build_srs.py từ thư mục srs/ — sửa trong srs/, KHÔNG sửa file này -->"
FR_HEAD_RE = re.compile(r"^#{3,4} +(FR-\d+)\s*[—–-]?\s*(.*)$", re.M)
NO_UI_RE = re.compile(r"không\s+có\s+ui[^·|\n]*", re.I)


def srs_parts(project: Path) -> list[Path]:
    d = project / "srs"
    return sorted(p for p in d.glob("*.md") if not p.name.startswith("_")) if d.is_dir() else []


def needs_build(project: Path) -> bool:
    parts = srs_parts(project)
    out = project / "SRS.md"
    return bool(parts) and (not out.exists() or max(p.stat().st_mtime for p in parts) > out.stat().st_mtime)


def fr_blocks(text: str) -> list[dict]:
    blocks = []
    heads = list(FR_HEAD_RE.finditer(text))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        nxt = re.search(r"^#{2,3} +(?!FR-)", text[m.end():end], re.M)
        body = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():end]
        trace = re.search(r"Truy vết:?\**:?\s*(.*)$", body, re.M)
        line = trace.group(1) if trace else ""
        us_part, _, scr_part = line.partition("Màn hình")
        scr_part = scr_part.lstrip(" :*")
        no_ui = ""
        if NO_UI_RE.match(scr_part):
            # "Không có UI (kết quả hiển thị ở SCR-02)" vẫn là không có UI; SCR trong ngoặc chỉ là ghi chú
            scrs = []
            no_ui = "Không có UI (đã bỏ)" if re.search(r"đã\s+bỏ", scr_part, re.I) else "Không có UI"
        else:
            scrs = re.findall(r"SCR-\d+", scr_part)
        blocks.append({
            "id": m.group(1), "title": m.group(2).strip(),
            "us": re.findall(r"US-\d+", us_part),
            "scr": scrs, "no_ui": no_ui,
            "has_trace": bool(trace),
        })
    return blocks


def trace_section(frs: list[dict]) -> str:
    rows = ["## 8. Ma trận truy vết", "",
            "> Sinh tự động từ dòng \"Truy vết\" của từng FR (build_srs.py).", "",
            "| FR | Tên | URD (US) | Màn hình (SCR) |", "|---|---|---|---|"]
    for f in frs:
        scr = ", ".join(f["scr"]) or f["no_ui"] or "Không có UI"
        title = f["title"].replace("|", "/")
        rows.append(f"| {f['id']} | {title} | {', '.join(f['us']) or '—'} | {scr} |")
    return "\n".join(rows) + "\n"


def build(project: Path, quiet: bool = False) -> tuple[Path, list[str]]:
    parts = srs_parts(project)
    if not parts:
        raise FileNotFoundError(f"không có {project.relative_to(REPO)}/srs/*.md")
    warns: list[str] = []
    texts = [(p, p.read_text(encoding="utf-8-sig").strip() + "\n") for p in parts]
    joined = "\n".join(t for _, t in texts)
    frs = fr_blocks(joined)
    for f in frs:
        if not f["has_trace"]:
            warns.append(f"{f['id']}: thiếu dòng 'Truy vết:' — ma trận truy vết sẽ ghi 'Không có UI'")
    has_manual_8 = any(p.name.startswith("08") for p, _ in texts)
    out_chunks = [GENERATED_NOTE, ""]
    inserted = has_manual_8
    for p, t in texts:
        if not inserted and p.name[:2] > "08":
            out_chunks.append(trace_section(frs))
            inserted = True
        out_chunks.append(t)
    if not inserted:
        out_chunks.append(trace_section(frs))
    out = project / "SRS.md"
    out.write_text("\n".join(out_chunks), encoding="utf-8")
    if not quiet:
        for w in warns:
            print(f"WARN: {w}")
        print(f"build_srs: {len(parts)} file -> {out.relative_to(REPO)} · {len(frs)} FR · ma trận truy vết "
              f"{'viết tay (08-*.md)' if has_manual_8 else 'tự sinh'}")
    return out, warns


def index(project: Path) -> dict:
    """Chỉ mục: mã -> file trong srs/ (để sửa đúng chỗ khi cập nhật)."""
    idx: dict = {"FR": {}, "NFR": {}, "SCR": {}, "AS": {}, "OQ": {}, "files": {}}
    for p in srs_parts(project):
        t = p.read_text(encoding="utf-8-sig")
        rel = f"srs/{p.name}"
        idx["files"][rel] = len(t.splitlines())
        for f in fr_blocks(t):
            idx["FR"][f["id"]] = {"file": rel, "title": f["title"], "us": f["us"], "scr": f["scr"] or f["no_ui"]}
        for m in re.finditer(r"^#{3,4} +(NFR-\d+)\s*[—–-]?\s*(.*)$", t, re.M):
            idx["NFR"][m.group(1)] = {"file": rel, "title": m.group(2).strip()}
        for m in re.finditer(r"^\|\s*(SCR-\d+)\s*\|\s*([^|]+)\|", t, re.M):
            idx["SCR"].setdefault(m.group(1), {"file": rel, "title": m.group(2).strip()})
        for m in re.finditer(r"ui/png/(SCR-\d+)-([a-z0-9-]+?)\.png", t):
            idx["SCR"].setdefault(m.group(1), {"file": rel})["slug"] = m.group(2)
        for kind in ("AS", "OQ"):
            for m in re.finditer(rf"^\|\s*({kind}-\d+)\s*\|\s*([^|]+)\|", t, re.M):
                idx[kind][m.group(1)] = {"file": rel, "text": m.group(2).strip()[:80]}
    for fr, v in idx["FR"].items():
        for s in v["scr"] if isinstance(v["scr"], list) else []:
            idx["SCR"].setdefault(s, {}).setdefault("fr", []).append(fr)
    return idx


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    project = REPO / "outputs" / args[0].strip("/\\")
    try:
        build(project)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return 1
    if "--index" in argv:
        print("INDEX " + json.dumps(index(project), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
