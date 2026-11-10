# BBA-91 GIRO mandate status tracking (Not set up/Pending/Rejected/Terminated) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | GIRO mandate status tracking (Not set up/Pending/Rejected/Terminated) |
| Mã ticket | BBA-91 |
| Mã WBS | 3.6.9.03 |
| Mã tài liệu | FRD-BBA-91 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-91: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả vòng đời trạng thái uỷ quyền GIRO (Not set up, Pending, Active, Rejected, Terminated), ngày và mã tham chiếu ngân hàng, loại uỷ quyền không hợp lệ khỏi đợt thu, cảnh báo trẻ chưa có uỷ quyền đang hoạt động. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Uỷ quyền GIRO đi qua nhiều trạng thái: chờ ngân hàng xác nhận, hoạt động, bị từ chối, chấm dứt. Finance cần cập nhật trạng thái theo kết quả của ngân hàng (kèm ngày và mã tham chiếu), chắc chắn đợt thu chỉ gồm uỷ quyền đang hoạt động, và được cảnh báo về trẻ chưa có uỷ quyền đang hoạt động.

Mục tiêu đo được: 0 dòng thu GIRO được tạo cho uỷ quyền không ở trạng thái Active.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Trạng thái: Not set up, Pending, Active, Rejected, Terminated. Chuyển trạng thái có ngày và mã tham chiếu ngân hàng; lý do khi Rejected / Terminated. Loại uỷ quyền không Active khỏi đợt thu. Cảnh báo trẻ chưa có uỷ quyền Active. Lịch sử trạng thái. Thông báo phụ huynh khi bị từ chối. | Nhập hàng loạt kết quả từ file ngân hàng (BBA-94). Tạo lại uỷ quyền (BBA-93). Đợt thu GIRO. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Cập nhật trạng thái, xem cảnh báo. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Phụ huynh | Con mình. | Nhận thông báo khi uỷ quyền bị từ chối. |
| Hệ thống | Toàn hệ thống. | Kiểm tra chuyển trạng thái hợp lệ, loại uỷ quyền khỏi đợt thu, cảnh báo, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| GIRO accounts › chi tiết uỷ quyền | Theo dõi và cập nhật trạng thái uỷ quyền. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Theo dõi trạng thái uỷ quyền GIRO

#### User Story

