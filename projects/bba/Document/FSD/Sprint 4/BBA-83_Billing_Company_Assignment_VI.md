# BBA-83 Billing company assignment (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › Payment schedule |
| Tính năng | Billing company assignment |
| Mã ticket | BBA-83 |
| Mã WBS | 3.6.7.04 |
| Mã tài liệu | FRD-BBA-83 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-83: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc gán pháp nhân xuất hoá đơn (Bill From) cho Centre và cho từng trẻ, ngày hiệu lực, ảnh hưởng tới hoá đơn, file GIRO và mã PayNow QR. 3 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Mỗi hoá đơn, file thu GIRO và mã PayNow QR phải mang đúng pháp nhân của BBA đứng tên thu tiền (Bill From). Finance cần gán pháp nhân mặc định cho từng Centre và, khi cần, gán riêng cho một trẻ.

Mục tiêu đo được: 100% hoá đơn mới phát hành có pháp nhân đúng theo thiết lập tại ngày phát hành.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Pháp nhân mặc định của Centre. Pháp nhân riêng cho một trẻ, có ngày hiệu lực. Danh sách trẻ và pháp nhân đang áp. Cảnh báo khi trẻ có uỷ quyền GIRO với pháp nhân cũ. Lịch sử. | Tạo và sửa pháp nhân, tài khoản ngân hàng, UEN, GST (Administration › Legal entities). Mẫu hoá đơn. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Gán pháp nhân cho Centre và trẻ. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Centre Director, Centre Admin | Centre của mình. | Xem pháp nhân đang áp. |
| Hệ thống | Toàn hệ thống. | Chọn pháp nhân khi tạo hoá đơn, file GIRO, mã PayNow QR; lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Payment schedule › Billing company | Gán pháp nhân xuất hoá đơn. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Gán pháp nhân xuất hoá đơn cho Centre và trẻ

#### User Story

