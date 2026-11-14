# BBA-90 GIRO mandate – set up for a child (eGIRO / manual) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | GIRO mandate – set up for a child (eGIRO / manual) |
| Mã ticket | BBA-90 |
| Mã WBS | 3.6.9.02 |
| Mã tài liệu | FRD-BBA-90 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-90: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc tạo uỷ quyền GIRO cho trẻ: loại, ngân hàng, tài khoản, chủ tài khoản, cách đăng ký (eGIRO / mẫu giấy), pháp nhân; tạo mẫu giấy khi đăng ký bằng giấy. 3 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Để thu học phí tự động, mỗi trẻ cần một uỷ quyền GIRO với ngân hàng, gắn với pháp nhân BBA đứng tên thu tiền. Phụ huynh đăng ký trực tuyến (eGIRO) hoặc điền mẫu giấy. Finance tạo bản ghi uỷ quyền, và với cách đăng ký bằng giấy thì in mẫu để phụ huynh ký.

Mục tiêu đo được: mọi uỷ quyền có đủ loại, ngân hàng, tài khoản, chủ tài khoản, cách đăng ký và pháp nhân; mẫu giấy được điền sẵn thông tin.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Tạo bản ghi uỷ quyền: loại (Non-CDA, CDA), ngân hàng, số tài khoản, chủ tài khoản, cách đăng ký (eGIRO, Manual form), pháp nhân. Gửi đường dẫn eGIRO cho phụ huynh. Tạo mẫu giấy để in. Trạng thái ban đầu. | Theo dõi trạng thái (BBA-91). Gửi lại (BBA-92). Tạo lại (BBA-93). Tài khoản hoàn tiền. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Tạo uỷ quyền, gửi eGIRO, in mẫu giấy. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Phụ huynh | Con mình. | Đăng ký eGIRO hoặc ký mẫu giấy. |
| Hệ thống | Toàn hệ thống. | Kiểm tra trùng, điền mẫu giấy, gửi đường dẫn, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| GIRO accounts › Set up mandate | Tạo uỷ quyền GIRO cho trẻ. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Tạo uỷ quyền GIRO cho trẻ

#### User Story

Là nhân viên Finance, tôi muốn tạo uỷ quyền GIRO cho trẻ theo cách phụ huynh chọn (trực tuyến hoặc giấy), để sớm thu học phí tự động.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Set up mandate" ở dòng trẻ Not set up: chọn loại (Non-CDA hoặc CDA), ngân hàng (danh sách ngân hàng), số tài khoản, chủ tài khoản, cách đăng ký (eGIRO hoặc Manual form), pháp nhân (mặc định pháp nhân xuất hoá đơn của trẻ). |
| FR-002 | Cách eGIRO: hệ thống gửi đường dẫn đăng ký cho phụ huynh qua Parents App và email; uỷ quyền ở trạng thái Pending, số lần gửi là 1. |
| FR-003 | Cách Manual form: hệ thống tạo mẫu giấy theo ngân hàng, điền sẵn tên trẻ, chủ tài khoản, số tài khoản, pháp nhân; Finance tải PDF để in cho phụ huynh ký; uỷ quyền ở trạng thái Pending. |
| FR-004 | Với cách eGIRO, ngân hàng và số tài khoản có thể để trống, hệ thống điền khi phụ huynh đăng ký xong. |
| FR-005 | Một gia đình chỉ có một uỷ quyền Non-CDA và một uỷ quyền CDA đang Pending hoặc Active; tạo thêm thì hệ thống chặn. |
| FR-006 | Sau khi tạo, danh sách GIRO (BBA-89) hiện trạng thái Pending, cách đăng ký, ngày cập nhật. |
| FR-007 | Lịch sử: người tạo, thời điểm, mọi giá trị đã nhập. |

#### Functional Flow - Main (Luồng chính)

