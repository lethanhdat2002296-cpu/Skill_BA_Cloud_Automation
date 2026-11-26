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

Tài liệu đặc tả việc quản lý thông tin đưa / đón trẻ trên SMS: xem giờ đến, giờ về, người đưa, người đón, quan hệ với trẻ và ảnh bàn giao; tìm kiếm, lọc; nhận biết trẻ đang ở trường; xuất dữ liệu; và cho người dùng có quyền ghi hoặc sửa thông tin đưa / đón ngay trên SMS.

Thông tin đưa / đón được ghi trên App khi nhân viên nhận và trả trẻ, rồi cung cấp cho SMS. Luồng và màn hình trên App thuộc đặc tả của App.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Xem, tìm kiếm, lọc thông tin đưa / đón trên SMS; xem ảnh bàn giao lúc đưa và lúc đón; nhận biết trẻ đang ở trường; xuất dữ liệu; người dùng có quyền ghi hoặc sửa thông tin đưa / đón; lưu lịch sử cập nhật. | Luồng và màn hình nhận / trả trẻ trên App; chụp ảnh và đồng bộ dữ liệu của App; tạo, thêm, duyệt người được phép đón (Children & Families, Parents App); ghi và sửa kết quả điểm danh Có mặt / Vắng (BBA-77); đo nhiệt độ (BBA-74); đến muộn (BBA-75); thông báo cho phụ huynh. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Centre Director (CD) | Trẻ trong các Centre được cấp. | Xem dữ liệu và ảnh; ghi và sửa thông tin đưa / đón. |
| Authorised SMS user | Dữ liệu trong phạm vi được cấp. | Xem dữ liệu, mở ảnh, tìm kiếm, lọc, xuất dữ liệu; ghi và sửa thông tin đưa / đón theo quyền. |
| System | Thông tin đưa / đón và hồ sơ trẻ liên quan. | Cung cấp dữ liệu để hiển thị và xuất; xác định trẻ đang ở trường; kiểm tra quyền; ghi lịch sử cập nhật. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-73 gồm hai User Story trên SMS, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Attendance** | Xem và xuất thông tin đưa / đón | Xem thông tin đưa / đón, ảnh bàn giao và trẻ đang ở trường; tìm kiếm, lọc, xuất dữ liệu. | BBA-73: US-001 |
| **Attendance** | Ghi và sửa thông tin đưa / đón | Người dùng có quyền ghi hoặc sửa giờ đến, người đưa, giờ về, người đón trên SMS. | BBA-73: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-73: US-001 - Xem và xuất thông tin đưa / đón

#### User Story

