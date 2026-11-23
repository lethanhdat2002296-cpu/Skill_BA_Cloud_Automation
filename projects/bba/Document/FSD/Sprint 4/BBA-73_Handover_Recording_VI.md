# Handover Recording

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | BBA-73 Handover recording (dropped off by / picked up by) |
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

Ghi nhận và quản lý thông tin đón và trả trẻ trên SMS. Tài liệu mô tả màn hình lưu những thông tin gì của trẻ mỗi lần trẻ được đưa đến và được đón về: giờ, người đưa / người đón, quan hệ với trẻ, ảnh giao nhận và người ghi. Danh sách người được phép đón của trẻ là dữ liệu có sẵn; màn hình chỉ dùng danh sách này để chọn và đối chiếu, không mô tả việc tạo hay duyệt người đón.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS web (Daily Operations › Class attendance), thông tin ghi nhận mỗi lần đưa / đón trẻ: giờ nhận, giờ trả; người đưa (người trong danh sách hoặc người khác kèm tên và quan hệ); người đón (chỉ người trong danh sách người được phép đón); ảnh trẻ cùng người giao / nhận; người ghi. Chặn trả trẻ cho người ngoài danh sách. Trẻ đi xe. Xem và sửa thông tin đưa / đón trên bảng điểm danh; thông báo cho phụ huynh; lịch sử. | Ứng dụng điểm danh ở cổng (iPad), gồm làm việc khi mất mạng. Tạo, thêm, duyệt người được phép đón (Children & Families, Parents App). Người đón một lần. Đo nhiệt độ khi nhận / trả trẻ (BBA-74). Đến muộn (BBA-75). Sửa trạng thái điểm danh (BBA-77). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Centre Admin, Teacher, Centre Director) | Centre / lớp của mình. | Nhận trẻ, trả trẻ, ghi và sửa người đưa / người đón; xem thông tin đưa / đón. |
| Centre Director | Centre của mình. | Như trên; xem lại các lần người đón không có trong danh sách. |
| Phụ huynh (Parents App) | Con mình. | Nhận thông báo khi con được nhận và được đón, có tên người đưa / người đón và giờ. |
| System | Centre được cấp. | Lấy danh sách người được phép đón, chặn người ngoài danh sách, lưu giờ, người đưa / đón, ảnh và người ghi, gửi thông báo. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Class attendance** | Ghi người đưa trẻ | Khi nhận trẻ, chọn người đưa từ danh sách của trẻ hoặc người khác kèm tên và quan hệ. | BBA-73: US-001 |
| **Class attendance** | Ghi người đón trẻ | Khi trả trẻ, chọn người đón từ danh sách người được phép đón; chặn người ngoài danh sách. | BBA-73: US-002 |
| **Class attendance** | Quản lý thông tin đưa / đón | Xem người đưa, người đón, giờ trên bảng điểm danh; sửa trong ngày; lọc theo xe; thông báo cho phụ huynh; lịch sử. | BBA-73: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-73: US-001 - Ghi người đưa trẻ

#### User Story

