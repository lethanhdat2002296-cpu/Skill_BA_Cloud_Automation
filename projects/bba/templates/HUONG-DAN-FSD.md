# Hướng dẫn viết FSD — chỉ dùng cho dự án BBA

Quy tắc riêng của BBA, **thắng** quy tắc chung của repo khi khác nhau. Cấu hình máy đọc: `projects/bba/project.json`.

## 1. Tài liệu chính
- **FSD (FRS) là tài liệu khách xác nhận.** SRS của BBA chỉ là Scope & Flow (đầu vào), không viết lại SRS theo chuỗi `srs-pipeline`.
- Không chạy `brainstorm` / `write-urd` / `write-srs` / `srs-pipeline` cho BBA trừ khi user yêu cầu rõ.
- Ngôn ngữ FSD: **tiếng Anh** (giống các FRS đã có). Tài liệu nội bộ (tóm tắt, workflow, phân tích): tiếng Việt.

## 2. Nguồn để viết FSD (bắt buộc theo thứ tự)
1. `Document/SRS/workflow.md` — chọn quy trình `WF-…` và dòng WBS ở bảng 2.1 (CRM) hoặc mục 3 (SMS).
2. SRS gốc (Markdown): `Document/SRS/BBA_CRM_SRS_v0.1.md`, `Document/SRS/BBA-SMS-SRS-*.md` — chỉ đọc phần liên quan (`grep -n "2.3 Reference Log"`, `grep -n "BR-CRM-00"`), không đọc cả file.
3. FSD đã có cùng module (`Document/FSD/Sprint 3/*.md`) — giữ thuật ngữ, quy ước, tham chiếu chéo (BBA-40…44).
4. Điểm lệch SRS ↔ FSD (`Document/SRS/workflow.md` mục 5) → đưa vào mục 7 Open Questions, **không tự chọn**.

## 3. Khung và quy ước
- Khung: `templates/template-fsd.md` (giống 5 FRS hiện có). Mục 2 phải có dòng **Source workflow and SRS references** (WF-…, mục SRS, BR-CRM / AC-CRM, WBS).
- Mã trong một FSD: `FR-001`, `BR-001`, `VAL-001`, `DATA-001`, `AC-001`, đánh tiếp liên tục qua các User Story của cùng FSD, không nhảy số. Validation luôn là `VAL-` (không dùng `VR-`).
- Mỗi FR có trong luồng hoặc AC; mỗi BR / VAL có ít nhất một AC ở cột Linked Rule; thông báo hệ thống ghi nguyên văn trong ngoặc kép.
- Thuật ngữ trạng thái theo bảng đã chốt; chưa chốt → dùng đúng chữ của FSD gần nhất và ghi OQ.
- Tên file: `Document/FSD/Sprint <n>/BBA-<ticket>-<WBS>_<Feature_Name>_v<x.y>.md` (vd. `BBA-45-2.3.1.01_Action_Framework_v0.1.md`) → `.output/<cùng tên>.docx` → Drive `[FRS] <cùng tên>.docx`.
- Bảng thuộc tính đầu tài liệu có dòng `| Sprint | 4 |` (trùng thư mục `Sprint <n>` chứa file).

## 4. Xuất bản và Google Drive
```bash
python .claude/skills/write-srs/scripts/to_docx.py bba --src "FSD/Sprint 4/<file>.md"   # Word theo docx_style của project.json
python .claude/skills/drive-sync/scripts/drive_pack.py bba                              # kế hoạch đẩy + gợi ý thư mục
```
- FSD lưu trong Git: `Document/FSD/Sprint <n>/BBA-xx-<WBS>_<Feature_Name>_v<x.y>.md` (sprint hiện tại: `project.json` › `sprint.current`).
- **FSD hoàn thành → đẩy Word**, theo `drive-sync`: **hỏi user thư mục đích** mỗi lần. Gợi ý mặc định: thư mục `Sprint <n>` của khách trong https://drive.google.com/drive/folders/199Zxc2yR_lxpasyaNkvo3db7vqKIIEyW (`project.json` › `drive.folder_hints`). Tên trên Drive: `[FRS] BBA-xx-<WBS>_<Feature_Name>_v<x.y>.docx` — giống Sprint 3.
- Drive của BBA giữ nguyên cấu trúc khách đang dùng (`Sprint 3`, `Sprint 4` nằm ngay dưới thư mục gốc); Claude không tạo / di chuyển thư mục.
- FSD lên phiên bản mới → đẩy bản mới vào thư mục user chọn; bản cũ trên Drive để nguyên (user tự dọn).
- Hiện tại: **Sprint 3 đã xong (BBA-40…44, bản Markdown ở `Document/FSD/Sprint 3/`), đang làm Sprint 4.**
- Định dạng Word (`project.json` › `docx_style`): Arial 10; giãn dòng 1.5; thụt đầu dòng đoạn văn 0.5" (1,27 cm); bảng kẻ khung đơn 0.5 pt toàn bộ, hàng tiêu đề nền xám nhạt in đậm, lặp lại khi sang trang; chữ trong bảng giãn dòng 1.0; A4.
