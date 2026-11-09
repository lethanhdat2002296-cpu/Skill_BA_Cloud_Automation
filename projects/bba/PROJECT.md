# bba (`bba`)

<!-- card:start -->
> Sinh bởi `python tools/project.py card bba` — không sửa tay đoạn này. Đọc thẻ này TRƯỚC khi mở tài liệu lớn.

- Phiên bản: chưa có tài liệu
- Mã: 0 US · 0 UC · 0 FR · 0 NFR · 0 SCR · 0 AS · 0 OQ
- OQ mở (0): không
- Màn chờ vẽ lại: không
- Drive: https://drive.google.com/drive/folders/14UfuNWREnhmc37BoMfmJLcnd0guar-_8 (2 mục)
- File: 
- Commit cuối: 2026-11-09 docs(bba): tóm tắt 5 FSD (BBA-40..44) — phân tích function và vấn đề cần chốt

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

## Google Drive

- Thư mục: https://drive.google.com/drive/folders/14UfuNWREnhmc37BoMfmJLcnd0guar-_8
- tom-tat-fsd: https://docs.google.com/document/d/1BesAEcrVQ2FFqq6j8q0Hb6lIvOhWKV5dCKNpBlOQHYI/edit
- workflow: https://docs.google.com/document/d/1C-DEUoYnRXPDS5g2PtQrMKVxHBXUxhJ5JaBgyJPOTKk/edit

<!-- card:end -->

## Ghi chú (viết tay — giữ nguyên khi sinh lại thẻ)

- **Tên dự án:** BBA — Busy Bees Asia (CRM tuyển sinh + School Management System) · **Lĩnh vực:** Giáo dục mầm non (Edtech) · Singapore, Malaysia (+ Vietnam cho CRM).
- **QUY TẮC RIÊNG (thắng quy tắc chung):** `project.json` + `templates/HUONG-DAN-FSD.md`.
  - Tài liệu chính khách xác nhận là **FSD (FRS, tiếng Anh)**, viết từ `docs/workflow.md` + SRS gốc. SRS của dự án chỉ là Scope & Flow — không chạy `srs-pipeline`.
  - **FSD hoàn thành → đẩy ngay** file .docx `[FRS] BBA-xx-…_vX.Y.docx` vào thư mục Sprint của khách: https://drive.google.com/drive/folders/199Zxc2yR_lxpasyaNkvo3db7vqKIIEyW (Sprint 3 = BBA-40…44 đã xong; **đang làm Sprint 4**). Tài liệu nội bộ → `BA Projects/bba/docs/` (Google Doc).
  - Word: Arial 10, giãn dòng 1.5, thụt đầu dòng 0.5", bảng kẻ khung đầy đủ.
- **Nguồn:** 13 SRS v0.1 (Drive gốc của user: https://drive.google.com/drive/folders/1VAVsI8xdn64H1f-myax38vHijyshqmRj) → `input/srs/`; 5 FRS (BBA-40…44) → `input/fsd/`; bản trích chữ ở `input/_extracted/`.
- **Đã có:** `docs/tom-tat-fsd.md` (phân tích 5 FRS), `docs/workflow.md` (81 quy trình: 7 CRM + 74 SMS, danh mục FSD Phase 1, điểm lệch SRS ↔ FSD).
