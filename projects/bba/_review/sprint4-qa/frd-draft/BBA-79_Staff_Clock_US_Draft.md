# [Nháp] BBA-79 Staff clock-in / out — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + **câu trả lời của BBA (Plane BBA-528)** + SRS Daily Operations, Attendance App + prototype SMS `/operations/staff-attendance`.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-79/wireframe.html`.

**Thay đổi chính so với bản trên Drive (theo BBA-528)**
1. Chấm công **chỉ trên Attendance app ở iPad cổng, có chụp ảnh**; ngoại lệ là **CD app**. **Bỏ chấm công trên SMS web** (SMS web chỉ xem và sửa).
2. Ghi **nguồn** của mỗi lượt (Attendance app / CD app).
3. **Centre Director** theo dõi và sửa chấm công.
4. HQ staff và khách chấm như **khách** (luồng Visitors), ghi mục đích.
5. Không ghi giờ nghỉ giữa ca.
6. **Bỏ** "On leave" và "Staff on site · Children still in" — BBA không yêu cầu; nghỉ phép nhân viên ngoài Phase 1.
7. Thông báo cho CD lúc giờ cấu hình (ví dụ 10:00) nếu có nhân viên vắng — BBA ghi "Possibly" → OQ-05.

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Phase 1 là chấm công **tối thiểu**: nhân viên báo có mặt, đo nhiệt độ, cần báo cáo (Q-90-05) — khớp.
- Trong file các câu Q-90-07, 08, 09, 10 chưa phản hồi; Q-90-09 (ai sửa) đã có câu trả lời trên Plane BBA-528: CD sửa.
- Trùng lượt offline / web: DOTB tự quyết (Q-90-12) — không còn chấm công trên web nên không phát sinh.

---

## US-001 - Chấm công vào / ra của nhân viên

#### User Story

*(sửa)* Là Centre Director, tôi muốn thấy trong ngày nhân viên nào đã vào, đã ra, chưa chấm công, kèm ảnh và nhiệt độ lúc vào, và sửa khi nhân viên quên chấm công, để biết chắc ai đang có mặt ở Centre.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | Nhân viên chấm công vào trên Attendance app ở iPad cổng: chọn tên mình (chỉ nhân viên của Centre), nhiệt độ (bắt buộc, cùng bộ chọn và ngưỡng sốt như trẻ), chụp ảnh (bắt buộc); giờ là giờ hiện tại. Centre Director chấm công được trên CD app. |
| FR-002 *(sửa)* | Nhân viên chấm công ra trên Attendance app ở iPad cổng (hoặc CD app với Centre Director): chụp ảnh; giờ là giờ hiện tại; không cần nhiệt độ. Nhân viên đã chấm vào thì thấy "Clock out" thay cho "Clock in". |
| FR-003 *(sửa)* | Màn Staff attendance (SMS web) theo Centre và ngày: ảnh, tên, vai trò, giờ vào, giờ ra, nhiệt độ, nguồn (Attendance app / CD app), trạng thái (On site, Clocked out, Not clocked in); đầu màn có số On site, Clocked out, Not clocked in. SMS web không có nút chấm công. |
| FR-004 *(bỏ)* | ~~Đánh dấu nhân viên "On leave" trong ngày.~~ Lý do: BBA không yêu cầu; nghỉ phép nhân viên ngoài Phase 1. |
| FR-005 *(bỏ)* | ~~"Staff on site" cạnh "Children still in".~~ Lý do: BBA không yêu cầu; tỷ lệ giáo viên / trẻ chưa có quy định. |
| FR-006 *(sửa)* | Nhân viên quên chấm công ra (hoặc vào): Centre Director chọn "Correct" trên SMS web, nhập giờ và lý do bắt buộc; lịch sử lưu giá trị cũ, giá trị mới, lý do, người sửa, thời điểm. |
| FR-007 *(sửa)* | Nhiệt độ từ ngưỡng sốt trở lên (theo quốc gia, mặc định 37,5 °C) hiện nổi bật trên màn Staff attendance; Centre Director nhận thông báo trong app. |
| FR-008 | Tìm theo tên nhân viên; lọc theo Centre, ngày, vai trò, trạng thái, nguồn; xuất báo cáo chấm công theo khoảng ngày ra Excel. |
| FR-009 | Một nhân viên chỉ ở trạng thái On site tại một Centre trong cùng lúc; muốn chấm công vào Centre khác phải chấm công ra trước. |
| FR-010 *(mới)* | HQ staff và khách không chấm công ở màn Staff; họ đăng ký qua Visitors trên Attendance app, ghi mục đích đến. |
| FR-011 *(mới)* | Chấm công trên iPad vẫn dùng được khi mất mạng; dữ liệu đồng bộ khi có mạng lại (SRS BR-ATT-030). |

