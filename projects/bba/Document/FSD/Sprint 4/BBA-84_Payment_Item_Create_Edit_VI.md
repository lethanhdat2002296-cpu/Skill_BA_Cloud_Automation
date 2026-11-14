# BBA-84 Payment item – create / edit (unit price, tax rate, criteria, effective period) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › Items, discounts & general |
| Tính năng | Payment item – create / edit (unit price, tax rate, criteria, effective period) |
| Mã ticket | BBA-84 |
| Mã WBS | 3.6.8.01 |
| Mã tài liệu | FRD-BBA-84 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-84: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc tạo và sửa mục phí: mô tả, mã, tiêu chí áp dụng, đơn giá, loại định kỳ / một lần, mặc định cho tiêu chí, thuế suất, thời gian hiệu lực. 3 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Mục phí là từng khoản thu (học phí Full Day N2, phí đăng ký, đồng phục…). Finance tạo mục phí với đơn giá, thuế suất, áp cho nhóm trẻ nào và trong thời gian nào. Mục phí mới hoặc thay đổi phải được duyệt (BBA-85) trước khi dùng.

Mục tiêu đo được: mọi mục phí có mã duy nhất, thời gian hiệu lực và lịch sử giá.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách mục phí. Tạo, sửa mục phí: mô tả, mã, level, chương trình, quốc tịch, nhãn trẻ, đơn giá, loại (định kỳ / một lần), mặc định cho tiêu chí, thuế suất, hiệu lực, ghi chú. Ngừng dùng. Gửi duyệt. Lịch sử. | Duyệt mục phí (BBA-85). Tài khoản kế toán và cách hạch toán. Lịch phí của trẻ (BBA-80). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Nhân viên Finance | Quốc gia / pháp nhân. | Tạo, sửa mục phí và gửi duyệt. |
| HQ Finance (người duyệt) | Quốc gia / pháp nhân. | Duyệt (BBA-85). |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Centre Director, Centre Admin | Centre của mình. | Xem mục phí đang dùng. |
| Hệ thống | Toàn hệ thống. | Kiểm tra mã trùng, mặc định trùng; lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Settings › Payment items | Tạo và sửa mục phí. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Tạo và sửa mục phí

#### User Story

Là nhân viên Finance, tôi muốn tạo và sửa mục phí với đơn giá, thuế suất và nhóm trẻ áp dụng theo thời gian hiệu lực, để hoá đơn lấy đúng khoản phí cho đúng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Danh sách mục phí: mã, mô tả, level, chương trình, quốc tịch, nhãn trẻ, đơn giá, loại, mặc định, thuế suất, hiệu lực từ – đến, trạng thái (Draft, Pending approval, Approved, Rejected, Stopped). Tìm theo mã, mô tả; lọc theo trạng thái, loại, level, chương trình. |
| FR-002 | Tạo mục phí: mô tả (bắt buộc), mã (bắt buộc, duy nhất), level, chương trình, quốc tịch, nhãn trẻ (để trống là áp cho mọi giá trị), đơn giá (bắt buộc), loại Recurring / One-off, "Default for these criteria", thuế suất (chọn từ danh sách thuế suất), hiệu lực từ (bắt buộc), hiệu lực đến, ghi chú. |
| FR-003 | "Default for these criteria" nghĩa là mục phí được tự đưa vào lịch phí của trẻ khớp tiêu chí; trong cùng thời gian, một bộ tiêu chí chỉ có một mục phí mặc định cho cùng loại chương trình. |
| FR-004 | Lưu ở trạng thái Draft; "Submit for approval" chuyển sang Pending approval và gửi vào hộp duyệt của Finance (BBA-85). |
| FR-005 | Sửa mục phí đã Approved tạo một phiên bản mới ở Pending approval; phiên bản đang dùng vẫn áp dụng cho đến khi phiên bản mới được duyệt. |
| FR-006 | Đổi đơn giá phải là phiên bản mới có ngày hiệu lực; giá cũ không bị sửa và vẫn dùng cho thời gian trước đó. |
| FR-007 | "Stop using from" kèm ngày: từ ngày đó mục phí không dùng cho hoá đơn hay lịch phí mới; mục phí đã dùng không bị xoá. |
| FR-008 | Lịch sử mục phí: mọi phiên bản, đơn giá, hiệu lực, người tạo, người duyệt, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Finance chọn New payment item, nhập thông tin (FR-002), lưu Draft.
2. Finance chọn Submit for approval (FR-004).
3. Sau khi được duyệt, mục phí dùng được từ ngày hiệu lực.

#### Functional Flow - Alternative (Luồng thay thế)

