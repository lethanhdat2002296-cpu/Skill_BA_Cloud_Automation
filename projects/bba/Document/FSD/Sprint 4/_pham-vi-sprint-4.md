# Phạm vi FSD Sprint 4 — BBA

> Tài liệu nội bộ (không đẩy Drive). Nguồn: 13 SRS v0.1 (`Document/SRS/`) trừ phần 5 FRS Sprint 3 đã đặc tả (`Document/FSD/Sprint 3/`).
> Quy ước tạm (user chốt 09/11/2026): mỗi **module** một FSD, tên `[FSD] <Module> - Sprint 4`; mã ticket sẽ đổi khi user có scope chính thức.
> Viết **từng FSD một**: xong → xuất Word → hỏi thư mục Drive → đẩy → FSD tiếp theo.
> Tính năng có phân loại WBS Phase 2 / Phase 3 trong SRS vẫn được đặc tả (user: "tất cả còn lại là Sprint 4") nhưng ghi rõ Phase ở bảng phân rã của FSD.

## 1. Phần đã có ở Sprint 3 (loại trừ)

| FRS Sprint 3 | Tính năng SRS đã phủ | Module |
|---|---|---|
| BBA-40 Inactive Lead | 2.1 Inactivate Lead, View Inactive Lead, Filter (trạng thái Inactive); 2.2 Open Inactive Lead confirmation, View Closed Lead audit history | Lead and Contact Management |
| BBA-41 Centre Sharing | 2.2 Manage Centre Sharing; 2.3 Automatically add Centre from Reference Log, Manually add / Remove shared Centre | Lead and Contact Management |
| BBA-42 Duplicate Detection | 2.1 Duplicate check Lead; 2.3 Create Reference Log for confirmed duplicate (API); 3.1 Duplicate check Enquiry (chặn tạo Enquiry trùng đang hoạt động) | Lead and Contact Management, Enquiry |
| BBA-43 Enquiry Detail Page | 3.2 View Enquiry admissions header, View intake source, View linked Visits / family Visit, View contacting parent, View Enquiry score (để trống) — phần **hiển thị** trang chi tiết | Enquiry and Customer Journey |
| BBA-44 View Timeline | 2.2 View Lead aggregate Activity history; 3.2 View Enquiry Activity history | Lead, Enquiry |

Phần còn lại của các mục trên (vd. 3.2 Assign owner, Update status, Log call, Set self-reported source; Duplicate Activity, Renewal) **thuộc Sprint 4**.

## 2. Danh sách FSD Sprint 4 (thứ tự viết)

| # | FSD | Nguồn SRS | Mục SRS chính | Trạng thái |
|---|---|---|---|---|
| 1 | [FSD] Lead and Contact Management - Sprint 4 | CRM | 4.2 (2.1, 2.2, 2.4), BR-CRM-001–011, 046–050 | **Xong v0.1** — đã lên Drive Sprint 4 |
| 2 | [FSD] Enquiry and Customer Journey - Sprint 4 | CRM | 4.3 (3.1–3.4), BR-CRM-012–022 | Tiếp theo |
| 3 | [FSD] Visits and Events - Sprint 4 | CRM | 4.4 (4.1–4.8), BR-CRM-023–036 | Chưa |
| 4 | [FSD] Waitlist, Registration and Child Record Preparation - Sprint 4 | CRM | 4.5 (5.1–5.6), BR-CRM-037–053 | Chưa |
| 5 | [FSD] Admissions Workspace - Sprint 4 | CRM | 4.1 (1.1–1.2) | Chưa |
| 6 | [FSD] Marketing Dashboard and Reports - Sprint 4 | CRM | 4.6, mục 7, BR-CRM-054–056 | Chưa |
| 7 | [FSD] Notifications and Follow-up Alerts - Sprint 4 | CRM | 4.7, mục 6.1 | Chưa |
| 8 | [FSD] SMS General Requirements - Sprint 4 | SMS 00 | Toàn bộ | Chưa |
| 9 | [FSD] Administration - Sprint 4 | SMS | Toàn bộ | Chưa |
| 10 | [FSD] Children and Families - Sprint 4 | SMS | Toàn bộ | Chưa |
| 11 | [FSD] Joining and Leaving - Sprint 4 | SMS | Toàn bộ | Chưa |
| 12 | [FSD] Daily Operations - Sprint 4 | SMS | Toàn bộ | Chưa |
| 13 | [FSD] Attendance App - Sprint 4 | SMS | Toàn bộ | Chưa |
| 14 | [FSD] Communication - Sprint 4 | SMS | Toàn bộ | Chưa |
| 15 | [FSD] Learning - Sprint 4 | SMS | Toàn bộ | Chưa |
| 16 | [FSD] Fees and Payments - Sprint 4 | SMS | Toàn bộ | Chưa |
| 17 | [FSD] Parents App - Sprint 4 | SMS | Toàn bộ | Chưa |
| 18 | [FSD] Teacher App - Sprint 4 | SMS | Toàn bộ | Chưa |
| 19 | [FSD] Centre Director App - Sprint 4 | SMS (Phase 2 theo SRS) | Toàn bộ | Chưa |

## 3. Quy ước chung khi viết
- Tiếng Anh, khung `templates/template-fsd.md`; mỗi sub-module SRS → một hoặc vài User Story.
- Chỉ đặc tả điều SRS nói; chi tiết SRS chưa có (trường dữ liệu chi tiết, thông báo, link Figma) → Open Questions, không tự đặt số liệu.
- Ghi WBS Phase của từng tính năng; tham chiếu chéo FRS Sprint 3 (BBA-40…44) thay vì đặc tả lại.
