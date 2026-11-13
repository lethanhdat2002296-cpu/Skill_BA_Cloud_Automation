# [Nháp] BBA-74 Temperature readings (3 or more per day) — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + SRS Daily Operations, Attendance App + prototype SMS (Class attendance, tab Health › Temperature log) và Attendance app (Settings). Không có câu trả lời Plane cho ticket này.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-74/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. **Bắt buộc đo khi nhận trẻ** (SRS Attendance App BR-ATT-012) — thêm FR-011.
2. "3 lần bắt buộc mỗi ngày" chỉ có trong tiêu đề ticket; SRS nói "any number of readings" → ghi rõ là giả định AS-04, chờ OQ-06.
3. Ngưỡng sốt: SRS đặt theo quốc gia (HQ Admin), prototype cho chỉnh trên iPad → OQ-05.

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Bộ chọn: không cần dưới 36, phải lên 39–40; **mặc định 36.5, hiện sẵn dải 36.3–36.7 để bấm**; nút ghi **"Enter manually"** (Q-76-05) → FR-001.
- Được sửa số đọc từ nhiệt kế Bluetooth (Q-76-06) → FR-003.
- **Một số Centre** đo 3 lần: lúc đến, **sau ngủ trưa**, lúc về; CD có nút "add temperature" (Q-81-02) → đổi "Before nap" thành **"After nap"**; số lần bắt buộc vẫn ở OQ-06.
- Nhập tay ngoài khoảng: cảnh báo hay chặn chưa rõ (Q-76-05) → giữ AS-02 / OQ-04.

---

## US-001 - Đo nhiệt độ ít nhất 3 lần mỗi ngày

#### User Story

Là giáo viên, tôi muốn ghi nhanh nhiệt độ của trẻ theo từng thời điểm trong ngày và được hệ thống báo khi trẻ sốt hoặc còn thiếu lần đo, để phát hiện sớm trẻ không khoẻ và báo cho phụ huynh.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | "Add reading" cho mỗi trẻ: nhiệt độ (mặc định 36,5 °C; nút chọn nhanh 36,3 – 36,4 – 36,5 – 36,6 – 36,7; bộ chọn từ 36 đến 40 °C, bước 0,1; nút "Enter manually" để nhập tay), giờ (mặc định hiện tại), thời điểm: On arrival, After nap, Before pickup, Extra. |
| FR-002 | Thời điểm Extra bắt buộc ghi lý do đo thêm (ví dụ "trẻ mệt, má đỏ"). |
| FR-003 *(sửa)* | Nhiệt kế Bluetooth đã kết nối với máy tính bảng tự điền nhiệt độ; nhân viên sửa được giá trị (Q-76-06) và vẫn chọn thời điểm. |
| FR-004 *(sửa)* | Mỗi trẻ cần 3 lần đo trong ngày: On arrival, After nap, Before pickup (giả định AS-04). Bảng điểm danh hiện số lần đã đo trên 3 (ví dụ "2 of 3") và các lần đo dạng "36,6 · On arrival · 08:12". |
| FR-005 | Lần đo từ ngưỡng sốt trở lên (theo quốc gia, mặc định 37,5 °C) hiện nổi bật trên bảng điểm danh; giáo viên chủ nhiệm và Centre Director nhận thông báo trong app có tên trẻ, nhiệt độ và giờ. |
| FR-006 | Trước giờ về, Centre Director thấy danh sách trẻ còn thiếu lần đo bắt buộc trong ngày. |
| FR-007 | Phụ huynh xem trong mục Attendance của Parents App: mỗi lần đo có giờ, thời điểm, nhiệt độ. |
| FR-008 | Sửa hoặc xoá một lần đo phải có lý do; lịch sử giữ giá trị cũ, người sửa, thời điểm. |
| FR-009 | Đo nhiệt độ vẫn dùng được khi ứng dụng điểm danh mất mạng; dữ liệu đồng bộ khi có mạng lại. |
| FR-010 | Xuất danh sách nhiệt độ theo khoảng ngày và lớp ra Excel. |
| FR-011 *(mới)* | Lượt nhận trẻ (Sign in) bắt buộc có nhiệt độ On arrival; thiếu nhiệt độ thì không lưu lượt nhận. |
| FR-012 *(mới)* | Centre Director thêm lần đo cho trẻ bằng nút "Add temperature" (Q-81-02). |

