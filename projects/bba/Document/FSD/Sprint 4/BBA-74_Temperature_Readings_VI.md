# Temperature Readings

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | BBA-74 Temperature readings (≥3/day) |
| Mã tài liệu | FRD-3.2.1.02_Temperature_Readings |
| Sprint | 4 |
| Phiên bản | 0.1 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 10/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Mỗi trẻ được đo nhiệt độ nhiều lần trong ngày, tối thiểu 3 lần: khi đến, trước / sau ngủ trưa và trước khi về; khi thấy trẻ có dấu hiệu bất thường thì đo thêm. Lần đo được ghi trên App và hiển thị trên SMS; ngoài ra người dùng có quyền thêm, sửa, xoá lần đo ngay trên SMS. Mỗi lần đo có giờ và thời điểm đo. Phụ huynh xem các lần đo trong ngày của con ở Parent App.

Tài liệu này chỉ mô tả thông tin đo nhiệt độ của trẻ trên SMS.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS (Daily Operations › Class attendance): hiển thị các lần đo nhiệt độ trong ngày của từng trẻ (nhiệt độ, thời điểm, giờ) lấy từ App và từ SMS; số lần đã đo trên số lần bắt buộc; thêm, sửa, xoá lần đo; lịch sử thay đổi. | Đo và nhập nhiệt độ trên App, gồm nhiệt kế Bluetooth. Đồng bộ dữ liệu giữa App và SMS. Phụ huynh xem lần đo (Parent App). Đơn vị °F. Xuất danh sách nhiệt độ. Hồ sơ sức khỏe của trẻ (Health). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Teacher, Centre Admin, Centre Director) | Lớp / Centre của mình. | Xem các lần đo nhiệt độ của trẻ; thêm, sửa, xoá lần đo trên SMS. |
| App (điểm danh / giáo viên) | Centre được cấp. | Đo và ghi lần đo. |
| System | Centre được cấp. | Hiển thị lần đo từ App và SMS, đếm số lần đo, ghi lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Class attendance** | Hiển thị các lần đo trên bảng điểm danh | Mỗi trẻ hiện các lần đo trong ngày và số lần đã đo trên số lần bắt buộc. | BBA-74: US-001 |
| **Class attendance** | Thêm, sửa, xoá lần đo | Người dùng thêm lần đo, sửa hoặc xoá lần đo đã có ngay trên SMS; có lịch sử. | BBA-74: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-74: US-001 - Hiển thị các lần đo trên bảng điểm danh

#### User Story

