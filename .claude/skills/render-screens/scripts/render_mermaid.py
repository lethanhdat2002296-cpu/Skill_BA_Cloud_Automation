#!/usr/bin/env python3
"""Render các khối ```mermaid trong một file Markdown ra PNG bằng mermaid-cli (mmdc).

Cách dùng (CLI):
    python .claude/skills/render-screens/scripts/render_mermaid.py <du-an>
        -> render ui/flows.md  -> ui/diagrams/flows-01.png, flows-02.png, ...
        -> render SRS.md       -> ui/diagrams/srs-01.png, ...
    python .../render_mermaid.py <du-an> --file ui/flows.md --prefix flows

Dùng như module (to_docx.py import):
    blocks = render_markdown(md_path, out_dir, prefix)  # [Diagram(...)]

Tìm mmdc: lệnh `mmdc` trên PATH, nếu không có thì `npx -y -p @mermaid-js/mermaid-cli mmdc`.
Nếu Chromium của puppeteer lỗi mà có Playwright thì thử lại bằng Chromium của Playwright.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
BLOCK_RE = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)


@dataclass
class Diagram:
    index: int          # 1-based
    start: int          # vị trí ký tự của khối trong file
    end: int
    code: str
    heading: str        # heading gần nhất phía trên
    png: Path | None    # None nếu render lỗi


def find_mmdc() -> list[str] | None:
    exe = shutil.which("mmdc")
    if exe:
        return [exe]
    npx = shutil.which("npx")
    if npx:
        return [npx, "-y", "-p", "@mermaid-js/mermaid-cli", "mmdc"]
    return None


def _playwright_chromium() -> str | None:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        return None
    try:
        with sync_playwright() as p:
            path = p.chromium.executable_path
            return path if path and Path(path).exists() else None
    except Exception:
        return None


def _run_mmdc(mmdc: list[str], src: Path, out: Path, cfg: Path) -> tuple[bool, str]:
    # Chỉ dùng option có ở mọi version mmdc (v12 đã bỏ -w/-H)
    cmd = mmdc + ["-i", str(src), "-o", str(out), "-b", "white", "-s", "2", "-p", str(cfg)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    ok = r.returncode == 0 and out.exists() and out.stat().st_size > 0
    return ok, (r.stderr or r.stdout).strip()[-800:]


def render_markdown(md_path: Path, out_dir: Path, prefix: str, quiet: bool = False) -> list[Diagram]:
    text = md_path.read_text(encoding="utf-8")
    matches = list(BLOCK_RE.finditer(text))
    diagrams: list[Diagram] = []
    if not matches:
        return diagrams

    mmdc = find_mmdc()
    if not mmdc and not quiet:
        print("WARN: không tìm thấy mmdc/npx — giữ nguyên code Mermaid (cài: npm install -g @mermaid-js/mermaid-cli)")

    out_dir.mkdir(parents=True, exist_ok=True)
    if mmdc:
        for old in out_dir.glob(f"{prefix}-*.png"):
            old.unlink()

    with tempfile.TemporaryDirectory() as tmp:
        tmpd = Path(tmp)
        cfg = tmpd / "puppeteer.json"
        cfg.write_text(json.dumps({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}), encoding="utf-8")
        fallback_cfg_ready = False

        for i, m in enumerate(matches, 1):
            heads = HEADING_RE.findall(text[: m.start()])
            heading = heads[-1].strip() if heads else md_path.stem
            png: Path | None = None
            if mmdc:
                src = tmpd / f"{prefix}-{i:02d}.mmd"
                src.write_text(m.group(1), encoding="utf-8")
                out = out_dir / f"{prefix}-{i:02d}.png"
                ok, log = _run_mmdc(mmdc, src, out, cfg)
                if not ok and not fallback_cfg_ready:
                    chromium = _playwright_chromium()
                    if chromium:
                        cfg.write_text(json.dumps({"executablePath": chromium,
                                                   "args": ["--no-sandbox", "--disable-setuid-sandbox"]}), encoding="utf-8")
                        fallback_cfg_ready = True
                        ok, log = _run_mmdc(mmdc, src, out, cfg)
                if ok:
                    png = out
                    if not quiet:
                        print(f"OK: {out.relative_to(REPO)}  ({heading})")
                elif not quiet:
                    print(f"ERROR: render Mermaid #{i} trong {md_path.name} ({heading}) thất bại:\n{log}")
            diagrams.append(Diagram(i, m.start(), m.end(), m.group(1), heading, png))
    return diagrams


def main(argv: list[str]) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("du_an")
    ap.add_argument("--file", help="file Markdown tương đối với outputs/<du-an>/")
    ap.add_argument("--prefix", help="tiền tố tên PNG")
    args = ap.parse_args(argv[1:])

    project = REPO / "outputs" / args.du_an.strip("/\\")
    out_dir = project / "ui" / "diagrams"
    targets = [(project / args.file, args.prefix or Path(args.file).stem.lower())] if args.file else [
        (project / "ui" / "flows.md", "flows"),
        (project / "SRS.md", "srs"),
    ]
    failed = 0
    total = 0
    for md, prefix in targets:
        if not md.exists():
            print(f"WARN: không có {md.relative_to(REPO)}")
            continue
        ds = render_markdown(md, out_dir, prefix)
        total += len(ds)
        failed += sum(1 for d in ds if d.png is None)
    print(f"render_mermaid: {total - failed}/{total} sơ đồ đã render vào outputs/{args.du_an}/ui/diagrams/")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
