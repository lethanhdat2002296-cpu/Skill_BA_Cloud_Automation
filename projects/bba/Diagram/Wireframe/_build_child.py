"""Đóng gói wireframe Child Record Overview (FRD 3.1 Sprint 4) và chụp PNG từng màn / trạng thái.

Chạy:  python projects/bba/Diagram/Wireframe/_build_child.py
- Template → child-overview-sprint4.html (trang publish làm Artifact / mở trực tiếp bằng trình duyệt).
- Chụp từng màn và trạng thái → png/SCR-xx-<slug>[--<state>].png (nhúng vào FRD Word).
"""
from __future__ import annotations

from pathlib import Path

from _build import shrink

HERE = Path(__file__).resolve().parent
SRC = HERE / "_child-overview-sprint4.template.html"
OUT = HERE / "child-overview-sprint4.html"
PNG = HERE / "png"


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    OUT.write_text(html, encoding="utf-8")
    print(f"OK: {OUT.name} ({OUT.stat().st_size // 1024} KB)")
    from playwright.sync_api import sync_playwright
    PNG.mkdir(exist_ok=True)
    n = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 900}, device_scale_factor=1.5)
        page.set_content("<!doctype html><html><head><meta charset='utf-8'></head><body>" + html + "</body></html>")
        for s in page.evaluate("window.WF_SCREENS"):
            for st in s["states"]:
                page.evaluate("([a, b]) => window.showWireframe(a, b)", [s["id"], st])
                name = f'{s["code"]}-{s["slug"]}' + ("" if st == "default" else f"--{st}") + ".png"
                page.locator("#frame .app").screenshot(path=str(PNG / name))
                shrink(PNG / name)
                n += 1
        browser.close()
    print(f"OK: {n} PNG → png/")


if __name__ == "__main__":
    main()