Là nhân viên Finance, tôi muốn cập nhật trạng thái uỷ quyền theo kết quả ngân hàng và được cảnh báo về trẻ chưa có uỷ quyền đang hoạt động, để đợt thu chỉ gồm tài khoản thu được và tôi kịp nhắc phụ huynh.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Uỷ quyền có một trong các trạng thái: Not set up, Pending (chờ ngân hàng), Active (đang hoạt động), Rejected (ngân hàng từ chối), Terminated (đã chấm dứt). |
| FR-002 | Chuyển trạng thái hợp lệ: Pending → Active hoặc Rejected; Active → Terminated. Mỗi lần chuyển nhập ngày hiệu lực và mã tham chiếu ngân hàng; Rejected và Terminated bắt buộc lý do. |
| FR-003 | Rejected và Terminated là trạng thái cuối; muốn dùng lại phải tạo lại uỷ quyền (BBA-93). |
| FR-004 | Khi tạo đợt thu GIRO, chỉ uỷ quyền Active được đưa vào; hoá đơn của trẻ không có uỷ quyền Active nằm trong danh sách "Not collected by GIRO" kèm lý do (trạng thái uỷ quyền). |
| FR-005 | Cảnh báo "Children without an active mandate": số trẻ đang học có phương thức thanh toán GIRO nhưng uỷ quyền không Active; hiện ở đầu màn GIRO accounts và trong việc cần làm của Finance trước ngày thu. |
| FR-006 | Khi uỷ quyền chuyển Rejected, phụ huynh nhận thông báo trong app kèm lý do và hướng dẫn đăng ký lại. |
| FR-007 | Lịch sử trạng thái: trạng thái cũ, trạng thái mới, ngày hiệu lực, mã tham chiếu, lý do, người cập nhật, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Ngân hàng xác nhận; Finance mở uỷ quyền Pending, chuyển Active với ngày và mã tham chiếu (FR-002).
2. Đợt thu GIRO tiếp theo gồm uỷ quyền này (FR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Ngân hàng từ chối: Finance chuyển Rejected với lý do; phụ huynh nhận thông báo (FR-002, FR-006).
2. Phụ huynh huỷ GIRO: Finance chuyển Terminated với lý do (FR-002).
3. Finance xem cảnh báo trẻ chưa có uỷ quyền Active trước ngày thu (FR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Chuyển trạng thái không hợp lệ (ví dụ Rejected → Active): không lưu (VAL-001).
2. Rejected / Terminated không có lý do: không lưu (VAL-002).
3. Thiếu ngày hiệu lực: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Chỉ uỷ quyền Active được dùng để thu GIRO. |
| BR-002 | Rejected và Terminated không quay lại được; dùng tạo lại uỷ quyền. |
| BR-003 | Mọi lần chuyển trạng thái có ngày, mã tham chiếu và lịch sử. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chuyển trạng thái không nằm trong FR-002. | Không lưu; hiện "This change is not allowed. Recreate the mandate instead." |
| VAL-002 | Rejected hoặc Terminated không có lý do. | Không lưu; hiện "Enter a reason." |
| VAL-003 | Thiếu ngày hiệu lực. | Không lưu; ô ngày bị đánh dấu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Chi tiết uỷ quyền — cập nhật trạng thái | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Trạng thái mới | Danh sách chọn | Có | Chỉ trạng thái hợp lệ | VAL-001. | FR-002. |
| Ngày hiệu lực | Ngày | Có | Hôm nay | VAL-003. | — |
| Mã tham chiếu ngân hàng | Ô nhập | Không | Trống | — | — |
| Lý do | Ô nhập | Khi Rejected / Terminated | Trống | VAL-002. | — |
| Cảnh báo trẻ chưa có uỷ quyền Active | Hộp cảnh báo | Khi có | — | — | FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần chuyển trạng thái lưu: uỷ quyền, trạng thái cũ, mới, ngày hiệu lực, mã tham chiếu, lý do, người cập nhật, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | uỷ quyền Pending | Finance chuyển Active, ngày 05/11, mã tham chiếu | uỷ quyền Active; lịch sử ghi Pending → Active, ngày, mã, người cập nhật | FR-001; FR-002; FR-007 |
| AC-002 | uỷ quyền Active | tạo đợt thu GIRO | uỷ quyền có trong đợt thu | FR-004; BR-001 |
| AC-003 | uỷ quyền Rejected | tạo đợt thu GIRO | hoá đơn của trẻ nằm trong "Not collected by GIRO" với lý do Rejected | FR-004; BR-001 |
| AC-004 | Finance chuyển Rejected không lý do | lưu | không lưu, hiện "Enter a reason." | VAL-002 |
| AC-005 | uỷ quyền Rejected | Finance chọn chuyển Active | không lưu, hiện "This change is not allowed. Recreate the mandate instead." | FR-003; VAL-001; BR-002 |
| AC-006 | uỷ quyền chuyển Rejected với lý do "Signature mismatch" | phụ huynh mở Parents App | nhận thông báo có lý do và hướng dẫn đăng ký lại | FR-006 |
| AC-007 | 12 trẻ đang học trả bằng GIRO chưa có uỷ quyền Active | Finance mở GIRO accounts | đầu màn hiện cảnh báo 12 trẻ chưa có uỷ quyền đang hoạt động | FR-005 |
| AC-008 | chuyển trạng thái không nhập ngày | lưu | không lưu, ô ngày bị đánh dấu | VAL-003; BR-003; DATA-001 |

#### Dependencies (Phụ thuộc)

Tạo uỷ quyền (BBA-90); tạo lại (BBA-93); nhập hàng loạt (BBA-94); đợt thu GIRO; phương thức thanh toán của trẻ; thông báo trong app.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Uỷ quyền Pending quá bao nhiêu ngày thì cần cảnh báo Finance theo dõi với ngân hàng? | BBA Finance | Trung bình |  |
| OQ-02 | Phụ huynh có được tự huỷ GIRO trong Parents App không, hay chỉ qua Centre / Finance? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Thêm trạng thái Active (thiếu trong mô tả ticket nhưng cần cho vòng đời). | FR-001 |
| AS-02 | Phụ huynh không tự huỷ GIRO trong app; Finance chuyển Terminated khi có yêu cầu. | FR-002 — chờ OQ-02 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Đợt thu GIRO | Lần tạo file gửi ngân hàng để trừ tiền các hoá đơn. |
| Mã tham chiếu ngân hàng | Mã ngân hàng cấp khi xác nhận, từ chối hoặc chấm dứt uỷ quyền. |
