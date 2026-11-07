#!/usr/bin/env python3
"""Kiểm tra outputs/<du-an>/backlog.md và xuất backlog.csv (import Jira Cloud / Google Sheet).

Cách dùng:
    python .claude/skills/write-user-story/scripts/backlog_csv.py <du-an>

ERROR: mã trùng; US không có trong URD.md; story nằm ngoài epic hoặc epic không có trong bảng mục 2;
       story chưa tách thiếu AC / story point; story point không thuộc 1,2,3,5,8,13; story con thiếu "Tách từ".
WARN:  US (chưa bỏ) của URD chưa có trong backlog; story 13 điểm; FR/SCR trích dẫn không có trong SRS.md.
CSV (UTF-8 BOM): Issue Id, Parent, Issue Type, Summary, Description, Priority, Story Points, Labels, Release.
Epic đứng trước story; Parent của story = Issue Id của epic. Story gốc đã tách và story đã bỏ không xuất.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / ".claude" / "skills" / "write-usecase" / "scripts"))
sys.path.insert(0, str(REPO / ".claude" / "skills" / "write-srs" / "scripts"))
from build_srs import fr_blocks  # noqa: E402
from check_uc import urd_stories  # noqa: E402

FIB = {1, 2, 3, 5, 8, 13}
PRIORITY = {"must": "Highest", "should": "High", "could": "Medium", "won't": "Low", "wont": "Low"}
EPIC_RE = re.compile(r"^### +(EP-\d+)\s*[—–-]\s*(.*)$", re.M)
STORY_RE = re.compile(r"^#### +(US-\d+(?:\.\d+)?)\s*[—–-]\s*(.*)$", re.M)


def field(body: str, name: str) -> str:
    m = re.search(rf"\*\*{re.escape(name)}:\*\*\s*([^·\n]*)", body)
    return m.group(1).strip() if m else ""


def plain(s: str) -> str:
    return re.sub(r"\*\*|`", "", s).strip()


def parse(text: str) -> tuple[dict, list[dict]]:
    epics_table = {}
    for row in re.findall(r"^\|\s*(EP-\d+)\s*\|([^\n]*)$", text, re.M):
        cells = [c.strip() for c in row[1].strip().strip("|").split("|")]
        epics_table[row[0]] = {"name": cells[0] if cells else "", "goal": cells[1] if len(cells) > 1 else "",
                               "release": cells[3] if len(cells) > 3 else ""}
    stories = []
    sec4 = re.search(r"^## +4\.", text, re.M)
    limit = sec4.start() if sec4 else len(text)
    epic_heads = [(m.start(), m.group(1)) for m in EPIC_RE.finditer(text)]
    heads = [m for m in STORY_RE.finditer(text) if m.start() < limit]
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else limit
        nxt = re.search(r"^#{2,3} ", text[m.end():end], re.M)
        body = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():end]
        epic = ""
        for pos, eid in epic_heads:
            if pos < m.start():
                epic = eid
        ac = re.search(r"\*\*Acceptance criteria:\*\*(.*)", body, re.S)
        ac_items = re.findall(r"^\s+\d+\.\s+(.+)$", ac.group(1), re.M) if ac else []
        sp = field(body, "Story point")
        stories.append({
            "id": m.group(1), "title": m.group(2).strip(), "epic": epic, "epic_field": field(body, "Epic"),
            "story": field(body, "Story"), "priority": field(body, "Ưu tiên"), "points": sp,
            "release": field(body, "Release"), "trace": field(body, "Truy vết"), "split_from": field(body, "Tách từ"),
            "split_into": field(body, "Đã tách thành"), "ac": ac_items, "dropped": "Đã bỏ" in m.group(2),
        })
    return epics_table, stories


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    du_an = args[0].strip("/\\")
    project = REPO / "outputs" / du_an
    path = project / "backlog.md"
    if not path.exists():
        print(f"ERROR: không có {path.relative_to(REPO)}")
        return 1
    text = path.read_text(encoding="utf-8")
    epics, stories = parse(text)
    urd = urd_stories(project / "URD.md")
    srs = project / "SRS.md"
    srs_text = srs.read_text(encoding="utf-8") if srs.exists() else ""
    fr_ids = {f["id"] for f in fr_blocks(srs_text)}
    scr_ids = set(re.findall(r"^\|\s*(SCR-\d+)\s*\|", srs_text, re.M))
    errors: list[str] = []
    warns: list[str] = []

    if "{{" in text:
        errors.append("còn placeholder '{{'")
    for k, c in Counter(s["id"] for s in stories).items():
        if c > 1:
            errors.append(f"mã trùng: {k} xuất hiện {c} lần")
    ids = {s["id"] for s in stories}
    for s in stories:
        base = s["id"].split(".")[0]
        if urd and base not in urd:
            errors.append(f"{s['id']}: {base} không có trong URD.md")
        if s["dropped"]:
            continue
        if not s["epic"] or s["epic"] not in epics:
            errors.append(f"{s['id']}: không nằm dưới epic nào có trong bảng mục 2")
        if "." in s["id"] and not s["split_from"]:
            errors.append(f"{s['id']}: story con thiếu dòng 'Tách từ'")
        if s["split_into"]:
            for child in re.findall(r"US-\d+\.\d+", s["split_into"]):
                if child not in ids:
                    errors.append(f"{s['id']}: 'Đã tách thành' trỏ {child} không có")
            continue
        if not s["ac"]:
            errors.append(f"{s['id']}: thiếu Acceptance criteria")
        if not s["points"].isdigit() or int(s["points"]) not in FIB:
            errors.append(f"{s['id']}: story point '{s['points']}' không thuộc 1, 2, 3, 5, 8, 13")
        elif int(s["points"]) == 13:
            warns.append(f"{s['id']}: 13 điểm — tách trước khi đưa vào sprint")
        if srs_text:
            for ref in re.findall(r"FR-\d+", s["trace"]):
                if ref not in fr_ids:
                    warns.append(f"{s['id']}: {ref} không có trong SRS.md")
            for ref in re.findall(r"SCR-\d+", s["trace"]):
                if ref not in scr_ids:
                    warns.append(f"{s['id']}: {ref} không có trong SRS.md")
    covered = {s["id"].split(".")[0] for s in stories}
    for us, v in urd.items():
        if not v["dropped"] and us not in covered:
            warns.append(f"{us} ({v['priority'] or '—'}) có trong URD nhưng chưa có trong backlog")

    # CSV
    rows = []
    epic_issue = {}
    for n, (eid, e) in enumerate(sorted(epics.items(), key=lambda x: int(x[0][3:])), 1):
        epic_issue[eid] = n
        rows.append([n, "", "Epic", f"{eid} — {plain(e['name'])}", plain(e["goal"]), "", "", eid, plain(e["release"])])
    total = defaultdict(int)
    n = len(rows)
    for s in stories:
        if s["dropped"] or s["split_into"] or not s["points"].isdigit():
            continue
        n += 1
        total[(s["release"], s["epic"])] += int(s["points"])
        desc = plain(s["story"]) + "\n\nAcceptance criteria:\n" + "\n".join(
            f"{i}. {plain(a)}" for i, a in enumerate(s["ac"], 1)) + (f"\n\nTruy vết: {plain(s['trace'])}" if s["trace"] else "")
        rows.append([n, epic_issue.get(s["epic"], ""), "Story", f"{s['id']} — {plain(s['title'])}", desc,
                     PRIORITY.get(s["priority"].lower().split()[0] if s["priority"] else "", "Medium"),
                     s["points"], s["id"], plain(s["release"])])
    out = project / "backlog.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Issue Id", "Parent", "Issue Type", "Summary", "Description", "Priority", "Story Points", "Labels", "Release"])
        w.writerows(rows)

    for wmsg in warns:
        print(f"WARN: {wmsg}")
    for e in errors:
        print(f"ERROR: {e}")
    by_rel = defaultdict(int)
    for (rel, _), pts in total.items():
        by_rel[rel] += pts
    rel_txt = ", ".join(f"{r or '—'}: {p} điểm" for r, p in sorted(by_rel.items()))
    print(f"backlog_csv: {len(epics)} epic, {sum(1 for r in rows if r[2] == 'Story')} story xuất CSV · {rel_txt} · "
          f"{out.relative_to(REPO)} · {'PASS' if not errors else 'FAIL'}, {len(warns)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
