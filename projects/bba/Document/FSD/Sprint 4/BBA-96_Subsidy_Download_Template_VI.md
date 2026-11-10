# BBA-96 Subsidy – download template (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | Subsidy – download template |
| Mã ticket | BBA-96 |
| Mã WBS | 3.6.9.08 |
| Mã tài liệu | FRD-BBA-96 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-96: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả mẫu bảng tính chuẩn để nhập trợ cấp hàng loạt: các cột, định dạng, trang hướng dẫn, phiên bản mẫu. 3 câu hỏi mở ở mục 7 cần BBA Finance chốt; BBA chưa gửi file đang dùng.

## 2. Mục tiêu và bối cảnh

Để nhập trợ cấp cho nhiều trẻ cùng lúc (BBA-97), Finance cần một mẫu bảng tính chuẩn: đúng tên cột, đúng định dạng ngày và số tiền, có hướng dẫn, để file tải lên không bị lỗi vì sai mẫu.

Mục tiêu đo được: file điền đúng theo mẫu được hệ thống đọc mà không lỗi định dạng.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Nút tải mẫu ở màn Subsidy. Mẫu Excel gồm trang dữ liệu (dòng tiêu đề cố định) và trang hướng dẫn (ý nghĩa cột, định dạng, danh sách loại SCFA). Phiên bản mẫu. | Nhập file (BBA-97). Danh sách trợ cấp (BBA-95). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Tải mẫu. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Hệ thống | Toàn hệ thống. | Tạo mẫu với danh sách loại SCFA hiện hành. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Settings › Subsidy › Download template | Tải mẫu nhập trợ cấp. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Tải mẫu bảng tính nhập trợ cấp

#### User Story

Là nhân viên Finance, tôi muốn tải mẫu bảng tính chuẩn có hướng dẫn, để điền trợ cấp cho nhiều trẻ và tải lên mà không bị lỗi sai mẫu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Màn Subsidy có nút "Download template" tải file Excel. |
| FR-002 | Trang "Data" có dòng tiêu đề cố định theo thứ tự: Student ID, Child name, Centre, Year, Application ID, SCFA type, Subsidy, Additional subsidy, Financial assistance, Expiry date, Renewal date. |
| FR-003 | Trang "Instructions" giải thích từng cột: bắt buộc hay không, định dạng (ngày dd/mm/yyyy, số tiền là số, 2 chữ số thập phân, không ký hiệu tiền tệ), cột nào dùng để tìm trẻ (Student ID), cột nào chỉ để đọc (Child name, Centre). |
| FR-004 | Trang "SCFA types" liệt kê loại SCFA hiện hành; ô SCFA type của trang Data chỉ chọn được từ danh sách này. |
| FR-005 | Tên file có phiên bản mẫu, ví dụ "subsidy-import-template-v1.xlsx"; khi cột thay đổi thì tăng phiên bản. |

#### Functional Flow - Main (Luồng chính)

1. Finance mở Subsidy, chọn Download template (FR-001).
2. Finance điền trang Data theo trang Instructions (FR-002, FR-003, FR-004).
3. Finance tải file lên ở BBA-97.

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người không có quyền: không có nút tải mẫu (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Tên cột của mẫu là chuẩn duy nhất để nhập; hệ thống đọc cột theo tên, không theo thứ tự. |
| BR-002 | Danh sách loại SCFA trong mẫu luôn là danh sách hiện hành tại lúc tải. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Người dùng không có quyền nhập trợ cấp. | Không có nút Download template. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Subsidy — Download template | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Download template | Nút | Theo quyền | — | VAL-001. | FR-001. |
| Trang Data | Trang Excel | — | Chỉ có dòng tiêu đề | — | FR-002. |
| Trang Instructions | Trang Excel | — | — | — | FR-003. |
| Trang SCFA types | Trang Excel | — | Danh sách hiện hành | — | FR-004. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Hệ thống lưu phiên bản mẫu hiện hành và danh sách cột của từng phiên bản. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Finance ở màn Subsidy | chọn Download template | tải file "subsidy-import-template-v1.xlsx" | FR-001; FR-005; DATA-001 |
| AC-002 | mở file mẫu | xem trang Data | dòng tiêu đề có đủ 11 cột theo đúng tên | FR-002; BR-001 |
| AC-003 | mở trang Instructions | đọc | mỗi cột có ghi bắt buộc / không, định dạng, cột dùng để tìm trẻ | FR-003 |
| AC-004 | danh sách SCFA hiện có LOR và một loại khác | mở trang Data, ô SCFA type | chỉ chọn được 2 loại này | FR-004; BR-002 |
| AC-005 | Centre Director không có quyền nhập trợ cấp | mở màn Subsidy | không có nút Download template | VAL-001 |

#### Dependencies (Phụ thuộc)

Danh sách trợ cấp (BBA-95); nhập trợ cấp (BBA-97); danh sách loại SCFA.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Cột nào dùng để tìm trẻ: Student ID của hệ thống, số giấy tờ của trẻ, hay mã hồ sơ trợ cấp? | BBA Finance | Cao |  |
| OQ-02 | BBA gửi file Finance đang dùng để nhập trợ cấp hôm nay (nếu có), để mẫu giống cách làm hiện tại. | BBA Finance | Cao |  |
| OQ-03 | Có cần tải mẫu kèm sẵn dữ liệu hiện tại của các trẻ đang lọc (để sửa rồi tải lên) không? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Student ID của hệ thống là cột dùng để tìm trẻ. | FR-002; FR-003 — chờ OQ-01 |
| AS-02 | Mẫu tải về chỉ có dòng tiêu đề, không kèm dữ liệu. | FR-002 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Mẫu nhập trợ cấp | File Excel chuẩn có tên cột cố định dùng để nhập trợ cấp cho nhiều trẻ. |
| Student ID | Mã học sinh do hệ thống cấp. |
