# Temperature Readings

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Temperature |
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

Mỗi trẻ được đo nhiệt độ nhiều lần trong ngày, tối thiểu 3 lần bắt buộc: khi đến, sau ngủ trưa và trước khi về; khi thấy trẻ có dấu hiệu bất thường thì đo thêm. Lần đo được ghi trên App và hiển thị trên SMS; ngoài ra người dùng có quyền thêm, sửa, xóa lần đo ngay trên SMS, mỗi thao tác có lý do và được ghi lịch sử. Mỗi lần đo có giờ và thời điểm đo (Round).

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS (Daily Operations › tab Temperature): danh sách lần đo nhiệt độ, mỗi lần đo một dòng (nhiệt độ, Round, giờ đo, lý do đo thêm, nguồn); lọc, tìm kiếm; số lần đã đo trên số lần bắt buộc. Thêm lần đo (trên danh sách hoặc từ dòng điểm danh). Sửa, xóa lần đo; Changelog. Cấu hình danh mục Round. | Đo và nhập nhiệt độ trên App, gồm nhiệt kế Bluetooth. Đồng bộ dữ liệu giữa App và SMS. Phụ huynh xem lần đo (Parent App). Đơn vị °F. Xuất danh sách nhiệt độ. Hồ sơ sức khỏe của trẻ (Health). Thông tin đưa / đón (BBA-73). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Centre Administrator, Centre Director, Teacher) | Centre / lớp được cấp. | Xem lần đo; thêm, sửa, xóa lần đo; xem Changelog; cấu hình Round khi được cấp quyền. |
| App (điểm danh / giáo viên) | Centre được cấp. | Đo và ghi lần đo. |
| System | Centre được cấp. | Hiển thị lần đo từ App và SMS, kiểm tra dữ liệu, đếm số lần đo bắt buộc, ghi lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Daily Operations › Temperature** | Xem lần đo nhiệt độ | Danh sách lần đo, mỗi lần đo một dòng; lọc; số lần đo bắt buộc; đánh dấu lần đo từ 37.5 °C. | BBA-74: US-001 |
| **Daily Operations › Temperature / Attendance** | Thêm lần đo | Thêm trên danh sách hoặc từ dòng điểm danh của trẻ; bắt buộc lý do thao tác. | BBA-74: US-002 |
| **Daily Operations › Temperature** | Sửa, xóa lần đo và Changelog | Sửa một lần đo trên dòng; xóa một hoặc nhiều lần đo; xem lịch sử. | BBA-74: US-003 |
| **Daily Operations › Temperature** | Cấu hình danh mục Round | Thêm / xóa Round tùy chọn; 3 Round bắt buộc cố định. | BBA-74: US-004 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-74: US-001 - Xem lần đo nhiệt độ

#### User Story

