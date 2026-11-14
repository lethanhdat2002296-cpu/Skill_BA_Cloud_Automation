# BBA-97 Subsidy – upload file (bulk import) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | Subsidy – upload file (bulk import) |
| Mã ticket | BBA-97 |
| Mã WBS | 3.6.9.09 |
| Mã tài liệu | FRD-BBA-97 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-97: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc tải file trợ cấp cho nhiều trẻ: đọc cột theo tên, kiểm tra từng dòng, xem trước, áp dụng, báo lỗi bằng lời dễ hiểu, chạy nền với tiến độ, không nhân đôi khi tải lại, và nhật ký nhập phục vụ báo cáo Import Subsidy. 3 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Đầu năm hoặc khi có kết quả trợ cấp mới, Finance cần cập nhật trợ cấp cho nhiều trẻ cùng lúc. Finance điền mẫu (BBA-96), tải lên, xem trước thay đổi của từng trẻ, rồi áp dụng. Mỗi lần nhập được ghi nhật ký để Finance kiểm tra lại lần nhập đã thay đổi những gì (báo cáo Import Subsidy).

Mục tiêu đo được: mỗi lần nhập có kết quả số dòng đã áp dụng và số dòng bị loại kèm lý do; tải lại cùng file không tạo thay đổi trùng.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Tải file theo mẫu. Đọc cột theo tên. Kiểm tra từng dòng. Xem trước giá trị cũ → mới. Áp dụng dòng hợp lệ, loại dòng lỗi kèm lý do. Chạy nền có tiến độ. Không nhân đôi khi tải lại. Nhật ký nhập. | Mẫu (BBA-96). Màn báo cáo Import Subsidy (ticket báo cáo, Sprint 8) — FRD này chỉ lưu dữ liệu cho báo cáo. Đối chiếu báo cáo trợ cấp hằng tháng của cơ quan quản lý. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Tải file, xem trước, áp dụng; chỉ trẻ trong phạm vi của mình. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Hệ thống | Toàn hệ thống. | Đọc, kiểm tra, áp dụng, lưu nhật ký và lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Settings › Subsidy › Upload file | Nhập trợ cấp hàng loạt. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Nhập trợ cấp hàng loạt từ file

#### User Story

Là nhân viên Finance, tôi muốn tải file trợ cấp của nhiều trẻ, xem trước thay đổi và biết rõ dòng nào bị loại vì sao, để cập nhật trợ cấp nhanh mà không sai và luôn kiểm tra lại được.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Upload file" nhận file Excel hoặc CSV; hệ thống đọc cột theo tên trong dòng tiêu đề của mẫu (thứ tự cột không quan trọng). |
| FR-002 | Mỗi dòng được kiểm tra: tìm thấy trẻ theo Student ID và trẻ thuộc phạm vi người tải; năm hợp lệ; loại SCFA có trong danh sách; subsidy, additional subsidy, FA là số từ 0; ngày đúng định dạng dd/mm/yyyy; ngày gia hạn không sau ngày hết hạn; cùng một trẻ và năm không xuất hiện hai lần trong file. |
| FR-003 | Màn xem trước: số dòng sẽ áp dụng, số dòng không đổi, số dòng lỗi. Dòng sẽ áp dụng hiện trẻ, năm, từng trường giá trị cũ → mới. Dòng lỗi hiện số dòng trong file và lý do bằng lời dễ hiểu, ví dụ "Row 8: Subsidy must be a number." |
| FR-004 | "Apply" áp dụng các dòng hợp lệ có thay đổi; dòng không đổi được bỏ qua; dòng lỗi không áp dụng. Tải được danh sách dòng lỗi ra Excel để sửa và tải lại. |
| FR-005 | File lớn được xử lý nền: màn hình hiện tiến độ (số dòng đã xử lý / tổng); Finance nhận thông báo trong app khi xong; nếu dừng giữa chừng, các dòng đã áp dụng được giữ và báo rõ số dòng chưa xử lý. |
| FR-006 | Tải lại cùng file, hoặc một file có các dòng đã áp dụng trước đó, không tạo thay đổi mới cho các dòng đó (hiện là "No change"). |
| FR-007 | Giá trị mới có hiệu lực cho hoá đơn tạo sau khi áp dụng; hoá đơn đã phát hành không đổi. |
| FR-008 | Nhật ký nhập lưu: tên file, người tải, thời điểm, số dòng đã áp dụng, giá trị trợ cấp đã đặt cho từng trẻ (subsidy, additional subsidy, FA, ngày hết hạn, ngày gia hạn), các dòng bị loại kèm lý do. |
| FR-009 | Mỗi trẻ được thay đổi có dòng lịch sử ở danh sách trợ cấp (BBA-95) với nguồn "nhập file" và tên file. |

#### Functional Flow - Main (Luồng chính)

1. Finance chọn Upload file, chọn file đã điền theo mẫu (FR-001).
2. Hệ thống kiểm tra từng dòng và hiện xem trước (FR-002, FR-003).
3. Finance chọn Apply; hệ thống áp dụng dòng hợp lệ, lưu nhật ký và lịch sử (FR-004, FR-008, FR-009).

#### Functional Flow - Alternative (Luồng thay thế)

