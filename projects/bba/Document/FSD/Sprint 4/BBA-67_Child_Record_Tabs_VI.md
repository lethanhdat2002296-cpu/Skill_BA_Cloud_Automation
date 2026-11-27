# Child Record Tabs – All

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Child record |
| Tính năng | BBA-67 Các tab của hồ sơ trẻ (Enrolment, Enrichment, Attendance, Finance, Communication) |
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

**Mức sẵn sàng:** Đã đặc tả nội dung tổng quan, thao tác theo quyền và liên kết sang module của 5 tab.

## 2. Mục đích và bối cảnh

Hồ sơ trẻ gom về một chỗ những gì các module ghi nhận về trẻ. Tài liệu này mô tả tổng quan 5 tab Enrolment, Enrichment, Attendance, Finance, Communication: tab hiển thị gì, người dùng có quyền được thao tác gì ngay trên tab, thao tác nào mở sang module sở hữu. Chi tiết nghiệp vụ của từng thao tác nằm ở FRS của module sở hữu.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Các tab Enrolment, Enrichment, Attendance, Finance, Communication: nội dung tổng quan, thao tác theo quyền, liên kết sang module sở hữu, trạng thái rỗng. | Header, tab Overview, sửa hồ sơ trẻ, lịch sử thay đổi (BBA-66). Các tab Guardians, Health, Documents, History. Flag của trẻ (SUG Child, Staff Child, KA Child). Medical alert (BBA-68), danh sách dị ứng (BBA-69), chiều cao cân nặng (BBA-70), giấy tờ và consent (BBA-71), đưa đón (BBA-73), đo nhiệt độ (BBA-74). Chi tiết nghiệp vụ của Joining & leaving, Learning › Enrichment, Fees & Payments, Communication. Parents App. |

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
| **Enrolment** | Bảng các lần ghi danh của trẻ. | Tạo withdrawal, temporary withdrawal, transfer (chuyển sang màn hình module); ghi change log. | Enrolment; Joining & leaving | US-001 |
| **Enrichment** | Lớp enrichment trẻ đang chờ, đang học, đã học. | Không có; chỉ hiển thị. | Learning | US-002 |
| **Attendance** | Bảng giờ vào, giờ ra, nhiệt độ theo ngày; xe đưa rước (chỉ xem). | Không có; chỉ hiển thị. | Daily Operations | US-003 |
| **Finance** | Việc cần làm, trợ cấp, GIRO/CDA, cách thanh toán, lịch thanh toán, đặt cọc, hoá đơn, công nợ, giảm giá. | Gửi nhắc phí, review trợ cấp, đổi Bill to, xuất GIRO, quản lý đặt cọc, thêm giảm giá. | Fees & Payments | US-004 |
| **Communication** | Các cuộc chat có phụ huynh của trẻ. | Bắt đầu tin nhắn, trả lời. | Communication | US-005 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-67: US-001 - Tab Enrolment

#### User Story

