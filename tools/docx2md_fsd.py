"""Dùng khi user sửa FRD trên Drive: python tools/docx2md_fsd.py <file.docx> <md gốc (để map ảnh)> <md ra>.
Chuyển FRD Word (đã sửa trên Drive) về Markdown theo định dạng repo; ảnh map về đường dẫn gốc theo alt text."""
import re, sys, docx
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

src, orig_md, out = sys.argv[1:4]
alt2line = {}
for m in re.finditer(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", open(orig_md, encoding="utf-8").read(), re.M):
    alt2line[m.group(1).replace('"', "”").strip()] = m.group(0)
    alt2line.setdefault(m.group(1).strip(), m.group(0))
d = docx.Document(src)

def numfmt(p):
    pPr = p._p.pPr
    if pPr is None or pPr.numPr is None: return None
    numId = pPr.numPr.numId.val
    ilvl = pPr.numPr.ilvl.val if pPr.numPr.ilvl is not None else 0
    np_ = d.part.numbering_part.element
    num = [n for n in np_.findall(qn("w:num")) if n.get(qn("w:numId")) == str(numId)]
    if not num: return "decimal"
    aid = num[0].find(qn("w:abstractNumId")).get(qn("w:val"))
    ab = [a for a in np_.findall(qn("w:abstractNum")) if a.get(qn("w:abstractNumId")) == aid][0]
    for lvl in ab.findall(qn("w:lvl")):
        if lvl.get(qn("w:ilvl")) == str(ilvl):
            f = lvl.find(qn("w:numFmt"))
            return f.get(qn("w:val")) if f is not None else "decimal"
    return "decimal"

def runs_md(p, br=" "):
    parts = []
    for r in p.runs:
        t = r.text
        if not t: continue
        if r.bold and t.strip():
            lead = t[:len(t) - len(t.lstrip())]; trail = t[len(t.rstrip()):]
            t = f"{lead}**{t.strip()}**{trail}"
        parts.append(t)
    s = "".join(parts).replace("\n", br).replace("\t", " ")
    s = re.sub(r" {2,}", " ", s)
    s = s.replace("****", "")
    return s.strip()

lines = []; prev_list = False; misses = []; last_alt = None; list_n = 0
def emit(block, is_list=False):
    global prev_list, list_n, last_alt
    if not is_list: list_n = 0
    if not block.startswith("!["): last_alt = None
    if lines and not (is_list and prev_list): lines.append("")
    lines.append(block); prev_list = is_list

for ch in d.element.body.iterchildren():
    tag = ch.tag.split("}")[1]
    if tag == "p":
        p = Paragraph(ch, d)
        descr = ch.xpath(".//wp:docPr/@descr")
        if not descr and last_alt is not None and p.text.strip() == last_alt:
            continue
        if descr:
            a = descr[0].strip()
            last_alt = a
            if a.startswith("Trạng thái:") or " — Trạng thái:" in a or a.startswith("Mobile 390px"):
                prev_list = False
                continue
            line = alt2line.get(a) or alt2line.get(a.replace("“", '"').replace("”", '"'))
            if line: emit(line); last_alt = a
            else: misses.append(a)
            continue
        text = runs_md(p)
        if not text: continue
        st = p.style.name
        if st.startswith("Heading "):
            emit("#" * int(st.split()[1]) + " " + p.text.strip()); continue
        f = numfmt(p)
        if f:
            if f == "bullet":
                emit("- " + text, True)
            else:
                n = list_n + 1 if prev_list else 1
                emit(f"{n}. " + text, True); list_n = n
            continue
        if text.startswith(("“", '"')) and text.endswith(("”", '"', '."', '.”')) and len(text) > 80:
            emit("> " + text); continue
        emit(text)
    elif tag == "tbl":
        t = Table(ch, d); rows = []
        for r in t.rows:
            cells = []
            seen = set()
            for c in r.cells:
                if id(c._tc) in seen: continue
                seen.add(id(c._tc))
                paras = [runs_md(pp) for pp in c.paragraphs]
                x = " ".join(x for x in paras if x).replace("|", "\\|")
                x = re.sub(r"(<br>\s*)+$", "", re.sub(r"^(\s*<br>)+", "", x))
                x = re.sub(r"\s*<br>\s*", "<br>", x)
                cells.append(x)
            rows.append("| " + " | ".join(cells) + " |")
        if rows:
            ncol = rows[0].count(" | ") + 1
            rows.insert(1, "|" + "---|" * ncol)
        emit("\n".join(rows))
open(out, "w", encoding="utf-8").write("\n".join(lines).rstrip() + "\n")
print("OK", out, "image misses:", misses)
