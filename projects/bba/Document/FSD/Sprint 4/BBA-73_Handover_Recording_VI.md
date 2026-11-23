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

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Ghi nhận và quản lý thông tin đón và trả trẻ trên SMS. Việc nhận trẻ, trả trẻ, chọn người đưa / người đón và chụp ảnh giao nhận làm trên App. SMS hiển thị thông tin ra vào của từng trẻ do App ghi nhận: giờ vào, giờ ra, ai đưa trẻ đến, ai đón trẻ về, quan hệ với trẻ và ảnh giao nhận. Trên SMS không tạo, sửa hay xoá thông tin đưa đón.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trên SMS (Daily Operations › Class attendance), hiển thị thông tin ra vào của từng trẻ trong ngày: giờ vào, giờ ra, người đưa, người đón (tên, quan hệ), ảnh giao nhận. Lọc theo xe bus. Chỉ xem. | Nhận / trả trẻ, chọn người đưa / người đón, chụp ảnh, chặn người ngoài danh sách (App). Đồng bộ dữ liệu giữa App và SMS. Tạo, sửa, xoá thông tin đưa đón trên SMS. Tạo, thêm, duyệt người được phép đón (Children & Families, Parents App). Thông báo cho phụ huynh. Đo nhiệt độ (BBA-74). Đến muộn (BBA-75). Sửa điểm danh (BBA-77). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Teacher, Centre Admin, Centre Director) | Lớp / Centre của mình. | Xem thông tin ra vào của trẻ trên bảng điểm danh. |
| App | Centre được cấp. | Ghi nhận lượt vào / ra của trẻ (nguồn dữ liệu). |
| System | Centre được cấp. | Hiển thị thông tin ra vào theo dữ liệu App ghi nhận. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy thông tin ra vào của trẻ. |

**Quy tắc chung:** Quyền xem theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Class attendance** | Xem thông tin ra vào của trẻ | Mỗi trẻ hiện giờ vào, giờ ra, người đưa, người đón, ảnh giao nhận; lọc theo xe bus; chỉ xem. | BBA-73: US-001 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-73: US-001 - Xem thông tin ra vào của trẻ

#### User Story

