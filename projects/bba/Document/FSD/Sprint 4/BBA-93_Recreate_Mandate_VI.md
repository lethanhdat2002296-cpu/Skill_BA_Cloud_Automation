# BBA-93 Recreate mandate (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | Recreate mandate |
| Mã ticket | BBA-93 |
| Mã WBS | 3.6.9.05 |
| Mã tài liệu | FRD-BBA-93 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-93: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc tạo lại uỷ quyền sau khi bị từ chối, chấm dứt hoặc khi phụ huynh đổi ngân hàng, giữ uỷ quyền cũ trong lịch sử và tránh thu hai lần. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Khi uỷ quyền bị ngân hàng từ chối, bị chấm dứt, hoặc phụ huynh muốn đổi sang ngân hàng khác, Finance cần tạo một uỷ quyền mới cho trẻ mà vẫn giữ uỷ quyền cũ để tra cứu. Khi đổi ngân hàng, uỷ quyền cũ vẫn dùng để thu cho đến khi uỷ quyền mới hoạt động, và không bao giờ có hai uỷ quyền cùng thu một hoá đơn.

Mục tiêu đo được: 100% lần tạo lại giữ uỷ quyền cũ trong lịch sử; 0 hoá đơn bị thu hai lần.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| "Recreate mandate" từ uỷ quyền Rejected, Terminated hoặc Active (đổi ngân hàng). Điền sẵn từ uỷ quyền cũ. Uỷ quyền cũ Active được chấm dứt khi uỷ quyền mới Active. Lịch sử liên kết cũ – mới. | Tạo uỷ quyền lần đầu (BBA-90). Cập nhật trạng thái (BBA-91). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Tạo lại uỷ quyền. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Hệ thống | Toàn hệ thống. | Liên kết uỷ quyền cũ – mới, chấm dứt uỷ quyền cũ khi mới Active, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| GIRO accounts › Recreate mandate | Tạo lại uỷ quyền. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Tạo lại uỷ quyền GIRO

#### User Story

