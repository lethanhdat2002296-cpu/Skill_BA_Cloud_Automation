"""Kiểm tra chất lượng câu chữ dùng chung cho check_srs / backlog_csv / check_tc.

- vague_hits(line): từ mơ hồ, không đo được (bỏ qua chữ trong "ngoặc kép" — đó là dữ liệu / thông báo nguyên văn).
- fr_sections(text): tách SRS thành từng FR {id, title, body, priority, dropped, ac[]}.
- is_negative(ac): AC mô tả tình huống lỗi / ngoại lệ / bị chặn.
- messages(ac): thông báo nguyên văn hệ thống hiện ra ('hiện lỗi "…"').
"""
from __future__ import annotations

import re

# Từ / cụm mơ hồ trong yêu cầu (AC, BR, NFR). Không đưa "nhiều", "cao", "an toàn" vào: thường dùng đúng nghĩa
# ("nhiều dòng", "tồn kho an toàn").
VAGUE_TERMS = (
    "nhanh chóng", "nhanh", "thân thiện", "dễ dùng", "dễ sử dụng", "trực quan", "phù hợp", "hợp lý",
    "linh hoạt", "tối ưu", "kịp thời", "ổn định", "hiệu quả", "tương đối", "hầu hết", "một số",
    "có thể", "nên", "v.v.", "vv.", "...", "khoảng", "đẹp", "chuyên nghiệp",
)
_VAGUE_RE = re.compile(r"(?<!\w)(" + "|".join(re.escape(t) for t in sorted(VAGUE_TERMS, key=len, reverse=True)) + r")(?!\w)", re.I)
_QUOTED_RE = re.compile(r"\"[^\"]*\"|“[^”]*”|`[^`]*`|\([^)]*AS-\d+[^)]*\)")

NEG_RE = re.compile(
    r"lỗi|cảnh báo|chặn|không (được|cho|hiển thị|thể|tạo|chuyển|gửi|có|đổi|lưu)|từ chối|giữ (nguyên|trạng thái)"
    r"|bị (khoá|khóa|huỷ|hủy|ẩn|chặn)|vô hiệu|quá hạn|hết hạn|thất bại|thử lại|retry|timeout|vượt",
    re.I)
MSG_RE = re.compile(r"(lỗi|cảnh báo|thông báo|xác nhận|hộp thoại)\s*(?:là\s*)?[\"“]([^\"”]{3,})[\"”]", re.I)
MSG_NOQUOTE_RE = re.compile(r"hiện (lỗi|cảnh báo)(?!\s*(?:là\s*)?[\"“])", re.I)
FR_HEAD_RE = re.compile(r"^#{3,4} +(FR-\d+)\s*[—–-]?\s*(.*)$", re.M)


def vague_hits(line: str) -> list[str]:
    clean = re.sub(r"trở nên|khoảng (?:thời gian|từ)", " ", _QUOTED_RE.sub(" ", line), flags=re.I)
    return list(dict.fromkeys(m.group(1).lower() for m in _VAGUE_RE.finditer(clean)))


def ac_items(body: str) -> list[str]:
    """Các tiêu chí đánh số sau dòng 'Acceptance criteria' (dừng ở trường '- **…:**' kế tiếp)."""
    idx = body.lower().find("acceptance criteria")
    if idx < 0:
        return []
    rest = body[idx:].split("\n", 1)[1] if "\n" in body[idx:] else ""
    stop = re.search(r"^- \*\*", rest, re.M)
    rest = rest[: stop.start()] if stop else rest
    return [m.group(1).strip() for m in re.finditer(r"^\s*\d+\.\s+(.*)$", rest, re.M)]


def then_part(ac: str) -> str:
    parts = re.split(r"\*\*Then\*\*|\bThen\b", ac, maxsplit=1)
    return parts[1] if len(parts) > 1 else ac


def is_negative(ac: str) -> bool:
    return bool(NEG_RE.search(ac))


def messages(ac: str) -> list[tuple[str, str]]:
    """[(loại, nội dung)] — loại: Lỗi / Cảnh báo / Thông báo / Xác nhận."""
    kinds = {"lỗi": "Lỗi", "cảnh báo": "Cảnh báo", "thông báo": "Thông báo", "xác nhận": "Xác nhận", "hộp thoại": "Xác nhận"}
    return [(kinds[m.group(1).lower()], m.group(2).strip()) for m in MSG_RE.finditer(then_part(ac))]


def fr_sections(text: str) -> list[dict]:
    heads = list(FR_HEAD_RE.finditer(text))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        nxt = re.search(r"^#{2,3} +(?!FR-)", text[m.end():end], re.M)
        body = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():end]
        pr = re.search(r"Độ ưu tiên:\**\s*(\w+)", body)
        out.append({
            "id": m.group(1), "title": m.group(2).strip(), "body": body,
            "priority": pr.group(1) if pr else "",
            "dropped": bool(re.search(r"Đã bỏ", m.group(2))),
            "ac": ac_items(body),
            "line": text[: m.start()].count("\n") + 1,
        })
    return out
