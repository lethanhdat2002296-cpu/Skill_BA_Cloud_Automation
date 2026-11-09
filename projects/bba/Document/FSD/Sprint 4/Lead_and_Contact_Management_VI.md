# Lead and Contact Management (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia CRM |
| Module | Lead and Contact Management (Quản lý Lead và Contact) |
| Tính năng | [FSD] Lead and Contact Management - Sprint 4 (mã ticket sẽ cập nhật sau) |
| Mã tài liệu | FSD-CRM-LCM-Sprint4-VI |
| Sprint | 4 |
| Phiên bản | 0.1 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 09/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

> Bản dịch tiếng Việt của FSD tiếng Anh cùng tên. Mã định danh (FR, BR, VAL, DATA, AC, OQ) và thuật ngữ hệ thống (Lead, Enquiry, Contact, Centre Sharing, Reference Log…) giữ nguyên tiếng Anh. Khi hai bản khác nhau, **bản tiếng Anh là bản chuẩn**.

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 09/11/2026 | Business Analysis | Khởi tạo từ BBA CRM SRS v0.1, loại trừ phạm vi đã đặc tả ở Sprint 3 (BBA-40, BBA-41, BBA-42, BBA-44). | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả danh sách Lead, tạo Lead, hồ sơ Lead, trạng thái vòng đời Lead, quan hệ gia đình và Contact master. Còn 10 quyết định mở ở mục 7; quan trọng nhất là bộ trạng thái Lead chính thức (OQ-LCM-01).

## 2. Mục đích và bối cảnh

FSD này đặc tả cách người dùng CRM có quyền tìm, tạo, xem và cập nhật Lead; cách lưu quan hệ gia đình và vai trò trách nhiệm ở cấp Lead; và cách quản lý Contact master dùng chung. Lead là hồ sơ định danh trẻ tiềm năng dùng lại được; Lead khác Enquiry và có thể liên kết với nhiều Enquiry (BR-CRM-001).

Các hành vi đã đặc tả ở Sprint 3 chỉ được dẫn chiếu, không viết lại: Inactive Lead (BBA-40), Centre Sharing (BBA-41), phát hiện trùng Lead / Enquiry và tạo Reference Log cho Lead trùng qua API (BBA-42), Timeline gộp của Lead (BBA-44).

**Quy trình và tham chiếu SRS:** WF-CRM-P1 (tiếp nhận Lead), WF-CRM-P3 (vòng đời Lead) · SRS: BBA_CRM_SRS v0.1 — §2 Vai trò, §3 P1 và P3, §4 Module 2 (2.1 Lead Master, 2.2 Lead Detail, 2.4 Contact and Family Relationships), §5 BR-CRM-001 đến BR-CRM-011 và BR-CRM-046 đến BR-CRM-050, §6.1 thông báo kết quả import Lead, §6.2 import Lead từ Excel, §8 AC-CRM-017, AC-CRM-018, AC-CRM-022, AC-CRM-041 · WBS 2.1.1.03–2.1.1.05 (các mục Phase 2 trong FSD này).

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách, tìm kiếm, lọc theo trạng thái, xuất file và điều hướng Lead (Core Platform); tạo Lead từ staff, website và sự kiện (Core Platform); xem và sửa hồ sơ Lead; hiển thị Enquiry liên quan, Child đã chuyển đổi và Reference Log; quy tắc trạng thái vòng đời Lead; quan hệ gia đình và vai trò trách nhiệm của Lead; Contact master: danh sách, tìm kiếm, kiểm tra trùng, dùng lại, tạo mới, sửa, gộp theo số định danh, xem nơi sử dụng (Core Platform); Bulk reassign Lead owner (WBS Phase 2, 2.1.1.04); Import Leads from Excel (WBS Phase 2, 2.1.1.05). | Inactive Lead và quy tắc chỉ đọc (BBA-40); Centre Sharing (BBA-41); quy tắc trùng Lead / Enquiry và tạo Reference Log qua API (BBA-42); Timeline của Lead (BBA-44); Merge with existing Lead (WBS Phase 2, 2.1.1.03 — FSD riêng); tạo Enquiry và nguyện vọng Enquiry (FSD Enquiry and Customer Journey); hồ sơ Child sau khi nhập học (SMS Children and Families). |

Ranh giới: tính năng này tạo và cập nhật Lead, Contact và quan hệ ở cấp Lead. Tính năng không tạo, không chuyển, không ghi đè nguyện vọng Enquiry, Journey runtime, lịch sử Visit hay hồ sơ Child.

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Admissions / Customer Service | Lead và Contact trong phạm vi Country, Brand, Centre được cấp và danh sách Centre Sharing của Lead. | Tạo và sửa Lead, cập nhật quan hệ gia đình và Contact, đặt Dead Lead khi có quyền. |
| Centre Administration | Lead và Contact của các Centre được cấp. | Cập nhật thông tin gia đình và Contact theo quyền đã cấu hình. |
| HQ Admin | Phạm vi xem liên Centre đã cấu hình. | Giao lại owner hàng loạt và import Lead khi vai trò có quyền này. |
| Marketing | Phạm vi marketing được cấp. | Xem nguồn Lead và Reference Log; import Lead khi vai trò có quyền. |
| System | Lead, Contact và bản ghi quan hệ. | Áp quy tắc trùng (BBA-42), khởi tạo Centre Sharing (BBA-41), suy ra trạng thái vòng đời, kiểm tra file import, ghi audit. |
| Người dùng không có quyền | Ngoài vai trò hoặc phạm vi dữ liệu được cấp. | Không xem, không thay đổi Lead, Contact hay trường dữ liệu bị giới hạn. |

