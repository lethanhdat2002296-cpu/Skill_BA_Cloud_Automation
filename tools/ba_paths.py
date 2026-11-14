"""Đường dẫn chuẩn của một dự án — mọi script dùng module này, không tự ghép đường dẫn.

projects/<du-an>/                              (Google Drive: thư mục do user tạo, gắn link — cùng cấu trúc)
  PROJECT.md     thẻ dự án (sinh bởi tools/project.py card) — đọc đầu tiên
  project.json   (tuỳ chọn) quy tắc riêng: tài liệu chính, sprint, định dạng Word, link Drive
  Document/
    Bien_Ban_Khao_Sat/  biên bản / tài liệu khảo sát (Markdown) + _manifest.md, _changes/, _extracted/, _tong-hop.md
    URD/                URD.md, brainstorm.md
    SRS/                srs/*.md (nguồn, tách phân hệ) → SRS.md (sinh tự động)
    FSD/                FSD (*.md); dự án chạy sprint: FSD/Sprint <n>/
    Use_Case/           UC.md
    Backlog/            backlog.md
    Test_Case/          test-cases.md; dự án chạy sprint: Test_Case/Sprint <n>/
  Diagram/
    Flow/               ảnh sơ đồ (srs-NN, flows-NN, uc-NN, swimlane-*) · swimlanes/*.json (nguồn swimlane)
    Wireframe/          flows.md, index.html, _pending.md, screens/*.html, png/*.png, assets/
  _drive.json    link / ID Drive đã dùng (drive-sync ghi)
  .output/       file Word / CSV xuất ra (không commit — chỉ đẩy lên Drive)
  .tmp/          file tạm (không commit)
Git chỉ lưu Markdown trong Document/ (file gốc .docx/.pdf/ảnh của khách bị .gitignore — bản gốc ở Drive).
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PROJECTS = REPO / "projects"
DOC_DIRS = {"survey": "Bien_Ban_Khao_Sat", "urd": "URD", "srs": "SRS", "fsd": "FSD",
            "uc": "Use_Case", "backlog": "Backlog", "tc": "Test_Case"}
DIAGRAM_DIRS = {"flow": "Flow", "wireframe": "Wireframe"}
SUBDIRS = tuple(f"Document/{d}" for d in DOC_DIRS.values()) + tuple(f"Diagram/{d}" for d in DIAGRAM_DIRS.values())
# tài liệu chính -> thư mục chứa nó trong Document/
DOC_HOME = {"SRS.md": "SRS", "URD.md": "URD", "brainstorm.md": "URD", "UC.md": "Use_Case",
            "backlog.md": "Backlog", "test-cases.md": "Test_Case"}


def slugify(text: str) -> str:
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


class Project:
    def __init__(self, slug: str):
        self.slug = slug
        self.root = PROJECTS / slug
        self.document = self.root / "Document"
        self.diagram = self.root / "Diagram"
        self.docs = self.document                       # gốc tính đường dẫn tương đối của tài liệu
        self.input = self.document / DOC_DIRS["survey"]
        self.srs_dir = self.document / "SRS" / "srs"
        self.diagrams = self.diagram / "Flow"
        self.swimlanes = self.diagrams / "swimlanes"
        self.ui = self.diagram / "Wireframe"
        self.screens = self.ui / "screens"
        self.png = self.ui / "png"
        self.assets = self.ui / "assets"
        self.exports = self.root / ".output"
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
        """Tài liệu trong Document/: tên chính (SRS.md, URD.md, UC.md, backlog.md, test-cases.md, brainstorm.md)
        tự vào đúng thư mục; đường dẫn có '/' (vd. 'FSD/Sprint 4/x.md') tính từ Document/."""
        if "/" in name:
            return self.document / name
        return self.document / DOC_HOME[name] / name if name in DOC_HOME else self.document / name

    def doc_dir(self, kind: str, sprint: str | int | None = None) -> Path:
        """Thư mục của một loại tài liệu (survey, urd, srs, fsd, uc, backlog, tc), có thể theo sprint."""
        d = self.document / DOC_DIRS[kind]
        return d / f"Sprint {sprint}" if sprint not in (None, "") else d

    @property
    def sprint(self) -> str:
        """Sprint hiện tại nếu dự án chạy theo sprint (project.json › sprint.current), không thì ''."""
        sp = self.config.get("sprint", {})
        return str(sp.get("current", "")) if sp.get("enabled") else ""

    def export(self, name: str) -> Path:
        """File xuất ra (.docx / .csv) — trong .output/, không commit."""
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
