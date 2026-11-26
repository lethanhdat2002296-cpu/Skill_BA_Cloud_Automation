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

Tài liệu đặc tả việc quản lý mọi lần đo nhiệt độ của trẻ trên SMS ở tab Temperature: tìm kiếm, lọc, thêm, sửa, xóa và xem lịch sử. Mỗi trẻ được đo tối thiểu 3 lần mỗi ngày (khi đến, sau ngủ trưa, trước khi về) và đo thêm khi thấy bất thường.

Lần đo được ghi trên App (nhập tay hoặc từ nhiệt kế) rồi cung cấp cho SMS. Luồng và màn hình trên App thuộc đặc tả của App.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Tab Temperature chứa mọi lần đo của trẻ; lọc theo Brand, Centre, lớp, ngày; tìm theo tên trẻ; thêm từ dòng điểm danh hoặc từ tab Temperature; sửa, xóa và xem lịch sử theo quyền; số lần đo bắt buộc trong ngày. | Luồng và màn hình đo nhiệt độ trên App; kết nối nhiệt kế và đồng bộ dữ liệu của App; phụ huynh xem lần đo (Parent App); đơn vị °F; hồ sơ sức khỏe của trẻ (Health); thông tin đưa / đón (BBA-73). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised SMS user | Dữ liệu trong phạm vi được cấp. | Xem, tìm kiếm, lọc, thêm, sửa, xóa lần đo và xem lịch sử theo quyền. |
| System | Lần đo nhiệt độ và hồ sơ trẻ liên quan. | Cung cấp dữ liệu để hiển thị; kiểm tra quyền và dữ liệu; đếm số lần đo bắt buộc; ghi lịch sử. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-74 gồm hai User Story trên SMS, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Temperature** | Xem lần đo nhiệt độ | Tab Temperature hiển thị mọi lần đo; tìm kiếm, lọc; số lần đo bắt buộc. | BBA-74: US-001 |
| **Temperature** | Thêm, sửa, xóa lần đo | Thêm từ dòng điểm danh hoặc tab Temperature; sửa, xóa và xem lịch sử. | BBA-74: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-74: US-001 - Xem lần đo nhiệt độ

#### User Story

Là người dùng có quyền trên SMS, tôi muốn xem mọi lần đo nhiệt độ của trẻ, tìm kiếm và lọc, để theo dõi nhiệt độ của trẻ trong ngày.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải có tab Temperature hiển thị mọi lần đo nhiệt độ của trẻ trong phạm vi được cấp, mỗi lần đo một dòng. |
| FR-002 | Hệ thống phải cho lọc theo Brand, Centre, lớp, ngày và tìm theo tên trẻ. |
| FR-003 | Hệ thống phải hiển thị số lần đo bắt buộc đã có của trẻ trong ngày. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Daily Operations › tab Temperature.
2. Người dùng chọn Brand, Centre, lớp, ngày hoặc tìm theo tên trẻ. Hệ thống hiển thị các lần đo khớp mọi điều kiện đã chọn.

#### Functional Flow - Alternative (Luồng thay thế)

