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

Ghi nhận và quản lý thông tin đưa và đón trẻ trên SMS: ai đưa trẻ đến, ai đón trẻ về, quan hệ với trẻ, giờ đưa, giờ đón và ảnh giao nhận. Thông tin được ghi trên App và hiển thị trên SMS; ngoài ra người dùng có quyền thêm, sửa, xoá thông tin đưa / đón ngay trên SMS.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS (Daily Operations › attendance): hiển thị thông tin đưa / đón của từng trẻ trong ngày (giờ đưa, giờ đón, người đưa, người đón, quan hệ, ảnh giao nhận) lấy từ App và từ SMS; lọc theo xe bus; thêm, sửa, xoá thông tin đưa / đón; lịch sử thay đổi. | Đồng bộ dữ liệu giữa App và SMS. Tạo, thêm, duyệt người được phép đón (Children & Families, Parents App). Trạng thái điểm danh (Present / Absent / On leave). Thông báo cho phụ huynh. Đo nhiệt độ (BBA-74). Đến muộn (BBA-75). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Teacher, Centre Admin, Centre Director) | Lớp / Centre của mình. | Xem thông tin đưa / đón; thêm, sửa, xoá thông tin đưa / đón trên SMS. |
| App | Centre được cấp. | Ghi nhận thông tin đưa / đón khi nhận và trả trẻ. |
| System | Centre được cấp. | Hiển thị thông tin đưa / đón từ App và SMS; kiểm tra người đón theo danh sách; ghi lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Attendance** | Xem thông tin đưa / đón | Mỗi trẻ hiện giờ đưa, giờ đón, người đưa, người đón, ảnh giao nhận; lọc theo xe bus. | BBA-73: US-001 |
| **Attendance** | Thêm, sửa, xoá thông tin đưa / đón | Người dùng thêm, sửa, xoá người đưa / người đón và giờ ngay trên SMS; có lịch sử. | BBA-73: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-73: US-001 - Xem thông tin đưa / đón

#### User Story

