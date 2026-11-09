# Hướng dẫn viết FSD — chỉ dùng cho dự án BBA

Quy tắc riêng của BBA, **thắng** quy tắc chung của repo khi khác nhau. Cấu hình máy đọc: `projects/bba/project.json`.

## 1. Tài liệu chính
- **FSD (FRS) là tài liệu khách xác nhận.** SRS của BBA chỉ là Scope & Flow (đầu vào), không viết lại SRS theo chuỗi `srs-pipeline`.
- Không chạy `brainstorm` / `write-urd` / `write-srs` / `srs-pipeline` cho BBA trừ khi user yêu cầu rõ.
- Ngôn ngữ FSD: **tiếng Anh** (giống các FRS đã có). Tài liệu nội bộ (tóm tắt, workflow, phân tích): tiếng Việt.

## 2. Nguồn để viết FSD (bắt buộc theo thứ tự)
1. `docs/workflow.md` — chọn quy trình `WF-…` và dòng WBS ở bảng 2.1 (CRM) hoặc mục 3 (SMS).
2. SRS gốc: `input/_extracted/<tài liệu>-docx.md` — chỉ đọc phần liên quan (`grep -n "2.3 Reference Log"`, `grep -n "BR-CRM-00"`), không đọc cả file.
3. FSD đã có cùng module (`input/fsd/`, `input/_extracted/FRS_*`) — giữ thuật ngữ, quy ước, tham chiếu chéo (BBA-40…44).
4. Điểm lệch SRS ↔ FSD (`docs/workflow.md` mục 5) → đưa vào mục 7 Open Questions, **không tự chọn**.

## 3. Khung và quy ước
- Khung: `templates/template-fsd.md` (giống 5 FRS hiện có). Mục 2 phải có dòng **Source workflow and SRS references** (WF-…, mục SRS, BR-CRM / AC-CRM, WBS).
- Mã trong một FSD: `FR-001`, `BR-001`, `VAL-001`, `DATA-001`, `AC-001`, đánh tiếp liên tục qua các User Story của cùng FSD, không nhảy số. Validation luôn là `VAL-` (không dùng `VR-`).
- Mỗi FR có trong luồng hoặc AC; mỗi BR / VAL có ít nhất một AC ở cột Linked Rule; thông báo hệ thống ghi nguyên văn trong ngoặc kép.
- Thuật ngữ trạng thái theo bảng đã chốt; chưa chốt → dùng đúng chữ của FSD gần nhất và ghi OQ.
- Tên file: `docs/fsd/BBA-<ticket>-<WBS>_<Feature_Name>_v<x.y>.md` (vd. `BBA-45-2.3.1.01_Action_Framework_v0.1.md`) → `exports/<cùng tên>.docx` → Drive `[FRS] <cùng tên>.docx`.
- Bảng thuộc tính đầu tài liệu có dòng `| Sprint | 4 |` — quyết định thư mục Sprint trên Drive.

## 4. Xuất bản và Google Drive (tự động cho BBA)
```bash
python .claude/skills/write-srs/scripts/to_docx.py bba --src fsd/<file>.md     # áp định dạng ở project.json
python .claude/skills/drive-sync/scripts/drive_pack.py bba                     # kế hoạch đẩy (docs theo project.json)
```
- **FSD hoàn thành** → đẩy **file .docx nguyên bản** (không chuyển Google Doc, `disableConversionToGoogleType: true`) vào thư mục Sprint của khách: https://drive.google.com/drive/folders/199Zxc2yR_lxpasyaNkvo3db7vqKIIEyW › `Sprint <n>` (id trong `project.json` › `drive.sprint_folders`). Tên trên Drive: `[FRS] BBA-xx-<WBS>_<Feature_Name>_v<x.y>.docx` — giống Sprint 3.
- FSD lên phiên bản mới (v0.1 → v0.2) → bản mới vào cùng thư mục Sprint, bản cũ chuyển vào `BA Projects/bba/_luu-tru/` (không xoá).
- Sprint mới: tìm thư mục `Sprint <n>` trong thư mục gốc trên (chưa có mới tạo), thêm id vào `sprint_folders`, đổi `current_sprint`.
- Tài liệu nội bộ (workflow, tóm tắt, phân tích) → Google Doc trong `BA Projects/bba/docs/`, không đưa vào thư mục Sprint của khách.
- Hiện tại: **Sprint 3 đã xong (BBA-40…44), đang làm Sprint 4.**
- Định dạng Word (project.json `docx_style`): Arial 10; giãn dòng 1.5; thụt đầu dòng đoạn văn 0.5" (1,27 cm); bảng kẻ khung đơn 0.5 pt toàn bộ, hàng tiêu đề nền xám nhạt in đậm, lặp lại khi sang trang; chữ trong bảng giãn dòng 1.0, không thụt.
