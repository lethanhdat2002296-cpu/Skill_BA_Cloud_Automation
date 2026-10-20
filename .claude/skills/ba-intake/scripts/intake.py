#!/usr/bin/env python3
"""Nạp tài liệu đầu vào cho một dự án vào inputs/<du-an>/, giữ phiên bản cũ, tạo diff, commit + push.

Cách dùng:
    python .claude/skills/ba-intake/scripts/intake.py <du-an> \
        [--file PATH ...] [--url URL ...] [--source chat|attachment|url] [--note "..."] \
        [--no-push] [--no-branch]

    --file   file cần nạp. File nằm trong .intake/ (Markdown Claude chuyển từ text trong chat)
             sẽ được CHUYỂN vào dự án; file ở nơi khác được COPY.
    --url    link tải về (http/https; link chia sẻ Google Drive dạng /file/d/<id> được đổi sang link tải).
    --source ghi vào manifest (mặc định: chat nếu file từ .intake/, attachment nếu file khác, url nếu --url).
    --note   ghi chú một dòng vào manifest (vd. "Email bổ sung của chị Hạnh").
    --no-push   chỉ commit, không push.
    --no-branch không tự chuyển sang branch docs/<du-an>.

Quy tắc giữ thông tin cũ:
  - Không bao giờ ghi đè. Trùng tên + khác nội dung -> lưu thành <ten>__v2.<ext>, __v3...
  - Trùng nội dung (SHA-256) với file đã có -> bỏ qua, báo "trùng".
  - Mỗi lần nạp ghi thêm dòng vào inputs/<du-an>/_manifest.md.
  - Lần nạp vào dự án đã có tài liệu -> tạo inputs/<du-an>/_changes/<thoi-diem>.md (diff + chỗ để BA mô tả khác biệt).

Cuối cùng in một dòng JSON (bắt đầu bằng "INTAKE_RESULT ") để Claude đọc.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
INTAKE_DIR = REPO / ".intake"
TEXT_EXT = {".md", ".txt", ".csv", ".json", ".eml", ".html", ".htm", ".xml", ".yaml", ".yml"}
PANDOC_EXT = {".docx", ".odt", ".rtf", ".epub"}
MAX_DOWNLOAD = 50 * 1024 * 1024
META_PREFIX = "_"  # file/thư mục hệ thống trong inputs/<du-an>/
DIFF_MAX_LINES = 400


# ---------------------------------------------------------------- tiện ích
def slugify(text: str) -> str:
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "tai-lieu"


def safe_name(name: str) -> str:
    p = Path(name)
    return f"{slugify(p.stem)}{p.suffix.lower()}"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args: str) -> tuple[int, str]:
    try:
        r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return 127, "git not found"
    return r.returncode, (r.stdout + r.stderr).strip()


def version_parts(name: str) -> tuple[str, int, str]:
    """'bien-ban__v3.md' -> ('bien-ban', 3, '.md'); 'bien-ban.md' -> ('bien-ban', 1, '.md')"""
    p = Path(name)
    m = re.fullmatch(r"(.+?)__v(\d+)", p.stem)
    return (m.group(1), int(m.group(2)), p.suffix) if m else (p.stem, 1, p.suffix)


def content_files(dest: Path) -> list[Path]:
    return sorted(p for p in dest.iterdir() if p.is_file() and not p.name.startswith(META_PREFIX) and not p.name.startswith("."))


def extract_text(path: Path, dest: Path, warnings: list[str]) -> Path | None:
    """Trả về file text dùng để đọc/diff. File nhị phân -> tạo _extracted/<ten>.md nếu trích được."""
    ext = path.suffix.lower()
    if ext in TEXT_EXT:
        return path
    out = dest / "_extracted" / f"{path.stem}{ext.replace('.', '-')}.md"
    if ext in PANDOC_EXT and shutil.which("pandoc"):
        out.parent.mkdir(exist_ok=True)
        r = subprocess.run(["pandoc", str(path), "-t", "gfm", "-o", str(out)], capture_output=True, text=True)
        if r.returncode == 0:
            return out
        warnings.append(f"pandoc không đọc được {path.name}: {r.stderr.strip()[:200]}")
    elif ext == ".pdf" and shutil.which("pdftotext"):
        out.parent.mkdir(exist_ok=True)
        r = subprocess.run(["pdftotext", "-layout", str(path), str(out)], capture_output=True, text=True)
        if r.returncode == 0:
            return out
    return None


def download(url: str, warnings: list[str]) -> Path | None:
    m = re.search(r"drive\.google\.com/file/d/([\w-]+)", url)
    if m:
        url = f"https://drive.google.com/uc?export=download&id={m.group(1)}"
    INTAKE_DIR.mkdir(exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 ba-intake"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            cd = resp.headers.get("Content-Disposition", "")
            fm = re.search(r"filename\*?=(?:UTF-8'')?\"?([^\";]+)", cd)
            name = urllib.parse.unquote(fm.group(1)) if fm else Path(urllib.parse.urlparse(resp.url).path).name
            if not name or "." not in name:
                ctype = resp.headers.get_content_type()
                name = (name or "tai-ve") + {"text/html": ".html", "application/pdf": ".pdf", "text/plain": ".txt"}.get(ctype, ".bin")
            data = resp.read(MAX_DOWNLOAD + 1)
    except Exception as exc:  # noqa: BLE001 — báo lỗi, không dừng
        warnings.append(f"không tải được {url}: {exc}")
        return None
    if len(data) > MAX_DOWNLOAD:
        warnings.append(f"{url}: file > 50MB, bỏ qua")
        return None
    out = INTAKE_DIR / safe_name(name)
    out.write_bytes(data)
    return out


# ---------------------------------------------------------------- git branch
def ensure_branch(du_an: str, warnings: list[str]) -> str:
    target = f"docs/{du_an}"
    code, current = git("rev-parse", "--abbrev-ref", "HEAD")
    if code != 0:
        warnings.append("không phải git repo — bỏ qua commit/push")
        return ""
    if current == target:
        git("pull", "--ff-only")
        return current
    git("fetch", "origin", target)
    if git("rev-parse", "--verify", "--quiet", target)[0] == 0:
        code, out = git("checkout", target)
    elif git("rev-parse", "--verify", "--quiet", f"origin/{target}")[0] == 0:
        code, out = git("checkout", "-b", target, "--track", f"origin/{target}")
    else:
        base = "origin/main" if git("rev-parse", "--verify", "--quiet", "origin/main")[0] == 0 else "main"
        if git("rev-parse", "--verify", "--quiet", base)[0] != 0:
            base = "HEAD"
        code, out = git("checkout", "-b", target, base)
    if code != 0:
        warnings.append(f"không chuyển được sang {target} (ở lại {current}): {out[:200]}")
        return current
    git("pull", "--ff-only")
    return target


# ---------------------------------------------------------------- manifest & diff
MANIFEST_HEAD = """# Manifest tài liệu đầu vào — {du_an}

