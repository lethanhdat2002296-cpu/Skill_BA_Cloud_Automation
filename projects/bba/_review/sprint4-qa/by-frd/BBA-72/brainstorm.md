# Brainstorm — BBA-72 Bulk class promotion

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-72 Bulk promotion (Q-74)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | 3 luồng khác nhau: **annual promotion** (cuối năm, cả lớp), **Infant promotion** (bất kỳ lúc nào, từng trẻ, 18 tháng tuổi), **class change** (đổi lớp cùng level). **K2 graduation = mass withdrawal** (reason graduation), chỉ K2 rời vào tháng 12 (Q-74-01, Q-74-06) | Ticket này = annual promotion; đóng OQ-05 |
| Đã chốt | Chỉ **trong cùng Centre**; khác Centre / brand là Transfer (Q-74-02) | BR mới |
| Đã chốt | Chọn cả cohort, **bỏ tick ngoại lệ**; trẻ ở lại giữ lớp hoặc chuyển lớp khác cùng level (Q-74-03 / 05) | Khớp FR-003 |
| Đã chốt | Capacity linh hoạt (vd tối đa 24 vẫn nhận em thứ 25); CD cấu hình sĩ số từng lớp (Q-74-08) | Khớp BR-003 |
| Đã chốt | Không void hoá đơn đã phát hành, sửa bằng credit note (Q-74-09) | Khớp BR-002 |
| Đã chốt | Lên lớp → **tạo thread mới** cho lớp mới; thread cũ **chỉ đọc**, giữ tới khi trẻ rời trường (Q-74-10) | Sửa FR-005 |
| DOTB tự quyết | Preview, lỗi từng phần, chạy lại (Q-74-11 / 12 / 13) | Ghi quyết định DOTB |
| Còn mở | Effective date mặc định / huỷ trước hiệu lực (Q-74-07); fee scheme áp từ ngày nào (Q-74-09); roster điểm danh chuyển khi nào (Q-74-10); thông báo, đóng lớp cũ (Q-74-15); trạng thái đủ điều kiện (Q-74-06) | Giữ / thêm OQ |


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

## BBA-72 — Lên lớp hàng loạt
**Đã biết**
- Chạy lên lớp hằng năm: chuyển trẻ sang level kế và lớp đích cho năm học mới, có xem trước và bỏ chọn trẻ học lại (SRS C&F BR-CHF-048).
- Proto: **chưa có màn** lên lớp (Joining & leaving chỉ có Joining, Leaving & transfers, Graduation, Re-enrolment).
- Không có câu trả lời Plane.

**Giả định / Câu hỏi**: giữ OQ-01…05 của FRD hiện tại (duyệt, ngày đầu năm học, trẻ tạm nghỉ, thông báo, K2 tốt nghiệp). Gợi ý: K2 → Graduation đã có trong Joining & leaving (Proto SMS /lifecycle/graduation) → đóng OQ-05 bằng "xử lý ở Joining & leaving › Graduation" sau khi BBA xác nhận.


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 72 Promotion | Giữ; K2 → Graduation (chờ xác nhận) |

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
