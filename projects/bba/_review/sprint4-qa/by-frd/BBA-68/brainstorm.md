# Brainstorm — BBA-68 Medical alert banner

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-68 Medical alert banner (Q-69)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Cảnh báo **sinh tự động** (Q-69-02); nguồn Health + Allergies SMS và Parents App (Q-69-03) | Khớp |
| Đã chốt | Critical = medical condition hoặc allergy; phụ huynh bỏ đánh dấu được (Q-69-01) | Không sửa định nghĩa critical (theo yêu cầu trước của user) |
| Đã chốt | Không có vai trò nào thiếu quyền Health (Q-69-05) | FR-012 (vai trò bị ẩn) chỉ là cấu hình dự phòng → ghi chú |
| DOTB tự quyết | Thứ tự, độ dài, mở xem toàn bộ (Q-69-06) | Giữ FR-003, FR-010 |
| **Mâu thuẫn** | File Q-69-08 (09/11): sửa trên Parents App **đồng bộ ngay, không duyệt** ↔ Plane BBA-1058 (13/11): **chỉ áp sau khi CD / Admin đánh giá** | Giữ theo Plane; OQ-MAB-09 ghi cả hai nguồn |


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

## BBA-68 — Medical alert banner
**Đã biết**
- Mức độ dị ứng Mild / Moderate / Severe, HQ Admin cấu hình được (SRS C&F BR-CHF-022). Biểu tượng cảnh báo ở mọi nơi có tên trẻ (BR-CHF-024; SRS TCH BR-TCH-014).
- Phụ huynh là nguồn thông tin sức khoẻ; khi phụ huynh đổi thông tin dị ứng, CD, School Admin và giáo viên lớp được báo (SRS C&F BR-CHF-029).
- **BBA trả lời: thay đổi của phụ huynh chỉ có hiệu lực sau khi CD hoặc Admin hoàn tất đánh giá (assessment)** (Plane BBA-1058 Q1).
- **Phụ huynh chưa ký đồng ý (cho hiện tên và ảnh trên danh sách y tế) thì dữ liệu không hiện trong hồ sơ trẻ** (Plane BBA-1058 Q2).
- Proto SMS tab Health: các khối From the family (Allergies, Skin conditions, Respiratory conditions, Note from the family), Note from staff, Attachments, Vaccination record, History, Temperature log, Height and weight by term.

**Lệch so với FRD hiện tại**
- FR-005 "mức cảnh báo được tính lại ngay khi phụ huynh lưu" → mâu thuẫn với Plane BBA-1058: phải chờ CD / Admin hoàn tất đánh giá.
- FRD chưa có trạng thái "đang chờ đánh giá" và chưa có quy tắc "chưa ký đồng ý thì không hiện".

**Giả định / Câu hỏi**
- AS-01: Trong lúc chờ đánh giá, banner và cảnh báo giữ nội dung **đã được xác nhận gần nhất**; hồ sơ trẻ hiện thêm dòng "Update from the family waiting for assessment" cho CD / Admin. → OQ-03.
- OQ-03: Trong lúc chờ đánh giá, nhân viên thấy nội dung cũ, nội dung mới hay cả hai? (Đặc biệt khi phụ huynh **thêm** một dị ứng mới — chờ đánh giá có rủi ro an toàn.)
- OQ-04: "Data will not appear in the child profile" khi phụ huynh chưa ký — áp cho toàn bộ thông tin sức khoẻ hay chỉ tên / ảnh trên danh sách in? Nếu ẩn toàn bộ thì giáo viên không biết trẻ dị ứng.
- OQ-05: Màn / bước "hoàn tất đánh giá" nằm ở ticket nào (Medical Care Assessment form)?


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 68 Medical alert banner | Thay đổi sức khoẻ chỉ áp sau đánh giá của CD / Admin; trạng thái chờ đánh giá; quy tắc phụ huynh chưa ký |

## Đề xuất của BA (chưa phải yêu cầu)

- BBA-68: khi phụ huynh thêm dị ứng mới, hiện ngay nhãn "New from the family · waiting for assessment" cho giáo viên (không chờ đánh giá mới thấy).

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
| AS-01 / OQ-03 | 68 | Nội dung hiện trong lúc chờ đánh giá | AS + OQ |
| OQ-04 | 68, 69 | Phạm vi ẩn dữ liệu khi phụ huynh chưa ký | OQ |
| OQ-05 | 68 | Bước "hoàn tất đánh giá" thuộc ticket nào | OQ |

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
