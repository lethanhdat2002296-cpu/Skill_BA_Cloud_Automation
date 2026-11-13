# Brainstorm — BBA-77 Attendance correction

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-77 Attendance correction (Q-81)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | **Check-in nhầm phải Void** (gỡ), không dùng check-out để thay (Q-81-01) | OQ-04 trả lời một phần: lượt nhầm → Void |
| Đã chốt | Ai cũng gửi yêu cầu; Admin, CD, Senior Teacher được chỉ định duyệt; chính họ void không cần duyệt (Q-81-03, Q-75-08) | Khớp FR-010, FR-011 |
| Đã chốt | Void check-in đổi trạng thái subsidy và cảnh báo ngày 18; e-Form 1 gửi ECDA ngày có điểm danh thật đầu tiên, lô 12:00 (Q-81-07) | Sửa FR-007 |
| DOTB tự quyết | Bản ghi chưa đồng bộ sửa trên iPad, đã đồng bộ void trên web (Q-81-10) | Khớp BR-005 |
| Còn mở | Sửa sai giờ (không nhầm cả lượt) dùng correction hay void (Q-81-01); danh sách trường được sửa (Q-81-02); reason code (Q-81-05); khoá kỳ (Q-81-09); thông báo phụ huynh (Q-81-08) | Giữ / thêm OQ |


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

## BBA-77 — Sửa điểm danh có lý do
**Đã biết**
- SMS web dùng để **sửa, huỷ (void) và báo cáo** điểm danh (SRS DO BR-OPS-002). Huỷ trực tiếp: Centre Admin, CD, Senior Teacher được giao, bắt buộc lý do (BR-OPS-022, 023); mọi lần huỷ giữ dấu vết (BR-OPS-024).
- iPad: bản ghi chưa đồng bộ được sửa; đã đồng bộ thì khoá, phải gửi yêu cầu huỷ (SRS ATT BR-ATT-017, 019, 020, 021).
- Proto CD: "You void a record yourself — this audit trail is the control. A teacher cannot void; their request arrives in Approvals." Proto SMS: nút trạng thái Present / Absent / On leave / **Void** trên từng dòng.

**Lệch so với FRD hiện tại**
- FRD dùng "Correct" sửa trực tiếp trạng thái / giờ / người. SRS và proto dùng mô hình **Void** (huỷ bản sai rồi ghi lại). Cần chốt: sửa trực tiếp hay chỉ huỷ + ghi lại.
- AS-01 FRD (giáo viên không sửa) khớp SRS (giáo viên gửi yêu cầu huỷ).

**Câu hỏi**: OQ-17: SMS web cho **sửa giờ / người** trực tiếp (có lý do) hay chỉ **Void** rồi ghi lượt mới? OQ-18 (giữ OQ-02 FRD): sửa lùi tối đa bao nhiêu ngày.


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 77 Correction | OQ sửa trực tiếp vs Void |

## 7. Ràng buộc & rủi ro

| Loại | Nội dung | Mức | Giảm thiểu |
|---|---|---|---|
| Trợ cấp | Sửa / huỷ điểm danh ảnh hưởng e-Form 1 và ngày đi học trong tháng | Trung bình | OQ-17, OQ-18 |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| OQ-17 | 77 | Sửa trực tiếp hay Void + ghi lại | OQ |
| OQ-18 | 77 | Sửa lùi tối đa bao nhiêu ngày | OQ |

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
