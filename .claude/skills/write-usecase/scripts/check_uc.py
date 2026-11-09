#!/usr/bin/env python3
"""Kiểm tra projects/<du-an>/Document/Use_Case/UC.md và sinh ma trận truy vết UC ↔ US ↔ FR.

Cách dùng:
    python .claude/skills/write-usecase/scripts/check_uc.py <du-an>
    python .claude/skills/write-usecase/scripts/check_uc.py <du-an> --write-matrix   # ghi mục 5 giữa 2 marker

ERROR: mã UC trùng; thiếu trường bắt buộc; kịch bản chính < 3 bước; US không có trong URD.md;
       include/extend hoặc sơ đồ trỏ UC không tồn tại; nhánh "3a" trỏ bước không có; còn "{{".
WARN:  user story Must (chưa bỏ) chưa thuộc UC nào; kịch bản chính > 9 bước; UC chưa có trên sơ đồ.
FR lấy từ dòng "Truy vết" của FR trong SRS.md (FR nào phục vụ US của UC) — chưa có SRS thì cột FR ghi "—".
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / ".claude" / "skills" / "write-srs" / "scripts"))
from build_srs import fr_blocks  # noqa: E402
sys.path.insert(0, str(REPO / "tools"))
from ba_paths import resolve  # noqa: E402

UC_HEAD_RE = re.compile(r"^#### +(UC-\d+)\s*[—–-]\s*(.*)$", re.M)
FIELD_RE = re.compile(r"^- \*\*([^*:]+):\*\*\s*(.*)$", re.M)
REQUIRED = ["Tác nhân chính", "Mức", "Kích hoạt", "Tiền điều kiện", "Đảm bảo khi thành công", "Truy vết", "Độ ưu tiên"]
START, END = "<!-- uc-matrix:start -->", "<!-- uc-matrix:end -->"


def parse_ucs(text: str) -> list[dict]:
    heads = list(UC_HEAD_RE.finditer(text))
    ucs = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        nxt = re.search(r"^#{2,3} ", text[m.end():end], re.M)
        body = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():end]
        fields = {k.strip(): v.strip() for k, v in FIELD_RE.findall(body)}
        main = re.search(r"\*\*Kịch bản chính:\*\*(.*?)(?=^- \*\*|\Z)", body, re.S | re.M)
        steps = [int(n) for n in re.findall(r"^\s+(\d+)\.\s+\S", main.group(1), re.M)] if main else []
        exts = re.findall(r"\*\*\\?(\*|\d+)([a-z])\.", body)
        ucs.append({"id": m.group(1), "title": m.group(2).strip(), "fields": fields, "steps": steps,
                    "exts": exts, "dropped": "Đã bỏ" in m.group(2)})
    return ucs


def urd_stories(urd: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    if not urd.exists():
        return out
    t = urd.read_text(encoding="utf-8")
    heads = list(re.finditer(r"^#{3,4} +(US-\d+)\s*[—–-]?\s*(.*)$", t, re.M))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        pr = re.search(r"\*\*Ưu tiên:\*\*\s*(\w+)", t[m.end():end])
        out[m.group(1)] = {"title": m.group(2).strip(), "priority": pr.group(1) if pr else "",
                           "dropped": "Đã bỏ" in m.group(2)}
    return out


def matrix(ucs: list[dict], stories: dict, srs: Path) -> tuple[str, list[str]]:
    frs = fr_blocks(srs.read_text(encoding="utf-8")) if srs.exists() else []
    rows = [START, "> Sinh tự động bởi `check_uc.py --write-matrix` — không sửa tay.", "",
            "| UC | Tên | Tác nhân chính | User story | FR (từ SRS) |", "|---|---|---|---|---|"]
    covered: set[str] = set()
    for u in ucs:
        us = re.findall(r"US-\d+", u["fields"].get("Truy vết", ""))
        covered |= set(us) if not u["dropped"] else set()
        fr = sorted({f["id"] for f in frs if set(f["us"]) & set(us)}, key=lambda x: int(x[3:]))
        rows.append(f"| {u['id']} | {u['title'].replace('|', '/')} | {u['fields'].get('Tác nhân chính', '—')} "
                    f"| {', '.join(us) or '—'} | {', '.join(fr) if frs else '—'} |")
    missing = [s for s, v in stories.items() if not v["dropped"] and s not in covered]
    rows += ["", f"User story chưa thuộc use case nào: {', '.join(missing) if missing else 'không có'}.", END]
    return "\n".join(rows), missing


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    project = resolve(args[0])
    uc_path = project.doc("UC.md")
    if not uc_path.exists():
        print(f"ERROR: không có {uc_path.relative_to(REPO)}")
        return 1
    text = uc_path.read_text(encoding="utf-8")
    stories = urd_stories(project.doc("URD.md"))
    ucs = parse_ucs(text)
    errors: list[str] = []
    warns: list[str] = []
    ids = {u["id"] for u in ucs}

    for k, c in Counter(u["id"] for u in ucs).items():
        if c > 1:
            errors.append(f"mã trùng: {k} xuất hiện {c} lần")
    if not ucs:
        errors.append("không có use case nào (heading phải dạng '#### UC-01 — Tên')")
    if "{{" in text:
        errors.append("còn placeholder '{{'")
    if not stories:
        warns.append("không đọc được user story trong URD.md — bỏ qua kiểm tra truy vết US")

    for u in ucs:
        if u["dropped"]:
            continue
        for f in REQUIRED:
            if not u["fields"].get(f):
                errors.append(f"{u['id']}: thiếu trường '{f}'")
        if len(u["steps"]) < 3:
            errors.append(f"{u['id']}: kịch bản chính cần ít nhất 3 bước đánh số (có {len(u['steps'])})")
        elif len(u["steps"]) > 9:
            warns.append(f"{u['id']}: kịch bản chính {len(u['steps'])} bước (> 9) — cân nhắc tách UC hoặc include")
        for num, letter in u["exts"]:
            if num != "*" and int(num) not in u["steps"]:
                errors.append(f"{u['id']}: nhánh {num}{letter} trỏ bước {num} không có trong kịch bản chính")
        for ref in re.findall(r"UC-\d+", u["fields"].get("Quan hệ", "")):
            if ref not in ids:
                errors.append(f"{u['id']}: quan hệ trỏ {ref} không tồn tại")
        us = re.findall(r"US-\d+", u["fields"].get("Truy vết", ""))
        if not us:
            errors.append(f"{u['id']}: dòng Truy vết không có US-xx")
        for s in us:
            if stories and s not in stories:
                errors.append(f"{u['id']}: {s} không có trong URD.md")

    diagrams = "\n".join(re.findall(r"```mermaid\n(.*?)```", text, re.S))
    for ref in sorted(set(re.findall(r"UC-\d+", diagrams))):
        if ref not in ids:
            errors.append(f"sơ đồ use case có {ref} không tồn tại")
    for u in ucs:
        if not u["dropped"] and diagrams and u["id"] not in diagrams:
            warns.append(f"{u['id']}: chưa có trên sơ đồ use case")

    block, missing = matrix(ucs, stories, project.doc("SRS.md"))
    for s in missing:
        if stories[s]["priority"].lower().startswith("must"):
            warns.append(f"{s} (Must) chưa thuộc use case nào")

    if "--write-matrix" in argv:
        if START in text and END in text:
            text = text[: text.index(START)] + block + text[text.index(END) + len(END):]
            uc_path.write_text(text, encoding="utf-8")
        else:
            errors.append(f"không thấy marker {START} … {END} ở mục 5 để ghi ma trận")

    for w in warns:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    active = [u for u in ucs if not u["dropped"]]
    print(f"check_uc: {len(active)} use case ({len(ucs) - len(active)} đã bỏ), "
          f"{len({s for u in active for s in re.findall(r'US-[0-9]+', u['fields'].get('Truy vết', ''))})} US được phủ / "
          f"{len([s for s in stories.values() if not s['dropped']])} US trong URD · "
          f"{'PASS' if not errors else 'FAIL'}, {len(warns)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
