# BBA-87 General settings – calculation order toggles (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › General settings |
| Tính năng | General settings – calculation order toggles |
| Mã ticket | BBA-87 |
| Mã WBS | 3.6.8.04 |
| Mã tài liệu | FRD-BBA-87 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-87: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả 3 thiết lập thứ tự tính (GST trước / sau giảm giá; giảm giá trước / sau trợ cấp; credit note có GST theo thuế suất riêng), ngày áp dụng, ví dụ tính trước khi lưu và lịch sử. 3 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Số tiền trên hoá đơn thay đổi theo thứ tự tính: tính GST trước hay sau khi giảm giá, trừ giảm giá trước hay sau khi trừ trợ cấp. Finance cần đặt thứ tự này giống cách BBA đang tính, thấy ví dụ trước khi lưu, và chắc chắn thay đổi không làm sai hoá đơn đã phát hành.

Mục tiêu đo được: mỗi thay đổi có ví dụ tính trước khi lưu và chỉ áp cho hoá đơn tạo từ ngày áp dụng.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Thiết lập "GST after discount" / "GST before discount". Thiết lập "Discount before subsidy" / "Discount after subsidy". Thiết lập "Credit note contains GST with its own rate". Ngày áp dụng. Ví dụ tính trước khi lưu. Lịch sử. | Thuế suất GST (Administration › Legal entities). Cách làm tròn (OQ-03). Tạo hoá đơn. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance, HQ Admin | Toàn hệ thống (AS-01). | Xem, sửa thiết lập. |
| Người dùng khác | — | Xem thiết lập. |
| Hệ thống | Toàn hệ thống. | Tính hoá đơn theo thiết lập đang hiệu lực tại ngày hoá đơn. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Settings › General settings › Calculation order | Thứ tự tính GST, giảm giá, trợ cấp. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Thiết lập thứ tự tính trên hoá đơn

#### User Story

Là nhân viên Finance, tôi muốn đặt thứ tự tính GST, giảm giá và trợ cấp như BBA đang áp dụng, xem ví dụ trước khi lưu, để hoá đơn ra đúng số tiền và không ảnh hưởng hoá đơn đã phát hành.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Thiết lập 1 — GST: "GST after discount" (GST tính trên số tiền đã trừ giảm giá) hoặc "GST before discount" (GST tính trên phí gốc). |
| FR-002 | Thiết lập 2 — Giảm giá và trợ cấp: "Discount before subsidy" (trừ giảm giá trên phí gốc, rồi trừ trợ cấp) hoặc "Discount after subsidy" (trừ trợ cấp trước, giảm giá tính trên phần còn lại). |
| FR-003 | Thiết lập 3 — "Credit note contains GST with its own rate" bật / tắt: bật thì credit note có dòng GST theo thuế suất của credit note; tắt thì credit note không có dòng GST. |
| FR-004 | Khi đổi thiết lập, người dùng chọn ngày áp dụng (mặc định ngày đầu tháng sau); hoá đơn có ngày từ ngày đó dùng thiết lập mới. |
| FR-005 | Trước khi lưu, màn hình hiện một ví dụ tính với cùng một bộ số (phí gốc, giảm giá, trợ cấp, thuế suất) theo thiết lập cũ và thiết lập mới, cạnh nhau, kèm số tiền phải trả của mỗi cách. |
| FR-006 | Hoá đơn đã phát hành không bị tính lại khi thiết lập thay đổi. |
| FR-007 | Lịch sử: thiết lập, giá trị cũ, giá trị mới, ngày áp dụng, người đổi, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Finance mở General settings › Calculation order (FR-001, FR-002, FR-003).
2. Finance đổi thiết lập, chọn ngày áp dụng (FR-004).
3. Finance xem ví dụ tính cũ / mới (FR-005), chọn Save.

#### Functional Flow - Alternative (Luồng thay thế)

