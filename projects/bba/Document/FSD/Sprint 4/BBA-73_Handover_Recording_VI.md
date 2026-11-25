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

Ghi nhận và quản lý thông tin đưa và đón trẻ trên SMS: ai đưa trẻ đến, ai đón trẻ về, quan hệ với trẻ, giờ đến, giờ về và ảnh bàn giao lúc đón. Thông tin được ghi trên App và hiển thị trên SMS; ngoài ra người dùng có quyền thêm, sửa, xóa thông tin đưa / đón ngay trên SMS, mỗi thay đổi đều có lý do và được ghi lịch sử.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS (Daily Operations › tab Attendance): bảng kết quả điểm danh theo trẻ và ngày, hiển thị giờ đến, người đưa, quan hệ, giờ về, người đón, quan hệ, ảnh bàn giao lúc đón; lọc, tìm kiếm. Thêm, sửa, xóa thông tin đưa / đón ngay trên dòng của trẻ, bắt buộc lý do. Changelog của thông tin đưa / đón. | Đồng bộ dữ liệu giữa App và SMS. Tạo, thêm, duyệt người được phép đón (Children & Families, Parents App). Sửa kết quả điểm danh (Có mặt / Vắng) và Hủy kết quả (BBA-77). Thêm và quản lý nhiệt độ (BBA-74). Đến muộn (BBA-75). Xuất CSV điểm danh. Thông báo cho phụ huynh. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Centre Administrator, Centre Director, Teacher) | Centre / lớp được cấp. | Xem thông tin đưa / đón; thêm, sửa, xóa thông tin đưa / đón; xem Changelog. |
| App | Centre được cấp. | Ghi nhận thông tin đưa / đón khi nhận và trả trẻ, kèm ảnh bàn giao. |
| System | Centre được cấp. | Hiển thị thông tin đưa / đón từ App và SMS; kiểm tra dữ liệu; ghi lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Daily Operations › Attendance** | Xem thông tin đưa / đón | Bảng kết quả điểm danh theo trẻ và ngày; mỗi dòng có giờ đến, người đưa, giờ về, người đón, quan hệ, ảnh bàn giao lúc đón; lọc, tìm kiếm. | BBA-73: US-001 |
| **Daily Operations › Attendance** | Thêm, sửa, xóa thông tin đưa / đón | Sửa ngay trên dòng của trẻ; bắt buộc lý do; ghi Changelog theo từng trường. | BBA-73: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-73: US-001 - Xem thông tin đưa / đón

#### User Story

