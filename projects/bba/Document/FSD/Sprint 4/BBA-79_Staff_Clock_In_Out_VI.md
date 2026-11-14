# BBA-79 Staff clock-in / out (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Staff attendance |
| Tính năng | Staff clock-in / out |
| Mã ticket | BBA-79 |
| Mã WBS | 3.2.5.01 |
| Mã tài liệu | FRD-BBA-79 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-79: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả chấm công vào / ra của nhân viên, đo nhiệt độ khi vào ca, đánh dấu nghỉ trong ngày, màn Staff và số nhân viên có mặt làm cơ sở kiểm tra tỷ lệ giáo viên / trẻ. 4 câu hỏi mở ở mục 7, trong đó OQ-01 và OQ-02 cần chốt phạm vi trước khi phát triển.

## 2. Mục tiêu và bối cảnh

Centre cần biết mỗi ngày nhân viên nào đang có mặt, vào lúc mấy giờ, ra lúc mấy giờ, ai nghỉ. Số nhân viên có mặt là cơ sở để Centre kiểm tra tỷ lệ giáo viên trên số trẻ.

Mục tiêu đo được: màn Staff hiện đúng số nhân viên đang có mặt ở Centre tại mọi thời điểm trong ngày.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Chấm công vào / ra trên ứng dụng điểm danh hoặc SMS web. Nhiệt độ khi vào ca. Đánh dấu nhân viên nghỉ trong ngày. Màn Staff theo Centre và ngày. Sửa giờ có lý do. Số nhân viên có mặt cạnh số trẻ đang ở trường. Xuất báo cáo. | Quản lý phép năm, duyệt đơn nghỉ, xếp ca, đào tạo, giáo viên dạy thay. Quy tắc và cảnh báo tỷ lệ giáo viên / trẻ (chờ OQ-02). Tính lương. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Nhân viên Centre (Teacher, Senior Teacher, Centre Admin…) | Bản thân. | Chấm công vào / ra, ghi nhiệt độ khi vào ca. |
| Centre Director, Centre Admin / School Admin | Centre của mình. | Xem màn Staff; đánh dấu nghỉ; sửa giờ có lý do; xuất báo cáo. |
| HQ Admin, HQ Ops | Mọi Centre / Centre phụ trách. | Xem và xuất báo cáo. |
| Hệ thống | Toàn hệ thống. | Lưu giờ, tính số nhân viên có mặt, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Daily operations › Staff attendance | Chấm công nhân viên, đánh dấu nghỉ, màn Staff. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Chấm công vào / ra của nhân viên

#### User Story

