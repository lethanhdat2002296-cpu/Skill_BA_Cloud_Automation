#!/usr/bin/env python3
"""Chuyển SRS.md một file (dự án cũ) sang cấu trúc tách phân hệ outputs/<du-an>/srs/*.md. Chạy MỘT lần / dự án.

Cách dùng:
    python .claude/skills/write-srs/scripts/split_srs.py <du-an>
    python .claude/skills/write-srs/scripts/split_srs.py <du-an> --modules "Yêu cầu mua hàng=FR-01..FR-06; Báo giá=FR-07..FR-10,FR-15"
    python .claude/skills/write-srs/scripts/split_srs.py <du-an> --keep-trace     # giữ mục 8 viết tay
    python .claude/skills/write-srs/scripts/split_srs.py <du-an> --force          # ghi đè srs/ đã có

--modules: gom FR thành phân hệ (mỗi phân hệ một file 03-NN-<slug>.md). Không truyền:
    - mục 3 đã có heading phân hệ (### 3.1 ...) -> tách theo heading đó;
    - không có -> tất cả FR vào một file 03-01-chuc-nang.md.
FR không thuộc phân hệ nào -> phân hệ "Chức năng khác".
Mục 8 viết tay bị bỏ (build_srs.py tự sinh), có so sánh và cảnh báo nếu khác.
Cuối cùng chạy build_srs.py để sinh lại SRS.md.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_srs import GENERATED_NOTE, build, fr_blocks  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
NAMES = {1: "gioi-thieu", 2: "tong-quan", 4: "phi-chuc-nang", 5: "tich-hop", 6: "man-hinh",
         7: "user-flow", 8: "truy-vet", 9: "gia-dinh-cau-hoi"}


def slugify(text: str) -> str:
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower() or "phan-he"


def parse_modules(spec: str) -> list[tuple[str, set[str]]]:
    mods = []
    for chunk in filter(None, (c.strip() for c in spec.split(";"))):
        name, _, ids = chunk.partition("=")
        frs: set[str] = set()
        for part in filter(None, (p.strip() for p in ids.split(","))):
            m = re.fullmatch(r"FR-(\d+)\s*\.\.\s*FR-(\d+)", part)
            if m:
                a, b = int(m.group(1)), int(m.group(2))
                frs |= {f"FR-{i:02d}" for i in range(a, b + 1)}
            elif re.fullmatch(r"FR-\d+", part):
                frs.add(part)
        mods.append((name.strip(), frs))
    return mods


def split_fr_section(sec3: str) -> tuple[str, list[tuple[str, str]]]:
    """-> (phần mở đầu mục 3, [(id FR, khối FR với heading ####)])."""
    heads = list(re.finditer(r"^#{3,4} +(FR-\d+)\b.*$", sec3, re.M))
    if not heads:
        return sec3, []
    intro = re.sub(r"^### +(?!FR-).*$\n?", "", sec3[: heads[0].start()], flags=re.M)
    blocks = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(sec3)
        block = sec3[m.start():end]
        block = re.sub(r"^#{3,4} +(?=FR-)", "#### ", block, count=1)
        block = re.sub(r"^#{3} +(?!FR-).*$\n?", "", block, flags=re.M)  # bỏ heading phân hệ cũ nằm giữa
        blocks.append((m.group(1), block.rstrip() + "\n"))
    return intro, blocks


def existing_modules(sec3: str) -> list[tuple[str, set[str]]]:
    mods = []
    for m in re.finditer(r"^### +(?!FR-)(.+)$", sec3, re.M):
        nxt = re.search(r"^### +(?!FR-)", sec3[m.end():], re.M)
        body = sec3[m.end(): m.end() + nxt.start()] if nxt else sec3[m.end():]
        name = re.sub(r"^\d+(\.\d+)*\s*", "", m.group(1)).strip()
        mods.append((name, set(re.findall(r"^#{3,4} +(FR-\d+)", body, re.M))))
    return mods


def manual_trace(sec8: str) -> dict[str, tuple[set, set]]:
    rows = {}
    for line in sec8.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"FR-\d+", cells[0]):
            rows[cells[0]] = (set(re.findall(r"US-\d+", " ".join(cells[1:-1]))), set(re.findall(r"SCR-\d+", cells[-1])))
    return rows


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("du_an")
    ap.add_argument("--modules", default="")
    ap.add_argument("--keep-trace", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args(argv[1:])

    project = REPO / "outputs" / args.du_an.strip("/\\")
    srs = project / "SRS.md"
    out_dir = project / "srs"
    if not srs.exists():
        print(f"ERROR: không có {srs.relative_to(REPO)}")
        return 1
    if out_dir.exists() and any(out_dir.glob("*.md")) and not args.force:
        print(f"ERROR: {out_dir.relative_to(REPO)} đã có — dự án đã tách rồi (dùng --force để tách lại)")
        return 1
    text = srs.read_text(encoding="utf-8-sig").replace(GENERATED_NOTE, "").lstrip()

    chunks = re.split(r"^(?=## )", text, flags=re.M)
    header, sections = chunks[0], chunks[1:]
    if "Lịch sử phiên bản" not in header:
        ver = re.search(r"\|\s*Phiên bản\s*\|\s*([^|]+)\|", header)
        header = header.rstrip() + (
            "\n\n**Lịch sử phiên bản**\n\n| Phiên bản | Ngày | Thay đổi | Nguồn | Ảnh hưởng |\n|---|---|---|---|---|\n"
            f"| {(ver.group(1).split()[0] if ver else '0.1')} | {date.today():%Y-%m-%d} | Chuyển sang cấu trúc tách phân hệ (srs/) | — | Không đổi nội dung |\n")

    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("*.md"):
        old.unlink()
    written = [("00-dau-trang.md", header)]
    extra_no = 10
    warns: list[str] = []
    for sec in sections:
        m = re.match(r"## +(\d+)\.", sec)
        num = int(m.group(1)) if m else None
        if num == 3:
            intro, blocks = split_fr_section(sec)
            seen: set[str] = set()
            for fid, _ in blocks:
                if fid in seen:
                    warns.append(f"{fid} xuất hiện 2 lần trong SRS nguồn — chỉ giữ bản đầu tiên, kiểm tra lại")
                seen.add(fid)
            blocks = [b for i, b in enumerate(blocks) if b[0] not in {x[0] for x in blocks[:i]}]
            written.append(("03-00-chuc-nang.md", intro))
            mods = parse_modules(args.modules) if args.modules else existing_modules(sec)
            if not mods:
                mods = [("Chức năng", {fid for fid, _ in blocks})]
            assigned = set().union(*(s for _, s in mods)) if mods else set()
            rest = [fid for fid, _ in blocks if fid not in assigned]
            if rest:
                mods.append(("Chức năng khác", set(rest)))
            by_id = dict(blocks)
            order = [fid for fid, _ in blocks]
            placed: dict[str, str] = {}
            for name, ids in mods:
                for f in sorted(ids):
                    if f in placed:
                        warns.append(f"{f} nằm trong 2 phân hệ ('{placed[f]}' và '{name}') — chỉ giữ ở '{placed[f]}'")
                        ids.discard(f)
                    else:
                        placed[f] = name
            for i, (name, ids) in enumerate(mods, 1):
                body = "".join(by_id[f] + "\n" for f in order if f in ids)
                if body:
                    written.append((f"03-{i:02d}-{slugify(name)}.md", f"### 3.{i} {name}\n\n{body}"))
            unknown = sorted(set().union(*(s for _, s in mods)) - set(order))
            if unknown:
                warns.append(f"--modules nhắc tới FR không tồn tại: {', '.join(unknown)}")
        elif num == 8 and not args.keep_trace:
            manual = manual_trace(sec)
            auto = {f["id"]: (set(f["us"]), set(f["scr"])) for f in fr_blocks(text)}
            for fid in sorted(set(manual) | set(auto)):
                if manual.get(fid) != auto.get(fid):
                    warns.append(f"truy vết {fid} khác nhau — viết tay {manual.get(fid)} vs dòng 'Truy vết' của FR {auto.get(fid)}; "
                                 "sửa dòng 'Truy vết:' trong FR cho đúng")
        elif num in NAMES:
            written.append((f"{num:02d}-{NAMES[num]}.md", sec))
        else:
            title = re.sub(r"^##\s+", "", sec.splitlines()[0])
            written.append((f"{extra_no:02d}-{slugify(title)[:40]}.md", sec))
            extra_no += 1

    for name, body in written:
        (out_dir / name).write_text(body.strip() + "\n", encoding="utf-8")
    for w in warns:
        print(f"WARN: {w}")
    print(f"split_srs: {len(written)} file trong {out_dir.relative_to(REPO)}/")
    for name, body in written:
        print(f"  {name:<40} {len(body.splitlines()):>5} dòng")
    build(project)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
