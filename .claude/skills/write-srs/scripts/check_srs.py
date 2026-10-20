#!/usr/bin/env python3
"""Kiểm tra tự động SRS.md theo checklist.md (các mục ⚙).

Cách dùng:
    python .claude/skills/write-srs/scripts/check_srs.py <du-an>            # sau write-srs: thiếu ảnh/HTML = WARN
    python .claude/skills/write-srs/scripts/check_srs.py <du-an> --final    # cuối pipeline: thiếu ảnh/HTML/docx = ERROR

Exit code 1 nếu có ERROR.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_srs import build, needs_build  # noqa: E402

SECTION_TITLES = {
    1: "Giới thiệu", 2: "Mô tả tổng quan", 3: "Yêu cầu chức năng", 4: "Yêu cầu phi chức năng",
    5: "Tích hợp & dữ liệu", 6: "Screen Inventory", 7: "User flow", 8: "Ma trận truy vết",
    9: "Assumptions & Open Questions",
}
PLACEHOLDER_RE = re.compile(r"\{\{|\}\}|\bTODO\b|\bTBD\b|\blorem\b|\b(?:FR|NFR|SCR|US|AS|OQ)-xx\b|^\s*…\s*$|\|\s*…\s*\|", re.I | re.M)
NO_UI_RE = re.compile(r"không\s+có\s+ui", re.I)


def strip_code(text: str) -> str:
    return re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)


def sections(text: str) -> dict[int, str]:
    out: dict[int, str] = {}
    parts = re.split(r"^(## +\d+\..*)$", text, flags=re.M)
    for i in range(1, len(parts), 2):
        num = int(re.match(r"## +(\d+)\.", parts[i]).group(1))
        out[num] = parts[i] + parts[i + 1]
    return out


def table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        s = line.strip()
        if s.startswith("|") and not re.fullmatch(r"\|[\s:|-]+\|?", s):
            rows.append([c.strip() for c in s.strip("|").split("|")])
    return rows


def find_col(header: list[str], *names: str) -> int | None:
    for i, h in enumerate(header):
        hl = h.lower()
        if any(n.lower() == hl or n.lower() in hl for n in names):
            return i
    return None


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    final = "--final" in argv
    if not args:
        print(__doc__)
        return 2
    du_an = args[0].strip("/\\")
    project = REPO / "outputs" / du_an
    if needs_build(project):
        build(project)
    srs_path = project / "SRS.md"
    if not srs_path.exists():
        print(f"ERROR: không có {srs_path.relative_to(REPO)}")
        return 1

    errors: list[str] = []
    warns: list[str] = []
    late = errors if final else warns  # lỗi chỉ tính khi đã qua bước render

    raw = srs_path.read_text(encoding="utf-8")
    text = strip_code(raw)
    secs = sections(text)

    # A. Cấu trúc
    nums = [int(n) for n in re.findall(r"^## +(\d+)\.", text, flags=re.M)]
    for n, title in SECTION_TITLES.items():
        if n not in secs:
            errors.append(f"thiếu mục {n}. {title}")
    if nums[: len(SECTION_TITLES)] != sorted(nums[: len(SECTION_TITLES)]):
        errors.append(f"thứ tự mục không đúng: {nums}")
    for m in PLACEHOLDER_RE.finditer(text):
        line_no = text[: m.start()].count("\n") + 1
        line = text.splitlines()[line_no - 1].strip()
        errors.append(f"placeholder còn sót (dòng ~{line_no}): {line[:90]}")

    # B. FR
    fr_blocks = {}
    fr_ids = re.findall(r"^#{3,4} +(FR-\d+)\b", text, flags=re.M)
    for k, c in Counter(fr_ids).items():
        if c > 1:
            errors.append(f"mã trùng: {k} xuất hiện {c} lần")
    for m in re.finditer(r"^#{3,4} +(FR-\d+)\b.*?(?=^#{2,4} |\Z)", text, flags=re.M | re.S):
        fr_blocks[m.group(1)] = m.group(0)
    for fr, block in fr_blocks.items():
        idx = block.lower().find("acceptance criteria")
        if idx < 0 or not re.search(r"^\s*(?:\d+\.|[-*])\s+\S", block[idx:], flags=re.M):
            errors.append(f"{fr}: thiếu Acceptance criteria (ít nhất 1 tiêu chí)")
    if not fr_ids:
        errors.append("không có FR nào (heading phải dạng '#### FR-01 — Tên' trong srs/03-*.md)")

    nfr_ids = re.findall(r"^#{3,4} +(NFR-\d+)\b", text, flags=re.M)
    for k, c in Counter(nfr_ids).items():
        if c > 1:
            errors.append(f"mã trùng: {k} xuất hiện {c} lần")
    if not nfr_ids:
        warns.append("không có NFR nào")

    # E. Screen Inventory
    scr_info: dict[str, dict] = {}
    inv = secs.get(6, "")
    rows = table_rows(inv.split("### 6.2")[0] if "### 6.2" in inv else inv)
    if rows:
        header = rows[0]
        c_fr = find_col(header, "FR")
        c_type = find_col(header, "Loại")
        ids = []
        for r in rows[1:]:
            if not re.fullmatch(r"SCR-\d+", r[0]):
                continue
            ids.append(r[0])
            frs = re.findall(r"FR-\d+", r[c_fr]) if c_fr is not None and c_fr < len(r) else []
            typ = r[c_type].strip().lower() if c_type is not None and c_type < len(r) else ""
            scr_info[r[0]] = {"fr": frs, "type": typ}
            if not frs:
                errors.append(f"{r[0]}: không map tới FR nào trong Screen Inventory")
            for f in frs:
                if f not in fr_blocks:
                    errors.append(f"{r[0]}: tham chiếu {f} không tồn tại")
            if typ not in ("storefront", "backend"):
                errors.append(f"{r[0]}: cột Loại phải là 'storefront' hoặc 'backend' (đang là '{typ}')")
        for k, c in Counter(ids).items():
            if c > 1:
                errors.append(f"mã trùng: {k} xuất hiện {c} lần trong Screen Inventory")
    if not scr_info:
        warns.append("Screen Inventory không có SCR nào (hệ thống không có UI?)")

    img_refs = dict()
    for scr, slug in re.findall(r"ui/png/(SCR-\d+)-([a-z0-9-]+?)\.png", raw):
        img_refs.setdefault(scr, slug)
    for scr in scr_info:
        if scr not in img_refs:
            errors.append(f"{scr}: thiếu dòng ảnh ![{scr} — …](ui/png/{scr}-<slug>.png) trong mục 6.2")
            continue
        stem = f"{scr}-{img_refs[scr]}"
        if not (project / "ui" / "png" / f"{stem}.png").exists():
            late.append(f"{scr}: chưa có ảnh ui/png/{stem}.png")
        if not (project / "ui" / "screens" / f"{stem}.html").exists():
            late.append(f"{scr}: chưa có wireframe ui/screens/{stem}.html")
    for scr in img_refs:
        if scr not in scr_info:
            errors.append(f"{scr}: có ảnh trong 6.2 nhưng không có trong bảng Screen Inventory")

    # C. Truy vết
    urd_path = project / "URD.md"
    us_ids = set(re.findall(r"^#{2,4} +(US-\d+)\b", urd_path.read_text(encoding="utf-8"), flags=re.M)) if urd_path.exists() else None
    if us_ids is None:
        warns.append("không có URD.md — bỏ qua kiểm tra US")
    trace_rows = [r for r in table_rows(secs.get(8, "")) if r and re.fullmatch(r"FR-\d+", r[0])]
    traced = {}
    for r in trace_rows:
        fr = r[0]
        traced[fr] = r
        if fr not in fr_blocks:
            errors.append(f"ma trận truy vết: {fr} không được định nghĩa ở mục 3")
        scr_cell = r[-1]
        scrs = re.findall(r"SCR-\d+", scr_cell)
        if not scrs and not NO_UI_RE.search(scr_cell):
            errors.append(f"{fr}: ma trận truy vết phải có SCR-xx hoặc 'Không có UI'")
        for s in scrs:
            if s not in scr_info:
                errors.append(f"{fr}: tham chiếu {s} không có trong Screen Inventory")
        if us_ids is not None:
            for us in re.findall(r"US-\d+", " ".join(r[1:-1])):
                if us not in us_ids:
                    errors.append(f"{fr}: tham chiếu {us} không có trong URD.md")
    for fr in fr_blocks:
        if fr not in traced:
            errors.append(f"{fr}: không có dòng trong ma trận truy vết (mục 8)")
    traced_scr = {s for r in trace_rows for s in re.findall(r"SCR-\d+", r[-1])}
    for s in scr_info:
        if s not in traced_scr:
            warns.append(f"{s}: không xuất hiện trong ma trận truy vết")

    # F. Assumptions & Open Questions
    aq_rows = table_rows(secs.get(9, ""))
    as_ids = [r[0] for r in aq_rows if re.fullmatch(r"AS-\d+", r[0])]
    oq_ids = [r[0] for r in aq_rows if re.fullmatch(r"OQ-\d+", r[0])]
    for k, c in Counter(as_ids + oq_ids).items():
        if c > 1:
            errors.append(f"mã trùng: {k} xuất hiện {c} lần trong mục 9")
    if as_ids and not oq_ids:
        errors.append("có giả định (AS) nhưng mục Câu hỏi mở (OQ) rỗng")
    for ref in sorted(set(re.findall(r"\b(?:AS|OQ)-\d+\b", text)) - set(as_ids) - set(oq_ids)):
        warns.append(f"{ref} được nhắc tới nhưng không có trong bảng mục 9")
    for ref in sorted(set(re.findall(r"\bFR-\d+\b", text)) - set(fr_blocks)):
        errors.append(f"{ref} được nhắc tới nhưng không được định nghĩa")

    # G. Xuất bản
    if final and not (project / "SRS.docx").exists():
        errors.append("chưa có SRS.docx")

    for w in warns:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    n_sf = sum(1 for v in scr_info.values() if v["type"] == "storefront")
    n_be = sum(1 for v in scr_info.values() if v["type"] == "backend")
    no_ui = sum(1 for r in trace_rows if NO_UI_RE.search(r[-1]))
    print(f"check_srs: {len(fr_blocks)} FR ({no_ui} không có UI), {len(nfr_ids)} NFR, "
          f"{len(scr_info)} SCR ({n_sf} storefront, {n_be} backend), {len(as_ids)} AS, {len(oq_ids)} OQ"
          f"{' · US trong URD: ' + str(len(us_ids)) if us_ids is not None else ''} · "
          f"{'PASS' if not errors else f'{len(errors)} lỗi'}, {len(warns)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
