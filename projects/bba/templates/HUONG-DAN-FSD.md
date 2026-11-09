# Hướng dẫn viết FSD — chỉ dùng cho dự án BBA

Quy tắc riêng của BBA, **thắng** quy tắc chung của repo khi khác nhau. Cấu hình máy đọc: `projects/bba/project.json`.

## 1. Tài liệu chính
- **FSD (FRS) là tài liệu khách xác nhận.** SRS của BBA chỉ là Scope & Flow (đầu vào), không viết lại SRS theo chuỗi `srs-pipeline`.
- Không chạy `brainstorm` / `write-urd` / `write-srs` / `srs-pipeline` cho BBA trừ khi user yêu cầu rõ.
- Ngôn ngữ FSD (user chốt 09/11/2026): **viết bản tiếng Việt trước** (`<file>_VI.md`), xuất Word và đẩy Drive cho user duyệt; **chỉ khi user OK mới dịch sang tiếng Anh** (`<file>.md`, bản gửi khách — khác nhau thì bản Anh thắng). Tài liệu nội bộ (tóm tắt, workflow, brainstorm): tiếng Việt.
- Bản tiếng Việt: H1 = `<Feature> (Tiếng Việt)`; mã (FR/BR/VAL/DATA/AC/OQ) và thuật ngữ hệ thống giữ tiếng Anh; tiêu đề mục song ngữ `Acceptance Criteria (Tiêu chí nghiệm thu)` (check_fsd chấp nhận). Bản Anh dịch giữ nguyên mọi mã, số lượng mã hai bản bằng nhau. Word của file `_VI` tự đặt ngôn ngữ vi-VN.
- Chỉ dùng dữ kiện trong SRS / FRS Sprint 3; mỗi FR, BR ghi nguồn (`BR-CHF-017`, `SRS OPS §4 mục 1.1`). Quy tắc BA tự thêm → bảng **Giả định của BA** (`AS-<mã>-xx`) ở mục 7; thiếu thông tin → `OQ-<mã>-xx`. Phân tích trước khi viết: `Document/FSD/Sprint <n>/_brainstorm-sprint-<n>.md`.

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
- Sprint 4 chính thức (user chốt 09/11/2026, theo ảnh WBS): 5 FRD — 2.3 Enquiry actions, 2.8 CRM Administration (CRM SRS); 3.1 Children & families, 3.2 Daily operations, 3.6 Finance (SMS SRS). Mỗi feature WBS một FRD: `Document/FSD/Sprint 4/<WBS>_<Feature_Name>[_VI].md`, H1 = `<WBS> <Feature>` → Drive `[FRD] <H1> - Sprint 4.docx`. Đổi tên theo mã ticket khi user cung cấp.
- Bảng thuộc tính đầu tài liệu có dòng `| Sprint | 4 |` (trùng thư mục `Sprint <n>` chứa file).

## 4. Xuất bản và Google Drive
```bash
python tools/check_fsd.py bba "FSD/Sprint 4/<file>.md"                              # ERROR phải sửa hết trước khi xuất (chạy cả bản _VI; số mã hai bản phải bằng nhau)
python .claude/skills/write-srs/scripts/to_docx.py bba --src "FSD/Sprint 4/<file>.md"   # Word theo docx_style của project.json
python .claude/skills/drive-sync/scripts/drive_pack.py bba                              # kế hoạch đẩy + gợi ý thư mục
```
- FSD lưu trong Git: Sprint 3 `Document/FSD/Sprint 3/BBA-xx-<WBS>_<Feature_Name>_v<x.y>.md`; Sprint 4 theo quy tắc tên ở mục 3 (sprint hiện tại: `project.json` › `sprint.current`).
- **FSD hoàn thành → đẩy Word**, theo `drive-sync`: **hỏi user thư mục đích** mỗi lần. Gợi ý mặc định: thư mục `Sprint <n>` của khách trong https://drive.google.com/drive/folders/199Zxc2yR_lxpasyaNkvo3db7vqKIIEyW (`project.json` › `drive.folder_hints`). Tên trên Drive: `[FRS] BBA-xx-<WBS>_<Feature_Name>_v<x.y>.docx` — giống Sprint 3.
- Drive của BBA giữ nguyên cấu trúc khách đang dùng (`Sprint 3`, `Sprint 4` nằm ngay dưới thư mục gốc); Claude không tạo / di chuyển thư mục.
- FSD lên phiên bản mới → đẩy bản mới vào thư mục user chọn; bản cũ trên Drive để nguyên (user tự dọn).
- Hiện tại: **Sprint 3 đã xong (BBA-40…44, bản Markdown ở `Document/FSD/Sprint 3/`), đang làm Sprint 4.**
- Định dạng Word (`project.json` › `docx_style`): Arial 10; giãn dòng 1.5; thụt đầu dòng đoạn văn 0.5" (1,27 cm); bảng kẻ khung đơn 0.5 pt toàn bộ, hàng tiêu đề nền xám nhạt in đậm, lặp lại khi sang trang; chữ trong bảng giãn dòng 1.0; A4.
- FRD có quy trình nhiều bước: vẽ sơ đồ **BPMN** (`Diagram/Flow/swimlanes/bpmn-<ticket>-<slug>.json`, `notation: bpmn`, render bằng `render-screens/scripts/swimlane.py`) và nhúng vào mục "Process Diagram (Sơ đồ BPMN)" của từng US. Wireframe theo bố cục BeeHive (sidebar, top bar ⌘K, card + filter + bảng + phân trang): mẫu `Diagram/Wireframe/_approvals-sprint4.template.html`, build bằng `_build.py` (đóng gói HTML + chụp PNG đã nén), publish HTML làm link chia sẻ; ảnh PNG nhúng ở mục UI Reference.
