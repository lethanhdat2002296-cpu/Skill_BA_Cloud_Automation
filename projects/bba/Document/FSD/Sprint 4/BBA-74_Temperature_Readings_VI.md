# Temperature Readings (3 or More per Day)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | BBA-74 Temperature readings (≥3/day) |
| Mã tài liệu | FRD-3.2.1.02_Temperature_Readings |
| Sprint | 4 |
| Phiên bản | 0.3 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 22/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 15/11/2026 | Business Analysis | Bổ sung theo phản hồi của BBA và wireframe. | |
| 0.3 | 22/11/2026 | Business Analysis | Theo format tài liệu đã duyệt: tách 3 User Story (ghi lần đo; cảnh báo sốt và lần đo còn thiếu; xem, sửa lần đo và phụ huynh xem). Bỏ phần không thuộc task: ứng dụng ở cổng khi mất mạng, nhiệt kế Bluetooth, đơn vị °F, xuất Excel. Đối chiếu prototype. | |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Mỗi trẻ được đo nhiệt độ nhiều lần trong ngày, tối thiểu 3 lần: khi đến, trước / sau ngủ trưa và trước khi về; khi thấy trẻ có dấu hiệu bất thường thì đo thêm. Mỗi lần đo ghi giờ và thời điểm đo. Lần đo từ ngưỡng sốt trở lên được đánh dấu và báo ngay cho Centre. Phụ huynh xem các lần đo trong ngày của con ở mục Attendance của Parents App.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS web (Daily Operations › Class attendance): thêm lần đo (nhiệt độ, giờ, thời điểm); nhiệt độ bắt buộc khi nhận trẻ; số lần đo bắt buộc trong ngày và trẻ còn thiếu lần đo; đánh dấu và báo khi trẻ sốt; sửa / xoá lần đo có lý do; phụ huynh xem lần đo trong Attendance. | Ứng dụng điểm danh ở cổng (iPad) và làm việc khi mất mạng. Nhiệt kế Bluetooth (sprint sau). Đơn vị °F. Xuất danh sách nhiệt độ. Hồ sơ sức khoẻ của trẻ (Health). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Teacher, Centre Admin, Centre Director) | Lớp / Centre của mình. | Thêm lần đo; sửa / xoá lần đo có lý do; xem trẻ còn thiếu lần đo. |
| Giáo viên chủ nhiệm, Centre Director | Lớp / Centre của mình. | Nhận thông báo khi trẻ sốt. |
| HQ Admin | Mọi Centre. | Đặt ngưỡng sốt theo quốc gia. |
| Phụ huynh (Parents App) | Con mình. | Xem các lần đo trong ngày ở Attendance. |
| System | Centre được cấp. | Đánh dấu sốt, gửi thông báo, đếm lần đo, lưu lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Class attendance** | Ghi lần đo nhiệt độ | Thêm lần đo cho trẻ: nhiệt độ, giờ, thời điểm; bắt buộc khi nhận trẻ. | BBA-74: US-001 |
| **Class attendance** | Cảnh báo sốt và lần đo còn thiếu | Đánh dấu và báo khi trẻ sốt; đếm lần đo bắt buộc, lọc trẻ còn thiếu lần đo. | BBA-74: US-002 |
| **Class attendance / Parents App** | Xem, sửa lần đo và phụ huynh xem | Xem các lần đo trên bảng điểm danh; sửa / xoá có lý do; phụ huynh xem trong Attendance. | BBA-74: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-74: US-001 - Ghi lần đo nhiệt độ

#### User Story