1. File lớn: chạy nền, Finance nhận thông báo khi xong (FR-005).
2. Tải danh sách dòng lỗi, sửa, tải lại; dòng đã áp dụng hiện "No change" (FR-004, FR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. File thiếu cột bắt buộc hoặc sai mẫu: không đọc (VAL-001).
2. File trống: không đọc (VAL-002).
3. Không có dòng nào để áp dụng: không có Apply (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Dòng hợp lệ được áp dụng, dòng lỗi bị loại và báo lý do (AS-01). |
| BR-002 | Nhập lại cùng dữ liệu không tạo thay đổi trùng. |
| BR-003 | Trợ cấp nhập từ file tuân theo cùng quy tắc kiểm tra như sửa tay (BBA-95). |
| BR-004 | Hoá đơn đã phát hành không bị thay đổi bởi lần nhập. |
| BR-005 | Mọi lần nhập có nhật ký; mọi thay đổi của trẻ có lịch sử. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Thiếu cột bắt buộc (Student ID, Year) hoặc không phải file Excel / CSV. | Không đọc; hiện "This file does not match the template. Missing column:" kèm tên cột. |
| VAL-002 | File không có dòng dữ liệu. | Không đọc; hiện "The file has no rows." |
| VAL-003 | Không có dòng nào hợp lệ có thay đổi. | Nút Apply bị mờ; hiện số dòng lỗi và số dòng không đổi. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Subsidy — Upload file và xem trước | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Chọn file | Tệp (Excel, CSV) | Có | — | VAL-001; VAL-002. | FR-001. |
| Xem trước | Bảng | Có | — | — | FR-003. |
| Apply | Nút | Có | — | VAL-003. | FR-004. |
| Tiến độ | Thanh tiến độ | Khi chạy nền | — | — | FR-005. |
| Download errors | Nút | Khi có lỗi | — | — | FR-004. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần nhập lưu: tên file, mã nhận diện file, người tải, thời điểm, số dòng đã áp dụng, không đổi, bị loại; với mỗi trẻ được áp dụng: giá trị đã đặt; với mỗi dòng bị loại: số dòng và lý do. |
| DATA-002 | Mỗi thay đổi của trẻ có lịch sử với nguồn "nhập file" và tên file. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | file theo mẫu 100 dòng: 90 hợp lệ có thay đổi, 6 không đổi, 4 lỗi | Finance tải lên | xem trước "90 to apply, 6 no change, 4 errors"; mỗi dòng lỗi có số dòng và lý do dễ hiểu | FR-001; FR-002; FR-003 |
| AC-002 | xem trước như AC-001 | Finance chọn Apply | 90 trẻ được cập nhật; 4 dòng lỗi không áp dụng; tải được danh sách dòng lỗi | FR-004; BR-001 |
| AC-003 | các cột trong file đổi thứ tự so với mẫu | tải lên | file vẫn được đọc đúng theo tên cột | FR-001 |
| AC-004 | một dòng có Subsidy là "abc" | kiểm tra | dòng lỗi "Row 8: Subsidy must be a number." | FR-002; BR-003 |
| AC-005 | cùng một trẻ và năm xuất hiện 2 lần | kiểm tra | cả hai dòng là lỗi trùng | FR-002 |
| AC-006 | file đã áp dụng hôm qua | tải lại cùng file | các dòng hiện "No change"; không có thay đổi mới | FR-006; BR-002 |
| AC-007 | file 5.000 dòng | Finance chọn Apply | hiện tiến độ; Finance nhận thông báo khi xong | FR-005 |
| AC-008 | hoá đơn tháng 12 đã phát hành | áp dụng file đổi subsidy | hoá đơn tháng 12 không đổi; hoá đơn tạo sau dùng giá trị mới | FR-007; BR-004 |
| AC-009 | đã áp dụng | Finance mở nhật ký nhập | thấy tên file, người tải, thời điểm, số dòng áp dụng, giá trị đã đặt cho từng trẻ, dòng bị loại kèm lý do | FR-008; BR-005; DATA-001 |
| AC-010 | đã áp dụng | Finance mở lịch sử một trẻ ở danh sách trợ cấp | thấy thay đổi với nguồn "nhập file" và tên file | FR-009; DATA-002 |
| AC-011 | file thiếu cột Student ID | tải lên | hiện "This file does not match the template. Missing column: Student ID" | VAL-001 |
| AC-012 | file chỉ có dòng tiêu đề | tải lên | hiện "The file has no rows." | VAL-002 |
| AC-013 | mọi dòng lỗi hoặc không đổi | xem trước | nút Apply bị mờ | VAL-003 |

#### Dependencies (Phụ thuộc)

Mẫu nhập (BBA-96); danh sách trợ cấp (BBA-95); danh sách loại SCFA; tính hoá đơn; báo cáo Import Subsidy (Sprint 8).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Áp dụng các dòng hợp lệ và bỏ dòng lỗi, hay phải đúng toàn bộ file mới áp dụng? | BBA Finance | Cao |  |
| OQ-02 | Ô để trống trong file nghĩa là "giữ nguyên" hay "xoá giá trị"? | BBA Finance | Cao |  |
| OQ-03 | Có cần một người khác duyệt trước khi áp dụng lần nhập không? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Áp dụng dòng hợp lệ, bỏ dòng lỗi và báo lý do. | FR-004; BR-001 — chờ OQ-01 |
| AS-02 | Ô trống nghĩa là giữ nguyên giá trị hiện có. | FR-002 — chờ OQ-02 |
| AS-03 | Không cần duyệt; người tải chọn Apply là áp dụng. | FR-004 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Nhật ký nhập | Bản ghi mỗi lần tải file trợ cấp; là dữ liệu cho báo cáo Import Subsidy. |
| No change | Dòng trong file có giá trị giống hệt giá trị hiện có, nên không cần áp dụng. |
