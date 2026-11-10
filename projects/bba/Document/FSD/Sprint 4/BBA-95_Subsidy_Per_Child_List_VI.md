# BBA-95 Subsidy per child – list & inline edit (SCFA type, subsidy, additional, FA, expiry, renewal) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › GIRO, subsidy & eGIRO |
| Tính năng | Subsidy per child – list & inline edit (SCFA type, subsidy, additional, FA, expiry, renewal) |
| Mã ticket | BBA-95 |
| Mã WBS | 3.6.9.07 |
| Mã tài liệu | FRD-BBA-95 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-95: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả danh sách trợ cấp theo năm của từng trẻ (mã hồ sơ, lớp, chương trình, loại SCFA, subsidy, additional subsidy, FA, ngày hết hạn, ngày gia hạn), sửa trực tiếp trên dòng có lịch sử, cảnh báo sắp hết hạn và ảnh hưởng tới hoá đơn. 4 câu hỏi mở ở mục 7 cần BBA Finance chốt; BBA chưa gửi mẫu danh sách trợ cấp hiện tại.

## 2. Mục tiêu và bối cảnh

Mỗi trẻ có thể được nhà nước trợ cấp học phí: trợ cấp cơ bản (subsidy), trợ cấp thêm (additional subsidy) và hỗ trợ tài chính (FA), theo loại hồ sơ SCFA và có ngày hết hạn. Hoá đơn hằng tháng trừ các khoản này. Finance cần một danh sách theo năm của mọi trẻ với số trợ cấp, sửa nhanh ngay trên dòng và luôn biết ai đã sửa gì.

Mục tiêu đo được: Finance thấy trong một bước toàn bộ trẻ có trợ cấp sắp hết hạn trong 30 ngày tới; mọi lần sửa có lịch sử.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách trợ cấp theo năm: trẻ, Centre, lớp, chương trình, mã hồ sơ, loại SCFA, subsidy, additional subsidy, FA, ngày hết hạn, ngày gia hạn. Sửa trực tiếp trên dòng. Cảnh báo sắp hết hạn / đã hết hạn. Lịch sử. Xuất file. | Tải mẫu (BBA-96) và nhập hàng loạt (BBA-97). Cách hoá đơn trừ trợ cấp và mức trần hằng tháng (ticket tính hoá đơn). Đối chiếu báo cáo trợ cấp hằng tháng của cơ quan quản lý. Nhập kết quả duyệt trợ cấp nhận qua email. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Xem, sửa, xuất danh sách. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Centre Admin, Centre Director | Centre của mình. | Xem (AS-02). |
| Hệ thống | Toàn hệ thống. | Đánh dấu hết hạn, lưu lịch sử, đưa giá trị mới vào lịch phí và hoá đơn. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Settings › Subsidy | Danh sách và sửa trợ cấp theo trẻ. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Danh sách trợ cấp theo trẻ và sửa trực tiếp

#### User Story

Là nhân viên Finance, tôi muốn xem trợ cấp của mọi trẻ theo năm, sửa ngay trên dòng và biết trẻ nào sắp hết hạn, để hoá đơn trừ đúng trợ cấp và tôi kịp nhắc gia hạn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Danh sách theo năm (chọn năm, mặc định năm hiện tại): tên trẻ, Centre, lớp, chương trình, mã hồ sơ (application ID), loại SCFA, subsidy, additional subsidy, FA, ngày hết hạn, ngày gia hạn, người cập nhật và thời điểm cập nhật gần nhất. |
| FR-002 | Tìm theo tên trẻ, mã hồ sơ; lọc theo Centre, lớp, loại SCFA, "Expiring in 30 days", "Expired". |
| FR-003 | Sửa trực tiếp: chọn ô của mã hồ sơ, loại SCFA, subsidy, additional subsidy, FA, ngày hết hạn hoặc ngày gia hạn, nhập giá trị mới, chọn lưu dòng; hệ thống kiểm tra trước khi lưu. |
| FR-004 | Dòng có ngày hết hạn trong 30 ngày tới hiện chữ "Expiring" màu cam; dòng đã hết hạn hiện "Expired" màu đỏ. |
| FR-005 | Giá trị mới áp dụng cho các hoá đơn tạo sau khi lưu; hoá đơn đã phát hành không đổi. Sau ngày hết hạn, hoá đơn không trừ trợ cấp đó nữa. |
| FR-006 | Lịch sử mỗi dòng: trường, giá trị cũ, giá trị mới, người sửa, thời điểm, nguồn (sửa tay hoặc nhập file). |
| FR-007 | Xuất danh sách theo bộ lọc ra Excel. |
| FR-008 | Loại SCFA chọn từ danh sách do HQ Finance quản lý (ví dụ LOR). |

#### Functional Flow - Main (Luồng chính)

