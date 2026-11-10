# BBA-94 Import GIRO mandates (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | Import GIRO mandates |
| Mã ticket | BBA-94 |
| Mã WBS | 3.6.9.06 |
| Mã tài liệu | FRD-BBA-94 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-94: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc nhập hàng loạt thông tin và trạng thái uỷ quyền GIRO từ file xác nhận của ngân hàng hoặc bảng tính: kiểm tra từng dòng, xem trước, áp dụng, báo lỗi, chặn nhập trùng. 3 câu hỏi mở ở mục 7, trong đó OQ-01 cần mẫu file của ngân hàng.

## 2. Mục tiêu và bối cảnh

Hằng tháng ngân hàng gửi file xác nhận kết quả đăng ký GIRO (đã duyệt, từ chối, chấm dứt). Khi chuyển dữ liệu từ hệ thống cũ, Finance cũng cần đưa uỷ quyền hiện có vào. Finance tải file lên, hệ thống kiểm tra từng dòng, cho xem trước thay đổi, rồi áp dụng các dòng hợp lệ.

Mục tiêu đo được: mỗi lần nhập có báo cáo số dòng đã áp dụng và số dòng lỗi kèm lý do bằng lời dễ hiểu; tải lại cùng file không tạo thay đổi trùng.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Tải file (file ngân hàng hoặc bảng tính theo mẫu). Kiểm tra từng dòng. Xem trước thay đổi. Áp dụng dòng hợp lệ, báo dòng lỗi. Chặn nhập trùng. Nhật ký nhập. | Gửi file thu GIRO cho ngân hàng và nhập kết quả thu. Tạo uỷ quyền từng trẻ (BBA-90). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Tải file, xem trước, áp dụng. |
| HQ Admin | Mọi Centre. | Mọi quyền; nhập khi chuyển dữ liệu. |
| Hệ thống | Toàn hệ thống. | Đọc file, kiểm tra, áp dụng, lưu nhật ký. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| GIRO accounts › Import | Nhập uỷ quyền GIRO hàng loạt. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Nhập uỷ quyền GIRO hàng loạt

#### User Story

Là nhân viên Finance, tôi muốn tải file xác nhận của ngân hàng lên để cập nhật trạng thái uỷ quyền của nhiều trẻ cùng lúc, xem trước và biết rõ dòng nào lỗi, để không phải cập nhật từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Import" cho chọn nguồn: file xác nhận của ngân hàng (theo định dạng của ngân hàng) hoặc bảng tính theo mẫu của hệ thống; tải được mẫu bảng tính. |
| FR-002 | Mỗi dòng được khớp với uỷ quyền theo mã uỷ quyền (mandate ID / DDA); dòng không có mã thì khớp theo trẻ, loại và số tài khoản. |
| FR-003 | Hệ thống kiểm tra từng dòng: có khớp uỷ quyền / trẻ, trạng thái hợp lệ, chuyển trạng thái được phép (như BBA-91), ngày hợp lệ, số tài khoản đúng định dạng. |
| FR-004 | Màn xem trước: số dòng hợp lệ, số dòng lỗi; mỗi dòng hợp lệ hiện trẻ, loại, giá trị cũ → giá trị mới; mỗi dòng lỗi hiện số dòng trong file và lý do bằng lời dễ hiểu (ví dụ "Row 12: no child found with this mandate ID."). |
| FR-005 | "Apply" áp dụng mọi dòng hợp lệ; dòng lỗi không được áp dụng; tải được danh sách dòng lỗi ra Excel để sửa và nhập lại. |
| FR-006 | File đã nhập thành công không nhập lại được; nhập lại một dòng đã áp dụng (cùng uỷ quyền, cùng trạng thái, cùng ngày) không tạo thay đổi mới. |
| FR-007 | Với file lớn, việc nhập chạy nền và hiện tiến độ; Finance nhận thông báo trong app khi xong. |
| FR-008 | Nhật ký nhập: tên file, nguồn, người nhập, thời điểm, số dòng đã áp dụng, số dòng lỗi kèm lý do. |

#### Functional Flow - Main (Luồng chính)

1. Finance chọn Import, chọn file xác nhận của ngân hàng (FR-001).
2. Hệ thống kiểm tra, hiện xem trước (FR-002, FR-003, FR-004).
3. Finance chọn Apply; hệ thống áp dụng dòng hợp lệ, lưu nhật ký (FR-005, FR-008).

#### Functional Flow - Alternative (Luồng thay thế)

