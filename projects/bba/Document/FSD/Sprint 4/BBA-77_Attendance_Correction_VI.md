# BBA-77 Attendance correction with reason (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | Attendance correction with reason |
| Mã ticket | BBA-77 |
| Mã WBS | 3.2.1.07 |
| Mã tài liệu | FRD-BBA-77 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-77: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc sửa trạng thái điểm danh hoặc giờ nhận / trả sau khi đã ghi, lý do bắt buộc, giữ giá trị cũ trong lịch sử, ai được sửa. 3 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Nhân viên đôi khi ghi sai điểm danh: đánh vắng nhầm, ghi sai giờ nhận hoặc giờ trả. Người có quyền sửa lại được sau khi đã ghi, nhưng phải ghi lý do, và giá trị cũ luôn được giữ để đối chiếu khi cần (ví dụ khi kiểm tra trợ cấp).

Mục tiêu đo được: 100% lần sửa có lý do, người sửa, thời điểm, giá trị cũ và giá trị mới.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Sửa trạng thái điểm danh (Present, Absent), giờ nhận, giờ trả, người đưa / người đón. Lý do bắt buộc. Lịch sử giá trị cũ. Tính lại dấu đến muộn. Quyền sửa. | Huỷ một lượt điểm danh sai (yêu cầu huỷ và duyệt). Nghỉ phép (đi qua đơn xin nghỉ). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Centre Admin / School Admin, Centre Director | Centre của mình. | Sửa trực tiếp, có lý do. |
| Senior Teacher được Centre Director giao | Centre của mình. | Sửa trực tiếp, có lý do. |
| Teacher | Lớp của mình. | Không sửa; báo Centre Admin hoặc gửi yêu cầu huỷ (AS-01). |
| HQ Admin | Mọi Centre. | Sửa, có lý do. |
| Hệ thống | Toàn hệ thống. | Lưu lịch sử, tính lại dấu đến muộn và số liệu. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Daily operations › Class attendance | Sửa điểm danh có lý do. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Sửa điểm danh có lý do

#### User Story

Là Centre Admin, tôi muốn sửa trạng thái hoặc giờ điểm danh bị ghi sai và ghi rõ lý do, để số liệu đúng mà vẫn biết trước đó đã ghi gì.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Ở dòng của trẻ trên bảng điểm danh của một ngày, người có quyền chọn "Correct" để sửa: trạng thái (Present, Absent), giờ nhận, giờ trả, người đưa, người đón. |
| FR-002 | Ô lý do là bắt buộc (ít nhất 10 ký tự); không có lý do thì không lưu. |
| FR-003 | Khi lưu, giá trị cũ, giá trị mới, lý do, người sửa và thời điểm được ghi vào lịch sử của lượt điểm danh; giá trị cũ không bị mất. |
| FR-004 | Trạng thái "On leave" không chọn được khi sửa; nghỉ phép chỉ đến từ đơn xin nghỉ đã duyệt. |
| FR-005 | Sửa giờ nhận thì hệ thống tính lại dấu đến muộn (BBA-75). |
| FR-006 | Sửa trạng thái từ Absent sang Present thì phải nhập giờ nhận; người đưa chọn theo quy tắc nhận trẻ (BBA-73). |
| FR-007 | Ngày đã sửa được tính lại trong báo cáo điểm danh, bảng tổng hợp và danh sách trẻ chưa có ngày đi học trong tháng. |
| FR-008 | Chọn biểu tượng lịch sử ở dòng của trẻ để xem mọi lần sửa của lượt điểm danh đó. |
| FR-009 | Không sửa được điểm danh của ngày sau hôm nay; ngày cũ hơn số ngày cho phép (AS-02) không sửa được. |

#### Functional Flow - Main (Luồng chính)