1. Một trẻ có nhiều lần đo trong ngày: mỗi lần đo một dòng, kể cả các lần cùng Round.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có lần đo phù hợp: hiển thị danh sách trống theo thiết kế chuẩn.
2. Người dùng không có quyền hoặc không tải được dữ liệu: theo hành vi chuẩn của hệ thống.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Tab Temperature chứa mọi lần đo của trẻ ở mọi Round. Mỗi dòng là một lần đo; không chỉ hiện lần đo mới nhất. Xem danh sách không tạo lần đo. |
| BR-002 | Mỗi dòng gồm: tên trẻ, lớp, Brand, Centre, Round, Temperature (°C, 1 chữ số thập phân), Time, Measurement method, lý do đo thêm (khi Extra). Lần đo từ 37.5 °C trở lên được tô đỏ. |
| BR-003 | Round gồm: On arrival, Before nap, After nap, Before pickup, Extra. Round bắt buộc mỗi ngày: On arrival, After nap, Before pickup; "x of 3" đếm số Round bắt buộc đã có lần đo trong ngày. |
| BR-004 | Áp dụng Brand, Centre, lớp, ngày và tìm theo tên cùng lúc. Lọc ngày theo thời điểm đo. Trẻ đang tạm nghỉ (Temporary Withdrawal) không hiện trong các ngày thuộc thời gian tạm nghỉ. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Người dùng yêu cầu xem dữ liệu ngoài phạm vi được cấp. | Không cung cấp dữ liệu ngoài phạm vi. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-74: UI-US-001 - Tab Temperature trên SMS | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Temperature | Tab | Có | Trong Daily Operations | FR-001; BR-001 | Hiển thị mọi lần đo trong phạm vi được cấp. |
| Brand / Centre / Class | Bộ lọc chọn | Không | Trong phạm vi được cấp | BR-004; VAL-001 | Áp dụng cùng lúc. |
| Date | Bộ lọc ngày | Không | Ngày hiện tại | BR-004 | Lọc theo ngày của lần đo. |
| Search | Ô nhập | Không | Trống | FR-002 | Tìm theo tên trẻ. |
| Temperature readings | Danh sách | Khi có | Mỗi lần đo một dòng | BR-001; BR-002 | Cột theo BR-002; thao tác Edit, Delete, View audit (US-002). |
| x of 3 | Hiển thị | — | Theo trẻ và ngày | FR-003; BR-003 | Số Round bắt buộc đã có lần đo. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Lưu mỗi lần đo là một bản ghi riêng: trẻ, Round, Temperature, Time, Measurement method, lý do đo thêm (khi Extra), nguồn ghi (App / SMS), Brand / Centre / lớp để lọc trong phạm vi được cấp. Không gộp các lần đo cùng ngày hay cùng Round thành một kết quả mới nhất. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Có lần đo của trẻ ở nhiều Brand, Centre, ngày | người dùng lọc Brand, Centre, ngày và tìm theo tên | chỉ hiện lần đo khớp mọi điều kiện trong phạm vi được cấp | FR-002; BR-004; VAL-001 |
| AC-002 | Ethan có 4 lần đo ngày 24/11/2026, trong đó 2 lần cùng Round Extra | người dùng xem danh sách | hiện đủ 4 dòng, không chỉ lần mới nhất | FR-001; BR-001; DATA-001 |
| AC-003 | Noah có lần đo 37.9 °C | người dùng xem danh sách | nhiệt độ 37.9 tô đỏ | BR-002 |
| AC-004 | Ethan có On arrival và After nap ngày 24/11/2026 | người dùng xem lần đo của Ethan ngày đó | hiện "2 of 3" | FR-003; BR-003 |
| AC-005 | Millie tạm nghỉ từ 24/11 đến 01/12/2026 | người dùng chọn ngày 25/11/2026 | không có lần đo của Millie | BR-004 |

#### Dependencies (Phụ thuộc)

App (đo và ghi lần đo); Temporary Withdrawal (Joining & leaving).

### 6.2 BBA-74: US-002 - Thêm, sửa, xóa lần đo

#### User Story

Là người dùng có quyền trên SMS, tôi muốn thêm, sửa, xóa lần đo nhiệt độ và xem lịch sử, để quản lý dữ liệu nhiệt độ của trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Hệ thống phải cho thêm lần đo từ dòng điểm danh hoặc từ tab Temperature. Từ dòng điểm danh, trẻ được chọn sẵn; từ tab Temperature, người dùng chọn trẻ. |
| FR-005 | Form thêm gồm Child, Round, Temperature, Time, Measurement method, và lý do đo thêm khi Round = Extra. Time mặc định là thời điểm tạo. |
| FR-006 | Người dùng có quyền sửa hoặc xóa lần đo; không cần lý do hay duyệt. |
| FR-007 | Hệ thống phải ghi lịch sử thêm, sửa, xóa lần đo và cho xem lịch sử. Lần đo đã xóa vẫn có trong lịch sử. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn Add temperature, chọn trẻ, nhập Round, Temperature, Time, Measurement method.
2. Người dùng chọn Save. Hệ thống kiểm tra dữ liệu, lưu một bản ghi cho lần đo và ghi lịch sử.
3. Người dùng chọn Edit hoặc Delete ở một lần đo. Hệ thống lưu thay đổi hoặc xóa, cập nhật danh sách và ghi lịch sử.
4. Người dùng chọn View audit để xem lịch sử thêm, sửa, xóa.

