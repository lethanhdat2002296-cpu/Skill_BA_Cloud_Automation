"""Định dạng file Word FRD theo mẫu "DOTB | FUNCTIONAL REQUIREMENTS SPECIFICATION" (mẫu PDF user gửi 12/11/2026).

Chỉ đổi cách trình bày, không đổi nội dung chữ. Chạy SAU to_docx.py:
    python tools/frs_format.py projects/bba/.output/<stem>.docx [--product "BBA SMS"]

Mẫu:
- Khổ Letter, lề trái / phải 1,25", trên 1", dưới 0,9".
- Đầu trang: "DOTB | FUNCTIONAL REQUIREMENTS SPECIFICATION". Chân trang (căn phải): "<product> · <tên tài liệu> · v<phiên bản> | Page N".
- H1 thứ nhất ("Functional Requirements Specification"): Calibri đậm, xanh đậm, kẻ đường xanh bên dưới.
  H1 thứ hai (tên tính năng): Arial đậm, cỡ lớn, xanh dương.
- Bảng thuộc tính đầu tài liệu → 3 dòng chữ "Nhãn: giá trị" (dự án / module / tính năng; mã tài liệu / sprint / phiên bản /
  trạng thái / ngày; người soạn / review / duyệt). Giữ nguyên nhãn và giá trị.
- Heading mục (H2), mục con (H3), nhãn phần (H4): Calibri đậm, xanh dương.
- Thân bài Arial 11pt, giãn dòng đơn, không thụt dòng đầu.
- Bảng: không kẻ dọc; đường xanh trên cùng, dưới hàng tiêu đề và cuối bảng; chữ tiêu đề xanh, chữ trong bảng Arial 8,5pt.
  Bảng ở mục "5. Tổng quan tính năng…": cột đầu in đậm, hàng nội dung tô xanh nhạt.
"""
from __future__ import annotations

import argparse
import copy
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

sys.path.insert(0, str(Path(__file__).resolve().parent))
from docx_style import _fit_columns, _repeat_header, _set_font, _shade  # noqa: E402

NAVY, BLUE, LIGHT = "1F3864", "2E74B5", "DCE6F2"
BODY_FONT, HEAD_FONT = "Arial", "Calibri"
HEADER_TEXT = "DOTB | FUNCTIONAL REQUIREMENTS SPECIFICATION"
META_LINES = [
    ["Dự án", "Project", "Module", "Tính năng", "Feature"],
    ["Mã tài liệu", "Document ID", "Mã ticket", "Mã WBS", "Sprint", "Phiên bản", "Version", "Trạng thái", "Status", "Ngày", "Date"],
    ["Người soạn", "Prepared by", "Người review", "Reviewed by", "Người duyệt", "Approved by"],
]


def _rgb(hexstr: str) -> RGBColor:
    return RGBColor.from_string(hexstr)


def _para_border(p, edge: str, color: str, sz: int = 8, space: int = 4) -> None:
    pPr = p._p.get_or_add_pPr()
    pbdr = pPr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        pPr.append(pbdr)
    el = OxmlElement(f"w:{edge}")
    el.set(qn("w:val"), "single")
    el.set(qn("w:sz"), str(sz))
    el.set(qn("w:space"), str(space))
    el.set(qn("w:color"), color)
    pbdr.append(el)


def _fmt_runs(p, font: str, size: float, color: str | None = None, bold: bool | None = None) -> None:
    for r in p.runs:
        _set_font(r, font, size, bold)
        r.font.italic = False
        if color:
            r.font.color.rgb = _rgb(color)


def _spacing(p, before: float, after: float, line: float = 1.0) -> None:
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = line
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.first_line_indent = Inches(0)


def _table_rules(tbl) -> None:
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        if edge in ("top", "bottom"):
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8")
            el.set(qn("w:color"), BLUE)
        else:
            el.set(qn("w:val"), "nil")
        el.set(qn("w:space"), "0")
        b.append(el)
    tblPr.append(b)