Là người dùng của Centre, tôi muốn xem trên bảng điểm danh ai đưa trẻ đến, ai đón trẻ về và lúc mấy giờ, để quản lý thông tin ra vào của từng trẻ trong ngày.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Bảng điểm danh hiển thị cho mỗi trẻ: giờ vào, giờ ra, người đưa, người đón và ảnh giao nhận (BR-001, BR-002, BR-003, BR-004). |
| FR-002 | Người dùng lọc bảng điểm danh theo xe để xem các trẻ đi cùng một xe bus (BR-005). |
| FR-003 | Thông tin ra vào trên SMS chỉ để xem (BR-006). |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên nhận / trả trẻ trên App; thông tin ra vào của trẻ hiện trên SMS.
2. Người dùng mở Daily Operations › Class attendance, chọn Centre, lớp, ngày (FR-001).
3. Mỗi dòng trẻ hiển thị giờ vào, giờ ra, Dropped off by, Picked up by và biểu tượng ảnh; người dùng bấm biểu tượng để xem ảnh giao nhận (FR-001; BR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Bus route: bảng chỉ còn các trẻ đi xe bus đó, thêm cột Class (FR-002; BR-005).
2. Người dùng chọn một ngày trước: bảng hiển thị thông tin ra vào của ngày đó (FR-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa vào hoặc chưa ra: ô tương ứng hiện "—" (BR-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi dòng trẻ hiển thị: Arrival (giờ vào, HH:mm), Departure (giờ ra, HH:mm), Dropped off by, Picked up by, ảnh giao nhận. Ô chưa có dữ liệu hiện "—". |
| BR-002 | Nhận và trả trẻ không gắn với buổi hay giờ cố định trong ngày: trẻ được đưa đến / đón về giờ nào thì hiển thị giờ đó, đúng theo App ghi nhận. |
| BR-003 | Dropped off by hiển thị "tên · quan hệ" của người đưa: phụ huynh, người khác (ví dụ người giúp việc, ghi "Someone else"), hoặc tài xế xe bus ("Bus driver · Bus n"). Picked up by hiển thị "tên · quan hệ" của người đón: chỉ người trong danh sách người được phép đón, hoặc phụ xe bus ("Bus attendant · Bus n"). |
| BR-004 | Mỗi lượt vào / ra có ảnh trẻ cùng người giao / nhận; dòng trẻ có biểu tượng ảnh kèm giờ, bấm để xem ảnh. |
| BR-005 | Lọc theo xe bus chỉ để gom trẻ của một xe bus vào một danh sách; mỗi trẻ vẫn là một dòng riêng với thông tin và ảnh riêng; bảng có thêm cột Class vì một xe bus chở trẻ nhiều lớp. |
| BR-006 | SMS chỉ hiển thị thông tin ra vào do App ghi nhận; trên SMS không có thao tác tạo, sửa hay xoá thông tin đưa đón. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — cột Arrival, Departure, Handover | Prototype: Daily operations › Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Centre, Class, Date | Bộ lọc | Không | Centre và lớp của người dùng, hôm nay | — | — |
| Bus route | Bộ lọc | Không | Tất cả | — | Gom trẻ đi cùng xe bus; thêm cột Class (FR-002; BR-005). |
| Child | Cột | — | — | — | Tên trẻ, level · tuổi. |
| Class | Cột | — | Chỉ hiện khi lọc theo xe bus | — | Lớp của trẻ (BR-005). |
| Arrival | Cột | — | "—" khi chưa vào | — | Giờ vào, HH:mm (BR-001; BR-002). |
| Departure | Cột | — | "—" khi chưa ra | — | Giờ ra, HH:mm (BR-001; BR-002). |
| Dropped off by | Text trong cột Handover | — | "—" khi chưa vào | — | "tên · quan hệ" (BR-003). |
| Picked up by | Text trong cột Handover | — | "—" khi chưa ra | — | "tên · quan hệ" (BR-003). |
| Ảnh giao nhận | Biểu tượng | — | Ẩn khi chưa có | — | "📷 in HH:mm · out HH:mm"; bấm để xem ảnh (BR-004). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Thông tin hiển thị cho mỗi lượt vào / ra lấy từ dữ liệu App ghi nhận: trẻ, lớp, ngày, loại (vào / ra), giờ, người đưa hoặc người đón (tên, quan hệ; Someone else; Bus driver / Bus attendant và số xe), ảnh giao nhận. SMS không tạo hay sửa dữ liệu này. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan được mẹ đưa đến lúc 08:12 (ghi trên App), chưa về | người dùng mở Class attendance | dòng Ethan: Arrival 08:12, Departure "—", "Dropped off by Serena Lim · mother", "Picked up by —", biểu tượng ảnh "in 08:12" | FR-001; BR-001; BR-003; DATA-001 |
| AC-002 | Noah được người giúp việc Siti đưa đến lúc 09:34 và bố đón lúc 17:40 | người dùng mở Class attendance | dòng Noah: "Dropped off by Siti · Helper (Someone else)", "Picked up by Marcus Tan · father", Arrival 09:34, Departure 17:40 | FR-001; BR-003 |
| AC-003 | Noah học buổi chiều, được đưa đến lúc 13:30 | người dùng mở Class attendance | Arrival hiện 13:30 | BR-002 |
| AC-004 | Ethan có ảnh giao nhận lúc vào | người dùng bấm biểu tượng ảnh ở dòng Ethan | hiển thị ảnh Ethan cùng người đưa | BR-004 |
| AC-005 | 6 trẻ ở nhiều lớp đi Bus 2 | người dùng chọn Bus route Bus 2 | bảng chỉ còn 6 trẻ, mỗi trẻ một dòng, có thêm cột Class; người đưa là "Bus driver · Bus 2" | FR-002; BR-003; BR-005 |
| AC-006 | Chloe đi xe bus Bus 2 về, được phụ xe nhận lúc 17:20 | người dùng mở Class attendance | dòng Chloe: Departure 17:20, "Picked up by Bus attendant · Bus 2" | BR-003 |
| AC-007 | người dùng xem bảng điểm danh | tìm thao tác thêm, sửa, xoá người đưa / người đón hoặc giờ vào / ra | không có thao tác nào; chỉ hiển thị | FR-003; BR-006 |
| AC-008 | Mia chưa được nhận hôm nay | người dùng mở Class attendance | dòng Mia: Arrival "—", Departure "—", Dropped off by "—", Picked up by "—" | BR-001 |
| AC-009 | hôm nay 23/11/2026 | người dùng chọn Date 20/11/2026 | bảng hiển thị thông tin ra vào của ngày 20/11/2026 | FR-001 |

#### Dependencies (Phụ thuộc)

App (nhận / trả trẻ, ghi người đưa / người đón và ảnh); Class attendance; danh sách người được phép đón (Children & Families); dịch vụ xe (Daily Operations › Bus services).

## 7. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lượt vào (Sign in) | Trẻ đến Centre, ghi trên App kèm giờ, người đưa và ảnh. |
| Lượt ra (Sign out) | Trẻ rời Centre, ghi trên App kèm giờ, người đón và ảnh. |
| Người được phép đón (Authorised pickup) | Người có trong danh sách đón của trẻ (dữ liệu có sẵn ở hồ sơ trẻ). |
| Someone else | Người đưa trẻ không phải phụ huynh, ghi kèm tên và quan hệ; chỉ có ở lượt vào. |
| Ảnh giao nhận | Ảnh trẻ cùng người đưa / người đón, chụp trên App mỗi lượt vào / ra. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Người đưa | Phụ huynh, Someone else, Bus driver. | Danh sách của trẻ; dịch vụ xe. |
| Người đón | Người được phép đón, Bus attendant. | Danh sách người được phép đón; dịch vụ xe. |
