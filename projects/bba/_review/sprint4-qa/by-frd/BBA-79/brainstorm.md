# Brainstorm — BBA-79 Staff clock-in / out

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-79 Staff clock (Q-90)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt (một phần) | Phase 1 chấm công **tối thiểu**: nhân viên báo có mặt, đo nhiệt độ, cần báo cáo (Q-90-05) | Khớp |
| Chưa phản hồi trong file | Nhiều lượt / ngày (Q-90-05); nhiệt độ vượt ngưỡng (Q-90-07); quên clock-out (Q-90-08); ai sửa (Q-90-09); nhiều Centre (Q-90-10) | Q-90-09 đã có Plane BBA-528 (CD sửa); còn lại OQ |
| DOTB tự quyết | Trùng lượt offline / web (Q-90-12) | Không còn web clock (Plane BBA-528) |


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

## BBA-79 — Chấm công nhân viên
**Đã biết**
- **BBA trả lời** (Plane BBA-528):
  - Nhân viên chấm công **chỉ trên Attendance app ở iPad cổng, có chụp ảnh**; **ngoại lệ: CD app**.
  - **Ghi nguồn** (Attendance app hay CD).
  - **Mọi nhân viên Centre** chấm công; **HQ staff và khách** chấm như khách, kèm mục đích.
  - **Không ghi giờ nghỉ giữa ca.**
  - **CD theo dõi và sửa khi cần**; có thể báo CD vào giờ cấu hình (ví dụ 10:00) nếu có nhân viên vắng.
- SRS: nhiệt độ bắt buộc khi chấm công vào, cùng ngưỡng sốt (ATT BR-ATT-012, 038); chặn chấm vào 2 lần; không dùng thiết bị cá nhân (BR-ATT-036); báo CD khi nhân viên sốt.
- Proto SMS /operations/staff-attendance: cột Name, Role, Centre, Clock in, Clock out, Temperature; trạng thái "On site"; "9 on site now".

**Lệch so với FRD hiện tại**
- FR-001 "ứng dụng điểm danh **hoặc SMS web**" → BBA: chỉ iPad cổng + CD app; **bỏ SMS web**, thêm **ảnh** và **nguồn**.
- FR-004 "On leave" và FR-005 "Children still in" (tỷ lệ) → không có trong câu trả lời BBA; nghỉ phép ngoài Phase 1 → đề xuất bỏ, hoặc giữ ở dạng OQ.
- FR-006 "CD / Centre Admin sửa giờ ra" → BBA: **CD** sửa.

**Giả định / Câu hỏi**
- AS-06: HQ staff và khách dùng luồng Visitor sign-in (đã có trong SRS DO), không vào màn Staff attendance. → OQ-20.
- OQ-20: Xác nhận.
- OQ-21: Thông báo vắng mặt cho CD lúc 10:00 — có làm trong Phase 1 không ("Possibly")? Giờ cấu hình ở cấp nào?
- OQ-22: Centre Admin có được sửa chấm công như CD không?


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 79 Staff clock | Chỉ iPad (ảnh) + CD app, ghi nguồn; bỏ SMS web; CD sửa; bỏ On leave / tỷ lệ (hoặc OQ); HQ staff, khách → Visitor |

## Đề xuất của BA (chưa phải yêu cầu)

- BBA-79: thẻ "Not clocked in by 10:00" trên màn Staff attendance của CD (nếu BBA chốt OQ-21).

## 7. Ràng buộc & rủi ro

| Loại | Nội dung | Mức | Giảm thiểu |
|---|---|---|---|
| Dữ liệu cá nhân | Ảnh nhân viên khi chấm công; số điện thoại khách (PDPA) | Trung bình | Thời gian lưu chưa chốt (Proto ATT: "treat 90 days as a suggestion"; Plane BBA-493 hỏi lưu 3 năm) |
| Phạm vi | FRD 79 có On leave, tỷ lệ giáo viên / trẻ — BBA không yêu cầu | Trung bình | Bỏ hoặc OQ |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| AS-06 / OQ-20 | 79 | HQ staff, khách dùng luồng Visitor | AS + OQ |
| OQ-21 | 79 | Thông báo vắng lúc 10:00 | OQ |
| OQ-22 | 79 | Centre Admin có sửa chấm công không | OQ |

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
