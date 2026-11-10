# BBA-85 Payment item – approve / reject (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › Items, discounts & general |
| Tính năng | Payment item – approve / reject |
| Mã ticket | BBA-85 |
| Mã WBS | 3.6.8.02 |
| Mã tài liệu | FRD-BBA-85 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-85: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc duyệt / từ chối mục phí mới hoặc thay đổi trước khi dùng, người gửi và người duyệt khác nhau, thông báo kết quả. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Mục phí mới hoặc thay đổi giá ảnh hưởng tới số tiền phụ huynh phải trả, nên phải được HQ Finance duyệt trước khi dùng. Người duyệt thấy rõ mục phí mới, hoặc giá cũ và giá mới, rồi duyệt hoặc từ chối có lý do.

Mục tiêu đo được: 0 mục phí được dùng trên hoá đơn khi chưa duyệt; mọi quyết định có người duyệt và thời điểm.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Hộp duyệt mục phí trong Finance approvals. Chi tiết yêu cầu: mục mới, hoặc so sánh phiên bản cũ / mới. Duyệt, từ chối có lý do. Thông báo người gửi. Lịch sử. | Tạo, sửa mục phí (BBA-84). Duyệt giảm giá (BBA-86). Thiết lập tuyến duyệt (Administration). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Nhân viên Finance (người gửi) | Quốc gia / pháp nhân. | Gửi yêu cầu, nhận kết quả. |
| HQ Finance (người duyệt) | Quốc gia / pháp nhân. | Duyệt hoặc từ chối. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Hệ thống | Toàn hệ thống. | Đưa yêu cầu vào hộp duyệt, chặn tự duyệt, thông báo, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Fees & payments › Finance approvals | Duyệt mục phí. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Duyệt hoặc từ chối mục phí

#### User Story

Là người duyệt ở HQ Finance, tôi muốn xem mục phí mới hoặc giá thay đổi và duyệt hay từ chối có lý do, để chỉ những khoản phí đã được kiểm tra mới xuất hiện trên hoá đơn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Yêu cầu "Apply for new payment item" xuất hiện trong Finance approvals với loại "Payment item", mã, mô tả, người gửi, ngày gửi, trạng thái Pending approval; sắp xếp mặc định cũ nhất lên đầu. |
| FR-002 | Chi tiết yêu cầu hiện mọi trường của mục phí; với yêu cầu thay đổi, hiện phiên bản đang dùng và phiên bản mới cạnh nhau, trường thay đổi được tô đậm. |
| FR-003 | "Approve" chuyển phiên bản sang Approved, ghi người duyệt và thời điểm; mục phí dùng được từ ngày hiệu lực của phiên bản. |
| FR-004 | "Reject" bắt buộc lý do; phiên bản chuyển Rejected; phiên bản đang dùng (nếu có) vẫn áp dụng. |
| FR-005 | Người gửi nhận thông báo trong app khi yêu cầu được duyệt hoặc bị từ chối, kèm lý do khi bị từ chối. |
| FR-006 | Người gửi không được duyệt yêu cầu của chính mình: không có nút Approve / Reject với yêu cầu đó. |
| FR-007 | Mục phí bị từ chối có thể được sửa và gửi lại; lần gửi lại là yêu cầu mới. |
| FR-008 | Lịch sử yêu cầu: gửi, duyệt, từ chối, gửi lại, kèm người và thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên Finance gửi mục phí (BBA-84); yêu cầu vào hộp duyệt (FR-001).
2. Người duyệt mở chi tiết, so sánh (FR-002), chọn Approve (FR-003).
3. Người gửi nhận thông báo (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người duyệt từ chối có lý do; người gửi sửa và gửi lại (FR-004, FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Từ chối không có lý do: không lưu (VAL-001).
2. Người gửi mở yêu cầu của mình: không có nút duyệt (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mọi duyệt của Finance nằm trong một hộp duyệt; từ chối phải có lý do. |
| BR-002 | Người gửi và người duyệt là hai người khác nhau. |
| BR-003 | Mục phí chỉ dùng được sau khi được duyệt; phiên bản đang dùng giữ nguyên cho đến khi phiên bản mới được duyệt. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Từ chối không có lý do. | Không lưu; hiện "Enter a reason. The requester sees it in the notification." |
| VAL-002 | Người gửi mở yêu cầu của chính mình. | Không có Approve / Reject; hiện "You submitted this request." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Finance approvals — Payment item | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Hộp duyệt | Bảng | Có | Cũ nhất lên đầu | — | FR-001. |
| So sánh phiên bản | Hai cột | Khi là thay đổi | — | — | FR-002. |
| Approve | Nút | Người duyệt | — | VAL-002. | FR-003. |
| Reject, lý do | Nút, ô nhập | Người duyệt | — | VAL-001; VAL-002. | FR-004. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi quyết định lưu: yêu cầu, phiên bản, kết quả, lý do, người duyệt, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | nhân viên A gửi mục UNI-01 | người duyệt B mở Finance approvals | thấy yêu cầu loại Payment item, mã UNI-01, người gửi A, Pending approval | FR-001; BR-001 |
| AC-002 | yêu cầu đổi giá 1.000 → 1.100 | B mở chi tiết | thấy hai phiên bản cạnh nhau, đơn giá được tô đậm | FR-002 |
| AC-003 | B chọn Approve | xem mục phí | phiên bản mới Approved, ghi B và thời điểm; A nhận thông báo đã duyệt | FR-003; FR-005; DATA-001 |
| AC-004 | B chọn Reject không lý do | lưu | không lưu, hiện "Enter a reason. The requester sees it in the notification." | FR-004; VAL-001 |
| AC-005 | B từ chối với lý do | A mở thông báo | thấy kết quả Rejected và lý do; giá 1.000 vẫn đang dùng | FR-004; FR-005; BR-003 |
| AC-006 | A mở yêu cầu của chính mình | xem | không có Approve / Reject, hiện "You submitted this request." | FR-006; VAL-002; BR-002 |
| AC-007 | mục bị từ chối | A sửa và gửi lại | có yêu cầu mới trong hộp duyệt; lịch sử có cả lần từ chối và lần gửi lại | FR-007; FR-008 |

#### Dependencies (Phụ thuộc)

Tạo, sửa mục phí (BBA-84); Finance approvals; thông báo trong app; tuyến duyệt (Administration).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Ai được gửi mục phí (chỉ Finance, hay cả Centre)? | BBA Finance | Trung bình |  |
| OQ-02 | Mục phí có cần duyệt hai cấp (ví dụ theo mức giá) không? | BBA Finance | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Chỉ nhân viên Finance gửi mục phí; duyệt một cấp bởi HQ Finance. | Mục 4 — chờ OQ-01, OQ-02 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Finance approvals | Hộp duyệt chung của Finance cho mọi loại yêu cầu tài chính. |