Là người dùng có quyền trên SMS, tôi muốn xem thông tin đưa / đón và ảnh bàn giao, tìm kiếm, lọc và xuất dữ liệu, để theo dõi ai đưa, ai đón trẻ, lúc mấy giờ và trẻ nào đang ở trường.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải hiển thị thông tin đưa / đón của trẻ trong phạm vi dữ liệu được cấp. |
| FR-002 | Hệ thống phải cho tìm theo tên hoặc mã trẻ và lọc theo Centre, lớp, ngày. |
| FR-003 | Hệ thống phải cho người dùng có quyền xuất dữ liệu đưa / đón theo khoảng ngày đã chọn, với các cột ở mục 8. |
| FR-004 | Hệ thống phải hiển thị ảnh bàn giao lúc đưa và lúc đón, và cho người dùng có quyền mở từng ảnh. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Daily Operations › Attendance.
2. Hệ thống hiển thị thông tin đưa / đón và ảnh bàn giao trong phạm vi được cấp.
3. Người dùng tìm theo tên / mã trẻ hoặc chọn Centre, lớp, ngày; chọn một ảnh để mở.
4. Người dùng chọn khoảng ngày và xuất dữ liệu bằng chức năng xuất dữ liệu chuẩn.

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có dữ liệu phù hợp: hệ thống hiển thị kết quả trống theo thiết kế chuẩn.
2. Trẻ chưa có giờ đến, giờ về hoặc ảnh: ô thiếu hiển thị "—".

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền hoặc yêu cầu dữ liệu ngoài phạm vi: hệ thống không cung cấp dữ liệu đó.
2. Không tải hoặc không xuất được dữ liệu: hệ thống báo lỗi theo hành vi chuẩn của hệ thống.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Xem dữ liệu, mở ảnh và xuất dữ liệu theo quyền người dùng và phạm vi dữ liệu Centre. |
| BR-002 | Trẻ được coi là đang ở trường khi có giờ đến và chưa có giờ về. |
| BR-003 | Danh sách gồm: ngày, tên trẻ, lớp, Centre, giờ đến, người đưa, quan hệ, giờ về, người đón, quan hệ, ảnh lúc đưa, ảnh lúc đón. Ô thiếu hiển thị "—"; ảnh có sẵn thì mở được. |
| BR-004 | Người đưa là người trong danh sách của trẻ, người khác ngoài danh sách (ghi tên và quan hệ, kèm "Someone else") hoặc tài xế xe bus ("Bus driver", kèm số xe). Người đón là người trong danh sách người được phép đón hoặc phụ xe bus ("Bus attendant", kèm số xe). |
| BR-005 | Giờ đến / giờ về là ngày giờ lúc nhân viên lưu trên App (hoặc giờ người dùng ghi trên SMS), hiển thị theo múi giờ của người dùng, không gắn với buổi hay giờ cố định trong ngày. |
| BR-006 | Xuất dữ liệu dùng các cột ở mục 8, theo khoảng ngày đã chọn và phạm vi dữ liệu được cấp; theo chức năng xuất dữ liệu chuẩn. |
| BR-007 | Trẻ đang tạm nghỉ (Temporary Withdrawal) không hiện trong các ngày thuộc thời gian tạm nghỉ. |

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
| Date | Chọn ngày | Có | Ngày hiện tại | BR-005 | Lọc theo ngày, theo múi giờ của người dùng. |
| Tên trẻ, lớp, Centre | Hiển thị | Có | Từ hồ sơ trẻ | BR-003 | Xác định trẻ. |
| Giờ đến / Giờ về | Hiển thị | Khi có | "—" khi thiếu | BR-005 | Ngày giờ ghi nhận, theo múi giờ của người dùng. |
| Người đưa / Người đón | Hiển thị | Khi có | "—" khi thiếu | BR-004 | Tên người đưa / người đón. |
| Quan hệ | Hiển thị | Khi có | "—" khi thiếu | BR-004 | Quan hệ với trẻ; Someone else hoặc số xe bus. |
| Ảnh lúc đưa / Ảnh lúc đón | Ảnh / mở | Khi có | Ảnh đã lưu | BR-001; FR-004 | Chọn để mở ảnh trẻ cùng người đưa / người đón. |
| Đang ở trường | Hiển thị | Có | Từ dữ liệu SMS | BR-002 | Dấu hiệu trẻ đang ở trường. |
| From date / To date | Chọn ngày | Khi xuất | From date = To date = ngày hiện tại | VAL-002 | Khoảng ngày xuất. |
| Export data | Thao tác | Theo quyền | Theo điều kiện xuất | BR-001; BR-006; VAL-002 | Xuất theo mục 8 và quy tắc chuẩn. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Dùng hồ sơ trẻ, Centre, lớp, ngày giờ đến / về, người đưa / người đón, quan hệ, ảnh bàn giao và nguồn ghi (App / SMS) để hiển thị và xuất dữ liệu. |
| DATA-002 | Lưu lịch sử cập nhật thông tin đưa / đón, gồm cả dữ liệu mới nhất từ App: giá trị cũ, giá trị mới, người cập nhật, thời điểm. Xem danh sách hay mở ảnh không tạo bản ghi đưa / đón. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Người dùng có quyền vào Attendance | người dùng mở màn hình | mặc định Centre của người dùng và ngày hiện tại; hiển thị thông tin đưa / đón và ảnh trong phạm vi được cấp | FR-001; BR-001; BR-003 |
| AC-002 | Có dữ liệu của nhiều Centre | người dùng tìm theo tên và chọn Centre, lớp, ngày | chỉ hiện dữ liệu khớp trong phạm vi được cấp | FR-002; BR-001; VAL-001 |
| AC-003 | Ethan có giờ đến 08:12, chưa có giờ về | hệ thống tải dữ liệu | Ethan có dấu hiệu đang ở trường | BR-002 |
| AC-004 | Ethan chưa có giờ về và ảnh lúc đón | hệ thống hiển thị danh sách | các ô thiếu hiện "—" | BR-003 |
| AC-005 | Noah được người giúp việc Siti đưa đến; Lucas đi xe bus Bus 2 | hệ thống hiển thị danh sách | Noah: Người đưa Siti, Quan hệ "Helper (Someone else)"; Lucas: Người đưa "Bus driver", Quan hệ "Bus 2" | BR-004 |
| AC-006 | Ethan có ảnh lúc đưa và ảnh lúc đón, người dùng có quyền xem | người dùng chọn từng ảnh | mở đúng ảnh tương ứng | FR-004; BR-001 |
| AC-007 | Người dùng có quyền xuất, không đổi From date / To date mặc định | người dùng xuất dữ liệu | From date và To date là ngày hiện tại; file có các cột ở mục 8 và dữ liệu trong phạm vi được cấp | FR-003; BR-006 |
| AC-008 | Ngày bắt đầu xuất sau ngày kết thúc | người dùng xuất | báo From date / To date không hợp lệ và không xuất | VAL-002 |
| AC-009 | Noah được đưa đến lúc 13:30 | hệ thống hiển thị danh sách | Giờ đến 13:30 | BR-005 |
| AC-010 | Millie tạm nghỉ từ 24/11 đến 01/12/2026 | người dùng chọn ngày 25/11/2026 | không có dòng của Millie | BR-007 |

