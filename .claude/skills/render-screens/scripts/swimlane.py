#!/usr/bin/env python3
"""Vẽ sơ đồ Activity – Swimlane từ file JSON ra PNG (SVG + Playwright Chromium).

Cách dùng:
    python .claude/skills/render-screens/scripts/swimlane.py <du-an>
        -> đọc outputs/<du-an>/ui/swimlanes/*.json, ghi outputs/<du-an>/ui/diagrams/swimlane-<ten>.png
    python .../swimlane.py <du-an> --only nhap-kho

Định dạng JSON:
    {
      "title": "Mua vật tư Nhập kho",
      "lanes": ["Người đề xuất", "Nhân viên MH", "Hệ thống"],
      "nodes": [
        {"id": "s",  "lane": 0, "col": 0, "type": "start"},
        {"id": "a1", "lane": 0, "col": 1, "label": "Tạo YCMH"},
        {"id": "d1", "lane": 1, "col": 2, "type": "decision", "label": "Duyệt?"},
        {"id": "x1", "lane": 2, "col": 3, "type": "system", "label": "Tạo RFQ"},
        {"id": "e",  "lane": 2, "col": 4, "type": "end"}
      ],
      "edges": [["s", "a1"], ["a1", "d1"], ["d1", "x1", "Duyệt"], ["d1", "a1", "Từ chối"], ["x1", "e"]]
    }
type: task (mặc định) | system (nền đậm hơn) | decision (hình thoi) | start | end.
"orientation": "vertical" → lane là cột, "col" là thứ tự bước từ trên xuống (vừa trang A4 dọc khi nhúng Word).
Mũi tên: tiến (cột đích > cột nguồn) đi ngang–dọc–ngang qua khe giữa hai cột;
lùi hoặc cùng cột khác lane đi theo rãnh trên cùng của lane đích để không cắt qua các bước.
"""
from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]

HEAD_W = 150      # cột tên lane
COL_W = 176       # bề rộng một cột bước
LANE_H = 116      # chiều cao một lane
TITLE_H = 44
NODE_W, NODE_H = 140, 58
DEC_W, DEC_H = 128, 76
PAD = 16
FONT = "-apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"


def wrap(text: str, width: int = 18) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines or [""]


