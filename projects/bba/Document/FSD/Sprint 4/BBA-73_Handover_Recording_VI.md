# Handover Recording

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | BBA-73 Handover recording |
| Mã tài liệu | FRD-3.2.1.01_Handover_Recording |
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

Tài liệu đặc tả việc quản lý thông tin đưa / đón trẻ trên SMS: xem giờ đến, giờ về, người đưa, người đón, quan hệ với trẻ, nhiệt độ lúc đưa / đón và ảnh bàn giao; tìm kiếm, lọc; nhận biết trẻ đang ở trường; xuất dữ liệu; và cho người dùng có quyền thêm thông tin đưa / đón còn thiếu ngay trên SMS, kèm lý do và qua duyệt.

Thông tin đưa / đón được ghi trên App khi nhân viên nhận và trả trẻ, rồi cung cấp cho SMS. Luồng và màn hình trên App thuộc đặc tả của App.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Xem, tìm kiếm, lọc thông tin đưa / đón trên SMS; xem nhiệt độ lúc đưa / đón và ảnh bàn giao; nhận biết trẻ đang ở trường; xuất dữ liệu; người dùng có quyền thêm thông tin đưa / đón còn thiếu, kèm lý do và qua duyệt; lưu lịch sử. | Sửa, xoá thông tin đưa / đón đã có. Luồng và màn hình nhận / trả trẻ trên App; chụp ảnh và đồng bộ dữ liệu của App; tạo, thêm, duyệt người được phép đón (Children & Families, Parents App); ghi và sửa kết quả điểm danh Có mặt / Vắng (BBA-77); quy tắc đo nhiệt độ (BBA-74); đến muộn (BBA-75); cấu hình approval route (BBA-53); thông báo cho phụ huynh. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Centre Director (CD) | Trẻ trong các Centre được cấp. | Xem dữ liệu và ảnh; thêm thông tin đưa / đón còn thiếu. |
| Authorised SMS user | Dữ liệu trong phạm vi được cấp. | Xem dữ liệu, mở ảnh, tìm kiếm, lọc, xuất dữ liệu; thêm thông tin đưa / đón theo quyền. |
| Approver | Yêu cầu thêm thông tin ở bước mình được giao theo approval route. | Duyệt hoặc từ chối yêu cầu trong My approvals. |
| System | Thông tin đưa / đón và hồ sơ trẻ liên quan. | Cung cấp dữ liệu để hiển thị và xuất; xác định trẻ đang ở trường; kiểm tra quyền; gửi yêu cầu đi duyệt; ghi lịch sử. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-73 gồm hai User Story trên SMS, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Attendance** | Xem và xuất thông tin đưa / đón | Xem thông tin đưa / đón, nhiệt độ, ảnh bàn giao và trẻ đang ở trường; tìm kiếm, lọc, xuất dữ liệu. | BBA-73: US-001 |
| **Attendance** | Thêm thông tin đưa / đón | Người dùng có quyền thêm thông tin đưa / đón còn thiếu trên SMS, kèm lý do; thông tin được ghi nhận sau khi duyệt. | BBA-73: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-73: US-001 - Xem và xuất thông tin đưa / đón

#### User Story