1. Finance chọn trẻ Not set up, chọn Set up mandate (FR-001).
2. Finance chọn cách eGIRO; hệ thống gửi đường dẫn cho phụ huynh (FR-002).
3. Uỷ quyền ở Pending chờ ngân hàng xác nhận (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Phụ huynh chọn mẫu giấy: Finance nhập thông tin, tải PDF in cho phụ huynh ký (FR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Gia đình đã có uỷ quyền cùng loại đang Pending / Active: không tạo (VAL-001).
2. Manual form thiếu ngân hàng, số tài khoản hoặc chủ tài khoản: không tạo (VAL-002).
3. Số tài khoản sai định dạng: không tạo (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mỗi gia đình có tối đa một uỷ quyền GIRO (Non-CDA) và một uỷ quyền CDA đang dùng. |
| BR-002 | Uỷ quyền gắn với một pháp nhân; file thu GIRO được tạo riêng cho từng pháp nhân. |
| BR-003 | Uỷ quyền mới luôn bắt đầu ở Pending; chỉ chuyển Active khi ngân hàng xác nhận (BBA-91). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Gia đình đã có uỷ quyền cùng loại đang Pending hoặc Active. | Không tạo; hiện "This family already has a Non-CDA mandate. Recreate it instead." (theo loại). |
| VAL-002 | Manual form thiếu ngân hàng, số tài khoản hoặc chủ tài khoản. | Không tạo; đánh dấu ô còn thiếu. |
| VAL-003 | Số tài khoản không đúng định dạng của ngân hàng đã chọn. | Không tạo; hiện "Check the account number." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Set up mandate | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Loại | Lựa chọn | Có | Non-CDA | VAL-001. | — |
| Ngân hàng | Danh sách chọn | Manual: có | — | VAL-002. | — |
| Số tài khoản | Ô nhập | Manual: có | — | VAL-002; VAL-003. | — |
| Chủ tài khoản | Ô nhập | Manual: có | Tên phụ huynh chính | VAL-002. | — |
| Cách đăng ký | Lựa chọn | Có | eGIRO | — | FR-002; FR-003. |
| Pháp nhân | Danh sách chọn | Có | Pháp nhân xuất hoá đơn của trẻ | — | — |
| Download form | Nút | Khi Manual form | — | — | FR-003. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi uỷ quyền lưu: gia đình, trẻ, loại, ngân hàng, số tài khoản, chủ tài khoản, cách đăng ký, pháp nhân, trạng thái, người tạo, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | trẻ Not set up | Finance tạo uỷ quyền Non-CDA cách eGIRO | phụ huynh nhận đường dẫn trong Parents App và email; uỷ quyền Pending, số lần gửi 1 | FR-001; FR-002; BR-003 |
| AC-002 | phụ huynh chọn mẫu giấy | Finance nhập ngân hàng, số tài khoản, chủ tài khoản, chọn Manual form | uỷ quyền Pending; tải được PDF đã điền sẵn tên trẻ, chủ tài khoản, số tài khoản, pháp nhân | FR-003 |
| AC-003 | gia đình đã có uỷ quyền Non-CDA Active | Finance tạo Non-CDA cho em của trẻ | không tạo, hiện "This family already has a Non-CDA mandate. Recreate it instead." | FR-005; VAL-001; BR-001 |
| AC-004 | Manual form thiếu số tài khoản | lưu | không tạo, ô số tài khoản bị đánh dấu | VAL-002 |
| AC-005 | số tài khoản sai định dạng | lưu | không tạo, hiện "Check the account number." | VAL-003 |
| AC-006 | cách eGIRO, để trống ngân hàng | lưu | uỷ quyền được tạo ở Pending; ngân hàng điền khi phụ huynh đăng ký xong | FR-004 |
| AC-007 | trẻ có pháp nhân xuất hoá đơn X | Finance mở Set up mandate | pháp nhân mặc định là X | FR-001; BR-002 |
| AC-008 | uỷ quyền vừa tạo | Finance mở danh sách GIRO và lịch sử | dòng trẻ hiện Pending, cách đăng ký; lịch sử ghi người tạo, thời điểm | FR-006; FR-007; DATA-001 |

#### Dependencies (Phụ thuộc)

Danh sách GIRO (BBA-89); pháp nhân xuất hoá đơn (BBA-83); Parents App và email; mẫu đơn GIRO của ngân hàng.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Mẫu giấy GIRO dùng mẫu của ngân hàng nào; mỗi ngân hàng một mẫu hay một mẫu chung? | BBA Finance | Cao |  |
| OQ-02 | Centre Admin có được tạo uỷ quyền (khi phụ huynh nộp mẫu giấy ở Centre) không? | BBA Finance | Trung bình |  |
| OQ-03 | Đường dẫn eGIRO do ngân hàng cung cấp hay do hệ thống tạo? Có hết hạn không? | BBA Finance | Cao |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Uỷ quyền tính theo gia đình; các anh chị em dùng chung. | FR-005; BR-001 |
| AS-02 | Chỉ Finance tạo uỷ quyền. | Mục 4 — chờ OQ-02 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Uỷ quyền GIRO (mandate) | Phụ huynh cho phép ngân hàng tự trừ tiền học phí từ tài khoản. |
| eGIRO / Manual form | Đăng ký trực tuyến / bằng mẫu giấy có chữ ký. |
| Pháp nhân | Công ty của BBA đứng tên thu tiền. |
