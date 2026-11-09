#!/usr/bin/env python3
"""Kiểm tra projects/<du-an>/docs/test-cases.md, sinh ma trận phủ (RTM) và xuất exports/test-cases.csv.

Cách dùng:
    python .claude/skills/write-testcase/scripts/check_tc.py <du-an>
    python .claude/skills/write-testcase/scripts/check_tc.py <du-an> --write-matrix   # ghi mục 6 giữa 2 marker

ERROR: mã TC trùng / sai dạng TC-001; còn placeholder; FR/NFR trong heading không có trong SRS;
       cột AC trỏ ACn không có trong FR, hoặc BR không có trong FR; thiếu Bước / Kết quả mong đợi; Loại sai.
WARN:  FR (chưa bỏ) chưa có test case; AC chưa được phủ; FR Must chưa có TC Ngoại lệ; NFR chưa có TC;
       từ mơ hồ trong Kết quả mong đợi; TC của FR đã bỏ chưa ghi [Đã bỏ].
CSV (UTF-8 BOM, mở bằng Excel / Google Sheet): Test ID, Yêu cầu, AC, Loại, Tiêu đề, Tiền điều kiện, Bước,
     Kết quả mong đợi, Ưu tiên, User story, Màn hình, Trạng thái, Kết quả thực tế, Người test, Ngày test.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / ".claude" / "skills" / "write-srs" / "scripts"))
sys.path.insert(0, str(REPO / "tools"))
from ba_lint import fr_sections, vague_hits  # noqa: E402
from ba_paths import resolve  # noqa: E402
from build_srs import build, fr_blocks, needs_build  # noqa: E402

TYPES = {"Chức năng", "Ngoại lệ", "Biên", "Phân quyền", "Trạng thái", "Tích hợp", "Phi chức năng"}
COLS = ["TC", "AC", "Loại", "Tiêu đề", "Tiền điều kiện", "Bước", "Kết quả mong đợi", "Ưu tiên"]
START, END = "<!-- tc-matrix:start -->", "<!-- tc-matrix:end -->"
PLACEHOLDER_RE = re.compile(r"\{\{|\}\}|TC-0?xx|\bTODO\b|\bTBD\b")


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_tc(text: str) -> list[dict]:
    """Mỗi dòng bảng có mã TC-xxx; 'group' = heading ### gần nhất (FR-xx / NFR-xx / tên mục)."""
    rows, group, header = [], "", COLS
    body = text.split(START)[0] + (text.split(END, 1)[1] if END in text else "")
    for n, line in enumerate(body.splitlines(), 1):
        h = re.match(r"^#{2,3} +(.*)$", line)
        if h:
            m = re.match(r"((?:N?FR)-\d+)\b", h.group(1))
            group = m.group(1) if m else h.group(1).strip()
            continue
        if not line.lstrip().startswith("|"):
            continue
        c = cells(line)
        if c and c[0] == "TC":
            header = c
            continue
        if not c or not re.match(r"TC-", c[0]):
            continue
        row = dict(zip(header, c + [""] * (len(header) - len(c))))
        row.update(group=group, line=n, raw=line)
        rows.append(row)
    return rows


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    project = resolve(args[0])
    if needs_build(project):
        build(project, quiet=True)
    tc_path, srs_path = project.doc("test-cases.md"), project.doc("SRS.md")
    if not tc_path.exists():
        print(f"ERROR: chưa có {project.rel(tc_path)} — chạy skill write-testcase")
        return 1
    if not srs_path.exists():
        print(f"ERROR: chưa có {project.rel(srs_path)} — test case viết từ SRS")
        return 1
    srs = srs_path.read_text(encoding="utf-8")
    frs = {f["id"]: f for f in fr_sections(srs)}
    trace = {f["id"]: f for f in fr_blocks(srs)}
    nfrs = dict(re.findall(r"^#{3,4} +(NFR-\d+)\s*[—–-]?\s*(.*)$", srs, re.M))
    text = tc_path.read_text(encoding="utf-8")
    rows = parse_tc(text)
    errors: list[str] = []
    warns: list[str] = []

    for m in PLACEHOLDER_RE.finditer(text.split(START)[0]):
        line = text[: m.start()].count("\n") + 1
        errors.append(f"placeholder còn sót (dòng {line}): {text.splitlines()[line - 1].strip()[:80]}")
    for k, c in Counter(r["TC"] for r in rows).items():
        if c > 1:
            errors.append(f"mã trùng: {k} xuất hiện {c} lần")
    covered: dict[str, set[int]] = {}
    by_group: dict[str, list[dict]] = {}
    for r in rows:
        tid, g = r["TC"], r["group"]
        by_group.setdefault(g, []).append(r)
        if not re.fullmatch(r"TC-\d{3,}", tid):
            if not PLACEHOLDER_RE.search(tid):
                errors.append(f"{tid}: mã phải dạng TC-001")
            continue
        if r.get("Loại", "") not in TYPES:
            errors.append(f"{tid}: Loại '{r.get('Loại', '')}' không thuộc {', '.join(sorted(TYPES))}")
        for col in ("Bước", "Kết quả mong đợi"):
            if not r.get(col, "").strip(" —-"):
                errors.append(f"{tid}: thiếu {col}")
        hits = vague_hits(r.get("Kết quả mong đợi", ""))
        if hits:
            warns.append(f"{tid}: kết quả mong đợi có từ mơ hồ {', '.join(hits)}")
        if g.startswith("FR-"):
            f = frs.get(g)
            if not f:
                errors.append(f"{tid}: {g} không có trong SRS")
                continue
            for n in map(int, re.findall(r"\bAC(\d+)\b", r.get("AC", ""))):
                if not 1 <= n <= len(f["ac"]):
                    errors.append(f"{tid}: {g} không có AC{n} (chỉ có {len(f['ac'])} AC)")
                else:
                    covered.setdefault(g, set()).add(n)
            for br in re.findall(r"BR-\d+\.\d+", r.get("AC", "")):
                if not re.search(re.escape(br) + r"(?![\d.])", f["body"]):
                    errors.append(f"{tid}: {br} không có trong {g}")
            if f["dropped"] and "Đã bỏ" not in r["raw"]:
                warns.append(f"{tid}: {g} đã bỏ — ghi [Đã bỏ] trong Tiêu đề")
        elif g.startswith("NFR-") and g not in nfrs:
            errors.append(f"{tid}: {g} không có trong SRS")

    gaps: dict[str, list[int]] = {}
    for fid, f in frs.items():
        if f["dropped"]:
            continue
        mine = [r for r in by_group.get(fid, []) if "Đã bỏ" not in r["raw"]]
        if not mine:
            gaps[fid] = list(range(1, len(f["ac"]) + 1))
            warns.append(f"{fid} ({f['priority'] or '—'}): chưa có test case")
            continue
        miss = [n for n in range(1, len(f["ac"]) + 1) if n not in covered.get(fid, set())]
        if miss:
            gaps[fid] = miss
            warns.append(f"{fid}: AC chưa có test case: {', '.join(f'AC{n}' for n in miss)}")
        if f["priority"].lower() == "must" and not any(r.get("Loại") == "Ngoại lệ" for r in mine):
            warns.append(f"{fid} (Must): chưa có test case Ngoại lệ")
    for nid in nfrs:
        if nid not in by_group:
            warns.append(f"{nid}: chưa có test case")

    active = [f for f in frs.values() if not f["dropped"]]
    n_ac = sum(len(f["ac"]) for f in active)
    n_cov = sum(len(covered.get(f["id"], set())) for f in active)

    if "--write-matrix" in argv and not errors:
        lines = [START, f"> Sinh tự động bởi `check_tc.py --write-matrix` — phủ {n_cov}/{n_ac} AC của {len(active)} FR.", "",
                 "| FR | Ưu tiên | User story | Màn hình | AC | AC đã phủ | Test case | AC còn thiếu |",
                 "|---|---|---|---|---|---|---|---|"]
        for f in active:
            t = trace.get(f["id"], {})
            tcs = [r["TC"] for r in by_group.get(f["id"], []) if "Đã bỏ" not in r["raw"]]
            lines.append(f"| {f['id']} | {f['priority'] or '—'} | {', '.join(t.get('us', [])) or '—'} | "
                         f"{', '.join(t.get('scr', [])) or 'Không có UI'} | {len(f['ac'])} | "
                         f"{len(covered.get(f['id'], set()))} | {', '.join(tcs) or '—'} | "
                         f"{', '.join(f'AC{n}' for n in gaps.get(f['id'], [])) or '—'} |")
        others = [(g, rs) for g, rs in by_group.items() if not g.startswith("FR-")]
        if others:
            lines += ["", "| Nhóm | Test case |", "|---|---|"]
            lines += [f"| {g} | {', '.join(r['TC'] for r in rs)} |" for g, rs in others]
        lines.append(END)
        if START in text and END in text:
            text = text.split(START)[0] + "\n".join(lines) + text.split(END, 1)[1]
            tc_path.write_text(text, encoding="utf-8")
        else:
            warns.append(f"không thấy marker {START} … {END} — bỏ qua ghi ma trận")

    out = project.export("test-cases.csv")
    if not errors:
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["Test ID", "Yêu cầu", "AC", "Loại", "Tiêu đề", "Tiền điều kiện", "Bước", "Kết quả mong đợi",
                        "Ưu tiên", "User story", "Màn hình", "Trạng thái", "Kết quả thực tế", "Người test", "Ngày test"])
            for r in rows:
                if "Đã bỏ" in r["raw"]:
                    continue
                t = trace.get(r["group"], {})
                br = lambda s: re.sub(r"\s*<br\s*/?>\s*", "\n", s)  # noqa: E731
                w.writerow([r["TC"], r["group"], r.get("AC", ""), r.get("Loại", ""), r.get("Tiêu đề", ""),
                            br(r.get("Tiền điều kiện", "")), br(r.get("Bước", "")), br(r.get("Kết quả mong đợi", "")),
                            r.get("Ưu tiên", ""), ", ".join(t.get("us", [])), ", ".join(t.get("scr", [])),
                            "Chưa chạy", "", "", ""])

    for w_ in warns:
        print(f"WARN: {w_}")
    for e in errors:
        print(f"ERROR: {e}")
    kinds = Counter(r.get("Loại", "") for r in rows)
    print(f"check_tc: {len(rows)} test case ({', '.join(f'{k} {v}' for k, v in kinds.most_common())}) · "
          f"phủ {n_cov}/{n_ac} AC, {sum(1 for f in active if f['id'] in by_group)}/{len(active)} FR · "
          f"{project.rel(out) if not errors else 'chưa xuất CSV'} · "
          f"{'PASS' if not errors else f'{len(errors)} lỗi'}, {len(warns)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
