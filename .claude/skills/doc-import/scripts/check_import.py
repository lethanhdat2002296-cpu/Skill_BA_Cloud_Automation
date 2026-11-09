#!/usr/bin/env python3
"""Kiểm tra bảng đối chiếu projects/<du-an>/Document/doi-chieu-ma.md sau khi nhập tài liệu có sẵn — không sót yêu cầu nào.

Cách dùng:
    python .claude/skills/doc-import/scripts/check_import.py <du-an>

doi-chieu-ma.md: mỗi tài liệu gốc một mục "## <tên file trong input/> — <loại> …" + bảng
    | Mã gốc | Mục gốc | Nội dung (tóm tắt) | Mã mới | Xử lý |
ERROR: mã gốc có trong tài liệu nhưng không có dòng; "Mã mới" trỏ mã không tồn tại trong URD/UC/SRS/backlog;
       file gốc không có trong input/; còn "{{".
WARN:  dòng "Mã mới" = "—" mà cột Xử lý không ghi Bỏ / Gộp / Ngoài phạm vi / OQ;
       mục lá (không chứa mã gốc) chưa được nhắc trong cột "Mục gốc" (đối chiếu theo số § hoặc tên mục).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ba_paths import resolve  # noqa: E402
from import_doc import load, norm  # noqa: E402

NEW_ID_RE = re.compile(r"\b(?:US-\d+(?:\.\d+)?|UC-\d+|FR-\d+|NFR-\d+|SCR-\d+|BR-\d+\.\d+|EP-\d+|AS-\d+|OQ-\d+)\b")
DROP_RE = re.compile(r"bỏ|gộp|ngoài phạm vi|OQ-\d+|trùng", re.I)


def defined_ids(project) -> set[str]:
    out: set[str] = set()
    for name in ("URD.md", "UC.md", "SRS.md", "backlog.md"):
        p = project.doc(name)
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        out |= set(re.findall(r"^#{2,4} +((?:US|UC|FR|NFR|EP|SCR)-\d+(?:\.\d+)?)\b", t, re.M))
        out |= set(re.findall(r"^\|\s*((?:SCR|AS|OQ|EP)-\d+)\s*\|", t, re.M))
        out |= set(re.findall(r"\b(BR-\d+\.\d+)\b", t))
    srs_dir = project.srs_dir
    if srs_dir.is_dir():
        for p in srs_dir.glob("*.md"):
            t = p.read_text(encoding="utf-8")
            out |= set(re.findall(r"^#{3,4} +((?:FR|NFR|SCR)-\d+)\b", t, re.M))
            out |= set(re.findall(r"^\|\s*((?:SCR|AS|OQ)-\d+)\s*\|", t, re.M))
            out |= set(re.findall(r"\b(BR-\d+\.\d+)\b", t))
    return out


def parse_map(text: str) -> list[dict]:
    """[{file, line, rows:[{goc, muc, moi, xu_ly, line}]}]"""
    blocks, cur, header = [], None, []
    for n, line in enumerate(text.splitlines(), 1):
        h = re.match(r"^## +(.+?)(?:\s+[—–-]\s+.*)?$", line)
        if h:
            cur = {"file": h.group(1).strip().strip("`"), "line": n, "rows": []}
            blocks.append(cur)
            header = []
            continue
        if not cur or not line.lstrip().startswith("|") or re.fullmatch(r"\s*\|[\s:|-]+\|?\s*", line):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if any("mã gốc" in x.lower() for x in c):
            header = [x.lower() for x in c]
            continue
        if not header:
            continue
        col = lambda key: next((c[i] for i, x in enumerate(header) if key in x and i < len(c)), "")  # noqa: E731
        cur["rows"].append({"goc": col("mã gốc"), "muc": col("mục gốc"), "moi": col("mã mới"),
                            "xu_ly": col("xử lý"), "line": n})
    return blocks


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    project = resolve(args[0])
    path = project.doc("doi-chieu-ma.md")
    if not path.exists():
        print(f"ERROR: chưa có {project.rel(path)} — tạo theo .claude/skills/doc-import/template-doi-chieu.md")
        return 1
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warns: list[str] = []
    if "{{" in text:
        errors.append("còn placeholder {{…}} trong doi-chieu-ma.md")
    known = defined_ids(project)
    total_ids = total_rows = 0
    blocks = parse_map(text)
    if not blocks:
        errors.append("không có mục '## <tên file gốc>' nào")
    for b in blocks:
        src, _md, ol, err = load(project, b["file"])
        if not ol:
            errors.append(f"{b['file']}: {err or 'không đọc được'}")
            continue
        rows = b["rows"]
        total_rows += len(rows)
        mapped = {m.upper() for r in rows for m in re.findall(r"[A-Za-z]+[-_.]?\d[\w.\-]*", r["goc"])}
        for i in ol["ids"]:
            total_ids += 1
            if i["id"].upper() not in mapped:
                errors.append(f"{src.name}: mã gốc {i['id']} (§{i['section']}, dòng {i['line']}) chưa có dòng đối chiếu")
        for r in rows:
            news = NEW_ID_RE.findall(r["moi"])
            for nid in news:
                if nid not in known:
                    errors.append(f"dòng {r['line']}: mã mới {nid} không có trong URD/UC/SRS/backlog")
            if not news and not DROP_RE.search(r["xu_ly"] + " " + r["moi"]):
                warns.append(f"dòng {r['line']}: '{r['goc'] or r['muc']}' không có mã mới — ghi Xử lý: Bỏ (lý do) / Gộp vào … / OQ-xx")
        muc_text = norm(" ".join(r["muc"] for r in rows))
        nums = set(re.findall(r"§\s*([\d.]+\d)", " ".join(r["muc"] for r in rows)))
        with_ids = {i["section"] for i in ol["ids"]}
        for h in ol["headings"]:
            if not h["leaf"] or h["lines"] < 3 or any(s == h["num"] or s.startswith(h["num"] + ".") for s in with_ids):
                continue
            if h["num"] not in nums and norm(h["title"]) not in muc_text:
                warns.append(f"{src.name}: mục §{h['num']} '{h['title'][:50]}' (dòng {h['line']}) chưa đối chiếu")

    for w in warns:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"check_import: {len(blocks)} tài liệu gốc, {total_rows} dòng đối chiếu, {total_ids} mã gốc · "
          f"{'PASS' if not errors else f'{len(errors)} lỗi'}, {len(warns)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