1. Finance mở Subsidy, năm hiện tại (FR-001).
2. Finance lọc "Expiring in 30 days" để nhắc gia hạn (FR-002, FR-004).
3. Khi có kết quả gia hạn, Finance sửa ngày hết hạn trên dòng và lưu (FR-003, FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Sửa số subsidy của một trẻ khi có kết quả duyệt mới (FR-003, FR-005).
2. Xuất danh sách (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Số tiền âm hoặc không phải số: không lưu (VAL-001).
2. Ngày gia hạn sau ngày hết hạn: không lưu (VAL-002).
3. Loại SCFA không có trong danh sách: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Trợ cấp chỉ được trừ trên hoá đơn đến hết ngày hết hạn. |
| BR-002 | Sửa trợ cấp không làm thay đổi hoá đơn đã phát hành; sai lệch của tháng đã phát hành xử lý bằng credit note hoặc hoá đơn bổ sung. |
| BR-003 | Mọi lần sửa có lịch sử, kể cả sửa qua nhập file. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Subsidy, additional subsidy hoặc FA âm hoặc không phải số. | Không lưu; hiện "Enter an amount of 0 or more." |
| VAL-002 | Ngày gia hạn sau ngày hết hạn. | Không lưu; hiện "The renewal date must be on or before the expiry date." |
| VAL-003 | Loại SCFA không có trong danh sách. | Không lưu; chỉ chọn được từ danh sách. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Subsidy — danh sách theo năm | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Năm | Danh sách chọn | Có | Năm hiện tại | — | — |
| Bộ lọc | Bộ lọc | Không | — | — | FR-002. |
| Mã hồ sơ | Ô nhập trên dòng | Không | — | — | — |
| Loại SCFA | Danh sách chọn trên dòng | Không | — | VAL-003. | FR-008. |
| Subsidy, additional subsidy, FA | Số tiền trên dòng | Không | 0 | VAL-001. | — |
| Ngày hết hạn, ngày gia hạn | Ngày trên dòng | Không | — | VAL-002. | FR-004. |
| Lưu dòng | Nút | Theo quyền | Khi dòng có thay đổi | — | FR-003. |
| Export | Nút | Theo quyền | — | — | FR-007. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi dòng trợ cấp lưu: trẻ, năm, mã hồ sơ, loại SCFA, subsidy, additional subsidy, FA, ngày hết hạn, ngày gia hạn, người cập nhật, thời điểm. |
| DATA-002 | Mỗi lần sửa lưu: trường, giá trị cũ, giá trị mới, người sửa, thời điểm, nguồn. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | năm 2026 có 120 trẻ có trợ cấp | Finance mở Subsidy năm 2026 | thấy 120 dòng với đủ các cột | FR-001 |
| AC-002 | 5 trẻ hết hạn trong 30 ngày tới | Finance lọc "Expiring in 30 days" | thấy 5 trẻ, mỗi dòng có chữ "Expiring" màu cam | FR-002; FR-004 |
| AC-003 | trẻ có subsidy cũ | Finance sửa subsidy trên dòng và lưu | giá trị mới được lưu; lịch sử ghi giá trị cũ, mới, người sửa, thời điểm, nguồn "sửa tay" | FR-003; FR-006; BR-003 |
| AC-004 | hoá đơn tháng 12 đã phát hành | sửa subsidy | hoá đơn tháng 12 không đổi; hoá đơn tạo sau dùng giá trị mới | FR-005; BR-002 |
| AC-005 | trợ cấp hết hạn 31/12/2026 | tạo hoá đơn tháng 1/2027 | hoá đơn không trừ trợ cấp đó; dòng hiện "Expired" | FR-004; FR-005; BR-001 |
| AC-006 | Finance nhập FA -50 | lưu dòng | không lưu, hiện "Enter an amount of 0 or more." | VAL-001 |
| AC-007 | ngày gia hạn 01/02, ngày hết hạn 31/01 | lưu dòng | không lưu, hiện "The renewal date must be on or before the expiry date." | VAL-002 |
| AC-008 | Finance mở ô loại SCFA | xem | chỉ chọn được từ danh sách (ví dụ LOR) | FR-008; VAL-003 |
| AC-009 | Finance lọc Centre A | chọn Export | file Excel có đúng các dòng đang hiện | FR-007 |

#### Dependencies (Phụ thuộc)

Lịch phí (BBA-80); tính hoá đơn; tải mẫu (BBA-96) và nhập hàng loạt (BBA-97); danh sách loại SCFA; hồ sơ trẻ.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | BBA gửi mẫu danh sách trợ cấp đang dùng (một Centre là đủ) để chốt cột và định dạng. | BBA Finance | Cao |  |
| OQ-02 | Danh sách loại SCFA đầy đủ là gì; mỗi loại có mức trợ cấp mặc định không? | BBA Finance | Cao |  |
| OQ-03 | Sửa trợ cấp có cần duyệt hoặc ghi lý do không? | BBA Finance | Trung bình |  |
| OQ-04 | Subsidy, additional subsidy, FA là số tiền mỗi tháng phải không? | BBA Finance | Cao |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Số trợ cấp là số tiền mỗi tháng. | FR-001 — chờ OQ-04 |
| AS-02 | Centre Admin, Centre Director chỉ xem. | Mục 4 |
| AS-03 | Sửa trợ cấp không cần duyệt, không bắt buộc lý do. | FR-003 — chờ OQ-03 |
| AS-04 | Cảnh báo sắp hết hạn tính trong 30 ngày. | FR-004 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Subsidy / additional subsidy | Trợ cấp học phí cơ bản / trợ cấp thêm của nhà nước. |
| FA (financial assistance) | Hỗ trợ tài chính cho gia đình. |
| SCFA | Loại hồ sơ trợ cấp của trẻ (ví dụ LOR). |
| Mã hồ sơ (application ID) | Mã hồ sơ xin trợ cấp của trẻ. |
| Ngày hết hạn / ngày gia hạn | Ngày trợ cấp hết hiệu lực / ngày cần nộp gia hạn. |
