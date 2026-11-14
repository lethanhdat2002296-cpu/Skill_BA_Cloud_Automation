# Brainstorm — BBA-68 đến BBA-79 (Health, Consent, Promotion, Daily operations)

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

## 1. Bối cảnh & vấn đề

**Đã biết**
- BBA thay Taidii bằng SMS + 4 app (Attendance iPad ở cổng, Teacher, Centre Director, Parents) — (SRS General; Drive WorkFlow).
- Sprint 4 bắt đầu 23/11/2026; BBA trả lời các câu hỏi đầu vào trước 13/11 để thiết kế (Plane BBA-1058, BBA-1059).
- Vấn đề cụ thể BBA nêu: nhiều Centre quên nhập chiều cao / cân nặng nên portfolio trống → cần danh sách "đã làm / chưa làm" (Plane BBA-1059 Q5).
- Thông tin sức khoẻ do phụ huynh khai trong Parents App; sau mỗi thay đổi phải làm lại Medical Care Assessment và CD xác nhận với phụ huynh mỗi 6 tháng (Plane BBA-1058).

**Chưa biết**
- OQ-01: Thứ tự go-live theo wave Centre (BBA-467 nói "Go-live wave TBC").

## 2. Mục tiêu kinh doanh

**Đã biết**
- Báo cáo HQ cho chiều cao / cân nặng chỉ cần **tỷ lệ hoàn thành** theo Centre, lớp, kỳ; người dùng: CD, Admin, Cluster Head (Plane BBA-1059 Q5).
- Chấm công nhân viên có báo cáo (BBA gửi mẫu báo cáo Taidii — file đính kèm, chưa đọc được) (Plane BBA-528).

**Chưa biết**
- OQ-02: KPI đo được cho nhóm vận hành (ví dụ % trẻ đo đủ nhiệt độ, % lớp ghi đủ routines) — không có trong nguồn.

## 3. Người dùng & vai trò

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

## 4. Phạm vi

| In scope (theo ticket) | Out of scope | Chưa rõ |
|---|---|---|
| 68 Medical alert banner · 69 Allergies list · 70 Growth · 71 Consent theo trẻ · 72 Lên lớp hàng loạt · 73 Ghi người đưa / đón · 74 Nhiệt độ · 75 Cờ đến muộn · 76 Tổng quan hôm nay · 77 Sửa / huỷ điểm danh · 78 Routines trên web · 79 Chấm công nhân viên | Nghỉ phép / phân ca nhân viên (SRS General: HR ngoài Phase 1); ghi giờ nghỉ giữa ca (Plane BBA-528: "Breaks not required") | Theo dõi đánh giá sức khoẻ 6 tháng (Plane BBA-1058, BBA-490) — chưa có ticket riêng; Late pickup (Proto SMS có tab "Late arrival & pickup", SRS không có) |

## 5. Quy trình nghiệp vụ — đối chiếu từng ticket

> Mỗi ticket: **Đã biết** (có nguồn) → **Lệch so với FRD hiện tại** (cần sửa FRD) → **Giả định / Câu hỏi**.

### BBA-68 — Medical alert banner
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

### BBA-69 — Allergies list (nặng nhất lên đầu)
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

### BBA-70 — Growth (chiều cao, cân nặng theo kỳ)
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

### BBA-71 — Consent status theo trẻ, gửi yêu cầu
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

### BBA-72 — Lên lớp hàng loạt
**Đã biết**
- Chạy lên lớp hằng năm: chuyển trẻ sang level kế và lớp đích cho năm học mới, có xem trước và bỏ chọn trẻ học lại (SRS C&F BR-CHF-048).
- Proto: **chưa có màn** lên lớp (Joining & leaving chỉ có Joining, Leaving & transfers, Graduation, Re-enrolment).
- Không có câu trả lời Plane.

**Giả định / Câu hỏi**: giữ OQ-01…05 của FRD hiện tại (duyệt, ngày đầu năm học, trẻ tạm nghỉ, thông báo, K2 tốt nghiệp). Gợi ý: K2 → Graduation đã có trong Joining & leaving (Proto SMS /lifecycle/graduation) → đóng OQ-05 bằng "xử lý ở Joining & leaving › Graduation" sau khi BBA xác nhận.