1. Chuyển dữ liệu: HQ Admin nhập bảng tính theo mẫu (FR-001).
2. Tải danh sách dòng lỗi, sửa, nhập lại (FR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. File sai định dạng hoặc thiếu cột: không đọc được (VAL-001).
2. File đã nhập trước đó: không nhập lại (VAL-002).
3. Không có dòng hợp lệ nào: không có Apply (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Dòng hợp lệ được áp dụng, dòng lỗi bị loại và báo lý do (AS-01). |
| BR-002 | Nhập lại cùng dữ liệu không tạo thay đổi trùng. |
| BR-003 | Chuyển trạng thái qua file tuân theo cùng quy tắc như cập nhật tay (BBA-91). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | File không đúng định dạng, thiếu cột bắt buộc. | Không đọc; hiện "This file does not match the template. Missing column:" kèm tên cột. |
| VAL-002 | File đã được nhập thành công trước đó. | Không nhập; hiện "This file was already imported on" kèm ngày và người nhập. |
| VAL-003 | Không có dòng hợp lệ. | Nút Apply bị mờ; chỉ tải được danh sách dòng lỗi. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Import mandates — tải file và xem trước | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Nguồn | Lựa chọn | Có | File ngân hàng | — | FR-001. |
| Chọn file | Tệp | Có | — | VAL-001; VAL-002. | — |
| Download template | Nút | — | — | — | FR-001. |
| Xem trước | Bảng | Có | — | — | FR-004. |
| Apply | Nút | Có | — | VAL-003. | FR-005. |
| Download errors | Nút | Khi có lỗi | — | — | FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần nhập lưu: tên file, mã nhận diện file, nguồn, người nhập, thời điểm, số dòng áp dụng, số dòng lỗi và lý do; mỗi uỷ quyền được đổi có lịch sử ghi nguồn là lần nhập này. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | file ngân hàng có 50 dòng, 47 khớp hợp lệ, 3 dòng mã uỷ quyền không tồn tại | Finance tải file | xem trước "47 valid, 3 errors"; mỗi dòng lỗi có số dòng và lý do dễ hiểu | FR-001; FR-002; FR-003; FR-004 |
| AC-002 | xem trước như AC-001 | Finance chọn Apply | 47 uỷ quyền được cập nhật; 3 dòng không áp dụng; tải được danh sách dòng lỗi | FR-005; BR-001 |
| AC-003 | file đã nhập hôm qua | Finance tải lại cùng file | không nhập, hiện "This file was already imported on" kèm ngày và người nhập | FR-006; VAL-002; BR-002 |
| AC-004 | một dòng chuyển Rejected → Active | kiểm tra | dòng đó là lỗi "This change is not allowed" | FR-003; BR-003 |
| AC-005 | file thiếu cột mã uỷ quyền | tải lên | hiện "This file does not match the template. Missing column: Mandate ID" | VAL-001 |
| AC-006 | mọi dòng đều lỗi | xem trước | nút Apply bị mờ | VAL-003 |
| AC-007 | file 3.000 dòng | Finance chọn Apply | việc nhập chạy nền, hiện tiến độ; Finance nhận thông báo khi xong | FR-007 |
| AC-008 | đã nhập xong | Finance mở nhật ký nhập | thấy tên file, người nhập, thời điểm, số dòng áp dụng, số dòng lỗi | FR-008; DATA-001 |

#### Dependencies (Phụ thuộc)

Trạng thái uỷ quyền (BBA-91); danh sách GIRO (BBA-89); định dạng file của từng ngân hàng; chuyển dữ liệu từ hệ thống cũ.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | BBA gửi mẫu file xác nhận của từng ngân hàng đang dùng (định dạng, cột, mã trạng thái). | BBA Finance | Cao |  |
| OQ-02 | Áp dụng các dòng hợp lệ và bỏ dòng lỗi, hay phải đúng toàn bộ file mới áp dụng? | BBA Finance | Cao |  |
| OQ-03 | Bảng tính dùng khi chuyển dữ liệu gồm những cột nào? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Áp dụng các dòng hợp lệ, bỏ dòng lỗi và báo lý do. | FR-005; BR-001 — chờ OQ-02 |
| AS-02 | File được nhận diện theo nội dung để chặn nhập trùng. | FR-006 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| File xác nhận của ngân hàng | File ngân hàng gửi về cho biết uỷ quyền nào đã duyệt, bị từ chối hoặc chấm dứt. |
| Nhật ký nhập | Bản ghi mỗi lần tải file: ai tải, khi nào, bao nhiêu dòng áp dụng, bao nhiêu dòng lỗi. |
