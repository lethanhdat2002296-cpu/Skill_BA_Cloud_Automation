#!/usr/bin/env python3
"""Chụp wireframe HTML ra PNG bằng Playwright (Chromium headless) + kiểm tra layout tự động.

Cách dùng:
    python .claude/skills/render-screens/scripts/shot.py <du-an>
    python .claude/skills/render-screens/scripts/shot.py <du-an> --only SCR-03 SCR-05
    python .claude/skills/render-screens/scripts/shot.py <du-an> --no-mobile

Quy ước tên ảnh (outputs/<du-an>/ui/png/):
    SCR-xx-<slug>.png               state đầu tiên (default), desktop 1440
    SCR-xx-<slug>--<state>.png      các state khác, desktop 1440
    SCR-xx-<slug>-mobile.png        state default, mobile 390 (chỉ storefront)
    SCR-xx-<slug>--<state>-mobile.png

Mỗi <section class="wf-state"> được chụp riêng (element screenshot).
Kiểm tra layout: tràn ngang trang, phần tử vượt mép phải frame, chữ bị cắt (overflow).
Cuối cùng chạy lại wireframe/scripts/build_ui.py để gallery có thumbnail.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
BUILD_UI = REPO / ".claude" / "skills" / "wireframe" / "scripts" / "build_ui.py"

DESKTOP = {"width": 1440, "height": 900}
MOBILE = {"width": 390, "height": 844}

# Trả về danh sách vấn đề layout cho từng state
LAYOUT_JS = r"""
() => {
  const out = [];
  const vw = document.documentElement.clientWidth;
  if (document.documentElement.scrollWidth > vw + 1) {
    out.push({state: '*', issue: `trang tràn ngang: scrollWidth ${document.documentElement.scrollWidth}px > ${vw}px`});
  }
  const label = el => {
    const t = (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    const cls = (el.className && typeof el.className === 'string') ? '.' + el.className.trim().split(/\s+/).join('.') : '';
    return `<${el.tagName.toLowerCase()}${cls}> "${t}"`;
  };
  document.querySelectorAll('.wf-state').forEach(st => {
    const key = st.dataset.state || '?';
    const frame = st.querySelector('.wf-frame');
    if (!frame) { out.push({state: key, issue: 'state không có .wf-frame'}); return; }
    const fr = frame.getBoundingClientRect();
    let n = 0;
    frame.querySelectorAll('*').forEach(el => {
      if (n >= 8) return;
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return;
      const inOverlay = el.closest('.wf-overlay, .wf-dropdown, .wf-toast');
      if (!inOverlay && r.right > fr.right + 1) { out.push({state: key, issue: `vượt mép phải frame ${Math.round(r.right - fr.right)}px: ${label(el)}`}); n++; return; }
      const cs = getComputedStyle(el);
      const clipsX = ['hidden', 'clip'].includes(cs.overflowX) || cs.textOverflow === 'ellipsis';
      if (clipsX && el.scrollWidth > el.clientWidth + 2 && el.children.length === 0) {
        out.push({state: key, issue: `chữ bị cắt: ${label(el)}`}); n++;
      }
      if (el.matches('.wf-btn, .wf-badge, .be-status, .wf-tab') && r.height > 48) {
        out.push({state: key, issue: `nhãn bị xuống dòng: ${label(el)}`}); n++;
      }
      if (el.matches('td, th') && r.width < 90 && r.height > 56 && (el.innerText || '').trim().length > 8) {
        out.push({state: key, issue: `ô bảng quá hẹp, chữ gãy nhiều dòng: ${label(el)}`}); n++;
      }
    });
  });
  return out;
}
"""


def screen_type(html_text: str) -> str:
    m = re.search(r'<meta\s+name=["\']wf-type["\']\s+content=["\']([a-z]+)["\']', html_text, re.I)
    return m.group(1).lower() if m else "backend"


def clean_old(png_dir: Path, stem: str) -> None:
    for p in [png_dir / f"{stem}.png", png_dir / f"{stem}-mobile.png", *png_dir.glob(f"{stem}--*.png")]:
        if p.exists():
            p.unlink()


def shoot(page, html_path: Path, png_dir: Path, stem: str, viewport: dict, suffix: str) -> tuple[list[Path], list[dict]]:
    page.set_viewport_size(viewport)
    page.goto(html_path.resolve().as_uri(), wait_until="load")
    page.evaluate("document.fonts ? document.fonts.ready.then(() => true) : true")
    page.wait_for_timeout(150)
    shots: list[Path] = []
    states = page.query_selector_all(".wf-state")
    if not states:
        out = png_dir / f"{stem}{suffix}.png"
        page.screenshot(path=str(out), full_page=True)
        return [out], [{"state": "*", "issue": "không có .wf-state — đã chụp cả trang"}]
    for i, el in enumerate(states):
        key = el.get_attribute("data-state") or f"state{i + 1}"
        name = f"{stem}{suffix}.png" if i == 0 else f"{stem}--{key}{suffix}.png"
        out = png_dir / name
        el.screenshot(path=str(out))
        shots.append(out)
    issues = page.evaluate(LAYOUT_JS)
    return shots, issues


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("du_an")
    ap.add_argument("--only", nargs="*", default=[], help="chỉ chụp các SCR này (vd. SCR-03 SCR-05)")
    ap.add_argument("--no-mobile", action="store_true", help="bỏ khung 390 cho storefront")
    args = ap.parse_args(argv[1:])

    du_an = args.du_an.strip("/\\")
    project = REPO / "outputs" / du_an
    screens_dir = project / "ui" / "screens"
    png_dir = project / "ui" / "png"
    png_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(screens_dir.glob("SCR-*.html"))
    if args.only:
        wanted = {s.upper() for s in args.only}
        files = [f for f in files if f.name.split("-")[0] + "-" + f.name.split("-")[1] in wanted]
    if not files:
        print(f"ERROR: không có màn hình nào trong {screens_dir.relative_to(REPO)}")
        return 1

    # Bảo đảm tokens.css đã được copy vào ui/assets
    if not (project / "ui" / "assets" / "tokens.css").exists():
        subprocess.run([sys.executable, str(BUILD_UI), du_an], check=False)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: chưa cài Playwright. Chạy: pip install playwright && python -m playwright install --with-deps chromium")
        return 1

    all_shots: list[Path] = []
    problems = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=1)
        for f in files:
            stem = f.stem
            kind = screen_type(f.read_text(encoding="utf-8"))
            clean_old(png_dir, stem)
            shots, issues = shoot(page, f, png_dir, stem, DESKTOP, "")
            if kind == "storefront" and not args.no_mobile:
                m_shots, m_issues = shoot(page, f, png_dir, stem, MOBILE, "-mobile")
                shots += m_shots
                issues += [dict(i, state=f"{i['state']} @390") for i in m_issues]
            all_shots += shots
            print(f"OK: {stem} ({kind}) -> {len(shots)} ảnh")
            for i in issues:
                problems += 1
                print(f"  LAYOUT [{i['state']}]: {i['issue']}")
        browser.close()

    subprocess.run([sys.executable, str(BUILD_UI), du_an], check=False, capture_output=True)

    print("\nẢnh cần mở xem (Read) để review:")
    for s in all_shots:
        print(f"  {s.relative_to(REPO).as_posix()}")
    print(f"\nshot: {len(files)} màn, {len(all_shots)} ảnh, {problems} cảnh báo layout")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
