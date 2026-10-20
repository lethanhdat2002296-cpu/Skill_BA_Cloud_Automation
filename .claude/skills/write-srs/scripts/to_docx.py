#!/usr/bin/env python3
"""Xuất outputs/<du-an>/SRS.md -> SRS.docx bằng pandoc, có ảnh wireframe và sơ đồ.

Cách dùng:
    python .claude/skills/write-srs/scripts/to_docx.py <du-an>

Việc làm:
  1. Render các khối ```mermaid trong SRS.md -> ui/diagrams/srs-NN.png và thay bằng ảnh
     (không có mmdc thì giữ nguyên code block).
  2. Với mỗi ảnh ui/png/SCR-xx-<slug>.png được tham chiếu: chèn thêm ngay sau nó các biến thể
     (--<state>.png, -mobile.png) nếu có, chú thích theo data-label trong HTML.
  3. Gắn kích thước ảnh cho vừa trang A4 (ảnh hẹp như mobile 390px không bị phóng to).
  4. Thêm Phụ lục "UI flows" với các sơ đồ ui/diagrams/flows-NN.png (nếu có).
  5. Gọi pandoc (dùng templates/reference.docx nếu có), rồi đếm ảnh nhúng trong docx.
Exit code 1 nếu thiếu pandoc, thiếu SRS.md, hoặc có ảnh tham chiếu không tồn tại.
"""
from __future__ import annotations

import re
import shutil
import struct
import subprocess
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[4]
REFERENCE_DOCX = REPO / "templates" / "reference.docx"
sys.path.insert(0, str(REPO / ".claude" / "skills" / "render-screens" / "scripts"))
from render_mermaid import render_markdown  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_srs import build, needs_build  # noqa: E402

IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)(\{[^}]*\})?')
SCR_PNG_RE = re.compile(r"^ui/png/(SCR-\d{2,}-[a-z0-9-]+)\.png$")

# Vùng chữ A4 lề 2cm ~ 17cm x 25cm; chừa chỗ cho chú thích
MAX_W_CM = 16.5
MAX_H_CM = 22.0
MOBILE_W_CM = 7.0
PX_PER_CM_DESKTOP = 1440 / MAX_W_CM


