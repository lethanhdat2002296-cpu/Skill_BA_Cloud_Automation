# Brainstorm — BBA-69 Allergies list

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-69 Allergies list (Q-70)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Không giới hạn số dị ứng / bệnh (Q-70-02) | BR mới |
| Đã chốt | Thang chính thức trên form: **Mild, Moderate, Life Threatening**; Life Threatening lên đầu; form có thể tuỳ theo brand / Centre (Q-70-03) | Ghi Life Threatening = Severe (giữ tên Severe trên UI); cấu hình theo brand → OQ |
| Đã chốt | **Chưa khai báo ≠ đã khai báo không dị ứng**; Health info bắt buộc; trẻ chưa sinh bỏ qua, hệ thống nhắc admin gần ngày nhập học (Q-70-09) | FR mới: trạng thái "Not provided" |
| Đã chốt | Staff không ghi đè thông tin phụ huynh (Q-70-10) | Khớp BR-001 |
| DOTB tự quyết | Mô hình dữ liệu (Q-70-01), cách sắp xếp (Q-70-04), export / audit (Q-70-11) | DOTB: giữ chữ tự do + mức độ; mỗi trẻ một dòng; không lưu nhật ký (khớp Plane BBA-1058) |
| Chưa phản hồi | Cột Reaction / Action Plan / EpiPen (Q-70-05); condition chung danh sách (Q-70-06); kênh cho bếp (Q-70-07); đồng bộ (Q-70-12) | Giữ OQ |


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

## BBA-69 — Allergies list (nặng nhất lên đầu)
**Đã biết**
- Danh sách theo Centre và lớp; tìm theo tên trẻ, chất gây dị ứng; lọc Centre, lớp, loại (allergy / medical condition / dietary) (SRS C&F mục 2.4). Xuất và in theo lớp cho bếp (SRS C&F).
- Teacher app: cột ảnh, lớp, allergy, severity and reaction, what to do, diet, underlying conditions; trẻ có bệnh nhưng không dị ứng liệt kê riêng (SRS TCH BR-TCH-015).
- Phụ huynh khai dị ứng trong **4 ô chữ tự do** + ghi chú gia đình (SRS C&F BR-CHF-021).
- **BBA: CD, Admin, Teacher được in / xuất; không cần ghi lại ai in / xuất** (Plane BBA-1058 Q2).
- Proto SMS /records/allergies: cột Child, Class, Type, From the family, Note from staff, Vaccination, Updated by the family; nút "Print for the kitchen", "Export (n)"; lọc Centre, Class, Condition type. **Proto không có cột mức độ.**
- Proto Teacher /allergies: chi tiết của gia đình chỉ đọc; nhân viên ghi "Note from staff".

**Lệch so với FRD hiện tại**
- FR-008, BR-004 "lưu người xuất, thời điểm" và BR-003 "bản in ghi người in" → BBA nói **không cần ghi lại** → bỏ phần lưu nhật ký xuất / in.
- FR-001 có cột "phản ứng, cách xử trí, nơi để EpiPen" và FR-006 báo "Chưa có thông tin" → SRS chỉ có 4 ô chữ tự do, không có trường riêng; proto cũng không có. Không đủ bằng chứng để giữ các cột riêng.

**Giả định / Câu hỏi**
- AS-02: Danh sách hiện nguyên văn chữ phụ huynh ghi (không tách phản ứng / xử trí / EpiPen); mức độ hiện cạnh từng dị ứng. → OQ-06.
- OQ-06: Có cần trường riêng cho phản ứng, cách xử trí, nơi để thuốc khẩn cấp không (SRS TCH liệt kê "reaction, what to do")?
- AS-03: Bản in vẫn ghi ngày giờ in ở đầu trang để bếp biết bản mới nhất (không lưu nhật ký). → OQ-07.
- OQ-07: Xác nhận chỉ ghi ngày giờ trên bản in, không ghi tên người in.


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 69 Allergies list | Bỏ lưu nhật ký in / xuất; Teacher được in / xuất; cột theo chữ phụ huynh ghi (bỏ cột phản ứng / xử trí / EpiPen riêng → OQ) |

## 7. Ràng buộc & rủi ro

| Loại | Nội dung | Mức | Giảm thiểu |
|---|---|---|---|
| An toàn trẻ | Chờ đánh giá mới áp dụng thay đổi sức khoẻ → dị ứng mới chưa hiện cho giáo viên | Cao | OQ-03; đề xuất hiện cảnh báo "chờ đánh giá" ngay |
| An toàn trẻ | Ẩn dữ liệu khi phụ huynh chưa ký (BBA-1058) có thể làm giáo viên không biết dị ứng | Cao | OQ-04 |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| OQ-04 | 68, 69 | Phạm vi ẩn dữ liệu khi phụ huynh chưa ký | OQ |
| AS-02 / OQ-06 | 69 | Trường riêng cho phản ứng, xử trí, nơi để thuốc | AS + OQ |
| AS-03 / OQ-07 | 69 | Bản in chỉ ghi ngày giờ in | AS + OQ |

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
