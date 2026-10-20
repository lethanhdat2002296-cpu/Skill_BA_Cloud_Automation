#!/usr/bin/env python3
"""Đồng bộ design kit, kiểm tra wireframe và sinh gallery ui/index.html.

Cách dùng:
    python .claude/skills/wireframe/scripts/build_ui.py <du-an>

Việc làm:
  1. Copy design-kit/tokens.css -> outputs/<du-an>/ui/assets/tokens.css
  2. Kiểm tra từng ui/screens/SCR-xx-<slug>.html:
     tên file, comment đầu file, meta wf-*, link tokens.css, URL ngoài, <img>, class ngoài kit, state.
  3. So khớp với ảnh dự kiến trong SRS.md (ui/png/SCR-xx-<slug>.png).
  4. Sinh ui/index.html (gallery).
Exit code 1 nếu có ERROR.
"""
from __future__ import annotations

import html
import re
import shutil
import sys
from html.parser import HTMLParser
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKILL_DIR = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[4]
KIT_CSS = SKILL_DIR / "design-kit" / "tokens.css"

FILE_RE = re.compile(r"^(SCR-\d{2,})-([a-z0-9]+(?:-[a-z0-9]+)*)\.html$")
EXTERNAL_RE = re.compile(r"""(?:src|href)\s*=\s*["']\s*(?:https?:)?//|url\(\s*["']?\s*(?:https?:)?//|@import""", re.I)


class ScreenParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.meta: dict[str, str] = {}
        self.classes: set[str] = set()
        self.states: list[tuple[str, str]] = []
        self.links: list[str] = []
        self.has_img = False
        self.has_style_block = False
        self.has_script = False
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("name", "").startswith("wf-"):
            self.meta[a["name"]] = (a.get("content") or "").strip()
        if tag == "link" and a.get("rel") == "stylesheet":
            self.links.append(a.get("href") or "")
        if tag == "img":
            self.has_img = True
        if tag == "style":
            self.has_style_block = True
        if tag == "script":
            self.has_script = True
        if tag == "title":
            self._in_title = True
        for c in (a.get("class") or "").split():
            self.classes.add(c)
        if "wf-state" in (a.get("class") or "").split():
            self.states.append(((a.get("data-state") or "").strip(), (a.get("data-label") or "").strip()))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def kit_classes() -> set[str]:
    css = KIT_CSS.read_text(encoding="utf-8")
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return set(re.findall(r"\.([a-zA-Z_][\w-]*)", css))


def expected_from_srs(project: Path) -> dict[str, str]:
    """SCR-xx -> slug, lấy từ đường dẫn ảnh trong SRS.md."""
    srs = project / "SRS.md"
    if not srs.exists():
        return {}
    found = {}
    for scr, slug in re.findall(r"ui/png/(SCR-\d{2,})-([a-z0-9-]+?)\.png", srs.read_text(encoding="utf-8")):
        found.setdefault(scr, slug)
    return found


def inspect_screen(path: Path, allowed: set[str], errors: list, warns: list) -> dict:
    name = path.name
    text = path.read_text(encoding="utf-8")
    info = {"file": name, "scr": "", "slug": "", "type": "", "fr": "", "title": "", "states": []}
    m = FILE_RE.match(name)
    if not m:
        errors.append(f"{name}: tên file phải dạng SCR-xx-<slug>.html (slug chữ thường không dấu)")
    else:
        info["scr"], info["slug"] = m.group(1), m.group(2)

    head = text.lstrip()[:600]
    comment = re.search(r"<!--(.*?)-->", head, re.S)
    if not comment or not re.search(r"SCR-\d+", comment.group(1)) or "FR" not in comment.group(1):
        errors.append(f"{name}: thiếu comment đầu file ghi SCR-xx và FR-xx")

    p = ScreenParser()
    p.feed(text)
    info["title"] = p.title.strip()
    info["type"] = p.meta.get("wf-type", "")
    info["fr"] = p.meta.get("wf-fr", "")
    info["states"] = p.states

    if p.meta.get("wf-screen") and info["scr"] and p.meta["wf-screen"] != info["scr"]:
        errors.append(f"{name}: meta wf-screen={p.meta['wf-screen']} không khớp tên file")
    if info["type"] not in ("storefront", "backend"):
        errors.append(f"{name}: meta wf-type phải là storefront hoặc backend")
    if not re.search(r"FR-\d+", info["fr"]):
        errors.append(f"{name}: meta wf-fr phải liệt kê FR-xx")
    if "../assets/tokens.css" not in p.links:
        errors.append(f'{name}: phải có <link rel="stylesheet" href="../assets/tokens.css">')
    if EXTERNAL_RE.search(text):
        errors.append(f"{name}: có tham chiếu ra ngoài (http/https/@import) — không dùng font/ảnh/CDN internet")
    if p.has_img:
        errors.append(f'{name}: có thẻ <img> — dùng <span class="wf-img"></span>')
    if p.has_script:
        warns.append(f"{name}: có <script> — wireframe nên là HTML tĩnh")
    if p.has_style_block:
        warns.append(f"{name}: có khối <style> — chỉ dùng CSS của kit")
    if not p.states:
        errors.append(f'{name}: không có <section class="wf-state"> nào')
    else:
        keys = [s for s, _ in p.states]
        if keys[0] != "default":
            errors.append(f"{name}: state đầu tiên phải có data-state=\"default\"")
        for key, label in p.states:
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key or ""):
                errors.append(f"{name}: data-state '{key}' phải là chữ thường không dấu, nối bằng '-'")
            if not label:
                warns.append(f"{name}: state '{key}' thiếu data-label")
        dup = {k for k in keys if keys.count(k) > 1}
        if dup:
            errors.append(f"{name}: data-state trùng: {', '.join(sorted(dup))}")
    unknown = sorted(c for c in p.classes if c not in allowed)
    if unknown:
        warns.append(f"{name}: class không có trong kit: {', '.join(unknown)}")
    return info