Là Centre Director, tôi muốn thấy trong ngày nhân viên nào đã vào, đã ra, đang nghỉ, và số nhân viên đang có mặt so với số trẻ đang ở trường, để bảo đảm lớp luôn đủ người trông.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Nhân viên chấm công vào trên ứng dụng điểm danh hoặc SMS web: giờ (mặc định hiện tại) và nhiệt độ (bắt buộc). |
| FR-002 | Nhân viên chấm công ra: giờ (mặc định hiện tại). |
| FR-003 | Màn Staff theo Centre và ngày: tên, vai trò, giờ vào, giờ ra, nhiệt độ, trạng thái (On site, Clocked out, Not clocked in, On leave). |
| FR-004 | Centre Director / Centre Admin đánh dấu một nhân viên "On leave" cho một ngày, kèm ghi chú; nhân viên đó không bị tính là "Not clocked in". |
| FR-005 | Đầu màn Staff hiện "Staff on site" (số nhân viên đang có mặt) cạnh "Children still in" (số trẻ đã đến mà chưa về) của Centre. |
| FR-006 | Nhân viên quên chấm công ra: Centre Director / Centre Admin sửa giờ ra, lý do bắt buộc; lịch sử lưu giá trị cũ. |
| FR-007 | Nhiệt độ từ ngưỡng sốt trở lên (theo quốc gia, mặc định 37,5 °C) hiện màu đỏ trên màn Staff. |
| FR-008 | Tìm theo tên nhân viên; lọc theo Centre, ngày; xuất báo cáo chấm công theo khoảng ngày ra Excel. |
| FR-009 | Một nhân viên chỉ ở trạng thái On site tại một Centre trong cùng lúc; muốn chấm công vào Centre khác phải chấm công ra trước. |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên đến Centre, chấm công vào và ghi nhiệt độ (FR-001).
2. Centre Director xem màn Staff, số nhân viên có mặt và số trẻ còn ở trường (FR-003, FR-005).
3. Cuối ngày, nhân viên chấm công ra (FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Nhân viên nghỉ: Centre Director đánh dấu On leave (FR-004).
2. Nhân viên quên chấm công ra: Centre Admin sửa có lý do (FR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không ghi nhiệt độ khi vào ca: không lưu (VAL-001).
2. Giờ ra trước giờ vào: không lưu (VAL-002).
3. Chấm công vào khi đang On site ở Centre khác: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Nhiệt độ của nhân viên được ghi khi chấm công vào. |
| BR-002 | Sửa giờ chấm công phải có lý do và giữ lịch sử. |
| BR-003 | "On leave" là đánh dấu trong ngày, không phải đơn xin nghỉ có duyệt. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chấm công vào không có nhiệt độ. | Không lưu; hiện "Enter your temperature." |
| VAL-002 | Giờ ra trước giờ vào, hoặc giờ sau thời điểm hiện tại. | Không lưu; hiện "Check the time." |
| VAL-003 | Nhân viên đang On site ở Centre khác. | Không lưu; hiện "You are still clocked in at" kèm tên Centre, ". Clock out there first." |
| VAL-004 | Sửa giờ không có lý do. | Không lưu; hiện "Enter a reason." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Staff attendance — theo Centre và ngày | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Clock in | Nút | Có | — | VAL-001; VAL-003. | FR-001. |
| Nhiệt độ | Số, 1 chữ số thập phân | Có khi vào ca | 36,5 | VAL-001. | FR-007. |
| Clock out | Nút | Có | — | VAL-002. | FR-002. |
| Bảng nhân viên | Bảng | Có | Theo tên | — | FR-003. |
| Staff on site, Children still in | Chữ | Có | — | — | FR-005. |
| Mark on leave | Nút | Theo quyền | — | — | FR-004. |
| Sửa giờ, lý do | Giờ, ô nhập | Theo quyền | — | VAL-002; VAL-004. | FR-006. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lượt chấm công lưu: nhân viên, Centre, giờ vào, giờ ra, nhiệt độ, thiết bị, người sửa và lý do khi có sửa. |
| DATA-002 | Mỗi lần đánh dấu On leave lưu: nhân viên, ngày, ghi chú, người đánh dấu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Aisyah đến Centre lúc 07:45 | chấm công vào với 36,4 °C | màn Staff hiện Aisyah On site, giờ vào 07:45, 36,4 °C | FR-001; FR-003; BR-001 |
| AC-002 | Aisyah chấm công vào không nhập nhiệt độ | lưu | không lưu, hiện "Enter your temperature." | VAL-001 |
| AC-003 | 6 nhân viên On site, 20 trẻ còn ở trường | Centre Director mở màn Staff | đầu màn hiện "Staff on site 6 · Children still in 20" | FR-005 |
| AC-004 | Chloe nghỉ ốm hôm nay | Centre Director đánh dấu On leave với ghi chú | Chloe hiện On leave, không bị tính "Not clocked in" | FR-004; BR-003; DATA-002 |
| AC-005 | Kelvin quên chấm công ra hôm qua | Centre Admin sửa giờ ra 18:05 với lý do | giờ ra được lưu; lịch sử ghi giá trị cũ, lý do, người sửa | FR-006; BR-002 |
| AC-006 | Centre Admin sửa giờ không có lý do | lưu | không lưu, hiện "Enter a reason." | VAL-004 |
| AC-007 | nhân viên ghi 37,8 °C khi vào ca | màn Staff hiển thị | nhiệt độ hiện màu đỏ | FR-007 |
| AC-008 | Siti đang On site ở Damansara | Siti chấm công vào ở Tampines | không lưu, hiện "You are still clocked in at Small Wonder Damansara. Clock out there first." | FR-009; VAL-003 |
| AC-009 | giờ vào 07:45 | sửa giờ ra thành 07:00 | không lưu, hiện "Check the time." | VAL-002 |
| AC-010 | Centre Director chọn tháng 10 | chọn xuất | file Excel có mọi lượt chấm công tháng 10 của Centre | FR-008; DATA-001 |
| AC-011 | Aisyah đã chấm công vào lúc 07:45 | Aisyah chấm công ra lúc 17:30 | màn Staff hiện Aisyah Clocked out, giờ ra 17:30 | FR-002 |

#### Dependencies (Phụ thuộc)

Danh sách nhân viên theo Centre (Users & permissions); ứng dụng điểm danh; ngưỡng sốt theo quốc gia; bảng tổng hợp trẻ đang ở trường (BBA-76).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | "Đánh dấu nghỉ" chỉ là đánh dấu trong ngày (như FRD này) hay cần quản lý phép (số ngày phép, đơn xin nghỉ, duyệt)? Quản lý phép nhân viên hiện nằm ngoài Phase 1. | HQ Ops | Cao |  |
| OQ-02 | Tỷ lệ giáo viên / trẻ theo từng level là bao nhiêu; ai nhận cảnh báo khi không đủ; cảnh báo thuộc ticket nào? | HQ Ops | Cao |  |
| OQ-03 | Nhân viên có nhiệt độ từ ngưỡng sốt trở lên: chỉ tô đỏ hay báo Centre Director? | Centre Director / HQ Ops | Trung bình |  |
| OQ-04 | Nhân viên làm ở nhiều Centre trong một ngày có được chấm công ở nhiều Centre không? | HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | "On leave" là đánh dấu trong ngày, không có số ngày phép hay duyệt. | FR-004; BR-003 — chờ OQ-01 |
| AS-02 | FRD này chỉ hiện số nhân viên có mặt và số trẻ còn ở trường; quy tắc tỷ lệ và cảnh báo làm sau. | FR-005 — chờ OQ-02 |
| AS-03 | Nhiệt độ từ ngưỡng sốt chỉ tô đỏ, không gửi thông báo. | FR-007 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Chấm công vào / ra | Ghi giờ nhân viên bắt đầu và kết thúc làm việc ở Centre trong ngày. |
| Tỷ lệ giáo viên / trẻ | Số trẻ tối đa một giáo viên được trông theo quy định cho từng level. |