Là người dùng của Centre, tôi muốn xem các lần đo nhiệt độ của trẻ theo ngày và giờ, để biết trẻ đã được đo những lần nào.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab Temperature hiển thị danh sách lần đo, mỗi lần đo một dòng (BR-001, BR-002, BR-003). |
| FR-002 | Người dùng tìm kiếm và lọc theo trẻ, ngày, Round, Centre (BR-004). |
| FR-003 | Khi lọc theo một trẻ và một ngày, hệ thống hiển thị số lần đo bắt buộc đã có của trẻ trong ngày đó (BR-005). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên đo trên App, hoặc người dùng thêm trên SMS (US-002); lần đo hiện ở tab Temperature.
2. Người dùng mở Daily Operations › tab Temperature; danh sách hiện các lần đo, ngày và giờ mới nhất trước (FR-001).
3. Người dùng lọc theo Child và Date; tiêu đề danh sách hiện "x of 3 bắt buộc" (FR-002, FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Xóa bộ lọc: danh sách hiện lại toàn bộ lần đo (FR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có lần đo khớp bộ lọc: hiện "Không có lần đo phù hợp. Chọn Add reading để nhập mới."

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi lần đo là một dòng độc lập; một trẻ có thể có nhiều lần đo trong một ngày. Danh sách sắp xếp theo ngày và giờ đo giảm dần. |
| BR-002 | Mỗi dòng gồm: Ngày, Child, Class, Round, Giờ đo, Temperature (°C, 1 chữ số thập phân), Reason (Extra), Nguồn (App / SMS). |
| BR-003 | Lần đo từ 37.5 °C trở lên được tô đỏ để nhận biết sốt. |
| BR-004 | Trẻ đang tạm nghỉ (Temporary Withdrawal) không hiện lần đo trong các ngày thuộc thời gian tạm nghỉ. |
| BR-005 | Mỗi trẻ cần đủ 3 Round bắt buộc mỗi ngày: On arrival, After nap, Before pickup. "x of 3" đếm số Round bắt buộc đã có lần đo; Round tùy chọn (Before nap, Extra, Round thêm mới) không tính. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Daily Operations — tab Temperature (Temperature readings) | UX/UI V13: BBA-73-74_Version_moi.html |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Bộ lọc** | | | | | |
| Search child / ID | Ô tìm kiếm | Không | Trống | — | Tìm theo tên hoặc mã trẻ. |
| Child, Date, Round, Centre | Danh sách chọn / chọn ngày | Không | Tất cả | — | FR-002. |
| Xóa bộ lọc | Nút | — | — | — | Đặt lại bộ lọc. |
| **Danh sách Temperature readings** | | | | | |
| Tiêu đề số dòng | Text | — | — | — | "<n> lần đo · ngày / giờ mới nhất trước"; thêm "· x of 3 bắt buộc" khi lọc Child + Date (FR-003; BR-005). |
| Ô chọn dòng / chọn tất cả | Checkbox | — | Chưa chọn | — | Dùng cho Edit, Xóa, Changelog (US-003). |
| Ngày, Child, Class, Round, Giờ đo | Cột | — | — | — | BR-002. |
| Temperature (°C) | Cột | — | — | — | Số đậm; từ 37.5 tô đỏ (BR-003). |
| Reason (Extra) | Cột | — | "—" khi không phải Extra | — | Lý do đo thêm. |
| Nguồn | Cột | — | — | — | App hoặc SMS. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần đo lưu: mã lần đo, trẻ, ngày, Round, giờ đo, nhiệt độ (°C), lý do đo thêm (khi Extra), nguồn (App / SMS), người ghi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | App ghi 3 lần đo của Ethan ngày 24/11/2026: 08:15, 13:45, 16:50 | người dùng mở tab Temperature | có 3 dòng của Ethan, dòng 16:50 ở trên, mỗi dòng có Round, giờ, nhiệt độ, Nguồn App | FR-001; BR-001; BR-002; DATA-001 |
| AC-002 | Noah có lần đo Extra 37.9 °C lý do "Child felt warm" | người dùng mở tab Temperature | dòng hiện 37.9 tô đỏ, Reason (Extra) "Child felt warm" | BR-002; BR-003 |
| AC-003 | Ethan có On arrival và After nap ngày 24/11/2026 | người dùng lọc Child = Ethan, Date = 24/11/2026 | tiêu đề hiện "… · 2 of 3 bắt buộc" | FR-002; FR-003; BR-005 |
| AC-004 | Ethan có thêm một lần đo Extra cùng ngày | người dùng lọc Child + Date | "x of 3" không đổi | BR-005 |
| AC-005 | Millie tạm nghỉ từ 24/11 đến 01/12/2026 | người dùng lọc Date = 25/11/2026 | không có lần đo của Millie | BR-004 |
| AC-006 | lần đo 36.6 °C | người dùng xem danh sách | nhiệt độ không tô đỏ | BR-003 |

#### Dependencies (Phụ thuộc)

App (đo và ghi lần đo); Temporary Withdrawal (Joining & leaving).

### 6.2 BBA-74: US-002 - Thêm lần đo

#### User Story

Là người dùng của Centre, tôi muốn thêm lần đo nhiệt độ cho trẻ ngay trên SMS, để có đủ các lần đo trong ngày.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Người dùng có quyền thêm lần đo ở tab Temperature bằng Add reading: một dòng mới để nhập ngay trên danh sách (BR-006, BR-007, BR-008). |
| FR-005 | Người dùng có quyền thêm lần đo từ dòng điểm danh của trẻ (menu ⋯ › Thêm nhiệt độ) (BR-006 đến BR-009). |
| FR-006 | Mỗi lần thêm bắt buộc nhập lý do thao tác; hệ thống ghi Changelog (BR-010). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn + Add reading ở tab Temperature; danh sách có thêm một dòng mới ở trên cùng (FR-004).
2. Người dùng chọn Date, Child, Round, nhập Giờ đo, Temperature (và lý do nếu Round = Extra), nhập Lý do thao tác, chọn Lưu thay đổi (BR-006, BR-007).
3. Hệ thống lưu với Nguồn SMS, báo "Đã thêm lần đo và ghi lịch sử." (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Từ tab Attendance, người dùng chọn ⋯ › Thêm nhiệt độ ở dòng trẻ Có mặt: popup "Thêm nhiệt độ" hiện giờ đến, số lần đo bắt buộc đã có, Round mặc định là Round bắt buộc tiếp theo chưa đo; người dùng chọn nhanh nhiệt độ hoặc nhập, nhập lý do thao tác, chọn Lưu lần đo; hệ thống báo "Đã thêm <Round> · <nhiệt độ>°C cho <tên trẻ>. Xem ở tab Temperature." (FR-005; BR-009).
2. Người dùng chọn Đóng chỉnh sửa: không thêm.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thiếu trường bắt buộc, nhiệt độ ngoài thang, Extra thiếu lý do, giờ không hợp lệ, trẻ không đủ điều kiện, thiếu lý do thao tác: không lưu (VAL-001 đến VAL-006).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Nhiệt độ nhận 36.0–40.0 °C, bước 0.1. Ô nhiệt độ mặc định để trống; có sẵn các nút 36.3, 36.4, 36.5, 36.6, 36.7 để chọn nhanh và cho nhập tay. |
| BR-007 | Round chọn từ danh mục Round (US-004). Round = Extra bắt buộc ghi lý do đo thêm, ví dụ "Child felt warm". |
| BR-008 | Chỉ thêm được lần đo khi trong ngày đó trẻ không tạm nghỉ, có kết quả điểm danh Có mặt và có giờ đến. Giờ đo mặc định là giờ hiện tại; không trước giờ đến và không sau thời điểm hiện tại. |
| BR-009 | Mục Thêm nhiệt độ ở dòng điểm danh chỉ bật khi trẻ Có mặt và đã có giờ đến; Round mặc định là Round bắt buộc tiếp theo chưa đo trong ngày. |
| BR-010 | Mỗi lần thêm bắt buộc có lý do thao tác; Changelog ghi: thời điểm, hành động "Add temperature reading", lần đo mới (Round · nhiệt độ · giờ), người thao tác, lý do. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Thiếu Child, Date, Round, giờ đo hoặc nhiệt độ. | Không lưu; hiện "Nhập đầy đủ Child, Date, Round, Time và Temperature." |
| VAL-002 | Nhiệt độ ngoài 36.0–40.0 °C hoặc không theo bước 0.1. | Không lưu; hiện "Check the temperature: nhận 36.0–40.0°C và bước 0.1." |
| VAL-003 | Round = Extra mà để trống lý do đo thêm. | Không lưu; hiện "Enter why this extra reading was taken." |
| VAL-004 | Giờ đo trước giờ đến hoặc sau thời điểm hiện tại. | Không lưu; hiện "Check the time: không trước Arrival hoặc sau thời điểm hiện tại." |
| VAL-005 | Trẻ đang tạm nghỉ, hoặc không có kết quả Có mặt kèm giờ đến trong ngày. | Không lưu; hiện "Trẻ không thuộc danh sách hoạt động ở ngày này." hoặc "Không có Attendance Có mặt và giờ đến hợp lệ cho trẻ/ngày này." |
| VAL-006 | Để trống lý do thao tác. | Không lưu; hiện "Bắt buộc ghi lý do thao tác vào Changelog." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Tab Temperature — dòng thêm mới | UX/UI V13: BBA-73-74_Version_moi.html |
| Thêm nhiệt độ (popup từ tab Attendance) | Như trên |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Dòng thêm mới (tab Temperature)** | | | | | |
| + Add reading | Nút | Theo quyền | Ẩn khi đang sửa | — | Thêm dòng mới (FR-004). |
| Date | Chọn ngày | Có | Ngày đang lọc hoặc hôm nay | VAL-001. | — |
| Child | Danh sách chọn | Có | Trẻ đang lọc | VAL-001; VAL-005. | Không có trẻ đang tạm nghỉ ở ngày đã chọn. |
| Class | Chỉ đọc | — | Theo hồ sơ trẻ | — | — |
| Round | Danh sách chọn | Có | On arrival | VAL-001. | Round bắt buộc ghi "· Mandatory" (BR-007). |
| Giờ đo | Giờ | Có | Giờ hiện tại | VAL-004. | BR-008. |
| Temperature (°C) | Ô số | Có | Trống | VAL-002. | BR-006. |
| Reason (Extra) | Ô nhập | Khi Round = Extra | Ẩn | VAL-003. | BR-007. |
| Nguồn | Chỉ đọc | — | SMS | — | — |
| Lý do thao tác | Ô nhập | Có | Trống | VAL-006. | Ghi vào Changelog (BR-010). |
| Lưu thay đổi / Đóng chỉnh sửa | Nút | — | — | VAL-001 đến VAL-006. | Lưu hoặc bỏ. |
| **Thêm nhiệt độ (popup)** | | | | | |
| Thông tin ngày | Text | — | — | — | "Giờ đến <giờ> · đã đo x of 3 lần bắt buộc trong ngày." |
| Round | Danh sách chọn | Có | Round bắt buộc tiếp theo chưa đo | VAL-001. | BR-009. |
| Giờ đo | Giờ | Có | Giờ hiện tại (hôm nay) | VAL-004. | — |
| Nhiệt độ (°C) | Ô số + nút chọn nhanh | Có | Trống | VAL-002. | Nút 36.3–36.7; ghi chú "36.0–40.0 °C, bước 0.1 · từ 37.5 °C là sốt" (BR-006). |
| Lý do đo thêm | Ô nhập | Khi Round = Extra | Ẩn | VAL-003. | — |
| Lý do thao tác | Ô nhập | Có | Trống | VAL-006. | — |
| Hủy / Lưu lần đo | Nút | — | — | VAL-001 đến VAL-006. | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi thao tác thêm, sửa, xóa lần đo lưu Changelog: mã lần đo, trẻ, ngày, hành động, trường thay đổi (giá trị cũ, giá trị mới), người thao tác, thời điểm, lý do. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | Ethan Có mặt ngày 25/11/2026, đến lúc 08:12 | người dùng chọn + Add reading, chọn Ethan, Round After nap, Giờ đo 13:40, Temperature 36.6, lý do "App lỗi", Lưu thay đổi | hiện "Đã thêm lần đo và ghi lịch sử."; có dòng mới Nguồn SMS; Changelog có "Add temperature reading" | FR-004; FR-006; BR-010; DATA-002 |
| AC-008 | người dùng nhập Temperature 41.0 | chọn Lưu thay đổi | không lưu, hiện "Check the temperature: nhận 36.0–40.0°C và bước 0.1." | BR-006; VAL-002 |
| AC-009 | người dùng chọn Round Extra, để trống lý do đo thêm | chọn Lưu thay đổi | không lưu, hiện "Enter why this extra reading was taken." | BR-007; VAL-003 |
| AC-010 | Ethan đến lúc 08:12 | người dùng nhập Giờ đo 07:50 | không lưu, hiện "Check the time: không trước Arrival hoặc sau thời điểm hiện tại." | BR-008; VAL-004 |
| AC-011 | Ava Vắng có phép ngày 25/11/2026 | người dùng thêm lần đo cho Ava ngày đó | không lưu, hiện "Không có Attendance Có mặt và giờ đến hợp lệ cho trẻ/ngày này." | BR-008; VAL-005 |
| AC-012 | người dùng để trống lý do thao tác | chọn Lưu thay đổi | không lưu, hiện "Bắt buộc ghi lý do thao tác vào Changelog." | FR-006; VAL-006 |
| AC-013 | Noah Có mặt, đã có On arrival | người dùng chọn ⋯ › Thêm nhiệt độ ở dòng Noah | popup có Round mặc định After nap, dòng "đã đo 1 of 3 lần bắt buộc"; chọn nút 36.6, nhập lý do, Lưu lần đo thì báo "Đã thêm After nap · 36.6°C cho Noah Tan. Xem ở tab Temperature." | FR-005; BR-009 |
| AC-014 | Mia Vắng không phép | người dùng mở menu ⋯ ở dòng Mia | mục Thêm nhiệt độ bị tắt | BR-009 |
| AC-015 | người dùng không nhập Child | chọn Lưu thay đổi | không lưu, hiện "Nhập đầy đủ Child, Date, Round, Time và Temperature." | VAL-001 |

#### Dependencies (Phụ thuộc)

US-001; kết quả điểm danh và giờ đến (BBA-73, BBA-77); danh mục Round (US-004).

### 6.3 BBA-74: US-003 - Sửa, xóa lần đo và Changelog

#### User Story

Là người dùng của Centre, tôi muốn sửa hoặc xóa lần đo ghi sai và xem lịch sử thay đổi, để thông tin đo nhiệt độ luôn đúng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-007 | Người dùng có quyền sửa một lần đo đã chọn ngay trên dòng, kể cả lần đo App ghi nhận (BR-011). |
| FR-008 | Người dùng có quyền xóa một hoặc nhiều lần đo đã chọn, bắt buộc lý do (BR-012). |
| FR-009 | Người dùng xem Changelog của một lần đo đã chọn (BR-013). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn đúng một dòng, chọn ✎ Edit; dòng chuyển sang chế độ chỉnh sửa (FR-007).
2. Người dùng sửa Round, Giờ đo, Temperature hoặc lý do đo thêm, nhập Lý do thao tác, chọn Lưu thay đổi; hệ thống báo "Đã sửa Reading và ghi lịch sử." (BR-011).

#### Functional Flow - Alternative (Luồng thay thế)

1. Xóa: người dùng chọn một hoặc nhiều dòng, chọn Xóa; popup liệt kê các lần đo được chọn; người dùng nhập Lý do xóa, xác nhận; các lần đo không còn trong danh sách (FR-008; BR-012).
2. Changelog: người dùng chọn đúng một dòng, chọn ◷ Changelog; popup hiện lịch sử của lần đo đó (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Dữ liệu sửa không hợp lệ: không lưu (VAL-001 đến VAL-006).
2. Không có trường nào thay đổi: không lưu (VAL-007).
3. Xóa không có lý do: không xóa (VAL-008).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-011 | Edit chỉ bật khi chọn đúng một dòng. Sửa áp dụng cùng quy tắc như khi thêm (BR-006 đến BR-008), bắt buộc lý do thao tác; Changelog ghi từng trường thay đổi. Sửa được cả giá trị App ghi từ nhiệt kế Bluetooth. |
| BR-012 | Xóa bật khi chọn từ một dòng trở lên; bắt buộc lý do xóa. Lần đo bị xóa không còn trong danh sách, không tính vào "x of 3", nhưng thông tin trước khi xóa và người thao tác vẫn lưu trong Changelog. |
| BR-013 | Changelog bật khi chọn đúng một dòng; hiển thị: Thời điểm, Module, Action, Field, Old, New, User, Reason. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-007 | Sửa mà không có trường nào thay đổi. | Không lưu; hiện "Không có trường dữ liệu nào được thay đổi." |
| VAL-008 | Xóa mà để trống lý do xóa. | Không xóa; hiện "Bắt buộc ghi lý do xóa." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Tab Temperature — sửa trên dòng; Xóa Temperature readings (popup); Changelog (popup) | UX/UI V13: BBA-73-74_Version_moi.html |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| "<n> dòng được chọn" | Text | — | 0 | — | Số dòng đang chọn. |
| ✎ Edit | Nút | Theo quyền | Bật khi chọn đúng 1 dòng | — | FR-007; BR-011. |
| Xóa | Nút | Theo quyền | Bật khi chọn ≥ 1 dòng | — | Mở popup Xóa Temperature readings (FR-008). |
| ◷ Changelog | Nút | — | Bật khi chọn đúng 1 dòng | — | FR-009; BR-013. |
| Lý do thao tác | Ô nhập | Có khi sửa | Trống | VAL-006. | Ghi vào Changelog. |
| Lưu thay đổi / Đóng chỉnh sửa | Nút | — | Hiện khi đang sửa | VAL-001 đến VAL-007. | — |
| **Xóa Temperature readings** | | | | | |
| Danh sách lần đo được chọn | Text | — | — | — | "<n> Reading được chọn." và từng dòng: tên trẻ · ngày · Round · nhiệt độ. |
| Lý do xóa | Ô nhập nhiều dòng | Có | Trống | VAL-008. | — |
| Hủy / Xác nhận xóa | Nút | — | — | VAL-008. | Báo "Đã xóa <n> …" sau khi xóa. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Lưu theo DATA-002; khi xóa lưu thêm thông tin lần đo trước khi xóa. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-016 | lần đo App 37.9 °C của Ethan, thực tế 36.9 °C | người dùng chọn dòng, ✎ Edit, sửa 36.9, nhập lý do, Lưu thay đổi | hiện "Đã sửa Reading và ghi lịch sử."; dòng hiện 36.9; Changelog có Old 37.9, New 36.9 | FR-007; BR-011; DATA-002 |
| AC-017 | người dùng chọn 2 dòng | xem nút ✎ Edit và ◷ Changelog | cả hai bị tắt; nút Xóa bật | BR-011; BR-012; BR-013 |
| AC-018 | người dùng đã chọn 2 lần đo | chọn Xóa, nhập lý do, xác nhận | 2 lần đo không còn trong danh sách; "x of 3" giảm nếu là Round bắt buộc; Changelog lưu thông tin trước khi xóa | FR-008; BR-012 |
| AC-019 | người dùng chọn Xóa, để trống lý do | xác nhận | không xóa, hiện "Bắt buộc ghi lý do xóa." | VAL-008 |
| AC-020 | người dùng mở Edit nhưng không đổi gì, có lý do | chọn Lưu thay đổi | không lưu, hiện "Không có trường dữ liệu nào được thay đổi." | VAL-007 |
| AC-021 | lần đo của Ethan đã sửa 1 lần | người dùng chọn dòng, ◷ Changelog | popup hiện Thời điểm, Module, Action, Field, Old, New, User, Reason | FR-009; BR-013 |

#### Dependencies (Phụ thuộc)

US-001, US-002.

### 6.4 BBA-74: US-004 - Cấu hình danh mục Round

#### User Story

Là người dùng được cấp quyền, tôi muốn thêm hoặc xóa các Round tùy chọn, để danh sách thời điểm đo phù hợp với hoạt động của Centre.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-010 | Người dùng có quyền mở ⚙ Round để xem danh mục Round và thêm Round tùy chọn mới (BR-014, BR-015). |
| FR-011 | Người dùng có quyền xóa Round tùy chọn tự thêm khi chưa có lần đo nào dùng Round đó (BR-016). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn ⚙ Round; popup "Cấu hình danh mục Round" liệt kê các Round và loại của từng Round (FR-010).
2. Người dùng nhập tên Round mới và lý do, chọn thêm; Round mới có trong danh sách chọn Round, báo "Round đã được thêm vào dropdown." (BR-015).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Remove ở Round tùy chọn tự thêm, nhập lý do; Round bị xóa khỏi danh mục, báo "Đã xóa Round tùy chọn." (FR-011; BR-016).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Tên trống, trùng, thiếu lý do, hoặc Round đang có lần đo: không thêm / không xóa (VAL-009 đến VAL-012).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-014 | Danh mục mặc định: On arrival, After nap, Before pickup (Mandatory, khóa, không xóa được); Before nap, Extra (Optional, mặc định, không xóa được). |
| BR-015 | Round thêm mới là Optional, tên không trùng (không phân biệt hoa thường), bắt buộc lý do; không tính vào "x of 3". |
| BR-016 | Chỉ xóa được Round tự thêm và chưa có lần đo nào dùng Round đó; bắt buộc lý do. Mỗi lần thêm / xóa Round ghi Changelog. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-009 | Tên Round trống. | Không thêm; hiện "Nhập tên Round." |
| VAL-010 | Tên Round đã tồn tại. | Không thêm; hiện "Round đã tồn tại." |
| VAL-011 | Thiếu lý do thêm / xóa Round. | Không lưu; hiện "Nhập lý do thêm Round." hoặc "Nhập lý do xóa Round." |
| VAL-012 | Xóa Round đang có lần đo. | Không xóa; hiện "Round này đang có dữ liệu Reading, không thể xóa danh mục." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Cấu hình danh mục Round (popup) | UX/UI V13: BBA-73-74_Version_moi.html |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| ⚙ Round | Nút | Theo quyền | — | — | Mở popup (FR-010). |
| Danh mục Round | Danh sách | — | — | — | Tên Round; loại "Mandatory · locked" / "Optional · default" / "Optional · custom"; nhãn Default hoặc nút Remove (BR-014). |
| Thêm Round mới | Ô nhập | Khi thêm | Trống | VAL-009; VAL-010. | Ví dụ "After outdoor activities". |
| Lý do thêm / xóa Round | Ô nhập | Có | Trống | VAL-011. | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi Round lưu: tên, loại (Mandatory / Optional), mặc định hay tự thêm. Mỗi lần thêm / xóa Round lưu Changelog: hành động, tên Round, người thao tác, thời điểm, lý do. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-022 | danh mục mặc định | người dùng mở ⚙ Round | On arrival, After nap, Before pickup ghi "Mandatory · locked"; Before nap, Extra ghi "Optional · default"; không có nút Remove ở 5 Round này | FR-010; BR-014; DATA-003 |
| AC-023 | người dùng nhập "After outdoor activities" và lý do | chọn thêm | báo "Round đã được thêm vào dropdown."; Round có trong danh sách chọn Round | BR-015 |
| AC-024 | đã có Round "After outdoor activities" | người dùng thêm "after outdoor activities" | không thêm, hiện "Round đã tồn tại." | VAL-010 |
| AC-025 | người dùng nhập tên Round, để trống lý do | chọn thêm | không thêm, hiện "Nhập lý do thêm Round." | VAL-011 |
| AC-026 | Round "After outdoor activities" đã có lần đo | người dùng chọn Remove, nhập lý do | không xóa, hiện "Round này đang có dữ liệu Reading, không thể xóa danh mục." | FR-011; BR-016; VAL-012 |
| AC-027 | người dùng để trống tên Round | chọn thêm | không thêm, hiện "Nhập tên Round." | VAL-009 |

#### Dependencies (Phụ thuộc)

US-002, US-003.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Vai trò nào được cấu hình danh mục Round; danh mục dùng chung toàn hệ thống hay theo Centre? | HQ Ops | Trung bình | |
| OQ-02 | Lần đo được thêm, sửa, xóa trong khoảng thời gian nào (chỉ trong ngày hay cả ngày trước)? | Centre Director / HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lần đo (Reading) | Một lần đo nhiệt độ của trẻ, có ngày, giờ, Round; ghi trên App hoặc trên SMS. |
| Round | Thời điểm đo trong ngày, chọn từ danh mục Round. |
| Round bắt buộc (Mandatory) | On arrival, After nap, Before pickup; mỗi trẻ cần đủ 3 Round này mỗi ngày. |
| Ngưỡng sốt | Từ 37.5 °C trở lên được tô đỏ để nhận biết sốt. |
| Changelog | Lịch sử thay đổi theo từng trường, kèm người thao tác và lý do. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Round | On arrival, Before nap, After nap, Before pickup, Extra; Round tùy chọn thêm mới. | US-004. |
| Nguồn | App, SMS. | — |
