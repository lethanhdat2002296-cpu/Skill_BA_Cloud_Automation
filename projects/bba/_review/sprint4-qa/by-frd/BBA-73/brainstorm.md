# Brainstorm — BBA-73 Handover recording

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-73 Handover (Q-75)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Check-out chỉ người đã duyệt, **không override**; người lạ → Centre gọi phụ huynh, phụ huynh điền đủ thông tin ngay, rồi người đó mới được đón (Q-75-02, Q-75-04) | Sửa FR-004 (hướng dẫn) |
| Đã chốt | Check-in: người giao có thể ngoài danh sách (tài xế xe, người giúp việc) (Q-75-02) | Khớp FR-001 |
| Đã chốt | Xe đưa đón: bộ lọc theo xe chỉ để gom; **check-in / out từng trẻ, ảnh riêng từng trẻ**; người giao là **tài xế**, người nhận về là **phụ xe** (Q-75-10) | **Sửa FR-008** (bỏ nhận cả nhóm) |
| Đã chốt | Parents App hiện **ảnh lúc giao nhận** (Q-81-02) | FR mới: ảnh |
| DOTB tự quyết | Cách hiện ô nhập tay ở check-in (Q-75-02) | DOTB: chỉ hiện khi chọn "Someone else" |
| Chưa phản hồi | Lưu ảnh bao lâu, ai xem (Q-75-12) | OQ |


---

> Bản nháp để review, **chưa đưa lên Drive / Git**. Ngày 13/11/2026.
>
> **Nguồn đã đọc**
> - 13 SRS v0.1 trong `Document/SRS/` — dùng chính: Children & Families (C&F), Daily Operations (DO), Attendance App (ATT), Teacher App (TCH), Centre Director App (CDP), Parents App (PAR), Administration (ADM), General Requirements.
> - Drive › "2. WorkFlow": 5 file Word chỉ chứa link prototype → đã khảo sát: SMS `bba-sms-crm.lovable.app` (/records, /records/allergies + tab Growth, /records/child/…#health, /operations, /operations/staff-attendance, /operations/routines, /operations/safety + Consent compliance), Attendance `bba-attendance-visitor.lovable.app` (/, /queue, /settings, /visitors), Teacher `bba-teacher.lovable.app` (/allergies, /growth, /routines, /students), CD `bba-centre-director.lovable.app` (/attendance, /more/routines, /more/students). 2 file HTML luồng CRM không liên quan nhóm này.
> - Plane: 26 task "BBA input…" trạng thái Done (câu trả lời của BBA trong comment). Liên quan trực tiếp: BBA-1058, BBA-1059, BBA-529, BBA-528, BBA-488, BBA-494, BBA-491, BBA-490, BBA-472, BBA-524, BBA-512, BBA-492.
> - 12 FRD hiện tại trên Drive (= Git, không ai sửa sau 12/11): `3.1_Medical_Alert_Banner_VI`, `BBA-69` … `BBA-79`.
>
> **Ký hiệu nguồn**: `SRS C&F BR-CHF-022`, `Plane BBA-528`, `Proto SMS /operations`, `FRD hiện tại FR-xx`.
> **Quy tắc**: không bịa — chỗ nào không có bằng chứng ghi `AS` (giả định tạm) kèm `OQ` (cần BBA chốt).


---

## BBA-73 — Ghi người đưa / người đón
**Đã biết**
- Khi nhận: chọn từ phụ huynh và danh sách người đón, hoặc **"Someone else" kèm tên và quan hệ** (SRS ATT mục 2.2).
- Khi trả: **chỉ người trong danh sách đã duyệt**; người mới phải được phụ huynh thêm và Centre duyệt trước (SRS DO BR-OPS-004; ATT BR-ATT-005). **Không có người đón một lần** (SRS CDP BR-CDP-025). CD hoặc School Admin duyệt người đón (BR-CDP-024).
- Phụ huynh nhận thông báo mỗi lần nhận / trả (SRS DO BR-OPS-009); thông báo không nhắc cờ muộn hay tên nhân viên ở cổng (SRS ATT BR-ATT-051).
- Proto SMS /operations: cột "Handover" — "Dropped off by —", "Picked up by —"; "Day record in 08:12 · out —".

**Lệch so với FRD hiện tại**
- FR-001 dùng nhãn "Other" + ghi chú → SRS dùng **"Someone else" + tên + quan hệ** (2 trường).
- OQ-01 (cho CD trả trẻ cho người ngoài danh sách) → SRS đã chốt **không** (BR-CDP-025) → đóng OQ, giữ chặn.
- AS-03 (thông báo ghi tên người đưa / đón) — SRS chỉ cấm ghi cờ muộn và tên nhân viên ở cổng; tên người đón không bị cấm → giữ AS.


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 73 Handover | "Other" → "Someone else" (tên + quan hệ); đóng OQ-01 (không trả cho người ngoài danh sách) |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |

## Vai trò liên quan (chung cho nhóm BBA-68..79)

| Vai trò | Việc chính trong nhóm ticket này | Hệ thống | Nguồn |
|---|---|---|---|
| Centre Director (CD) | Xác nhận đánh giá sức khoẻ; theo dõi và sửa chấm công nhân viên; huỷ / duyệt huỷ điểm danh; duyệt người đón | SMS web, CD app | Plane BBA-1058, BBA-528; SRS DO BR-OPS-022; SRS CDP BR-CDP-024 |
| School Admin / Centre Admin | Như CD với đánh giá sức khoẻ, in danh sách dị ứng, huỷ điểm danh, duyệt người đón | SMS web | Plane BBA-1058; SRS DO BR-OPS-022 |
| Senior Teacher được CD giao | Duyệt / huỷ điểm danh | SMS web | SRS DO BR-OPS-022 |
| Teacher | Nhập chiều cao / cân nặng cả lớp; ghi routines; đo nhiệt độ; in danh sách dị ứng; gửi yêu cầu huỷ | Teacher app, SMS web | SRS C&F mục 1.4; Plane BBA-1059 Q3, BBA-1058 Q2 |
| Nhân viên ở cổng (dùng iPad chung) | Nhận / trả trẻ, đo nhiệt độ, chấm công | Attendance app | SRS ATT |
| Cluster Head (CH) — trước gọi District Manager | Xem tổng quan nhiều Centre, báo cáo hoàn thành đo | SMS web | Plane BBA-524 ("DM will now be known as Cluster Heads"); BBA-1059 |
| HQ Admin | Cài đặt ngưỡng sốt, giờ chốt muộn, mục routines bắt buộc | SMS web | SRS ATT §2; SRS ADM BR-ADM-040 |
| Phụ huynh | Khai sức khoẻ, người đón; trả lời consent; xem số đo, nhiệt độ, routines | Parents app | SRS PAR |
| HQ staff, khách | Chấm công như khách, ghi mục đích | Attendance app | Plane BBA-528 |