Là người dùng của Centre, tôi muốn xem ai đưa trẻ đến, ai đón trẻ về và lúc mấy giờ theo từng trẻ, từng ngày, để quản lý việc đưa đón của trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab Attendance hiển thị bảng kết quả điểm danh, mỗi dòng là một trẻ trong một ngày, kèm thông tin đưa / đón (BR-001, BR-002, BR-003). |
| FR-002 | Người dùng tìm kiếm và lọc bảng theo trẻ, ngày, Centre, lớp, kết quả điểm danh (BR-004). |
| FR-003 | Người dùng xem ảnh bàn giao lúc đón của trẻ (BR-005). |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên nhận / trả trẻ trên App, hoặc người dùng ghi trên SMS (US-002); thông tin đưa / đón hiện trên SMS.
2. Người dùng mở Daily Operations › tab Attendance; bảng hiển thị các dòng kết quả, ngày mới nhất trước (FR-001).
3. Người dùng tìm theo tên / mã trẻ hoặc lọc theo Date, Centre, Class, Attendance result (FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng bấm ảnh ở cột Picture: hiện ảnh trẻ cùng người đón, tên người đón, quan hệ, giờ về và nguồn ghi (FR-003; BR-005).
2. Người dùng chọn Xóa bộ lọc: bảng quay về tất cả ngày, ngày mới nhất trước (FR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có dòng nào khớp bộ lọc: bảng hiện "Không có dữ liệu phù hợp với bộ lọc."
2. Trẻ chưa được đưa đến hoặc chưa được đón: ô tương ứng hiện "—" (BR-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi dòng là một kết quả điểm danh của một trẻ trong một ngày, gồm: Ngày, Child, Class, Kết quả, Giờ đến, Người đưa, Quan hệ, Giờ về, Người đón, Quan hệ, Picture. Ô chưa có dữ liệu hiện "—". Dòng đã Hủy kết quả không hiện thông tin đưa / đón. |
| BR-002 | Người đưa là phụ huynh / người trong danh sách của trẻ, người khác ngoài danh sách (Quan hệ hiện "<quan hệ> (Someone else)"), hoặc tài xế xe bus ("Bus driver", Quan hệ hiện số xe). Người đón là người trong danh sách người được phép đón, hoặc phụ xe bus ("Bus attendant", Quan hệ hiện số xe). Cột Quan hệ lấy tự động theo người được chọn. |
| BR-003 | Giờ đến và giờ về hiển thị đúng giờ ghi nhận (HH:mm), không gắn với buổi hay giờ cố định trong ngày. |
| BR-004 | Mặc định bảng hiện mọi ngày, ngày mới nhất trước. Trẻ đang tạm nghỉ (Temporary Withdrawal) không hiện trong các ngày thuộc thời gian tạm nghỉ. |
| BR-005 | Cột Picture hiện ảnh bàn giao lúc đón (ảnh trẻ cùng người đón) khi đã có thông tin đón; chưa có thì hiện "—". |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Daily Operations — tab Attendance (Attendance results) | UX/UI V13: BBA-73-74_Version_moi.html |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Bộ lọc** | | | | | |
| Search child / ID | Ô tìm kiếm | Không | Trống | — | Tìm theo tên hoặc mã trẻ (FR-002). |
| Date | Chọn ngày | Không | Trống = tất cả ngày | — | BR-004. |
| Centre, Class | Danh sách chọn | Không | All centres, All classes | — | FR-002. |
| Attendance result | Danh sách chọn | Không | All results | — | Có mặt, Vắng không phép, Vắng có phép, Đã huỷ kết quả. |
| Xóa bộ lọc | Nút | — | — | — | Đặt lại bộ lọc. |
| **Bảng Attendance results** | | | | | |
| Ngày, Child, Class | Cột | — | — | — | Child có ảnh đại diện và tên. |
| Kết quả | Cột (nhãn) | — | — | — | Có mặt, Vắng không phép, Vắng có phép, Đã huỷ kết quả; chỉ hiển thị trong tài liệu này. |
| Giờ đến, Giờ về | Cột | — | "—" khi chưa có | — | HH:mm (BR-003). |
| Người đưa, Người đón | Cột | — | "—" khi chưa có | — | BR-002. |
| Quan hệ (2 cột) | Cột | — | "—" khi chưa có | — | Lấy tự động theo người đưa / người đón (BR-002). |
| Picture | Biểu tượng ảnh | — | "—" khi chưa đón | — | Bấm mở popup "Ảnh bàn giao lúc đón" (FR-003; BR-005). |
| ⋯ | Menu dòng | Theo quyền | — | — | Sửa, Changelog (US-002). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi kết quả điểm danh lưu thông tin đưa / đón: giờ đến, người đưa, quan hệ người đưa, nguồn ghi người đưa (App / SMS); giờ về, người đón, quan hệ người đón, nguồn ghi người đón (App / SMS); ảnh bàn giao lúc đón. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan được Serena Lim (Mother) đưa đến lúc 08:12 ngày 25/11/2026, chưa được đón | người dùng mở tab Attendance | dòng Ethan 25/11/2026: Giờ đến 08:12, Người đưa Serena Lim, Quan hệ Mother, Giờ về "—", Người đón "—", Picture "—" | FR-001; BR-001; DATA-001 |
| AC-002 | Noah được người giúp việc Siti đưa đến | người dùng mở tab Attendance | Người đưa Siti, Quan hệ "Helper (Someone else)" | BR-002 |
| AC-003 | Lucas đi xe bus Bus 2 đến và về | người dùng mở tab Attendance | Người đưa "Bus driver", Người đón "Bus attendant", Quan hệ "Bus 2" | BR-002 |
| AC-004 | Ethan được Daniel Lim (Father) đón lúc 17:22 ngày 24/11/2026 | người dùng bấm ảnh ở cột Picture | popup "Ảnh bàn giao lúc đón" hiện ảnh trẻ cùng người đón, Daniel Lim, Father, 17:22, nguồn ghi | FR-003; BR-005 |
| AC-005 | có dữ liệu các ngày 23–25/11/2026 | người dùng để trống Date | bảng hiện mọi ngày, 25/11 ở trên | FR-002; BR-004 |
| AC-006 | Millie tạm nghỉ từ 24/11 đến 01/12/2026 | người dùng chọn Date 25/11/2026 | không có dòng của Millie | BR-004 |
| AC-007 | Noah được đưa đến lúc 13:30 | người dùng mở tab Attendance | Giờ đến hiện 13:30 | BR-003 |

#### Dependencies (Phụ thuộc)

App (nhận / trả trẻ, ghi người đưa / người đón và ảnh); danh sách người được phép đón (Children & Families); dịch vụ xe bus; Temporary Withdrawal (Joining & leaving).

### 6.2 BBA-73: US-002 - Thêm, sửa, xóa thông tin đưa / đón

#### User Story

Là người dùng của Centre, tôi muốn thêm, sửa hoặc xóa thông tin đưa / đón ngay trên dòng của trẻ, để thông tin luôn đúng khi App chưa ghi hoặc ghi sai.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Người dùng có quyền chọn Sửa ở menu ⋯ của một dòng để chỉnh thông tin đưa / đón ngay trên dòng đó (BR-006, BR-007, BR-008). |
| FR-005 | Người dùng thêm, sửa hoặc xóa giờ đến, người đưa, giờ về, người đón; kể cả thông tin App ghi nhận (BR-006 đến BR-010). |
| FR-006 | Mỗi lần lưu bắt buộc nhập lý do thay đổi; hệ thống ghi Changelog theo từng trường thay đổi (BR-011). |
| FR-007 | Người dùng xem Changelog của một dòng (BR-012). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn ⋯ › Sửa ở dòng của trẻ; dòng chuyển sang chế độ chỉnh sửa, hiện "Đang chỉnh sửa · thay đổi trực tiếp ở các ô của dòng đã chọn." (FR-004).
2. Người dùng nhập / sửa Giờ đến, chọn Người đưa, nhập / sửa Giờ về, chọn Người đón; cột Quan hệ tự cập nhật (FR-005; BR-006, BR-007).
3. Người dùng nhập Lý do thay đổi, chọn Lưu thay đổi; hệ thống lưu, báo "Đã lưu kết quả điểm danh, log ghi theo từng trường." (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người đưa không có trong danh sách: chọn "+ Someone else — thêm người mới", nhập Họ tên và Quan hệ, chọn Lưu người đưa (BR-006).
2. Xóa thông tin đón: để trống Giờ về và Người đón, nhập lý do, lưu (BR-009).
3. Xóa thông tin đưa: để trống Giờ đến và Người đưa, cùng với thông tin đón, nhập lý do, lưu (BR-009).
4. Người dùng chọn Đóng chỉnh sửa: không lưu thay đổi.
5. Người dùng chọn ⋯ › Changelog: hiện lịch sử của dòng (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thiếu lý do thay đổi: không lưu (VAL-001).
2. Dữ liệu đưa / đón không hợp lệ: không lưu (VAL-002 đến VAL-007).
3. Không có trường nào thay đổi: không lưu (VAL-008).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Người đưa chọn từ: người trong danh sách của trẻ (tên · quan hệ), Someone else (bắt buộc họ tên và quan hệ với trẻ), hoặc Bus driver · <số xe> (chỉ khi trẻ được gán dịch vụ xe bus). Someone else chỉ dùng cho người đưa. |
| BR-007 | Người đón chọn từ: người trong danh sách người được phép đón của trẻ, hoặc Bus attendant · <số xe> (chỉ khi trẻ được gán dịch vụ xe bus). Không có lựa chọn người lạ hay đón tạm thời. |
| BR-008 | Hệ thống tự ghi giờ đến / giờ về khi trẻ đến và về; người dùng sửa được. Giờ đến đi cùng người đưa, giờ về đi cùng người đón: phải nhập cả hai hoặc để trống cả hai. Giờ về không sớm hơn giờ đến. |
| BR-009 | Chỉ ghi được thông tin đón khi đã có thông tin đưa. Xóa thông tin đưa thì phải xóa cả thông tin đón; xóa thông tin đón thì thông tin đưa giữ nguyên. |
| BR-010 | Chỉ ghi thông tin đưa / đón khi kết quả điểm danh của ngày là Có mặt. |
| BR-011 | Mỗi lần lưu bắt buộc có lý do thay đổi. Changelog ghi một dòng cho mỗi trường thay đổi: thời điểm, module, hành động, trường, giá trị cũ, giá trị mới, người thao tác, lý do. Thông tin đã xóa không còn hiển thị nhưng vẫn có trong Changelog. |
| BR-012 | Changelog của một dòng hiển thị theo thứ tự thời gian, gồm cả lịch sử ghi từ App. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Để trống Lý do thay đổi. | Không lưu; hiện "Nhập lý do chỉnh sửa để ghi Changelog." |
| VAL-002 | Có giờ đến mà không có người đưa, hoặc ngược lại. | Không lưu; hiện "Giờ đến và người đưa phải được nhập cùng nhau." |
| VAL-003 | Có giờ về mà không có người đón, hoặc ngược lại. | Không lưu; hiện "Giờ về và người đón phải được nhập cùng nhau." |
| VAL-004 | Có thông tin đón mà không có thông tin đưa. | Không lưu; hiện "Phải có Drop-off trước khi ghi Pick-up." |
| VAL-005 | Giờ về sớm hơn giờ đến. | Không lưu; hiện "Giờ trả trẻ không thể sớm hơn giờ đến." |
| VAL-006 | Someone else thiếu họ tên hoặc quan hệ. | Không lưu; hiện "Enter the name and relationship of the adult." |
| VAL-007 | Người đón không có trong danh sách người được phép đón; hoặc chọn Bus driver / Bus attendant khi trẻ không được gán xe bus. | Không lưu; hiện "Only a person authorised to collect this child may be named here." hoặc "Trẻ không được gán dịch vụ Bus." |
| VAL-008 | Không có trường nào thay đổi. | Không lưu; hiện "Chưa có trường dữ liệu nào được thay đổi." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Tab Attendance — chỉnh sửa trên dòng | UX/UI V13: BBA-73-74_Version_moi.html |
| Someone else — người đưa trẻ (popup) | Như trên |
| Changelog (popup) | Như trên |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Chỉnh sửa trên dòng** | | | | | |
| ⋯ › Sửa | Mục menu | Theo quyền | Tắt khi đang sửa dòng khác | — | Mở chỉnh sửa dòng (FR-004). |
| Giờ đến | Giờ | Cùng Người đưa | Giá trị hiện có | VAL-002; VAL-005. | HH:mm (BR-008). |
| Người đưa | Danh sách chọn | Cùng Giờ đến | Giá trị hiện có | VAL-002; VAL-006. | "— Chọn người đưa —", người trong danh sách, "+ Someone else — thêm người mới", Bus driver · <xe> (BR-006). |
| Giờ về | Giờ | Cùng Người đón | Giá trị hiện có | VAL-003; VAL-004; VAL-005. | HH:mm (BR-008). |
| Người đón | Danh sách chọn | Cùng Giờ về | Giá trị hiện có | VAL-003; VAL-007. | "— Chọn người đón —", người được phép đón, Bus attendant · <xe> (BR-007). |
| Quan hệ (2 cột) | Chỉ đọc | — | Theo người được chọn | — | BR-002. |
| Lý do thay đổi | Ô nhập | Có | Trống | VAL-001. | Ghi vào Changelog (BR-011). |
| Lưu thay đổi / Đóng chỉnh sửa | Nút | — | Hiện khi đang sửa | VAL-001 đến VAL-008. | Lưu hoặc bỏ thay đổi. |
| **Someone else — người đưa trẻ** | | | | | |
| Họ tên người đưa | Ô nhập | Có | Trống | VAL-006. | Ví dụ "Siti". |
| Quan hệ với trẻ | Ô nhập | Có | Trống | VAL-006. | Ví dụ "Helper, Family driver". |
| Hủy / Lưu người đưa | Nút | — | — | VAL-006. | Lưu thì người đưa hiện "<tên> · <quan hệ> (Someone else)" kèm nút Sửa thông tin. |
| **Changelog** | | | | | |
| Changelog · <tên trẻ> | Popup | — | — | — | Cột Thời điểm, Module, Action, Field, Old, New, User, Reason (BR-011; BR-012). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi lần lưu ghi Changelog: mã kết quả điểm danh, trẻ, ngày, hành động, từng trường thay đổi (giá trị cũ, giá trị mới), người thao tác, thời điểm, lý do. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-008 | Ethan Có mặt, App chưa ghi người đón | người dùng chọn ⋯ › Sửa, nhập Giờ về 17:22, chọn Người đón Daniel Lim, Lý do "App chưa ghi", Lưu thay đổi | hiện "Đã lưu kết quả điểm danh, log ghi theo từng trường."; dòng Ethan có Giờ về 17:22, Người đón Daniel Lim, Quan hệ Father | FR-004; FR-005; BR-007 |
| AC-009 | App ghi Ethan được Serena Lim đưa đến | người dùng sửa Người đưa thành Grandmother Lim, nhập lý do, lưu | Người đưa Grandmother Lim, Quan hệ Grandmother; Changelog có Old Serena Lim, New Grandmother Lim, người thao tác, lý do | FR-005; FR-006; BR-011; DATA-002 |
| AC-010 | người dùng sửa dòng, để trống Lý do thay đổi | chọn Lưu thay đổi | không lưu, hiện "Nhập lý do chỉnh sửa để ghi Changelog." | VAL-001 |
| AC-011 | người dùng chọn "+ Someone else — thêm người mới", để trống Quan hệ | chọn Lưu người đưa | không lưu, hiện "Enter the name and relationship of the adult." | BR-006; VAL-006 |
| AC-012 | người dùng nhập Giờ về nhưng không chọn Người đón | chọn Lưu thay đổi | không lưu, hiện "Giờ về và người đón phải được nhập cùng nhau." | BR-008; VAL-003 |
| AC-013 | người dùng chọn Người đưa nhưng để trống Giờ đến | chọn Lưu thay đổi | không lưu, hiện "Giờ đến và người đưa phải được nhập cùng nhau." | BR-008; VAL-002 |
| AC-014 | Ethan đến lúc 08:12 | người dùng nhập Giờ về 07:50, chọn người đón, lưu | không lưu, hiện "Giờ trả trẻ không thể sớm hơn giờ đến." | BR-008; VAL-005 |
| AC-015 | Mia chưa có thông tin đưa | người dùng nhập Giờ về và Người đón, lưu | không lưu, hiện "Phải có Drop-off trước khi ghi Pick-up." | BR-009; VAL-004 |
| AC-016 | Ethan có thông tin đưa và đón | người dùng để trống Giờ về và Người đón, nhập lý do, lưu | Giờ về, Người đón, Picture hiện "—"; thông tin đưa giữ nguyên; Changelog có dòng xóa | BR-009; BR-011 |
| AC-017 | Ethan không được gán xe bus | người dùng mở danh sách Người đưa | không có lựa chọn Bus driver; danh sách Người đón chỉ có người được phép đón của Ethan | BR-006; BR-007; VAL-007 |
| AC-018 | người dùng mở Sửa nhưng không đổi gì | chọn Lưu thay đổi | không lưu, hiện "Chưa có trường dữ liệu nào được thay đổi." | VAL-008 |
| AC-019 | dòng Ethan 24/11/2026 đã sửa 2 lần | người dùng chọn ⋯ › Changelog | popup hiện các dòng lịch sử với Thời điểm, Module, Action, Field, Old, New, User, Reason | FR-007; BR-012 |
| AC-020 | Ava Vắng có phép ngày 25/11/2026 | người dùng nhập Giờ đến và Người đưa, lưu | không lưu; thông tin đưa / đón chỉ ghi khi kết quả Có mặt | BR-010 |

#### Dependencies (Phụ thuộc)

US-001; danh sách người được phép đón (Children & Families); dịch vụ xe bus; kết quả điểm danh (BBA-77).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Thông tin đưa / đón được thêm, sửa, xóa trong khoảng thời gian nào (chỉ trong ngày hay cả ngày trước)? | Centre Director / HQ Ops | Cao | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Kết quả điểm danh | Bản ghi điểm danh của một trẻ trong một ngày: Có mặt, Vắng không phép, Vắng có phép, Đã huỷ kết quả. |
| Đưa trẻ (Drop-off) | Trẻ được đưa đến Centre, kèm giờ đến và người đưa. |
| Đón trẻ (Pick-up) | Trẻ được đón về, kèm giờ về và người đón. |
| Người được phép đón | Người có trong danh sách đón của trẻ (dữ liệu có sẵn ở hồ sơ trẻ). |
| Someone else | Người đưa trẻ không có trong danh sách của trẻ, ghi kèm họ tên và quan hệ. |
| Ảnh bàn giao lúc đón | Ảnh trẻ cùng người đón, chụp trên App khi trả trẻ. |
| Changelog | Lịch sử thay đổi theo từng trường, kèm người thao tác và lý do. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Người đưa | Người trong danh sách của trẻ, Someone else, Bus driver. | Danh sách của trẻ; dịch vụ xe bus. |
| Người đón | Người được phép đón, Bus attendant. | Danh sách người được phép đón; dịch vụ xe bus. |
| Kết quả điểm danh | Có mặt, Vắng không phép, Vắng có phép, Đã huỷ kết quả. | BBA-77. |