Quyền truy cập theo mô hình phân quyền theo vai trò và phạm vi dữ liệu hiện có. Preferred Centre chỉ là một thuộc tính của Lead; danh sách Centre Sharing mới quyết định Centre nào được xem Lead (SRS §2). Mọi màn hình danh sách hỗ trợ tìm kiếm, lọc, sắp xếp cột, phân trang 20 / 50 / 100 dòng và xuất file trong phạm vi của người dùng. Bản ghi đã được sử dụng trong hệ thống không bao giờ bị xoá.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Chức năng | User Story | Phân loại WBS |
|---|---|---|---|---|
| Lead | Danh sách Lead | Liệt kê, tìm kiếm, lọc theo trạng thái, sắp xếp, phân trang, xuất file và mở Lead. | US-001 | Core Platform (included) |
| Lead | Tạo Lead | Ghi nhận Lead trẻ tiềm năng từ staff, website hoặc sự kiện. | US-002 | Core Platform (included) |
| Lead | Chi tiết Lead | Xem và sửa định danh Lead; xem Enquiry liên quan, Child đã chuyển đổi và Reference Log. | US-003 | Core Platform (included) |
| Lead | Trạng thái vòng đời Lead | Suy ra và đổi trạng thái Lead theo quy tắc chuyển trạng thái đã duyệt. | US-004 | Core Platform (included) |
| Family | Quan hệ gia đình của Lead | Cập nhật quan hệ và vai trò trách nhiệm ở cấp Lead. | US-005 | Core Platform (included) |
| Contact | Contact master | Liệt kê, tìm kiếm, kiểm tra trùng, dùng lại, tạo, sửa và gộp Contact. | US-006 | Core Platform (included) |
| Lead | Giao lại owner hàng loạt | Đổi owner của nhiều Lead đã chọn trong phạm vi được phép. | US-007 | WBS Phase 2 (2.1.1.04) |
| Lead | Import Lead từ Excel | Kiểm tra từng dòng, áp quy tắc trùng và báo kết quả theo dòng. | US-008 | WBS Phase 2 (2.1.1.05) |

## 6. Yêu cầu chức năng theo User Story

### 6.1 US-001 - Tìm và mở Lead

#### User Story

