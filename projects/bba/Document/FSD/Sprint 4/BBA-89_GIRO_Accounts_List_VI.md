# BBA-89 GIRO accounts – list (Non-CDA / CDA / Refund) & filters (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | GIRO accounts – list (Non-CDA / CDA / Refund) & filters |
| Mã ticket | BBA-89 |
| Mã WBS | 3.6.9.01 |
| Mã tài liệu | FRD-BBA-89 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-89: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả danh sách tài khoản GIRO của từng trẻ theo 3 loại (Non-CDA, CDA, Refund), các cột, che số tài khoản, bộ lọc và xuất file. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Finance cần một danh sách cho thấy mỗi trẻ đã có tài khoản GIRO nào (tài khoản thường Non-CDA, tài khoản CDA, tài khoản nhận hoàn tiền), ngân hàng nào, uỷ quyền đang ở trạng thái gì, để biết trẻ nào chưa thể thu tiền tự động và cần nhắc phụ huynh.

Mục tiêu đo được: Finance lọc được trong một bước toàn bộ trẻ đang học chưa có uỷ quyền GIRO đang hoạt động.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách theo trẻ với 3 loại tài khoản: Non-CDA, CDA, Refund. Cột: ngân hàng, số tài khoản (che), chủ tài khoản, mã uỷ quyền (mandate ID / DDA), cập nhật lần cuối, cách đăng ký, trạng thái. Lọc theo trẻ, năm, trạng thái trẻ, trạng thái uỷ quyền. Xuất file. Mở chi tiết. | Tạo uỷ quyền (BBA-90), theo dõi trạng thái (BBA-91), gửi lại (BBA-92), tạo lại (BBA-93), nhập hàng loạt (BBA-94). Đợt thu GIRO và file ngân hàng. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Xem, lọc, xuất danh sách; xem đầy đủ số tài khoản ở chi tiết. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Centre Admin, Centre Director | Centre của mình. | Xem danh sách với số tài khoản đã che (AS-01). |
| Hệ thống | Toàn hệ thống. | Che số tài khoản, lưu lại các lần xem đầy đủ và xuất file. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Settings › GIRO accounts | Danh sách tài khoản GIRO theo trẻ. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Danh sách tài khoản GIRO của trẻ

#### User Story

Là nhân viên Finance, tôi muốn xem tài khoản GIRO của mọi trẻ theo 3 loại và lọc theo trạng thái uỷ quyền, để biết trẻ nào chưa thu tự động được và cần nhắc phụ huynh.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Danh sách có 3 nhóm (tab): Non-CDA, CDA, Refund; mỗi dòng một trẻ với: tên trẻ, Centre, ngân hàng, số tài khoản (chỉ hiện 4 số cuối), chủ tài khoản, mã uỷ quyền (mandate ID / DDA), cập nhật lần cuối, cách đăng ký (eGIRO / mẫu giấy), trạng thái uỷ quyền. |
| FR-002 | Trẻ chưa có tài khoản ở một loại hiện trong nhóm đó với trạng thái "Not set up". |
| FR-003 | Lọc theo tên trẻ, năm, trạng thái trẻ (đang học, tạm nghỉ, đã thôi học), trạng thái uỷ quyền (Not set up, Pending, Active, Rejected, Terminated); các bộ lọc dùng kết hợp được. |
| FR-004 | Chọn một dòng mở chi tiết tài khoản: đủ thông tin, lịch sử trạng thái, các uỷ quyền cũ; số tài khoản đầy đủ chỉ hiện khi Finance chọn "Show" và lần xem đó được lưu lại. |
| FR-005 | Xuất danh sách theo bộ lọc ra Excel; số tài khoản trong file chỉ có 4 số cuối; lần xuất được lưu lại. |
| FR-006 | Danh sách Refund chỉ để xem: tài khoản nhận hoàn tiền do phụ huynh đặt, Finance không sửa. |

#### Functional Flow - Main (Luồng chính)

