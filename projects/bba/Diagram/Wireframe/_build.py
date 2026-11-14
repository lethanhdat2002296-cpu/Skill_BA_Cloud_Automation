"""Đóng gói wireframe Approvals (FRD 2.8 Sprint 4) và chụp PNG từng màn / trạng thái.

Chạy:  python projects/bba/Diagram/Wireframe/_build.py
- Ghép 4 sơ đồ BPMN (Diagram/Flow/swimlane-bpmn-*.png) vào template dạng data URI
  → approvals-sprint4.html (trang publish làm Artifact / mở trực tiếp bằng trình duyệt).
- Chụp từng màn và trạng thái → png/SCR-xx-<slug>[--<state>].png (nhúng vào FRD Word).
"""
from __future__ import annotations

import base64
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FLOW = HERE.parent / "Flow"
SRC = HERE / "_approvals-sprint4.template.html"
OUT = HERE / "approvals-sprint4.html"
PNG = HERE / "png"
BPMN = {
    "BPMN_52": "swimlane-bpmn-bba-52-duyet-hai-cap.png",
    "BPMN_4953": "swimlane-bpmn-bba-49-53-cau-hinh-route.png",
    "BPMN_50": "swimlane-bpmn-bba-50-uy-quyen-duyet.png",
    "BPMN_51": "swimlane-bpmn-bba-51-tac-dong-thiet-lap.png",
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def shrink(path: Path) -> None:
    """Giảm còn 64 màu (wireframe tông xám) để file Word nhẹ, dưới giới hạn upload Drive."""
    from PIL import Image
    Image.open(path).convert("RGB").quantize(colors=64, method=Image.Quantize.MEDIANCUT).save(path, optimize=True)


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    for key, name in BPMN.items():
        data = base64.b64encode((FLOW / name).read_bytes()).decode()
        html = html.replace("{{%s}}" % key, f"data:image/png;base64,{data}")
    OUT.write_text(html, encoding="utf-8")
    print(f"OK: {OUT.relative_to(HERE.parents[2])} ({OUT.stat().st_size // 1024} KB)")

    from playwright.sync_api import sync_playwright
    PNG.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 900}, device_scale_factor=1.5)
        page.set_content("<!doctype html><html><head><meta charset='utf-8'></head><body>" + html + "</body></html>")
        screens = page.evaluate("window.WF_SCREENS")
        n = 0
        for s in screens:
            if s["id"] == "bpmn":
                continue
            for st in s["states"]:
                page.evaluate("([a, b]) => window.showWireframe(a, b)", [s["id"], st])
                name = f'{s["code"]}-{s.get("slug") or slug(s["name"])}' + ("" if st == "default" else f"--{st}") + ".png"
                page.locator("#frame .app").screenshot(path=str(PNG / name))
                shrink(PNG / name)
                n += 1
        browser.close()
    print(f"OK: {n} PNG → {PNG.relative_to(HERE.parents[2])}")


if __name__ == "__main__":
    main()