> Sinh tự động bởi `ba-intake/scripts/intake.py`. Mỗi lần nạp thêm dòng mới; không xoá dòng cũ.
> File `__vN` là phiên bản mới của file cùng tên; bản cũ vẫn giữ nguyên.

| Thời điểm | File | Nguồn | Trạng thái | SHA-256 | Phiên bản trước | Ghi chú |
|---|---|---|---|---|---|---|
"""


def append_manifest(dest: Path, du_an: str, rows: list[dict]) -> None:
    mf = dest / "_manifest.md"
    if not mf.exists():
        mf.write_text(MANIFEST_HEAD.format(du_an=du_an), encoding="utf-8")
    with mf.open("a", encoding="utf-8") as f:
        for r in rows:
            note = r.get("note", "").replace("|", "/")
            f.write(f"| {r['time']} | {r['file']} | {r['source']} | {r['status']} | `{r['sha'][:10]}` | {r.get('previous') or '—'} | {note or '—'} |\n")


def read_text(path: Path | None) -> list[str] | None:
    if not path or not path.exists():
        return None
    try:
        return path.read_text(encoding="utf-8-sig").splitlines()
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig", errors="replace").splitlines()


def write_change_report(dest: Path, stamp: str, pairs: list[dict], added: list[dict], existing_before: list[str]) -> Path:
    ch = dest / "_changes"
    ch.mkdir(exist_ok=True)
    out = ch / f"{stamp}.md"
    lines = [f"# Thay đổi tài liệu đầu vào — {stamp}", "",
             f"- Tài liệu đã có trước lần nạp này: {len(existing_before)} file",
             f"- File mới bổ sung: {', '.join(a['file'] for a in added) or '—'}",
             f"- File có phiên bản mới: {', '.join(p['file'] for p in pairs) or '—'}", ""]
    for p in pairs:
        lines += [f"## {p['previous']} → {p['file']}", ""]
        if p.get("diff") is None:
            lines += ["_Không so sánh tự động được (file nhị phân, chưa trích text). Claude đọc trực tiếp hai file để mô tả khác biệt._", ""]
            continue
        lines += [f"Thống kê: +{p['added']} dòng, −{p['removed']} dòng.", "", "```diff", *p["diff"], "```", ""]
    lines += ["## Nhận định của BA", "",
              "<!-- Claude điền: bảng Mục | Thông tin cũ (nguồn) | Thông tin mới (nguồn) | Loại (Thêm/Sửa/Bỏ/Mâu thuẫn) | Ảnh hưởng -->",
              "", "## Quyết định", "", "<!-- Claude điền sau khi hỏi người làm: Merge / Giữ cả hai / Người làm tự mô tả -->", ""]
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


# ---------------------------------------------------------------- main
def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("du_an")
    ap.add_argument("--file", action="append", default=[])
    ap.add_argument("--url", action="append", default=[])
    ap.add_argument("--source")
    ap.add_argument("--note", default="")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--no-branch", action="store_true")
    args = ap.parse_args(argv[1:])

    du_an = slugify(args.du_an) if args.du_an != "_example" else "_example"
    warnings: list[str] = []
    branch = "" if args.no_branch else ensure_branch(du_an, warnings)

    dest = REPO / "inputs" / du_an
    dest.mkdir(parents=True, exist_ok=True)
    existing_before = [p.name for p in content_files(dest)]
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    sources: list[tuple[Path, str]] = []
    for f in args.file:
        p = Path(f)
        p = p if p.is_absolute() else (Path.cwd() / p)
        if not p.exists():
            warnings.append(f"không tìm thấy file {f}")
            continue
        src = args.source or ("chat" if INTAKE_DIR in p.resolve().parents else "attachment")
        sources.append((p.resolve(), src))
    for u in args.url:
        p = download(u, warnings)
        if p:
            sources.append((p, args.source or f"url: {u}"))

    known = {sha256(p): p.name for p in content_files(dest)}
    added, versions, duplicates, rows, extracted = [], [], [], [], []
    for src, source in sources:
        digest = sha256(src)
        if digest in known:
            duplicates.append({"file": src.name, "same_as": known[digest]})
            if INTAKE_DIR in src.parents:
                src.unlink()
            continue
        if src.parent == dest:  # đã nằm sẵn trong thư mục dự án (vd. Claude ghi thẳng vào)
            name, prev = src.name, None
            target = src
        else:
            name = safe_name(src.name)
            base, _, ext = version_parts(name)
            same = [p for p in content_files(dest) if version_parts(p.name)[0] == base and version_parts(p.name)[2] == ext]
            prev = max(same, key=lambda p: version_parts(p.name)[1]) if same else None
            if prev:
                name = f"{base}__v{version_parts(prev.name)[1] + 1}{ext}"
            target = dest / name
            if INTAKE_DIR in src.parents:
                shutil.move(str(src), target)
            else:
                shutil.copy2(src, target)
        known[digest] = target.name
        text_path = extract_text(target, dest, warnings)
        if text_path and text_path != target:
            extracted.append(text_path.relative_to(REPO).as_posix())
        row = {"time": now, "file": target.name, "source": source, "sha": digest, "note": args.note,
               "status": "phiên bản mới" if prev else "mới"}
        if prev:
            row["previous"] = prev.name
            old_txt = read_text(extract_text(prev, dest, warnings))
            new_txt = read_text(text_path)
            item = {"file": target.name, "previous": prev.name}
            if old_txt is not None and new_txt is not None:
                diff = list(difflib.unified_diff(old_txt, new_txt, prev.name, target.name, lineterm="", n=2))
                item["added"] = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
                item["removed"] = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
                item["diff"] = diff[:DIFF_MAX_LINES] + (["... (cắt bớt)"] if len(diff) > DIFF_MAX_LINES else [])
            else:
                item["diff"] = None
            versions.append(item)
        else:
            added.append({"file": target.name})
        rows.append(row)

    change_report = None
    if rows:
        append_manifest(dest, du_an, rows)
        if existing_before:
            change_report = write_change_report(dest, stamp, versions, added, existing_before).relative_to(REPO).as_posix()

    commit = pushed = None
    if rows and branch:
        git("add", "--", f"inputs/{du_an}")
        msg = f"input({du_an}): {len(added)} file mới, {len(versions)} phiên bản mới"
        code, out = git("commit", "-m", msg)
        if code == 0:
            commit = git("rev-parse", "--short", "HEAD")[1]
            if not args.no_push and git("remote", "get-url", "origin")[0] == 0:
                code, out = git("push", "-u", "origin", "HEAD")
                pushed = code == 0
                if not pushed:
                    warnings.append(f"push thất bại: {out[-300:]}")
        else:
            warnings.append(f"commit thất bại: {out[-300:]}")

    for w in warnings:
        print(f"WARN: {w}")
    for a in added:
        print(f"MỚI: inputs/{du_an}/{a['file']}")
    for v in versions:
        stat = f"+{v['added']}/−{v['removed']} dòng" if v.get("diff") is not None else "không diff được"
        print(f"PHIÊN BẢN MỚI: {v['previous']} → {v['file']} ({stat})")
    for d in duplicates:
        print(f"TRÙNG (bỏ qua): {d['file']} = {d['same_as']}")
    result = {
        "project": du_an, "branch": branch, "is_update": bool(existing_before) and bool(rows),
        "added": [a["file"] for a in added],
        "versions": [{k: v[k] for k in ("previous", "file", "added", "removed") if k in v} for v in versions],
        "duplicates": duplicates, "extracted": extracted, "change_report": change_report,
        "commit": commit, "pushed": pushed, "warnings": warnings,
    }
    print("INTAKE_RESULT " + json.dumps(result, ensure_ascii=False))
    return 0 if rows or duplicates else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
