# Child Record Tabs – All

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Child record |
| Tính năng | BBA-67 Các tab của hồ sơ trẻ (Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History) |
| Mã tài liệu | FRD-3.1.1.02_Child_Record_Tabs |
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

**Mức sẵn sàng:** Đã đặc tả nội dung tổng quan, thao tác theo quyền và liên kết sang module của từng tab.

## 2. Mục đích và bối cảnh

Hồ sơ trẻ gom về một chỗ những gì các module ghi nhận về trẻ. Tài liệu này mô tả tổng quan từng tab sau tab Overview: tab hiển thị gì, người dùng có quyền được thao tác gì ngay trên tab, thao tác nào mở sang module sở hữu. Chi tiết nghiệp vụ của từng thao tác nằm ở FRS của module sở hữu.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Các tab Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History: nội dung tổng quan, thao tác theo quyền, liên kết sang module sở hữu, trạng thái rỗng. | Header, tab Overview, sửa hồ sơ trẻ (BBA-66). Anh chị em và người được đón trên tab Guardians (task khác). Medical alert (BBA-68), danh sách dị ứng (BBA-69), chiều cao cân nặng (BBA-70), giấy tờ và consent (BBA-71), đưa đón (BBA-73), đo nhiệt độ (BBA-74). Chi tiết nghiệp vụ của Joining & leaving, Learning › Enrichment, Fees & Payments, Communication. Parents App. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ trong phạm vi dữ liệu được cấp (HQ: mọi Centre; nhân viên Centre: Centre của mình; Teacher: lớp của mình). | Xem các tab được cấp quyền; thực hiện thao tác trên tab theo quyền. |
| System | Dữ liệu các module của trẻ. | Đọc dữ liệu module, áp quyền, che hoặc ẩn trường được bảo vệ, ghi History. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy tab hoặc hồ sơ trẻ. |

**Quy tắc chung:** Quyền xem từng tab và từng thao tác do BBA cấu hình trong Roles & permissions; thao tác không có quyền thì không hiển thị. Tài liệu này không gán cứng quyền cho vai trò nào.

## 5. Tổng quan tính năng và phân rã chức năng

| Tab | Nội dung | Thao tác trên tab (theo quyền) | Module sở hữu | User Story |
|---|---|---|---|---|
| **Enrolment** | Lịch sử quá trình ghi danh của trẻ; flag của trẻ. | Đặt flag; tạo withdrawal, temporary withdrawal, transfer (chuyển sang màn hình module); ghi change log. | Enrolment; Joining & leaving | US-001 |
| **Enrichment** | Lớp enrichment trẻ đang học, đã học, đang chờ HQ xác nhận. | Không có; chỉ hiển thị. | Learning | US-002 |
| **Guardians** | Bảng người giám hộ và vai trò. | Thêm, sửa; xóa phải qua duyệt; ghi change log. | Children & Families | US-003 |
| **Attendance** | Bảng giờ vào, giờ ra, nhiệt độ theo ngày; xe đưa rước (chỉ xem). | Không có; chỉ hiển thị. | Daily Operations | US-004 |
| **Finance** | Việc cần làm, trợ cấp, GIRO/CDA, cách thanh toán, lịch thanh toán, đặt cọc, hoá đơn, công nợ, giảm giá. | Gửi nhắc phí, review trợ cấp, đổi Bill to, xuất GIRO, quản lý đặt cọc, thêm giảm giá. | Fees & Payments | US-005 |
| **Health** | Thông tin từ gia đình, ghi chú nhân viên, tiêm chủng, nhiệt độ theo ngày, chiều cao cân nặng theo kỳ. | Thêm lần đo nhiệt độ; thêm, sửa ghi chú nhân viên. | Children & Families; Daily Operations | US-006 |
| **Communication** | Các cuộc chat có phụ huynh của trẻ. | Bắt đầu tin nhắn, trả lời. | Communication | US-007 |
| **Documents** | Giấy tờ của trẻ và consent. | Tải lên, tải lại giấy tờ. | Children & Families; Communication | US-008 |
| **History** | Nhật ký mọi thay đổi và lần xem dữ liệu được bảo vệ. | Tìm, lọc, xuất. | Children & Families | US-009 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-67: US-001 - Tab Enrolment

#### User Story