### BBA-73 — Ghi người đưa / người đón
**Đã biết**
- Khi nhận: chọn từ phụ huynh và danh sách người đón, hoặc **"Someone else" kèm tên và quan hệ** (SRS ATT mục 2.2).
- Khi trả: **chỉ người trong danh sách đã duyệt**; người mới phải được phụ huynh thêm và Centre duyệt trước (SRS DO BR-OPS-004; ATT BR-ATT-005). **Không có người đón một lần** (SRS CDP BR-CDP-025). CD hoặc School Admin duyệt người đón (BR-CDP-024).
- Phụ huynh nhận thông báo mỗi lần nhận / trả (SRS DO BR-OPS-009); thông báo không nhắc cờ muộn hay tên nhân viên ở cổng (SRS ATT BR-ATT-051).
- Proto SMS /operations: cột "Handover" — "Dropped off by —", "Picked up by —"; "Day record in 08:12 · out —".

**Lệch so với FRD hiện tại**
- FR-001 dùng nhãn "Other" + ghi chú → SRS dùng **"Someone else" + tên + quan hệ** (2 trường).
- OQ-01 (cho CD trả trẻ cho người ngoài danh sách) → SRS đã chốt **không** (BR-CDP-025) → đóng OQ, giữ chặn.
- AS-03 (thông báo ghi tên người đưa / đón) — SRS chỉ cấm ghi cờ muộn và tên nhân viên ở cổng; tên người đón không bị cấm → giữ AS.

### BBA-74 — Nhiệt độ (≥ 3 lần / ngày)
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

### BBA-75 — Cờ đến muộn (chỉ nội bộ)
**Đã biết**: giờ chốt theo Centre, mặc định 9:15 (SRS DO BR-OPS-014; ADM BR-ADM-040); chỉ nhân viên thấy (BR-OPS-015; ATT BR-ATT-009, BR-ATT-051). Proto: "Late (staff only)"; tab "Late arrival & pickup".
**Lệch**: FRD khớp SRS. Proto có thêm "late pickup" → OQ-15: có cần cờ đón muộn không (SRS không có)?

### BBA-76 — Tổng quan hôm nay theo Centre / brand
**Đã biết**: Proto SMS /operations có đúng bảng: Centre, Brand, Signed in of expected, Signed out, Still in; dòng tổng "15 of 15 centres · 15 children signed in of 20 expected"; lọc All brands / All centres. Proto CD app: Signed in "68 of 72 expected", Still in the building, Signed out, Not yet in, Absent; "Not in, nothing reported" kèm "Usually arrives by 8:00 am"; theo lớp và tuyến xe (SRS CDP "Today's attendance").
**Lệch**: FRD khớp proto SMS. Tên vai trò "DM" → **Cluster Head** (Plane BBA-524).
**Câu hỏi**: OQ-16: Bảng HQ có cần thêm cột "Not yet in" và "Absent" như CD app không?

### BBA-77 — Sửa điểm danh có lý do
**Đã biết**
- SMS web dùng để **sửa, huỷ (void) và báo cáo** điểm danh (SRS DO BR-OPS-002). Huỷ trực tiếp: Centre Admin, CD, Senior Teacher được giao, bắt buộc lý do (BR-OPS-022, 023); mọi lần huỷ giữ dấu vết (BR-OPS-024).
- iPad: bản ghi chưa đồng bộ được sửa; đã đồng bộ thì khoá, phải gửi yêu cầu huỷ (SRS ATT BR-ATT-017, 019, 020, 021).
- Proto CD: "You void a record yourself — this audit trail is the control. A teacher cannot void; their request arrives in Approvals." Proto SMS: nút trạng thái Present / Absent / On leave / **Void** trên từng dòng.

**Lệch so với FRD hiện tại**
- FRD dùng "Correct" sửa trực tiếp trạng thái / giờ / người. SRS và proto dùng mô hình **Void** (huỷ bản sai rồi ghi lại). Cần chốt: sửa trực tiếp hay chỉ huỷ + ghi lại.
- AS-01 FRD (giáo viên không sửa) khớp SRS (giáo viên gửi yêu cầu huỷ).

**Câu hỏi**: OQ-17: SMS web cho **sửa giờ / người** trực tiếp (có lý do) hay chỉ **Void** rồi ghi lượt mới? OQ-18 (giữ OQ-02 FRD): sửa lùi tối đa bao nhiêu ngày.

