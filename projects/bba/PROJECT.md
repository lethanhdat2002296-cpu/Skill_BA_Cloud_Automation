# bba (`bba`)

<!-- card:start -->
> Sinh bởi `python tools/project.py card bba` — không sửa tay đoạn này. Đọc thẻ này TRƯỚC khi mở tài liệu lớn.

- Phiên bản: chưa có tài liệu
- Mã: 0 US · 0 UC · 0 FR · 0 NFR · 0 SCR · 0 AS · 0 OQ
- OQ mở (0): không
- Màn chờ vẽ lại: không
- File: 

## Bản đồ file

| Cần | Mở | Ghi chú |
|---|---|---|
| Yêu cầu hợp nhất mới nhất | `input/_tong-hop.md` | Nguồn ưu tiên khi có |
| Lịch sử nạp / khác biệt | `input/_manifest.md`, `input/_changes/` | Đọc change report mới nhất, không đọc hết |
| FR / NFR / SCR / AS / OQ | `docs/SRS.md` (hoặc `docs/srs/*.md`) | Tra mã → file: `build_srs.py <du-an> --index`; Read theo offset |
| User story / Use case | `docs/URD.md`, `docs/UC.md` | `grep -n "^#### US-07"` rồi Read đoạn đó |
| Backlog | `docs/backlog.md` → `exports/backlog.csv` | |
| Mã gốc của khách (nếu nhập URD/FSD) | `docs/doi-chieu-ma.md` | `grep -n "REQ-012"` → mã mới |
| Test case | `docs/test-cases.md` → `exports/test-cases.csv` | Tra `grep -n "^### FR-07"`; ma trận phủ ở mục 6 |
| Màn hình | `ui/flows.md`, `ui/screens/SCR-xx-*.html` | Chỉ mở ảnh `ui/png/` khi cần review |
| Sơ đồ | `diagrams/` (`swimlanes/*.json` là nguồn) | |
| File giao khách | `exports/` | Sinh ra — không sửa tay |

<!-- card:end -->

## Ghi chú (viết tay — giữ nguyên khi sinh lại thẻ)

- **Tên dự án:** BBA · **Lĩnh vực:** Giáo dục (Edtech).
- **Tài liệu khách có:** FSD (nội dung yêu cầu) + template FSD (mẫu trình bày). Chưa nạp — chờ user đính kèm.
- **Luồng dự kiến:** `ba-intake` (FSD ghi chú "FSD gốc") → `srs-pipeline` bước `doc-import` loại FSD (giữ nội dung, `docs/doi-chieu-ma.md`, URD suy ngược) → use case → backlog → wireframe → Word.
- **Template FSD:** lưu vào `input/` như tài liệu tham chiếu (không phải yêu cầu); không đưa vào bảng đối chiếu mã. Cách dùng (mẫu xuất Word / khung mục) quyết định sau khi xem file.

