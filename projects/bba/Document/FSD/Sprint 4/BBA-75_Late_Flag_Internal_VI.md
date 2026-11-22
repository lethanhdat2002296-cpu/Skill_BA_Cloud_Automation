# Late Flag (Internal Only)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | BBA-75 Late flag (internal only) |
| Mã tài liệu | FRD-3.2.1.03_Late_Flag_Internal |
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
| 0.2 | 22/11/2026 | Business Analysis | Theo format tài liệu đã duyệt: tách 3 User Story (giờ chốt theo Centre; tự đánh dấu Late nội bộ; báo cáo đến muộn). Bỏ phần đón muộn (không thuộc task). Đối chiếu prototype. | |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Centre cần biết trẻ nào đến muộn để báo cáo nội bộ và trao đổi với gia đình khi cần. Trẻ được nhận sau giờ chốt của Centre được hệ thống tự đánh dấu "Late". Dấu này chỉ dùng cho báo cáo của Centre, không bao giờ hiện cho phụ huynh.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Giờ chốt đến muộn theo Centre. Tự đánh dấu Late khi nhận trẻ sau giờ chốt; tính lại khi giờ nhận được sửa. Hiện Late trên bảng điểm danh cho nhân viên. Báo cáo số lần đến muộn của Centre. Ẩn dấu Late với phụ huynh ở mọi nơi. | Đón trẻ muộn (Late pickup) và phí đón muộn. Thông báo cho phụ huynh về việc đến muộn. Hiện dấu Late cho phụ huynh. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User (Teacher, Centre Admin, Centre Director) | Lớp / Centre của mình. | Xem dấu Late và báo cáo đến muộn. |
| HQ Admin | Mọi Centre. | Đặt giờ chốt đến muộn của từng Centre. |
| HQ Ops (Cluster Head, Operations Manager) | Các Centre mình phụ trách. | Xem báo cáo đến muộn. |
| Phụ huynh | — | Không thấy dấu Late ở bất kỳ đâu. |
| System | Mọi Centre. | So giờ nhận với giờ chốt, đánh dấu và tính lại. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Daily Operations › Late arrival** | Giờ chốt đến muộn | Thiết lập giờ chốt đến muộn của từng Centre. | BBA-75: US-001 |
| **Class attendance** | Tự đánh dấu Late nội bộ | Tự gắn Late khi nhận trẻ sau giờ chốt; hiện cho nhân viên; ẩn với phụ huynh. | BBA-75: US-002 |
| **Attendance report** | Báo cáo đến muộn | Số lần đến muộn của từng trẻ theo khoảng ngày; lọc trẻ đến muộn. | BBA-75: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-75: US-001 - Giờ chốt đến muộn

#### User Story

Là HQ Admin, tôi muốn đặt giờ chốt đến muộn cho từng Centre, để hệ thống biết khi nào trẻ bị tính là đến muộn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Người dùng có quyền đặt giờ chốt đến muộn (Late arrival after) của từng Centre (BR-001, BR-002). |

#### Functional Flow - Main (Luồng chính)

1. HQ Admin mở Daily Operations › Late arrival, chọn Centre.
2. HQ Admin nhập Late arrival after, lưu (FR-001).

#### Functional Flow - Alternative (Luồng thay thế)