### BBA-78 — Routines trên web
**Đã biết**
- Xem theo lớp và ngày: bữa ăn, ngủ, thay tã; mục còn thiếu (SRS DO); ghi một lần cho cả lớp rồi chỉnh từng trẻ (BR-OPS-028); mục bắt buộc theo level, mặc định Infant và Playgroup (BR-OPS-029); phụ huynh chỉ thấy của con mình (BR-OPS-031); báo phụ huynh mỗi ngày một lần khi trả trẻ.
- CD app: Meals, milk, nap, nappy and toilet, **mood**, note from home; ai ghi, lúc nào (SRS CDP).
- **BBA: routines nên chạy được khi mất mạng (Teacher app)** (Plane BBA-494).
- Proto SMS /operations/routines: "Record for the whole class", "Required every day for Infant Playgroup N1 N2 K1 K2", cột Meal, Nap, Nappy and toilet, **Mood**; "Note from home"; mỗi mục "recorded by Grace Tan in the Teacher app", "Change time", "Add another …"; "Nap window 13:00–14:30"; "Parent view…".

**Lệch so với FRD hiện tại**
- FR-001 thiếu **Mood** (có trong SRS CDP và proto).
- FR-007 "Shown to parents" bật / tắt theo loại — SRS không có; proto chỉ có "Parent view…" (xem trước). → OQ.

**Câu hỏi**: OQ-19: Có cần bật / tắt từng loại sinh hoạt cho phụ huynh không, hay phụ huynh thấy tất cả (SRS)?

### BBA-79 — Chấm công nhân viên
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

## 6. Tích hợp & dữ liệu

| Dữ liệu | Nguồn nhập | Nơi dùng | Chiều | Nguồn |
|---|---|---|---|---|
| Health record (dị ứng, bệnh, ghi chú gia đình) | Parents app → chờ CD / Admin đánh giá | Hồ sơ trẻ, danh sách dị ứng, banner, Teacher app | Phụ huynh → SMS | SRS C&F BR-CHF-029; Plane BBA-1058 |
| Chiều cao / cân nặng | Teacher app, SMS web | Hồ sơ trẻ, Parents app, portfolio "About me", báo cáo HQ | Một chiều | Plane BBA-529, BBA-1059 |
| Điểm danh, nhiệt độ, người đưa / đón | Attendance iPad (offline), SMS web | Bảng điểm danh, tổng quan, e-Form 1 (trợ cấp) | iPad → SMS (đồng bộ) | SRS ATT, DO |
| Chấm công nhân viên | Attendance iPad (ảnh), CD app | Staff attendance, báo cáo | Một chiều | Plane BBA-528 |
| Consent | Parents app | Hồ sơ trẻ (chỉ đọc), Consent compliance | Phụ huynh → SMS | SRS C&F BR-CHF-010 |
| Routines | Teacher app (offline nên có), CD app, SMS web | Parents app, báo cáo | Một chiều | SRS DO; Plane BBA-494 |

Định dạng: ngày **DD/MM/YYYY**, tiền SGD / MYR, chưa cần tiếng Mã Lai (Plane BBA-472). Proto dùng ngày ISO (2026-09-17) → wireframe dùng DD/MM/YYYY theo BBA.

## 7. Ràng buộc & rủi ro

| Loại | Nội dung | Mức | Giảm thiểu |
|---|---|---|---|
| An toàn trẻ | Chờ đánh giá mới áp dụng thay đổi sức khoẻ → dị ứng mới chưa hiện cho giáo viên | Cao | OQ-03; đề xuất hiện cảnh báo "chờ đánh giá" ngay |
| An toàn trẻ | Ẩn dữ liệu khi phụ huynh chưa ký (BBA-1058) có thể làm giáo viên không biết dị ứng | Cao | OQ-04 |
| Dữ liệu cá nhân | Ảnh nhân viên khi chấm công; số điện thoại khách (PDPA) | Trung bình | Thời gian lưu chưa chốt (Proto ATT: "treat 90 days as a suggestion"; Plane BBA-493 hỏi lưu 3 năm) |
| Trợ cấp | Sửa / huỷ điểm danh ảnh hưởng e-Form 1 và ngày đi học trong tháng | Trung bình | OQ-17, OQ-18 |
| Phạm vi | FRD 79 có On leave, tỷ lệ giáo viên / trẻ — BBA không yêu cầu | Trung bình | Bỏ hoặc OQ |

## Đề xuất của BA (chưa phải yêu cầu)
- BBA-68: khi phụ huynh thêm dị ứng mới, hiện ngay nhãn "New from the family · waiting for assessment" cho giáo viên (không chờ đánh giá mới thấy).
- BBA-70: màn nhập tách 2 nhóm "Present today" và "Absent / temporary withdrawal" như BBA gợi ý.
- BBA-79: thẻ "Not clocked in by 10:00" trên màn Staff attendance của CD (nếu BBA chốt OQ-21).