Là nhân viên Finance, tôi muốn gán pháp nhân xuất hoá đơn cho từng Centre và riêng cho trẻ khi cần, để hoá đơn, file GIRO và mã PayNow QR luôn mang đúng tên, UEN và tài khoản ngân hàng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Mỗi Centre có một pháp nhân mặc định (Bill From), chọn từ danh sách pháp nhân đang hoạt động; đổi pháp nhân của Centre phải có ngày hiệu lực. |
| FR-002 | Một trẻ có thể có pháp nhân riêng khác pháp nhân của Centre, có ngày hiệu lực từ và đến; ghi chú lý do là bắt buộc. |
| FR-003 | Khi tạo hoá đơn, file thu GIRO và mã PayNow QR, hệ thống dùng pháp nhân riêng của trẻ nếu đang hiệu lực, nếu không thì dùng pháp nhân của Centre tại ngày hoá đơn. |
| FR-004 | Danh sách "Billing company": trẻ, Centre, pháp nhân đang áp, nguồn (Centre / riêng cho trẻ), hiệu lực từ – đến; lọc theo Centre, pháp nhân, nguồn. |
| FR-005 | Khi đổi pháp nhân của trẻ hoặc Centre mà trẻ có uỷ quyền GIRO gắn với pháp nhân cũ, hệ thống hiện cảnh báo kèm danh sách trẻ bị ảnh hưởng: "These children have a GIRO authorisation linked to the old company." |
| FR-006 | Hoá đơn đã phát hành giữ tên, địa chỉ và số đăng ký của pháp nhân tại lúc phát hành; đổi pháp nhân sau đó không sửa hoá đơn cũ. |
| FR-007 | Mọi thay đổi lưu lịch sử: pháp nhân cũ, pháp nhân mới, ngày hiệu lực, lý do, người đổi, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Finance mở Billing company, chọn Centre, chọn pháp nhân mới và ngày hiệu lực (FR-001).
2. Hệ thống cảnh báo các trẻ có uỷ quyền GIRO với pháp nhân cũ (FR-005).
3. Finance xác nhận; hoá đơn từ ngày hiệu lực dùng pháp nhân mới (FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Gán pháp nhân riêng cho một trẻ, kèm lý do (FR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có lý do khi gán riêng cho trẻ: không lưu (VAL-001).
2. Ngày hiệu lực trong tháng đã khoá sổ: không lưu (VAL-002).
3. Pháp nhân đã ngừng hoạt động: không có trong danh sách chọn (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mỗi pháp nhân có một tài khoản ngân hàng và một UEN PayNow; file GIRO được tạo riêng cho từng pháp nhân. |
| BR-002 | Hoá đơn đã phát hành giữ thông tin pháp nhân tại lúc phát hành. |
| BR-003 | Pháp nhân riêng của trẻ được ưu tiên hơn pháp nhân của Centre khi đang hiệu lực. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Gán pháp nhân riêng cho trẻ không có lý do. | Không lưu; hiện "Enter a reason." |
| VAL-002 | Ngày hiệu lực trong tháng đã khoá sổ. | Không lưu; hiện "This month is closed." |
| VAL-003 | Pháp nhân đã ngừng hoạt động. | Không có trong danh sách chọn. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Billing company — danh sách và gán | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Pháp nhân (Bill From) | Danh sách chọn | Có | Pháp nhân hiện tại | VAL-003. | FR-001; FR-002. |
| Hiệu lực từ / đến | Ngày | Từ: có | Ngày đầu tháng sau | VAL-002. | — |
| Lý do | Ô nhập | Khi gán riêng cho trẻ | Trống | VAL-001. | — |
| Danh sách Billing company | Bảng | Có | — | — | FR-004. |
| Cảnh báo GIRO | Hộp cảnh báo | Khi có | — | — | FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần gán lưu: Centre hoặc trẻ, pháp nhân cũ, pháp nhân mới, hiệu lực, lý do, người đổi, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Centre A dùng pháp nhân X | Finance đổi sang pháp nhân Y từ 01/01/2027 | hoá đơn tháng 1/2027 của Centre A mang tên, UEN, tài khoản của Y | FR-001; FR-003; BR-001 |
| AC-002 | hoá đơn tháng 12 đã phát hành với pháp nhân X | đổi Centre A sang Y | hoá đơn tháng 12 vẫn mang thông tin X | FR-006; BR-002 |
| AC-003 | trẻ được gán riêng pháp nhân Z từ 01/01/2027 | tạo hoá đơn tháng 1 | hoá đơn của trẻ mang pháp nhân Z, các trẻ khác của Centre mang pháp nhân của Centre | FR-002; FR-003; BR-003 |
| AC-004 | 5 trẻ có uỷ quyền GIRO với pháp nhân X | Finance đổi Centre A sang Y | hiện cảnh báo kèm danh sách 5 trẻ | FR-005 |
| AC-005 | gán riêng cho trẻ không có lý do | lưu | không lưu, hiện "Enter a reason." | VAL-001 |
| AC-006 | tháng 10 đã khoá sổ | ngày hiệu lực 01/10 | không lưu, hiện "This month is closed." | VAL-002 |
| AC-007 | Finance lọc nguồn "riêng cho trẻ" | xem danh sách | chỉ các trẻ có pháp nhân riêng | FR-004 |
| AC-008 | đã đổi pháp nhân | Finance mở lịch sử | thấy pháp nhân cũ, mới, hiệu lực, lý do, người đổi | FR-007; DATA-001 |
| AC-009 | pháp nhân W đã ngừng hoạt động | Finance mở danh sách chọn | không có W | VAL-003 |

#### Dependencies (Phụ thuộc)

Administration › Legal entities (pháp nhân, tài khoản ngân hàng, UEN, GST); uỷ quyền GIRO (BBA-90, BBA-91); tạo hoá đơn; mã PayNow QR; khoá sổ tháng.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Khi đổi pháp nhân, uỷ quyền GIRO với pháp nhân cũ còn dùng để thu được không, hay phụ huynh phải đăng ký lại? | BBA Finance | Cao |  |
| OQ-02 | Trường hợp nào một trẻ có pháp nhân khác Centre (ví dụ hoá đơn gửi công ty)? | BBA Finance | Trung bình |  |
| OQ-03 | Hoá đơn enrichment có dùng pháp nhân riêng không? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Hệ thống chỉ cảnh báo, không tự huỷ uỷ quyền GIRO khi đổi pháp nhân. | FR-005 — chờ OQ-01 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Pháp nhân (Bill From) | Công ty của BBA đứng tên thu tiền trên hoá đơn. |
| UEN | Mã số đăng ký doanh nghiệp, dùng cho PayNow. |
| Uỷ quyền GIRO | Phụ huynh cho phép ngân hàng tự trừ tiền học phí từ tài khoản. |