def render_svg(spec: dict) -> tuple[str, int, int]:
    lanes = spec["lanes"]
    nodes = {n["id"]: n for n in spec["nodes"]}
    ncols = max(n["col"] for n in nodes.values()) + 1
    width = HEAD_W + ncols * COL_W + PAD
    height = TITLE_H + len(lanes) * LANE_H + PAD

    def cx(n):
        return HEAD_W + n["col"] * COL_W + COL_W / 2

    def cy(n):
        return TITLE_H + n["lane"] * LANE_H + LANE_H / 2 + 8

    def half(n):
        t = n.get("type", "task")
        if t == "decision":
            return DEC_W / 2, DEC_H / 2
        if t in ("start", "end"):
            return 14, 14
        return NODE_W / 2, NODE_H / 2

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="{FONT}">',
           '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
           '<path d="M0,0 L10,5 L0,10 z" fill="#333"/></marker></defs>',
           f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fff"/>',
           f'<text x="{PAD}" y="28" font-size="17" font-weight="700" fill="#1f1f1f">{html.escape(spec.get("title", ""))}</text>']
    # lanes
    for i, name in enumerate(lanes):
        y = TITLE_H + i * LANE_H
        fill = "#f7f7f7" if i % 2 == 0 else "#ffffff"
        out.append(f'<rect x="0" y="{y}" width="{width - PAD}" height="{LANE_H}" fill="{fill}" stroke="#bdbdbd"/>')
        out.append(f'<rect x="0" y="{y}" width="{HEAD_W}" height="{LANE_H}" fill="#e6e6e6" stroke="#bdbdbd"/>')
        for k, line in enumerate(wrap(name, 16)):
            out.append(f'<text x="{HEAD_W / 2}" y="{y + LANE_H / 2 + 5 + (k - (len(wrap(name, 16)) - 1) / 2) * 16}" font-size="13" font-weight="700" text-anchor="middle" fill="#333">{html.escape(line)}</text>')

    # edges (vẽ trước để node đè lên)
    for e in spec["edges"]:
        a, b = nodes[e[0]], nodes[e[1]]
        label = e[2] if len(e) > 2 else ""
        ax, ay, bx, by = cx(a), cy(a), cx(b), cy(b)
        aw, ah = half(a)
        bw, bh = half(b)
        if a["lane"] == b["lane"] and b["col"] > a["col"]:
            pts = [(ax + aw, ay), (bx - bw, by)]
            lx, ly = ax + aw + 6, ay - 8
        elif b["col"] > a["col"]:
            gx = ax + COL_W / 2
            pts = [(ax + aw, ay), (gx, ay), (gx, by), (bx - bw, by)]
            lx, ly = ax + aw + 6, ay - 8
        else:
            # lùi hoặc cùng cột: theo rãnh trên của lane đích
            ch = TITLE_H + b["lane"] * LANE_H + 12
            if b["col"] == a["col"] and a["lane"] != b["lane"]:
                sy = ay - ah if b["lane"] < a["lane"] else ay + ah
                ey = by + bh if b["lane"] < a["lane"] else by - bh
                pts = [(ax, sy), (bx, ey)]
                lx, ly = ax + 6, (sy + ey) / 2
            else:
                sy = ay - ah if b["lane"] <= a["lane"] else ay + ah
                pts = [(ax, sy), (ax, ch), (bx, ch), (bx, by - bh)]
                lx, ly = ax + 6, ch - 3 if b["lane"] <= a["lane"] else sy + 14
        d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="#333" stroke-width="1.4" marker-end="url(#arr)"/>')
        if label:
            out.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="11" font-weight="700" fill="#333" paint-order="stroke" stroke="#fff" stroke-width="3">{html.escape(label)}</text>')

    # nodes
    for n in nodes.values():
        x, y, t = cx(n), cy(n), n.get("type", "task")
        label = n.get("label", "")
        if t in ("start", "end"):
            out.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{"#333" if t == "start" else "#fff"}" stroke="#333" stroke-width="2"/>')
            if t == "end":
                out.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#333"/>')
            if label:
                out.append(f'<text x="{x}" y="{y + 30}" font-size="11" text-anchor="middle" fill="#555">{html.escape(label)}</text>')
            continue
        if t == "decision":
            w, h = DEC_W / 2, DEC_H / 2
            out.append(f'<polygon points="{x},{y - h} {x + w},{y} {x},{y + h} {x - w},{y}" fill="#fff" stroke="#333" stroke-width="1.6"/>')
            lines = wrap(label, 14)
        else:
            fill = "#d9d9d9" if t == "system" else "#fff"
            out.append(f'<rect x="{x - NODE_W / 2}" y="{y - NODE_H / 2}" width="{NODE_W}" height="{NODE_H}" rx="8" fill="{fill}" stroke="#333" stroke-width="1.4"/>')
            lines = wrap(label, 19)
        for k, line in enumerate(lines):
            out.append(f'<text x="{x}" y="{y + 4 + (k - (len(lines) - 1) / 2) * 14}" font-size="11.5" text-anchor="middle" fill="#1f1f1f">{html.escape(line)}</text>')
    out.append("</svg>")
    return "\n".join(out), width, height


V_LANE_W = 172     # bề rộng một lane (cột) khi vẽ dọc
V_ROW_H = 96       # chiều cao một bước (hàng)
V_HEAD_H = 40      # hàng tên lane