#### Dependencies (Phụ thuộc)

App (nhận / trả trẻ, người đưa / người đón, ảnh); danh sách người được phép đón (Children & Families); dịch vụ xe bus; Temporary Withdrawal (Joining & leaving).

### 6.2 BBA-73: US-002 - Ghi và sửa thông tin đưa / đón trên SMS

#### User Story

Là Centre Director có quyền, tôi muốn ghi hoặc sửa thông tin đưa / đón trên SMS, để bổ sung thông tin còn thiếu hoặc sửa thông tin sai.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Hệ thống phải cho người dùng có quyền ghi hoặc sửa thông tin đưa / đón trên SMS: giờ đến, người đưa, giờ về, người đón, ảnh bàn giao. |
| FR-006 | Sau khi lưu, hệ thống phải hiển thị dữ liệu đã cập nhật và ghi lịch sử. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Attendance, chọn trẻ, Centre, ngày cần ghi hoặc sửa trong phạm vi được cấp.
2. Hệ thống hiển thị dữ liệu hiện có. Người dùng nhập hoặc sửa giờ đến, người đưa, giờ về, người đón, ảnh bàn giao.
3. Người dùng chọn Save. Hệ thống kiểm tra quyền và dữ liệu (VAL-003 đến VAL-008); không cần lý do hay duyệt.
4. Hệ thống lưu dữ liệu và ghi lịch sử.

#### Functional Flow - Alternative (Luồng thay thế)

