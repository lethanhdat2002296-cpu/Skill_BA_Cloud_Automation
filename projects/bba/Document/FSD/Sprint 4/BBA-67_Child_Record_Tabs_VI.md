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
| Các tab Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History: nội dung tổng quan, thao tác theo quyền, liên kết sang module sở hữu, trạng thái rỗng. | Header, tab Overview, sửa hồ sơ trẻ (BBA-66). Medical alert (BBA-68), danh sách dị ứng (BBA-69), chiều cao cân nặng (BBA-70), giấy tờ và consent (BBA-71), đưa đón (BBA-73), đo nhiệt độ (BBA-74). Chi tiết nghiệp vụ của Joining & leaving, Learning › Enrichment, Fees & Payments, Communication. Parents App. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ trong phạm vi dữ liệu được cấp (HQ: mọi Centre; nhân viên Centre: Centre của mình; Teacher: lớp của mình). | Xem các tab được cấp quyền; thực hiện thao tác trên tab theo quyền. |
| Read-only User | Trẻ trong phạm vi được cấp. | Xem tab; không thấy nút thao tác. |
| System | Dữ liệu các module của trẻ. | Đọc dữ liệu module, áp quyền, che hoặc ẩn trường được bảo vệ, ghi History. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy tab hoặc hồ sơ trẻ. |

**Quy tắc chung:** Quyền xem từng tab và từng thao tác do BBA cấu hình trong Roles & permissions; thao tác không có quyền thì không hiển thị. Tài liệu này không gán cứng quyền cho vai trò nào.

## 5. Tổng quan tính năng và phân rã chức năng

| Tab | Nội dung | Thao tác trên tab (theo quyền) | Module sở hữu | User Story |
|---|---|---|---|---|
| **Enrolment** | Lịch sử quá trình ghi danh của trẻ; flag của trẻ. | Đặt flag; mở withdrawal, temporary withdrawal, transfer. | Enrolment; Joining & leaving | US-001 |
| **Enrichment** | Lớp enrichment trẻ đang học, đã học, đang chờ HQ xác nhận. | Không có; mở Learning › Enrichment. | Learning | US-002 |
| **Guardians** | Người giám hộ và vai trò; anh chị em; người được đón. | Tạo, sửa, gỡ guardian; liên kết anh chị em; gỡ người được đón. | Children & Families | US-003 |
| **Attendance** | Xe đưa đón, số ngày đi học, chi tiết một ngày, điểm danh gần đây. | Chọn xe đưa đón. | Daily Operations | US-004 |
| **Finance** | Việc cần làm, trợ cấp, GIRO/CDA, cách thanh toán, lịch thanh toán, đặt cọc, hoá đơn, công nợ, giảm giá. | Gửi nhắc phí, review trợ cấp, đổi Bill to, xuất GIRO, quản lý đặt cọc, thêm giảm giá. | Fees & Payments | US-005 |
| **Health** | Thông tin từ gia đình, ghi chú nhân viên, tiêm chủng, nhiệt độ, chiều cao cân nặng. | Ghi chú nhân viên, thêm lần đo nhiệt độ, thêm chiều cao cân nặng. | Children & Families; Daily Operations | US-006 |
| **Communication** | Các cuộc chat có phụ huynh của trẻ. | Bắt đầu tin nhắn, trả lời. | Communication | US-007 |
| **Documents** | Giấy tờ của trẻ và consent. | Tải lên, tải lại giấy tờ. | Children & Families; Communication | US-008 |
| **History** | Nhật ký mọi thay đổi và lần xem dữ liệu được bảo vệ. | Tìm, lọc, xuất. | Children & Families | US-009 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-67: US-001 - Tab Enrolment

#### User Story