Là người dùng của Centre, tôi muốn thấy trên bảng điểm danh các lần đo nhiệt độ trong ngày của từng trẻ, để biết trẻ đã được đo những lần nào.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Bảng điểm danh hiển thị các lần đo nhiệt độ trong ngày của từng trẻ, lấy từ App và từ SMS (BR-001, BR-002). |
| FR-002 | Mỗi trẻ hiển thị số lần đã đo trên số lần đo bắt buộc trong ngày (BR-003). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên đo và nhập nhiệt độ trên App, hoặc người dùng thêm trên SMS (US-002).
2. Người dùng mở Daily Operations › Class attendance; cột Screening của mỗi trẻ hiển thị các lần đo trong ngày và "x of 3" (FR-001, FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lần đo được sửa trên App hoặc trên SMS: SMS hiển thị giá trị mới nhất (BR-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa có lần đo nào trong ngày: cột Screening hiện "—".

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | SMS hiển thị lần đo App ghi nhận và lần đo người dùng thêm / sửa trên SMS; luôn hiển thị giá trị mới nhất. Lần đo đã xoá không hiển thị. |
| BR-002 | Mỗi lần đo hiển thị dạng "<nhiệt độ>°C · <thời điểm> · <giờ>", ví dụ "36.6°C · On arrival · 08:12", theo thứ tự giờ đo. Thời điểm đo là một trong: On arrival, Before nap, After nap, Before pickup, Extra. |
| BR-003 | Mỗi trẻ cần tối thiểu 3 lần đo bắt buộc mỗi ngày: On arrival, After nap, Before pickup. "x of 3" đếm số thời điểm bắt buộc đã có lần đo; lần đo Extra không tính vào số này. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — cột Screening | Prototype: Daily operations › Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Screening | Cột | — | "—" khi chưa đo | — | Danh sách lần đo theo BR-002; bấm một lần đo để sửa / xoá (FR-001; US-002). |
| x of 3 | Nhãn | — | — | — | Số lần đo bắt buộc đã có (FR-002; BR-003). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần đo gồm: trẻ, ngày, giờ đo, thời điểm đo, nhiệt độ (°C), lý do (khi Extra), nguồn ghi (App / SMS), người ghi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | App ghi 2 lần đo của Ethan: 36.6 °C On arrival 08:12, 36.8 °C Before nap 12:40 | người dùng mở Class attendance | cột Screening của Ethan hiện "36.6°C · On arrival · 08:12" rồi "36.8°C · Before nap · 12:40" | FR-001; BR-002; DATA-001 |
| AC-002 | Ethan có On arrival và After nap | người dùng xem bảng điểm danh | dòng Ethan hiện "2 of 3" | FR-002; BR-003 |
| AC-003 | Ethan có thêm một lần đo Extra | người dùng xem bảng điểm danh | "x of 3" không đổi; lần đo Extra vẫn hiển thị trong cột Screening | BR-002; BR-003 |
| AC-004 | lần đo 37.9 °C của Ethan được sửa thành 36.9 °C trên App | người dùng mở lại Class attendance | cột Screening hiện 36.9 °C | BR-001 |
| AC-005 | Mia chưa có lần đo nào hôm nay | người dùng mở Class attendance | cột Screening của Mia hiện "—", "0 of 3" | FR-001; FR-002 |

#### Dependencies (Phụ thuộc)

App (đo và ghi lần đo); Class attendance.

### 6.2 BBA-74: US-002 - Thêm, sửa, xoá lần đo

#### User Story

Là người dùng của Centre, tôi muốn thêm lần đo nhiệt độ cho trẻ, sửa hoặc xoá lần đo đã có ngay trên SMS, để thông tin đo nhiệt độ luôn đủ và đúng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-003 | Người dùng có quyền thêm lần đo cho trẻ: thời điểm đo, nhiệt độ, giờ đo (BR-004, BR-005, BR-006). |
| FR-004 | Người dùng có quyền sửa hoặc xoá một lần đo đã có, kể cả lần đo App ghi nhận (BR-007). |
| FR-005 | Hệ thống ghi lịch sử mỗi lần thêm, sửa, xoá lần đo (BR-008; DATA-002). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn Add reading ở dòng trẻ (FR-003).
2. Người dùng chọn thời điểm đo, chọn hoặc nhập nhiệt độ, giữ hoặc sửa giờ, chọn Save reading (BR-004, BR-005).
3. Hệ thống lưu, cột Screening hiện lần đo mới và ghi lịch sử (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ có dấu hiệu bất thường: chọn thời điểm Extra và ghi lý do (BR-006).
2. Sửa: người dùng bấm một lần đo trong cột Screening, đổi giá trị, chọn Save (FR-004).
3. Xoá: người dùng bấm một lần đo, chọn Delete reading, xác nhận; lần đo không còn hiển thị và không tính vào "x of 3" (FR-004; BR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Nhiệt độ ngoài thang cho phép: không lưu (VAL-001).
2. Extra không có lý do: không lưu (VAL-002).
3. Giờ đo trước giờ trẻ đến hoặc sau giờ hiện tại: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-004 | Ô nhiệt độ mặc định 36.5 °C, có sẵn dải 36.3–36.7 để bấm nhanh; thang từ 36.0, lên được 39–40 °C, bước 0.1; có nút "Enter manually" để nhập tay. |
| BR-005 | Giờ đo mặc định là giờ hiện tại, sửa được; không trước giờ trẻ đến và không sau giờ hiện tại. |
| BR-006 | Thời điểm Extra bắt buộc ghi lý do đo thêm, ví dụ "trẻ mệt, má đỏ". |
| BR-007 | Người dùng sửa / xoá được mọi lần đo trong phạm vi được cấp, kể cả giá trị App ghi từ nhiệt kế Bluetooth. Lần đo bị xoá không còn hiển thị, không tính vào số lần đo, nhưng vẫn có trong lịch sử. |
| BR-008 | Mỗi lần thêm, sửa, xoá ghi lịch sử: lần đo, giá trị cũ, giá trị mới (hoặc đã xoá), người thực hiện, thời điểm. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Nhiệt độ nhập tay ngoài thang 36.0–40.0 °C. | Không lưu; hiện "Check the temperature." (chờ OQ-01) |
| VAL-002 | Thời điểm Extra không có lý do. | Không lưu; hiện "Enter why this extra reading was taken." |
| VAL-003 | Giờ đo trước giờ trẻ đến hoặc sau giờ hiện tại. | Không lưu; hiện "Check the time." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Add a reading (popup) | Prototype: Daily operations › Class attendance › Add reading |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Add reading | Nút ở dòng trẻ | Theo quyền | — | — | Mở popup thêm lần đo (FR-003). |
| Round | Danh sách chọn | Có | Thời điểm bắt buộc tiếp theo chưa đo | — | On arrival, Before nap, After nap, Before pickup, Extra. |
| Reason | Ô nhập | Khi Round = Extra | Ẩn | VAL-002. | Lý do đo thêm (BR-006). |
| Temperature (°C) | Nút chọn nhanh + bộ chọn | Có | 36.5 | VAL-001. | Dải nhanh 36.3–36.7; bộ chọn 36.0–40.0, bước 0.1; nút "Enter manually" (BR-004). |
| Time | Giờ | Có | Giờ hiện tại | VAL-003. | HH:mm (BR-005). |
| Save reading / Close | Nút | — | — | VAL-001; VAL-002; VAL-003. | Lưu lần đo hoặc đóng. |
| Edit reading | Popup | Theo quyền | Mở khi bấm một lần đo | — | Như Add a reading, có thêm Delete reading (FR-004). |
| Delete reading | Nút | Theo quyền | — | — | Xoá lần đo sau khi xác nhận (BR-007). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi lần thêm, sửa, xoá lưu: lần đo, trẻ, ngày, giá trị cũ, giá trị mới (hoặc đã xoá), người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | Ethan đã đến lúc 08:12, chưa có lần đo After nap | người dùng chọn Add reading, Round After nap, chọn nút 36.6, Save reading | cột Screening có thêm "36.6°C · After nap · <giờ hiện tại>"; lịch sử có dòng thêm | FR-003; FR-005; BR-004; BR-008 |
| AC-007 | người dùng mở Add reading | xem ô Temperature | mặc định 36.5; có các nút 36.3–36.7 và nút "Enter manually" | BR-004 |
| AC-008 | người dùng chọn "Enter manually", nhập 41.5 | chọn Save reading | không lưu, hiện "Check the temperature." | VAL-001 |
| AC-009 | người dùng chọn Round Extra, để trống lý do | chọn Save reading | không lưu, hiện "Enter why this extra reading was taken." | BR-006; VAL-002 |
| AC-010 | Ethan đến lúc 08:12 | người dùng nhập giờ đo 07:50 | không lưu, hiện "Check the time." | BR-005; VAL-003 |
| AC-011 | App ghi lần đo Bluetooth 37.9 °C của Ethan, thực tế là 36.9 °C | người dùng bấm lần đo, sửa thành 36.9, Save | cột Screening hiện 36.9 °C; lịch sử có 37.9 → 36.9, người sửa, thời điểm | FR-004; BR-007; DATA-002 |
| AC-012 | Ethan có lần đo After nap ghi nhầm | người dùng chọn Delete reading, xác nhận | lần đo không còn hiển thị; "x of 3" giảm 1; lịch sử có dòng xoá | FR-004; BR-007; BR-008 |

#### Dependencies (Phụ thuộc)

US-001; giờ trẻ đến (BBA-73).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Nhập tay ngoài thang 36–40 °C thì chặn hay chỉ cảnh báo? | HQ Ops | Trung bình | |
| OQ-02 | Sửa / xoá lần đo trên SMS có cần nhập lý do không; được sửa trong khoảng thời gian nào? | Centre Director / HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lần đo (Reading) | Một lần đo nhiệt độ của trẻ, có giờ và thời điểm đo; ghi trên App hoặc trên SMS. |
| Thời điểm đo (Round) | Lúc đo trong ngày: On arrival, Before nap, After nap, Before pickup, Extra. |
| Ngưỡng sốt | Nhiệt độ từ mức này trở lên được coi là sốt; đặt theo quốc gia. |
| Lần đo bắt buộc | Các thời điểm phải đo mỗi ngày: On arrival, After nap, Before pickup. |
