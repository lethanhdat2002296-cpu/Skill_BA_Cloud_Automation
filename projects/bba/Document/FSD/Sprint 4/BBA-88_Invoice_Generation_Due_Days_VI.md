# BBA-88 General settings – invoice generation & due days (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › General settings |
| Tính năng | General settings – invoice generation & due days |
| Mã ticket | BBA-88 |
| Mã WBS | 3.6.8.05 |
| Mã tài liệu | FRD-BBA-88 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-88: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả thiết lập ngày tạo hoá đơn trong tháng, kỳ phí được tạo, trạng thái khi tạo và số ngày đến hạn mặc định, kèm lịch xem trước và lịch sử. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Finance cần đặt hoá đơn hằng tháng được tạo vào ngày nào, cho kỳ phí nào (ví dụ tháng sau), tạo ở trạng thái nào (bản nháp để kiểm tra, hay phát hành ngay) và bao nhiêu ngày thì đến hạn thanh toán. Trước khi lưu, Finance thấy lịch ví dụ cho tháng tới.

Mục tiêu đo được: mỗi thay đổi có lịch xem trước và chỉ áp dụng từ kỳ tạo hoá đơn kế tiếp.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Ngày trong tháng tạo hoá đơn. Kỳ phí (tháng hiện tại, tháng sau). Trạng thái khi tạo (Draft, Billed). Số ngày đến hạn mặc định. Lịch xem trước. Lịch sử. | Ngày chuyển bản nháp thành phát hành, ngày nhắc nợ, ngày thu GIRO (Billing settings). Chạy tạo hoá đơn. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance, HQ Admin | Toàn hệ thống (AS-01). | Xem, sửa thiết lập. |
| Người dùng khác | — | Xem thiết lập. |
| Hệ thống | Toàn hệ thống. | Tạo hoá đơn theo thiết lập; tính ngày đến hạn. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Settings › General settings › Invoice generation | Ngày tạo, kỳ phí, trạng thái, số ngày đến hạn. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Thiết lập tạo hoá đơn và ngày đến hạn

#### User Story

Là nhân viên Finance, tôi muốn đặt ngày tạo hoá đơn, kỳ phí, trạng thái khi tạo và số ngày đến hạn, xem trước lịch của tháng tới, để hoá đơn được tạo đúng lịch BBA đang làm.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Generate on day" — ngày trong tháng hệ thống tạo hoá đơn, từ 1 đến 28 (mặc định 24). |
| FR-002 | "For period" — kỳ phí của hoá đơn được tạo: "Next month" (mặc định) hoặc "Current month". |
| FR-003 | "Create as" — trạng thái khi tạo: "Draft" (mặc định, Finance kiểm tra trước khi phát hành) hoặc "Billed" (phát hành ngay). |
| FR-004 | "Default due days" — số ngày từ ngày phát hành đến ngày đến hạn; hoá đơn mới lấy giá trị này làm hạn thanh toán. |
| FR-005 | Màn hình hiện lịch xem trước theo giá trị đang nhập, ví dụ: "January 2027 fees: created 24 Dec 2026 as Draft · due" kèm ngày đến hạn tính được. |
| FR-006 | Thay đổi áp dụng từ kỳ tạo hoá đơn kế tiếp; hoá đơn đã tạo không đổi ngày đến hạn. |
| FR-007 | Lịch sử: thiết lập, giá trị cũ, giá trị mới, người đổi, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Finance mở General settings › Invoice generation (FR-001 đến FR-004).
2. Finance đổi giá trị, xem lịch xem trước (FR-005), chọn Save.

#### Functional Flow - Alternative (Luồng thay thế)

1. Finance huỷ sau khi xem lịch xem trước: không thay đổi.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngày tạo ngoài 1–28: không lưu (VAL-001).
2. Số ngày đến hạn không phải số nguyên từ 0 đến 60: không lưu (VAL-002).
3. Người không có quyền: chỉ xem (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Ngày tạo hoá đơn là thiết lập, không cố định, do HQ Finance hoặc HQ Admin đổi. |
| BR-002 | Ngày tạo chỉ từ 1 đến 28 để tháng nào cũng có ngày đó. |
| BR-003 | Thay đổi không ảnh hưởng hoá đơn đã tạo. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Ngày tạo ngoài 1–28. | Không lưu; hiện "Choose a day from 1 to 28." |
| VAL-002 | Số ngày đến hạn không phải số nguyên từ 0 đến 60. | Không lưu; hiện "Enter a number of days from 0 to 60." |
| VAL-003 | Người dùng không có quyền sửa. | Các ô bị mờ, không có nút Save. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - General settings — Invoice generation | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Generate on day | Số | Có | 24 | VAL-001. | FR-001. |
| For period | Lựa chọn | Có | Next month | — | FR-002. |
| Create as | Lựa chọn | Có | Draft | — | FR-003. |
| Default due days | Số | Có | Theo giá trị hiện tại | VAL-002. | FR-004. |
| Lịch xem trước | Chữ | Có | — | — | FR-005. |
| Save | Nút | Theo quyền | — | VAL-003. | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi thay đổi lưu: thiết lập, giá trị cũ, giá trị mới, người đổi, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Generate on day 24, Next month, Draft | Finance xem màn hình | lịch xem trước ghi "January 2027 fees: created 24 Dec 2026 as Draft · due" kèm ngày đến hạn | FR-001; FR-002; FR-003; FR-005 |
| AC-002 | Default due days đặt mới | hoá đơn tháng sau được phát hành | ngày đến hạn = ngày phát hành cộng số ngày đã đặt | FR-004 |
| AC-003 | Finance nhập ngày tạo 30 | lưu | không lưu, hiện "Choose a day from 1 to 28." | VAL-001; BR-002 |
| AC-004 | Finance nhập số ngày đến hạn -5 | lưu | không lưu, hiện "Enter a number of days from 0 to 60." | VAL-002 |
| AC-005 | hoá đơn tháng 12 đã tạo | Finance đổi số ngày đến hạn | hoá đơn tháng 12 giữ ngày đến hạn cũ; kỳ sau dùng giá trị mới | FR-006; BR-003 |
| AC-006 | Centre Director mở thiết lập | xem | các ô bị mờ, không có Save | VAL-003; BR-001 |
| AC-007 | đã đổi ngày tạo 24 → 20 | Finance mở lịch sử | thấy 24 → 20, người đổi, thời điểm | FR-007; DATA-001 |

#### Dependencies (Phụ thuộc)

Chạy tạo hoá đơn; Billing settings (ngày phát hành, ngày nhắc nợ, ngày thu GIRO).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Ngày đến hạn tính theo "số ngày sau ngày phát hành" hay theo "ngày cố định trong tháng" (ví dụ ngày 5 của tháng thu phí)? | BBA Finance | Cao |  |
| OQ-02 | Thiết lập áp cho toàn hệ thống, theo quốc gia hay theo pháp nhân? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Một bộ thiết lập cho toàn hệ thống. | Mục 4 — chờ OQ-02 |
| AS-02 | Số ngày đến hạn tính từ ngày phát hành, giới hạn 0–60 ngày. | FR-004; VAL-002 — chờ OQ-01 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Draft / Billed | Bản nháp Finance còn kiểm tra / hoá đơn đã phát hành cho phụ huynh. |
| Kỳ phí | Tháng mà hoá đơn thu phí. |
| Ngày đến hạn | Ngày cuối phụ huynh phải thanh toán. |