1. Finance mở GIRO accounts, tab Non-CDA (FR-001).
2. Finance lọc trẻ đang học, trạng thái Not set up (FR-002, FR-003).
3. Finance xuất danh sách để nhắc phụ huynh (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Finance mở chi tiết một trẻ và chọn Show để đối chiếu với ngân hàng (FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có dòng nào: danh sách trống (VAL-001).
2. Người không có quyền: không có Show (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Số tài khoản chỉ hiện 4 số cuối ngoài màn chi tiết; xem đầy đủ được lưu lại. |
| BR-002 | Mỗi gia đình có tối đa một tài khoản GIRO (Non-CDA) và một tài khoản CDA; CDA chỉ dùng cho khoản phí được trừ từ CDA. |
| BR-003 | Tài khoản nhận hoàn tiền chỉ do phụ huynh đặt hoặc đổi. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có dòng nào. | Hiện "No accounts match these filters." |
| VAL-002 | Người dùng không có quyền xem số tài khoản đầy đủ. | Không có nút Show. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - GIRO accounts — danh sách và chi tiết | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Non-CDA, CDA, Refund | Tab | Có | Non-CDA | — | FR-001. |
| Bộ lọc | Bộ lọc | Không | Năm hiện tại, trẻ đang học | VAL-001. | FR-003. |
| Số tài khoản | Chữ | — | ••••1234 | VAL-002. | Show ở chi tiết (FR-004). |
| Export | Nút | Theo quyền | — | — | FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần xem đầy đủ số tài khoản và mỗi lần xuất file được lưu: người, thời điểm, trẻ / bộ lọc. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | trẻ có tài khoản Non-CDA đang Active | Finance mở tab Non-CDA | dòng của trẻ hiện ngân hàng, ••••1234, chủ tài khoản, mã uỷ quyền, cập nhật lần cuối, cách đăng ký, Active | FR-001; BR-001 |
| AC-002 | trẻ chưa có tài khoản CDA | Finance mở tab CDA | trẻ hiện với trạng thái Not set up | FR-002 |
| AC-003 | Finance lọc trẻ đang học, Not set up, năm 2026 | xem | chỉ trẻ đang học chưa có uỷ quyền trong năm 2026 | FR-003 |
| AC-004 | Finance mở chi tiết và chọn Show | xem | số tài khoản đầy đủ hiện; hệ thống lưu người xem và thời điểm | FR-004; DATA-001 |
| AC-005 | Finance xuất danh sách đã lọc | mở file | có đúng các dòng đang hiện; số tài khoản chỉ có 4 số cuối | FR-005 |
| AC-006 | Finance mở tab Refund | xem một dòng | không có nút sửa | FR-006; BR-003 |
| AC-007 | bộ lọc không có dòng nào | xem | hiện "No accounts match these filters." | VAL-001 |
| AC-008 | Centre Admin mở chi tiết | xem | không có nút Show | VAL-002 |
| AC-009 | một gia đình đã có tài khoản Non-CDA Active | xem tab Non-CDA của các con trong gia đình | các con dùng chung một tài khoản Non-CDA | BR-002 |

#### Dependencies (Phụ thuộc)

Uỷ quyền GIRO (BBA-90 đến BBA-94); tài khoản hoàn tiền (Parents App); hồ sơ trẻ.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Centre Admin / Centre Director có được xem danh sách GIRO không? | BBA Finance | Trung bình |  |
| OQ-02 | Tài khoản Refund là tài khoản ngân hàng hay PayNow (số điện thoại, NRIC, UEN)? | BBA Finance | Cao |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Centre Admin, Centre Director xem được danh sách với số tài khoản đã che. | Mục 4 — chờ OQ-01 |
| AS-02 | Tài khoản dùng theo gia đình: các anh chị em dùng chung tài khoản. | BR-002 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| GIRO | Hình thức ngân hàng tự trừ tiền học phí từ tài khoản của phụ huynh. |
| CDA | Child Development Account — tài khoản phát triển trẻ em (Singapore), chỉ trừ cho khoản phí được phép. |
| Uỷ quyền (mandate) | Phụ huynh cho phép ngân hàng tự trừ tiền; có mã uỷ quyền (mandate ID / DDA). |
| eGIRO | Đăng ký GIRO trực tuyến. |
