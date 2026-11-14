# Brainstorm — BBA-71 Consent status per child

## Cập nhật theo file câu hỏi phản hồi (13/11/2026)

> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.

### BBA-71 Consent (Q-73)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Loại và vòng đời: Privacy policy, Medical authorisation, Media — **một lần lúc nhập học, không hết hạn** (media khác nội dung theo brand); Field trip / learning journey và ad hoc — **theo từng chuyến / sự kiện, có ngày đóng**; Crossroad — **chỉ Singapore, Centre không có sân ngoài trời, gia hạn hằng năm** (Q-73-04, Q-73-12) | Sửa FR-001, FR-007 |
| Đã chốt | **CD tạo consent và gửi theo lớp hoặc cả Centre, có ngày đóng**; GV chỉ thấy lớp mình (Q-73-04); tạo consent phải có **Announcement kèm link**; email chỉ khi người tạo chọn (Q-73-08) | Sửa FR-003; bỏ "email tự động cho phụ huynh chưa có app" |
| Đã chốt | Người nhận mặc định cả hai phụ huynh; mỗi trẻ cấu hình "cả hai" hay "chỉ người liên hệ chính" (Q-73-07) | FR mới |
| Đã chốt | Phụ huynh trả lời trong app → kết quả về SMS và **tự tick Consent trong checklist học sinh** (Q-73-08) | FR mới |
| Đã chốt | Nhiều request mở cùng lúc cho cùng trẻ và loại (mỗi request gắn một sự kiện) (Q-73-14) | Sửa FR-001 |
| Đã chốt | Rút media / data consent bằng văn bản; trẻ không có media consent → chặn hoặc cảnh báo khi tag; Marketing phải biết (Q-73-13) | Khớp BR-005 |
| DOTB tự quyết | Đếm lần nhắc; **thẻ tổng quan "đã trả lời / tổng", bấm vào chỉ hiện người chưa trả lời; bộ lọc consent** (Q-73-10); bằng chứng lưu (Q-73-15) | FR mới (theo mong muốn BBA nêu) |
| Một phần | Form đăng ký cần 2 chữ ký; consent gửi sau cần 1 hay 2 phụ huynh chưa rõ (Q-73-06) | OQ |
| Chưa phản hồi | Nhắc tự động / giới hạn (Q-73-09); phiên bản (Q-73-11) | Q-73-11 đã có Plane BBA-488 (tuỳ từng lần) |


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

## BBA-71 — Consent status theo trẻ, gửi yêu cầu
**Đã biết**
- Consent quản lý ở Communication › Surveys & consents; hồ sơ trẻ chỉ đọc (SRS C&F BR-CHF-010). Giáo viên chỉ đọc (SRS TCH BR-TCH-054).
- Phụ huynh: đồng ý / không đồng ý một lần cho mỗi trẻ, ký khi cần, rút lại khi consent cho phép; giữ cả câu trả lời gốc và việc rút (SRS PAR BR-PAR-036). Nhắc tự động 1 ngày trước hạn (SRS PAR).
- **BBA: danh sách loại consent theo file đính kèm (chưa đọc được); muốn có tuỳ chọn gửi lại consent khi có cập nhật — không phải lần cập nhật nào cũng cần** (Plane BBA-488). Consent hiện thu một lần qua bản khai đăng ký (Plane BBA-492).
- Proto SMS Safety overview › Consent compliance: cột Child, Not sent, Waiting on the parent, Declined or withdrawn; loại consent mẫu "Outings and excursions", "Media release"; "Read from the consents on each child's Documents tab".

**Lệch so với FRD hiện tại**
- FRD cho gửi / nhắc consent ngay trên hồ sơ trẻ; SRS nói hồ sơ trẻ chỉ đọc, gửi ở Surveys & consents → cần chốt nơi thao tác.
- Tên trạng thái FRD (Awaiting reply, Agreed, Declined, Expired, Withdrawn) khác proto (Waiting on the parent; Declined or withdrawn).
- FR-006 "phiên bản mới → Not sent" → BBA muốn **người tạo chọn có yêu cầu đồng ý lại hay không** khi cập nhật.

**Giả định / Câu hỏi**
- AS-04: Khi sửa nội dung consent, người sửa có ô "Ask parents to agree again"; tick thì mọi trẻ về "Not sent" cho bản mới, không tick thì câu trả lời cũ vẫn dùng. → OQ-10.
- OQ-10: Xác nhận cách "retrigger" trên.
- OQ-11: Cần file "Consent Types" BBA đính kèm (Plane BBA-488) để lấy danh sách loại và nội dung.
- OQ-12: Nút gửi / nhắc đặt trên hồ sơ trẻ (theo ticket) hay chỉ ở Surveys & consents (theo SRS)?


## Thay đổi đề xuất cho FRD

| FRD | Thay đổi chính |
|---|---|
| 71 Consent | Tên trạng thái theo proto; tuỳ chọn yêu cầu đồng ý lại; nơi gửi → OQ |

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| AS-04 / OQ-10 | 71 | Tuỳ chọn yêu cầu đồng ý lại khi sửa consent | AS + OQ |
| OQ-11 | 71 | File danh sách loại consent của BBA | OQ |
| OQ-12 | 71 | Gửi consent ở hồ sơ trẻ hay Surveys & consents | OQ |

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