1. Người đưa không có trong danh sách: người dùng chọn Someone else, nhập họ tên và quan hệ với trẻ.
2. Người dùng đóng màn hình hoặc chọn Cancel trước khi lưu: hệ thống không lưu thay đổi.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền sửa hoặc bản ghi ngoài phạm vi: hệ thống từ chối.
2. Không lưu được thay đổi: hệ thống báo lỗi theo hành vi chuẩn và không hiển thị thay đổi chưa lưu như dữ liệu đã lưu.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Người dùng có quyền ghi hoặc sửa giờ đến, người đưa, giờ về, người đón, ảnh bàn giao, kể cả dữ liệu App đã ghi. Không cần lý do hay duyệt, không giới hạn thời gian sửa. |
| BR-009 | Người đưa chọn từ người trong danh sách của trẻ, Someone else (bắt buộc họ tên và quan hệ) hoặc Bus driver (chỉ khi trẻ đi xe bus). Người đón chỉ chọn từ danh sách người được phép đón hoặc Bus attendant (chỉ khi trẻ đi xe bus); không có lựa chọn người lạ hay đón tạm thời. |
| BR-010 | Giờ đến đi cùng người đưa, giờ về đi cùng người đón. Chỉ ghi được thông tin đón khi đã có thông tin đưa; giờ về không sớm hơn giờ đến. |
| BR-011 | Lưu lịch sử mọi lần cập nhật thông tin đưa / đón: giá trị cũ, giá trị mới, người cập nhật, thời điểm. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Người dùng không có quyền sửa hoặc bản ghi ngoài phạm vi. | Từ chối lưu thay đổi. |
| VAL-004 | Có giờ đến mà không có người đưa (hoặc ngược lại); có giờ về mà không có người đón (hoặc ngược lại). | Báo lỗi tại trường và không lưu. |
| VAL-005 | Có thông tin đón khi chưa có thông tin đưa. | Báo "Phải có Drop-off trước khi ghi Pick-up." và không lưu. |
| VAL-006 | Giờ về sớm hơn giờ đến. | Báo "Giờ trả trẻ không thể sớm hơn giờ đến." và không lưu. |
| VAL-007 | Someone else thiếu họ tên hoặc quan hệ. | Báo "Enter the name and relationship of the adult." và không lưu. |
| VAL-008 | Người đón không có trong danh sách người được phép đón. | Báo "Only a person authorised to collect this child may be named here." và không lưu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-73: UI-US-002 - Ghi và sửa thông tin đưa / đón trên SMS | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Trẻ / Centre / Ngày | Hiển thị / chọn | Có | Theo bản ghi đã chọn | VAL-003 | Xác định dữ liệu cần ghi hoặc sửa. |
| Giờ đến | Ngày giờ | Khi có người đưa | Giá trị hiện có hoặc trống | VAL-004; VAL-006 | Nhập hoặc sửa, theo múi giờ của người dùng (BR-005). |
| Người đưa | Chọn | Khi có giờ đến | Giá trị hiện có | VAL-004; VAL-007 | Người trong danh sách, Someone else, Bus driver (BR-009). |
| Họ tên, Quan hệ (Someone else) | Ô nhập | Khi chọn Someone else | Trống | VAL-007 | Thông tin người đưa ngoài danh sách. |
| Giờ về | Ngày giờ | Khi có người đón | Giá trị hiện có hoặc trống | VAL-004; VAL-005; VAL-006 | Nhập hoặc sửa. |
| Người đón | Chọn | Khi có giờ về | Giá trị hiện có | VAL-004; VAL-008 | Người được phép đón, Bus attendant (BR-009). |
| Ảnh lúc đưa / Ảnh lúc đón | Ảnh | Khi có | Ảnh hiện có, nếu có | BR-001; BR-008 | Mở và cập nhật ảnh tương ứng. |
| Save | Thao tác | Theo quyền | Khi ghi hoặc sửa | VAL-003 đến VAL-008 | Lưu và ghi lịch sử; không cần lý do hay duyệt. |
| Cancel | Thao tác | — | Trong khi dùng màn hình | Hành vi chuẩn | Đóng màn hình, không lưu thay đổi. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Lưu dữ liệu người dùng ghi hoặc sửa, gồm cả ảnh bàn giao. Ghi lịch sử mọi lần cập nhật theo BR-011; không cần lý do hay thông tin duyệt. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-011 | Người dùng có quyền, bản ghi trong phạm vi | người dùng sửa người đưa, giờ về, người đón, ảnh rồi lưu dữ liệu hợp lệ | hiển thị dữ liệu đã cập nhật, mở được ảnh mới; lịch sử có giá trị cũ / mới, người cập nhật, thời điểm | FR-005; FR-006; BR-011; DATA-003 |
| AC-012 | App chưa ghi thông tin đón của Ethan | người dùng ghi giờ về 17:22 và người đón Daniel Lim rồi lưu | lưu dữ liệu; Ethan không còn dấu hiệu đang ở trường; lịch sử có dòng cập nhật | FR-005; BR-002; BR-011 |
| AC-013 | Dữ liệu sửa hợp lệ, kể cả dữ liệu của ngày trước | người dùng lưu mà không nhập lý do | không cần lý do hay duyệt, không giới hạn thời gian; lưu dữ liệu và ghi lịch sử | BR-008; BR-011 |
| AC-014 | Người dùng đang sửa | người dùng chọn Cancel trước khi lưu | đóng màn hình, không lưu thay đổi | FR-005 |
| AC-015 | Người dùng không có quyền sửa | người dùng lưu thay đổi | hệ thống từ chối | VAL-003 |
| AC-016 | Người dùng chọn Someone else, để trống quan hệ | người dùng lưu | báo "Enter the name and relationship of the adult." và không lưu | BR-009; VAL-007 |
| AC-017 | Người dùng nhập giờ về nhưng không chọn người đón | người dùng lưu | báo lỗi tại trường và không lưu | BR-010; VAL-004 |
| AC-018 | Mia chưa có thông tin đưa | người dùng ghi giờ về và người đón rồi lưu | báo "Phải có Drop-off trước khi ghi Pick-up." và không lưu | BR-010; VAL-005 |
| AC-019 | Ethan đến lúc 08:12 | người dùng ghi giờ về 07:50 rồi lưu | báo "Giờ trả trẻ không thể sớm hơn giờ đến." và không lưu | BR-010; VAL-006 |
| AC-020 | Danh sách người được phép đón của Ethan có Serena Lim và Daniel Lim; Ethan không đi xe bus | người dùng mở danh sách Người đón | chỉ có Serena Lim và Daniel Lim; không có Bus attendant | BR-009; VAL-008 |

#### Dependencies (Phụ thuộc)

US-001; danh sách người được phép đón (Children & Families); dịch vụ xe bus.

## 7. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Đưa trẻ (Drop-off) | Trẻ được đưa đến Centre, kèm giờ đến và người đưa. |
| Đón trẻ (Pick-up) | Trẻ được đón về, kèm giờ về và người đón. |
| Người được phép đón | Người có trong danh sách đón của trẻ (dữ liệu có sẵn ở hồ sơ trẻ). |
| Someone else | Người đưa trẻ không có trong danh sách của trẻ, ghi kèm họ tên và quan hệ. |
| Đang ở trường | Trẻ có giờ đến và chưa có giờ về. |
| Nguồn ghi | App hoặc tài khoản ghi dữ liệu trên SMS. |

## 8. Phụ lục B. Cột xuất dữ liệu đưa / đón

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
