#!/usr/bin/env python3
"""Kiểm tra một FSD (khung FRS của dự án, vd. BBA) trước khi xuất Word.

Cách dùng:
    python tools/check_fsd.py <du-an> "FSD/Sprint 4/<file>.md"     # đường dẫn tính từ Document/
    python tools/check_fsd.py <du-an> --all                          # mọi FSD trong Document/FSD/ (bỏ file "_")

ERROR: mã FR / BR / VAL / DATA / AC trùng; mã được nhắc tới nhưng không định nghĩa (vd. dùng VR-001 thay VAL-001);
       còn "{{" ; thiếu mục bắt buộc (User Story, Functional Requirements, Acceptance Criteria) trong một US.
WARN:  BR / VAL / FR không có AC nào ở cột Linked Rule; từ mơ hồ trong AC (tools/ba_lint.py); mã nhảy số.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ba_lint import vague_hits  # noqa: E402
from ba_paths import resolve  # noqa: E402

KINDS = ("FR", "BR", "VAL", "DATA", "AC")
DEF_RE = re.compile(r"^\|\s*\**((?:FR|BR|VAL|DATA|AC)-\d{3})\**\s*\|", re.M)
REQUIRED = ("User Story", "Functional Requirements?", "Acceptance Criteria")


def expand(ref: str) -> list[str]:
    """'BR-001/003/004' -> BR-001, BR-003, BR-004."""
    m = re.match(r"((?:FR|BR|VAL|DATA|AC|VR)-)(\d{3})((?:/\d{3})*)", ref)
    if not m:
        return [ref]
    return [m.group(1) + m.group(2)] + [m.group(1) + n for n in m.group(3).split("/") if n]


def check(path: Path) -> tuple[list[str], list[str], str]:
    text = path.read_text(encoding="utf-8")
    errors, warns = [], []
    if "{{" in text:
        errors.append("còn placeholder {{…}}")
    defs = DEF_RE.findall(text)
    for k, c in Counter(defs).items():
        if c > 1:
            errors.append(f"mã trùng: {k} ({c} lần)")
    defined = set(defs)
    for kind in KINDS:
        nums = sorted(int(d.split("-")[1]) for d in defined if d.startswith(kind + "-"))
        gaps = [n for n in range(1, (nums[-1] if nums else 0) + 1) if n not in nums]
        if gaps:
            warns.append(f"{kind} nhảy số: thiếu {', '.join(f'{kind}-{n:03d}' for n in gaps[:8])}")
    refs = set()
    for m in re.finditer(r"\b((?:FR|BR|VAL|DATA|AC|VR)-\d{3}(?:/\d{3})*)\b", text):
        refs.update(expand(m.group(1)))
    for r in sorted(refs - defined):
        errors.append(f"{r} được nhắc tới nhưng không định nghĩa" + (" (dùng VAL- thay VR-)" if r.startswith("VR-") else ""))
    # AC: cột cuối (Linked Rule) + cả dòng
    ac_rows = re.findall(r"^\|\s*(AC-\d{3})\s*\|(.*)$", text, re.M)
    linked = set()
    for ac, rest in ac_rows:
        for m in re.finditer(r"\b((?:FR|BR|VAL|DATA)-\d{3}(?:/\d{3})*)\b", rest):
            linked.update(expand(m.group(1)))
        hits = vague_hits(rest)
        if hits:
            warns.append(f"{ac}: từ mơ hồ {', '.join(hits)}")
    for d in sorted(defined):
        if d.split("-")[0] in ("BR", "VAL") and d not in linked:
            warns.append(f"{d} chưa có AC nào ở Linked Rule")
    uncovered_fr = sorted(d for d in defined if d.startswith("FR-") and d not in linked)
    if uncovered_fr:
        warns.append(f"FR chưa có AC trực tiếp: {', '.join(uncovered_fr)}")
    # mỗi User Story đủ mục bắt buộc
    parts = re.split(r"^#{2,3} +\d+\.\d+ ", text, flags=re.M)[1:]
    stories = [s for s in parts if re.match(r"[^\n]*\bUS-\d{3}\b", s)]   # chỉ mục User Story, bỏ phụ lục
    for s in stories:
        title = s.splitlines()[0][:60]
        for sec in REQUIRED:
            if not re.search(rf"^#{{3,4}} +{sec}\s*$", s, re.M):
                errors.append(f"US '{title}': thiếu mục {sec.rstrip('?')}")
    summary = (f"{len(stories)} US · " + " · ".join(f"{sum(1 for d in defined if d.startswith(k + '-'))} {k}" for k in KINDS))
    return errors, warns, summary


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    project = resolve(argv[1])
    paths = (sorted(p for p in project.doc_dir("fsd").rglob("*.md") if not p.name.startswith("_") and p.name != "tom-tat-fsd.md")
             if argv[2] == "--all" else [project.doc(argv[2])])
    bad = 0
    for p in paths:
        if not p.exists():
            print(f"ERROR: không có {project.rel(p)}")
            return 1
        errors, warns, summary = check(p)
        for w in warns:
            print(f"WARN: {p.name}: {w}")
        for e in errors:
            print(f"ERROR: {p.name}: {e}")
        print(f"check_fsd: {project.rel(p)} · {summary} · {'PASS' if not errors else f'{len(errors)} lỗi'}, {len(warns)} cảnh báo")
        bad += bool(errors)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
