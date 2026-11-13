# Brainstorm — BBA-74 Temperature readings

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-74 Temperature (Q-76)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Thang không cần dưới 36, phải lên 39–40; **mặc định 36.5, hiện sẵn dải 36.3–36.7 để bấm**; nút ghi **"Enter manually"** (Q-76-05) | Sửa FR-001 |
| Đã chốt | Được sửa số đọc từ nhiệt kế Bluetooth (Q-76-06) | Sửa FR-003 |
| Đã chốt | **Một số Centre** đo 3 lần: arrival, **sau ngủ trưa**, lúc về; CD có nút "add temperature" (Q-81-02) | "3 lần" không bắt buộc mọi Centre → OQ-06 có thêm dữ kiện; "Before nap" → **"After nap"** |
| Còn mở | Nhập tay ngoài khoảng: cảnh báo hay chặn (Q-76-05) | Giữ AS / OQ |


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

## BBA-74 — Nhiệt độ (≥ 3 lần / ngày)
**Đã biết**
- Không giới hạn số lần đo (SRS DO BR-OPS-010); **bắt buộc đo khi nhận trẻ** (SRS ATT BR-ATT-012). Bộ chọn mặc định 36,5 °C, 36–40 °C, nhập tay được (BR-OPS-011). Ngưỡng sốt theo quốc gia, mặc định 37,5 °C, báo giáo viên lớp và CD (BR-OPS-012). Chạy offline (BR-OPS-007).
- Proto SMS: "36.6°C · On arrival · 08:12", "36.8°C · Before nap · 12:40", "Add reading"; tab Health "Temperature log — Flagged at or above 37.5 °C ⚠️ To confirm", nguồn "Bluetooth thermometer", Edit / Delete. Proto Attendance /settings: ngưỡng "When a temperature counts as raised" chỉnh trên iPad.
- Không có câu trả lời Plane.

**Lệch so với FRD hiện tại**
- FR-004 "3 lần bắt buộc: On arrival, Before nap, Before pickup" → SRS chỉ bắt buộc lúc nhận; "≥ 3" chỉ từ tiêu đề ticket → giữ nhưng ghi rõ là giả định.
- Ngưỡng: SRS theo quốc gia (HQ Admin) vs proto chỉnh trên iPad → OQ.

**Giả định / Câu hỏi**
- AS-05: 3 lần bắt buộc theo tiêu đề ticket (On arrival, Before nap, Before pickup); trẻ học nửa ngày chưa rõ. → OQ-13.
- OQ-13: Xác nhận số lần bắt buộc và thời điểm (FRD OQ-02 cũ).
- OQ-14: Ngưỡng sốt đặt ở đâu — HQ theo quốc gia (SRS) hay trên từng iPad (proto)?


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 74 Temperature | Ghi rõ "3 lần" là giả định; ngưỡng → OQ |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| AS-05 / OQ-13 | 74 | Số lần đo bắt buộc | AS + OQ |
| OQ-14 | 74 | Ngưỡng sốt đặt ở HQ hay iPad | OQ |

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
