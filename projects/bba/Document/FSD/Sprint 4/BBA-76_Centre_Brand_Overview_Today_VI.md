# Centre / Brand Overview Today

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | BBA-76 Centre/brand overview today |
| Mã tài liệu | FRD-3.2.1.06_Centre_Brand_Overview_Today |
| Sprint | 4 |
| Phiên bản | 0.2 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 22/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 22/11/2026 | Business Analysis | Theo format tài liệu đã duyệt: tách 2 User Story (bảng tổng hợp theo Centre / brand; mở xuống lớp). District Manager đổi thành Cluster Head. Đối chiếu prototype. | |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

HQ và Cluster Head cần nhìn một bảng là biết hôm nay mỗi Centre đã nhận bao nhiêu trẻ so với số trẻ dự kiến, bao nhiêu trẻ đã về và còn bao nhiêu trẻ trong trường, theo từng brand, có tổng của các Centre, và mở xuống được từng lớp.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Bảng hôm nay theo Centre: brand, số trẻ đã đến / dự kiến, đã về, còn ở trường. Lọc brand, Centre; sắp xếp. Dòng tổng. Giờ cập nhật và làm mới. Mở xuống các lớp của Centre, rồi đến bảng điểm danh của lớp. | Số liệu nhân viên. Báo cáo điểm danh theo khoảng ngày. Biểu đồ. Nhận / trả trẻ từ bảng tổng hợp. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Admin | Mọi Centre. | Xem bảng tổng hợp và mở xuống lớp. |
| Cluster Head, Operations Manager | Các Centre mình phụ trách. | Xem bảng tổng hợp của các Centre đó và mở xuống lớp. |
| Centre Director | Centre của mình. | Xem dòng của Centre mình và các lớp. |
| System | Centre trong phạm vi người dùng. | Tính số liệu theo điểm danh hôm nay. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy Centre ngoài phạm vi. |

**Quy tắc chung:** Quyền xem theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Daily Operations** | Bảng tổng hợp theo Centre / brand | Mỗi Centre một dòng: brand, đã đến / dự kiến, đã về, còn ở trường; lọc, sắp xếp, dòng tổng, làm mới. | BBA-76: US-001 |
| **Daily Operations** | Mở xuống lớp | Từ một Centre mở bảng các lớp cùng số liệu, từ một lớp mở bảng điểm danh của lớp. | BBA-76: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-76: US-001 - Bảng tổng hợp theo Centre và brand

#### User Story

Là Cluster Head, tôi muốn xem trong một bảng số trẻ đã đến, đã về và còn ở trường của từng Centre tôi phụ trách, theo brand, để biết ngay Centre nào có số trẻ đến thấp bất thường.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Bảng có một dòng cho mỗi Centre trong phạm vi người dùng: Centre, Brand, Signed in of expected, Signed out, Still in (BR-001, BR-002, BR-003). |
| FR-002 | Người dùng lọc theo brand và Centre, sắp xếp theo cột Centre (BR-001). |
| FR-003 | Cuối bảng có dòng tổng của các Centre đang hiển thị (BR-004). |
| FR-004 | Bảng ghi giờ cập nhật và có nút làm mới (BR-005). |

#### Functional Flow - Main (Luồng chính)