def render_svg_vertical(spec: dict) -> tuple[str, int, int]:
    """Swimlane dọc: mỗi lane là một cột, các bước đi từ trên xuống (vừa trang A4 dọc)."""
    lanes = spec["lanes"]
    nodes = {n["id"]: n for n in spec["nodes"]}
    nrows = max(n["col"] for n in nodes.values()) + 1
    width = len(lanes) * V_LANE_W + PAD + 90  # chừa lề phải cho nhãn điểm kết thúc
    top = TITLE_H + V_HEAD_H
    height = top + nrows * V_ROW_H + PAD

    def cx(n):
        return n["lane"] * V_LANE_W + V_LANE_W / 2

    def cy(n):
        return top + n["col"] * V_ROW_H + V_ROW_H / 2

    def half(n):
        t = n.get("type", "task")
        if t == "decision":
            return DEC_W / 2, DEC_H / 2 - 6
        if t in ("start", "end"):
            return 14, 14
        return NODE_W / 2, NODE_H / 2

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="{FONT}">',
           '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
           '<path d="M0,0 L10,5 L0,10 z" fill="#333"/></marker></defs>',
           f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fff"/>',
           f'<text x="{PAD / 2}" y="28" font-size="16" font-weight="700" fill="#1f1f1f">{html.escape(spec.get("title", ""))}</text>']
    for i, name in enumerate(lanes):
        x = i * V_LANE_W
        fill = "#f7f7f7" if i % 2 == 0 else "#ffffff"
        out.append(f'<rect x="{x}" y="{TITLE_H}" width="{V_LANE_W}" height="{height - TITLE_H - PAD}" fill="{fill}" stroke="#bdbdbd"/>')
        out.append(f'<rect x="{x}" y="{TITLE_H}" width="{V_LANE_W}" height="{V_HEAD_H}" fill="#e6e6e6" stroke="#bdbdbd"/>')
        lines = wrap(name, 20)
        for k, line in enumerate(lines):
            out.append(f'<text x="{x + V_LANE_W / 2}" y="{TITLE_H + V_HEAD_H / 2 + 5 + (k - (len(lines) - 1) / 2) * 14}" font-size="12.5" font-weight="700" text-anchor="middle" fill="#333">{html.escape(line)}</text>')

    labels = []
    for e in spec["edges"]:
        a, b = nodes[e[0]], nodes[e[1]]
        label = e[2] if len(e) > 2 else ""
        ax, ay, bx, by = cx(a), cy(a), cx(b), cy(b)
        aw, ah = half(a)
        bw, bh = half(b)
        if b["col"] > a["col"] and a["lane"] == b["lane"]:
            pts = [(ax, ay + ah), (bx, by - bh)]
            lx, ly = ax + 6, ay + ah + 13
        elif b["col"] > a["col"]:
            gy = ay + V_ROW_H / 2
            pts = [(ax, ay + ah), (ax, gy), (bx, gy), (bx, by - bh)]
            lx, ly = (ax + bx) / 2 - 16, gy - 5
        elif b["col"] == a["col"]:
            sx = ax + aw if bx > ax else ax - aw
            ex = bx - bw if bx > ax else bx + bw
            pts = [(sx, ay), (ex, by)]
            lx, ly = min(sx, ex) + 6, ay - 6
        else:
            # lùi: theo rãnh trái của lane đích
            ch = b["lane"] * V_LANE_W + 10
            sx = ax - aw if b["lane"] <= a["lane"] else ax + aw
            pts = [(sx, ay), (ch, ay), (ch, by), (bx - bw, by)]
            lx, ly = ch + 4, (ay + by) / 2
        d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="#333" stroke-width="1.4" marker-end="url(#arr)"/>')
        if label:
            labels.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="11" font-weight="700" fill="#333" paint-order="stroke" stroke="#fff" stroke-width="3">{html.escape(label)}</text>')

    for n in nodes.values():
        x, y, t = cx(n), cy(n), n.get("type", "task")
        label = n.get("label", "")
        if t in ("start", "end"):
            out.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{"#333" if t == "start" else "#fff"}" stroke="#333" stroke-width="2"/>')
            if t == "end":
                out.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#333"/>')
            if label:
                out.append(f'<text x="{x + 20}" y="{y + 4}" font-size="11" fill="#555">{html.escape(label)}</text>')
            continue
        if t == "decision":
            w, h = DEC_W / 2, DEC_H / 2 - 6
            out.append(f'<polygon points="{x},{y - h} {x + w},{y} {x},{y + h} {x - w},{y}" fill="#fff" stroke="#333" stroke-width="1.6"/>')
            lines = wrap(label, 14)
        else:
            fill = "#d9d9d9" if t == "system" else "#fff"
            out.append(f'<rect x="{x - NODE_W / 2}" y="{y - NODE_H / 2}" width="{NODE_W}" height="{NODE_H}" rx="8" fill="{fill}" stroke="#333" stroke-width="1.4"/>')
            lines = wrap(label, 21)
        for k, line in enumerate(lines):
            out.append(f'<text x="{x}" y="{y + 4 + (k - (len(lines) - 1) / 2) * 14}" font-size="11.5" text-anchor="middle" fill="#1f1f1f">{html.escape(line)}</text>')
    out += labels  # nhãn vẽ sau cùng để không bị khung bước che
    out.append("</svg>")
    return "\n".join(out), width, height


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("du_an")
    ap.add_argument("--only", nargs="*", default=[])
    args = ap.parse_args(argv[1:])
    project = REPO / "outputs" / args.du_an.strip("/\\")
    src = project / "ui" / "swimlanes"
    out_dir = project / "ui" / "diagrams"
    out_dir.mkdir(parents=True, exist_ok=True)
    specs = sorted(src.glob("*.json"))
    if args.only:
        specs = [s for s in specs if s.stem in args.only]
    if not specs:
        print(f"WARN: không có file JSON nào trong {src.relative_to(REPO)}")
        return 0
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: chưa cài Playwright (xem setup/cloud-setup.sh)")
        return 1
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        for sp in specs:
            spec = json.loads(sp.read_text(encoding="utf-8"))
            svg, w, h = (render_svg_vertical if spec.get("orientation") == "vertical" else render_svg)(spec)
            page.set_viewport_size({"width": int(w), "height": int(h)})
            page.set_content(f"<!doctype html><html><body style='margin:0'>{svg}</body></html>")
            out = out_dir / f"swimlane-{sp.stem}.png"
            page.locator("svg").screenshot(path=str(out))
            print(f"OK: {out.relative_to(REPO).as_posix()}  ({spec.get('title', sp.stem)})")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