def build_index(project: Path, screens: list[dict], du_an: str) -> None:
    ui = project / "ui"
    png_dir = ui / "png"

    def card(s: dict) -> str:
        stem = Path(s["file"]).stem
        thumb = png_dir / f"{stem}.png"
        img = (f'<a href="png/{stem}.png"><span style="display:block;height:200px;overflow:hidden;border-bottom:1px solid var(--wf-border)">'
               f'<span style="display:block;height:200px;background:url(\'png/{stem}.png\') top left/100% auto no-repeat"></span></span></a>'
               if thumb.exists() else '<span class="wf-img wf-img--wide"></span>')
        variants = []
        for key, label in s["states"]:
            fn = f"{stem}.png" if key == "default" else f"{stem}--{key}.png"
            label_txt = html.escape(label or key)
            variants.append(f'<a href="png/{fn}">{label_txt}</a>' if (png_dir / fn).exists() else f"<span>{label_txt}</span>")
        mobile = ""
        if s["type"] == "storefront":
            mfn = f"{stem}-mobile.png"
            mobile = f' · <a href="png/{mfn}">Mobile 390</a>' if (png_dir / mfn).exists() else " · Mobile 390 (chưa render)"
        return (
            '<div class="wf-card">'
            f"{img}"
            '<div class="wf-card__body wf-stack" style="gap:6px">'
            f'<span class="wf-row"><span class="wf-badge wf-badge--solid">{html.escape(s["scr"])}</span>'
            f'<span class="wf-strong">{html.escape(s["title"].split("—", 1)[-1].strip() or s["slug"])}</span></span>'
            f'<span class="wf-small wf-muted">{html.escape(s["fr"])}</span>'
            f'<span class="wf-small">Trạng thái: {" · ".join(variants)}{mobile}</span>'
            f'<span class="wf-row"><a class="wf-btn wf-btn--sm" href="screens/{html.escape(s["file"])}">Mở HTML</a></span>'
            "</div></div>"
        )

    groups = []
    for kind, label in (("storefront", "Storefront (Magento)"), ("backend", "Backend (Odoo)")):
        items = [s for s in screens if s["type"] == kind]
        if items:
            groups.append(f'<h2 class="wf-h2" style="margin:24px 0 12px">{label} · {len(items)} màn</h2>'
                          f'<div class="wf-grid-3">{"".join(card(s) for s in items)}</div>')
    other = [s for s in screens if s["type"] not in ("storefront", "backend")]
    if other:
        groups.append(f'<h2 class="wf-h2" style="margin:24px 0 12px">Chưa phân loại</h2><div class="wf-grid-3">{"".join(card(s) for s in other)}</div>')

    page = f"""<!doctype html>
<!-- Gallery wireframe — sinh tự động bởi build_ui.py, không sửa tay -->
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wireframe — {html.escape(du_an)}</title>
<link rel="stylesheet" href="assets/tokens.css">
</head>
<body style="background:var(--wf-gray-100)">
<div class="wf-doc-header"><strong>Wireframe · {html.escape(du_an)}</strong><span class="wf-doc-meta">{len(screens)} màn hình · <a href="flows.md" style="color:inherit">flows.md</a></span></div>
<div class="wf-container" style="padding-bottom:48px">
{''.join(groups) if groups else '<div class="wf-empty"><span class="wf-empty__icon"></span><span class="wf-empty__title">Chưa có màn hình nào</span></div>'}
</div>
</body>
</html>
"""
    (ui / "index.html").write_text(page, encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    du_an = argv[1].strip("/\\")
    project = REPO / "outputs" / du_an
    screens_dir = project / "ui" / "screens"
    errors: list[str] = []
    warns: list[str] = []

    assets = project / "ui" / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(KIT_CSS, assets / "tokens.css")

    files = sorted(screens_dir.glob("*.html")) if screens_dir.exists() else []
    if not files:
        errors.append(f"Không có file nào trong {screens_dir.relative_to(REPO)}")

    allowed = kit_classes()
    screens = [inspect_screen(f, allowed, errors, warns) for f in files]

    seen: dict[str, str] = {}
    for s in screens:
        if s["scr"] and s["scr"] in seen:
            errors.append(f"{s['scr']} có 2 file: {seen[s['scr']]} và {s['file']}")
        seen.setdefault(s["scr"], s["file"])

    expected = expected_from_srs(project)
    for scr, slug in expected.items():
        want = f"{scr}-{slug}.html"
        if not (screens_dir / want).exists():
            errors.append(f"SRS.md tham chiếu {scr} (ảnh ui/png/{scr}-{slug}.png) nhưng thiếu ui/screens/{want}")
    for s in screens:
        if expected and s["scr"] and s["scr"] not in expected:
            warns.append(f"{s['file']}: {s['scr']} không có trong SRS mục 6.2")
        elif expected.get(s["scr"]) and expected[s["scr"]] != s["slug"]:
            errors.append(f"{s['file']}: slug khác với SRS ({expected[s['scr']]})")

    build_index(project, screens, du_an)

    for w in warns:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    n_sf = sum(1 for s in screens if s["type"] == "storefront")
    n_be = sum(1 for s in screens if s["type"] == "backend")
    n_states = sum(len(s["states"]) for s in screens)
    print(f"build_ui: {len(screens)} màn ({n_sf} storefront, {n_be} backend), {n_states} state · "
          f"{len(errors)} lỗi, {len(warns)} cảnh báo · gallery: outputs/{du_an}/ui/index.html")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