1. Cluster Head mở Daily Operations; bảng hiển thị các Centre mình phụ trách, sắp xếp theo tên Centre (FR-001).
2. Cluster Head xem dòng tổng (FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Cluster Head lọc một brand: bảng và dòng tổng chỉ tính các Centre của brand đó (FR-002, FR-003).
2. Cluster Head chọn Refresh để lấy số liệu mới (FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có Centre nào: bảng trống (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Người dùng chỉ thấy Centre trong phạm vi của mình. Mặc định All brands, All centres, sắp xếp theo tên Centre tăng dần. |
| BR-002 | Số trẻ dự kiến (expected) của một Centre = trẻ đang học có lịch học hôm nay, trừ trẻ có nghỉ phép đã duyệt hôm nay và trẻ đang tạm nghỉ. Centre không có trẻ dự kiến (ví dụ ngày đóng cửa) vẫn hiện "0 of 0". |
| BR-003 | Signed in = số trẻ đã được nhận hôm nay; Signed out = số trẻ đã được trả; Still in = Signed in − Signed out. Lượt điểm danh đã huỷ (Void) không được tính. |
| BR-004 | Dòng tổng dạng "<số Centre đang hiển thị> of <tổng Centre trong phạm vi> centres · <tổng đã đến> children signed in of <tổng dự kiến> expected". |
| BR-005 | Bảng hiện "Updated at HH:mm" là giờ lấy số liệu; Refresh lấy lại số liệu. Bảng chỉ để xem, không nhận hay trả trẻ từ bảng. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có Centre nào. | Hiện "No centres match these filters." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Daily Operations — bảng tổng hợp hôm nay | Prototype: Daily operations (bảng Centre / Brand) |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Brand | Bộ lọc | Không | All brands | VAL-001. | Danh sách brand trong phạm vi (FR-002). |
| Centre | Bộ lọc | Không | All centres | VAL-001. | Danh sách Centre trong phạm vi (FR-002). |
| Centre | Cột, sắp xếp được | — | Tăng dần | — | Tên Centre; bấm để mở xuống lớp (US-002). |
| Brand | Cột | — | — | — | — |
| Signed in of expected | Cột | — | — | — | Ví dụ "5 of 7" (BR-002; BR-003). |
| Signed out | Cột | — | — | — | BR-003. |
| Still in | Cột | — | — | — | BR-003. |
| Dòng tổng | Text | — | — | — | BR-004. |
| Updated at, Refresh | Text, nút | — | Giờ mở màn | — | BR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Bảng đọc điểm danh hôm nay, lịch học, nghỉ phép đã duyệt và trạng thái tạm nghỉ của trẻ; không lưu dữ liệu mới. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Small Wonder Tampines có 7 trẻ dự kiến, 5 trẻ đã đến, chưa ai về | HQ Admin mở bảng | dòng Tampines: Brand Small Wonder, "5 of 7", Signed out 0, Still in 5 | FR-001; BR-003 |
| AC-002 | Centre có 8 trẻ có lịch hôm nay, 1 trẻ nghỉ phép đã duyệt | hệ thống tính | số dự kiến là 7 | BR-002; DATA-001 |
| AC-003 | Cluster Head phụ trách 4 Centre | mở bảng | chỉ thấy 4 Centre đó | FR-001; BR-001 |
| AC-004 | HQ Admin thấy 15 Centre | lọc brand Small Wonder | bảng còn 4 Centre Small Wonder; dòng tổng "4 of 15 centres · 12 children signed in of 15 expected" | FR-002; FR-003; BR-004 |
| AC-005 | bảng đang sắp xếp tên Centre tăng dần | HQ Admin bấm tiêu đề cột Centre | bảng sắp xếp giảm dần | FR-002 |
| AC-006 | một lượt nhận trẻ bị Void | hệ thống tính | lượt đó không được tính vào Signed in | BR-003 |
| AC-007 | bảng mở lúc 09:00, có thêm trẻ đến lúc 09:05 | chọn Refresh | số liệu mới, "Updated at 09:05" | FR-004; BR-005 |
| AC-008 | Agape Punggol đóng cửa hôm nay | mở bảng | Agape Punggol hiện "0 of 0" | BR-002 |
| AC-009 | phạm vi của Cluster Head không có Centre Odyssey | lọc brand Odyssey | hiện "No centres match these filters." | VAL-001 |

#### Dependencies (Phụ thuộc)

Class attendance; nghỉ phép đã duyệt; trạng thái tạm nghỉ (Joining & leaving); phạm vi Centre của người dùng (Users & permissions).

### 6.2 BBA-76: US-002 - Mở xuống lớp

#### User Story

Là Cluster Head, tôi muốn từ một Centre mở xem số liệu của từng lớp và bảng điểm danh của lớp, để biết lớp nào có số trẻ đến thấp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Chọn một Centre mở bảng các lớp của Centre đó với cùng các cột số liệu (BR-006). |
| FR-006 | Chọn một lớp mở bảng điểm danh của lớp đó (BR-007). |

#### Functional Flow - Main (Luồng chính)

1. Cluster Head chọn Small Wonder Tampines; hệ thống hiển thị các lớp của Centre với Signed in of expected, Signed out, Still in (FR-005).
2. Cluster Head chọn lớp Sunbeams; hệ thống mở bảng điểm danh của lớp (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Cluster Head chọn breadcrumb để quay lại bảng Centre (FR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Centre không có lớp nào mở: hiện "No classes at this centre today."

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Bảng lớp dùng cùng cách tính của BR-002, BR-003 cho từng lớp; tổng các lớp bằng số liệu của dòng Centre. |
| BR-007 | Bảng điểm danh của lớp mở ở chế độ theo quyền của người dùng: người chỉ có quyền xem thì không có nút nhận / trả trẻ. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Bảng lớp của Centre | Prototype chưa có màn mở xuống lớp; tham khảo thẻ "CLASS · <lớp>" ở Daily operations |
| Class attendance | Prototype: Daily operations › Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Breadcrumb | Đường dẫn | — | — | — | All centres › <Centre>. |
| Class | Cột | — | — | — | Level · tên lớp; bấm để mở bảng điểm danh (FR-006). |
| Signed in of expected, Signed out, Still in | Cột | — | — | — | Như US-001, tính theo lớp (BR-006). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Đọc dữ liệu như DATA-001; không lưu dữ liệu mới. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-010 | Small Wonder Tampines: Sunbeams 3 of 3, Bumblebees 2 of 4 | Cluster Head chọn Tampines | bảng lớp có Sunbeams "3 of 3" và Bumblebees "2 of 4"; tổng bằng "5 of 7" của dòng Centre | FR-005; BR-006 |
| AC-011 | đang xem bảng lớp của Tampines | Cluster Head chọn Sunbeams | mở bảng điểm danh lớp Sunbeams hôm nay | FR-006 |
| AC-012 | Cluster Head chỉ có quyền xem điểm danh | mở bảng điểm danh lớp Sunbeams | không có nút Sign in / Sign out | BR-007 |

#### Dependencies (Phụ thuộc)

US-001; Class attendance.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | "Expected" có trừ trẻ bị đánh vắng (Absent) bằng tay trong ngày không? Có cần thêm cột Not yet in / Absent không? | HQ Ops | Trung bình | |
| OQ-02 | Số liệu cần tự làm mới sau bao nhiêu phút, hay chỉ khi bấm Refresh? | HQ Ops | Thấp | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Expected | Số trẻ dự kiến đến hôm nay (BR-002). |
| Signed in / Signed out / Still in | Đã được nhận / đã được trả / còn ở trường hôm nay (BR-003). |
| Cluster Head | Tên mới của District Manager. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Brand | Small Wonder, Learning Vision, The Schoolhouse, Agape, Brighton Montessori, Odyssey, Bright Path. | Organisation. |
