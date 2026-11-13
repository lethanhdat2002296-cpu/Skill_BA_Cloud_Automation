# Brainstorm — BBA-70 Growth — height & weight

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-70 Growth (Q-71)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Term **do HQ đặt theo brand**, Centre không sửa; 4 term, bắt đầu 1/1, ngày đổi theo năm (vd Schoolhouse T1 2/1–15/3, Agape T1 2/1–10/3); nhắc **giữa tháng cuối mỗi term** (Q-71-03) | Sửa FR-001, FR-011 |
| Đã chốt | Đơn vị cm, kg (Q-71-05); **mọi trẻ** của lớp (Q-71-06); một lần mỗi term + **Measurement history** (Q-71-07); Change record có "Updated By" (Q-71-08); Teacher lớp mình, CD và Admin mọi trẻ (Q-71-10) | Khớp / sửa BR-005 |
| DOTB tự quyết | Lưu cả lớp khi có dòng lỗi (Q-71-09) | DOTB: lưu dòng hợp lệ, dòng lỗi giữ lại kèm báo lỗi |
| **Mâu thuẫn** | File Q-71-02 (09/11): **bỏ BMI và percentile, chỉ cần height + weight** ↔ Plane BBA-1059 (13/11): gửi chuẩn biểu đồ SG / MY | Giữ biểu đồ theo Plane; OQ ghi cả hai |
| Chưa phản hồi trong file | Phụ huynh thấy gì (Q-71-11), báo cáo HQ (Q-71-12) | Đã có trả lời trên Plane BBA-1059 Q4, Q5 |


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

## BBA-70 — Growth (chiều cao, cân nặng theo kỳ)
**Đã biết**
- Nhân viên ghi trực tiếp, không duyệt (SRS C&F BR-CHF-026); một màn cho cả lớp; biểu đồ theo đường bách phân vị (SRS C&F mục 2.4).
- **Lịch đo**: 4 kỳ / năm cho mọi brand, riêng Brighton theo học kỳ; **nhắc giữa tháng cuối của mỗi quý (giữa 3, 6, 9, 12) cho mọi brand** (Plane BBA-529).
- **Biểu đồ**: Singapore theo nghiên cứu nhân trắc của Singapore National Healthcare Group Polyclinics; Malaysia theo Child Health Record Book (Plane BBA-1059 Q1). **BBA đã bỏ BMI** (Plane BBA-1059 — "you removed BMI").
- **Trẻ vắng và trẻ tạm nghỉ vẫn có trên màn nhập, có thể tách nhóm riêng** (Q2).
- **Được xoá số đo**; một quyền chung cho thêm / sửa / xoá; hiện giao cho CD, Admin, mọi Teacher (Q3).
- **Phụ huynh thấy ngay khi lưu** (Q4).
- **Báo cáo HQ chỉ cần trạng thái hoàn thành; người dùng CD, Admin, Cluster Head** (Q5).
- Proto SMS Growth: chọn lớp + kỳ ("Term 3 2026"), "Save the whole class", cột Child, Age, Already recorded this term, Height (cm), Weight (kg); "Saving a term that already has an entry overwrites it. Entries appear immediately". Proto Teacher: "Nursery 2 · Term 3 · 12 of 18 recorded", mỗi trẻ "Not recorded yet" / "Recorded · 93 cm · 13.5 kg".

**Lệch so với FRD hiện tại**
- FR-004, FR-008, BR-003 có **BMI** → bỏ BMI.
- OQ-02 (chuẩn biểu đồ), OQ-01 (lịch kỳ đo), OQ-04 (nội dung báo cáo), OQ-05 (nhắc) của FRD → **đã có câu trả lời**, đóng lại.
- FR-002 chỉ trẻ đang học → thêm nhóm "Absent today / Temporary withdrawal".
- Chưa có thao tác **xoá** số đo.

**Giả định / Câu hỏi**
- OQ-08: Brighton đo theo học kỳ — màn nhập của Brighton có 2 kỳ thay vì 4?
- OQ-09: Ai nhận nhắc giữa tháng cuối quý (CD, Admin, giáo viên lớp)?


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 70 Growth | Bỏ BMI; chuẩn biểu đồ SG / MY; lịch 4 kỳ (Brighton học kỳ); nhắc giữa tháng cuối quý; trẻ vắng / tạm nghỉ vẫn trong danh sách; thêm xoá; báo cáo chỉ tỷ lệ hoàn thành, người dùng CD / Admin / Cluster Head; đóng OQ-01, 02, 04, 05 |

## Đề xuất của BA (chưa phải yêu cầu)

- BBA-70: màn nhập tách 2 nhóm "Present today" và "Absent / temporary withdrawal" như BBA gợi ý.

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| OQ-08 | 70 | Kỳ đo của Brighton (học kỳ) | OQ |
| OQ-09 | 70 | Người nhận nhắc đo | OQ |

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