1. HQ Admin đổi giờ chốt đang có: chỉ áp từ ngày đổi trở đi (BR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Giờ chốt sai định dạng: không lưu (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Giờ chốt là thiết lập theo Centre, mặc định 09:15. Một giờ chốt chung cho mọi trẻ của Centre. |
| BR-002 | Đổi giờ chốt chỉ áp cho lượt nhận từ ngày đổi trở đi; dấu Late của các ngày trước giữ nguyên. Mỗi lần đổi được lưu lịch sử. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Giờ chốt không phải giờ hợp lệ (HH:mm). | Không lưu; hiện "Enter a time such as 09:15." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Late arrival — thiết lập theo Centre | Prototype: Daily operations › Late arrival & pickup |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Per-centre setting · <Centre> | Tiêu đề | — | Centre đang chọn | — | — |
| Late arrival after | Giờ | Có | 09:15 | VAL-001. | Giờ chốt của Centre (FR-001). |
| Save | Nút | Theo quyền | — | VAL-001. | Lưu và ghi lịch sử (BR-002). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần đổi giờ chốt lưu: Centre, giá trị cũ, giá trị mới, ngày áp dụng, người đổi, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Small Wonder Tampines chưa đặt giờ chốt | HQ Admin mở thiết lập | Late arrival after là 09:15 | FR-001; BR-001 |
| AC-002 | HQ Admin đổi giờ chốt từ 09:15 sang 09:00 ngày 01/12/2026 | xem lượt nhận lúc 09:10 ngày 30/11 và ngày 01/12 | 30/11 không Late; 01/12 Late; lịch sử có dòng đổi giờ chốt | BR-002; DATA-001 |
| AC-003 | HQ Admin nhập "9h" | chọn Save | không lưu, hiện "Enter a time such as 09:15." | VAL-001 |

#### Dependencies (Phụ thuộc)

Thiết lập theo Centre.

### 6.2 BBA-75: US-002 - Tự đánh dấu Late nội bộ

#### User Story

Là Centre Director, tôi muốn hệ thống tự đánh dấu trẻ đến sau giờ chốt và chỉ nhân viên thấy dấu này, để theo dõi việc đến muộn mà phụ huynh không thấy.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-002 | Khi trẻ được nhận sau giờ chốt, hệ thống tự gắn dấu Late cho lượt nhận đó (BR-003). |
| FR-003 | Bảng điểm danh hiện "Late (staff only)" ở trẻ đến muộn (BR-004). |
| FR-004 | Khi giờ nhận được sửa, hệ thống tính lại dấu Late theo giờ mới (BR-003). |
| FR-005 | Dấu Late không hiện cho phụ huynh ở bất kỳ đâu (BR-005). |

#### Functional Flow - Main (Luồng chính)

1. Trẻ được nhận lúc 09:34, giờ chốt 09:15; hệ thống gắn Late (FR-002).
2. Bảng điểm danh hiện "Late (staff only)" ở dòng trẻ (FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Giờ nhận được sửa sớm hơn hoặc bằng giờ chốt: dấu Late bị bỏ (FR-004).
2. Giờ nhận được sửa muộn hơn giờ chốt: dấu Late được gắn (FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa được nhận: không có dấu Late.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-003 | Dấu Late do hệ thống tự gắn khi giờ nhận sau giờ chốt; nhận đúng giờ chốt không bị tính muộn. Nhân viên không gắn hay bỏ dấu Late bằng tay. |
| BR-004 | Dấu Late hiện cho nhân viên dưới dạng "Late (staff only)" cạnh tuổi / giờ nhận của trẻ. |
| BR-005 | Dấu Late không xuất hiện trong Parents App, thông báo gửi phụ huynh, hoá đơn, hay bất kỳ tài liệu, báo cáo nào gửi phụ huynh. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Class attendance — dấu Late | Prototype: Daily operations › Class attendance |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Late (staff only) | Nhãn ở dòng trẻ | — | Khi đến muộn | — | FR-003; BR-004. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi lượt nhận lưu: có dấu Late hay không và giờ chốt dùng để tính. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-004 | giờ chốt 09:15 | Noah được nhận lúc 09:34 | dòng Noah hiện "Late (staff only)" | FR-002; FR-003; BR-003; BR-004 |
| AC-005 | giờ chốt 09:15 | Ethan được nhận đúng 09:15 | không có dấu Late | BR-003 |
| AC-006 | Noah có dấu Late hôm nay | mẹ Noah mở Parents App và đọc thông báo nhận trẻ | không có chữ Late ở bất kỳ đâu | FR-005; BR-005 |
| AC-007 | giờ nhận 09:34 bị nhập nhầm | nhân viên sửa thành 08:34 | dấu Late bị bỏ | FR-004 |
| AC-008 | Noah được nhận lúc 09:34 | lượt nhận được lưu | dữ liệu lượt nhận có dấu Late và giờ chốt 09:15 | DATA-002 |

#### Dependencies (Phụ thuộc)

US-001; nhận trẻ (BBA-73); sửa điểm danh có lý do (BBA-77).

### 6.3 BBA-75: US-003 - Báo cáo đến muộn

#### User Story

Là Centre Director hoặc HQ Ops, tôi muốn xem số lần đến muộn của từng trẻ trong một khoảng ngày, để trao đổi với gia đình khi cần.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Báo cáo điểm danh có cột số lần đến muộn của mỗi trẻ trong khoảng ngày đã chọn và bộ lọc Late only (BR-006). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở Attendance report, chọn khoảng ngày (From, To) (FR-006).
2. Người dùng bật Late only; báo cáo chỉ còn trẻ có ít nhất 1 lần đến muộn, kèm số lần (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng xem theo Centre / lớp trong phạm vi được cấp.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có trẻ đến muộn trong khoảng ngày: báo cáo trống.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Số lần đến muộn đếm theo dấu Late đã lưu của từng lượt nhận trong khoảng ngày. Báo cáo chỉ dành cho nhân viên. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Attendance report | Prototype: Daily operations › Attendance report |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| From, To | Chọn ngày | Có | Tháng hiện tại | — | Khoảng ngày của báo cáo. |
| Late only | Bộ lọc | Không | Tắt | — | Chỉ trẻ có dấu Late (FR-006). |
| Late arrivals | Cột | — | 0 | — | Số lần đến muộn trong khoảng ngày (BR-006). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Báo cáo đọc dấu Late của DATA-002; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-009 | Noah đến muộn 4 lần trong tháng 9/2026 | Centre Director xem báo cáo 01/09–30/09/2026, bật Late only | Noah hiện số lần đến muộn là 4 | FR-006; BR-006 |
| AC-010 | Ethan không đến muộn lần nào trong tháng 9/2026 | Centre Director bật Late only | Ethan không có trong báo cáo | FR-006 |

#### Dependencies (Phụ thuộc)

US-002; báo cáo điểm danh.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Trẻ học buổi chiều (Half Day PM) dùng giờ chốt riêng hay không tính đến muộn? | Centre Director / HQ Ops | Cao | |
| OQ-02 | Trẻ đi xe đến muộn vì xe có bị tính Late không? | Centre Director / HQ Ops | Trung bình | |
| OQ-03 | Centre Director có được tự đổi giờ chốt của Centre mình không, hay chỉ HQ Admin? | HQ Ops | Thấp | |
| OQ-04 | Giáo viên có được tự đánh dấu Late theo nhận định (prototype có "Mark late — teacher judgement") hay chỉ hệ thống tự gắn theo giờ chốt? | Centre Director / HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Giờ chốt đến muộn | Giờ mà trẻ được nhận sau giờ đó bị tính là đến muộn. |
| Late (staff only) | Dấu đến muộn chỉ nhân viên thấy. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Giờ chốt | Theo Centre, mặc định 09:15. | Thiết lập theo Centre. |