Là người dùng, tôi muốn xem lịch sử quá trình ghi danh của trẻ khi học ở trường, đánh dấu trẻ và tạo các việc rút, tạm nghỉ, chuyển Centre ngay từ hồ sơ trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab hiển thị toàn bộ thông tin nhập học của trẻ (BR-001). |
| FR-002 | Người dùng có quyền đánh dấu trẻ (flag) (BR-002). |
| FR-003 | Người dùng có quyền tạo withdrawal, temporary withdrawal, transfer từ tab Enrolment; hệ thống chuyển sang màn hình của module tương ứng (BR-003). |
| FR-004 | Mọi thay đổi thực hiện từ tab được ghi change log vào tab History (BR-004). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Enrolment; hệ thống hiển thị flag và thông tin nhập học (FR-001).
2. Người dùng chọn Set it ở một flag, chọn giá trị, lưu; hệ thống ghi change log (FR-002, FR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Start a withdrawal / Start a temporary withdrawal / Start a transfer: hệ thống chuyển sang màn hình tạo yêu cầu của Joining & leaving; hệ thống ghi change log (FR-003, FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền: không thấy Set it và các nút Start (BR-002, BR-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi lần ghi danh một dòng: Centre, level, lớp, programme (Full day / Half day), năm học, ngày ghi danh, ngày bắt đầu học, ngày kết thúc hoặc “ongoing”, trạng thái, pháp nhân. Dòng đầu ghi tổng số lần ghi danh và số lần đang chạy. Ghi danh và thay đổi không bị xóa. |
| BR-002 | Tab có 3 flag: SUG Child, Staff Child, KA Child; mỗi flag có giá trị Yes / No, mặc định No. Cạnh mỗi flag hiện quyền lợi tính phí đi kèm: Staff Child gắn với giảm giá “Staff child discount” trong Fees & Payments; SUG Child và KA Child chưa có quy tắc tính phí, hiện “<flag> — no billing rule set. Finance to confirm what this entitles the child to.” |
| BR-003 | Withdrawal, temporary withdrawal, transfer thuộc Joining & leaving. Bấm Start, hệ thống chuyển sang đúng màn hình của module, không mở popup trên tab. Trạng thái ghi danh chỉ đổi qua Joining & leaving. |
| BR-004 | Đánh dấu trẻ và tạo yêu cầu withdrawal, temporary withdrawal, transfer từ tab đều ghi change log vào tab History: nội dung, giá trị cũ → giá trị mới, người thực hiện, thời điểm. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Enrolment | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Flags on this child | Section | — | No | — | SUG / Staff / KA Child, nút Set it (BR-002). |
| Start a case on this child | Nhóm nút | — | Theo quyền | — | Start a withdrawal, Start a temporary withdrawal, Start a transfer; chuyển sang màn hình module (BR-003). |
| Danh sách ghi danh | Danh sách | — | Mới nhất trước | — | BR-001. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Change log của tab Enrolment lưu vào History của trẻ theo BR-004. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | trẻ ghi danh Small Wonder Tampines · Playgroup · Bumblebees, Half Day, năm 2026, đang học | người dùng mở tab Enrolment | dòng ghi danh hiện Centre, level, lớp, programme, năm học, ngày ghi danh, ngày bắt đầu, “ongoing”, Active; đầu danh sách ghi “1 enrolment · 1 running now” | FR-001; BR-001 |
| AC-002 | Staff Child = No | người dùng có quyền chọn Set it, chọn Yes, lưu | flag Staff Child = Yes; History có dòng No → Yes kèm người đổi, thời điểm | FR-002; FR-004; BR-002; BR-004; DATA-001 |
| AC-003 | người dùng có quyền | chọn Start a transfer | hệ thống chuyển sang màn hình tạo Transfer của Joining & leaving cho trẻ, không mở popup; History có dòng tạo yêu cầu transfer | FR-003; BR-003; BR-004 |

#### Dependencies (Phụ thuộc)

Enrolment; Joining & leaving; Fees & Payments (quy tắc tính phí theo flag); tab History (US-009).
### 6.2 BBA-67: US-002 - Tab Enrichment

#### User Story

Là người dùng, tôi muốn xem các lớp enrichment của trẻ, để biết trẻ học gì, khi nào, ở đâu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Tab chỉ hiển thị các lớp enrichment của trẻ đã đăng ký và yêu cầu đang chờ HQ xác nhận (BR-005, BR-006, BR-007). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Enrichment; hệ thống hiển thị danh sách lớp (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ có yêu cầu tham gia lớp đang chờ HQ: dòng lớp có trạng thái Waiting, nằm đầu bảng (BR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa học lớp enrichment nào: hiển thị thông báo rỗng (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Mỗi lớp một dòng: Programme, Centre, Day, From, To, Start date, End date, Status. Status gồm Waiting (chờ HQ xác nhận), Active (đang học), Completed (đã học xong), Withdrawn (đã rút). Lớp đang học có End date “—”. Một trẻ học được nhiều lớp. |
| BR-006 | Thứ tự: lớp Waiting trước, rồi lớp đang học, rồi lớp đã kết thúc. Lớp Waiting chưa có lịch học và ngày: các ô Day, From, To, Start date, End date hiện “—”. |
| BR-007 | Tab chỉ hiển thị thông tin; không có thao tác thêm, sửa, xóa. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Trẻ chưa có lớp enrichment và không có yêu cầu chờ. | Hiển thị “No enrichment programme for this child.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Enrichment | Wireframe BBA-67 (26/11/2026) › tab Enrichment; Prototype: Records › Child › Enrichment |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tiêu đề | Display | — | “Enrichment programmes” | — | Dòng phụ “Pending requests first, followed by current and past programmes.” |
| Tóm tắt | Display | — | — | — | “n programmes · n Waiting · n active”. |
| Bảng Enrichment programmes | Bảng | — | Theo thứ tự BR-006 | VAL-001. | Cột Programme, Centre, Day, From, To, Start date, End date, Status; chỉ xem (BR-005; BR-007). |
| Status | Nhãn | — | — | — | Waiting, Active, Completed, Withdrawn (BR-005). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Tab đọc dữ liệu của Learning; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-004 | trẻ học Speech & Drama (Thứ Năm 15:30–16:30) và Swimming từ 01/07/2026; đã học xong Little Coders (12/01–29/06/2026); đã rút Art Explorers; yêu cầu Mandarin Explorers chờ HQ | người dùng mở tab Enrichment | tóm tắt “5 programmes · 1 Waiting · 2 active”; dòng đầu Mandarin Explorers Waiting, các ô lịch và ngày “—”; tiếp theo Speech & Drama, Swimming Active, End date “—”; sau cùng Little Coders Completed, Art Explorers Withdrawn | FR-005; BR-005; BR-006; DATA-002 |
| AC-005 | người dùng có quyền xem trẻ | mở tab Enrichment | không có thao tác thêm, sửa, xóa | BR-007 |
| AC-006 | trẻ chưa có lớp enrichment | mở tab Enrichment | hiện “No enrichment programme for this child.” | VAL-001 |

#### Dependencies (Phụ thuộc)

Learning › Enrichment.
### 6.3 BBA-67: US-003 - Tab Guardians

#### User Story

Là người dùng, tôi muốn xem và cập nhật người giám hộ của trẻ, để liên hệ đúng người.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Tab hiển thị người giám hộ của trẻ dạng bảng (BR-008). |
| FR-007 | Người dùng có quyền thêm, sửa, xóa người giám hộ; xóa phải qua duyệt (BR-009, BR-010). |
| FR-008 | Mọi thao tác trên tab được ghi change log vào tab History (BR-011). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Guardians; hệ thống hiển thị bảng người giám hộ (FR-006).
2. Người dùng chọn Create guardian hoặc Edit, nhập thông tin và vai trò, lưu; hệ thống ghi change log (FR-007, FR-008).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Remove ở một người giám hộ: hệ thống gửi yêu cầu xóa đi duyệt; người duyệt chọn Approve thì người giám hộ bị xóa (FR-007; BR-010).
2. Người duyệt chọn Reject: người giám hộ giữ nguyên (BR-010).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có quyền: không thấy Create guardian, Edit, Remove (FR-007).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Bảng người giám hộ: họ tên, quan hệ với trẻ, điện thoại, email, vai trò (Primary contact, Emergency contact, Authorised to collect, Billing contact). Một người giám hộ có một hoặc nhiều vai trò. |
| BR-009 | Thêm, sửa người giám hộ có hiệu lực khi lưu. |
| BR-010 | Xóa người giám hộ phải qua duyệt theo approval route (BBA-53), duyệt trong My approvals (BBA-52). Người giám hộ chỉ bị xóa khi được duyệt; bị từ chối thì giữ nguyên. |
| BR-011 | Thêm, sửa, yêu cầu xóa, kết quả duyệt xóa đều ghi change log vào tab History: nội dung, giá trị cũ → giá trị mới, người thực hiện, người duyệt (với xóa), thời điểm. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Guardians | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Bảng Guardians | Bảng | — | — | — | BR-008. |
| Create guardian / Edit | Nút | — | Theo quyền | — | FR-007; BR-009. |
| Remove | Nút | — | Theo quyền | — | Gửi yêu cầu xóa đi duyệt (BR-010). |
| Vai trò | Nhãn chọn | Có ít nhất 1 | — | — | BR-008. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Change log của tab Guardians lưu vào History của trẻ theo BR-011. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | trẻ có người giám hộ Mr Wong (father, Primary contact) | người dùng mở tab Guardians | bảng hiện Mr Wong, quan hệ father, điện thoại, email, vai trò Primary contact | FR-006; BR-008 |
| AC-008 | người dùng có quyền | chọn Create guardian, nhập Mrs Wong, vai trò Emergency contact, lưu | Mrs Wong hiện trong bảng; History có dòng thêm người giám hộ | FR-007; FR-008; BR-009; BR-011; DATA-003 |
| AC-009 | Mrs Wong có trong bảng | người dùng chọn Remove | yêu cầu xóa được gửi đi duyệt; Mrs Wong vẫn trong bảng | FR-007; BR-010 |
| AC-010 | yêu cầu xóa Mrs Wong đang chờ duyệt | người duyệt chọn Approve | Mrs Wong bị xóa khỏi bảng; History có dòng xóa kèm người duyệt | BR-010; BR-011 |
| AC-011 | yêu cầu xóa Mrs Wong đang chờ duyệt | người duyệt chọn Reject | Mrs Wong giữ nguyên trong bảng | BR-010 |

#### Dependencies (Phụ thuộc)

Approval routes (BBA-53); My approvals (BBA-52); tab History (US-009).
### 6.4 BBA-67: US-004 - Tab Attendance

#### User Story

Là người dùng, tôi muốn xem giờ vào, giờ ra và nhiệt độ của trẻ theo từng ngày, để trả lời phụ huynh mà không phải mở màn điểm danh của lớp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-009 | Tab hiển thị thông tin điểm danh của trẻ dạng bảng: giờ vào, giờ ra, nhiệt độ (BR-012). |
| FR-010 | Tab hiển thị xe đưa rước của trẻ ở dạng chỉ xem (BR-013). |
| FR-011 | Tab chỉ hiển thị; không có thao tác thêm, sửa, xóa (BR-014). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Attendance; hệ thống hiển thị bảng điểm danh và xe đưa rước của trẻ (FR-009, FR-010).

#### Functional Flow - Alternative (Luồng thay thế)

1. Ngày chưa có giờ ra hoặc chưa đo nhiệt độ: ô thiếu hiển thị “—” (BR-012).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa có thông tin điểm danh: hiển thị thông báo rỗng (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-012 | Bảng mỗi ngày một dòng: ngày, giờ vào, giờ ra, nhiệt độ đo được trong ngày; mới nhất trước. Dữ liệu lấy từ điểm danh (BBA-73) và đo nhiệt độ (BBA-74). |
| BR-013 | Xe đưa rước (tuyến xe hoặc No bus) lấy từ thông tin điểm danh; chỉ xem, không chọn được trên tab. |
| BR-014 | Tab không có thao tác thêm, sửa, xóa. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Trẻ chưa có thông tin điểm danh. | Hiển thị bảng rỗng theo thiết kế chuẩn. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Attendance | |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Xe đưa rước | Hiển thị | — | Theo điểm danh | — | Chỉ xem (BR-013). |
| Bảng điểm danh | Bảng | — | Mới nhất trước | VAL-002. | Cột Ngày, Giờ vào, Giờ ra, Nhiệt độ; “—” khi thiếu (BR-012; BR-014). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Tab đọc dữ liệu điểm danh và nhiệt độ; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-012 | ngày 25/11/2026 trẻ vào 08:03, ra 17:20, đo 36.7 °C lúc đến | người dùng mở tab Attendance | dòng 25/11/2026 hiện giờ vào 08:03, giờ ra 17:20, nhiệt độ 36.7 °C | FR-009; BR-012; DATA-004 |
| AC-013 | ngày 26/11/2026 trẻ vào 08:10, chưa ra, chưa đo nhiệt độ | người dùng mở tab Attendance | giờ ra và nhiệt độ hiện “—” | BR-012 |
| AC-014 | trẻ đi Bus A — Tampines North loop | người dùng mở tab Attendance | xe đưa rước hiện Bus A, không chọn hay đổi được | FR-010; BR-013 |
| AC-015 | người dùng có quyền xem trẻ | mở tab Attendance | không có thao tác thêm, sửa, xóa | FR-011; BR-014 |
| AC-016 | trẻ chưa có thông tin điểm danh | mở tab Attendance | bảng rỗng | VAL-002 |

#### Dependencies (Phụ thuộc)

Điểm danh đưa / đón (BBA-73); đo nhiệt độ (BBA-74).
### 6.5 BBA-67: US-005 - Tab Finance

#### User Story

Là người dùng, tôi muốn thấy tình hình tài chính của trẻ và xử lý các việc tài chính thường gặp ngay trên hồ sơ, để không phải mở từng màn của Fees & Payments.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-012 | Tab hiển thị tổng quan tài chính của trẻ (BR-015, BR-016). |
| FR-013 | Người dùng có quyền thực hiện các thao tác tài chính trên tab hoặc mở màn tương ứng của Fees & Payments (BR-017). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Finance; hệ thống hiển thị các khối tài chính (FR-012).
2. Người dùng chọn một thao tác ở khối tương ứng (FR-013).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn See what the parent sees: hệ thống hiển thị tài chính như phụ huynh thấy (FR-012).
2. Người dùng chọn số hoá đơn: hệ thống mở chi tiết hoá đơn (FR-013).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ thuộc Centre Malaysia: không có khối GIRO and CDA accounts và trợ cấp ECDA (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-015 | Các khối: What needs doing (hoá đơn quá hạn); What the flags have done; Subsidies; Bill to; GIRO and CDA accounts; How this family pays (Payment method, citizenship tính phí, tiền đặt cọc đang giữ); Payment schedule; Deposit; Invoices (theo loại); Outstanding and chasing (theo nhóm tuổi nợ); Discounts. |
| BR-016 | Số tài khoản ngân hàng và tiền đặt cọc là trường được bảo vệ: hiển thị đầy đủ, che hoặc ẩn theo quyền; mỗi lần xem đầy đủ ghi History. |
| BR-017 | Thao tác trên tab: Send a reminder (hoá đơn quá hạn), Review child (trợ cấp), Bill to Parent / Company (Save), Export GIRO, Manage (đặt cọc), Add a discount, Open schedule, Open (công nợ). Quy tắc nghiệp vụ của từng thao tác theo Fees & Payments. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Trẻ thuộc Centre Malaysia. | Ẩn khối GIRO and CDA accounts và trợ cấp ECDA. |
| VAL-004 | Vai trò không có quyền xem Fees & Payments. | Không hiển thị tab Finance. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Finance | Prototype: Records › Child › Finance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| See what the parent sees | Nút | — | — | — | Xem như phụ huynh. |
| Các khối tài chính | Section | — | — | VAL-003. | BR-015. |
| Nút thao tác | Nút / liên kết | — | Theo quyền | — | BR-017. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-005 | Thao tác làm trên tab (Bill to, giảm giá, đặt cọc, nhắc phí) lưu theo Fees & Payments và ghi History của trẻ. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-017 | hoá đơn SW-TAM-ADH-2026-10-0003 quá hạn 37 ngày, SGD 34.88 | người dùng mở tab Finance | What needs doing hiện hoá đơn kèm số ngày quá hạn, số tiền và nút Send a reminder; Outstanding hiện nhóm 31–60 days | FR-012; BR-015 |
| AC-018 | người dùng không có quyền xem đầy đủ tiền đặt cọc | mở tab Finance | tiền đặt cọc bị che | BR-016 |
| AC-019 | Bill to chưa chọn | người dùng có quyền chọn Company, Save | Bill to = Company; History có dòng thay đổi | FR-013; BR-017; DATA-005 |
| AC-020 | trẻ thuộc Centre Malaysia | mở tab Finance | không có khối GIRO and CDA accounts và trợ cấp ECDA | VAL-003 |
| AC-021 | vai trò không có quyền Fees & Payments | mở hồ sơ trẻ | không có tab Finance | VAL-004 |

#### Dependencies (Phụ thuộc)

Fees & Payments (hoá đơn, công nợ, GIRO, trợ cấp, giảm giá, đặt cọc, lịch thanh toán).

### 6.6 BBA-67: US-006 - Tab Health

#### User Story

Là người dùng, tôi muốn xem thông tin sức khỏe của trẻ ở một chỗ, thêm lần đo nhiệt độ và ghi chú của nhân viên, để chăm sóc trẻ an toàn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-014 | Tab hiển thị thông tin sức khỏe của trẻ (BR-018, BR-019). |
| FR-015 | Người dùng có quyền thêm lần đo nhiệt độ; xem toàn bộ các lần đo của trẻ ở màn Temperature (BR-020). |
| FR-016 | Tab hiển thị chiều cao, cân nặng theo kỳ, chỉ xem (BR-021). |
| FR-017 | Người dùng có quyền thêm, sửa ghi chú của nhân viên; thông tin phụ huynh khai chỉ xem (BR-022). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Health; hệ thống hiển thị các khối sức khỏe (FR-014).
2. Người dùng chọn Add a reading, nhập lần đo nhiệt độ, lưu (FR-015).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn xem toàn bộ nhiệt độ: hệ thống chuyển sang màn Temperature (BBA-74) của trẻ (FR-015).
2. Người dùng chọn Edit ở Note from staff, nhập ghi chú, lưu (FR-017).
3. Người dùng chọn Parent view: hệ thống hiển thị thông tin như phụ huynh thấy (FR-014).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò chỉ được đọc ghi chú nhân viên: không có Edit (BR-022).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-018 | Các khối: From the family (tiền sử bệnh, dị ứng, chế độ ăn, người cập nhật, kênh); Note from staff; Attachments from the family; Vaccination record; History; Temperature log; Height and weight by term; Height percentile. |
| BR-019 | Thông tin gia đình khai chỉ dùng sau khi có consent và Centre Director duyệt; bản chờ duyệt không thay bản đã duyệt (BBA-68, BBA-69). |
| BR-020 | Nhiệt độ hiển thị theo ngày. Người dùng có quyền thêm lần đo nhiệt độ tại tab; lần đo thêm ở đây hiển thị trên màn Temperature (BBA-74). Xem toàn bộ các lần đo của trẻ ở màn Temperature (BBA-74). |
| BR-021 | Chiều cao, cân nặng hiển thị số đo theo kỳ của trẻ; không thêm, không sửa số đo tại tab (BBA-70). |
| BR-022 | Thông tin phụ huynh khai về sức khỏe của trẻ không sửa được. Nhân viên chỉ được thêm, sửa ghi chú của nhân viên (Edit) theo quyền |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Health | Prototype: Records › Child › Health |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Các khối sức khỏe | Section | — | — | — | BR-018. |
| From the family | Section | — | Chỉ xem | — | BR-022. |
| Note from staff | Text + Edit | — | Edit theo quyền | — | BR-022; vai trò chỉ đọc thấy “Your role reads this note and does not write it.” |
| Temperature log | Section | — | Theo ngày | — | BR-020. |
| Add a reading | Nút | — | Theo quyền | — | Thêm lần đo nhiệt độ (BR-020). |
| Xem toàn bộ nhiệt độ | Liên kết | — | — | — | Chuyển sang màn Temperature (BBA-74). |
| Height and weight by term | Section | — | Chỉ xem | — | BR-021. |
| Parent view | Nút | — | — | — | Xem như phụ huynh. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-006 | Ghi chú nhân viên và lần đo nhiệt độ thêm tại tab ghi change log vào History: giá trị cũ, giá trị mới, người thực hiện, thời điểm. Lần đo nhiệt độ lưu cùng dữ liệu của BBA-74. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-022 | gia đình khai tiền sử co giật do sốt, đã duyệt | người dùng mở tab Health | From the family hiện nội dung, người cập nhật, ngày, kênh Parent app; không có thao tác sửa | FR-014; BR-018; BR-019; BR-022 |
| AC-023 | người dùng có quyền | chọn Add a reading, nhập 36.8 °C, lưu | lần đo hiện trong Temperature log của ngày hôm đó và trên màn Temperature (BBA-74); History có dòng thêm | FR-015; BR-020; DATA-006 |
| AC-024 | trẻ có 12 lần đo trong tháng | người dùng chọn xem toàn bộ nhiệt độ | hệ thống chuyển sang màn Temperature (BBA-74) của trẻ | FR-015; BR-020 |
| AC-025 | Term 1 2026 có chiều cao 98 cm, cân nặng 15 kg | người dùng mở tab Health | Height and weight by term hiện số đo Term 1 2026; không có nút Add hay Edit | FR-016; BR-021 |
| AC-026 | người dùng có quyền viết ghi chú | chọn Edit ở Note from staff, nhập ghi chú, lưu | ghi chú hiện trên tab; History có dòng thay đổi | FR-017; BR-022; DATA-006 |
| AC-027 | vai trò chỉ đọc ghi chú nhân viên | mở tab Health | Note from staff không có Edit, ghi “Your role reads this note and does not write it.” | BR-022 |

#### Dependencies (Phụ thuộc)

BBA-68, BBA-69, BBA-70, BBA-74; Parents App (khai sức khỏe).
### 6.7 BBA-67: US-007 - Tab Communication

#### User Story

Là người dùng, tôi muốn xem các cuộc trao đổi với phụ huynh của trẻ và nhắn tin ngay trên hồ sơ, để không bỏ sót tin phụ huynh đang chờ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-018 | Tab hiển thị các cuộc chat có phụ huynh của trẻ, giống phụ huynh thấy trong app (BR-023, BR-024). |
| FR-019 | Người dùng có quyền bắt đầu tin nhắn và trả lời (BR-025). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Communication; hệ thống hiển thị danh sách cuộc chat (FR-018).
2. Người dùng mở một cuộc chat, nhập trả lời, chọn Send (FR-019).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Start a message để mở cuộc chat mới (FR-019).
2. Người dùng chọn Hide conversation để thu gọn cuộc chat (FR-018).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thread lớp cũ: chỉ đọc, không có ô trả lời (BR-024).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-023 | Mỗi cuộc chat hiện tên, loại (Class, Group, Private), người tham gia, ngày bắt đầu, tin gần nhất; tin cuối của phụ huynh chưa được trả lời hiện “Waiting on a reply · n days”. |
| BR-024 | Người dùng chỉ thấy cuộc chat theo quyền của Communication; Teacher không thấy Private chat Centre Director – phụ huynh. Thread lớp cũ chỉ đọc. |
| BR-025 | Gửi tin, bắt đầu cuộc chat theo quy tắc của Communication. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Communication | Prototype: Records › Child › Communication |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Start a message | Nút | — | Theo quyền | — | FR-019. |
| Danh sách cuộc chat | Danh sách | — | — | — | BR-023. |
| Reply / Send | Ô nhập + nút | — | Ẩn ở thread chỉ đọc | — | BR-024; BR-025. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-007 | Tin gửi từ tab lưu ở Communication như tin gửi từ màn Communication. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-028 | tin cuối của Mr Wong trong class thread Bumblebees chưa được trả lời 67 ngày | người dùng mở tab Communication | cuộc chat hiện loại Class, người tham gia, “Waiting on a reply · 67 days” | FR-018; BR-023 |
| AC-029 | người dùng có quyền | nhập trả lời, chọn Send | tin hiện trong cuộc chat | FR-019; BR-025; DATA-007 |
| AC-030 | Teacher của lớp | mở tab Communication | không thấy Private chat Centre Director – phụ huynh; thread lớp cũ không có ô trả lời | BR-024 |

#### Dependencies (Phụ thuộc)

Communication.

### 6.8 BBA-67: US-008 - Tab Documents

#### User Story

Là người dùng, tôi muốn xem giấy tờ và consent của trẻ và tải lên giấy tờ thiếu, để hồ sơ đủ và còn hạn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-020 | Tab hiển thị giấy tờ của trẻ và consent (BR-026, BR-027). |
| FR-021 | Người dùng có quyền tải lên và tải lại giấy tờ (BR-026). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Documents; hệ thống hiển thị tóm tắt, giấy tờ và consent (FR-020).
2. Người dùng chọn Upload document hoặc Re-upload, chọn tệp, lưu (FR-021).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Open Surveys & consents: hệ thống mở Communication › Surveys & consents (FR-020; BR-027).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có quyền: không thấy Upload document và Re-upload (BR-026).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-026 | Mỗi giấy tờ hiện loại, trạng thái xác minh, tên tệp, phiên bản, ngày tải, ngày hết hạn. Tải lại tạo phiên bản mới chờ xác minh. Quy tắc giấy tờ, xác minh, hết hạn theo BBA-71. |
| BR-027 | Consent hiện tên, phiên bản, trạng thái (Not sent, Sent awaiting parent, Agreed, Declined), ngày trả lời. Gửi và nhắc consent làm ở Surveys & consents. ECDA form chỉ áp cho Singapore. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Documents | Prototype: Records › Child › Documents |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tóm tắt | Display | — | — | — | Số giấy tờ thiếu, hết hạn, chưa xác minh; số consent chờ phụ huynh. |
| Upload document / Re-upload | Nút | — | Theo quyền | — | FR-021; BR-026. |
| Consents | Bảng | — | — | — | BR-027; nút Open Surveys & consents. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-008 | Tải lên, tải lại, xác minh giấy tờ ghi History: giá trị cũ, giá trị mới, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-031 | Immunisation record v1, Verified, hết hạn 30/06/2027 | người dùng có quyền chọn Re-upload, chọn tệp | giấy tờ có v2 chờ xác minh; History có dòng tải lên | FR-021; BR-026; DATA-008 |
| AC-032 | consent Outings and excursions đã gửi, chưa trả lời | người dùng mở tab Documents | dòng consent ghi Sent, awaiting parent; tóm tắt ghi 1 consent waiting on a parent | FR-020; BR-027 |

#### Dependencies (Phụ thuộc)

BBA-71; Communication › Surveys & consents.

### 6.9 BBA-67: US-009 - Tab History

#### User Story

Là người dùng, tôi muốn xem mọi thay đổi trên hồ sơ trẻ và ai đã xem dữ liệu được bảo vệ, để kiểm tra khi có thắc mắc.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-022 | Tab hiển thị nhật ký thay đổi và lần xem dữ liệu được bảo vệ của trẻ (BR-028, BR-029). |
| FR-023 | Người dùng có quyền tìm, lọc và xuất nhật ký (BR-030). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab History; hệ thống hiển thị nhật ký, mới nhất trước (FR-022).
2. Người dùng chọn loại ở Show hoặc nhập Search (FR-023).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Export: hệ thống xuất nhật ký (FR-023).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có dòng khớp bộ lọc: hiển thị 0 entries (FR-023).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-028 | Mỗi dòng: nội dung thay đổi, giá trị cũ → giá trị mới (kèm lý do nếu có), thời điểm, người thực hiện, vai trò, kênh (SMS / Parent app). |
| BR-029 | Nhật ký chỉ thêm, không sửa, không xóa. Sửa sai thêm một dòng mới mang giá trị cũ. |
| BR-030 | Export theo quyền. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › History | Prototype: Records › Child › History |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Show | Lọc | — | All | — | FR-023. |
| Search | Ô tìm | — | Rỗng | — | FR-023. |
| Export | Nút | — | Theo quyền | — | BR-030. |
| Danh sách | Danh sách | — | “n entries, newest first.” | — | BR-028; BR-029. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-009 | Nhật ký nhận change log từ các tab và module ghi thay đổi cho trẻ (Enrolment, Guardians, Health, Finance, Documents; BBA-66). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-033 | HQ Admin vừa xem đầy đủ số NRIC của trẻ | người dùng mở tab History | dòng đầu ghi Viewed NRIC / identity document number → Viewed unmasked, thời điểm, người xem, vai trò, SMS | FR-022; BR-028; DATA-009 |
| AC-034 | người dùng có quyền | tìm một dòng để sửa hoặc xóa | không có thao tác sửa hay xóa | BR-029 |
| AC-035 | người dùng có quyền Export | người dùng chọn Export | hệ thống xuất nhật ký của trẻ | FR-023; BR-030 |

#### Dependencies (Phụ thuộc)

BBA-66 (nhật ký sửa hồ sơ, xem NRIC); các module ghi thay đổi cho trẻ.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Bản trước mô tả tab Communication chỉ hiển thị, không trả lời; prototype có Start a message và Reply / Send. Xác nhận tab cho nhắn tin trực tiếp. | HQ Ops | Cao |  |
| OQ-02 | Gỡ guardian duy nhất giữ vai trò Primary contact có bị chặn không? | HQ Ops | Trung bình |  |
| OQ-03 | SUG Child và KA Child nghĩa là gì, trẻ được hưởng quyền lợi tính phí gì? Đặt Staff Child = Yes có tự áp giảm giá Staff child discount không, hay Finance áp tay? | HQ Finance | Cao |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Module sở hữu | Module lưu dữ liệu và quy tắc nghiệp vụ của thao tác; tab chỉ hiển thị hoặc mở thao tác. |
| Flag | Đánh dấu trẻ (SUG Child, Staff Child, KA Child) dùng cho quy tắc tính phí. |
| Trường được bảo vệ | Trường hiển thị đầy đủ, che hoặc ẩn theo quyền; xem đầy đủ được ghi History. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Thứ tự tab | Overview, Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History. | BBA-66 FR-003. |
| Vai trò guardian | Primary contact, Emergency contact, Authorised to collect, Billing contact. | Children & Families. |