Là người dùng có quyền trên SMS, tôi muốn xem thông tin đưa / đón và ảnh bàn giao, tìm kiếm, lọc và xuất dữ liệu, để theo dõi ai đưa, ai đón trẻ, lúc mấy giờ và trẻ nào đang ở trường.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải hiển thị thông tin đưa / đón của trẻ trong phạm vi dữ liệu được cấp. |
| FR-002 | Hệ thống phải cho tìm theo tên hoặc mã trẻ và lọc theo Centre, lớp, ngày, kết quả điểm danh. |
| FR-003 | Hệ thống phải cho người dùng có quyền xuất dữ liệu đưa / đón theo khoảng ngày đã chọn, với các cột ở Phụ lục B. |
| FR-004 | Hệ thống phải hiển thị ảnh bàn giao lúc đưa và lúc đón, và cho người dùng có quyền mở từng ảnh. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Daily Operations › Attendance.
2. Hệ thống hiển thị thông tin đưa / đón và ảnh bàn giao trong phạm vi được cấp.
3. Người dùng tìm theo tên / mã trẻ hoặc chọn Centre, lớp, ngày; chọn một ảnh để mở.
4. Người dùng chọn khoảng ngày và xuất dữ liệu bằng chức năng xuất dữ liệu chuẩn.

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có dữ liệu phù hợp: hệ thống hiển thị kết quả trống theo thiết kế chuẩn.
2. Trẻ chưa có giờ đến, giờ về, nhiệt độ hoặc ảnh: ô thiếu hiển thị “—”.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền hoặc yêu cầu dữ liệu ngoài phạm vi: hệ thống không cung cấp dữ liệu đó.
2. Không tải hoặc không xuất được dữ liệu: hệ thống báo lỗi theo hành vi chuẩn của hệ thống.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Xem dữ liệu, mở ảnh và xuất dữ liệu theo quyền người dùng và phạm vi dữ liệu Centre. |
| BR-002 | Trẻ được coi là đang ở trường khi có giờ đến và chưa có giờ về. |
| BR-003 | Danh sách gồm: ngày, tên trẻ, lớp, Centre, giờ đến, người đưa, quan hệ, nhiệt độ lúc đưa, giờ về, người đón, quan hệ, nhiệt độ lúc đón, ảnh lúc đưa, ảnh lúc đón, lý do (với thông tin thêm trên SMS). Ô thiếu hiển thị “—”; ảnh có sẵn thì mở được. |
| BR-004 | Người đưa là người thân của trẻ: chọn từ danh sách người thân. Người đưa không có trong danh sách thì người dùng chọn “Someone else” và nhập họ tên, quan hệ với trẻ (bắt buộc). |
| BR-005 | Trẻ đi xe bus: người đưa là “Bus driver”, người đón là “Bus attendant”, kèm số xe. Chỉ chọn được Bus driver / Bus attendant khi trẻ đi xe bus. |
| BR-006 | Người đón chỉ chọn từ danh sách người được phép đón; không có lựa chọn người lạ hay đón tạm thời. |
| BR-007 | Giờ đến / giờ về là ngày giờ lúc nhân viên lưu trên App (hoặc giờ người dùng thêm trên SMS), hiển thị theo múi giờ của người dùng, không gắn với buổi hay giờ cố định trong ngày. |
| BR-008 | Xuất dữ liệu dùng các cột ở Phụ lục B, theo khoảng ngày đã chọn và phạm vi dữ liệu được cấp; theo chức năng xuất dữ liệu chuẩn. |
| BR-009 | Trẻ đang tạm nghỉ (Temporary Withdrawal) không hiện trong các ngày thuộc thời gian tạm nghỉ. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Người dùng yêu cầu xem hoặc xuất dữ liệu ngoài phạm vi được cấp. | Không cung cấp dữ liệu ngoài phạm vi. |
| VAL-002 | Ngày bắt đầu xuất sau ngày kết thúc. | Báo khoảng ngày không hợp lệ và không xuất. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-73: UI-US-001 - Thông tin đưa / đón trên SMS | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Search | Ô nhập | Không | Trống | BR-001 | Tìm theo tên hoặc mã trẻ. |
| Centre | Chọn | Không | Centre của người dùng | VAL-001 | Lọc theo Centre được cấp. |
| Class | Chọn | Không | Tất cả | — | Lọc theo lớp. |
| Date | Chọn ngày | Có | Ngày hiện tại | BR-007 | Lọc theo ngày, theo múi giờ của người dùng. |
| Tên trẻ, lớp, Centre | Hiển thị | Có | Từ hồ sơ trẻ | BR-003 | Xác định trẻ. |
| Giờ đến / Giờ về | Hiển thị | Khi có | “—” khi thiếu | BR-007 | Ngày giờ ghi nhận, theo múi giờ của người dùng. |
| Người đưa / Người đón | Hiển thị | Khi có | “—” khi thiếu | BR-004; BR-005; BR-006 | Tên người đưa / người đón. |
| Quan hệ | Hiển thị | Khi có | “—” khi thiếu | BR-004; BR-005 | Quan hệ với trẻ; Someone else hoặc số xe bus. |
| Nhiệt độ lúc đưa / Nhiệt độ lúc đón | Hiển thị | Khi có | “—” khi thiếu | BR-003 | Nhiệt độ đo lúc nhận trẻ / lúc trả trẻ (°C), theo BBA-74. |
| Ảnh lúc đưa / Ảnh lúc đón | Ảnh / mở | Khi có | Ảnh đã lưu | BR-001; FR-004 | Chọn để mở ảnh trẻ cùng người đưa / người đón. |
| Lý do | Hiển thị | Khi có | “—” với dữ liệu từ App | BR-003 | Lý do người dùng nhập khi thêm thông tin trên SMS (US-002). |
| Đang ở trường | Hiển thị | Có | Từ dữ liệu SMS | BR-002 | Dấu hiệu trẻ đang ở trường. |
| From date / To date | Chọn ngày | Khi xuất | From date = To date = ngày hiện tại | VAL-002 | Khoảng ngày xuất. |
| Export data | Thao tác | Theo quyền | Theo điều kiện xuất | BR-001; BR-008; VAL-002 | Xuất theo Phụ lục B và quy tắc chuẩn. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Dùng hồ sơ trẻ, Centre, lớp, ngày giờ đến / về, người đưa / người đón, quan hệ, nhiệt độ lúc đưa / đón, ảnh bàn giao, lý do và nguồn ghi (App / SMS) để hiển thị và xuất dữ liệu. |
| DATA-002 | Xem danh sách hay mở ảnh không tạo bản ghi đưa / đón. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Người dùng có quyền vào Attendance | người dùng mở màn hình | mặc định Centre của người dùng và ngày hiện tại; hiển thị thông tin đưa / đón và ảnh trong phạm vi được cấp | FR-001; BR-001; BR-003; DATA-002 |
| AC-002 | Có dữ liệu của nhiều Centre | người dùng tìm theo tên và chọn Centre, lớp, ngày | chỉ hiện dữ liệu khớp trong phạm vi được cấp | FR-002; BR-001; VAL-001 |
| AC-003 | Ethan có giờ đến 08:12, chưa có giờ về | hệ thống tải dữ liệu | Ethan có dấu hiệu đang ở trường | BR-002 |
| AC-004 | Ethan chưa có giờ về, nhiệt độ lúc đón và ảnh lúc đón | hệ thống hiển thị danh sách | các ô thiếu hiện “—” | BR-003; DATA-001 |
| AC-005 | Noah được người giúp việc Siti (không có trong danh sách người thân) đưa đến; Lucas đi xe bus Bus 2 | hệ thống hiển thị danh sách | Noah: Người đưa Siti, Quan hệ “Helper (Someone else)”; Lucas: Người đưa “Bus driver”, Quan hệ “Bus 2” | BR-004; BR-005 |
| AC-006 | Ethan có ảnh lúc đưa và ảnh lúc đón, người dùng có quyền xem | người dùng chọn từng ảnh | mở đúng ảnh tương ứng | FR-004; BR-001 |
| AC-007 | Người dùng có quyền xuất, không đổi From date / To date mặc định | người dùng xuất dữ liệu | From date và To date là ngày hiện tại; file có các cột ở Phụ lục B và dữ liệu trong phạm vi được cấp | FR-003; BR-008 |
| AC-008 | Ngày bắt đầu xuất sau ngày kết thúc | người dùng xuất | báo From date / To date không hợp lệ và không xuất | VAL-002 |
| AC-009 | Noah được đưa đến lúc 13:30 | hệ thống hiển thị danh sách | Giờ đến 13:30 | BR-007 |
| AC-010 | Millie tạm nghỉ từ 24/11 đến 01/12/2026 | người dùng chọn ngày 25/11/2026 | không có dòng của Millie | BR-009 |
| AC-011 | Ethan đo 36.6 °C lúc đưa và 36.8 °C lúc đón | hệ thống hiển thị danh sách | Nhiệt độ lúc đưa 36.6 °C, Nhiệt độ lúc đón 36.8 °C | BR-003 |