#### Functional Flow - Alternative (Luồng thay thế)

1. Thêm từ dòng điểm danh: người dùng chọn Add temperature ở dòng của trẻ; form mở với trẻ đã chọn sẵn, các trường khác theo FR-005.
2. Người dùng đóng form hoặc chọn Cancel trước khi lưu: không lưu thay đổi.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thiếu dữ liệu bắt buộc hoặc dữ liệu không hợp lệ: báo lỗi tại trường và không lưu (VAL-002 đến VAL-006).
2. Người dùng không có quyền hoặc lưu / xóa thất bại: theo hành vi chuẩn; không hiển thị thao tác thất bại như đã hoàn tất.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Thêm từ dòng điểm danh thì trẻ được chọn sẵn. Thêm từ tab Temperature thì người dùng chọn trẻ trong phạm vi được cấp. |
| BR-006 | Temperature nhận 36.0–40.0 °C, bước 0.1. Measurement method gồm Manual và Device. Time mặc định là thời điểm tạo, hiển thị theo múi giờ của người dùng. |
| BR-007 | Round = Extra bắt buộc ghi lý do đo thêm, ví dụ "Child felt warm". |
| BR-008 | Chỉ thêm được lần đo cho trẻ có mặt trong ngày (đã có giờ đến); Time không trước giờ đến và không sau thời điểm hiện tại. |
| BR-009 | Sửa và xóa lần đo không giới hạn theo ngày, Round hay Measurement method; không cần lý do hay duyệt; theo quyền người dùng. Sửa được cả lần đo App ghi nhận. |
| BR-010 | Lịch sử ghi: thao tác, lần đo / trẻ, giá trị cũ / mới (khi có), người thao tác, thời điểm. Xóa lần đo không xóa lịch sử của lần đo đó. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Chưa chọn Child, Round hoặc Measurement method; thiếu Temperature hoặc Time. | Báo trường bắt buộc và không lưu. |
| VAL-003 | Temperature không phải số, ngoài 36.0–40.0 °C hoặc không theo bước 0.1. | Báo "Check the temperature: nhận 36.0–40.0°C và bước 0.1." và không lưu. |
| VAL-004 | Round = Extra mà để trống lý do đo thêm. | Báo "Enter why this extra reading was taken." và không lưu. |
| VAL-005 | Time trước giờ đến hoặc sau thời điểm hiện tại. | Báo "Check the time: không trước Arrival hoặc sau thời điểm hiện tại." và không lưu. |
| VAL-006 | Trẻ không có mặt trong ngày (chưa có giờ đến) hoặc đang tạm nghỉ. | Báo trẻ không thuộc danh sách hoạt động ở ngày này và không lưu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-74: UI-US-002 - Form thêm / sửa lần đo trên SMS | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Add temperature | Thao tác | Theo quyền | Ở dòng điểm danh hoặc tab Temperature | FR-004; BR-005 | Mở form thêm; trẻ được chọn sẵn khi mở từ dòng điểm danh. |
| Child | Chọn | Có | Chọn sẵn từ dòng điểm danh; chọn ở tab Temperature | VAL-002; VAL-006 | Xác định trẻ của lần đo. |
| Round | Chọn | Có | Theo lựa chọn | VAL-002; BR-003 | On arrival / Before nap / After nap / Before pickup / Extra. |
| Temperature | Ô số | Có | Giá trị nhập hoặc đo | VAL-002; VAL-003 | Ghi nhiệt độ (°C). |
| Time | Ngày giờ | Có | Thời điểm tạo | VAL-002; VAL-005 | Ghi hoặc sửa thời điểm đo. |
| Measurement method | Chọn | Có | Theo dữ liệu hoặc lựa chọn | VAL-002; BR-006 | Manual / Device. |
| Lý do đo thêm | Ô nhập | Khi Round = Extra | Ẩn | VAL-004 | BR-007. |
| Save / Cancel | Thao tác | — | Trong form thêm / sửa | VAL-002 đến VAL-006 | Lưu dữ liệu hợp lệ và ghi lịch sử; Cancel đóng không lưu. |
| Edit / Delete | Thao tác | Theo quyền | Ở từng lần đo | FR-006; BR-009 | Sửa các trường hoặc xóa lần đo; ghi lịch sử. |
| View audit | Thao tác | Theo quyền | Ở tab Temperature và từng lần đo | FR-007; BR-010 | Xem lịch sử thêm, sửa, xóa, gồm cả lần đo đã xóa. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Ghi lịch sử thêm, sửa, xóa theo BR-010; cho xem lịch sử ở từng lần đo và ở tab Temperature, gồm cả lần đo đã xóa. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | Người dùng đang xem dòng điểm danh của Ethan (có mặt) | người dùng chọn Add temperature | form mở với Ethan đã chọn sẵn, Time mặc định là thời điểm tạo | FR-004; FR-005; BR-005 |
| AC-007 | Người dùng ở tab Temperature | người dùng chọn Add, chọn trẻ và lưu dữ liệu hợp lệ | tạo lần đo với Round, Temperature, Time, Measurement method; ghi lịch sử | FR-004; FR-005; DATA-001; DATA-002 |
| AC-008 | Có lần đo của ngày trước, người dùng có quyền | người dùng sửa hoặc xóa lần đo | cho phép, không cần lý do hay duyệt; ghi lịch sử | FR-006; BR-009; DATA-002 |
| AC-009 | Lần đo đã được thêm, sửa và xóa | người dùng mở View audit | hiện thao tác, giá trị cũ / mới (khi có), người thao tác, thời điểm, gồm cả lần đo đã xóa | FR-007; BR-010 |
| AC-010 | Thiếu Round hoặc Temperature | người dùng chọn Save | báo trường bắt buộc và không lưu | VAL-002 |
| AC-011 | Người dùng nhập Temperature 41.0 | người dùng chọn Save | báo "Check the temperature: nhận 36.0–40.0°C và bước 0.1." và không lưu | BR-006; VAL-003 |
| AC-012 | Round = Extra, lý do đo thêm để trống | người dùng chọn Save | báo "Enter why this extra reading was taken." và không lưu | BR-007; VAL-004 |
| AC-013 | Ethan đến lúc 08:12 | người dùng nhập Time 07:50 và lưu | báo "Check the time: không trước Arrival hoặc sau thời điểm hiện tại." và không lưu | BR-008; VAL-005 |
| AC-014 | Ava vắng ngày 25/11/2026 | người dùng thêm lần đo cho Ava ngày đó | báo trẻ không thuộc danh sách hoạt động ở ngày này và không lưu | BR-008; VAL-006 |
| AC-015 | Người dùng đang thêm hoặc sửa lần đo | người dùng chọn Cancel | đóng form, không lưu thay đổi | FR-004; FR-006 |

#### Dependencies (Phụ thuộc)

US-001; giờ đến của trẻ (BBA-73).

## 7. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lần đo (Reading) | Một lần đo nhiệt độ của trẻ; mỗi lần đo là một bản ghi riêng. |
| Round | Thời điểm đo: On arrival, Before nap, After nap, Before pickup, Extra. |
| Round bắt buộc | On arrival, After nap, Before pickup; mỗi trẻ cần đủ 3 Round này mỗi ngày. |
| Measurement method | Manual hoặc Device; khác với nguồn ghi App / SMS. |
| Nguồn ghi | App hoặc tài khoản ghi dữ liệu trên SMS. |
