# Attendance Correction with Reason

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | BBA-77 Attendance correction with reason |
| Mã tài liệu | FRD-3.2.1.07_Attendance_Correction |
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
| 0.2 | 22/11/2026 | Business Analysis | Theo format tài liệu đã duyệt: tách 3 User Story (sửa trạng thái điểm danh; sửa giờ nhận / trả; lịch sử giữ giá trị gốc). Thêm Void có lý do theo prototype. Sửa người đưa / người đón chuyển về BBA-73. | |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Nhân viên đôi khi ghi sai điểm danh: đánh vắng nhầm, ghi sai giờ nhận hoặc giờ trả, hoặc ghi một lượt điểm danh không có thật. Người có quyền sửa lại được sau khi đã ghi, nhưng bắt buộc ghi lý do; giá trị gốc luôn được giữ trong lịch sử để đối chiếu khi cần (ví dụ khi kiểm tra trợ cấp).

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Sửa trạng thái điểm danh (Present, Absent, Void) sau khi đã ghi, bắt buộc lý do. Sửa giờ nhận, giờ trả, bắt buộc lý do. Giữ giá trị gốc trong lịch sử; xem lịch sử sửa. Tính lại dấu đến muộn và số liệu điểm danh sau khi sửa. | Nghỉ phép (On leave) — chỉ đến từ đơn xin nghỉ đã duyệt. Sửa người đưa / người đón (BBA-73). Sửa lần đo nhiệt độ (BBA-74). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Centre Admin / School Admin, Centre Director, Senior Teacher được giao, HQ Admin) | Centre / lớp được cấp. | Sửa trạng thái và giờ điểm danh có lý do; Void có lý do; xem lịch sử. |
| Teacher | Lớp của mình. | Ghi điểm danh trong ngày; không sửa sau khi đã ghi (OQ-01). |
| System | Centre được cấp. | Lưu lịch sử, tính lại dấu đến muộn và số liệu. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy thao tác sửa. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Class attendance** | Sửa trạng thái điểm danh | Đổi Present / Absent / Void sau khi đã ghi, bắt buộc lý do. | BBA-77: US-001 |
| **Class attendance** | Sửa giờ nhận / giờ trả | Sửa giờ đã ghi, bắt buộc lý do; tính lại dấu đến muộn. | BBA-77: US-002 |
| **Class attendance** | Lịch sử sửa | Giữ giá trị gốc; xem mọi lần sửa của một lượt điểm danh. | BBA-77: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-77: US-001 - Sửa trạng thái điểm danh

#### User Story

Là Centre Admin, tôi muốn đổi trạng thái điểm danh bị ghi sai và ghi rõ lý do, để số liệu đúng mà vẫn biết trước đó đã ghi gì.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Người dùng có quyền đổi trạng thái điểm danh đã ghi của trẻ sang Present, Absent hoặc Void, bắt buộc ghi lý do (BR-001, BR-002, BR-003). |
| FR-002 | Sau khi đổi, hệ thống tính lại số liệu điểm danh liên quan (BR-004). |

#### Functional Flow - Main (Luồng chính)