#### Functional Flow - Main (Luồng chính)

1. *(sửa)* Nhân viên đến Centre, chọn tên trên iPad cổng, đo nhiệt độ, chụp ảnh, chọn Clock in (FR-001).
2. *(sửa)* Centre Director xem màn Staff attendance: ai On site, ai chưa chấm công (FR-003).
3. *(sửa)* Cuối ngày, nhân viên chụp ảnh và chọn Clock out trên iPad (FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. *(sửa)* Nhân viên quên chấm công ra: Centre Director sửa có lý do (FR-006).
2. *(mới)* Centre Director chấm công trên CD app (FR-001).
3. *(mới)* HQ staff đến Centre: đăng ký như khách, ghi mục đích (FR-010).
4. *(mới)* Nhân viên có nhiệt độ cao lúc vào: Centre Director nhận thông báo (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không ghi nhiệt độ khi vào ca: không lưu (VAL-001).
2. Giờ ra trước giờ vào: không lưu (VAL-002).
3. Chấm công vào khi đang On site ở Centre khác: không lưu (VAL-003).
4. Sửa giờ không có lý do: không lưu (VAL-004).
5. *(mới)* Không chụp ảnh: không lưu (VAL-005).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Nhiệt độ của nhân viên được ghi khi chấm công vào. |
| BR-002 *(sửa)* | Chỉ Centre Director sửa giờ chấm công; sửa phải có lý do và giữ lịch sử. |
| BR-003 *(bỏ)* | ~~"On leave" là đánh dấu trong ngày.~~ (đi cùng FR-004) |
| BR-004 *(mới)* | Nhân viên chỉ chấm công trên iPad cổng của Centre (kèm ảnh) hoặc CD app; không chấm trên SMS web hay thiết bị cá nhân. |
| BR-005 *(mới)* | Mọi nhân viên của Centre phải chấm công; không ghi giờ nghỉ giữa ca. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chấm công vào không có nhiệt độ. | Không lưu; hiện "Enter your temperature." |
| VAL-002 | Giờ ra trước giờ vào, hoặc giờ sau thời điểm hiện tại. | Không lưu; hiện "Check the time." |
| VAL-003 | Nhân viên đang On site ở Centre khác. | Không lưu; hiện "You are still clocked in at" kèm tên Centre, ". Clock out there first." |
| VAL-004 | Sửa giờ không có lý do. | Không lưu; hiện "Enter a reason." |
| VAL-005 *(mới)* | Chấm công vào / ra không có ảnh. | Không lưu; hiện "Take a photo to continue." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Who are you? *(mới)* | Danh sách chọn (iPad) | Có | Trống | — | Nhân viên của Centre. |
| Temperature | Bộ chọn số (iPad) | Có khi vào ca | 36,5 | VAL-001. | FR-007. |
| Photo *(mới)* | Chụp ảnh (iPad / CD app) | Có | — | VAL-005. | FR-001; FR-002. |
| Clock in / Clock out *(sửa)* | Nút (iPad, CD app) | Có | Theo trạng thái nhân viên | VAL-003. | FR-001; FR-002. |
| Bảng nhân viên *(sửa)* | Bảng (SMS web) | Có | Theo tên | — | Cột: Photo, Staff, Clock in, Clock out, Temp, Source, Status (FR-003). |
| Số On site / Clocked out / Not clocked in *(sửa)* | Thẻ số | Có | — | — | FR-003. |
| Correct *(sửa)* | Nút (SMS web) | Centre Director | — | VAL-002; VAL-004. | FR-006. |
| Mark on leave *(bỏ)* | — | — | — | — | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 *(sửa)* | Mỗi lượt chấm công lưu: nhân viên, Centre, giờ vào, giờ ra, nhiệt độ, ảnh vào, ảnh ra, nguồn (Attendance app / CD app), thiết bị, người sửa và lý do khi có sửa. |
| DATA-002 *(bỏ)* | ~~Lưu đánh dấu On leave.~~ |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 *(sửa)* | Aisyah đến Centre lúc 07:42 | Aisyah chọn tên trên iPad cổng, nhập 36,5 °C, chụp ảnh, chọn Clock in | màn Staff attendance hiện Aisyah On site, giờ vào 07:42, 36,5 °C, nguồn Attendance app, có ảnh | FR-001; FR-003; BR-001 |
| AC-002 | Aisyah chấm công vào không nhập nhiệt độ | lưu | không lưu, hiện "Enter your temperature." | VAL-001 |
| AC-003 *(bỏ)* | ~~"Staff on site 6 · Children still in 20"~~ | | | ~~FR-005~~ |
| AC-004 *(bỏ)* | ~~Đánh dấu Chloe On leave~~ | | | ~~FR-004~~ |
| AC-005 *(sửa)* | Aisyah quên chấm công ra hôm qua | Centre Director chọn Correct, nhập giờ ra 18:05 và lý do | giờ ra được lưu; lịch sử ghi giá trị cũ, giá trị mới, lý do, người sửa | FR-006; BR-002 |
| AC-006 | Centre Director sửa giờ không có lý do | lưu | không lưu, hiện "Enter a reason." | VAL-004 |
| AC-007 *(sửa)* | Grace ghi 37,9 °C khi vào ca | lượt chấm công được lưu | nhiệt độ hiện nổi bật trên màn Staff attendance; Centre Director nhận thông báo | FR-007 |
| AC-008 | Siti đang On site ở Damansara | Siti chấm công vào ở Tampines | không lưu, hiện "You are still clocked in at Small Wonder Damansara. Clock out there first." | FR-009; VAL-003 |
| AC-009 | giờ vào 07:45 | Centre Director sửa giờ ra thành 07:00 | không lưu, hiện "Check the time." | VAL-002 |
| AC-010 | Centre Director chọn tháng 10 | chọn xuất | file Excel có mọi lượt chấm công tháng 10 của Centre, có cột nguồn | FR-008; DATA-001 |
| AC-011 *(sửa)* | Aisyah đã chấm công vào lúc 07:42 | Aisyah mở iPad cổng lúc 17:30, chụp ảnh, chọn Clock out | màn Staff attendance hiện Aisyah Clocked out, giờ ra 17:30 | FR-002 |
| AC-012 *(mới)* | Centre Director mở Staff attendance trên SMS web | tìm nút chấm công | không có nút Clock in / Clock out; chỉ có Correct | FR-003; BR-004 |
| AC-013 *(mới)* | Chloe chấm công vào trên CD app | Centre Director mở Staff attendance | dòng Chloe có nguồn "CD app" | FR-001; FR-003 |
| AC-014 *(mới)* | nhân viên chọn Clock in nhưng chưa chụp ảnh | lưu | không lưu, hiện "Take a photo to continue." | VAL-005 |
| AC-015 *(mới)* | nhân viên HQ đến Centre | dùng iPad cổng | đăng ký ở Visitors với mục đích đến; không có trong màn Staff attendance | FR-010 |

#### Dependencies (Phụ thuộc)

Danh sách nhân viên theo Centre (Users & permissions); Attendance app ở cổng (camera, offline); CD app; luồng Visitors; ngưỡng sốt theo quốc gia; thông báo trong app.

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái / Quyết định của BBA |
|---|---|---|
| OQ-01 | Đánh dấu nghỉ hay quản lý phép? | **Đã rõ:** BBA không yêu cầu (BBA-528) → bỏ FR-004 |
| OQ-02 | Tỷ lệ giáo viên / trẻ. | **Đã rõ:** BBA không yêu cầu (BBA-528) → bỏ FR-005 |
| OQ-03 | Nhân viên sốt: chỉ tô nổi bật hay báo CD? | **Đã có trong SRS:** báo Centre Director (SRS Attendance App) |
| OQ-04 | Nhân viên làm ở nhiều Centre trong một ngày; lượt đồng bộ trễ tính On site thế nào? | Mở (Q-90-10) |
| OQ-08 *(mới)* | Một nhân viên có được chấm công nhiều lượt trong ngày (ca gãy) không? | Mở (Q-90-05 chưa trả lời) |
| OQ-09 *(mới)* | Nhiệt độ vượt ngưỡng khi vào ca: chỉ cảnh báo hay chặn vào làm? | Mở (Q-90-07) — FRD đang chỉ cảnh báo và báo CD (SRS) |
| OQ-10 *(mới)* | Quên chấm công ra: hệ thống tự đóng ca, nhắc nhân viên, hay CD sửa hôm sau? | Mở (Q-90-08) — FRD đang để CD sửa |
| OQ-05 *(mới)* | Có làm thông báo cho CD lúc giờ cấu hình (ví dụ 10:00) nếu có nhân viên chưa chấm công không? BBA ghi "Possibly". Giờ đặt ở cấp nào? | Mở |
| OQ-06 *(mới)* | Centre Admin có được sửa chấm công như Centre Director không? | Mở |
| OQ-07 *(mới)* | Ảnh chấm công lưu bao lâu (PDPA)? | Mở |
| AS-04 *(mới)* | Giờ chấm công luôn là giờ hiện tại trên iPad, không sửa tại chỗ; sửa chỉ ở SMS web bởi Centre Director. | Chờ xác nhận |
