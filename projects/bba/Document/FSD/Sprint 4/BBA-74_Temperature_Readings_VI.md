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

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Mỗi trẻ được đo nhiệt độ nhiều lần trong ngày, tối thiểu 3 lần: khi đến, trước / sau ngủ trưa và trước khi về; khi thấy trẻ có dấu hiệu bất thường thì đo thêm. Việc đo và nhập nhiệt độ làm trên App; SMS chỉ hiển thị các lần đo App gửi lên. Mỗi lần đo có giờ và thời điểm đo. Lần đo từ ngưỡng sốt trở lên được đánh dấu để Centre thấy ngay. Phụ huynh xem các lần đo trong ngày của con ở Parent App.

Tài liệu này chỉ mô tả thông tin nhiệt độ hiển thị trên SMS; không mô tả việc đo, nhập, sửa hay xoá lần đo.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS (Daily Operations › Class attendance), hiển thị thông tin nhiệt độ từ App: các lần đo trong ngày của từng trẻ (nhiệt độ, thời điểm, giờ, cách đo); số lần đã đo trên số lần bắt buộc; đánh dấu lần đo từ ngưỡng sốt trở lên; lọc trẻ sốt và trẻ còn thiếu lần đo; chi tiết các lần đo trong ngày của một trẻ. | Đo và nhập nhiệt độ (App), gồm nhiệt kế Bluetooth và nhập tay. Thêm, sửa, xoá lần đo trên SMS. Phụ huynh xem lần đo (Parent App). Ứng dụng điểm danh ở cổng (iPad) khi mất mạng. Đơn vị °F. Xuất danh sách nhiệt độ. Hồ sơ sức khỏe của trẻ (Health). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Teacher, Centre Admin, Centre Director) | Lớp / Centre của mình. | Xem các lần đo nhiệt độ của trẻ trên SMS. |
| HQ Admin | Mọi Centre. | Xem; đặt ngưỡng sốt theo quốc gia. |
| App (điểm danh / giáo viên) | Centre được cấp. | Đo, nhập lần đo và gửi lên SMS. |
| System | Centre được cấp. | Nhận lần đo từ App, so ngưỡng sốt, đếm số lần đo, hiển thị. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy thông tin nhiệt độ. |

**Quy tắc chung:** Quyền xem theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Class attendance** | Hiển thị các lần đo trên bảng điểm danh | Mỗi trẻ hiện các lần đo trong ngày từ App và số lần đã đo trên số lần bắt buộc. | BBA-74: US-001 |
| **Class attendance** | Hiển thị cảnh báo sốt và trẻ còn thiếu lần đo | Đánh dấu lần đo từ ngưỡng sốt trở lên; lọc trẻ sốt, trẻ còn thiếu lần đo. | BBA-74: US-002 |
| **Class attendance** | Xem chi tiết lần đo trong ngày | Mở chi tiết một trẻ để xem mọi lần đo trong ngày: giờ, thời điểm, nhiệt độ, cách đo. | BBA-74: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-74: US-001 - Hiển thị các lần đo trên bảng điểm danh

#### User Story