Là nhân viên Finance, tôi muốn tạo uỷ quyền mới khi uỷ quyền cũ bị từ chối, chấm dứt hoặc phụ huynh đổi ngân hàng, mà vẫn giữ uỷ quyền cũ và không thu trùng, để việc thu tự động không bị gián đoạn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Recreate mandate" có ở uỷ quyền Rejected, Terminated và Active; màn tạo điền sẵn loại, chủ tài khoản, pháp nhân từ uỷ quyền cũ; người dùng nhập ngân hàng, số tài khoản, cách đăng ký (eGIRO / Manual form) và lý do tạo lại (bắt buộc). |
| FR-002 | Uỷ quyền mới bắt đầu ở Pending và được gửi cho phụ huynh như BBA-90 (đường dẫn eGIRO hoặc mẫu giấy). |
| FR-003 | Tạo lại từ uỷ quyền Active (đổi ngân hàng): uỷ quyền cũ vẫn Active và dùng để thu cho đến khi uỷ quyền mới chuyển Active; lúc đó uỷ quyền cũ tự chuyển Terminated với lý do "Replaced by new mandate". |
| FR-004 | Tại mọi thời điểm, mỗi loại (Non-CDA, CDA) của một gia đình chỉ có một uỷ quyền Active dùng cho đợt thu. |
| FR-005 | Uỷ quyền cũ không bị xoá; chi tiết uỷ quyền mới có liên kết "Replaces" tới uỷ quyền cũ, và ngược lại "Replaced by". |
| FR-006 | Lịch sử ghi: uỷ quyền cũ, uỷ quyền mới, lý do tạo lại, người tạo, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Uỷ quyền bị Rejected; Finance chọn Recreate mandate (FR-001).
2. Finance nhập ngân hàng mới, cách đăng ký, lý do; hệ thống gửi cho phụ huynh (FR-002).
3. Uỷ quyền mới Active, dùng cho đợt thu sau (FR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Phụ huynh đổi ngân hàng: tạo lại từ uỷ quyền Active; uỷ quyền cũ thu đến khi uỷ quyền mới Active rồi tự chấm dứt (FR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không nhập lý do tạo lại: không lưu (VAL-001).
2. Đã có một uỷ quyền tạo lại đang Pending cho cùng loại: không tạo thêm (VAL-002).
3. Uỷ quyền Pending hoặc Not set up: không có Recreate mandate (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Uỷ quyền cũ không bao giờ bị xoá. |
| BR-002 | Mỗi loại của một gia đình chỉ có một uỷ quyền Active tại một thời điểm. |
| BR-003 | Khi đổi ngân hàng, uỷ quyền cũ tiếp tục thu đến khi uỷ quyền mới Active. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Không có lý do tạo lại. | Không lưu; hiện "Enter a reason." |
| VAL-002 | Đã có uỷ quyền tạo lại đang Pending cùng loại. | Không tạo; hiện "A new mandate is already pending. Resend it instead." |
| VAL-003 | Uỷ quyền đang Pending hoặc Not set up. | Không có nút Recreate mandate. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Recreate mandate | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Recreate mandate | Nút | Theo quyền | Rejected, Terminated, Active | VAL-003. | FR-001. |
| Ngân hàng, số tài khoản | Danh sách chọn, ô nhập | Manual: có | Trống | — | — |
| Cách đăng ký | Lựa chọn | Có | eGIRO | — | FR-002. |
| Lý do tạo lại | Ô nhập | Có | Trống | VAL-001. | — |
| Replaces / Replaced by | Liên kết | — | — | — | FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần tạo lại lưu: uỷ quyền cũ, uỷ quyền mới, lý do, người tạo, thời điểm; thời điểm uỷ quyền cũ tự chấm dứt. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | uỷ quyền Rejected | Finance chọn Recreate mandate, nhập ngân hàng mới, eGIRO, lý do | uỷ quyền mới Pending, phụ huynh nhận đường dẫn; uỷ quyền cũ vẫn còn | FR-001; FR-002; BR-001 |
| AC-002 | uỷ quyền Active ngân hàng A, phụ huynh đổi sang ngân hàng B | Finance tạo lại; đợt thu diễn ra khi uỷ quyền mới còn Pending | đợt thu dùng uỷ quyền ngân hàng A | FR-003; BR-003 |
| AC-003 | như AC-002 | uỷ quyền mới chuyển Active | uỷ quyền ngân hàng A tự chuyển Terminated với lý do "Replaced by new mandate"; đợt thu sau dùng ngân hàng B | FR-003; FR-004; BR-002 |
| AC-004 | đã tạo lại | Finance mở chi tiết uỷ quyền mới | thấy liên kết "Replaces" tới uỷ quyền cũ | FR-005; FR-006; DATA-001 |
| AC-005 | không nhập lý do | lưu | không lưu, hiện "Enter a reason." | VAL-001 |
| AC-006 | đã có uỷ quyền tạo lại đang Pending | Finance tạo lại lần nữa | không tạo, hiện "A new mandate is already pending. Resend it instead." | VAL-002 |
| AC-007 | uỷ quyền Pending | Finance mở chi tiết | không có nút Recreate mandate | VAL-003 |

#### Dependencies (Phụ thuộc)

Tạo uỷ quyền (BBA-90); trạng thái uỷ quyền (BBA-91); gửi lại (BBA-92); đợt thu GIRO.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Khi đổi ngân hàng, Finance có cần gửi yêu cầu chấm dứt uỷ quyền cũ cho ngân hàng không, hay chỉ đổi trạng thái trong hệ thống? | BBA Finance | Cao |  |
| OQ-02 | Uỷ quyền mới có được đổi pháp nhân so với uỷ quyền cũ không? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Hệ thống tự chuyển uỷ quyền cũ sang Terminated khi uỷ quyền mới Active; việc báo ngân hàng làm ngoài hệ thống. | FR-003 — chờ OQ-01 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Tạo lại uỷ quyền | Tạo uỷ quyền mới thay cho uỷ quyền đã bị từ chối, chấm dứt, hoặc khi đổi ngân hàng. |