1. Centre Admin mở Class attendance của ngày cần sửa, chọn trạng thái mới ở dòng trẻ (FR-001).
2. Hệ thống mở popup yêu cầu lý do; Centre Admin nhập lý do, chọn Save.
3. Hệ thống lưu, báo "Saved", hiện dòng sửa ở trẻ và ghi lịch sử (US-003); số liệu được tính lại (FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Đổi sang Absent: nhập lý do trẻ vắng và ai báo cho Centre (BR-002).
2. Đổi từ Absent sang Present: nhập giờ nhận và người đưa (BR-002).
3. Chọn Void: nhập lý do và xác nhận đã hiểu hệ quả, chọn Void record (BR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có lý do: không lưu (VAL-001).
2. Ngày ngoài giới hạn sửa: không sửa được (VAL-002).
3. Chọn On leave: không được (BR-005).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mọi lần đổi trạng thái điểm danh đã ghi đều bắt buộc lý do; lần đổi được ghi kèm người đổi, ngày giờ, giá trị cũ, giá trị mới. |
| BR-002 | Đổi sang Absent bắt buộc lý do trẻ vắng và ai báo cho Centre (ví dụ "Mother, by phone at 07:40"). Đổi từ Absent sang Present bắt buộc giờ nhận và người đưa (theo BBA-73). |
| BR-003 | Void dùng khi lượt điểm danh không có thật; bắt buộc lý do và xác nhận đã hiểu: Void xoá một lượt phụ huynh có thể đã thấy trong Parents App; ở Singapore, lượt đi học đầu tiên của tháng khởi động việc nộp ECDA; mỗi lần Void ghi tên người làm, ngày giờ. Lượt đã Void không tính vào số liệu. |
| BR-004 | Sau khi sửa, ngày đó được tính lại trong báo cáo điểm danh, bảng tổng hợp hôm nay (BBA-76) và danh sách trẻ chưa có ngày đi học trong tháng. |
| BR-005 | On leave không chọn được khi sửa; nghỉ phép chỉ đến từ đơn xin nghỉ đã duyệt. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Thiếu lý do (hoặc thiếu "Who told the centre" khi Absent, thiếu xác nhận khi Void). | Nút Save / Void record tắt. |
| VAL-002 | Ngày sau hôm nay hoặc cũ hơn giới hạn sửa (OQ-02). | Không có thao tác sửa; rê chuột hiện "This day can no longer be corrected." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Absent — <tên trẻ> (popup) | Prototype: Class attendance › chọn Absent |
| Void this attendance record (popup) | Prototype: Class attendance › chọn Void |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Present / Absent / On leave / Void | Nút chọn ở dòng trẻ | Theo quyền | Trạng thái hiện tại | VAL-002. | Chọn trạng thái mới mở popup lý do; On leave chỉ hiển thị (BR-005). |
| **Absent — <tên trẻ>** | | | | | |
| Reason the child is away | Ô nhập nhiều dòng | Có | Trống | VAL-001. | Ví dụ "Fever since last night, seeing the doctor this morning". |
| Who told the centre | Ô nhập | Có | Trống | VAL-001. | Ví dụ "Mother, by phone at 07:40". |
| Cancel / Save | Nút | — | Save tắt khi thiếu | VAL-001. | Lưu, báo "Saved". |
| **Void this attendance record** | | | | | |
| Reason | Ô nhập nhiều dòng | Có | Trống | VAL-001. | Lý do Void. |
| Xác nhận hệ quả | Ô chọn | Có | Chưa chọn | VAL-001. | Nội dung theo BR-003. |
| Cancel / Void record | Nút | — | Void record tắt khi thiếu | VAL-001. | — |
| Dòng sửa ở trẻ | Text | — | Sau khi sửa | — | Ví dụ "Absent: Fever since last night · centre told by Mother, by phone". |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần sửa lưu: trẻ, ngày điểm danh, trường được sửa, giá trị cũ, giá trị mới, lý do, người báo (khi Absent), người sửa, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan Present, nhận lúc 08:12 nhưng thực tế vắng | Centre Admin chọn Absent, nhập lý do "Fever since last night", người báo "Mother, by phone", chọn Save | hiện "Saved"; Ethan Absent; dòng sửa hiện lý do và người báo; lịch sử có Present → Absent | FR-001; BR-001; BR-002; DATA-001 |
| AC-002 | Centre Admin chọn Absent, để trống Who told the centre | nhìn nút Save | nút tắt | VAL-001 |
| AC-003 | Mia bị đánh vắng nhầm hôm qua | Centre Admin chọn Present, nhập giờ nhận 08:20, người đưa, lý do | Mia Present 08:20 hôm qua; lịch sử có Absent → Present | FR-001; BR-002 |
| AC-004 | Noah có lượt điểm danh không có thật | Centre Admin chọn Void, nhập lý do, đánh dấu xác nhận, chọn Void record | lượt bị Void, không tính vào số liệu; lịch sử ghi người Void, ngày giờ, lý do | FR-001; BR-003 |
| AC-005 | Centre Admin mở Void, chưa đánh dấu xác nhận | nhìn nút Void record | nút tắt | VAL-001; BR-003 |
| AC-006 | Mia là trẻ Singapore chưa có ngày đi học trong tháng | Centre Admin sửa một ngày sang Present | Mia không còn trong danh sách trẻ chưa có ngày đi học trong tháng | FR-002; BR-004 |
| AC-007 | Centre Admin xem các nút trạng thái | chọn On leave | không đổi được; On leave chỉ đến từ đơn xin nghỉ | BR-005 |
| AC-008 | ngày cũ hơn giới hạn sửa | Centre Admin xem dòng trẻ | không có thao tác sửa, rê chuột hiện "This day can no longer be corrected." | VAL-002 |
| AC-009 | Teacher mở Class attendance của ngày hôm qua | xem dòng trẻ | không có thao tác sửa | FR-001 |

#### Dependencies (Phụ thuộc)

Class attendance; nhận trẻ, người đưa (BBA-73); đơn xin nghỉ; báo cáo điểm danh; bảng tổng hợp (BBA-76).

### 6.2 BBA-77: US-002 - Sửa giờ nhận / giờ trả

#### User Story

Là Centre Admin, tôi muốn sửa giờ nhận hoặc giờ trả bị ghi sai và ghi lý do, để giờ đi học của trẻ đúng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-003 | Người dùng có quyền sửa giờ nhận, giờ trả đã ghi, bắt buộc lý do (BR-001, BR-006). |
| FR-004 | Sửa giờ nhận thì hệ thống tính lại dấu đến muộn (BR-007). |

#### Functional Flow - Main (Luồng chính)

1. Centre Admin chọn Correct time ở dòng trẻ; popup hiện giờ nhận, giờ trả hiện tại (FR-003).
2. Centre Admin sửa giờ, nhập lý do, chọn Save; hệ thống lưu và ghi lịch sử (FR-003).
3. Hệ thống tính lại dấu đến muộn (FR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Chỉ sửa giờ trả: giờ nhận giữ nguyên.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Giờ trả trước giờ nhận, hoặc giờ sau hiện tại: không lưu (VAL-003).
2. Không có lý do: không lưu (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Giờ sau khi sửa phải hợp lệ: giờ trả không trước giờ nhận; không sau giờ hiện tại (với hôm nay). |
| BR-007 | Sửa giờ nhận thì dấu đến muộn được tính lại theo giờ chốt của ngày đó (BBA-75). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Giờ trả trước giờ nhận, hoặc giờ sau giờ hiện tại. | Không lưu; hiện "Check the times." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Correct time (popup) | Prototype chưa có; tham khảo cột Arrival / Departure ở Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Correct time | Nút ở dòng trẻ | Theo quyền | — | VAL-002. | Mở popup sửa giờ. |
| Arrival, Departure | Giờ | Theo trạng thái | Giá trị hiện tại | VAL-003. | HH:mm. |
| Reason | Ô nhập | Có | Trống | VAL-001. | — |
| Cancel / Save | Nút | — | Save tắt khi thiếu lý do | VAL-001; VAL-003. | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Lưu theo DATA-001. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-010 | giờ nhận của Noah 09:34 có dấu Late, giờ chốt 09:15 | Centre Admin sửa thành 08:34, lý do "Nhập nhầm giờ" | giờ nhận 08:34; dấu Late bị bỏ; lịch sử có 09:34 → 08:34 | FR-003; FR-004; BR-007 |
| AC-011 | giờ nhận 08:12 | Centre Admin sửa giờ trả thành 07:00 | không lưu, hiện "Check the times." | BR-006; VAL-003 |
| AC-012 | Centre Admin sửa giờ, để trống lý do | nhìn nút Save | nút tắt | FR-003; BR-001; VAL-001 |

#### Dependencies (Phụ thuộc)

US-001; dấu đến muộn (BBA-75).

### 6.3 BBA-77: US-003 - Lịch sử sửa

#### User Story

Là Centre Director, tôi muốn xem mọi lần sửa của một lượt điểm danh cùng giá trị gốc, để đối chiếu khi kiểm tra.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Giá trị gốc của lượt điểm danh luôn được giữ; mỗi lần sửa thêm một dòng lịch sử (BR-008). |
| FR-006 | Người dùng xem lịch sử sửa của một lượt điểm danh ở dòng trẻ (BR-009). |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở Class attendance, xem dòng sửa ở trẻ hoặc mở lịch sử (FR-006).
2. Hệ thống hiển thị mọi lần sửa theo thời gian, mới nhất ở trên (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lượt chưa từng sửa: lịch sử chỉ có giá trị gốc.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người dùng không có quyền xem lịch sử: không thấy thao tác xem lịch sử.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Không ai xoá hoặc sửa được dòng lịch sử; giá trị gốc không bị ghi đè. |
| BR-009 | Mỗi dòng lịch sử hiển thị: ngày giờ sửa, người sửa, giá trị cũ → giá trị mới, lý do, người báo (khi Absent). Ví dụ "22/11/2026 03:58 · Daniel Yeo · Present · in 08:12 · out — → Absent · Fever since last night". |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — dòng sửa ở trẻ | Prototype: Class attendance sau khi đổi trạng thái |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Dòng sửa gần nhất | Text ở dòng trẻ | — | Khi đã sửa | — | BR-009. |
| History | Nút / popup | — | — | — | Mọi lần sửa, mới nhất ở trên (FR-006). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Đọc DATA-001; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-013 | lượt điểm danh của Ethan đã sửa 2 lần | Centre Director mở History | thấy 2 dòng sửa với ngày giờ, người sửa, giá trị cũ → mới, lý do; giá trị gốc vẫn còn | FR-005; FR-006; BR-009 |
| AC-014 | Ethan đổi từ Present sang Absent | Centre Director xem dòng Ethan | dòng hiện "Present · in 08:12 · out — → Absent · Fever since last night" kèm ngày giờ và người sửa | FR-006; BR-009 |
| AC-015 | có dòng lịch sử sửa | HQ Admin tìm cách xoá dòng đó | không có thao tác xoá hay sửa | BR-008 |

#### Dependencies (Phụ thuộc)

US-001, US-002.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Giáo viên có được sửa điểm danh của lớp mình sau khi đã ghi, hay gửi yêu cầu để Centre Admin duyệt? | Centre Director / HQ Ops | Trung bình | |
| OQ-02 | Được sửa điểm danh lùi về tối đa bao nhiêu ngày (ví dụ trong tháng hiện tại và tháng trước)? | Centre Director / HQ Ops | Cao | |
| OQ-03 | Sửa ngày đã gửi báo cáo trợ cấp (ECDA) thì có cần thêm bước gì không? | HQ Ops | Trung bình | |
| OQ-04 | Void có cần người khác duyệt không, hay người có quyền Void trực tiếp (như prototype)? | Centre Director / HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lượt điểm danh | Bản ghi điểm danh của một trẻ trong một ngày: trạng thái, giờ nhận, giờ trả. |
| Void | Huỷ một lượt điểm danh không có thật; lượt bị Void không tính vào số liệu. |
| Giá trị gốc | Giá trị ghi lần đầu, giữ trong lịch sử dù đã sửa. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Trạng thái điểm danh | Present, Absent, On leave (chỉ từ đơn xin nghỉ), Void. | Class attendance; đơn xin nghỉ. |
