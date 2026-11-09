"""Đường dẫn chuẩn của một dự án — mọi script dùng module này, không tự ghép đường dẫn.

projects/<du-an>/
  PROJECT.md      thẻ dự án (sinh bởi tools/project.py card) — đọc đầu tiên
  input/          tài liệu khảo sát gốc (ba-intake): _manifest.md, _changes/, _extracted/, _tong-hop.md
  docs/           brainstorm.md, URD.md, UC.md, srs/*.md → SRS.md, backlog.md
  diagrams/       ảnh sơ đồ (Mermaid, swimlane, use case); swimlanes/*.json là nguồn swimlane
  ui/             flows.md, index.html, _pending.md, screens/*.html, png/*.png, assets/
  exports/        file giao khách: SRS.docx, URD.docx, UC.docx, backlog.csv
  _drive.json     ID/link Google Drive
  project.json    (tuỳ chọn) quy tắc riêng của dự án: tài liệu chính, định dạng Word, tự đẩy Drive
  .tmp/           file tạm (không commit)
Trên Google Drive: "BA Projects/<du-an>/" có cùng tên thư mục con (+ _luu-tru/).
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PROJECTS = REPO / "projects"
SUBDIRS = ("input", "docs", "diagrams", "ui", "exports")


def slugify(text: str) -> str:
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


class Project:
    def __init__(self, slug: str):
        self.slug = slug
        self.root = PROJECTS / slug
        self.input = self.root / "input"
        self.docs = self.root / "docs"
        self.srs_dir = self.docs / "srs"
        self.diagrams = self.root / "diagrams"
        self.swimlanes = self.diagrams / "swimlanes"
        self.ui = self.root / "ui"
        self.screens = self.ui / "screens"
        self.png = self.ui / "png"
        self.assets = self.ui / "assets"
        self.exports = self.root / "exports"
        self.tmp = self.root / ".tmp"
        self.drive_json = self.root / "_drive.json"
        self.card = self.root / "PROJECT.md"
        self.config_file = self.root / "project.json"

    @property
    def config(self) -> dict:
        """Quy tắc riêng của dự án (project.json) — {} nếu không có."""
        if not self.config_file.exists():
            return {}
        return json.loads(self.config_file.read_text(encoding="utf-8"))

    def doc(self, name: str) -> Path:
        """Tài liệu nguồn trong docs/ (SRS.md, URD.md, UC.md, backlog.md, brainstorm.md)."""
        return self.docs / name

    def export(self, name: str) -> Path:
        return self.exports / name

    def rel(self, path: Path) -> str:
        """Đường dẫn hiển thị, tính từ gốc repo."""
        return Path(path).resolve().relative_to(REPO).as_posix()

    def exists(self) -> bool:
        return self.root.is_dir()


def all_projects() -> list[str]:
    return sorted(p.name for p in PROJECTS.iterdir() if p.is_dir() and not p.name.startswith(".")) if PROJECTS.is_dir() else []


def find(name: str) -> tuple[Project | None, list[str]]:
    """Tìm đúng MỘT dự án theo tên gần đúng. Trả về (dự án, []) hoặc (None, danh sách ứng viên)."""
    names = all_projects()
    key = slugify(name)
    if key in names:
        return Project(key), []
    contains = [n for n in names if key and key in n]  # "odoo" -> "odoo-mua-hang"
    if len(contains) == 1:
        return Project(contains[0]), []
    # không tự chọn khi chỉ trùng vài chữ (vd. "odoo-ban-hang" ≠ "odoo-mua-hang") — chỉ gợi ý
    words = set(key.split("-")) - {""}
    cands = contains or [n for n in names if words & set(n.split("-"))]
    return None, cands or names


def resolve(name: str) -> Project:
    """Dùng trong script: tìm dự án hoặc thoát với thông báo ngắn (không quét dự án khác)."""
    p, cands = find(name)
    if p:
        return p
    raise SystemExit(f"ERROR: không có dự án '{name}'. Dự án gần đúng: {', '.join(cands) or '(chưa có dự án nào)'}")