#### Functional Flow - Main (Luồng chính)

1. *(sửa)* Khi nhận trẻ, nhân viên đo và ghi On arrival ngay trong bước Sign in (FR-001, FR-011).
2. Sau giờ ngủ trưa và trước khi về, giáo viên ghi After nap, Before pickup (FR-001, FR-004).
3. Phụ huynh xem các lần đo trong Parents App (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ có dấu hiệu bất thường: ghi Extra kèm lý do (FR-002).
2. Trẻ sốt: hệ thống báo giáo viên chủ nhiệm và Centre Director (FR-005).
3. Ghi nhầm: sửa có lý do (FR-008).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Nhập tay ngoài khoảng cho phép: không lưu (VAL-001).
2. Extra không có lý do: không lưu (VAL-002).
3. Giờ đo trước giờ nhận trẻ hoặc sau hiện tại: không lưu (VAL-003).
4. *(mới)* Sign in không có nhiệt độ: không lưu lượt nhận (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 *(sửa)* | Mỗi trẻ có ít nhất 3 lần đo mỗi ngày đi học (giả định AS-04); không giới hạn số lần đo thêm. |
| BR-002 | Ngưỡng sốt là thiết lập theo quốc gia (mặc định 37,5 °C). |
| BR-003 | Lần đo đã lưu không bị xoá mất; sửa hoặc xoá đều có lý do và lịch sử. |
| BR-004 *(mới)* | Nhiệt độ là bắt buộc khi nhận trẻ (SRS BR-ATT-012). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Nhập tay nhiệt độ ngoài khoảng 34,0–42,0 °C (AS-02). | Không lưu; hiện "Check the temperature." |
| VAL-002 | Thời điểm Extra không có lý do. | Không lưu; hiện "Enter why this extra reading was taken." |
| VAL-003 | Giờ đo trước giờ nhận trẻ hoặc sau thời điểm hiện tại. | Không lưu; hiện "Check the time." |
| VAL-004 *(mới)* | Sign in không có nhiệt độ. | Không lưu lượt nhận; hiện "Enter the temperature on arrival." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Temperature (°C) *(sửa)* | Nút chọn nhanh 36,3–36,7 + bộ chọn 36–40 + "Enter manually" | Có | 36,5 | VAL-001; VAL-004. | Nhiệt kế Bluetooth tự điền, sửa được. |
| When | Nút chọn | Có | Thời điểm còn thiếu sớm nhất | — | On arrival, After nap, Before pickup, Extra. |
| Reason (Extra) | Ô nhập | Khi Extra | Trống | VAL-002. | — |
| Time | Giờ | Có | Hiện tại | VAL-003. | — |
| Số lần đo | Chữ | — | "x of 3" | — | FR-004. |
| Cảnh báo sốt | Khối cảnh báo trong hộp thoại | Khi ≥ ngưỡng | — | — | "Saving notifies the class teacher and the Centre Director." (FR-005). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần đo lưu: trẻ, nhiệt độ, giờ, thời điểm, lý do (Extra), cách nhập (bộ chọn, nhập tay, nhiệt kế), nhân viên, thiết bị. |
| DATA-002 | Mỗi lần sửa / xoá lưu giá trị cũ, giá trị mới, lý do, người sửa, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan vừa được nhận lúc 08:12 | nhân viên ghi 36,6 °C, On arrival | lần đo lưu với giờ 08:12; bảng hiện "1 of 3" | FR-001; FR-004 |
| AC-002 | Aiden đã có On arrival và After nap | giáo viên ghi 37,9 °C, Before pickup | lần đo hiện nổi bật; giáo viên chủ nhiệm và Centre Director nhận thông báo có tên Aiden, 37,9 °C, giờ | FR-005; BR-002 |
| AC-003 | trẻ có dấu hiệu mệt | giáo viên ghi Extra không có lý do | không lưu, hiện "Enter why this extra reading was taken." | FR-002; VAL-002 |
| AC-004 | nhiệt kế đã kết nối | giáo viên đo | nhiệt độ tự điền; giáo viên chọn thời điểm và lưu | FR-003 |
| AC-005 | 16:30, 3 trẻ chưa có Before pickup | Centre Director mở danh sách trẻ thiếu lần đo | thấy 3 trẻ và thời điểm còn thiếu | FR-006; BR-001 |
| AC-006 | Ethan có 3 lần đo trong ngày | phụ huynh mở Attendance | thấy 3 lần đo với giờ, thời điểm, nhiệt độ | FR-007 |
| AC-007 | giáo viên ghi nhầm 37,9 thay vì 36,9 | giáo viên sửa và nhập lý do | giá trị mới được lưu; lịch sử giữ 37,9, lý do, người sửa | FR-008; BR-003; DATA-002 |
| AC-008 | nhân viên nhập tay 3,7 | chọn lưu | không lưu, hiện "Check the temperature." | VAL-001 |
| AC-009 | ứng dụng điểm danh mất mạng | nhân viên ghi nhiệt độ | lần đo được giữ trên máy và lên hệ thống khi có mạng lại | FR-009 |
| AC-010 | Centre Director chọn lớp Sunbeams, tháng 9 | chọn xuất | file Excel có mọi lần đo của lớp trong tháng | FR-010 |
| AC-011 | trẻ được nhận lúc 08:12 | giáo viên ghi lần đo lúc 07:30 | không lưu, hiện "Check the time." | VAL-003 |
| AC-012 *(mới)* | nhân viên nhận Noah ở cổng | chọn Sign in mà không nhập nhiệt độ | không lưu lượt nhận, hiện "Enter the temperature on arrival." | FR-011; BR-004; VAL-004 |

#### Dependencies (Phụ thuộc)

Class attendance và nhận trẻ (BBA-73); ứng dụng điểm danh ở cổng và nhiệt kế kết nối; thiết lập ngưỡng sốt; thông báo trong app; Parents App (Attendance).

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 | Phụ huynh có nhận thông báo ngay khi con sốt không, hay chỉ xem trong Attendance? | Mở — cao |
| OQ-02 | Trẻ học nửa ngày (không ngủ trưa) cần mấy lần đo bắt buộc? | Mở |
| OQ-03 | Nhắc lần đo còn thiếu gửi cho ai và vào giờ nào? | Mở |
| OQ-04 | Khoảng nhiệt độ hợp lệ khi nhập tay? | Mở |
| OQ-05 *(mới)* | Ngưỡng sốt đặt ở đâu: HQ Admin theo quốc gia (SRS) hay chỉnh trên từng iPad (prototype)? | Mở |
| OQ-06 *(mới)* | Số lần đo bắt buộc mỗi ngày: BBA nói **một số Centre** đo 3 lần (lúc đến, sau ngủ trưa, lúc về) (Q-81-02); SRS chỉ bắt buộc khi nhận trẻ. Có cần thiết lập số lần theo Centre không? | Mở — cao |
| AS-01 | Danh sách trẻ thiếu lần đo chỉ hiện cho Centre Director, không gửi thông báo. | Chờ OQ-03 |
| AS-02 | Khoảng hợp lệ khi nhập tay: 34,0–42,0 °C. | Chờ OQ-04 |
| AS-03 | Thời điểm Extra bắt buộc ghi lý do. | — |
| AS-04 *(mới)* | 3 lần đo bắt buộc theo tiêu đề ticket ("3 or more per day"). | Chờ OQ-06 |