1. Centre Admin mở bảng điểm danh ngày cần sửa, chọn Correct ở dòng của trẻ (FR-001).
2. Centre Admin sửa giá trị, nhập lý do (FR-002), chọn lưu.
3. Hệ thống lưu lịch sử (FR-003), tính lại dấu đến muộn và số liệu (FR-005, FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ bị đánh vắng nhầm: sửa sang Present, nhập giờ nhận (FR-006).
2. Xem lịch sử sửa (FR-008).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có lý do: không lưu (VAL-001).
2. Giờ trả trước giờ nhận: không lưu (VAL-002).
3. Ngày quá giới hạn sửa: không sửa được (VAL-003).
4. Người không có quyền: không có nút Correct (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mọi lần sửa điểm danh phải có lý do. |
| BR-002 | Giá trị cũ luôn được giữ trong lịch sử; không ai xoá được lịch sử. |
| BR-003 | Centre Admin, Centre Director, Senior Teacher được giao và HQ Admin được sửa trực tiếp. |
| BR-004 | Nghỉ phép chỉ đến từ đơn xin nghỉ đã duyệt, không sửa tay. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Lý do trống hoặc dưới 10 ký tự. | Không lưu; hiện "Enter a reason (at least 10 characters)." |
| VAL-002 | Giờ trả trước giờ nhận, hoặc sửa sang Present mà không có giờ nhận. | Không lưu; hiện "Check the times." |
| VAL-003 | Ngày sau hôm nay hoặc cũ hơn giới hạn sửa. | Không có nút Correct; hiện "This day can no longer be corrected." khi rê chuột. |
| VAL-004 | Người dùng không có quyền sửa. | Không có nút Correct. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Class attendance — Correct | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Correct | Nút | Theo quyền | — | VAL-003; VAL-004. | Mở cửa sổ sửa. |
| Trạng thái | Danh sách chọn | Có | Giá trị hiện tại | — | Present, Absent (FR-004). |
| Giờ nhận, giờ trả | Giờ | Theo trạng thái | Giá trị hiện tại | VAL-002. | — |
| Lý do | Ô nhập | Có | Trống | VAL-001. | — |
| Lịch sử | Cửa sổ chi tiết | — | Đóng | — | FR-008. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần sửa lưu: trẻ, ngày điểm danh, trường được sửa, giá trị cũ, giá trị mới, lý do, người sửa, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Mia bị đánh vắng nhầm hôm qua | Centre Admin sửa sang Present, giờ nhận 08:20, lý do "Trẻ có đến, ghi nhầm khi nhận" | điểm danh hôm qua là Present 08:20; lịch sử có Absent → Present, lý do, người sửa | FR-001; FR-003; FR-006; BR-002 |
| AC-002 | Centre Admin sửa giờ nhưng để trống lý do | chọn lưu | không lưu, hiện "Enter a reason (at least 10 characters)." | FR-002; VAL-001; BR-001 |
| AC-003 | giờ nhận 09:34 có dấu Late | sửa thành 08:34 có lý do | dấu Late bị bỏ | FR-005 |
| AC-004 | Centre Admin mở cửa sổ sửa | xem danh sách trạng thái | không có On leave | FR-004; BR-004 |
| AC-005 | giờ nhận 08:12 | sửa giờ trả thành 07:00 | không lưu, hiện "Check the times." | VAL-002 |
| AC-006 | Teacher mở bảng điểm danh | xem dòng của trẻ | không có nút Correct | VAL-004; BR-003 |
| AC-007 | Mia là trẻ Singapore chưa có ngày đi học trong tháng | sửa một ngày sang Present | Mia không còn trong danh sách "No attendance this month" | FR-007 |
| AC-008 | ngày cũ hơn giới hạn sửa | Centre Admin xem dòng của trẻ | không có nút Correct | FR-009; VAL-003 |
| AC-009 | lượt điểm danh đã sửa 2 lần | Centre Director mở lịch sử | thấy 2 lần sửa với giá trị cũ, giá trị mới, lý do, người sửa, thời điểm | FR-008; DATA-001 |

#### Dependencies (Phụ thuộc)

Class attendance; ghi người đưa / người đón (BBA-73); dấu đến muộn (BBA-75); báo cáo điểm danh; danh sách trẻ chưa có ngày đi học trong tháng; quyền giao cho Senior Teacher.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Giáo viên có được gửi yêu cầu sửa (để Centre Admin duyệt) không, hay chỉ báo miệng? | Centre Director / HQ Ops | Trung bình |  |
| OQ-02 | Được sửa điểm danh lùi về tối đa bao nhiêu ngày (ví dụ trong tháng hiện tại)? | Centre Director / HQ Ops | Cao |  |
| OQ-03 | Sửa ngày đã gửi báo cáo trợ cấp cho cơ quan quản lý thì có cần thêm bước gì không? | HQ Ops | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Giáo viên không sửa trực tiếp; báo Centre Admin hoặc gửi yêu cầu huỷ lượt sai. | Mục 4 — chờ OQ-01 |
| AS-02 | Chỉ sửa được ngày trong tháng hiện tại và tháng trước. | FR-009 — chờ OQ-02 |
| AS-03 | Lý do tối thiểu 10 ký tự. | FR-002 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Sửa điểm danh | Thay đổi trạng thái, giờ hoặc người đưa / người đón của một lượt điểm danh đã ghi. |
| Huỷ lượt điểm danh | Bỏ một lượt điểm danh sai hoàn toàn; khác với sửa. |