Là giáo viên, tôi muốn ghi nhanh nhiệt độ của trẻ kèm giờ và thời điểm đo, để Centre có đủ các lần đo trong ngày của từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Người dùng thêm lần đo cho trẻ: nhiệt độ, giờ, thời điểm đo (BR-001, BR-002). |
| FR-002 | Lượt nhận trẻ (Sign in) bắt buộc có nhiệt độ lúc đến (BR-003). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn Add reading ở dòng trẻ trên bảng điểm danh (FR-001).
2. Người dùng chọn thời điểm đo, nhập nhiệt độ, giữ hoặc sửa giờ, chọn Save reading.
3. Bảng điểm danh hiện lần đo mới dạng "36.6°C · On arrival · 08:12" (US-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Khi nhận trẻ, người dùng nhập nhiệt độ ngay trong popup Sign in; lần đo lưu với thời điểm On arrival (FR-002; BR-003).
2. Trẻ có dấu hiệu bất thường: chọn thời điểm Extra và ghi lý do (BR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Nhiệt độ ngoài khoảng cho phép: không lưu (VAL-001).
2. Extra không có lý do: không lưu (VAL-002).
3. Giờ đo trước giờ nhận trẻ hoặc sau hiện tại: không lưu (VAL-003).
4. Sign in không có nhiệt độ: không lưu lượt nhận (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi lần đo gồm nhiệt độ (°C, 1 chữ số thập phân), giờ đo (mặc định giờ hiện tại) và thời điểm đo. Không giới hạn số lần đo trong ngày. |
| BR-002 | Thời điểm đo là một trong: On arrival (khi đến), Before nap (trước ngủ trưa), After nap (sau ngủ trưa), Before pickup (trước khi về), Extra (đo thêm khi thấy bất thường). Extra bắt buộc ghi lý do, ví dụ "trẻ mệt, má đỏ". |
| BR-003 | Nhiệt độ lúc đến là bắt buộc khi nhận trẻ; thiếu nhiệt độ thì không lưu lượt nhận. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Nhiệt độ ngoài khoảng 34.0–42.0 °C. | Không lưu; hiện "Check the temperature." |
| VAL-002 | Thời điểm Extra không có lý do. | Không lưu; hiện "Enter why this extra reading was taken." |
| VAL-003 | Giờ đo trước giờ nhận trẻ hoặc sau giờ hiện tại. | Không lưu; hiện "Check the time." |
| VAL-004 | Sign in không có nhiệt độ. | Không lưu lượt nhận; hiện "Enter the temperature on arrival." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Add a reading (popup) | Prototype: Daily operations › Class attendance › Add reading |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Add a reading · <tên trẻ> | Tiêu đề popup | — | — | — | — |
| Round | Danh sách chọn | Có | Thời điểm bắt buộc tiếp theo chưa đo | — | BR-002. |
| Reason | Ô nhập | Khi Round = Extra | Ẩn | VAL-002. | Lý do đo thêm. |
| Temperature (°C) | Ô số | Có | 36.5 | VAL-001. | Bước 0.1. |
| Time | Giờ | Có | Giờ hiện tại | VAL-003. | HH:mm. |
| Save reading / Close | Nút | — | — | VAL-001; VAL-002; VAL-003. | Lưu lần đo hoặc đóng. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần đo lưu: trẻ, ngày, giờ đo, thời điểm, nhiệt độ, lý do (khi Extra), có sốt hay không, người ghi, thời điểm ghi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan đã được nhận lúc 08:12 | người dùng thêm lần đo Before nap 36.8 °C lúc 12:40 | bảng điểm danh của Ethan có thêm "36.8°C · Before nap · 12:40" | FR-001; BR-001; DATA-001 |
| AC-002 | người dùng chọn Round Extra, để trống lý do | chọn Save reading | không lưu, hiện "Enter why this extra reading was taken." | BR-002; VAL-002 |
| AC-003 | người dùng nhập 44.0 | chọn Save reading | không lưu, hiện "Check the temperature." | VAL-001 |
| AC-004 | Ethan được nhận lúc 08:12 | người dùng nhập giờ đo 07:50 | không lưu, hiện "Check the time." | VAL-003 |
| AC-005 | người dùng nhận Noah, để trống nhiệt độ | chọn Sign in | không lưu lượt nhận, hiện "Enter the temperature on arrival." | FR-002; BR-003; VAL-004 |
| AC-006 | người dùng nhận Noah với 36.6 °C lúc 08:12 | lượt nhận được lưu | Noah có lần đo "36.6°C · On arrival · 08:12" | FR-002; BR-003 |

#### Dependencies (Phụ thuộc)

Nhận trẻ (Sign in) trên Class attendance (BBA-73).

### 6.2 BBA-74: US-002 - Cảnh báo sốt và lần đo còn thiếu

#### User Story

Là giáo viên chủ nhiệm hoặc Centre Director, tôi muốn được báo ngay khi trẻ sốt và biết trẻ nào còn thiếu lần đo, để xử lý kịp và đủ 3 lần đo mỗi ngày.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-003 | Lần đo từ ngưỡng sốt trở lên được đánh dấu trên bảng điểm danh và gửi thông báo trong app (BR-004, BR-005). |
| FR-004 | Bảng điểm danh hiện số lần đã đo trên số lần bắt buộc của mỗi trẻ (BR-006). |
| FR-005 | Người dùng lọc trẻ còn thiếu lần đo bắt buộc trong ngày và thêm lần đo ngay từ danh sách (BR-006). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng lưu lần đo từ ngưỡng sốt trở lên; hệ thống báo "Screening failed at <nhiệt độ>°C — flagged on the class list." và đánh dấu dòng trẻ (FR-003).
2. Giáo viên chủ nhiệm và Centre Director nhận thông báo trong app (FR-003; BR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trước giờ về, người dùng chọn bộ lọc Missing a reading; danh sách hiện trẻ còn thiếu lần đo và thời điểm còn thiếu; người dùng chọn Add reading (FR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngưỡng sốt của quốc gia chưa đặt: dùng mặc định 37.5 °C (BR-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-004 | Ngưỡng sốt là thiết lập theo quốc gia, mặc định 37.5 °C; dùng chung cho trẻ và nhân viên. |
| BR-005 | Lần đo từ ngưỡng sốt trở lên: dòng trẻ trên bảng điểm danh hiện "Screening failed — <ngưỡng>°C or above. Parent to be called and the child isolated."; giáo viên chủ nhiệm và Centre Director nhận thông báo trong app có tên trẻ, nhiệt độ, giờ đo. |
| BR-006 | Mỗi trẻ cần tối thiểu 3 lần đo bắt buộc mỗi ngày: On arrival, After nap, Before pickup. Trẻ còn thiếu là trẻ đang ở trường chưa có lần đo của một thời điểm bắt buộc đã qua. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — cột Screening, bộ lọc nhiệt độ | Prototype: Daily operations › Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Cảnh báo sốt trên dòng trẻ | Thông báo | — | Khi có lần đo ≥ ngưỡng | — | BR-005. |
| x of 3 | Nhãn | — | — | — | Số lần đã đo / số lần bắt buộc (FR-004). |
| Temperature | Bộ lọc | Không | Any | — | Any / Fever today / Missing a reading (FR-005). |
| Thời điểm còn thiếu | Text | — | Khi lọc Missing a reading | — | Ví dụ "Missing: After nap". |
| Add reading | Nút | Theo quyền | — | — | Mở popup của US-001. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi thông báo sốt lưu: trẻ, lần đo, người nhận, thời điểm gửi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | ngưỡng sốt Singapore 37.5 °C | người dùng lưu lần đo 38.2 °C cho Noah | hiện "Screening failed at 38.2°C — flagged on the class list."; dòng Noah hiện cảnh báo sốt | FR-003; BR-004; BR-005 |
| AC-008 | Noah có lần đo 38.2 °C lúc 15:38 | lần đo được lưu | giáo viên chủ nhiệm lớp Sunbeams và Centre Director nhận thông báo có tên Noah, 38.2 °C, 15:38 | FR-003; BR-005; DATA-002 |
| AC-009 | Ethan có On arrival và After nap | người dùng xem bảng điểm danh | dòng Ethan hiện "2 of 3" | FR-004; BR-006 |
| AC-010 | 15:00, Mia đang ở trường, chưa có lần đo After nap | người dùng chọn lọc Missing a reading | Mia có trong danh sách, ghi "Missing: After nap", có nút Add reading | FR-005; BR-006 |
| AC-011 | lần đo 37.4 °C | người dùng lưu | không có cảnh báo sốt | BR-004 |

#### Dependencies (Phụ thuộc)

US-001; thiết lập ngưỡng sốt theo quốc gia (Settings); dịch vụ notification.

### 6.3 BBA-74: US-003 - Xem, sửa lần đo và phụ huynh xem

#### User Story

Là người dùng của Centre, tôi muốn xem và sửa các lần đo của trẻ trong ngày, và phụ huynh xem được các lần đo của con, để thông tin luôn đúng và minh bạch.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Bảng điểm danh hiển thị mọi lần đo trong ngày của từng trẻ (BR-007). |
| FR-007 | Người dùng có quyền sửa hoặc xoá một lần đo, bắt buộc ghi lý do (BR-008). |
| FR-008 | Phụ huynh xem các lần đo trong ngày của con ở mục Attendance của Parents App (BR-009). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Class attendance; cột Screening hiện các lần đo của từng trẻ (FR-006).
2. Phụ huynh mở Attendance trong Parents App, thấy các lần đo trong ngày (FR-008).

#### Functional Flow - Alternative (Luồng thay thế)

1. Ghi nhầm: người dùng chọn lần đo, sửa giá trị hoặc xoá, ghi lý do, lưu (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Sửa / xoá không có lý do: không lưu (VAL-005).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-007 | Mỗi lần đo hiển thị dạng "<nhiệt độ>°C · <thời điểm> · <giờ>", theo thứ tự giờ đo; lần đo từ ngưỡng sốt trở lên in đậm kèm ⚠. |
| BR-008 | Lần đo đã lưu không bị xoá mất: sửa hoặc xoá đều bắt buộc lý do; lịch sử giữ giá trị cũ, giá trị mới, lý do, người sửa, thời điểm. Lần đo bị xoá không còn hiển thị và không tính vào số lần đo. |
| BR-009 | Phụ huynh thấy giờ, thời điểm và nhiệt độ của mỗi lần đo; không thấy lý do sửa và tên người ghi. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-005 | Sửa hoặc xoá lần đo mà để trống lý do. | Không lưu; hiện "Enter a reason for the change." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — cột Screening | Prototype: Daily operations › Class attendance |
| Parents App — Attendance | Parents App |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Screening | Cột | — | "—" khi chưa đo | — | Danh sách lần đo theo BR-007; bấm một lần đo để sửa / xoá (FR-006; FR-007). |
| Edit reading | Popup | — | — | VAL-005. | Như Add a reading, thêm ô Reason (bắt buộc), nút Delete reading. |
| Parents App › Attendance | Section | — | — | — | Các lần đo trong ngày theo BR-009 (FR-008). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi lần sửa / xoá lần đo lưu: lần đo, giá trị cũ, giá trị mới (hoặc đã xoá), lý do, người sửa, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-012 | Ethan có 36.6 °C lúc 08:12 và 36.8 °C lúc 12:40 | người dùng mở Class attendance | cột Screening của Ethan hiện "36.6°C · On arrival · 08:12" rồi "36.8°C · Before nap · 12:40" | FR-006; BR-007 |
| AC-013 | lần đo 37.9 °C ghi nhầm, đúng là 36.9 °C | người dùng sửa thành 36.9, lý do "nhập nhầm" | lần đo hiện 36.9 °C; lịch sử có 37.9 → 36.9, lý do, người sửa | FR-007; BR-008; DATA-003 |
| AC-014 | người dùng xoá một lần đo, để trống lý do | chọn lưu | không lưu, hiện "Enter a reason for the change." | VAL-005 |
| AC-015 | lần đo After nap của Ethan bị xoá | người dùng xem bảng điểm danh | lần đo không còn hiển thị; số lần đo giảm 1 | BR-008 |
| AC-016 | Ethan có 3 lần đo hôm nay | mẹ Ethan mở Attendance trong Parents App | thấy 3 lần đo với giờ, thời điểm, nhiệt độ; không thấy tên người ghi | FR-008; BR-009 |

#### Dependencies (Phụ thuộc)

US-001; Parents App (Attendance).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Phụ huynh có nhận thông báo ngay khi con sốt không, hay chỉ xem trong Attendance? | Centre Director / HQ Ops | Cao | |
| OQ-02 | Trẻ học nửa ngày (không ngủ trưa) cần những lần đo bắt buộc nào? | Centre Director / HQ Ops | Trung bình | |
| OQ-03 | Ngưỡng sốt Singapore và Malaysia có giống nhau không? | HQ Ops | Cao | |
| OQ-04 | Khoảng nhiệt độ hợp lệ khi nhập (đề xuất 34.0–42.0 °C); ngoài khoảng thì chặn hay chỉ cảnh báo? | HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lần đo (Reading) | Một lần đo nhiệt độ của trẻ, có giờ và thời điểm đo. |
| Thời điểm đo (Round) | Lúc đo trong ngày: On arrival, Before nap, After nap, Before pickup, Extra. |
| Ngưỡng sốt | Nhiệt độ từ mức này trở lên được coi là sốt; đặt theo quốc gia. |
| Lần đo bắt buộc | Các thời điểm phải đo mỗi ngày: On arrival, After nap, Before pickup. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Thời điểm đo | On arrival, Before nap, After nap, Before pickup, Extra. | — |
| Ngưỡng sốt | Theo quốc gia, mặc định 37.5 °C. | Settings. |