## Assumptions & Open Questions

| Mã | Ticket | Nội dung | Loại |
|---|---|---|---|
| OQ-01 | chung | Thứ tự go-live theo wave Centre | OQ |
| OQ-02 | chung | KPI vận hành | OQ |
| AS-01 / OQ-03 | 68 | Nội dung hiện trong lúc chờ đánh giá | AS + OQ |
| OQ-04 | 68, 69 | Phạm vi ẩn dữ liệu khi phụ huynh chưa ký | OQ |
| OQ-05 | 68 | Bước "hoàn tất đánh giá" thuộc ticket nào | OQ |
| AS-02 / OQ-06 | 69 | Trường riêng cho phản ứng, xử trí, nơi để thuốc | AS + OQ |
| AS-03 / OQ-07 | 69 | Bản in chỉ ghi ngày giờ in | AS + OQ |
| OQ-08 | 70 | Kỳ đo của Brighton (học kỳ) | OQ |
| OQ-09 | 70 | Người nhận nhắc đo | OQ |
| AS-04 / OQ-10 | 71 | Tuỳ chọn yêu cầu đồng ý lại khi sửa consent | AS + OQ |
| OQ-11 | 71 | File danh sách loại consent của BBA | OQ |
| OQ-12 | 71 | Gửi consent ở hồ sơ trẻ hay Surveys & consents | OQ |
| AS-05 / OQ-13 | 74 | Số lần đo bắt buộc | AS + OQ |
| OQ-14 | 74 | Ngưỡng sốt đặt ở HQ hay iPad | OQ |
| OQ-15 | 75 | Cờ đón muộn | OQ |
| OQ-16 | 76 | Thêm cột Not yet in, Absent cho bảng HQ | OQ |
| OQ-17 | 77 | Sửa trực tiếp hay Void + ghi lại | OQ |
| OQ-18 | 77 | Sửa lùi tối đa bao nhiêu ngày | OQ |
| OQ-19 | 78 | Bật / tắt từng loại routines cho phụ huynh | OQ |
| AS-06 / OQ-20 | 79 | HQ staff, khách dùng luồng Visitor | AS + OQ |
| OQ-21 | 79 | Thông báo vắng lúc 10:00 | OQ |
| OQ-22 | 79 | Centre Admin có sửa chấm công không | OQ |

## Tóm tắt thay đổi đề xuất cho 12 FRD (chờ user duyệt)

| FRD | Thay đổi chính |
|---|---|
| 68 Medical alert banner | Thay đổi sức khoẻ chỉ áp sau đánh giá của CD / Admin; trạng thái chờ đánh giá; quy tắc phụ huynh chưa ký |
| 69 Allergies list | Bỏ lưu nhật ký in / xuất; Teacher được in / xuất; cột theo chữ phụ huynh ghi (bỏ cột phản ứng / xử trí / EpiPen riêng → OQ) |
| 70 Growth | Bỏ BMI; chuẩn biểu đồ SG / MY; lịch 4 kỳ (Brighton học kỳ); nhắc giữa tháng cuối quý; trẻ vắng / tạm nghỉ vẫn trong danh sách; thêm xoá; báo cáo chỉ tỷ lệ hoàn thành, người dùng CD / Admin / Cluster Head; đóng OQ-01, 02, 04, 05 |
| 71 Consent | Tên trạng thái theo proto; tuỳ chọn yêu cầu đồng ý lại; nơi gửi → OQ |
| 72 Promotion | Giữ; K2 → Graduation (chờ xác nhận) |
| 73 Handover | "Other" → "Someone else" (tên + quan hệ); đóng OQ-01 (không trả cho người ngoài danh sách) |
| 74 Temperature | Ghi rõ "3 lần" là giả định; ngưỡng → OQ |
| 75 Late flag | Không đổi; thêm OQ đón muộn |
| 76 Overview | DM → Cluster Head; OQ cột Not yet in / Absent |
| 77 Correction | OQ sửa trực tiếp vs Void |
| 78 Routines | Thêm Mood; OQ bật / tắt cho phụ huynh |
| 79 Staff clock | Chỉ iPad (ảnh) + CD app, ghi nguồn; bỏ SMS web; CD sửa; bỏ On leave / tỷ lệ (hoặc OQ); HQ staff, khách → Visitor |