Là người dùng, tôi muốn xem lịch sử quá trình ghi danh của trẻ khi học ở trường và các flag của trẻ, để trả lời phụ huynh và mở các việc rút, tạm nghỉ, chuyển Centre.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab hiển thị lịch sử quá trình ghi danh của trẻ (BR-001). |
| FR-002 | Người dùng có quyền đặt flag của trẻ (BR-002). |
| FR-003 | Người dùng có quyền mở withdrawal, temporary withdrawal hoặc transfer từ tab (BR-003). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Enrolment; hệ thống hiển thị flag và lịch sử ghi danh (FR-001).
2. Người dùng chọn Set it ở một flag, chọn giá trị, lưu (FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Start a withdrawal / Start a temporary withdrawal / Start a transfer: hệ thống mở luồng tương ứng của Joining & leaving (FR-003).
2. Người dùng chọn một lần ghi danh: hệ thống mở chi tiết ghi danh (FR-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền: không thấy Set it và các nút Start (BR-002, BR-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi lần ghi danh một dòng: Centre, level, lớp, programme (Full day / Half day), năm học, ngày ghi danh, ngày bắt đầu học, ngày kết thúc hoặc “ongoing”, trạng thái, pháp nhân. Dòng đầu ghi tổng số lần ghi danh và số lần đang chạy. Ghi danh và thay đổi không bị xoá. |
| BR-002 | Flag gồm SUG Child, Staff Child, KA Child, giá trị Yes / No. Mỗi flag hiện quy tắc tính phí đang áp; chưa có quy tắc thì ghi chờ Finance xác nhận. Đổi flag ghi History. |
| BR-003 | Withdrawal, temporary withdrawal, transfer thuộc Joining & leaving; tab chỉ là điểm mở luồng. Trạng thái ghi danh chỉ đổi qua Joining & leaving. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Enrolment | Prototype: Records › Child › Enrolment |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Flags on this child | Section | — | No | — | SUG / Staff / KA Child, nút Set it (BR-002). |
| Start a case on this child | Nhóm nút | — | Theo quyền | — | Start a withdrawal, Start a temporary withdrawal, Start a transfer (BR-003). |
| Danh sách ghi danh | Danh sách | — | Mới nhất trước | — | BR-001. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Đổi flag lưu flag, giá trị cũ, giá trị mới, người đổi, thời điểm vào History (BR-002). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | trẻ ghi danh Small Wonder Tampines · Playgroup · Bumblebees, Half Day, năm 2026, đang học | người dùng mở tab Enrolment | dòng ghi danh hiện Centre, level, lớp, programme, năm học, ngày ghi danh, ngày bắt đầu, “ongoing”, Active; đầu danh sách ghi “1 enrolment · 1 running now” | FR-001; BR-001 |
| AC-002 | Staff Child = No | người dùng có quyền chọn Set it, chọn Yes, lưu | flag Staff Child = Yes; History có dòng No → Yes kèm người đổi | FR-002; BR-002; DATA-001 |
| AC-003 | người dùng có quyền | chọn Start a transfer | hệ thống mở luồng Transfer của Joining & leaving cho trẻ | FR-003; BR-003 |

#### Dependencies (Phụ thuộc)

Enrolment; Joining & leaving; Fees & Payments (quy tắc tính phí theo flag).

### 6.2 BBA-67: US-002 - Tab Enrichment

#### User Story

Là người dùng, tôi muốn xem các lớp enrichment của trẻ, để biết trẻ học gì, khi nào, ở đâu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Tab hiển thị các lớp enrichment của trẻ và yêu cầu đang chờ HQ xác nhận (BR-004, BR-005). |
| FR-005 | Tab chỉ hiển thị; thay đổi thực hiện ở Learning › Enrichment (BR-006). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Enrichment; hệ thống hiển thị danh sách lớp (FR-004).
2. Người dùng chọn tên lớp: hệ thống mở lớp ở Learning › Enrichment (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ có yêu cầu tham gia lớp đang chờ HQ: hiển thị ở khối Waiting for HQ to confirm (BR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa học lớp enrichment nào: hiển thị thông báo rỗng (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-004 | Mỗi lớp một dòng: Programme, Centre, Day and time, Start date, End date. Lớp đang học có End date “—”. Một trẻ học được nhiều lớp. |
| BR-005 | Yêu cầu tham gia lớp do Centre gửi, chờ HQ xác nhận, hiện tên lớp, ngày gửi, người gửi và vai trò. |
| BR-006 | Tab không có nút thêm, sửa, gỡ trẻ khỏi lớp. HQ Enrichment team quản lý lớp và học sinh ở Learning. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Trẻ chưa có lớp enrichment và không có yêu cầu chờ. | Hiển thị “No enrichment programme for this child.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Enrichment | Prototype: Records › Child › Enrichment |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Enrichment programmes | Bảng | — | — | VAL-001. | BR-004; tên lớp là liên kết (FR-005). |
| Waiting for HQ to confirm | Section | — | Khi có yêu cầu | — | BR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Tab đọc dữ liệu của Learning; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-004 | trẻ học Speech & Drama (Thứ Năm 15:30–16:30) và Swimming từ 01/07/2026; yêu cầu Mandarin Explorers gửi 15/09/2026 | người dùng mở tab Enrichment | 2 dòng lớp, End date “—”; khối Waiting for HQ to confirm hiện Mandarin Explorers, ngày gửi, người gửi | FR-004; BR-004; BR-005; DATA-002 |
| AC-005 | người dùng có quyền xem trẻ | mở tab Enrichment | không có nút thêm, sửa, gỡ; chọn Swimming mở lớp ở Learning | FR-005; BR-006 |
| AC-006 | trẻ chưa có lớp enrichment | mở tab Enrichment | hiện “No enrichment programme for this child.” | VAL-001 |

#### Dependencies (Phụ thuộc)

Learning › Enrichment.

### 6.3 BBA-67: US-003 - Tab Guardians

#### User Story

Là người dùng, tôi muốn xem và cập nhật người giám hộ, anh chị em và người được đón của trẻ, để liên hệ đúng người và giao trẻ đúng người.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Tab hiển thị guardian và vai trò, anh chị em, người được đón (BR-007, BR-008, BR-009). |
| FR-007 | Người dùng có quyền tạo, sửa, gỡ guardian và liên kết anh chị em (BR-007, BR-008). |
| FR-008 | Người dùng có quyền gỡ người được đón (BR-009). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Guardians; hệ thống hiển thị guardian, anh chị em, người được đón (FR-006).
2. Người dùng chọn Create guardian hoặc Edit, nhập thông tin và vai trò, lưu (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng tìm một trẻ đã có trong hệ thống để liên kết anh chị em (FR-007; BR-008).
2. Người dùng gỡ người được đón: gỡ có hiệu lực ngay, không cần duyệt (FR-008; BR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có quyền: không thấy Create guardian, Edit, Remove (FR-007).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-007 | Mỗi guardian có quan hệ với trẻ, điện thoại, email và một hoặc nhiều vai trò: Primary contact, Emergency contact, Authorised to collect, Billing contact. |
| BR-008 | Anh chị em là trẻ đã có trong hệ thống, liên kết bằng tìm kiếm. |
| BR-009 | Phụ huynh thêm người được đón trong Parents App; mỗi người thêm chờ Centre Director hoặc School Admin của Centre duyệt và chỉ được đón trẻ sau khi duyệt. Gỡ người được đón không cần duyệt. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Guardians | Prototype: Records › Child › Guardians |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Create guardian / Edit / Remove | Nút | — | Theo quyền | — | FR-007. |
| Vai trò guardian | Nhãn chọn | Có ít nhất 1 | — | — | BR-007. |
| Siblings | Section + ô tìm | — | “No sibling is linked…” khi rỗng | — | BR-008. |
| Authorised pickup | Danh sách | — | — | — | Tên, quan hệ, người thêm, ngày, trạng thái duyệt; nút Remove (BR-009). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi lần tạo, sửa, gỡ guardian, liên kết anh chị em, duyệt hoặc gỡ người được đón ghi History: giá trị cũ, giá trị mới, người thực hiện, thời điểm, kênh (SMS / Parent app). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | trẻ có guardian Mr Wong (father, Primary contact) | người dùng có quyền chọn Create guardian, nhập Mrs Wong, vai trò Emergency contact, lưu | Mrs Wong hiện trong danh sách với vai trò Emergency contact; History có dòng thêm guardian | FR-006; FR-007; BR-007; DATA-003 |
| AC-008 | trẻ chưa có anh chị em | người dùng tìm và chọn một trẻ có trong hệ thống | trẻ đó hiện ở Siblings | FR-007; BR-008 |
| AC-009 | bà nội được phụ huynh thêm trong Parents App, chưa duyệt | người dùng mở tab Guardians | bà nội hiện trạng thái chờ duyệt, chưa được đón trẻ | FR-006; BR-009 |
| AC-010 | Mr Wong được duyệt đón trẻ | người dùng chọn Remove ở Authorised pickup | Mr Wong bị gỡ ngay, không qua bước duyệt | FR-008; BR-009 |

#### Dependencies (Phụ thuộc)

Parents App (người được đón); Roles & permissions.

### 6.4 BBA-67: US-004 - Tab Attendance

#### User Story

Là người dùng, tôi muốn xem tình hình đi học của trẻ và chi tiết một ngày, để trả lời phụ huynh mà không phải mở màn điểm danh của lớp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-009 | Tab hiển thị số ngày đi học, chi tiết một ngày và điểm danh gần đây (BR-010, BR-011). |
| FR-010 | Người dùng có quyền chọn xe đưa đón của trẻ (BR-012). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Attendance; hệ thống hiển thị số ngày đi học và điểm danh gần đây (FR-009).
2. Người dùng chọn một ngày; khối One day, in full hiện chi tiết ngày đó (FR-009).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng có quyền chọn xe đưa đón (FR-010).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngày không có check-in hoặc đo nhiệt độ: khối tương ứng ghi chưa có dữ liệu (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-010 | Days attended: số ngày đi học tháng này, kỳ này, số lần vắng. Ngày đi học là ngày có check-in không bị void; điểm danh enrichment không tính. |
| BR-011 | Chi tiết một ngày: lớp, programme, giờ vào, giờ ra, người đưa; check-in và check-out (BBA-73); mọi lần đo nhiệt độ (BBA-74); trạng thái ngày (Present, Absent, On leave). Sửa điểm danh làm ở Daily Operations, không làm trên tab. |
| BR-012 | Bus service: No bus hoặc một tuyến xe của Centre. Đổi xe ghi History. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Ngày được chọn không có check-in / đo nhiệt độ. | Hiện “No sign-in recorded on this day.” / “No reading recorded on this day.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Attendance | Prototype: Records › Child › Attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Bus service | Chọn một | — | No bus | — | Theo quyền (FR-010; BR-012). |
| Days attended | Thẻ số | — | — | — | BR-010. |
| One day, in full | Section | — | Ngày gần nhất | VAL-002. | BR-011. |
| Recent attendance | Danh sách | — | Mới nhất trước | — | Ngày, lớp, programme, giờ đến, trạng thái; chọn dòng để xem chi tiết. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Đổi xe đưa đón ghi History: giá trị cũ, giá trị mới, người đổi, thời điểm. Dữ liệu điểm danh đọc từ Daily Operations. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-011 | trẻ đi học 20 ngày kỳ này, 0 ngày tháng này, 1 lần vắng | người dùng mở tab Attendance | Days attended hiện 0 this month, 20 this term, 1 absences recorded | FR-009; BR-010 |
| AC-012 | ngày 17/09/2026 trẻ nghỉ phép | người dùng chọn ngày 17/09/2026 | chi tiết ngày ghi On leave, lớp Bumblebees; “No sign-in recorded on this day.”; “No reading recorded on this day.” | FR-009; BR-011; VAL-002 |
| AC-013 | trẻ No bus | người dùng có quyền chọn Bus A — Tampines North loop | Bus service = Bus A; History có dòng No bus → Bus A | FR-010; BR-012; DATA-004 |

#### Dependencies (Phụ thuộc)

Daily Operations › Child attendance (BBA-73, BBA-74); danh sách tuyến xe của Centre.

### 6.5 BBA-67: US-005 - Tab Finance

#### User Story

Là người dùng, tôi muốn thấy tình hình tài chính của trẻ và xử lý các việc tài chính thường gặp ngay trên hồ sơ, để không phải mở từng màn của Fees & Payments.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-011 | Tab hiển thị tổng quan tài chính của trẻ (BR-013, BR-014). |
| FR-012 | Người dùng có quyền thực hiện các thao tác tài chính trên tab hoặc mở màn tương ứng của Fees & Payments (BR-015). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Finance; hệ thống hiển thị các khối tài chính (FR-011).
2. Người dùng chọn một thao tác ở khối tương ứng (FR-012).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn See what the parent sees: hệ thống hiển thị tài chính như phụ huynh thấy (FR-011).
2. Người dùng chọn số hoá đơn: hệ thống mở chi tiết hoá đơn (FR-012).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ thuộc Centre Malaysia: không có khối GIRO and CDA accounts và trợ cấp ECDA (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-013 | Các khối: What needs doing (hoá đơn quá hạn); What the flags have done; Subsidies; Bill to; GIRO and CDA accounts; How this family pays (Payment method, citizenship tính phí, tiền đặt cọc đang giữ); Payment schedule; Deposit; Invoices (theo loại); Outstanding and chasing (theo nhóm tuổi nợ); Discounts. |
| BR-014 | Số tài khoản ngân hàng và tiền đặt cọc là trường được bảo vệ: hiển thị đầy đủ, che hoặc ẩn theo quyền; mỗi lần xem đầy đủ ghi History. |
| BR-015 | Thao tác trên tab: Send a reminder (hoá đơn quá hạn), Review child (trợ cấp), Bill to Parent / Company (Save), Export GIRO, Manage (đặt cọc), Add a discount, Open schedule, Open (công nợ). Quy tắc nghiệp vụ của từng thao tác theo Fees & Payments. |

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
| Các khối tài chính | Section | — | — | VAL-003. | BR-013. |
| Nút thao tác | Nút / liên kết | — | Theo quyền | — | BR-015. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-005 | Thao tác làm trên tab (Bill to, giảm giá, đặt cọc, nhắc phí) lưu theo Fees & Payments và ghi History của trẻ. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-014 | hoá đơn SW-TAM-ADH-2026-10-0003 quá hạn 37 ngày, SGD 34.88 | người dùng mở tab Finance | What needs doing hiện hoá đơn kèm số ngày quá hạn, số tiền và nút Send a reminder; Outstanding hiện nhóm 31–60 days | FR-011; BR-013 |
| AC-015 | người dùng không có quyền xem đầy đủ tiền đặt cọc | mở tab Finance | tiền đặt cọc bị che | BR-014 |
| AC-016 | Bill to chưa chọn | người dùng có quyền chọn Company, Save | Bill to = Company; History có dòng thay đổi | FR-012; BR-015; DATA-005 |
| AC-017 | trẻ thuộc Centre Malaysia | mở tab Finance | không có khối GIRO and CDA accounts và trợ cấp ECDA | VAL-003 |
| AC-018 | vai trò không có quyền Fees & Payments | mở hồ sơ trẻ | không có tab Finance | VAL-004 |

#### Dependencies (Phụ thuộc)

Fees & Payments (hoá đơn, công nợ, GIRO, trợ cấp, giảm giá, đặt cọc, lịch thanh toán).

### 6.6 BBA-67: US-006 - Tab Health

#### User Story

Là người dùng, tôi muốn xem thông tin sức khoẻ của trẻ ở một chỗ và ghi các số đo được phép, để chăm sóc trẻ an toàn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-013 | Tab hiển thị thông tin sức khoẻ của trẻ (BR-016, BR-017). |
| FR-014 | Người dùng có quyền ghi chú nhân viên, thêm lần đo nhiệt độ, thêm chiều cao cân nặng (BR-018). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Health; hệ thống hiển thị các khối sức khoẻ (FR-013).
2. Người dùng chọn Add a reading hoặc Add ở một kỳ, nhập số đo, lưu (FR-014).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Record a whole class: hệ thống mở màn Growth của lớp (FR-014; BBA-70).
2. Người dùng chọn Parent view: hệ thống hiển thị thông tin như phụ huynh thấy (FR-013).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò chỉ được đọc ghi chú nhân viên: không có ô sửa ghi chú (BR-018).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-016 | Các khối: From the family (tiền sử bệnh, dị ứng, chế độ ăn, người cập nhật, kênh); Note from staff; Attachments from the family; Vaccination record; History; Temperature log; Height and weight by term; Height percentile. |
| BR-017 | Thông tin gia đình khai chỉ dùng sau khi có consent và Centre Director duyệt; bản chờ duyệt không thay bản đã duyệt (BBA-68, BBA-69). Gia đình được nhắc cập nhật tiêm chủng 12 tháng sau lần ghi gần nhất. |
| BR-018 | Ghi chú nhân viên chỉ vai trò có quyền được viết; vai trò khác chỉ đọc. Đo nhiệt độ theo BBA-74; chiều cao cân nặng theo BBA-70. Thông tin từ gia đình không sửa trên tab. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Health | Prototype: Records › Child › Health |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Các khối sức khoẻ | Section | — | — | — | BR-016. |
| Note from staff | Text | — | Chỉ đọc theo vai trò | — | BR-018; vai trò chỉ đọc thấy “Your role reads this note and does not write it.” |
| Add a reading | Nút | — | Theo quyền | — | BBA-74. |
| Add / Record a whole class | Nút | — | Theo quyền | — | BBA-70. |
| Parent view | Nút | — | — | — | Xem như phụ huynh. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-006 | Ghi chú nhân viên, lần đo nhiệt độ, chiều cao cân nặng ghi History: giá trị cũ, giá trị mới, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-019 | gia đình khai tiền sử co giật do sốt, đã duyệt | người dùng mở tab Health | From the family hiện nội dung, người cập nhật, ngày, kênh Parent app | FR-013; BR-016; BR-017 |
| AC-020 | vai trò chỉ đọc ghi chú nhân viên | mở tab Health | Note from staff không có ô sửa, ghi “Your role reads this note and does not write it.” | BR-018 |
| AC-021 | Term 1 2026 chưa có số đo | người dùng có quyền chọn Add, nhập chiều cao cân nặng, lưu | Term 1 2026 hiện số đo; History có dòng thêm số đo | FR-014; BR-018; DATA-006 |

#### Dependencies (Phụ thuộc)

BBA-68, BBA-69, BBA-70, BBA-74; Parents App (khai sức khoẻ).

### 6.7 BBA-67: US-007 - Tab Communication

#### User Story

Là người dùng, tôi muốn xem các cuộc trao đổi với phụ huynh của trẻ và nhắn tin ngay trên hồ sơ, để không bỏ sót tin phụ huynh đang chờ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-015 | Tab hiển thị các cuộc chat có phụ huynh của trẻ, giống phụ huynh thấy trong app (BR-019, BR-020). |
| FR-016 | Người dùng có quyền bắt đầu tin nhắn và trả lời (BR-021). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Communication; hệ thống hiển thị danh sách cuộc chat (FR-015).
2. Người dùng mở một cuộc chat, nhập trả lời, chọn Send (FR-016).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Start a message để mở cuộc chat mới (FR-016).
2. Người dùng chọn Hide conversation để thu gọn cuộc chat (FR-015).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thread lớp cũ: chỉ đọc, không có ô trả lời (BR-020).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-019 | Mỗi cuộc chat hiện tên, loại (Class, Group, Private), người tham gia, ngày bắt đầu, tin gần nhất; tin cuối của phụ huynh chưa được trả lời hiện “Waiting on a reply · n days”. |
| BR-020 | Người dùng chỉ thấy cuộc chat theo quyền của Communication; Teacher không thấy Private chat Centre Director – phụ huynh. Thread lớp cũ chỉ đọc. |
| BR-021 | Gửi tin, bắt đầu cuộc chat theo quy tắc của Communication. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Communication | Prototype: Records › Child › Communication |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Start a message | Nút | — | Theo quyền | — | FR-016. |
| Danh sách cuộc chat | Danh sách | — | — | — | BR-019. |
| Reply / Send | Ô nhập + nút | — | Ẩn ở thread chỉ đọc | — | BR-020; BR-021. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-007 | Tin gửi từ tab lưu ở Communication như tin gửi từ màn Communication. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-022 | tin cuối của Mr Wong trong class thread Bumblebees chưa được trả lời 67 ngày | người dùng mở tab Communication | cuộc chat hiện loại Class, người tham gia, “Waiting on a reply · 67 days” | FR-015; BR-019 |
| AC-023 | người dùng có quyền | nhập trả lời, chọn Send | tin hiện trong cuộc chat | FR-016; BR-021; DATA-007 |
| AC-024 | Teacher của lớp | mở tab Communication | không thấy Private chat Centre Director – phụ huynh; thread lớp cũ không có ô trả lời | BR-020 |

#### Dependencies (Phụ thuộc)

Communication.

### 6.8 BBA-67: US-008 - Tab Documents

#### User Story

Là người dùng, tôi muốn xem giấy tờ và consent của trẻ và tải lên giấy tờ thiếu, để hồ sơ đủ và còn hạn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-017 | Tab hiển thị giấy tờ của trẻ và consent (BR-022, BR-023). |
| FR-018 | Người dùng có quyền tải lên và tải lại giấy tờ (BR-022). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Documents; hệ thống hiển thị tóm tắt, giấy tờ và consent (FR-017).
2. Người dùng chọn Upload document hoặc Re-upload, chọn tệp, lưu (FR-018).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Open Surveys & consents: hệ thống mở Communication › Surveys & consents (FR-017; BR-023).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có quyền: không thấy Upload document và Re-upload (BR-022).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-022 | Mỗi giấy tờ hiện loại, trạng thái xác minh, tên tệp, phiên bản, ngày tải, ngày hết hạn. Tải lại tạo phiên bản mới chờ xác minh. Quy tắc giấy tờ, xác minh, hết hạn theo BBA-71. |
| BR-023 | Consent hiện tên, phiên bản, trạng thái (Not sent, Sent awaiting parent, Agreed, Declined), ngày trả lời. Gửi và nhắc consent làm ở Surveys & consents. ECDA form chỉ áp cho Singapore. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Documents | Prototype: Records › Child › Documents |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tóm tắt | Display | — | — | — | Số giấy tờ thiếu, hết hạn, chưa xác minh; số consent chờ phụ huynh. |
| Upload document / Re-upload | Nút | — | Theo quyền | — | FR-018; BR-022. |
| Consents | Bảng | — | — | — | BR-023; nút Open Surveys & consents. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-008 | Tải lên, tải lại, xác minh giấy tờ ghi History: giá trị cũ, giá trị mới, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-025 | Immunisation record v1, Verified, hết hạn 30/06/2027 | người dùng có quyền chọn Re-upload, chọn tệp | giấy tờ có v2 chờ xác minh; History có dòng tải lên | FR-018; BR-022; DATA-008 |
| AC-026 | consent Outings and excursions đã gửi, chưa trả lời | người dùng mở tab Documents | dòng consent ghi Sent, awaiting parent; tóm tắt ghi 1 consent waiting on a parent | FR-017; BR-023 |

#### Dependencies (Phụ thuộc)

BBA-71; Communication › Surveys & consents.

### 6.9 BBA-67: US-009 - Tab History

#### User Story

Là người dùng, tôi muốn xem mọi thay đổi trên hồ sơ trẻ và ai đã xem dữ liệu được bảo vệ, để kiểm tra khi có thắc mắc.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-019 | Tab hiển thị nhật ký thay đổi và lần xem dữ liệu được bảo vệ của trẻ (BR-024, BR-025). |
| FR-020 | Người dùng có quyền tìm, lọc và xuất nhật ký (BR-026). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab History; hệ thống hiển thị nhật ký, mới nhất trước (FR-019).
2. Người dùng chọn loại ở Show hoặc nhập Search (FR-020).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Export: hệ thống xuất nhật ký (FR-020).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có dòng khớp bộ lọc: hiển thị 0 entries (FR-020).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-024 | Mỗi dòng: nội dung thay đổi, giá trị cũ → giá trị mới (kèm lý do nếu có), thời điểm, người thực hiện, vai trò, kênh (SMS / Parent app). |
| BR-025 | Nhật ký chỉ thêm, không sửa, không xoá. Sửa sai thêm một dòng mới mang giá trị cũ. |
| BR-026 | Export theo quyền. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › History | Prototype: Records › Child › History |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Show | Lọc | — | All | — | FR-020. |
| Search | Ô tìm | — | Rỗng | — | FR-020. |
| Export | Nút | — | Theo quyền | — | BR-026. |
| Danh sách | Danh sách | — | “n entries, newest first.” | — | BR-024; BR-025. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-009 | Nhật ký nhận dòng từ mọi tab và module ghi thay đổi cho trẻ (DATA-001, DATA-003 đến DATA-008; BBA-66). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-027 | HQ Admin vừa xem đầy đủ số NRIC của trẻ | người dùng mở tab History | dòng đầu ghi Viewed NRIC / identity document number → Viewed unmasked, thời điểm, người xem, vai trò, SMS | FR-019; BR-024; DATA-009 |
| AC-028 | người dùng có quyền | tìm một dòng để sửa hoặc xoá | không có thao tác sửa hay xoá | BR-025 |
| AC-029 | người dùng có quyền Export | người dùng chọn Export | hệ thống xuất nhật ký của trẻ | FR-020; BR-026 |

#### Dependencies (Phụ thuộc)

BBA-66 (nhật ký sửa hồ sơ, xem NRIC); các module ghi thay đổi cho trẻ.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Bản trước mô tả tab Communication chỉ hiển thị, không trả lời; prototype có Start a message và Reply / Send. Xác nhận tab cho nhắn tin trực tiếp. | HQ Ops | Cao |  |
| OQ-02 | Gỡ guardian duy nhất giữ vai trò Primary contact có bị chặn không? | HQ Ops | Trung bình |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Module sở hữu | Module lưu dữ liệu và quy tắc nghiệp vụ của thao tác; tab chỉ hiển thị hoặc mở thao tác. |
| Flag | Đánh dấu trẻ (SUG Child, Staff Child, KA Child) dùng cho quy tắc tính phí. |
| Authorised pickup | Người được đón trẻ, do phụ huynh thêm và Centre duyệt. |
| Trường được bảo vệ | Trường hiển thị đầy đủ, che hoặc ẩn theo quyền; xem đầy đủ được ghi History. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Thứ tự tab | Overview, Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History. | BBA-66 FR-003. |
| Vai trò guardian | Primary contact, Emergency contact, Authorised to collect, Billing contact. | Children & Families. |
