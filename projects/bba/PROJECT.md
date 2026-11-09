# bba (`bba`)

<!-- card:start -->
> Sinh bởi `python tools/project.py card bba` — không sửa tay đoạn này. Đọc thẻ này TRƯỚC khi mở tài liệu lớn.

- Phiên bản: chưa có tài liệu
- Mã: 0 US · 0 UC · 0 FR · 0 NFR · 0 SCR · 0 AS · 0 OQ
- OQ mở (0): không
- Màn chờ vẽ lại: không
- Drive: https://drive.google.com/drive/folders/199Zxc2yR_lxpasyaNkvo3db7vqKIIEyW · 7 file đã đẩy
- Sprint hiện tại: 4
- File: Document/FSD/Sprint 3/BBA-40-2.1.1.00_Inactive_Lead_v0.2.md (317 dòng), Document/FSD/Sprint 3/BBA-41-2.1.1.01_Centre_Sharing_v0.1.md (292 dòng), Document/FSD/Sprint 3/BBA-42-2.1.1.02_Duplicate_Detection_v0.2.md (424 dòng), Document/FSD/Sprint 3/BBA-43-2.1.2.01_Enquiry_Detail_Page_v0.1.md (532 dòng), Document/FSD/Sprint 3/BBA-44-2.1.2.03_View_Timeline_v0.1.md (310 dòng), Document/FSD/tom-tat-fsd.md (244 dòng)
- Commit cuối: 2026-11-09 refactor: nhiều dự án một repo — projects/<du-an>/Document/<loại>/ + Diagram/; Drive luôn Word, hỏi thư mục m

## Bản đồ file

| Cần | Mở | Ghi chú |
|---|---|---|
| Biên bản / tài liệu khảo sát | `Document/Bien_Ban_Khao_Sat/` (`_tong-hop.md` là bản hợp nhất — nguồn ưu tiên) | Lịch sử nạp: `_manifest.md`, `_changes/` — đọc change report mới nhất |
| URD (+ brainstorm) | `Document/URD/` | `grep -n "^#### US-07"` rồi Read đoạn đó |
| SRS | `Document/SRS/SRS.md` (nguồn `Document/SRS/srs/*.md`) | Tra mã → file: `build_srs.py <du-an> --index`; Read theo offset |
| FSD | `Document/FSD/` (theo sprint: `FSD/Sprint <n>/`) | `grep -n "^#### "` để xem mục |
| Use case / Backlog | `Document/Use_Case/UC.md`, `Document/Backlog/backlog.md` | |
| Test case | `Document/Test_Case/` (theo sprint: `Test_Case/Sprint <n>/`) | Ma trận phủ ở mục 6 |
| Mã gốc của khách (nếu nhập URD/FSD) | `Document/doi-chieu-ma.md` | `grep -n "REQ-012"` → mã mới |
| Sơ đồ | `Diagram/Flow/` (`swimlanes/*.json` là nguồn) | |
| Màn hình | `Diagram/Wireframe/flows.md`, `screens/SCR-xx-*.html` | Chỉ mở ảnh `png/` khi cần review |
| File Word / CSV xuất ra | `.output/` (không commit) | Đẩy lên Drive: hỏi link thư mục mỗi lần |

## Google Drive

- Thư mục gốc của dự án (user tạo): https://drive.google.com/drive/folders/199Zxc2yR_lxpasyaNkvo3db7vqKIIEyW
- FSD/Sprint 3/BBA-40-2.1.1.00_Inactive_Lead: https://drive.google.com/file/d/12Mt9ql4Ik6BDHIEiWjmI7KChtkyAMOQn/view
- FSD/Sprint 3/BBA-41-2.1.1.01_Centre_Sharing: https://drive.google.com/file/d/1ssSGdteYhaQnNBmNeAyz9FpLf9qt_7wu/view
- FSD/Sprint 3/BBA-42-2.1.1.02_Duplicate_Detection: https://drive.google.com/file/d/11OwW2c3gZH2g9zExpxzpUSbMaFhR_vOh/view
- FSD/Sprint 3/BBA-43-2.1.2.01_Enquiry_Detail_Page: https://drive.google.com/file/d/1n8vPgwrVW_1YHG7N6SF1lWEC7AOaG4Eh/view
- FSD/Sprint 3/BBA-44-2.1.2.03_View_Timeline: https://drive.google.com/file/d/1Qzk8QUM_RwDR0tnZ30Gd26jpbCZH58_Q/view
- FSD/tom-tat-fsd: https://docs.google.com/document/d/1BesAEcrVQ2FFqq6j8q0Hb6lIvOhWKV5dCKNpBlOQHYI/edit
- SRS/workflow: https://docs.google.com/document/d/1C-DEUoYnRXPDS5g2PtQrMKVxHBXUxhJ5JaBgyJPOTKk/edit

<!-- card:end -->

## Ghi chú (viết tay — giữ nguyên khi sinh lại thẻ)

- **Tên dự án:** BBA — Busy Bees Asia (CRM tuyển sinh + School Management System) · **Lĩnh vực:** Giáo dục mầm non (Edtech) · Singapore, Malaysia (+ Vietnam cho CRM).
- **QUY TẮC RIÊNG (thắng quy tắc chung):** `project.json` + `templates/HUONG-DAN-FSD.md`.
  - Tài liệu chính khách xác nhận là **FSD (FRS, tiếng Anh)**, viết từ `Document/SRS/workflow.md` + SRS (`Document/SRS/*.md`). SRS của dự án chỉ là Scope & Flow — không chạy `srs-pipeline`.
  - Dự án chạy theo **sprint**: Sprint 3 xong (`Document/FSD/Sprint 3/`, BBA-40…44), **đang làm Sprint 4** (`Document/FSD/Sprint 4/`).
  - FSD xong → xuất Word, **hỏi user thư mục Drive** (gợi ý: thư mục `Sprint <n>` của khách trong https://drive.google.com/drive/folders/199Zxc2yR_lxpasyaNkvo3db7vqKIIEyW). Word: Arial 10, giãn dòng 1.5, thụt 0.5", bảng kẻ khung.
- **Nguồn:** 13 SRS v0.1 (Drive của user: https://drive.google.com/drive/folders/1VAVsI8xdn64H1f-myax38vHijyshqmRj) → Markdown ở `Document/SRS/`; 5 FRS Sprint 3 → Markdown ở `Document/FSD/Sprint 3/`. File gốc .docx không lưu trong Git.
- **Đã có:** `Document/FSD/tom-tat-fsd.md` (phân tích 5 FRS), `Document/SRS/workflow.md` (81 quy trình: 7 CRM + 74 SMS, danh mục FSD Phase 1, điểm lệch SRS ↔ FSD).
