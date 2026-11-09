#!/usr/bin/env python3
"""Đọc dàn ý một tài liệu có sẵn (URD / FSD / SRS / BRD) trong projects/<du-an>/input/ để nhập vào chuẩn của repo.

Cách dùng:
    python .claude/skills/doc-import/scripts/import_doc.py <du-an> <file-trong-input> [--type urd|fsd|srs|brd] [--depth 3]

Làm gì:
- .docx/.odt/.rtf → Markdown bằng pandoc (kèm ảnh) vào input/_extracted/<ten>-<ext>.md và <ten>-<ext>-media/
  (dùng lại bản đã trích nếu có); .md/.txt đọc thẳng; .pdf dùng bản pdftotext nếu ba-intake đã trích.
- Lập dàn ý: mục (số mục gốc, hoặc số theo thứ tự nếu Word đánh số tự động bị mất), dòng bắt đầu, số dòng;
  mã yêu cầu gốc (REQ-012, FR-1.2, UC01, US-003, BR-05…) và mục chứa nó; số bảng, số ảnh.
- Đoán loại tài liệu (URD / FSD / SRS / BRD) theo từ khoá — `--type` của user luôn thắng.
In: 1 dòng tổng kết + cây mục (≤ --depth) kèm số dòng để Read theo offset. Chi tiết: .tmp/import/<ten>.json
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "tools"))
from ba_paths import Project, resolve  # noqa: E402

PANDOC_EXT = {".docx", ".odt", ".rtf", ".epub"}
TEXT_EXT = {".md", ".txt", ".markdown"}
# Tiền tố mã yêu cầu hay gặp trong tài liệu của khách / nhóm khác
ID_RE = re.compile(
    r"(?<![\w-])((?:REQ|RQ|FR|NFR|BR|UC|US|UR|SR|FS|FN|FUNC|SRS|URD|FSD|SCR|UI|SC|RULE|VAL|MSG|ERR|E|F|R)"
    r"[-_.]?\d{1,4}(?:[.\-]\d{1,3}){0,2})(?![\w])", re.I)
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
NUM_RE = re.compile(r"^((?:\d+\.)*\d+)\.?\s+(.*)$")
TYPE_HINTS = {
    "urd": [r"user stor", r"\blà một\b", r"\btôi muốn\b", r"\bas an? \b", r"\bi want\b", r"user requirement",
            r"yêu cầu người dùng", r"\bURD\b", r"acceptance criteria"],
    "fsd": [r"functional spec", r"đặc tả chức năng", r"\bFSD\b", r"màn hình", r"\bscreen\b", r"\bfield\b",
            r"\btrường\b", r"validation", r"\bbutton\b", r"\bnút\b", r"mockup"],
    "srs": [r"software requirement", r"\bSRS\b", r"non-functional", r"phi chức năng", r"IEEE", r"\bFR-\d"],
    "brd": [r"business requirement", r"\bBRD\b", r"yêu cầu nghiệp vụ", r"\bAS-IS\b", r"\bTO-BE\b", r"stakeholder",
            r"\bROI\b", r"mục tiêu kinh doanh"],
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def to_markdown(project: Project, src: Path) -> tuple[Path | None, str]:
    ext = src.suffix.lower()
    if ext in TEXT_EXT:
        return src, ""
    out = project.input / "_extracted" / f"{src.stem}{ext.replace('.', '-')}.md"
    if ext in PANDOC_EXT:
        media = out.with_name(out.stem + "-media")
        if out.exists() and (media.exists() or not shutil.which("pandoc")):
            return out, ""
        if not shutil.which("pandoc"):
            return None, "không có pandoc để đọc " + src.name
        out.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(["pandoc", str(src), "-t", "gfm", "--wrap=none", f"--extract-media={media}", "-o", str(out)],
                           capture_output=True, text=True, encoding="utf-8")
        return (out, "") if r.returncode == 0 else (None, f"pandoc lỗi: {r.stderr.strip()[:200]}")
    if ext == ".pdf":
        return (out, "") if out.exists() else (None, "PDF chưa có bản trích — Read file PDF theo trang")
    return None, f"không đọc được loại file {ext}"


def outline(text: str) -> dict:
    lines = text.splitlines()
    raw, in_code = [], False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
        m = None if in_code else HEAD_RE.match(line)
        if m:
            raw.append((len(m.group(1)), re.sub(r"[*_`]", "", m.group(2)).strip(), i))
    # Một H1 duy nhất ở đầu = tiêu đề tài liệu → đánh số từ cấp 2 (giống mục lục Word)
    top = 2 if raw and raw[0][0] == 1 and sum(1 for r in raw if r[0] == 1) == 1 else 1
    heads, counters = [], [0] * 8
    for level, title, i in raw:
        nm = NUM_RE.match(title)
        if level < top:
            num = "0"
        else:
            counters[level] += 1
            for k in range(level + 1, 8):
                counters[k] = 0
            num = ".".join(str(counters[k]) for k in range(top, level + 1) if counters[k]) or str(counters[level])
        heads.append({"level": level, "num": nm.group(1) if nm else num, "numbered": bool(nm),
                      "title": nm.group(2) if nm else title, "line": i})
    for k, h in enumerate(heads):
        end = len(lines) + 1
        for h2 in heads[k + 1:]:
            if h2["level"] <= h["level"]:
                end = h2["line"]
                break
        nxt = heads[k + 1]["line"] if k + 1 < len(heads) else len(lines) + 1
        h["end"], h["lines"], h["leaf"] = end, end - h["line"], nxt >= end

    def section_of(line_no: int) -> str:
        cur = ""
        for h in heads:
            if h["line"] <= line_no:
                cur = h["num"]
            else:
                break
        return cur

    found: dict[str, dict] = {}
    for i, line in enumerate(lines, 1):
        for m in ID_RE.finditer(line):
            raw = m.group(1)
            key = raw.upper()
            if key not in found:
                found[key] = {"id": raw, "line": i, "section": section_of(i), "count": 0}
            found[key]["count"] += 1
    prefixes = Counter(re.match(r"[A-Za-z]+", v["id"]).group(0).upper() for v in found.values())
    systems = {p for p, n in prefixes.items() if n >= 3}           # tiền tố xuất hiện ≥ 3 mã khác nhau = hệ mã thật
    ids = [v for v in found.values() if re.match(r"[A-Za-z]+", v["id"]).group(0).upper() in systems]
    ids.sort(key=lambda v: v["line"])
    tables = sum(1 for k, l in enumerate(lines) if re.match(r"^\s*\|?\s*:?-{3,}", l) and k and "|" in lines[k - 1])
    images = len(re.findall(r"!\[[^\]]*\]\(|<img\s", text))
    scores = {t: sum(len(re.findall(p, text, re.I)) for p in pats) for t, pats in TYPE_HINTS.items()}
    return {"lines": len(lines), "headings": heads, "ids": ids, "id_prefixes": sorted(systems), "tables": tables,
            "images": images, "type_scores": scores}


def load(project: Project, name: str) -> tuple[Path | None, Path | None, dict | None, str]:
    src = project.input / name
    if not src.exists():
        cands = [p for p in project.input.iterdir() if p.is_file() and norm(name) in norm(p.name)]
        if len(cands) != 1:
            return None, None, None, f"không thấy '{name}' trong {project.rel(project.input)}/" + (
                f" — gợi ý: {', '.join(p.name for p in cands)}" if cands else "")
        src = cands[0]
    md, err = to_markdown(project, src)
    if not md:
        return src, None, None, err
    return src, md, outline(md.read_text(encoding="utf-8", errors="replace")), ""


def main(argv: list[str]) -> int:
    args, opts, i = [], {}, 1
    while i < len(argv):
        if argv[i].startswith("--"):
            opts[argv[i]] = argv[i + 1] if i + 1 < len(argv) else ""
            i += 2
        else:
            args.append(argv[i])
            i += 1
    if len(args) < 2:
        print(__doc__)
        return 2
    project = resolve(args[0])
    forced = opts.get("--type", "").lower()
    depth = int(opts.get("--depth", 3))
    if forced and forced not in TYPE_HINTS:
        print(f"ERROR: --type phải là {', '.join(TYPE_HINTS)}")
        return 2
    src, md, ol, err = load(project, args[1])
    if not ol:
        print(f"ERROR: {err}")
        return 1
    guess = max(ol["type_scores"], key=ol["type_scores"].get) if any(ol["type_scores"].values()) else "brd"
    ol.update(source=project.rel(src), markdown=project.rel(md), type=forced or guess, type_guess=guess)
    out = project.tmp / "import" / f"{src.stem}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ol, ensure_ascii=False, indent=1), encoding="utf-8")

    for h in ol["headings"]:
        if h["level"] <= depth:
            ids_here = sum(1 for i in ol["ids"] if i["section"] == h["num"] or i["section"].startswith(h["num"] + "."))
            print(f"{'  ' * (h['level'] - 1)}§{h['num']} {h['title'][:70]}  [dòng {h['line']}, {h['lines']} dòng"
                  f"{f', {ids_here} mã' if ids_here else ''}]")
    sc = ", ".join(f"{k} {v}" for k, v in sorted(ol["type_scores"].items(), key=lambda x: -x[1]))
    print(f"import_doc: {src.name} → {project.rel(md)} · {ol['lines']} dòng, {len(ol['headings'])} mục, "
          f"{len(ol['ids'])} mã gốc ({', '.join(ol['id_prefixes']) or 'không có hệ mã — đối chiếu theo mục'}), "
          f"{ol['tables']} bảng, {ol['images']} ảnh · loại: {ol['type'].upper()}"
          f"{' (user chỉ định)' if forced else ''} — điểm {sc} · chi tiết {project.rel(out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