def _cell_bottom(cell, color: str, sz: int = 6) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:tcBorders")):
        tcPr.remove(old)
    tb = OxmlElement("w:tcBorders")
    el = OxmlElement("w:bottom")
    el.set(qn("w:val"), "single")
    el.set(qn("w:sz"), str(sz))
    el.set(qn("w:space"), "0")
    el.set(qn("w:color"), color)
    tb.append(el)
    tcPr.append(tb)


def _clear_shade(cell) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)


def _add_field(run, instr: str) -> None:
    for kind, text in (("begin", None), (None, instr), ("separate", None), (None, "1"), ("end", None)):
        if kind:
            fc = OxmlElement("w:fldChar")
            fc.set(qn("w:fldCharType"), kind)
            run._r.append(fc)
        elif text == instr:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = f" {instr} "
            run._r.append(it)
        else:
            t = OxmlElement("w:t")
            t.text = text
            run._r.append(t)


def _meta_from_table(tbl) -> list[tuple[str, str]]:
    out = []
    for row in tbl.rows[1:]:
        cells = row.cells
        if len(cells) >= 2:
            out.append((cells[0].text.strip(), cells[1].text.strip()))
    return out


def format_frs(path: Path, product: str = "auto") -> dict:
    doc = Document(str(path))
    body = doc.element.body

    # 1. Trang
    for sec in doc.sections:
        sec.page_width, sec.page_height = Inches(8.5), Inches(11)
        sec.left_margin = sec.right_margin = Inches(1.25)
        sec.top_margin, sec.bottom_margin = Inches(1), Inches(0.9)
        sec.header_distance, sec.footer_distance = Inches(0.45), Inches(0.45)

    # 2. Style chung
    for st in doc.styles:
        if st.type == 1:
            if st.name.startswith(("Heading", "Title")):
                _set_font(st, HEAD_FONT, None, True)
                st.font.italic = False
                st.font.color.rgb = _rgb(BLUE)
            else:
                _set_font(st, BODY_FONT, 11)

    # 3. Tiêu đề: đoạn đầu tiên có chữ. Nếu là "Functional Requirements Specification" thì đoạn có chữ tiếp theo là tên
    #    tính năng; nếu không có dòng đó (FRD sinh theo ticket) thì thêm dòng tiêu đề cố định của mẫu phía trên.
    nonempty = [p for p in doc.paragraphs if p.text.strip()]
    if nonempty and nonempty[0].text.strip().lower() == "functional requirements specification":
        t1, t2 = nonempty[0], (nonempty[1] if len(nonempty) > 1 else None)
    else:
        t2 = nonempty[0] if nonempty else None
        t1 = t2.insert_paragraph_before("Functional Requirements Specification") if t2 is not None else None
    h1 = [x for x in (t1, t2) if x is not None]
    title = t2.text.strip() if t2 is not None else path.stem
    if t1 is not None:
        _spacing(t1, 0, 10)
        _fmt_runs(t1, HEAD_FONT, 20, NAVY, True)
        _para_border(t1, "bottom", BLUE, 8, 4)
    if t2 is not None:
        _spacing(t2, 12, 6)
        _fmt_runs(t2, BODY_FONT, 26, BLUE, True)
    title_els = [x._p for x in h1]
    meta: list[tuple[str, str]] = []
    if doc.tables:
        first = doc.tables[0]
        hdr = [c.text.strip() for c in first.rows[0].cells]
        if hdr[:2] in (["Thuộc tính", "Giá trị"], ["Attribute", "Value"], ["Property", "Value"]):
            meta = _meta_from_table(first)
            anchor = first._tbl
            lines: list[list[tuple[str, str]]] = [[], [], []]
            for k, v in meta:
                idx = next((i for i, keys in enumerate(META_LINES) if k in keys), 1)
                lines[idx].append((k, v))
            prev = anchor
            for items in lines:
                if not items:
                    continue
                newp = copy.deepcopy(h1[1]._p) if len(h1) > 1 else OxmlElement("w:p")
                for child in list(newp):
                    if child.tag != qn("w:pPr"):
                        newp.remove(child)
                pPr = newp.find(qn("w:pPr"))
                if pPr is not None:
                    newp.remove(pPr)
                prev.addnext(newp)
                prev = newp
                from docx.text.paragraph import Paragraph
                para = Paragraph(newp, h1[1]._parent if len(h1) > 1 else doc._body)
                para.style = doc.styles["Normal"] if "Normal" in [s.name for s in doc.styles] else para.style
                for i, (k, v) in enumerate(items):
                    r = para.add_run(("     " if i else "") + f"{k}: {v}")
                    _set_font(r, BODY_FONT, 11)
                _spacing(para, 0, 4)
            anchor.getparent().remove(anchor)
    version = next((v for k, v in meta if k in ("Phiên bản", "Version")), "")

    # 4. Duyệt thân bài theo thứ tự để biết bảng thuộc mục nào
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    current_h2 = ""
    n_tables = 0
    for el in list(body.iterchildren()):
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc._body)
            name = p.style.name
            if any(el is x for x in title_els) or name == "Heading 1":
                continue
            if name == "Heading 2":
                current_h2 = p.text.strip()
                _spacing(p, 16, 6)
                _fmt_runs(p, HEAD_FONT, 15, BLUE, True)
            elif name == "Heading 3":
                _spacing(p, 12, 4)
                _fmt_runs(p, HEAD_FONT, 12.5, BLUE, True)
            elif name.startswith("Heading"):
                _spacing(p, 9, 3)
                _fmt_runs(p, HEAD_FONT, 10.5, BLUE, True)
            else:
                if p._p.xpath(".//w:drawing"):
                    _spacing(p, 6, 6)
                    continue
                _spacing(p, 0, 6, 1.05)
                for r in p.runs:
                    _set_font(r, BODY_FONT, 11)
        elif el.tag == qn("w:tbl"):
            tbl = Table(el, doc._body)
            n_tables += 1
            _table_rules(tbl)
            _fit_columns(tbl, int(6.0 * 1440))
            overview = current_h2.startswith("5.")
            for ri, row in enumerate(tbl.rows):
                if ri == 0:
                    _repeat_header(row)
                for ci, cell in enumerate(row.cells):
                    _clear_shade(cell)
                    if ri == 0:
                        _cell_bottom(cell, BLUE, 6)
                    elif overview:
                        _shade(cell, LIGHT)
                    for cp in cell.paragraphs:
                        _spacing(cp, 2, 2, 1.0)
                        for r in cp.runs:
                            if ri == 0:
                                _set_font(r, BODY_FONT, 8.5, False)
                                r.font.color.rgb = _rgb(BLUE)
                            else:
                                _set_font(r, BODY_FONT, 8.5, True if (overview and ci == 0) else None)

    # 5. Đầu trang, chân trang
    proj = next((v for k, v in meta if k in ("Dự án", "Project")), "")
    if product == "auto":
        product = "BBA CRM" if "CRM" in proj else "BBA SMS"
    footer_label = f"{product} · {title}" + (f" · v{version}" if version else "")
    for sec in doc.sections:
        sec.different_first_page_header_footer = False
        hp = sec.header.paragraphs[0] if sec.header.paragraphs else sec.header.add_paragraph()
        for r in list(hp.runs):
            r._r.getparent().remove(r._r)
        rr = hp.add_run(HEADER_TEXT)
        _set_font(rr, BODY_FONT, 11)
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        fp = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
        for r in list(fp.runs):
            r._r.getparent().remove(r._r)
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r1 = fp.add_run(f"{footer_label}  |  Page ")
        _set_font(r1, BODY_FONT, 10)
        r2 = fp.add_run()
        _set_font(r2, BODY_FONT, 12)
        _add_field(r2, "PAGE")

    doc.save(str(path))
    return {"title": title, "version": version, "tables": n_tables, "footer": footer_label}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--product", default="auto")
    a = ap.parse_args(argv)
    st = format_frs(Path(a.docx), a.product)
    print(f"frs_format: {Path(a.docx).name} · {st['tables']} bảng · chân trang \"{st['footer']} | Page N\"")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
