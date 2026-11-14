# Brainstorm — BBA-78 Daily routines (web)

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-78 Daily routines (Q-86)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Taidii và file export của BBA có **4 loại: Bottle, Food, Nap, Potty** (Q-86-01) | **Bỏ Mood** đã thêm ở nháp trước → OQ |
| DOTB tự quyết | Trường dữ liệu dùng lại như Taidii (Q-86-02); lỗi từng phần (Q-86-05) | Ghi quyết định DOTB |
| Một phần | Ghi cả lớp: chỉnh ngoại lệ "cả 2" (trước và sau khi lưu) (Q-86-04) | Sửa FR-003; trẻ vắng có áp không → OQ |
| Một phần | Thông báo theo category, có Routines, phụ huynh chọn nhận (Q-86-09) | Sửa FR-012 |
| Chưa phản hồi | Backdated / future (Q-86-06); cài đặt hiện cho phụ huynh (Q-86-08); ghi chú từ gia đình (Q-86-10) | Giữ OQ |


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

## BBA-78 — Routines trên web
**Đã biết**
- Xem theo lớp và ngày: bữa ăn, ngủ, thay tã; mục còn thiếu (SRS DO); ghi một lần cho cả lớp rồi chỉnh từng trẻ (BR-OPS-028); mục bắt buộc theo level, mặc định Infant và Playgroup (BR-OPS-029); phụ huynh chỉ thấy của con mình (BR-OPS-031); báo phụ huynh mỗi ngày một lần khi trả trẻ.
- CD app: Meals, milk, nap, nappy and toilet, **mood**, note from home; ai ghi, lúc nào (SRS CDP).
- **BBA: routines nên chạy được khi mất mạng (Teacher app)** (Plane BBA-494).
- Proto SMS /operations/routines: "Record for the whole class", "Required every day for Infant Playgroup N1 N2 K1 K2", cột Meal, Nap, Nappy and toilet, **Mood**; "Note from home"; mỗi mục "recorded by Grace Tan in the Teacher app", "Change time", "Add another …"; "Nap window 13:00–14:30"; "Parent view…".

**Lệch so với FRD hiện tại**
- FR-001 thiếu **Mood** (có trong SRS CDP và proto).
- FR-007 "Shown to parents" bật / tắt theo loại — SRS không có; proto chỉ có "Parent view…" (xem trước). → OQ.

**Câu hỏi**: OQ-19: Có cần bật / tắt từng loại sinh hoạt cho phụ huynh không, hay phụ huynh thấy tất cả (SRS)?


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 78 Routines | Thêm Mood; OQ bật / tắt cho phụ huynh |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| OQ-19 | 78 | Bật / tắt từng loại routines cho phụ huynh | OQ |

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