#### Dependencies (Phụ thuộc)

App (nhận / trả trẻ, người đưa / người đón, ảnh); danh sách người được phép đón (Children & Families); dịch vụ xe bus; Temporary Withdrawal (Joining & leaving); đo nhiệt độ (BBA-74).

### 6.2 BBA-73: US-002 - Thêm thông tin đưa / đón trên SMS

#### User Story

Là Centre Director có quyền, tôi muốn thêm thông tin đưa / đón còn thiếu trên SMS, kèm lý do, để bổ sung thông tin App chưa ghi.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Hệ thống phải cho người dùng có quyền thêm thông tin đưa / đón còn thiếu trên SMS, kèm lý do: giờ đến, người đưa, nhiệt độ lúc đưa, giờ về, người đón, nhiệt độ lúc đón, ảnh bàn giao (BR-004, BR-005, BR-006, BR-010, BR-011, BR-012). |
| FR-006 | Mỗi lần thêm phải qua duyệt; thông tin được ghi nhận và hiển thị sau khi duyệt (BR-013, BR-014). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Attendance, chọn trẻ, Centre, ngày cần thêm thông tin trong phạm vi được cấp.
2. Hệ thống hiển thị thông tin hiện có ở dạng chỉ xem. Người dùng nhập thông tin còn thiếu và lý do (FR-005).
3. Người dùng chọn Save. Hệ thống kiểm tra quyền và dữ liệu (VAL-003 đến VAL-007), rồi gửi yêu cầu đi duyệt (FR-006).
4. Người duyệt chọn Approve trong My approvals; hệ thống ghi nhận thông tin, hiển thị ở US-001 và ghi lịch sử (BR-013, BR-014).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người đưa không có trong danh sách người thân của trẻ: người dùng chọn Someone else, nhập họ tên và quan hệ với trẻ (BR-004).
2. Người duyệt chọn Reject: thông tin không được ghi nhận (BR-013).
3. Người dùng đóng màn hình hoặc chọn Cancel trước khi lưu: hệ thống không gửi yêu cầu.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền hoặc bản ghi ngoài phạm vi: hệ thống từ chối (VAL-003).
2. Không lưu được: hệ thống báo lỗi theo hành vi chuẩn và không gửi yêu cầu.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-010 | Trên SMS chỉ được thêm mới thông tin đưa / đón; không được sửa hay xoá bất kỳ thông tin nào đã có, kể cả khi trẻ đã có thông tin điểm danh buổi sáng. |
| BR-011 | Sau khi thêm, thông tin điểm danh của trẻ phải có giờ đến, giờ về, người đưa và người đón. |
| BR-012 | Mỗi lần thêm bắt buộc có lý do. Lý do theo quy định tại BBA-77. |
| BR-013 | Mỗi lần thêm phải qua duyệt theo approval route (BBA-53), duyệt trong My approvals (BBA-52). Thông tin chỉ được ghi nhận khi được duyệt; bị từ chối thì không ghi nhận. |
| BR-014 | Lưu lịch sử mỗi lần thêm: giá trị thêm, lý do, người thêm, người duyệt, kết quả duyệt, thời điểm. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Người dùng không có quyền thêm hoặc bản ghi ngoài phạm vi. | Từ chối, không gửi yêu cầu. |
| VAL-004 | Sau khi thêm, vẫn thiếu giờ đến, giờ về, người đưa hoặc người đón. | Báo lỗi tại trường và không gửi yêu cầu. |
| VAL-005 | Không nhập lý do. | Báo lỗi tại trường Lý do và không gửi yêu cầu. |
| VAL-006 | Someone else thiếu họ tên hoặc quan hệ. | Báo “Enter the name and relationship of the adult.” và không gửi yêu cầu. |
| VAL-007 | Người đón không có trong danh sách người được phép đón. | Báo “Only a person authorised to collect this child may be named here.” và không gửi yêu cầu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-73: UI-US-002 - Thêm thông tin đưa / đón trên SMS | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Trẻ / Centre / Ngày | Hiển thị / chọn | Có | Theo bản ghi đã chọn | VAL-003 | Xác định dữ liệu cần thêm. |
| Thông tin đã có | Hiển thị | — | Chỉ xem | BR-010 | Không sửa, không xoá. |
| Giờ đến | Ngày giờ | Khi còn thiếu | Trống khi còn thiếu | VAL-004 | Nhập theo múi giờ của người dùng (BR-007). |
| Người đưa | Chọn | Khi còn thiếu | Trống khi còn thiếu | VAL-004; VAL-006 | Người trong danh sách, Someone else, Bus driver (BR-004; BR-005). |
| Họ tên, Quan hệ (Someone else) | Ô nhập | Khi chọn Someone else | Trống | VAL-006 | Thông tin người đưa ngoài danh sách. |
| Nhiệt độ lúc đưa | Số (°C) | Không | Trống khi còn thiếu | — | Theo BBA-74. |
| Giờ về | Ngày giờ | Khi còn thiếu | Trống khi còn thiếu | VAL-004 | Nhập theo múi giờ của người dùng. |
| Người đón | Chọn | Khi còn thiếu | Trống khi còn thiếu | VAL-004; VAL-007 | Người được phép đón, Bus attendant (BR-005; BR-006). |
| Nhiệt độ lúc đón | Số (°C) | Không | Trống khi còn thiếu | — | Theo BBA-74. |
| Ảnh lúc đưa / Ảnh lúc đón | Ảnh | Không | Trống khi còn thiếu | BR-001 | Tải ảnh tương ứng. |
| Lý do | Chọn / ô nhập | Có | Trống | VAL-005 | Lý do thêm thông tin, theo BBA-77 (BR-012). |
| Save | Thao tác | Theo quyền | — | VAL-003 đến VAL-007 | Gửi yêu cầu đi duyệt (BR-013). |
| Cancel | Thao tác | — | Trong khi dùng màn hình | Hành vi chuẩn | Đóng màn hình, không gửi yêu cầu. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Lưu yêu cầu thêm thông tin kèm lý do và kết quả duyệt; thông tin được duyệt lưu vào dữ liệu đưa / đón, gồm cả nhiệt độ và ảnh bàn giao. Ghi lịch sử theo BR-014. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-012 | App chưa ghi thông tin đưa / đón của Ethan ngày 25/11/2026 | người dùng nhập giờ đến 08:12, người đưa Serena Lim, giờ về 17:22, người đón Daniel Lim, lý do, rồi Save | yêu cầu được gửi đi duyệt | FR-005; FR-006; BR-011; BR-012; BR-013 |
| AC-013 | yêu cầu của Ethan đang chờ duyệt | người duyệt chọn Approve | danh sách hiện thông tin mới và lý do; lịch sử có giá trị thêm, lý do, người thêm, người duyệt, thời điểm | FR-006; BR-013; BR-014; DATA-003 |
| AC-014 | yêu cầu của Ethan đang chờ duyệt | người duyệt chọn Reject | thông tin không được ghi nhận; lịch sử có kết quả Reject | BR-013; BR-014 |
| AC-015 | App đã ghi giờ đến và người đưa của Mia | người dùng mở màn hình thêm | giờ đến và người đưa ở dạng chỉ xem, không sửa được | BR-010 |
| AC-016 | Người dùng không có quyền thêm | người dùng Save | hệ thống từ chối | VAL-003 |
| AC-017 | Người dùng nhập giờ về nhưng không chọn người đón | người dùng Save | báo lỗi tại trường và không gửi yêu cầu | BR-011; VAL-004 |
| AC-018 | App đã ghi Mia đến 08:00, người đưa mẹ; chưa có phần về | người dùng chỉ nhập giờ về 17:00, người đón bố, lý do, rồi Save | yêu cầu được gửi đi duyệt; phần đến giữ nguyên | BR-010; BR-011 |
| AC-019 | Người dùng nhập đủ thông tin nhưng để trống lý do | người dùng Save | báo lỗi tại trường Lý do và không gửi yêu cầu | BR-012; VAL-005 |
| AC-020 | Người dùng chọn Someone else, để trống quan hệ | người dùng Save | báo “Enter the name and relationship of the adult.” và không gửi yêu cầu | BR-004; VAL-006 |
| AC-021 | Danh sách người được phép đón của Ethan có Serena Lim và Daniel Lim; Ethan không đi xe bus | người dùng mở danh sách Người đón | chỉ có Serena Lim và Daniel Lim; không có Bus attendant | BR-005; BR-006; VAL-007 |
| AC-022 | Người dùng đang nhập | người dùng chọn Cancel trước khi lưu | đóng màn hình, không gửi yêu cầu | FR-005 |