Là người dùng của Centre, tôi muốn thấy trên bảng điểm danh các lần đo nhiệt độ trong ngày của từng trẻ do App gửi lên, để biết trẻ đã được đo những lần nào.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Bảng điểm danh hiển thị các lần đo nhiệt độ trong ngày của từng trẻ, lấy từ App (BR-001, BR-002, BR-003). |
| FR-002 | Mỗi trẻ hiển thị số lần đã đo trên số lần đo bắt buộc trong ngày (BR-004). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên đo và nhập nhiệt độ trên App; App gửi lần đo lên SMS.
2. Người dùng mở Daily Operations › Class attendance; cột Screening của mỗi trẻ hiển thị các lần đo trong ngày và "x of 3" (FR-001, FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lần đo được sửa trên App: SMS hiển thị giá trị mới nhất App gửi lên (BR-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa có lần đo nào trong ngày: cột Screening hiện "—".

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | SMS chỉ hiển thị lần đo App gửi lên; SMS không có thao tác thêm, sửa hay xoá lần đo. Lần đo được sửa trên App thì SMS hiển thị giá trị mới nhất. |
| BR-002 | Mỗi lần đo hiển thị dạng "<nhiệt độ>°C · <thời điểm> · <giờ>", ví dụ "36.6°C · On arrival · 08:12", theo thứ tự giờ đo. Thời điểm đo là một trong: On arrival, Before nap, After nap, Before pickup, Extra. |
| BR-003 | Nhiệt độ hiển thị theo °C, 1 chữ số thập phân. Trên App, nhiệt độ mặc định 36.5, có sẵn dải 36.3–36.7 để bấm nhanh, thang không xuống dưới 36 và lên được 39–40, có nút "Enter manually"; nên giá trị hiển thị trên SMS thường nằm trong khoảng này. |
| BR-004 | Mỗi trẻ cần tối thiểu 3 lần đo bắt buộc mỗi ngày: On arrival, After nap, Before pickup. "x of 3" đếm số thời điểm bắt buộc đã có lần đo; lần đo Extra không tính vào số này. |

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
| Screening | Cột | — | "—" khi chưa đo | — | Danh sách lần đo theo BR-002; chỉ hiển thị (FR-001; BR-001). |
| x of 3 | Nhãn | — | — | — | Số lần đo bắt buộc đã có (FR-002; BR-004). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | SMS nhận từ App cho mỗi lần đo: trẻ, ngày, giờ đo, thời điểm đo, nhiệt độ (°C), cách đo (Bluetooth thermometer / nhập tay), người đo, có phải giá trị đã sửa hay không. SMS không tạo hay sửa dữ liệu này. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | App gửi lên 2 lần đo của Ethan: 36.6 °C On arrival 08:12, 36.8 °C Before nap 12:40 | người dùng mở Class attendance | cột Screening của Ethan hiện "36.6°C · On arrival · 08:12" rồi "36.8°C · Before nap · 12:40" | FR-001; BR-002; BR-003; DATA-001 |
| AC-002 | Ethan có On arrival và After nap | người dùng xem bảng điểm danh | dòng Ethan hiện "2 of 3" | FR-002; BR-004 |
| AC-003 | Ethan có thêm một lần đo Extra | người dùng xem bảng điểm danh | "x of 3" không đổi; lần đo Extra vẫn hiển thị trong cột Screening | BR-002; BR-004 |
| AC-004 | lần đo 37.9 °C của Ethan được sửa thành 36.9 °C trên App | người dùng mở lại Class attendance | cột Screening hiện 36.9 °C | BR-001 |
| AC-005 | người dùng xem cột Screening | tìm thao tác thêm, sửa, xoá lần đo | không có thao tác nào; chỉ hiển thị | BR-001 |
| AC-006 | Mia chưa có lần đo nào hôm nay | người dùng mở Class attendance | cột Screening của Mia hiện "—", "0 of 3" | FR-001; FR-002 |

#### Dependencies (Phụ thuộc)

App (đo và nhập nhiệt độ, gửi lần đo lên SMS); Class attendance.

### 6.2 BBA-74: US-002 - Hiển thị cảnh báo sốt và trẻ còn thiếu lần đo

#### User Story

Là giáo viên chủ nhiệm hoặc Centre Director, tôi muốn thấy ngay trên SMS trẻ nào có lần đo sốt và trẻ nào còn thiếu lần đo, để xử lý kịp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-003 | Lần đo từ ngưỡng sốt trở lên được đánh dấu trên bảng điểm danh (BR-005, BR-006). |
| FR-004 | Người dùng lọc bảng điểm danh theo trẻ có lần đo sốt hôm nay hoặc trẻ còn thiếu lần đo bắt buộc (BR-007). |

#### Functional Flow - Main (Luồng chính)

1. App gửi lên lần đo 38.2 °C của Noah; SMS đánh dấu lần đo và dòng của Noah (FR-003).
2. Người dùng thấy cảnh báo sốt trên dòng Noah ở bảng điểm danh.

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn bộ lọc Temperature › Fever today: bảng chỉ còn trẻ có lần đo sốt hôm nay (FR-004).
2. Người dùng chọn bộ lọc Temperature › Missing a reading: bảng chỉ còn trẻ còn thiếu lần đo bắt buộc, kèm thời điểm còn thiếu (FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngưỡng sốt của quốc gia chưa đặt: dùng mặc định 37.5 °C (BR-005).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Ngưỡng sốt là thiết lập theo quốc gia, mặc định 37.5 °C; dùng chung cho trẻ và nhân viên. |
| BR-006 | Lần đo từ ngưỡng sốt trở lên in đậm kèm ⚠; dòng trẻ hiện "Screening failed — <ngưỡng>°C or above. Parent to be called and the child isolated." |
| BR-007 | Trẻ còn thiếu lần đo là trẻ đang ở trường chưa có lần đo của một thời điểm bắt buộc đã qua; danh sách hiện thời điểm còn thiếu, ví dụ "Missing: After nap". |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — cảnh báo sốt, bộ lọc nhiệt độ | Prototype: Daily operations › Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Cảnh báo sốt trên dòng trẻ | Thông báo | — | Khi có lần đo ≥ ngưỡng | — | BR-006. |
| Temperature | Bộ lọc | Không | Any | — | Any / Fever today / Missing a reading (FR-004). |
| Thời điểm còn thiếu | Text | — | Khi lọc Missing a reading | — | BR-007. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Đọc lần đo theo DATA-001 và ngưỡng sốt theo quốc gia; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | ngưỡng sốt Singapore 37.5 °C; App gửi lên lần đo 38.2 °C của Noah lúc 15:38 | người dùng mở Class attendance | lần đo "38.2°C · … · 15:38" in đậm kèm ⚠; dòng Noah hiện "Screening failed — 37.5°C or above. Parent to be called and the child isolated." | FR-003; BR-005; BR-006 |
| AC-008 | App gửi lên lần đo 37.4 °C | người dùng mở Class attendance | không có cảnh báo sốt | BR-005 |
| AC-009 | Noah có lần đo sốt hôm nay, Ethan không | người dùng chọn Fever today | bảng chỉ còn Noah | FR-004 |
| AC-010 | 15:00, Mia đang ở trường, chưa có lần đo After nap | người dùng chọn Missing a reading | Mia có trong bảng, ghi "Missing: After nap" | FR-004; BR-007 |

#### Dependencies (Phụ thuộc)

US-001; thiết lập ngưỡng sốt theo quốc gia (Settings).

### 6.3 BBA-74: US-003 - Xem chi tiết lần đo trong ngày

#### User Story

Là người dùng của Centre, tôi muốn mở chi tiết một trẻ để xem mọi lần đo trong ngày và cách đo, để đối chiếu khi cần.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Chọn Day record ở dòng trẻ mở chi tiết ngày của trẻ, có bảng mọi lần đo nhiệt độ trong ngày (BR-008). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn Day record ở dòng Ethan (FR-005).
2. Popup hiển thị "Every temperature today (n)" với giờ, thời điểm, nhiệt độ, cách đo của từng lần (BR-008).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lần đo đã được sửa trên App: dòng hiển thị giá trị mới nhất kèm nhãn đã sửa (BR-008).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa có lần đo: bảng hiện "No temperature today."

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Chi tiết ngày hiển thị mọi lần đo trong ngày, theo thứ tự giờ đo, mỗi dòng: Time, Round, °C, Taken by (Bluetooth thermometer hoặc nhập tay, kèm người đo). Giá trị đọc từ nhiệt kế Bluetooth có thể đã được người dùng sửa trên App; khi đó dòng ghi rõ đã sửa. Chi tiết chỉ để xem. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Day record (popup) | Prototype: Class attendance › Day record |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Day record | Nút ở dòng trẻ | — | — | — | Mở chi tiết ngày (FR-005). |
| Every temperature today (n) | Bảng | — | — | — | Cột Time, Round, °C, Taken by (BR-008). |
| Close | Nút | — | — | — | Đóng popup. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Đọc DATA-001; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-011 | Ethan có 2 lần đo bằng Bluetooth thermometer lúc 08:12 và 12:40 | người dùng chọn Day record của Ethan | popup hiện "Every temperature today (2)": 08:12 · On arrival · 36.6 · Bluetooth thermometer; 12:40 · Before nap · 36.8 · Bluetooth thermometer | FR-005; BR-008 |
| AC-012 | lần đo Bluetooth 37.9 °C của Ethan được sửa thành 36.9 °C trên App | người dùng mở Day record | dòng hiện 36.9 kèm nhãn đã sửa | BR-008 |
| AC-013 | Mia được đo bằng cách nhập tay trên App | người dùng mở Day record của Mia | cột Taken by ghi nhập tay kèm tên người đo | BR-008 |

#### Dependencies (Phụ thuộc)

US-001; App.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Phụ huynh có nhận thông báo ngay khi con sốt không, hay chỉ xem trong Parent App? | Centre Director / HQ Ops | Cao | |
| OQ-02 | Trẻ học nửa ngày (không ngủ trưa) cần những lần đo bắt buộc nào? | Centre Director / HQ Ops | Trung bình | |
| OQ-03 | Ngưỡng sốt Singapore và Malaysia có giống nhau không? | HQ Ops | Cao | |
| OQ-04 | Trên App, nhập tay ngoài thang 36–40 °C thì cảnh báo hay chặn? (Ảnh hưởng tới giá trị SMS có thể nhận.) | HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lần đo (Reading) | Một lần đo nhiệt độ của trẻ trên App, có giờ và thời điểm đo; SMS chỉ hiển thị. |
| Thời điểm đo (Round) | Lúc đo trong ngày: On arrival, Before nap, After nap, Before pickup, Extra. |
| Ngưỡng sốt | Nhiệt độ từ mức này trở lên được coi là sốt; đặt theo quốc gia. |
| Lần đo bắt buộc | Các thời điểm phải đo mỗi ngày: On arrival, After nap, Before pickup. |
| Cách đo | Bluetooth thermometer (tự điền vào tablet, sửa được trên App) hoặc nhập tay. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Thời điểm đo | On arrival, Before nap, After nap, Before pickup, Extra. | App. |
| Cách đo | Bluetooth thermometer, nhập tay. | Thiết bị của Centre. |
| Ngưỡng sốt | Theo quốc gia, mặc định 37.5 °C. | Settings. |