Là người dùng Admissions, tôi muốn liệt kê, tìm kiếm và lọc Lead trong phạm vi của mình để mở đúng hồ sơ trẻ tiềm năng mà không tạo trùng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống liệt kê Lead (hồ sơ định danh trẻ tiềm năng dùng lại được) trong phạm vi Country, Brand, Centre và Centre Sharing của người dùng. |
| FR-002 | Hệ thống tìm Lead theo các trường hiển thị đã duyệt (OQ-LCM-02) và chỉ trả về Lead trong phạm vi của người dùng. |
| FR-003 | Hệ thống lọc Lead theo trạng thái, gồm mọi trạng thái trong bộ trạng thái đã duyệt (OQ-LCM-01). Lead Inactive vẫn tìm được (BBA-40). |
| FR-004 | Hệ thống hỗ trợ sắp xếp cột, phân trang 20, 50 hoặc 100 dòng và xuất danh sách đã lọc trong phạm vi người dùng. |
| FR-005 | Chọn một Lead sẽ mở Lead Detail, không chuyển Lead thành Enquiry. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở danh sách Lead (FR-001).
2. Hệ thống tải các Lead trong phạm vi, sắp xếp theo thứ tự mặc định của prototype đã duyệt (FR-001; VAL-001).
3. Người dùng nhập giá trị tìm kiếm hoặc chọn bộ lọc trạng thái (FR-002, FR-003).
4. Hệ thống trả về các Lead khớp trong phạm vi (FR-002, FR-003).
5. Người dùng mở một Lead; hệ thống hiển thị Lead Detail (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có Lead nào khớp: hiển thị trạng thái rỗng đã duyệt; không tạo Lead.
2. Người dùng xuất danh sách: file chỉ chứa các Lead đã lọc trong phạm vi (FR-004; VAL-002).
3. Người dùng đổi số dòng mỗi trang thành 20, 50 hoặc 100; bộ lọc và thứ tự sắp xếp được giữ (FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Lead ra khỏi phạm vi của người dùng sau khi danh sách đã tải: mở Lead áp dụng hành vi từ chối truy cập chuẩn (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Lead là hồ sơ định danh trẻ tiềm năng dùng lại được, khác Enquiry, và có thể liên kết với nhiều Enquiry (BR-CRM-001). |
| BR-002 | Danh sách, tìm kiếm, lọc và xuất file không bao giờ trả về bản ghi ngoài phạm vi Country, Brand, Centre hoặc Centre Sharing của người dùng (AC-CRM-022). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Lead nằm ngoài phạm vi dữ liệu của người dùng. | Không liệt kê, không mở; áp dụng hành vi từ chối truy cập chuẩn. |
| VAL-002 | Người dùng xuất danh sách đã lọc. | Chỉ xuất các bản ghi do bộ lọc đang áp dụng trả về trong phạm vi. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-001 - Leads list | Màn prototype "Leads" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Ô tìm kiếm | Search field | Không | Trống | Quy tắc tìm kiếm hiện có. | Tìm theo các trường hiển thị đã duyệt trong phạm vi. |
| Lọc trạng thái Lead | Filter | Không | Tất cả trạng thái | Bộ trạng thái đã duyệt. | Thu hẹp danh sách theo trạng thái. |
| Các cột danh sách Lead | Table | Có | Cột theo prototype (OQ-LCM-02) | Trường theo quyền. | Mỗi Lead một dòng; trường bị che theo mô hình quyền. |
| Số dòng mỗi trang | Selector | Có | 20 | 20, 50, 100. | Đổi số dòng hiển thị mỗi trang. |
| Xuất file | Action | Không | Theo quyền | Quyền xuất file. | Xuất danh sách đã lọc trong phạm vi. |
| Dòng Lead | Link | Có | — | Lead trong phạm vi. | Mở Lead Detail. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Liệt kê, tìm kiếm, lọc và xuất file không tạo hay sửa bản ghi Lead. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | người dùng chỉ có phạm vi Centre A và có các Lead chia sẻ với Centre A và Centre B | người dùng mở danh sách Lead | chỉ các Lead chia sẻ với Centre A được liệt kê | FR-001; BR-002; VAL-001 |
| AC-002 | một Lead Inactive trong phạm vi | người dùng lọc theo trạng thái Inactive | Lead Inactive được trả về | FR-003 |
| AC-003 | danh sách đã lọc có 35 Lead | người dùng chọn 20 dòng mỗi trang | trang 1 có 20 dòng, trang 2 có 15 dòng, giữ nguyên bộ lọc | FR-004 |
| AC-004 | đang áp dụng một bộ lọc | người dùng xuất danh sách | file chỉ chứa các Lead đã lọc trong phạm vi | FR-004; VAL-002 |
| AC-005 | một Lead trong danh sách | người dùng mở Lead đó | Lead Detail mở ra và không có Enquiry nào được tạo | FR-005; BR-001 |

#### Dependencies (Phụ thuộc)

Mô hình vai trò, Centre và phạm vi dữ liệu hiện có; danh sách Centre Sharing (BBA-41); bộ trạng thái Lead đã duyệt (OQ-LCM-01); prototype "Leads".

### 6.2 US-002 - Tạo Lead

#### User Story

Là người dùng Admissions, tôi muốn ghi nhận một Lead trẻ tiềm năng mới từ staff, website hoặc sự kiện để gia đình được theo dõi qua Enquiry.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Hệ thống ghi nhận Lead từ staff có quyền, website hoặc API, hoặc sự kiện, với các trường định danh Lead của prototype đã duyệt (OQ-LCM-03). |
| FR-007 | Trước khi lưu, hệ thống chạy kiểm tra trùng Lead của BBA-42 và chuyển kết quả cho luồng xử lý của BBA-42. |
| FR-008 | Không có trùng: hệ thống lưu Lead với trạng thái New và khởi tạo Centre Sharing bằng Centre của người tạo (BBA-41 FR-001). |
| FR-009 | Hệ thống ghi nguồn gốc thật (true source) bất biến của Lead lúc tạo (BR-CRM-004). |
| FR-010 | Hệ thống gán owner của Lead theo quy tắc phân công đã duyệt (OQ-LCM-04). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Create Lead và nhập dữ liệu định danh Lead (FR-006).
2. Người dùng chọn Save; hệ thống kiểm tra các trường bắt buộc (VAL-003).
3. Hệ thống chạy kiểm tra trùng BBA-42 (FR-007).
4. Không có trùng: hệ thống lưu Lead trạng thái New, khởi tạo Centre Sharing, ghi true source và gán owner (FR-008, FR-009, FR-010).
5. Hệ thống mở Lead Detail của Lead mới.

#### Functional Flow - Alternative (Luồng thay thế)

1. Có trùng: áp dụng xử lý kết quả thủ công của BBA-42 (Cancel, Save trên Lead có sẵn, hoặc Reopen Lead); không tạo Lead mới (FR-007).
2. Lead đến từ website hoặc API: áp dụng cùng quy tắc trùng và Centre Sharing, không có màn hình người dùng (FR-006, FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thiếu trường bắt buộc hoặc sai định dạng: không lưu Lead, trường hiển thị thông báo kiểm tra chuẩn (VAL-003).
2. Lưu thất bại: không lưu Lead, Centre Sharing hay bản ghi nguồn nào; hiển thị kết quả thất bại chuẩn (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-003 | Chỉ tạo Lead mới khi BBA-42 không xác nhận trùng; trùng đã xác nhận thì dùng lại Lead có sẵn và không tự gộp Lead (BR-CRM-002, BR-CRM-005). |
| BR-004 | True source và Reference Log là bản chụp tiếp nhận bất biến. Sửa attribution sau này không ghi đè bản chụp đó (BR-CRM-004). |
| BR-005 | Preferred Centre chỉ là thuộc tính của Lead; không cấp quyền truy cập Centre (SRS §2). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Thiếu trường định danh bắt buộc hoặc sai định dạng. | Không lưu; hiển thị thông báo kiểm tra chuẩn tại trường. |
| VAL-004 | Bất kỳ phần nào của giao dịch tạo Lead thất bại. | Rollback Lead, Centre Sharing và bản ghi nguồn; hiển thị kết quả thất bại chuẩn. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-002 - Create Lead | Màn prototype "Leads" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Các trường định danh Lead | Form | Theo OQ-LCM-03 | Trống | Quy tắc từng trường của prototype đã duyệt. | Lead Full Name, Email và Date of Birth là các trường so trùng của BBA-42. |
| Preferred Centre | Selector | Không | Trống | Centre đang hoạt động. | Chỉ lưu là thuộc tính của Lead. |
| Save | Action | Có | Bật | VAL-003. | Chạy kiểm tra trùng rồi lưu. |
| Cancel | Action | Có | Bật | Không. | Đóng màn hình, không tạo Lead. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Lưu người tạo, thời điểm tạo, true source và trạng thái ban đầu New qua cơ chế audit hiện có. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | dữ liệu Lead hợp lệ, không trùng theo BBA-42 | người dùng lưu | Lead được tạo với trạng thái New và Centre của người tạo đứng đầu Centre Sharing | FR-007; FR-008; BR-003 |
| AC-007 | dữ liệu Lead trùng với một Lead có sẵn theo BBA-42 | người dùng lưu | không tạo Lead mới và hiển thị các hành động kết quả của BBA-42 | FR-007; BR-003 |
| AC-008 | một trường định danh bắt buộc để trống | người dùng lưu | Lead không được lưu và trường hiển thị thông báo kiểm tra | VAL-003 |
| AC-009 | Lead được tạo từ website | người dùng sau đó sửa campaign attribution của Lead | true source ghi lúc tạo không đổi | FR-009; BR-004 |
| AC-010 | Preferred Centre là B, Centre người tạo là A | Lead được lưu | Centre B được lưu là Preferred Centre và không được thêm vào Centre Sharing | BR-005 |
| AC-011 | giao dịch lưu thất bại sau bước kiểm tra trùng | kết quả được hiển thị | không có Lead, Centre Sharing hay bản ghi nguồn nào tồn tại | VAL-004 |

#### Dependencies (Phụ thuộc)

Phát hiện trùng BBA-42; khởi tạo Centre Sharing BBA-41; quy tắc phân công owner (OQ-LCM-04); trường định danh Lead đã duyệt (OQ-LCM-03).

### 6.3 US-003 - Xem và sửa hồ sơ Lead

#### User Story

Là người dùng Admissions, tôi muốn xem và sửa hồ sơ Lead, xem các Enquiry liên quan, Child đã chuyển đổi và Reference Log để làm việc trên một hồ sơ định danh chính xác.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-011 | Lead Detail hiển thị thông tin định danh trẻ tiềm năng ở cấp Lead, tách khỏi nguyện vọng và lịch sử của Enquiry. |
| FR-012 | Người dùng có quyền sửa các trường định danh Lead đã duyệt mà không ghi đè nguyện vọng Enquiry, Journey hay lịch sử Visit. |
| FR-013 | Lead Detail liệt kê mọi Enquiry liên kết với Lead kèm Brand và Centre, và mở Enquiry Detail (BBA-43) mà không chuyển lịch sử của Enquiry sang Lead. |
| FR-014 | Khi đã có Child được chuyển đổi, Lead Detail mở hồ sơ Child liên kết mà không thay thế định danh Lead. |
| FR-015 | Lead Detail hiển thị lịch sử Reference Log bất biến, Centre liên quan và true source gốc mà không đổi attribution của Enquiry. |
| FR-016 | Trước khi lưu thay đổi, hệ thống chạy kiểm tra trùng của BBA-42 cho thao tác sửa Lead thủ công. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Lead Detail (FR-011).
2. Hệ thống hiển thị dữ liệu định danh, Enquiry liên quan, Reference Log và link Child nếu có (FR-011, FR-013, FR-014, FR-015).
3. Người dùng sửa các trường định danh và chọn Save (FR-012).
4. Hệ thống kiểm tra các trường và chạy kiểm tra trùng khi sửa theo BBA-42 (VAL-005; FR-016).
5. Không có trùng: hệ thống lưu thay đổi và ghi audit (DATA-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lead chưa có Enquiry: danh sách Enquiry liên quan hiển thị trạng thái rỗng đã duyệt.
2. Chưa có Child: không hiển thị link Child.
3. Người dùng mở một Enquiry liên quan: Enquiry Detail (BBA-43) mở ra (FR-013).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thay đổi tạo ra trùng theo BBA-42: chặn lưu và áp dụng kết quả sửa của BBA-42 (FR-016).
2. Lead đang Inactive: không cho sửa (BBA-40 BR-009).
3. Người dùng khác đã lưu Lead sau khi Lead được mở: từ chối lưu và người dùng xem lại dữ liệu mới (VAL-006).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Quan hệ gia đình và vai trò trách nhiệm của Contact thuộc về Lead, không thuộc Enquiry; Lead Detail hiển thị các Enquiry liên quan mà không sao chép lịch sử vận hành của chúng (BR-CRM-003). |
| BR-007 | Sửa định danh Lead không bao giờ thay đổi nguyện vọng Enquiry, Journey runtime hay lịch sử Visit. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-005 | Trường đã sửa không hợp lệ hoặc trường bắt buộc bị xoá trống. | Không lưu; hiển thị thông báo kiểm tra chuẩn tại trường. |
| VAL-006 | Lead đã thay đổi sau khi người dùng mở. | Từ chối lưu; tải lại Lead và yêu cầu người dùng xem lại trước khi lưu lại. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-003 - Lead Detail | Màn prototype "Lead Detail" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Các trường định danh Lead | Display / Form | Theo OQ-LCM-03 | Giá trị đã lưu | VAL-005. | Sửa được theo quyền; chỉ đọc khi Inactive. |
| Enquiry liên quan | Table | Có | Các Enquiry liên kết / rỗng | Enquiry trong phạm vi. | Hiển thị Enquiry, Brand, Centre và trạng thái; bấm dòng mở Enquiry Detail. |
| Child đã chuyển đổi | Link | Có điều kiện | Hiện khi đã có Child | Quyền truy cập Child. | Mở hồ sơ Child. |
| Reference Log | Table | Có | Các bản ghi đã lưu / rỗng | Chỉ đọc. | Hiển thị ngày, nguồn, campaign, Centre và true source. |
| Edit / Save | Action | Theo quyền | Bật với Lead sửa được | VAL-005, VAL-006; BBA-42. | Lưu thay đổi định danh. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Ghi người sửa, thời điểm, giá trị trước và sau cho mọi thay đổi định danh Lead đã lưu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-012 | một Lead có hai Enquiry ở hai Centre khác nhau | người dùng mở Lead Detail | cả hai Enquiry được liệt kê kèm Brand và Centre | FR-013; BR-006 |
| AC-013 | một Enquiry có preferred Level K1 | người dùng sửa tên Lead và lưu | preferred Level của Enquiry vẫn là K1 | FR-012; BR-007 |
| AC-014 | một Lead đã có Child chuyển đổi | người dùng chọn link Child | hồ sơ Child mở ra và định danh Lead không đổi | FR-014 |
| AC-015 | một Lead có Reference Log từ một lần tiếp nhận qua API | người dùng mở Lead Detail | Reference Log hiển thị nguồn, campaign và Centre ở dạng chỉ đọc | FR-015 |
| AC-016 | thay đổi khiến Lead trùng với Lead khác theo BBA-42 | người dùng lưu | chặn lưu và hiển thị kết quả sửa của BBA-42 | FR-016 |
| AC-017 | người dùng khác đã lưu Lead sau khi Lead được mở | người dùng lưu | từ chối lưu và hiển thị dữ liệu mới | VAL-006 |
| AC-018 | một thay đổi định danh đã lưu | thay đổi được commit | audit ghi người sửa, thời điểm, giá trị cũ và giá trị mới | DATA-003 |
| AC-019 | một Lead sửa được | người dùng xoá trống một trường định danh bắt buộc và lưu | thay đổi không được lưu và trường hiển thị thông báo kiểm tra | VAL-005 |

#### Dependencies (Phụ thuộc)

Kiểm tra trùng khi sửa của BBA-42; Enquiry Detail BBA-43; giới hạn Inactive của BBA-40; hồ sơ Child (SMS Children and Families).

### 6.4 US-004 - Quản lý trạng thái vòng đời Lead

#### User Story

Là người dùng Admissions, tôi muốn trạng thái Lead phản ánh đúng tiến độ của Lead để danh sách, bộ lọc và báo cáo cho biết từng gia đình đang ở bước nào.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-017 | Hệ thống đặt trạng thái New khi Lead được tạo. |
| FR-018 | Hệ thống đổi trạng thái thành Inprogress khi Call đầu tiên của Lead được ghi nhận. |
| FR-019 | Hệ thống đổi trạng thái thành Converted khi có ít nhất một Enquiry liên kết được chuyển đổi. |
| FR-020 | Người dùng có quyền đặt Dead Lead thủ công. |
| FR-021 | Thao tác Inactive Lead (BBA-40) đặt trạng thái inactive / closed theo OQ-LCM-01. |
| FR-022 | Mọi thay đổi trạng thái được kiểm soát theo quyền và ghi vào audit. |

#### Functional Flow - Main (Luồng chính)

1. Lead được tạo với trạng thái New (FR-017).
2. Người dùng ghi Call đầu tiên của Lead; hệ thống đặt Inprogress (FR-018).
3. Một Enquiry của Lead được chuyển đổi; hệ thống đặt Converted (FR-019).
4. Mỗi thay đổi được ghi vào audit (FR-022).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng có quyền đặt Dead Lead kèm lý do theo OQ-LCM-06 (FR-020).
2. Người dùng chạy Inactive Lead: áp dụng BBA-40 (FR-021).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền đổi trạng thái thử đặt Dead Lead: thao tác không hiển thị (VAL-007).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Trạng thái vòng đời Lead gồm New, Inprogress, Converted, Dead Lead và Closed (BR-CRM-008). Inprogress do Call đầu tiên; Converted cần ít nhất một Enquiry đã chuyển đổi; Dead Lead do người dùng chọn; Closed do chức năng Inactive Lead. Tên trạng thái chính thức, kể cả Inactive, chờ OQ-LCM-01. |
| BR-009 | Thay đổi trạng thái được kiểm soát theo quyền và có audit (BR-CRM-008, BR-CRM-022). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-007 | Người dùng không có quyền đổi trạng thái Lead. | Không hiển thị thao tác đổi trạng thái; giữ nguyên trạng thái. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-004 - Lead status | Màn prototype "Lead Detail" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Trạng thái Lead | Display | Có | New | Bộ trạng thái đã duyệt. | Hiển thị trạng thái vòng đời hiện tại. |
| Set Dead Lead | Action | Không | Theo quyền | VAL-007. | Đổi trạng thái thành Dead Lead. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Ghi tác nhân (người dùng hoặc System), thời điểm, trạng thái trước và trạng thái mới cho mọi lần đổi trạng thái Lead. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-020 | một Lead mới | Lead được lưu | trạng thái là New | FR-017; BR-008 |
| AC-021 | một Lead trạng thái New, chưa có Call | người dùng ghi Call đầu tiên | trạng thái thành Inprogress và audit ghi tác nhân là System | FR-018; DATA-004 |
| AC-022 | một Lead có hai Enquiry | một Enquiry được chuyển đổi | trạng thái Lead thành Converted | FR-019 |
| AC-023 | người dùng không có quyền đổi trạng thái | người dùng mở Lead Detail | không hiển thị Set Dead Lead | VAL-007; BR-009 |

#### Dependencies (Phụ thuộc)

Ghi Call (FSD Enquiry and Customer Journey); chuyển đổi Enquiry (FSD Waitlist, Registration and Child Record Preparation); BBA-40; OQ-LCM-01, OQ-LCM-06.

### 6.5 US-005 - Cập nhật quan hệ gia đình của Lead

#### User Story

Là người dùng Admissions, tôi muốn cập nhật các thành viên gia đình của Lead và vai trò trách nhiệm của họ để liên hệ và lập hoá đơn đúng người về sau.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-023 | Lead Detail hiển thị quan hệ gia đình và các Contact liên kết kèm vai trò quan hệ ở cấp Lead. |
| FR-024 | Người dùng có quyền thêm, đổi hoặc bỏ một quan hệ và vai trò của quan hệ đó (Primary, Billing, Emergency, Authorised pickup) ở cấp Lead. |
| FR-025 | Khi thêm thành viên gia đình, hệ thống tìm trong Contact master trước và dùng lại Contact có sẵn (US-006). |
| FR-026 | Dữ liệu Contact master được sửa trong ngữ cảnh Contact; Lead Detail chỉ sửa quan hệ. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở phần Family của Lead Detail (FR-023).
2. Người dùng thêm thành viên gia đình; hệ thống tìm trong Contact master (FR-025).
3. Có Contact khớp: người dùng liên kết Contact và chọn vai trò (FR-024).
4. Hệ thống lưu quan hệ và ghi audit (DATA-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có Contact khớp: người dùng tạo Contact (US-006) rồi liên kết (FR-025).
2. Người dùng chuyển vai trò Primary sang Contact khác: Contact Primary cũ mất vai trò Primary (BR-011).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Lead đang Inactive: không cho đổi quan hệ (BBA-40 BR-009).
2. Chọn Primary thứ hai mà chưa bỏ Primary đầu: hệ thống giữ một Primary theo BR-011.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-010 | Vai trò quan hệ và trách nhiệm (Primary, Billing, Emergency, Authorised pickup) tồn tại ở cấp Lead và Child, không ở cấp Enquiry (BR-CRM-046, BR-CRM-047). |
| BR-011 | Mỗi Lead chỉ có một Primary Contact. Đổi Primary Contact của Child không đổi Primary Contact của Lead liên kết (BR-CRM-049). |
| BR-012 | Contact có sẵn được dùng lại và chỉ tạo thêm quan hệ (BR-CRM-048). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-008 | Người dùng chọn Primary cho một Contact trong khi Lead đã có Contact khác giữ Primary. | Chuyển Primary sang Contact được chọn sau khi người dùng xác nhận; Lead giữ đúng một Primary. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-005 - Lead Family | Màn prototype "Lead Detail" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Thành viên gia đình | Table | Có | Contact liên kết / rỗng | Trường theo quyền. | Hiển thị tên, quan hệ và vai trò. |
| Thêm thành viên gia đình | Action | Không | Theo quyền | Lead sửa được. | Tìm trong Contact master rồi liên kết hoặc tạo mới. |
| Vai trò | Multi-select | Không | Không có | VAL-008. | Primary, Billing, Emergency, Authorised pickup. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-005 | Ghi người sửa, thời điểm, quan hệ và vai trò trước và sau cho mọi thay đổi đã lưu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-024 | đã có Contact khớp với phụ huynh | người dùng thêm phụ huynh vào Lead | Contact có sẵn được liên kết, không tạo Contact mới | FR-025; BR-012 |
| AC-025 | Lead có Primary là Contact A | người dùng đặt Primary cho Contact B và xác nhận | Contact B là Primary, Contact A giữ các vai trò khác | VAL-008; BR-011 |
| AC-026 | một Lead và một Child liên kết có Primary Contact khác nhau | người dùng đổi Primary của Child | Primary của Lead không đổi (AC-CRM-018) | BR-011 |
| AC-027 | một Enquiry của Lead | người dùng mở Enquiry | không hiển thị và không sửa được vai trò quan hệ trên Enquiry | BR-010 |
| AC-028 | một thay đổi quan hệ đã lưu | thay đổi được commit | audit ghi người sửa, thời điểm, giá trị cũ và mới | DATA-005 |

#### Dependencies (Phụ thuộc)

US-006 Contact master; giới hạn Inactive của BBA-40; quan hệ của Child (FSD Waitlist, Registration and Child Record Preparation).

### 6.6 US-006 - Quản lý Contact master

#### User Story

Là người dùng Admissions hoặc Centre Administration, tôi muốn mỗi người chỉ có một hồ sơ dùng chung để thông tin phụ huynh được nhập một lần và nhất quán giữa Lead, Enquiry và Child.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-027 | Hệ thống liệt kê Contact trong phạm vi người dùng và tìm theo tên, số điện thoại, email hoặc Contact ID. |
| FR-028 | Trước khi tạo Contact, hệ thống so khớp chính xác Full name + Phone + Email trong Contact master và đề xuất dùng lại Contact khớp. |
| FR-029 | Hệ thống chỉ tạo Contact mới khi không dùng lại được Contact có sẵn. |
| FR-030 | Sửa Contact master cập nhật cùng một người ở mọi ngữ cảnh Lead, Enquiry và Child liên kết. |
| FR-031 | Khi số định danh (NRIC / FIN / MyKad / Passport) trùng với Contact khác, hệ thống gộp tài khoản theo OQ-LCM-05. |
| FR-032 | Contact Detail hiển thị các quan hệ của Contact với Lead và Child, và dẫn người dùng tới quan hệ của Lead hoặc Child để cập nhật vai trò. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng tìm trong danh sách Contact (FR-027).
2. Người dùng chọn Create Contact và nhập thông tin.
3. Hệ thống so khớp Full name + Phone + Email (FR-028; VAL-009).
4. Không khớp: hệ thống tạo Contact (FR-029).
5. Người dùng liên kết Contact vào quan hệ của Lead hoặc Child (US-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Có Contact khớp chính xác: hệ thống đề xuất Contact có sẵn; người dùng dùng lại (FR-028; BR-012).
2. Người dùng sửa một Contact: thay đổi xuất hiện ở mọi ngữ cảnh liên kết (FR-030).
3. Số định danh trùng với Contact khác: áp dụng gộp theo OQ-LCM-05 (FR-031).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thiếu trường bắt buộc của Contact hoặc sai định dạng: không lưu Contact (VAL-010).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-013 | Sửa Contact master cập nhật cùng một người ở mọi ngữ cảnh Lead, Enquiry và Child liên kết (BR-CRM-050). |
| BR-014 | Vai trò trách nhiệm thuộc về quan hệ của Lead hoặc Child, không thuộc riêng Contact. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-009 | Full name, Phone và Email khớp chính xác với một Contact có sẵn. | Không tạo Contact thứ hai; đề xuất dùng lại Contact có sẵn. |
| VAL-010 | Thiếu trường bắt buộc của Contact hoặc sai định dạng. | Không lưu; hiển thị thông báo kiểm tra chuẩn tại trường. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-006 - Contacts / Contact Detail | Màn prototype "Contacts" và "Contact Detail" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Ô tìm kiếm | Search field | Không | Trống | Tên, số điện thoại, email, Contact ID. | Tìm Contact trong phạm vi. |
| Full name, Phone, Email | Form | Có | Trống | VAL-009, VAL-010. | Dùng để kiểm tra trùng. |
| Số định danh | Form | Không | Trống | Định dạng NRIC / FIN / MyKad / Passport. | Dùng để gộp (OQ-LCM-05). |
| Nơi sử dụng quan hệ | Table | Có | Lead và Child liên kết | Chỉ đọc. | Mở quan hệ của Lead hoặc Child. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-006 | Ghi người sửa, thời điểm, giá trị trước và sau cho mọi thay đổi và lần gộp Contact; Contact đã gộp giữ lịch sử. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-029 | Contact "Nguyen Thu Ha", 0901 234 567, ha.nguyen@example.com | người dùng tạo Contact với đúng ba giá trị này | Contact có sẵn được đề xuất và không tạo Contact thứ hai (AC-CRM-017) | FR-028; VAL-009 |
| AC-030 | một Contact liên kết với một Lead và một Child | người dùng đổi số điện thoại của Contact | số mới hiển thị trên Lead và Child | FR-030; BR-013 |
| AC-031 | cùng các giá trị nhưng email khác | người dùng lưu | Contact mới được tạo | FR-029 |
| AC-032 | một Contact liên kết với một Lead | người dùng mở Contact Detail | quan hệ với Lead được liệt kê và mở được quan hệ của Lead | FR-032; BR-014 |
| AC-033 | Create Contact với số điện thoại để trống | người dùng lưu | Contact không được lưu và trường số điện thoại hiển thị thông báo kiểm tra | VAL-010 |

#### Dependencies (Phụ thuộc)

Quyết định về gộp Contact theo số định danh (OQ-LCM-05); US-005; quan hệ của Child.

### 6.7 US-007 - Giao lại owner hàng loạt (WBS Phase 2)

#### User Story

Là HQ Admin, tôi muốn đổi owner của nhiều Lead một lần để phân bổ lại công việc khi nhân sự thay đổi.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-033 | Người dùng có quyền chọn nhiều Lead trong danh sách và gán một owner mới trong phạm vi được phép. |
| FR-034 | Hệ thống lưu từng Lead độc lập, giữ các thay đổi thành công và chỉ rõ từng Lead thất bại. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn các Lead trong danh sách và chọn Reassign owner (FR-033).
2. Người dùng chọn owner mới và xác nhận.
3. Hệ thống cập nhật từng Lead và hiển thị kết quả (FR-034; DATA-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Một số Lead không qua kiểm tra: Lead thành công giữ owner mới; Lead thất bại được liệt kê (FR-034).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Owner mới ngoài phạm vi của Lead hoặc đã ngừng hoạt động: không giao lại Lead đó (VAL-011).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-015 | Giao lại hàng loạt chỉ đổi owner của Lead; owner của Enquiry chỉ đổi theo OQ-LCM-08. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-011 | Owner được chọn đã ngừng hoạt động hoặc không có quyền truy cập Lead. | Bỏ qua Lead đó và liệt kê là thất bại kèm lý do. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-007 - Bulk reassign | Màn prototype "Leads" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Chọn dòng | Checkbox | Không | Chưa chọn | Lead trong phạm vi. | Chọn các Lead cần giao lại. |
| Owner mới | Selector | Có | Trống | VAL-011. | Liệt kê người dùng đang hoạt động trong phạm vi. |
| Thông báo kết quả | Message | Có | Chuẩn của hệ thống | Kết quả thực tế. | Hiển thị thành công, thất bại hoặc thành công một phần. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-007 | Ghi người thực hiện, thời điểm, owner cũ và owner mới cho từng Lead được giao lại. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-034 | 10 Lead được chọn, 1 Lead ngoài phạm vi của owner mới | người dùng xác nhận giao lại | 9 Lead có owner mới, 1 Lead được liệt kê là thất bại kèm lý do | FR-034; VAL-011 |
| AC-035 | một Lead đã được giao lại | thay đổi được commit | audit ghi owner cũ và owner mới | DATA-007 |
| AC-036 | một Lead có Enquiry được giao lại | việc giao lại hoàn tất | owner của Enquiry theo OQ-LCM-08 | BR-015 |

#### Dependencies (Phụ thuộc)

Dữ liệu người dùng và phạm vi; OQ-LCM-08.

### 6.8 US-008 - Import Lead từ Excel (WBS Phase 2)

#### User Story

Là người dùng Marketing hoặc Admissions có quyền, tôi muốn import Lead từ file Excel để danh sách từ sự kiện và campaign vào CRM mà không phải nhập tay.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-035 | Hệ thống nhận file Excel theo mẫu đã duyệt (OQ-LCM-07) và kiểm tra từng dòng. |
| FR-036 | Mỗi dòng hợp lệ áp dụng cùng quy tắc trùng và trùng mơ hồ như tiếp nhận thông thường (BBA-42): không khớp → tạo Lead mới; trùng đã xác nhận → tạo Reference Log trên Lead có sẵn; trùng mơ hồ → chuyển rà soát. |
| FR-037 | Hệ thống báo kết quả từng dòng (đã tạo, Reference Log, mơ hồ, bị từ chối kèm lý do) trên màn kết quả và trong file lỗi tải về được. |
| FR-038 | Người import nhận thông báo kết quả import trong ứng dụng. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng tải lên file Excel (FR-035).
2. Hệ thống kiểm tra từng dòng (VAL-012).
3. Hệ thống áp quy tắc trùng cho từng dòng hợp lệ (FR-036).
4. Hệ thống hiển thị kết quả từng dòng và thông báo cho người dùng (FR-037, FR-038).

#### Functional Flow - Alternative (Luồng thay thế)

1. Dòng khớp với một Lead có sẵn: thêm Reference Log; không tạo Lead (FR-036).
2. Dòng trùng mơ hồ: chuyển rà soát, không tạo (FR-036).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. File không đúng mẫu đã duyệt: dừng import trước khi xử lý dòng nào (VAL-013).
2. Một dòng không qua kiểm tra: dòng đó bị từ chối kèm lý do; các dòng khác tiếp tục (VAL-012).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-016 | Import Excel áp dụng cùng quy tắc trùng và trùng mơ hồ như tiếp nhận thông thường; lỗi import được báo theo từng dòng và không bao giờ bị bỏ qua im lặng (BR-CRM-011). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-012 | Dòng thiếu giá trị bắt buộc hoặc sai định dạng. | Từ chối dòng, ghi lý do trên màn kết quả và trong file lỗi. |
| VAL-013 | File không đúng mẫu đã duyệt. | Dừng import; không xử lý dòng nào; hiển thị lỗi mẫu file. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| LCM: UI-US-008 - Import Leads | Màn prototype "Leads" — chờ link Figma (OQ-LCM-09) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tải file lên | File input | Có | Trống | VAL-013. | Nhận file Excel theo mẫu đã duyệt. |
| Bảng kết quả theo dòng | Table | Có | Sau khi xử lý | — | Hiển thị số dòng, kết quả và lý do. |
| Tải file lỗi | Action | Có điều kiện | Hiện khi có dòng bị từ chối hoặc mơ hồ | — | Tải kết quả theo từng dòng. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-008 | Lưu lần import, người import, thời điểm và kết quả từng dòng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-037 | một dòng Excel khớp với Lead có sẵn | dòng được import | Reference Log được tạo trên Lead có sẵn và kết quả dòng được ghi lại (AC-CRM-041) | FR-036; BR-016 |
| AC-038 | file 50 dòng, 2 dòng thiếu tên bắt buộc | import hoàn tất | 48 dòng được xử lý, 2 dòng bị từ chối kèm lý do và file lỗi liệt kê cả hai | FR-037; VAL-012 |
| AC-039 | file không đúng mẫu đã duyệt | người dùng tải lên | không dòng nào được xử lý và hiển thị lỗi mẫu file | VAL-013 |
| AC-040 | một lần import đã hoàn tất | kết quả sẵn sàng | người import nhận thông báo import trong ứng dụng | FR-038 |

#### Dependencies (Phụ thuộc)

Mẫu import và ánh xạ trường đã duyệt (OQ-LCM-07); quy tắc trùng BBA-42; hàng đợi rà soát cho trùng mơ hồ.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-LCM-01 | Chốt bộ trạng thái Lead. SRS BR-CRM-008 ghi New, Inprogress, Converted, Dead Lead và Closed; SRS mục 2.1 ghi New, Inprogress, Converted, Closed Lead và Inactive; BBA-40 đặt Inactive còn BBA-42 mở lại Closed thành New. | Business Owner | Cao | |
| OQ-LCM-02 | Trường nào của Lead là cột danh sách và là "dữ liệu hiển thị đã duyệt" để tìm kiếm? | Business Owner / Design | Trung bình | |
| OQ-LCM-03 | Trường định danh Lead nào bắt buộc khi tạo (SRS: trường định danh chưa chốt; BBA-42 so Lead Full Name, Email và Date of Birth)? | Business Owner | Cao | |
| OQ-LCM-04 | Owner của Lead được gán thế nào khi tạo (người tạo, mặc định theo Centre, xoay vòng)? | Business Owner | Trung bình | |
| OQ-LCM-05 | Gộp Contact theo số định danh: tự động hay người dùng xác nhận, ai được gộp, giá trị nào được giữ khi hai Contact khác nhau? | Business Owner | Cao | |
| OQ-LCM-06 | Dead Lead: có bắt buộc lý do không, có đảo ngược được không, có ảnh hưởng Enquiry liên kết không? | Business Owner | Trung bình | |
| OQ-LCM-07 | Mẫu file Excel import, các cột bắt buộc, số dòng tối đa mỗi file, ai phụ trách hàng đợi rà soát trùng mơ hồ. | Business Owner / Marketing | Trung bình | |
| OQ-LCM-08 | Giao lại owner của Lead hàng loạt có giao lại cả owner của các Enquiry thuộc Lead không? | Business Owner | Trung bình | |
| OQ-LCM-09 | Link Figma cho các màn Lead và Contact của Sprint 4. | Design | Trung bình | |
| OQ-LCM-10 | Khi Enquiry duy nhất đã chuyển đổi về sau bị rút, Lead có rời trạng thái Converted không? | Business Owner | Thấp | |

## 8. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FSD này |
|---|---|
| Lead | Hồ sơ định danh trẻ tiềm năng dùng lại được, liên kết với một hoặc nhiều Enquiry. |
| Contact | Hồ sơ người dùng chung (phụ huynh, người giám hộ, thành viên gia đình khác). |
| Quan hệ gia đình (Family relationship) | Liên kết giữa một Contact và một Lead hoặc Child, kèm vai trò trách nhiệm. |
| Vai trò trách nhiệm (Responsibility role) | Primary, Billing, Emergency hoặc Authorised pickup, ở cấp Lead hoặc Child. |
| True source | Nguồn tiếp nhận bất biến được ghi khi tạo Lead. |
| Reference Log | Bản ghi tiếp nhận bất biến trên Lead có sẵn khi tiếp nhận bị xác nhận trùng (BBA-42). |
| Core Platform (included) | Phân loại triển khai trong SRS: thuộc nền tảng cơ sở. |