#### Dependencies (Phụ thuộc)

US-001; danh sách người được phép đón (Children & Families); dịch vụ xe bus; lý do (BBA-77); approval route (BBA-53); My approvals (BBA-52); đo nhiệt độ (BBA-74).

## 7. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Đưa trẻ (Drop-off) | Trẻ được đưa đến Centre, kèm giờ đến và người đưa. |
| Đón trẻ (Pick-up) | Trẻ được đón về, kèm giờ về và người đón. |
| Người được phép đón | Người có trong danh sách đón của trẻ (dữ liệu có sẵn ở hồ sơ trẻ). |
| Someone else | Người đưa trẻ không có trong danh sách người thân của trẻ; người dùng nhập họ tên và quan hệ với trẻ. |
| Đang ở trường | Trẻ có giờ đến và chưa có giờ về. |
| Nguồn ghi | App hoặc tài khoản thêm dữ liệu trên SMS. |

### Phụ lục B. Cột xuất dữ liệu đưa / đón

File xuất gồm các cột sau, theo khoảng ngày đã chọn và phạm vi Centre được cấp. Thao tác xuất, định dạng file và bảo vệ dữ liệu theo chức năng xuất dữ liệu chuẩn.

| STT | Cột | Ý nghĩa / Dữ liệu |
|---|---|---|
| 1 | Date | Ngày của bản ghi. |
| 2 | Child ID | Mã trẻ. |
| 3 | Child | Họ tên trẻ. |
| 4 | Class | Lớp của trẻ. |
| 5 | Centre | Centre của trẻ. |
| 6 | Arrival | Giờ đến. |
| 7 | Departure | Giờ về. |
| 8 | In building | Yes khi trẻ đang ở trường (BR-002), No trong trường hợp khác. |