def png_size(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as f:
            head = f.read(24)
        if head[:8] != b"\x89PNG\r\n\x1a\n":
            return None
        return struct.unpack(">II", head[16:24])
    except OSError:
        return None


def size_attr(path: Path) -> str:
    """Thuộc tính kích thước pandoc để ảnh vừa trang và giữ tỉ lệ thật."""
    size = png_size(path)
    if not size:
        return "{width=100%}"
    w, h = size
    if "diagrams" in path.parts:
        # Mermaid render với scale 2 -> độ rộng CSS = w/2 px, 1px CSS = 0.02646cm
        w_cm = min(MAX_W_CM, (w / 2) * 0.02646)
    elif w <= 600:
        w_cm = MOBILE_W_CM
    else:
        w_cm = min(MAX_W_CM, w / PX_PER_CM_DESKTOP)
    h_cm = w_cm * h / w
    if h_cm > MAX_H_CM:
        return f"{{height={MAX_H_CM:.1f}cm}}"
    return f"{{width={w_cm:.1f}cm}}"


def state_labels(project: Path, stem: str) -> dict[str, str]:
    html = project / "ui" / "screens" / f"{stem}.html"
    if not html.exists():
        return {}
    text = html.read_text(encoding="utf-8")
    labels = {}
    for tag in re.findall(r"<section[^>]*class=\"[^\"]*wf-state[^\"]*\"[^>]*>", text):
        key = re.search(r'data-state="([^"]*)"', tag)
        lab = re.search(r'data-label="([^"]*)"', tag)
        if key:
            labels[key.group(1)] = lab.group(1) if lab else key.group(1)
    return labels


def variants(project: Path, stem: str) -> list[tuple[str, str]]:
    """[(đường dẫn tương đối, chú thích)] các biến thể ngoài ảnh chính, theo thứ tự state trong HTML."""
    png_dir = project / "ui" / "png"
    labels = state_labels(project, stem)
    order = list(labels) or sorted({p.name[len(stem) + 2:].removesuffix(".png").removesuffix("-mobile")
                                    for p in png_dir.glob(f"{stem}--*.png")})
    out = []
    for key in order:
        if key == "default":
            continue
        fn = f"{stem}--{key}.png"
        if (png_dir / fn).exists():
            out.append((f"ui/png/{fn}", f"Trạng thái: {labels.get(key, key)}"))
    if (png_dir / f"{stem}-mobile.png").exists():
        out.append((f"ui/png/{stem}-mobile.png", "Mobile 390px"))
    for key in order:
        if key == "default":
            continue
        fn = f"{stem}--{key}-mobile.png"
        if (png_dir / fn).exists():
            out.append((f"ui/png/{fn}", f"Mobile 390px — {labels.get(key, key)}"))
    return out


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    du_an = argv[1].strip("/\\")
    project = REPO / "outputs" / du_an
    if needs_build(project):
        build(project)
    srs = project / "SRS.md"
    if not srs.exists():
        print(f"ERROR: không có {srs.relative_to(REPO)}")
        return 1
    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("ERROR: không tìm thấy pandoc (apt-get install -y pandoc / winget install JohnMacFarlane.Pandoc)")
        return 1

    text = srs.read_text(encoding="utf-8")
    errors: list[str] = []

    # 1. Mermaid -> PNG
    diagrams = render_markdown(srs, project / "ui" / "diagrams", "srs")
    for d in reversed(diagrams):
        if d.png:
            rel = d.png.relative_to(project).as_posix()
            text = text[: d.start] + f"![Sơ đồ {d.index} — {d.heading}]({rel})\n" + text[d.end:]

    # 2 + 3. Ảnh: kiểm tra tồn tại, kích thước, chèn biến thể
    def replace_img(m: re.Match) -> str:
        alt, src, attrs = m.group(1), m.group(2), m.group(3)
        path = (project / src)
        if src.startswith(("http://", "https://")):
            errors.append(f"ảnh ngoài internet không được phép: {src}")
            return m.group(0)
        if not path.exists():
            errors.append(f"thiếu ảnh {src} (tham chiếu trong SRS.md)")
            return m.group(0)
        out = f"![{alt}]({src}){attrs or size_attr(path)}"
        sm = SCR_PNG_RE.match(src)
        if sm:
            scr_id = sm.group(1).split("-")[0] + "-" + sm.group(1).split("-")[1]
            for vsrc, cap in variants(project, sm.group(1)):
                out += f"\n\n![{scr_id} — {cap}]({vsrc}){size_attr(project / vsrc)}"
        return out

    text = IMG_RE.sub(replace_img, text)

    # 4. Phụ lục UI flows
    flows = sorted((project / "ui" / "diagrams").glob("flows-*.png"))
    if flows:
        flows_md = project / "ui" / "flows.md"
        heads = {}
        if flows_md.exists():
            from render_mermaid import BLOCK_RE, HEADING_RE
            ft = flows_md.read_text(encoding="utf-8")
            for i, m in enumerate(BLOCK_RE.finditer(ft), 1):
                hs = HEADING_RE.findall(ft[: m.start()])
                heads[i] = hs[-1].strip() if hs else f"Sơ đồ {i}"
        text += "\n\n## Phụ lục A. UI flows\n"
        for p in flows:
            idx = int(re.search(r"(\d+)", p.stem).group(1))
            rel = p.relative_to(project).as_posix()
            text += f"\n### {heads.get(idx, f'Sơ đồ {idx}')}\n\n![{heads.get(idx, p.stem)}]({rel}){size_attr(p)}\n"

    if errors:
        for e in errors:
            print(f"ERROR: {e}")

    # 5. pandoc
    tmp_dir = project / ".tmp"
    tmp_dir.mkdir(exist_ok=True)
    tmp_md = tmp_dir / "SRS.for-docx.md"
    tmp_md.write_text(text, encoding="utf-8")
    out = project / "SRS.docx"
    cmd = [
        pandoc, str(tmp_md),
        "-f", "markdown+pipe_tables+lists_without_preceding_blankline-tex_math_dollars-raw_tex-yaml_metadata_block",
        "-t", "docx", "-o", str(out),
        f"--resource-path={project}",
        "--toc", "--toc-depth=2",
        "-M", "lang=vi-VN",
    ]
    if REFERENCE_DOCX.exists():
        cmd.append(f"--reference-doc={REFERENCE_DOCX}")
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.stderr.strip():
        print(r.stderr.strip())
    if r.returncode != 0 or not out.exists():
        print(f"ERROR: pandoc thất bại (exit {r.returncode})")
        return 1

    expected = len(set(m.group(2) for m in IMG_RE.finditer(text) if (project / m.group(2)).exists()))
    with zipfile.ZipFile(out) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
    n_mermaid_left = len(re.findall(r"^```mermaid", text, re.M))
    print(f"to_docx: {out.relative_to(REPO)} · {len(media)} ảnh nhúng / {expected} ảnh tham chiếu"
          f" · reference.docx: {'có' if REFERENCE_DOCX.exists() else 'không'}"
          + (f" · {n_mermaid_left} sơ đồ Mermaid chưa render (giữ dạng code)" if n_mermaid_left else ""))
    if len(media) < expected:
        print("ERROR: số ảnh nhúng ít hơn số ảnh tham chiếu")
        return 1
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
