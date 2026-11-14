# Brainstorm — BBA-76 Centre-brand overview today

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-76 Overview today (Q-80)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Temporary withdrawal: không điểm danh, không tính enrolment number, vẫn trong student list (có tag), **ẩn khỏi Attendance app** (Q-80-01, Q-80-03) | Khớp FR-002 |
| Đã chốt | Điểm danh gắn với **bản ghi enrolment**, không gắn hồ sơ trẻ (Q-80-03) | DATA |
| Đã chốt | "Today" theo Centre hay người xem như nhau (UTC+8) (Q-80-08) | Ghi chú |
| Một phần | 3 stream: Main, Early Intervention (Bright Path), Enrichment; đếm trên overview thế nào chưa rõ (Q-80-09) | OQ |
| Còn mở | Nghỉ phép có trừ khỏi expected không (Q-80-03); realtime (Q-80-04); drill-down (Q-80-07); export (Q-80-11) | Giữ / thêm OQ |


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

## BBA-76 — Tổng quan hôm nay theo Centre / brand
**Đã biết**: Proto SMS /operations có đúng bảng: Centre, Brand, Signed in of expected, Signed out, Still in; dòng tổng "15 of 15 centres · 15 children signed in of 20 expected"; lọc All brands / All centres. Proto CD app: Signed in "68 of 72 expected", Still in the building, Signed out, Not yet in, Absent; "Not in, nothing reported" kèm "Usually arrives by 8:00 am"; theo lớp và tuyến xe (SRS CDP "Today's attendance").
**Lệch**: FRD khớp proto SMS. Tên vai trò "DM" → **Cluster Head** (Plane BBA-524).
**Câu hỏi**: OQ-16: Bảng HQ có cần thêm cột "Not yet in" và "Absent" như CD app không?


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 76 Overview | DM → Cluster Head; OQ cột Not yet in / Absent |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| OQ-16 | 76 | Thêm cột Not yet in, Absent cho bảng HQ | OQ |

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