Là người dùng, tôi muốn xem lịch sử quá trình ghi danh của trẻ khi học ở trường và tạo các việc rút, tạm nghỉ, chuyển Centre ngay từ hồ sơ trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab hiển thị toàn bộ các lần ghi danh của trẻ dạng bảng (BR-001, BR-002). |
| FR-002 | Người dùng có quyền tạo withdrawal, temporary withdrawal, transfer từ tab Enrolment; hệ thống chuyển sang màn hình của module tương ứng (BR-003). |
| FR-003 | Mỗi lần tạo withdrawal, temporary withdrawal, transfer từ tab được ghi change log vào History của trẻ (BR-004). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Enrolment; hệ thống hiển thị bảng Enrolments (FR-001).
2. Người dùng chọn nút “⋯” ở góc phải bảng, chọn Start withdrawal / Start temporary withdrawal / Start transfer (FR-002).
3. Hệ thống chuyển sang màn hình tạo yêu cầu của Joining & leaving cho trẻ và ghi change log (FR-002, FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chỉ có quyền xem: không có nút “⋯”; bảng Enrolments vẫn hiển thị đầy đủ (BR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không chuyển được sang màn hình Joining & leaving: hệ thống báo lỗi theo hành vi chuẩn, không ghi change log.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Bảng Enrolments: mỗi lần ghi danh một dòng, mới nhất trước. Cột: Centre, Level, Class, Programme, Academic year, Enrolled on, Start date, End date, Status, Legal entity. Lần ghi danh đang học có End date “ongoing”. |
| BR-002 | Status gồm Active (đang học), Transferred (đã chuyển Centre), Completed (đã kết thúc). Dòng tóm tắt trên bảng ghi tổng số lần ghi danh và số lần đang chạy, ví dụ “3 enrolments · 1 running now”. Ghi danh và thay đổi không bị xóa. |
| BR-003 | Withdrawal, temporary withdrawal, transfer thuộc Joining & leaving; tab chỉ là điểm mở luồng. Nút “⋯” (Start a case on this child) chỉ hiện với người dùng có quyền. Trạng thái ghi danh chỉ đổi qua Joining & leaving. |
| BR-004 | Change log ghi: thao tác (tạo withdrawal / temporary withdrawal / transfer), người thực hiện, thời điểm. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Enrolment | Wireframe BBA-67 › tab Enrolment |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tiêu đề | Display | — | “Enrolments” | — | Dòng phụ “One row per enrolment, newest first. Enrolments and changes are never deleted.” |
| Tóm tắt | Display | — | — | — | “n enrolments · n running now” (BR-002). |
| Nút “⋯” | Menu | — | Ẩn với người chỉ có quyền xem | — | Góc phải bảng; mục Start withdrawal, Start temporary withdrawal, Start transfer (BR-003). |
| Bảng Enrolments | Bảng | — | Mới nhất trước | — | Cột theo BR-001; chỉ xem. |
| Status | Nhãn | — | — | — | Active, Transferred, Completed (BR-002). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Tab đọc dữ liệu ghi danh của trẻ; change log lưu vào History của trẻ theo BR-004. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan có 3 lần ghi danh: N2 Sunbeams 2026 đang học, N1 Little Stars 2025 đã chuyển Centre, Infant care Little Stars 2024 đã kết thúc | người dùng mở tab Enrolment | bảng có 3 dòng, mới nhất trước; dòng 2026 End date “ongoing”, Status Active; dòng 2025 Transferred; dòng 2024 Completed; tóm tắt “3 enrolments · 1 running now” | FR-001; BR-001; BR-002; DATA-001 |
| AC-002 | người dùng có quyền | chọn “⋯” › Start transfer | hệ thống chuyển sang màn hình tạo Transfer của Joining & leaving cho Ethan; History có dòng tạo yêu cầu transfer kèm người thực hiện, thời điểm | FR-002; FR-003; BR-003; BR-004 |
| AC-003 | người dùng chỉ có quyền xem | mở tab Enrolment | không có nút “⋯”; bảng Enrolments hiển thị đầy đủ | BR-003 |

#### Dependencies (Phụ thuộc)

Enrolment; Joining & leaving; History của trẻ (BBA-66).

### 6.2 BBA-67: US-002 - Tab Enrichment

#### User Story

Là người dùng, tôi muốn xem các lớp enrichment của trẻ, để biết trẻ học gì, khi nào, ở đâu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Tab chỉ hiển thị các lớp enrichment của trẻ đã đăng ký và yêu cầu đang chờ HQ xác nhận (BR-005, BR-006, BR-007). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Enrichment; hệ thống hiển thị bảng Enrichment programmes (FR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ có yêu cầu tham gia lớp đang chờ HQ: dòng lớp có trạng thái Waiting, nằm đầu bảng (BR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa học lớp enrichment nào: hiển thị thông báo rỗng (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Mỗi lớp một dòng: Programme, Centre, Day, From, To, Start date, End date, Status. Status gồm Waiting (chờ HQ xác nhận), Active (đang học), Completed (đã học xong), Withdrawn (đã rút). Lớp đang học có End date “—”. Một trẻ học được nhiều lớp. |
| BR-006 | Thứ tự: lớp Waiting trước, rồi lớp đang học, rồi lớp đã kết thúc. Lớp Waiting chưa có lịch học và ngày: các ô Day, From, To, Start date, End date hiện “—”. |
| BR-007 | Tab chỉ hiển thị thông tin; không có thao tác thêm, sửa, xóa. Người có quyền thao tác và người chỉ có quyền xem thấy cùng một nội dung. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Trẻ chưa có lớp enrichment và không có yêu cầu chờ. | Hiển thị “No enrichment programme for this child.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Enrichment | Wireframe BBA-67 › tab Enrichment |

#### UX / UI

1. Tab Enrichment nằm sau tab Enrolment trên thanh tab của hồ sơ trẻ; tab đang chọn được gạch chân.
2. Nội dung tab là một khối duy nhất: tiêu đề “Enrichment programmes”; bên dưới, dòng phụ “Pending requests first, followed by current and past programmes.” ở bên trái và dòng tóm tắt ở bên phải; sau đó là bảng.
3. Dòng tóm tắt đếm theo bảng: tổng số lớp, số lớp Waiting, số lớp Active, ví dụ “5 programmes · 1 Waiting · 2 active”.
4. Tên Programme in đậm. Dòng Waiting có nền màu nhạt để nổi bật yêu cầu đang chờ.
5. Status hiển thị dạng nhãn (badge): Waiting màu vàng, Active màu xanh lá, Completed và Withdrawn màu xám.
6. Bảng không có nút, không có ô chọn, không có menu thao tác; không bấm vào dòng để mở màn hình khác.
7. Ô không có dữ liệu hiển thị “—”. Ngày hiển thị dạng “01 Jul 2026”; giờ dạng 24 giờ “15:30”.

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tiêu đề | Display | — | “Enrichment programmes” | — | Dòng phụ “Pending requests first, followed by current and past programmes.” |
| Tóm tắt | Display | — | — | — | “n programmes · n Waiting · n active”. |
| Bảng Enrichment programmes | Bảng | — | Theo thứ tự BR-006 | VAL-001. | Cột Programme, Centre, Day, From, To, Start date, End date, Status; chỉ xem (BR-005; BR-007). |
| Day | Display | — | “—” khi Waiting | — | Thứ trong tuần của buổi học, ví dụ Thursday. |
| From / To | Display | — | “—” khi Waiting | — | Giờ bắt đầu / kết thúc buổi học, ví dụ 15:30 / 16:30. |
| Start date / End date | Display | — | “—” khi chưa có | — | Ngày bắt đầu / kết thúc học lớp; lớp đang học End date “—”. |
| Status | Nhãn | — | — | — | Waiting, Active, Completed, Withdrawn (BR-005). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Tab đọc dữ liệu của Learning; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-004 | trẻ học Speech & Drama (Thứ Năm 15:30–16:30) và Swimming từ 01/07/2026; đã học xong Little Coders (12/01–29/06/2026); đã rút Art Explorers; yêu cầu Mandarin Explorers chờ HQ | người dùng mở tab Enrichment | tóm tắt “5 programmes · 1 Waiting · 2 active”; dòng đầu Mandarin Explorers Waiting, các ô lịch và ngày “—”; tiếp theo Speech & Drama, Swimming Active, End date “—”; sau cùng Little Coders Completed, Art Explorers Withdrawn | FR-004; BR-005; BR-006; DATA-002 |
| AC-005 | người dùng có quyền thao tác hoặc chỉ có quyền xem | mở tab Enrichment | cùng một nội dung; không có thao tác thêm, sửa, xóa | BR-007 |
| AC-006 | trẻ chưa có lớp enrichment | mở tab Enrichment | hiện “No enrichment programme for this child.” | VAL-001 |

#### Dependencies (Phụ thuộc)

Learning › Enrichment.

### 6.3 BBA-67: US-003 - Tab Attendance

#### User Story

Là người dùng, tôi muốn xem giờ vào, giờ ra và nhiệt độ của trẻ theo từng ngày, để trả lời phụ huynh mà không phải mở màn điểm danh của lớp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Tab hiển thị thông tin điểm danh của trẻ dạng bảng: giờ vào, giờ ra, nhiệt độ (BR-008). |
| FR-006 | Tab hiển thị xe đưa rước của trẻ ở dạng chỉ xem (BR-009). |
| FR-007 | Tab chỉ hiển thị; không có thao tác thêm, sửa, xóa (BR-010). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Attendance; hệ thống hiển thị bảng điểm danh và xe đưa rước của trẻ (FR-005, FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Ngày chưa có giờ ra hoặc chưa đo nhiệt độ: ô thiếu hiển thị “—” (BR-008).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa có thông tin điểm danh: hiển thị thông báo rỗng (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Bảng mỗi ngày một dòng: ngày, giờ vào, giờ ra, nhiệt độ đo được trong ngày; mới nhất trước. Dữ liệu lấy từ điểm danh (BBA-73) và đo nhiệt độ (BBA-74). |
| BR-009 | Xe đưa rước (tuyến xe hoặc No bus) lấy từ thông tin điểm danh; chỉ xem, không chọn được trên tab. |
| BR-010 | Tab không có thao tác thêm, sửa, xóa. |

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
| Xe đưa rước | Hiển thị | — | Theo điểm danh | — | Chỉ xem (BR-009). |
| Bảng điểm danh | Bảng | — | Mới nhất trước | VAL-002. | Cột Ngày, Giờ vào, Giờ ra, Nhiệt độ; “—” khi thiếu (BR-008; BR-010). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Tab đọc dữ liệu điểm danh và nhiệt độ; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | ngày 25/11/2026 trẻ vào 08:03, ra 17:20, đo 36.7 °C lúc đến | người dùng mở tab Attendance | dòng 25/11/2026 hiện giờ vào 08:03, giờ ra 17:20, nhiệt độ 36.7 °C | FR-005; BR-008; DATA-003 |
| AC-008 | ngày 26/11/2026 trẻ vào 08:10, chưa ra, chưa đo nhiệt độ | người dùng mở tab Attendance | giờ ra và nhiệt độ hiện “—” | BR-008 |
| AC-009 | trẻ đi Bus A — Tampines North loop | người dùng mở tab Attendance | xe đưa rước hiện Bus A, không chọn hay đổi được | FR-006; BR-009 |
| AC-010 | người dùng có quyền xem trẻ | mở tab Attendance | không có thao tác thêm, sửa, xóa | FR-007; BR-010 |
| AC-011 | trẻ chưa có thông tin điểm danh | mở tab Attendance | bảng rỗng | VAL-002 |

#### Dependencies (Phụ thuộc)

Điểm danh đưa / đón (BBA-73); đo nhiệt độ (BBA-74).

### 6.4 BBA-67: US-004 - Tab Finance

#### User Story

Là người dùng, tôi muốn thấy tình hình tài chính của trẻ và xử lý các việc tài chính thường gặp ngay trên hồ sơ, để không phải mở từng màn của Fees & Payments.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-008 | Tab hiển thị tổng quan tài chính của trẻ (BR-011, BR-012). |
| FR-009 | Người dùng có quyền thực hiện các thao tác tài chính trên tab hoặc mở màn tương ứng của Fees & Payments (BR-013). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Finance; hệ thống hiển thị các khối tài chính (FR-008).
2. Người dùng chọn một thao tác ở khối tương ứng (FR-009).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn See what the parent sees: hệ thống hiển thị tài chính như phụ huynh thấy (FR-008).
2. Người dùng chọn số hoá đơn: hệ thống mở chi tiết hoá đơn (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ thuộc Centre Malaysia: không có khối GIRO and CDA accounts và trợ cấp ECDA (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-011 | Các khối: What needs doing (hoá đơn quá hạn); What the flags have done; Subsidies; Bill to; GIRO and CDA accounts; How this family pays (Payment method, citizenship tính phí, tiền đặt cọc đang giữ); Payment schedule; Deposit; Invoices (theo loại); Outstanding and chasing (theo nhóm tuổi nợ); Discounts. |
| BR-012 | Số tài khoản ngân hàng và tiền đặt cọc là trường được bảo vệ: hiển thị đầy đủ, che hoặc ẩn theo quyền; mỗi lần xem đầy đủ ghi History. |
| BR-013 | Thao tác trên tab: Send a reminder (hoá đơn quá hạn), Review child (trợ cấp), Bill to Parent / Company (Save), Export GIRO, Manage (đặt cọc), Add a discount, Open schedule, Open (công nợ). Quy tắc nghiệp vụ của từng thao tác theo Fees & Payments. |

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
| Các khối tài chính | Section | — | — | VAL-003. | BR-011. |
| Nút thao tác | Nút / liên kết | — | Theo quyền | — | BR-013. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Thao tác làm trên tab (Bill to, giảm giá, đặt cọc, nhắc phí) lưu theo Fees & Payments và ghi History của trẻ. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-012 | hoá đơn SW-TAM-ADH-2026-10-0003 quá hạn 37 ngày, SGD 34.88 | người dùng mở tab Finance | What needs doing hiện hoá đơn kèm số ngày quá hạn, số tiền và nút Send a reminder; Outstanding hiện nhóm 31–60 days | FR-008; BR-011 |
| AC-013 | người dùng không có quyền xem đầy đủ tiền đặt cọc | mở tab Finance | tiền đặt cọc bị che | BR-012 |
| AC-014 | Bill to chưa chọn | người dùng có quyền chọn Company, Save | Bill to = Company; History có dòng thay đổi | FR-009; BR-013; DATA-004 |
| AC-015 | trẻ thuộc Centre Malaysia | mở tab Finance | không có khối GIRO and CDA accounts và trợ cấp ECDA | VAL-003 |
| AC-016 | vai trò không có quyền Fees & Payments | mở hồ sơ trẻ | không có tab Finance | VAL-004 |

#### Dependencies (Phụ thuộc)

Fees & Payments (hoá đơn, công nợ, GIRO, trợ cấp, giảm giá, đặt cọc, lịch thanh toán).

### 6.5 BBA-67: US-005 - Tab Communication

#### User Story

Là người dùng, tôi muốn xem các cuộc trao đổi với phụ huynh của trẻ và nhắn tin ngay trên hồ sơ, để không bỏ sót tin phụ huynh đang chờ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-010 | Tab hiển thị các cuộc chat có phụ huynh của trẻ, giống phụ huynh thấy trong app (BR-014, BR-015). |
| FR-011 | Người dùng có quyền bắt đầu tin nhắn và trả lời (BR-016). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Communication; hệ thống hiển thị danh sách cuộc chat (FR-010).
2. Người dùng mở một cuộc chat, nhập trả lời, chọn Send (FR-011).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Start a message để mở cuộc chat mới (FR-011).
2. Người dùng chọn Hide conversation để thu gọn cuộc chat (FR-010).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thread lớp cũ: chỉ đọc, không có ô trả lời (BR-015).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-014 | Mỗi cuộc chat hiện tên, loại (Class, Group, Private), người tham gia, ngày bắt đầu, tin gần nhất; tin cuối của phụ huynh chưa được trả lời hiện “Waiting on a reply · n days”. |
| BR-015 | Người dùng chỉ thấy cuộc chat theo quyền của Communication; Teacher không thấy Private chat Centre Director – phụ huynh. Thread lớp cũ chỉ đọc. |
| BR-016 | Gửi tin, bắt đầu cuộc chat theo quy tắc của Communication. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record › Communication | Prototype: Records › Child › Communication |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Start a message | Nút | — | Theo quyền | — | FR-011. |
| Danh sách cuộc chat | Danh sách | — | — | — | BR-014. |
| Reply / Send | Ô nhập + nút | — | Ẩn ở thread chỉ đọc | — | BR-015; BR-016. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-005 | Tin gửi từ tab lưu ở Communication như tin gửi từ màn Communication. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-017 | tin cuối của Mr Wong trong class thread Bumblebees chưa được trả lời 67 ngày | người dùng mở tab Communication | cuộc chat hiện loại Class, người tham gia, “Waiting on a reply · 67 days” | FR-010; BR-014 |
| AC-018 | người dùng có quyền | nhập trả lời, chọn Send | tin hiện trong cuộc chat | FR-011; BR-016; DATA-005 |
| AC-019 | Teacher của lớp | mở tab Communication | không thấy Private chat Centre Director – phụ huynh; thread lớp cũ không có ô trả lời | BR-015 |

#### Dependencies (Phụ thuộc)

Communication.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Bản trước mô tả tab Communication chỉ hiển thị, không trả lời; prototype có Start a message và Reply / Send. Xác nhận tab cho nhắn tin trực tiếp. | HQ Ops | Cao |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Module sở hữu | Module lưu dữ liệu và quy tắc nghiệp vụ của thao tác; tab chỉ hiển thị hoặc mở thao tác. |
| Trường được bảo vệ | Trường hiển thị đầy đủ, che hoặc ẩn theo quyền; xem đầy đủ được ghi History. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Thứ tự tab | Overview, Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History. | BBA-66 FR-003. |