Là người dùng của Centre, tôi muốn xem trên màn điểm danh ai đưa trẻ đến, ai đón trẻ về và lúc mấy giờ, để quản lý việc đưa đón từng trẻ trong ngày.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Màn điểm danh hiển thị cho mỗi trẻ: giờ đưa, giờ đón, người đưa, người đón và ảnh giao nhận (BR-001, BR-002, BR-003, BR-004). |
| FR-002 | Người dùng lọc theo xe bus để xem các trẻ đi cùng một xe bus (BR-005). |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên nhận / trả trẻ trên App, hoặc người dùng ghi trên SMS (US-002); thông tin đưa / đón hiện trên SMS.
2. Người dùng mở Daily Operations › attendance, chọn Centre, lớp, ngày (FR-001).
3. Mỗi dòng trẻ hiển thị giờ đưa, giờ đón, Dropped off by, Picked up by và biểu tượng ảnh; người dùng bấm biểu tượng để xem ảnh giao nhận (FR-001; BR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Bus: bảng chỉ còn các trẻ đi xe bus đó, thêm cột Class (FR-002; BR-005).
2. Người dùng chọn một ngày trước: bảng hiển thị thông tin đưa / đón của ngày đó (FR-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa được đưa đến hoặc chưa được đón: ô tương ứng hiện "—" (BR-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi dòng trẻ hiển thị: Arrival (giờ đưa, HH:mm), Departure (giờ đón, HH:mm), Dropped off by, Picked up by, ảnh giao nhận. Ô chưa có dữ liệu hiện "—". |
| BR-002 | Đưa và đón trẻ không gắn với buổi hay giờ cố định trong ngày: trẻ được đưa đến / đón về giờ nào thì hiển thị giờ đó. |
| BR-003 | Dropped off by hiển thị "tên · quan hệ" của người đưa: phụ huynh, người khác (ví dụ người giúp việc, ghi "Someone else"), hoặc tài xế xe bus ("Bus driver · Bus n"). Picked up by hiển thị "tên · quan hệ" của người đón: chỉ người trong danh sách người được phép đón, hoặc phụ xe bus ("Bus attendant · Bus n"). |
| BR-004 | Mỗi lượt đưa / đón ghi trên App có ảnh trẻ cùng người giao / nhận; dòng trẻ có biểu tượng ảnh kèm giờ, bấm để xem ảnh. |
| BR-005 | Lọc theo xe bus chỉ để gom trẻ của một xe bus vào một danh sách; mỗi trẻ vẫn là một dòng riêng với thông tin và ảnh riêng; bảng có thêm cột Class vì một xe bus chở trẻ nhiều lớp. |
| BR-006 | Thông tin hiển thị gồm thông tin App ghi nhận và thông tin người dùng thêm / sửa trên SMS; luôn hiển thị giá trị mới nhất. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Attendance — cột Arrival, Departure, Handover | Prototype: Daily operations › Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Centre, Class, Date | Bộ lọc | Không | Centre và lớp của người dùng, hôm nay | — | — |
| Bus | Bộ lọc | Không | Tất cả | — | Gom trẻ đi cùng xe bus; thêm cột Class (FR-002; BR-005). |
| Child | Cột | — | — | — | Tên trẻ, level · tuổi. |
| Class | Cột | — | Chỉ hiện khi lọc theo xe bus | — | Lớp của trẻ (BR-005). |
| Arrival | Cột | — | "—" khi chưa đưa đến | — | Giờ đưa, HH:mm (BR-001; BR-002). |
| Departure | Cột | — | "—" khi chưa đón | — | Giờ đón, HH:mm (BR-001; BR-002). |
| Dropped off by | Text trong cột Handover | — | "—" khi chưa đưa đến | — | "tên · quan hệ" (BR-003). |
| Picked up by | Text trong cột Handover | — | "—" khi chưa đón | — | "tên · quan hệ" (BR-003). |
| Ảnh giao nhận | Biểu tượng | — | Ẩn khi chưa có | — | "📷 in HH:mm · out HH:mm"; bấm để xem ảnh (BR-004). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lượt đưa / đón gồm: trẻ, lớp, ngày, loại (đưa / đón), giờ, người đưa hoặc người đón (tên, quan hệ; Someone else; Bus driver / Bus attendant và số xe), ảnh giao nhận (nếu có), nguồn ghi (App / SMS). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan được mẹ đưa đến lúc 08:12 (ghi trên App), chưa được đón | người dùng mở attendance | dòng Ethan: Arrival 08:12, Departure "—", "Dropped off by Serena Lim · mother", "Picked up by —", biểu tượng ảnh "in 08:12" | FR-001; BR-001; BR-003; DATA-001 |
| AC-002 | Noah được người giúp việc Siti đưa đến lúc 09:34 và bố đón lúc 17:40 | người dùng mở attendance | dòng Noah: "Dropped off by Siti · Helper (Someone else)", "Picked up by Marcus Tan · father", Arrival 09:34, Departure 17:40 | FR-001; BR-003 |
| AC-003 | Noah học buổi chiều, được đưa đến lúc 13:30 | người dùng mở attendance | Arrival hiện 13:30 | BR-002 |
| AC-004 | Ethan có ảnh giao nhận lúc đưa đến | người dùng bấm biểu tượng ảnh ở dòng Ethan | hiển thị ảnh Ethan cùng người đưa | BR-004 |
| AC-005 | 6 trẻ ở nhiều lớp đi xe bus Bus 2 | người dùng chọn Bus = Bus 2 | bảng chỉ còn 6 trẻ, mỗi trẻ một dòng, có thêm cột Class; người đưa là "Bus driver · Bus 2" | FR-002; BR-003; BR-005 |
| AC-006 | App ghi Ethan được mẹ đưa đến; sau đó người dùng sửa trên SMS thành bà ngoại | người dùng mở lại attendance | dòng Ethan hiện "Dropped off by Grandmother Lim · grandmother" | BR-006 |
| AC-007 | Mia chưa được đưa đến hôm nay | người dùng mở attendance | dòng Mia: Arrival "—", Departure "—", Dropped off by "—", Picked up by "—" | BR-001 |

#### Dependencies (Phụ thuộc)

App (nhận / trả trẻ, ghi người đưa / người đón và ảnh); danh sách người được phép đón (Children & Families); dịch vụ xe bus (Daily Operations › Bus services).

### 6.2 BBA-73: US-002 - Thêm, sửa, xoá thông tin đưa / đón

#### User Story

Là người dùng của Centre, tôi muốn thêm, sửa hoặc xoá thông tin đưa / đón của trẻ ngay trên SMS, để thông tin luôn đúng khi App chưa ghi hoặc ghi sai.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-003 | Người dùng có quyền thêm thông tin đưa (người đưa, giờ đưa) và thông tin đón (người đón, giờ đón) cho trẻ trên SMS (BR-007, BR-008, BR-009). |
| FR-004 | Người dùng có quyền sửa thông tin đưa / đón đã có, kể cả thông tin App ghi nhận (BR-007, BR-008, BR-009). |
| FR-005 | Người dùng có quyền xoá thông tin đưa hoặc thông tin đón của một lượt (BR-010). |
| FR-006 | Hệ thống ghi lịch sử mỗi lần thêm, sửa, xoá (BR-011; DATA-002). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn Record ở dòng trẻ trên màn điểm danh (FR-003).
2. Người dùng chọn người đưa và giờ đưa, hoặc người đón và giờ đón, chọn Save (FR-003; BR-007, BR-008).
3. Hệ thống lưu, báo "Handover recorded on the attendance record.", cập nhật dòng trẻ và ghi lịch sử (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Sửa: người dùng mở Record ở dòng trẻ đã có thông tin, đổi người đưa / người đón hoặc giờ, chọn Save (FR-004).
2. Người đưa không phải phụ huynh (ví dụ người giúp việc): chọn Someone else, nhập tên và quan hệ (BR-007).
3. Xoá: người dùng xoá thông tin đưa hoặc đón, xác nhận; ô tương ứng quay về "—" (FR-005; BR-010).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Someone else thiếu tên hoặc quan hệ: không lưu (VAL-001).
2. Người đón không có trong danh sách người được phép đón: không lưu (VAL-002).
3. Giờ không hợp lệ: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-007 | Người đưa là phụ huynh, Someone else (bắt buộc tên và quan hệ với trẻ), hoặc tài xế xe bus. Someone else chỉ dùng cho người đưa. |
| BR-008 | Người đón chỉ chọn từ danh sách người được phép đón của trẻ (gồm cả phụ huynh) hoặc phụ xe bus; không có lựa chọn người lạ hay đón tạm thời, không có cơ chế cho phép ngoại lệ (override). |
| BR-009 | Giờ đưa không sau giờ hiện tại; giờ đón không trước giờ đưa và không sau giờ hiện tại. Chỉ ghi được giờ đón khi đã có thông tin đưa của ngày đó. |
| BR-010 | Xoá thông tin đưa của một lượt thì cũng xoá thông tin đón của lượt đó; xoá thông tin đón thì thông tin đưa giữ nguyên. Thông tin bị xoá không còn hiển thị nhưng vẫn có trong lịch sử. |
| BR-011 | Mỗi lần thêm, sửa, xoá trên SMS ghi lịch sử: trẻ, ngày, trường thay đổi, giá trị cũ, giá trị mới, người thực hiện, thời điểm. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Chọn Someone else mà để trống tên hoặc quan hệ. | Không lưu; hiện "Enter the name and relationship of the adult." |
| VAL-002 | Người đón không có trong danh sách người được phép đón. | Không lưu; hiện "Only a person authorised to collect this child may be named here." |
| VAL-003 | Giờ vi phạm BR-009. | Không lưu; hiện "Check the time." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Handover (popup) | Prototype: nút Record ở cột Handover |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Record | Nút ở dòng trẻ | Theo quyền | — | — | Mở popup Handover (FR-003; FR-004). |
| Handover · <tên trẻ> | Tiêu đề popup | — | — | — | Ghi chú "Only a person authorised to collect this child may be named here." |
| Dropped off by | Danh sách chọn | Khi ghi thông tin đưa | Giá trị hiện có | VAL-001. | Phụ huynh, Someone else, Bus driver · Bus n (BR-007). |
| Name, Relationship | Ô nhập | Khi chọn Someone else | Ẩn | VAL-001. | Tên và quan hệ với trẻ. |
| Arrival time | Giờ | Khi ghi thông tin đưa | Giá trị hiện có hoặc giờ hiện tại | VAL-003. | HH:mm (BR-009). |
| Picked up by | Danh sách chọn | Khi ghi thông tin đón | Giá trị hiện có | VAL-002. | Người được phép đón (tên · quan hệ), Bus attendant · Bus n (BR-008). |
| Departure time | Giờ | Khi ghi thông tin đón | Giá trị hiện có hoặc giờ hiện tại | VAL-003. | HH:mm (BR-009). |
| Remove drop-off / Remove pick-up | Nút | Theo quyền | Chỉ hiện khi đã có thông tin | — | Xoá sau khi xác nhận (FR-005; BR-010). |
| Save / Close | Nút | — | — | VAL-001; VAL-002; VAL-003. | Lưu, báo "Handover recorded on the attendance record."; hoặc đóng. |
| History | Danh sách | — | — | — | Các lần thêm / sửa / xoá: thời điểm, người thực hiện, giá trị cũ → mới (BR-011). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi lần thêm, sửa, xoá lưu: trẻ, ngày, loại (đưa / đón), trường thay đổi, giá trị cũ, giá trị mới, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-008 | Mia được mẹ đưa đến lúc 08:20 nhưng App chưa ghi | người dùng chọn Record ở dòng Mia, chọn Dropped off by mẹ, Arrival 08:20, Save | hiện "Handover recorded on the attendance record."; dòng Mia: Arrival 08:20, "Dropped off by <mẹ> · mother"; lịch sử có dòng thêm | FR-003; BR-007; BR-011 |
| AC-009 | người dùng chọn Someone else, để trống Relationship | chọn Save | không lưu, hiện "Enter the name and relationship of the adult." | VAL-001 |
| AC-010 | App ghi Ethan được mẹ đưa đến | người dùng sửa Dropped off by thành bà ngoại, Save | dòng Ethan hiện bà ngoại; lịch sử có mẹ → bà ngoại, người sửa, thời điểm | FR-004; FR-006; BR-011; DATA-002 |
| AC-011 | người dùng mở Record của Ethan | chọn Picked up by là người không có trong danh sách người được phép đón | không lưu; hiện "Only a person authorised to collect this child may be named here." | BR-008; VAL-002 |
| AC-012 | Ethan được đưa đến lúc 08:12 | người dùng nhập Departure 07:50 | không lưu, hiện "Check the time." | BR-009; VAL-003 |
| AC-013 | Mia chưa có thông tin đưa hôm nay | người dùng mở Record của Mia | không ghi được Picked up by và Departure | BR-009 |
| AC-014 | Ethan có thông tin đưa và đón | người dùng chọn Remove pick-up, xác nhận | Picked up by và Departure hiện "—"; thông tin đưa giữ nguyên; lịch sử có dòng xoá | FR-005; BR-010; BR-011 |
| AC-015 | Ethan có thông tin đưa và đón | người dùng chọn Remove drop-off, xác nhận | cả thông tin đưa và đón của lượt đó hiện "—"; lịch sử có dòng xoá | BR-010 |

#### Dependencies (Phụ thuộc)

US-001; danh sách người được phép đón (Children & Families); dịch vụ xe bus.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Thông tin đưa / đón được thêm, sửa, xoá trong khoảng thời gian nào (chỉ trong ngày hay cả ngày trước), bởi vai trò nào? | Centre Director / HQ Ops | Cao | |
| OQ-02 | Khi thêm thông tin đưa / đón trên SMS, có bắt buộc tải ảnh giao nhận không? | Centre Director / HQ Ops | Trung bình | |
| OQ-03 | Sửa / xoá thông tin đưa / đón trên SMS có cần nhập lý do không? | Centre Director / HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Đưa trẻ (Drop-off) | Trẻ được đưa đến Centre, kèm giờ và người đưa. |
| Đón trẻ (Pick-up) | Trẻ được đón về, kèm giờ và người đón. |
| Người được phép đón (Authorised pickup) | Người có trong danh sách đón của trẻ (dữ liệu có sẵn ở hồ sơ trẻ). |
| Someone else | Người đưa trẻ không phải phụ huynh, ghi kèm tên và quan hệ; chỉ dùng cho người đưa. |
| Ảnh giao nhận | Ảnh trẻ cùng người đưa / người đón, chụp trên App. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Người đưa | Phụ huynh, Someone else, Bus driver. | Danh sách của trẻ; dịch vụ xe bus. |
| Người đón | Người được phép đón, Bus attendant. | Danh sách người được phép đón; dịch vụ xe bus. |