1. Đổi đơn giá từ năm sau: tạo phiên bản mới, gửi duyệt (FR-005, FR-006).
2. Ngừng dùng một mục phí (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Mã trùng: không lưu (VAL-001).
2. Hai mục mặc định trùng tiêu chí và thời gian: không lưu (VAL-002).
3. Thiếu trường bắt buộc hoặc đơn giá âm: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mục phí chỉ dùng được sau khi được duyệt. |
| BR-002 | Đổi giá là giá mới có ngày hiệu lực; giá cũ không bao giờ bị sửa. |
| BR-003 | Mục phí đã dùng không bị xoá; chỉ ngừng dùng. |
| BR-004 | Mã mục phí là duy nhất. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Mã đã tồn tại. | Không lưu; hiện "This code is already used." |
| VAL-002 | Đã có mục mặc định khác cho cùng tiêu chí, cùng loại chương trình, trùng thời gian. | Không lưu; hiện "Another default item already covers these criteria in this period." |
| VAL-003 | Thiếu mô tả, mã, đơn giá hoặc hiệu lực từ; đơn giá âm; hiệu lực đến trước hiệu lực từ. | Không lưu; đánh dấu ô lỗi. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Payment items — danh sách và chi tiết | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Mô tả, mã | Ô nhập | Có | — | VAL-001; VAL-003. | — |
| Level, chương trình, quốc tịch, nhãn trẻ | Danh sách chọn | Không | Tất cả | VAL-002. | — |
| Đơn giá | Số tiền | Có | — | VAL-003. | — |
| Loại | Lựa chọn | Có | Recurring | — | Recurring / One-off. |
| Default for these criteria | Ô chọn | Không | Không chọn | VAL-002. | FR-003. |
| Thuế suất | Danh sách chọn | Có | Thuế suất mặc định của pháp nhân | — | — |
| Hiệu lực từ / đến | Ngày | Từ: có | — | VAL-003. | — |
| Submit for approval | Nút | Có | — | — | FR-004. |
| Stop using from | Nút + ngày | Theo quyền | — | — | FR-007. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi phiên bản mục phí lưu mọi trường, trạng thái, người tạo, người gửi duyệt, người duyệt, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | chưa có mục "Uniform" | Finance tạo mục mã UNI-01, đơn giá, One-off, thuế suất, hiệu lực từ 01/01/2027 | mục lưu ở Draft | FR-001; FR-002 |
| AC-002 | mục ở Draft | Finance chọn Submit for approval | mục chuyển Pending approval và có trong hộp duyệt | FR-004 |
| AC-003 | mục Pending approval | tạo hoá đơn | mục không được dùng | BR-001 |
| AC-004 | đã có mã UNI-01 | tạo mục mới mã UNI-01 | không lưu, hiện "This code is already used." | VAL-001; BR-004 |
| AC-005 | đã có mục mặc định Full Day N2 công dân Singapore năm 2027 | tạo mục mặc định thứ hai cùng tiêu chí năm 2027 | không lưu, hiện "Another default item already covers these criteria in this period." | FR-003; VAL-002 |
| AC-006 | mục Approved giá 1.000 | Finance sửa giá thành 1.100 từ 01/01/2027 | phiên bản mới Pending approval; giá 1.000 vẫn dùng cho đến khi bản mới được duyệt và cho thời gian trước 01/01/2027 | FR-005; FR-006; BR-002 |
| AC-007 | mục đã dùng trên hoá đơn | Finance chọn Stop using from 01/02/2027 | từ 01/02/2027 mục không dùng cho hoá đơn mới; mục không bị xoá | FR-007; BR-003 |
| AC-008 | Finance để trống đơn giá | lưu | không lưu, ô đơn giá bị đánh dấu | VAL-003 |
| AC-009 | mục có 2 phiên bản | Finance mở lịch sử | thấy 2 phiên bản với giá, hiệu lực, người tạo, người duyệt | FR-008; DATA-001 |

#### Dependencies (Phụ thuộc)

Duyệt mục phí (BBA-85); danh sách thuế suất (Administration › Legal entities); lịch phí (BBA-80); tạo hoá đơn.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Danh sách "nhãn trẻ" (ví dụ con nhân viên) là gì; ai quản lý? | BBA Finance | Cao |  |
| OQ-02 | Mục phí có cần tài khoản kế toán và cờ "được trừ từ CDA" ở màn này không? | BBA Finance | Trung bình |  |
| OQ-03 | Mục phí áp theo brand / Centre hay toàn quốc gia? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Tiêu chí để trống nghĩa là áp cho mọi giá trị. | FR-002 |
| AS-02 | Sửa mục đã duyệt phải duyệt lại. | FR-005 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Mục phí | Một khoản thu trên hoá đơn, ví dụ học phí, phí đăng ký, đồng phục. |
| Recurring / One-off | Thu hằng tháng / thu một lần. |
| Nhãn trẻ | Nhóm đặc biệt của trẻ dùng để áp phí riêng. |
