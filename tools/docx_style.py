"""Áp định dạng Word theo project.json (`docx_style`) lên file .docx do pandoc sinh ra.

Dùng: from docx_style import apply_style; apply_style(Path("x.docx"), Project("bba").config["docx_style"])
CLI:  python tools/docx_style.py <file.docx> <du-an>

Quy tắc:
- Khổ A4, lề 2,54 cm (page, margin_cm).
- Mọi style chữ (Normal, Body Text, First Paragraph, Compact, Heading 1-6, Title, List…) → font + cỡ chữ cấu hình
  (heading theo heading_sizes_pt, in đậm). Font gán cả ascii / hAnsi / eastAsia / cs để tiếng Việt không đổi font.
- Đoạn văn thân bài (không phải heading, list, ô bảng, chú thích ảnh): giãn dòng line_spacing, thụt dòng đầu first_line_indent_in.
- List: giãn dòng line_spacing, không thụt dòng đầu (list có thụt riêng).
- Bảng: kẻ khung đơn (ngoài + trong) border_pt, màu border_color; hàng đầu là tiêu đề: nền header_fill, chữ đậm,
  lặp lại khi sang trang; độ rộng 100%, cột rộng theo nội dung; chữ trong ô giãn dòng table.line_spacing, không thụt, cách trên/dưới cell_space_pt.
"""
from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Mm, Pt

HEADING_PREFIX = ("Heading", "Title", "Subtitle", "TOC Heading")


def _set_font(style_or_run, name: str, size: float | None = None, bold: bool | None = None) -> None:
    font = style_or_run.font
    font.name = name
    if size:
        font.size = Pt(size)
    if bold is not None:
        font.bold = bold
    rpr = style_or_run.element.get_or_add_rPr() if hasattr(style_or_run.element, "get_or_add_rPr") else None
    if rpr is None:
        return
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(attr), name)
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rfonts.get(qn(attr)) is not None:
            del rfonts.attrib[qn(attr)]


def _spacing(pf, line: float, before: float | None = None, after: float | None = None) -> None:
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = line
    if before is not None:
        pf.space_before = Pt(before)
    if after is not None:
        pf.space_after = Pt(after)


def _table_borders(tbl, size_eighths: int, color: str) -> None:
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(size_eighths))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.append(borders)
    for old in tblPr.findall(qn("w:tblW")):
        tblPr.remove(old)
    w = OxmlElement("w:tblW")
    w.set(qn("w:w"), "5000")
    w.set(qn("w:type"), "pct")
    tblPr.append(w)


def _fit_columns(tbl, total_twips: int) -> None:
    """Độ rộng cột theo độ dài chữ (cột ngắn như '#', 'Mã' không chiếm ngang cột mô tả)."""
    rows = tbl.rows
    if not rows:
        return
    n = max(len(r.cells) for r in rows)
    need = [4] * n
    for r in rows:
        for i, c in enumerate(r.cells[:n]):
            longest_word = max((len(w) for w in c.text.split()), default=0)
            need[i] = max(need[i], min(len(c.text), 70), longest_word + 2)
    weights = [max(4.0, x ** 0.85) for x in need]
    widths = [int(total_twips * w / sum(weights)) for w in weights]
    grid = tbl._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(w))
    for r in rows:
        for c, w in zip(r.cells[:n], widths):
            tcPr = c._tc.get_or_add_tcPr()
            for old in tcPr.findall(qn("w:tcW")):
                tcPr.remove(old)
            tcw = OxmlElement("w:tcW")
            tcw.set(qn("w:w"), str(w))
            tcw.set(qn("w:type"), "dxa")
            tcPr.insert(0, tcw)
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn("w:tblLayout")):
        tblPr.remove(old)
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)


def _shade(cell, fill: str) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def _repeat_header(row) -> None:
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:tblHeader")) is None:
        el = OxmlElement("w:tblHeader")
        el.set(qn("w:val"), "true")
        trPr.append(el)


def _is_list(p) -> bool:
    ppr = p._p.pPr
    return (ppr is not None and ppr.numPr is not None) or p.style.name.lower().startswith("list")


def apply_style(path: Path, cfg: dict) -> dict:
    doc = Document(str(path))
    font, size = cfg.get("font", "Arial"), float(cfg.get("size_pt", 10))
    line, indent = float(cfg.get("line_spacing", 1.5)), float(cfg.get("first_line_indent_in", 0.5))
    hsizes = cfg.get("heading_sizes_pt", [14, 12, 11, 10])
    t = cfg.get("table", {})
    t_line, cell_sp = float(t.get("line_spacing", 1.0)), float(t.get("cell_space_pt", 2))

    for st in doc.styles:
        if st.type != 1:  # 1 = paragraph; character styles dùng font của đoạn
            if st.type == 2:
                _set_font(st, font)
            continue
        if st.name.startswith(HEADING_PREFIX):
            lvl = int(st.name.split()[-1]) if st.name.split()[-1].isdigit() else 1
            _set_font(st, font, hsizes[min(lvl, len(hsizes)) - 1] if st.name.startswith("Heading") else hsizes[0] + 2, True)
            st.paragraph_format.first_line_indent = Inches(0)
        else:
            _set_font(st, font, size)

    for sec in doc.sections:  # pandoc không ghi khổ giấy → A4, lề 2,54 cm (cấu hình: page / margin_cm)
        if cfg.get("page", "A4") == "A4":
            sec.page_width, sec.page_height = Mm(210), Mm(297)
        m = Cm(float(cfg.get("margin_cm", 2.54)))
        sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = m
    sec = doc.sections[0]
    text_width = int((sec.page_width - sec.left_margin - sec.right_margin) / 635)  # EMU -> twips
    in_table = set()
    for tbl in doc.tables:
        _fit_columns(tbl, text_width)
        _table_borders(tbl, max(2, round(float(t.get("border_pt", 0.5)) * 8)), t.get("border_color", "000000"))
        for r_i, row in enumerate(tbl.rows):
            if r_i == 0 and t.get("repeat_header", True):
                _repeat_header(row)
            for cell in row.cells:
                if r_i == 0 and t.get("header_fill"):
                    _shade(cell, t["header_fill"])
                for p in cell.paragraphs:
                    in_table.add(id(p._p))
                    pf = p.paragraph_format
                    pf.first_line_indent = Inches(0)
                    _spacing(pf, t_line, cell_sp, cell_sp)
                    for run in p.runs:
                        run.font.size = Pt(size)
                        run.font.name = font
                        if r_i == 0 and t.get("header_bold", True):
                            run.font.bold = True

    stats = {"body": 0, "list": 0, "table_paras": len(in_table), "tables": len(doc.tables)}
    for p in doc.paragraphs:
        name = p.style.name
        if name.startswith(HEADING_PREFIX) or name in ("Image Caption", "Captioned Figure", "Table Caption", "Source Code"):
            continue
        pf = p.paragraph_format
        if _is_list(p):
            _spacing(pf, line)
            pf.first_line_indent = Inches(0)
            stats["list"] += 1
        elif p.text.strip() and not p._p.xpath(".//w:drawing"):
            _spacing(pf, line)
            pf.first_line_indent = Inches(indent)
            stats["body"] += 1
    doc.save(str(path))
    return stats


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from ba_paths import resolve
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    cfg = resolve(sys.argv[2]).config.get("docx_style")
    if not cfg:
        print("ERROR: dự án không có docx_style trong project.json")
        sys.exit(1)
    print(f"docx_style: {apply_style(Path(sys.argv[1]), cfg)}")