Là nhân viên của Centre, khi nhận trẻ tôi muốn ghi ai đưa trẻ đến và lúc mấy giờ, để Centre biết trẻ được giao bởi ai.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Khi nhận trẻ, người dùng chọn người đưa (Dropped off by) từ danh sách phụ huynh và người được phép đón của trẻ, hoặc chọn Someone else và nhập tên, quan hệ (BR-001). |
| FR-002 | Hệ thống lưu giờ nhận, mặc định giờ hiện tại, sửa được trong ngày (BR-002). |
| FR-003 | Người dùng chụp ảnh trẻ cùng người đưa; ảnh lưu vào lượt nhận (BR-004). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Daily Operations › Class attendance, chọn Sign in ở dòng trẻ.
2. Người dùng chọn người đưa trong danh sách, giữ hoặc sửa giờ, chụp ảnh trẻ cùng người đưa, chọn Sign in (FR-001, FR-002, FR-003).
3. Bảng điểm danh hiện giờ nhận và người đưa (US-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người đưa không có trong danh sách (ví dụ người giúp việc): chọn Someone else, nhập tên và quan hệ (FR-001; BR-001).
2. Trẻ đi xe: người đưa là tài xế của xe (BR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Someone else thiếu tên hoặc quan hệ: không lưu (VAL-001).
2. Giờ nhận sau giờ hiện tại: không lưu (VAL-002).
3. Chưa chụp ảnh: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Khi nhận trẻ, người đưa có thể không phải phụ huynh hay người được phép đón (ví dụ tài xế xe, người giúp việc). Người đưa là phụ huynh, người được phép đón, hoặc Someone else; Someone else bắt buộc có tên và quan hệ với trẻ. Someone else chỉ dùng khi nhận trẻ. |
| BR-002 | Nhận và trả trẻ không gắn với buổi trong ngày: mỗi lượt có giờ riêng do người dùng ghi. Giờ mặc định là giờ hiện tại, sửa được trong cùng ngày. |
| BR-003 | Trẻ đi xe: lúc xe đến, người giao là tài xế ("Bus driver · Bus n"); lúc xe về, người nhận là phụ xe ("Bus attendant · Bus n"). Bộ lọc theo xe chỉ để gom trẻ của một xe vào một danh sách; nhận / trả vẫn làm từng trẻ, mỗi trẻ một bản ghi và một ảnh riêng, không có bản ghi chung cho cả nhóm. |
| BR-004 | Mỗi lượt nhận / trả bắt buộc có ảnh trẻ cùng người giao / nhận (trẻ đi xe: cùng tài xế khi xe đến, cùng phụ xe trước khi xe đi). Phụ huynh xem được ảnh này trong Parents App. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Chọn Someone else mà để trống tên hoặc quan hệ. | Không lưu; hiện "Enter the name and relationship of the adult." |
| VAL-002 | Giờ nhận sau giờ hiện tại, hoặc giờ trả trước giờ nhận / sau giờ hiện tại. | Không lưu; hiện "Check the time." |
| VAL-003 | Chưa có ảnh giao nhận. | Nút Sign in / Sign out tắt. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Sign in (popup) | Prototype: Daily operations › Class attendance › Sign in |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Sign in · <tên trẻ> | Tiêu đề popup | — | — | — | — |
| Time | Giờ | Có | Giờ hiện tại | VAL-002. | HH:mm (FR-002). |
| Dropped off by | Danh sách chọn | Có | Trống | VAL-001. | Phụ huynh và người được phép đón (tên · quan hệ); Someone else; trẻ đi xe có thêm "Bus driver · Bus n" (FR-001; BR-003). |
| Name, Relationship | Ô nhập | Khi chọn Someone else | Ẩn | VAL-001. | Tên và quan hệ với trẻ. |
| Photo | Chụp ảnh | Có | Chưa có | VAL-003. | Ảnh trẻ cùng người đưa (BR-004). |
| Recorded by | Display | — | Người dùng hiện tại | — | Vai trò và tên người ghi. |
| Sign in / Close | Nút | — | — | VAL-001; VAL-002; VAL-003. | Lưu lượt nhận hoặc đóng. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lượt nhận / trả lưu: trẻ, lớp, ngày, loại (nhận / trả), giờ; người đưa hoặc người đón (người trong danh sách: tên và quan hệ; Someone else: tên và quan hệ nhập tay; trẻ đi xe: Bus driver / Bus attendant và số xe); ảnh giao nhận; người ghi và vai trò; thời điểm ghi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | bà ngoại của Ethan có trong danh sách người được phép đón | người dùng nhận Ethan, chọn bà ngoại, chọn Sign in | lượt nhận lưu bà ngoại (tên, quan hệ), giờ hiện tại, ảnh và người ghi | FR-001; FR-002; FR-003; DATA-001 |
| AC-002 | người giúp việc đưa Noah đến, không có trong danh sách | người dùng chọn Someone else, Name "Siti", Relationship "Helper" | lượt nhận được lưu kèm tên và quan hệ | FR-001; BR-001 |
| AC-003 | người dùng chọn Someone else, để trống Relationship | chọn Sign in | không lưu, hiện "Enter the name and relationship of the adult." | VAL-001 |
| AC-004 | Noah được bố đưa đến lúc 13:30 (học buổi chiều) | người dùng nhận Noah lúc 13:30 | lượt nhận lưu giờ 13:30, không phụ thuộc buổi sáng / chiều | BR-002 |
| AC-005 | Chloe đi Bus 2 đến trường | người dùng nhận Chloe | người đưa là "Bus driver · Bus 2" | BR-003 |
| AC-006 | 6 trẻ đi Bus 2 đến trường | người dùng lọc Bus 2 và nhận từng trẻ | 6 bản ghi riêng, mỗi bản ghi có ảnh riêng của trẻ cùng tài xế | BR-003; BR-004 |
| AC-007 | người dùng chưa chụp ảnh | nhìn nút Sign in | nút tắt | VAL-003; BR-004 |
| AC-008 | bây giờ là 08:10 | người dùng sửa giờ nhận thành 08:30 | không lưu, hiện "Check the time." | VAL-002 |

#### Dependencies (Phụ thuộc)

Danh sách phụ huynh và người được phép đón của trẻ (Children & Families); dịch vụ xe (Daily Operations › Bus services).

### 6.2 BBA-73: US-002 - Ghi người đón trẻ

#### User Story

Là nhân viên của Centre, khi trả trẻ tôi muốn chọn người đón từ danh sách người được phép đón và được hệ thống chặn nếu người đến đón không có trong danh sách, để trẻ chỉ được giao cho đúng người.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Khi trả trẻ, người dùng chọn người đón (Picked up by) từ danh sách người được phép đón của trẻ; mỗi người hiện thông tin để đối chiếu (BR-005). |
| FR-005 | Người đến đón không có trong danh sách: hệ thống không cho trả trẻ (BR-006). |
| FR-006 | Hệ thống lưu giờ trả, mặc định giờ hiện tại, sửa được trong ngày (BR-002). |
| FR-007 | Người dùng chụp ảnh trẻ cùng người đón; ảnh lưu vào lượt trả (BR-004). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn Sign out ở dòng trẻ đang ở trường.
2. Người dùng chọn người đón trong danh sách, đối chiếu ảnh và giấy tờ, chụp ảnh trẻ cùng người đón, chọn Sign out (FR-004, FR-006, FR-007).
3. Bảng điểm danh hiện giờ trả và người đón (US-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ đi xe về: người nhận là phụ xe của xe (BR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người đến đón không có trong danh sách: người dùng chọn Not on the list; không trả trẻ, gọi phụ huynh (FR-005; BR-006).
2. Chưa chọn người đón: không trả trẻ (VAL-004).
4. Trẻ chưa được nhận: không trả được (VAL-005).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Người đón phải là người trong danh sách người được phép đón của trẻ (gồm cả phụ huynh); không có lựa chọn người lạ hay đón tạm thời. Mỗi người hiện ảnh, họ tên, quan hệ với trẻ và 4 ký tự cuối giấy tờ để đối chiếu. |
| BR-006 | Người không có trong danh sách không được đón trẻ; không có cơ chế cho phép ngoại lệ (override). Hệ thống hiện "Do not release the child. Call the parent to add this person in the Parents App. The person can collect the child once approved." và lưu lại lần này (trẻ, giờ, người ghi) để Centre Director xem. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-004 | Chưa chọn người đón. | Không lưu; hiện "Choose who is collecting the child — a sign-out needs the collector verified." |
| VAL-005 | Trẻ chưa được nhận trong ngày. | Không có nút Sign out ở dòng trẻ. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Sign out (popup) | Prototype: Daily operations › Class attendance › Sign out |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Sign out · <tên trẻ> | Tiêu đề popup | — | — | — | — |
| Time | Giờ | Có | Giờ hiện tại | VAL-002. | HH:mm (FR-006). |
| Picked up by — authorised pickup list | Danh sách chọn | Có | Trống | VAL-004. | Người được phép đón: ảnh, tên · quan hệ, 4 ký tự cuối giấy tờ; trẻ đi xe có thêm "Bus attendant · Bus n" (FR-004; BR-005). |
| Not on the list | Lựa chọn | — | — | — | Hiện cảnh báo của BR-006, khoá nút Sign out (FR-005). |
| Photo | Chụp ảnh | Có | Chưa có | VAL-003. | Ảnh trẻ cùng người đón (BR-004). |
| Recorded by | Display | — | Người dùng hiện tại | — | Vai trò và tên người ghi. |
| Sign out / Close | Nút | — | — | VAL-003; VAL-004. | Lưu lượt trả hoặc đóng. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi lần chọn Not on the list lưu: trẻ, giờ, người dùng, để Centre Director xem lại. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-009 | danh sách người được phép đón của Ethan có Serena Lim (mother) và Marcus Ng (step-parent) | người dùng chọn Sign out của Ethan, mở Picked up by | danh sách có 2 người, mỗi người hiện ảnh, tên · quan hệ, 4 ký tự cuối giấy tờ | FR-004; BR-005 |
| AC-010 | người dùng chọn Serena Lim | chọn Sign out | lượt trả lưu Serena Lim (tên, quan hệ), giờ hiện tại, ảnh và người ghi | FR-004; FR-006; FR-007; DATA-001 |
| AC-011 | người đến đón không có trong danh sách | người dùng chọn Not on the list | không trả trẻ, nút Sign out bị khoá, hiện hướng dẫn gọi phụ huynh; hệ thống lưu lại lần này | FR-005; BR-006; DATA-002 |
| AC-012 | người dùng chưa chọn người đón | chọn Sign out | không lưu, hiện "Choose who is collecting the child — a sign-out needs the collector verified." | VAL-004 |
| AC-013 | Chloe đi Bus 2 về | người dùng trả Chloe, chọn "Bus attendant · Bus 2", chụp ảnh Chloe cùng phụ xe | lượt trả của Chloe lưu riêng với người nhận là phụ xe Bus 2 và ảnh | BR-003; BR-004 |
| AC-014 | Mia chưa được nhận hôm nay | người dùng xem dòng của Mia | không có nút Sign out | VAL-005 |

#### Dependencies (Phụ thuộc)

Danh sách người được phép đón của trẻ (Children & Families).

### 6.3 BBA-73: US-003 - Quản lý thông tin đưa / đón

#### User Story

Là nhân viên của Centre, tôi muốn xem và sửa thông tin đưa / đón của từng trẻ trên bảng điểm danh, để thông tin luôn đúng và phụ huynh biết ai đưa, ai đón con.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-008 | Bảng điểm danh của lớp hiển thị giờ nhận, giờ trả, người đưa, người đón của từng trẻ (BR-007). |
| FR-009 | Người dùng có quyền sửa người đưa / người đón trong ngày qua nút Record ở dòng trẻ (BR-005, BR-008). |
| FR-010 | Người dùng lọc bảng theo xe để xem các trẻ đi cùng một xe (BR-003). |
| FR-011 | Mỗi lượt nhận / trả gửi thông báo trong Parents App cho phụ huynh (BR-009). |
| FR-012 | Hệ thống lưu lịch sử mọi lần ghi và sửa thông tin đưa / đón (DATA-003). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Class attendance; mỗi dòng trẻ hiển thị giờ nhận, giờ trả, Dropped off by, Picked up by (FR-008).
2. Người dùng chọn Record ở dòng trẻ, sửa người đưa hoặc người đón, chọn Save (FR-009).
3. Hệ thống lưu, báo "Handover recorded on the attendance record." và ghi lịch sử (FR-012).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Bus route để xem trẻ của một xe; bảng có thêm cột Class (FR-010).
2. Phụ huynh nhận thông báo khi con được nhận và được đón (FR-011).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Sửa người đón thành người không có trong danh sách: không lưu (BR-008).
2. Sửa thông tin của ngày đã qua: không cho sửa (BR-008).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-007 | Bảng điểm danh hiển thị cho mỗi trẻ: In (giờ nhận), Out (giờ trả), Dropped off by (tên · quan hệ; tài xế "Bus driver · Bus n"; hoặc "Someone else: tên · quan hệ"), Picked up by (tên · quan hệ hoặc "Bus attendant · Bus n"). Ô chưa có dữ liệu hiện "—". |
| BR-008 | Chỉ sửa được thông tin đưa / đón trong ngày. Người đón khi sửa vẫn phải là người trong danh sách người được phép đón; hệ thống hiện "Only a person authorised to collect this child may be named here." |
| BR-009 | Thông báo cho phụ huynh có tên người đưa / người đón, giờ và ảnh giao nhận; không có cờ đến muộn và tên nhân viên ghi. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — cột Handover | Prototype: Daily operations › Class attendance |
| Handover (popup) | Prototype: nút Record ở cột Handover |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Class attendance** | | | | | |
| Centre, Class, Date | Bộ lọc | Không | Centre và lớp của người dùng, hôm nay | — | — |
| Bus route | Bộ lọc | Không | Tất cả | — | Gom trẻ đi cùng xe; thêm cột Class (FR-010). |
| Arrival, Departure | Cột | — | "—" khi chưa có | — | Giờ nhận, giờ trả, HH:mm (BR-007). |
| Handover | Cột | — | "—" khi chưa có | — | "Dropped off by <tên · quan hệ>", "Picked up by <tên · quan hệ>", biểu tượng ảnh giao nhận; nút Record (FR-008; FR-009). |
| Sign in / Sign out | Nút cuối dòng | Theo quyền | — | — | Mở popup của US-001 / US-002. |
| **Handover (popup)** | | | | | |
| Handover · <tên trẻ> | Tiêu đề | — | — | — | Ghi chú "Only a person authorised to collect this child may be named here." |
| Dropped off by | Danh sách chọn | Không | Giá trị hiện có | — | Như US-001. |
| Picked up by | Danh sách chọn | Không | Giá trị hiện có | — | Chỉ người được phép đón (BR-008). |
| Save / Close | Nút | — | — | — | Lưu, báo "Handover recorded on the attendance record." |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi lần sửa thông tin đưa / đón lưu: trẻ, ngày, trường bị sửa, giá trị cũ, giá trị mới, người sửa, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-015 | Ethan được mẹ đưa đến lúc 08:12, chưa về | người dùng mở Class attendance | dòng Ethan: Arrival 08:12, Departure "—", "Dropped off by Serena Lim · mother", "Picked up by —" | FR-008; BR-007 |
| AC-016 | Ethan đã có người đưa là mẹ | người dùng chọn Record, đổi Dropped off by thành bà ngoại, chọn Save | hiện "Handover recorded on the attendance record."; dòng Ethan hiện bà ngoại; lịch sử có giá trị cũ và mới | FR-009; FR-012; DATA-003 |
| AC-017 | người dùng mở Record của Ethan | nhập Picked up by là người không có trong danh sách | không lưu; hiện "Only a person authorised to collect this child may be named here." | BR-008 |
| AC-018 | 6 trẻ ở nhiều lớp đi Bus 2 | người dùng chọn Bus route Bus 2 | bảng chỉ còn 6 trẻ, có thêm cột Class | FR-010 |
| AC-019 | Ethan được bố đón lúc 17:40 | lượt trả được lưu | phụ huynh nhận thông báo có tên người bố, giờ 17:40 và ảnh giao nhận, không có tên nhân viên | FR-011; BR-009 |
| AC-020 | Noah đến lúc 09:34, bị đánh dấu đến muộn | phụ huynh nhận thông báo nhận trẻ | thông báo có tên người đưa và giờ, không có chữ "Late" | BR-009 |
| AC-021 | hôm nay 21/11/2026 | người dùng mở Class attendance ngày 20/11/2026 | không có nút Record để sửa | BR-008 |

#### Dependencies (Phụ thuộc)

US-001, US-002; thông báo trong Parents App; dịch vụ xe.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Trẻ đi xe về nhà: phụ xe của công ty xe có phải nằm trong danh sách người được phép đón của từng trẻ không? | Centre Director / HQ Ops | Trung bình | |
| OQ-02 | Giờ nhận / giờ trả được chỉnh trong khoảng nào, bởi ai; có được nhập giờ tương lai hoặc sửa ngày khác không? (Tài liệu đang để: sửa trong ngày, không nhập giờ tương lai.) | Centre Director / HQ Ops | Trung bình | |
| OQ-03 | Ảnh và thông tin giao nhận được lưu bao lâu, ai được xem / xuất, có tự xoá hoặc ẩn không? | HQ Ops / DPO | Cao | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Nhận trẻ (Sign in) | Ghi trẻ đến Centre, kèm giờ và người đưa. |
| Trả trẻ (Sign out) | Ghi trẻ rời Centre, kèm giờ và người đón. |
| Người được phép đón (Authorised pickup) | Người có trong danh sách đón của trẻ (dữ liệu có sẵn ở hồ sơ trẻ). |
| Someone else | Người đưa trẻ không có trong danh sách, ghi kèm tên và quan hệ; chỉ dùng khi nhận trẻ. |
| Not on the list | Người đến đón không có trong danh sách người được phép đón; không được đón trẻ. |
| Ảnh giao nhận | Ảnh trẻ cùng người đưa / người đón, chụp mỗi lần nhận / trả trẻ. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Người đưa | Phụ huynh, người được phép đón, Bus driver, Someone else. | Danh sách của trẻ; dịch vụ xe. |
| Người đón | Người được phép đón, Bus attendant. | Danh sách người được phép đón; dịch vụ xe. |
