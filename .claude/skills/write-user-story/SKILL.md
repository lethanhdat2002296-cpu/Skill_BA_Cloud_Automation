---
name: write-user-story
description: Biến user story trong URD thành Product Backlog sẵn sàng cho đội phát triển - gom Epic (EP-xx), tách story quá lớn theo mẫu splitting (US-07.1, US-07.2), kiểm INVEST, ước lượng story point (Fibonacci), xếp release (R1 MVP…), phụ thuộc, truy vết UC/FR/SCR, Definition of Ready/Done; xuất backlog.md và backlog.csv để import Jira (Issue Id/Parent) hoặc Google Sheet. Dùng sau write-srs trong srs-pipeline, hoặc khi user yêu cầu "viết user story", "làm backlog", "tách story", "ước lượng story point", "xuất Jira". Keywords - user story, product backlog, epic, INVEST, story splitting, story points, Fibonacci, MoSCoW, release plan, definition of ready, definition of done, Jira CSV import, Scrum. Output outputs/<du-an>/backlog.md + backlog.csv. Không hỏi user.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *)
---

# write-user-story — Product Backlog

URD viết user story **cho khách hàng duyệt** (đủ phạm vi, theo vai trò). Backlog viết lại các story đó **cho đội phát triển làm**: gom epic, cắt nhỏ vừa sprint, ước lượng, xếp thứ tự, gắn FR/SCR. Mã US giữ nguyên từ URD để truy vết.

## Input
- `outputs/<du-an>/URD.md` (bắt buộc), `UC.md` (nếu có), `SRS.md` (nếu có — FR, SCR, BR để ước lượng và viết AC chi tiết).
- `outputs/<du-an>/ui/flows.md` nếu có (màn hình theo luồng).

## Cách làm
1. Đọc `template-backlog.md` (khung) và `references.md` (INVEST, mẫu tách story, thang điểm). Giữ cấu trúc, thay hết `{{…}}`.
2. **Epic (mục 2):** mỗi epic = một năng lực nghiệp vụ trọn vẹn khách nhận ra (thường trùng phân hệ SRS hoặc nhóm UC). Mã `EP-xx`. Mỗi epic có mục tiêu đo được và release dự kiến.
3. **Story (mục 3):** mỗi US chưa bỏ trong URD có trong backlog, cùng mã `US-xx`, nằm dưới đúng một epic.
   - Story statement giữ nghĩa URD; được viết gọn lại.
   - **Acceptance criteria:** lấy từ URD, bổ sung chi tiết hệ thống từ FR tương ứng (thông báo lỗi, giá trị giới hạn) — Given/When/Then, đánh số.
   - **Truy vết:** `UC-xx · FR-xx, FR-yy · SCR-xx` (lấy từ UC.md và dòng "Truy vết" của FR trong SRS; FR nào phục vụ US này).
   - **Story point** Fibonacci 1, 2, 3, 5, 8, 13 theo `references.md` (so với story mốc 3 điểm). Ghi 1 dòng căn cứ (số màn, số quy tắc, tích hợp, model mới).
   - **Story > 8 điểm hoặc không qua INVEST → tách** theo mẫu trong `references.md` (luồng theo lát mỏng end-to-end, biến thể quy tắc, biến thể dữ liệu, đơn giản / phức tạp, CRUD, trì hoãn hiệu năng, spike). Story con mã `US-07.1`, `US-07.2`… có dòng `- **Tách từ:** US-07 — <mẫu tách>`; story gốc giữ heading, thêm `- **Đã tách thành:** US-07.1, US-07.2` và không có story point.
   - **Phụ thuộc:** story phải xong trước (vd. danh mục trước giao dịch, cấu hình trước luồng).
   - **Release:** `R1` (MVP — đủ chạy một luồng end-to-end các story Must), `R2`, … Story `Won't` → `Ngoài phạm vi`.
4. **Kế hoạch phát hành (mục 4):** bảng release → epic → tổng điểm; thứ tự ưu tiên trong release theo phụ thuộc rồi MoSCoW. Không ghi ngày (chưa có velocity) — ghi "velocity giả định" bằng `AS-xx` nếu cần ước số sprint.
5. **DoR / DoD (mục 5):** dùng mặc định trong template, chỉnh theo dự án (Odoo: có module, quyền, dữ liệu mẫu…).
6. **AS/OQ (mục 6):** chỉ AS/OQ mới, đánh tiếp số lớn nhất trong toàn dự án (URD, UC, SRS).

## Kiểm tra + xuất CSV
```bash
python .claude/skills/write-user-story/scripts/backlog_csv.py <du-an>
```
- `ERROR`: US không có trong URD, epic không tồn tại, thiếu AC, story point không thuộc Fibonacci, story chưa tách mà > 13 điểm, mã trùng → sửa.
- `WARN`: US (chưa bỏ) của URD chưa có trong backlog; story 13 điểm (nên tách); FR/SCR trích dẫn không có trong SRS.
- Sinh `backlog.csv` (UTF-8 BOM, mở được bằng Excel / Google Sheet / import Jira). Cột: `Issue Id, Parent, Issue Type, Summary, Description, Priority, Story Points, Labels, Release`. Epic đứng trước story; `Parent` của story = `Issue Id` của epic. Khi import Jira Cloud: map `Issue Id` → Issue ID, `Parent` → Parent, `Release` → Fix Version.

## Cập nhật (srs-update)
US thêm / sửa / bỏ trong URD → sửa đúng story trong backlog.md (`Edit`), story bỏ giữ heading + `**[Đã bỏ — v<ver>]**`; chạy lại `backlog_csv.py`. Không ước lượng lại story không đổi.

## Output
`outputs/<du-an>/backlog.md`, `outputs/<du-an>/backlog.csv`