1. Finance huỷ sau khi xem ví dụ: không thay đổi.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngày áp dụng trong tháng đã khoá sổ hoặc trước hôm nay: không lưu (VAL-001).
2. Người không có quyền: chỉ xem (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Thiết lập thứ tự tính chỉ áp cho hoá đơn từ ngày áp dụng; hoá đơn đã phát hành không đổi. |
| BR-002 | Chỉ HQ Finance và HQ Admin sửa; mọi người xem được. |
| BR-003 | Mọi thay đổi có lịch sử. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Ngày áp dụng trước hôm nay hoặc trong tháng đã khoá sổ. | Không lưu; hiện "Choose a date from today in an open month." |
| VAL-002 | Người dùng không có quyền sửa. | Các lựa chọn bị mờ, không có nút Save. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - General settings — Calculation order | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| GST after / before discount | Lựa chọn | Có | Giá trị hiện tại | VAL-002. | FR-001. |
| Discount before / after subsidy | Lựa chọn | Có | Giá trị hiện tại | VAL-002. | FR-002. |
| Credit note contains GST | Bật / tắt | Có | Giá trị hiện tại | VAL-002. | FR-003. |
| Ngày áp dụng | Ngày | Có khi đổi | Đầu tháng sau | VAL-001. | FR-004. |
| Ví dụ tính | Bảng hai cột | Khi đổi | — | — | FR-005. |
| Save | Nút | Theo quyền | — | VAL-001; VAL-002. | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi thay đổi lưu: thiết lập, giá trị cũ, giá trị mới, ngày áp dụng, người đổi, thời điểm. Mỗi hoá đơn lưu thiết lập đã dùng khi tính. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | đang "GST after discount" | Finance chọn "GST before discount", ngày áp dụng 01/01/2027 | màn hình hiện ví dụ tính theo cả hai cách với số tiền phải trả của mỗi cách | FR-001; FR-004; FR-005 |
| AC-002 | đã lưu đổi từ 01/01/2027 | tạo hoá đơn tháng 12/2026 và tháng 1/2027 | hoá đơn tháng 12 tính theo thiết lập cũ, tháng 1 theo thiết lập mới | FR-004; BR-001 |
| AC-003 | hoá đơn tháng 11 đã phát hành | đổi thiết lập | hoá đơn tháng 11 không đổi | FR-006; BR-001 |
| AC-004 | Finance đổi "Discount before subsidy" sang "after" | xem ví dụ | hai cột cho thấy số giảm giá và số tiền phải trả khác nhau theo mỗi cách | FR-002; FR-005 |
| AC-005 | bật "Credit note contains GST" | tạo credit note sau ngày áp dụng | credit note có dòng GST theo thuế suất của credit note | FR-003 |
| AC-006 | Finance chọn ngày áp dụng hôm qua | lưu | không lưu, hiện "Choose a date from today in an open month." | VAL-001 |
| AC-007 | Centre Director mở thiết lập | xem | các lựa chọn bị mờ, không có Save | VAL-002; BR-002 |
| AC-008 | đã đổi | Finance mở lịch sử | thấy giá trị cũ, mới, ngày áp dụng, người đổi | FR-007; BR-003; DATA-001 |

#### Dependencies (Phụ thuộc)

Thuế suất GST (Administration › Legal entities); tạo hoá đơn; credit note; khoá sổ tháng; lịch phí (BBA-80).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Thiết lập áp cho toàn hệ thống, theo quốc gia hay theo pháp nhân? | BBA Finance | Cao |  |
| OQ-02 | Giá trị BBA đang dùng hôm nay cho 3 thiết lập là gì (để đặt mặc định)? | BBA Finance | Cao |  |
| OQ-03 | Làm tròn GST và số tiền theo quy tắc nào (từng dòng hay tổng hoá đơn, 2 chữ số)? | BBA Finance | Cao |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Một bộ thiết lập cho toàn hệ thống. | Mục 4 — chờ OQ-01 |
| AS-02 | Mặc định ngày áp dụng là đầu tháng sau. | FR-004 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| GST | Thuế hàng hoá và dịch vụ. |
| Credit note | Phiếu giảm trừ số tiền đã lập hoá đơn. |
| Ngày áp dụng | Ngày thiết lập mới bắt đầu dùng cho hoá đơn. |
