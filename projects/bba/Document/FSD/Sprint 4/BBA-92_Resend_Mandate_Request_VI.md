# BBA-92 Resend mandate request to parent (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | Resend mandate request to parent |
| Mã ticket | BBA-92 |
| Mã WBS | 3.6.9.04 |
| Mã tài liệu | FRD-BBA-92 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-92: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc gửi lại đường dẫn eGIRO hoặc mẫu giấy cho phụ huynh qua Parents App / email, đếm số lần nhắc và ngày gửi gần nhất. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Nhiều phụ huynh chưa hoàn tất đăng ký GIRO sau lần gửi đầu. Finance cần gửi lại đường dẫn eGIRO hoặc mẫu giấy, và biết đã nhắc bao nhiêu lần, lần gần nhất khi nào, để quyết định có cần gọi điện cho phụ huynh không.

Mục tiêu đo được: mọi lần gửi lại được đếm và lưu ngày, kênh gửi.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Gửi lại cho một trẻ hoặc nhiều trẻ cùng lúc. Kênh Parents App và email. Đếm số lần nhắc, ngày gửi gần nhất. Lịch sử. | Tạo uỷ quyền (BBA-90). Nhắc tự động theo lịch (OQ-02). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Gửi lại yêu cầu. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Phụ huynh | Con mình. | Nhận yêu cầu, đăng ký GIRO. |
| Hệ thống | Toàn hệ thống. | Gửi, đếm, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| GIRO accounts › Resend request | Gửi lại yêu cầu đăng ký GIRO. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Gửi lại yêu cầu đăng ký GIRO cho phụ huynh

#### User Story

Là nhân viên Finance, tôi muốn gửi lại yêu cầu đăng ký GIRO cho phụ huynh chưa hoàn tất và thấy đã nhắc bao nhiêu lần, để thúc đẩy phụ huynh đăng ký trước ngày thu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Resend request" có ở uỷ quyền trạng thái Pending: gửi lại đường dẫn eGIRO (cách eGIRO) hoặc thông báo kèm mẫu giấy PDF (cách Manual form). |
| FR-002 | Kênh gửi: Parents App và email của phụ huynh chính; phụ huynh chưa có Parents App chỉ nhận email. |
| FR-003 | Mỗi lần gửi tăng "Reminders sent" thêm 1 và cập nhật "Last sent" (ngày giờ); hai cột này hiện ở danh sách GIRO (BBA-89). |
| FR-004 | Chọn nhiều trẻ Pending trong danh sách GIRO và chọn "Resend request" để gửi cùng lúc; kết quả hiện số yêu cầu đã gửi và số bị bỏ qua kèm lý do. |
| FR-005 | Uỷ quyền không ở Pending (Active, Rejected, Terminated, Not set up) không gửi lại được. |
| FR-006 | Lịch sử: mỗi lần gửi lại với ngày giờ, kênh, người gửi. |

#### Functional Flow - Main (Luồng chính)

1. Finance lọc uỷ quyền Pending, chọn một trẻ, chọn Resend request (FR-001).
2. Hệ thống gửi qua Parents App và email (FR-002), tăng số lần nhắc (FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Gửi lại cho nhiều trẻ cùng lúc (FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Uỷ quyền không ở Pending: bị bỏ qua (VAL-001).
2. Phụ huynh không có Parents App lẫn email: bị bỏ qua (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Chỉ gửi lại cho uỷ quyền đang Pending. |
| BR-002 | Mọi lần gửi lại được đếm và lưu. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Uỷ quyền không ở Pending. | Không có nút Resend request; khi gửi nhiều trẻ thì trẻ đó bị bỏ qua với lý do "Mandate is not pending". |
| VAL-002 | Phụ huynh không có Parents App và email. | Không gửi; lý do "No app account or email". |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - GIRO accounts — Resend request | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Resend request | Nút | Theo quyền | Chỉ uỷ quyền Pending | VAL-001; VAL-002. | FR-001; FR-004. |
| Reminders sent | Cột số | — | 1 sau lần gửi đầu | — | FR-003. |
| Last sent | Cột ngày giờ | — | — | — | FR-003. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần gửi lưu: uỷ quyền, kênh, người nhận, người gửi, ngày giờ, kết quả. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | uỷ quyền eGIRO Pending, đã gửi 1 lần | Finance chọn Resend request | phụ huynh nhận lại đường dẫn qua Parents App và email; Reminders sent là 2, Last sent cập nhật | FR-001; FR-002; FR-003 |
| AC-002 | uỷ quyền Manual form Pending | Finance chọn Resend request | phụ huynh nhận thông báo kèm mẫu giấy PDF | FR-001 |
| AC-003 | phụ huynh chưa có Parents App | gửi lại | phụ huynh chỉ nhận email | FR-002 |
| AC-004 | chọn 10 trẻ, 8 Pending, 2 Active | chọn Resend request | 8 yêu cầu được gửi, 2 bị bỏ qua với "Mandate is not pending" | FR-004; FR-005; VAL-001; BR-001 |
| AC-005 | phụ huynh không có Parents App và email | gửi lại | không gửi, lý do "No app account or email" | VAL-002 |
| AC-006 | đã gửi lại 3 lần | Finance mở lịch sử | thấy 3 lần với ngày giờ, kênh, người gửi | FR-006; BR-002; DATA-001 |

#### Dependencies (Phụ thuộc)

Tạo uỷ quyền (BBA-90); danh sách GIRO (BBA-89); Parents App; email.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Có giới hạn số lần gửi lại hoặc khoảng cách tối thiểu giữa hai lần gửi không? | BBA Finance | Thấp |  |
| OQ-02 | Có cần tự động nhắc theo lịch (ví dụ trước ngày thu GIRO) không? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Không giới hạn số lần gửi lại. | FR-003 — chờ OQ-01 |
| AS-02 | Gửi lại do Finance bấm, không tự động. | FR-001 — chờ OQ-02 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Reminders sent | Số lần đã gửi yêu cầu đăng ký GIRO cho phụ huynh, tính cả lần đầu. |
