# BBA-81 Apply payment schedule template (bulk) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › Payment schedule |
| Tính năng | Apply payment schedule template (bulk) |
| Mã ticket | BBA-81 |
| Mã WBS | 3.6.7.02 |
| Mã tài liệu | FRD-BBA-81 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-81: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc chọn nhiều trẻ theo lớp / level / quốc tịch và áp một mẫu lịch phí cho một khoảng thời gian, có xem trước, tạo mới hoặc thay lịch phí đang có. 3 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Đầu năm học hoặc khi mở lớp mới, Finance cần tạo lịch phí cho nhiều trẻ cùng lúc. Finance chọn nhóm trẻ (theo lớp, level, quốc tịch), chọn một mẫu lịch phí và khoảng thời gian, xem trước kết quả cho từng trẻ rồi xác nhận.

Mục tiêu đo được: tạo lịch phí cho cả một lớp trong một lần xác nhận; mỗi trẻ được tạo hoặc thay đều có lịch sử.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Chọn trẻ theo Centre, lớp, level, quốc tịch. Chọn mẫu lịch phí và khoảng thời gian. Chế độ "Create" (chỉ trẻ chưa có) hoặc "Replace" (thay lịch đang có). Xem trước từng trẻ, bỏ chọn trẻ. Xác nhận và lịch sử. | Sửa lịch phí từng trẻ (BBA-80). Cập nhật một trường cho nhiều trẻ (BBA-82). Tạo và sửa mẫu lịch phí (OQ-01). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Áp mẫu lịch phí. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Hệ thống | Toàn hệ thống. | Tính số tiền theo từng trẻ, kết thúc lịch cũ khi thay, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Payment schedule › Apply template | Áp mẫu lịch phí cho nhiều trẻ. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Áp mẫu lịch phí cho nhiều trẻ

#### User Story

Là nhân viên Finance, tôi muốn áp một mẫu lịch phí cho cả nhóm trẻ trong một lần và xem trước kết quả, để không phải tạo lịch phí cho từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Apply template" cho chọn trẻ theo Centre, lớp, level, quốc tịch (kết hợp được); chỉ trẻ đang học hoặc đã xác nhận nhập học được chọn. |
| FR-002 | Chọn mẫu lịch phí (loại chương trình, tên lịch phí, nett), hiệu lực từ (bắt buộc) và hiệu lực đến (không bắt buộc). |
| FR-003 | Chọn chế độ: "Create" chỉ tạo cho trẻ chưa có lịch phí cùng loại chương trình trong khoảng đó; "Replace" kết thúc lịch phí cùng loại đang có vào ngày trước hiệu lực từ rồi tạo lịch mới. |
| FR-004 | Màn xem trước: mỗi trẻ một dòng gồm lịch phí hiện có, lịch phí mới, nett, amount do hệ thống tính, kết quả dự kiến (Will create, Will replace, Skipped kèm lý do); mỗi dòng có ô chọn. |
| FR-005 | Ở chế độ Create, trẻ đã có lịch phí cùng loại trong khoảng đó hiện "Skipped — already has a schedule". |
| FR-006 | "Confirm" thực hiện cho các trẻ được chọn và hiện kết quả: số trẻ được tạo, được thay, bị bỏ qua. |
| FR-007 | Mỗi trẻ được tạo hoặc thay có dòng lịch sử ghi mẫu đã áp, lịch cũ, lịch mới, người thực hiện, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Finance chọn Apply template, chọn Centre và lớp (FR-001).
2. Finance chọn mẫu Full Day, hiệu lực từ 01/01/2027, chế độ Create (FR-002, FR-003).
3. Finance xem trước, bỏ chọn trẻ không áp dụng, chọn Confirm (FR-004, FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Chế độ Replace để đổi lịch phí của cả lớp từ năm học mới (FR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có trẻ nào phù hợp bộ lọc: không có màn xem trước (VAL-001).
2. Hiệu lực từ trong tháng đã khoá sổ: không thực hiện (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Thay lịch phí là kết thúc lịch cũ, không xoá lịch cũ. |
| BR-002 | Một trẻ không có hai lịch phí cùng loại chương trình trùng thời gian. |
| BR-003 | Tháng đã khoá sổ không thay đổi được. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có trẻ nào. | Hiện "No children match these filters." |
| VAL-002 | Hiệu lực từ trong tháng đã khoá sổ. | Không thực hiện; hiện "This month is closed." |
| VAL-003 | Không còn trẻ nào được chọn. | Nút Confirm bị mờ. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Apply template — chọn trẻ, mẫu và xem trước | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Centre, lớp, level, quốc tịch | Bộ lọc | Centre: có | — | VAL-001. | FR-001. |
| Mẫu lịch phí | Danh sách chọn | Có | — | — | FR-002. |
| Hiệu lực từ / đến | Ngày | Từ: có | — | VAL-002. | — |
| Chế độ | Lựa chọn | Có | Create | — | FR-003. |
| Xem trước | Bảng có ô chọn | Có | Tất cả trẻ hợp lệ được chọn | VAL-003. | FR-004; FR-005. |
| Confirm | Nút | Có | — | VAL-003. | FR-006. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần áp mẫu lưu: mẫu, bộ lọc, chế độ, hiệu lực, số trẻ tạo / thay / bỏ qua, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Sunbeams có 20 trẻ, 2 trẻ đã có Full Day từ 01/01/2027 | Finance áp mẫu Full Day, hiệu lực 01/01/2027, chế độ Create | xem trước: 18 trẻ "Will create", 2 trẻ "Skipped — already has a schedule" | FR-001; FR-002; FR-004; FR-005 |
| AC-002 | xem trước như AC-001 | Finance chọn Confirm | 18 lịch phí được tạo; kết quả hiện "18 created, 0 replaced, 2 skipped" | FR-006 |
| AC-003 | trẻ có Half Day không ngày kết thúc | áp mẫu Half Day mới từ 01/01/2027, chế độ Replace | lịch cũ kết thúc 31/12/2026, lịch mới bắt đầu 01/01/2027 | FR-003; BR-001; BR-002 |
| AC-004 | lọc quốc tịch "Foreigner" ở lớp không có trẻ nước ngoài | xem | hiện "No children match these filters." | VAL-001 |
| AC-005 | tháng 10 đã khoá sổ | áp mẫu hiệu lực 01/10 | không thực hiện, hiện "This month is closed." | VAL-002; BR-003 |
| AC-006 | Finance bỏ chọn tất cả trẻ | nhìn nút Confirm | nút bị mờ | VAL-003 |
| AC-007 | đã áp mẫu cho 18 trẻ | Finance mở lịch sử một trẻ | thấy mẫu đã áp, lịch mới, người thực hiện, thời điểm | FR-007; DATA-001 |

#### Dependencies (Phụ thuộc)

Lịch phí từng trẻ (BBA-80); mẫu lịch phí; bảng giá; thứ tự tính (BBA-87); khoá sổ tháng.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Mẫu lịch phí do ai tạo, lưu ở đâu, gồm những trường nào? | BBA Finance | Cao |  |
| OQ-02 | Nett trong mẫu cố định hay lấy theo bảng giá của từng trẻ (level, quốc tịch)? | BBA Finance | Cao |  |
| OQ-03 | Ở chế độ Replace, trẻ có nett riêng (sửa tay) có bị thay không? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Mẫu lịch phí gồm loại chương trình, tên lịch phí, nett; Finance quản lý danh sách mẫu. | FR-002 — chờ OQ-01 |
| AS-02 | Trẻ có nett riêng vẫn hiện trong xem trước để Finance tự bỏ chọn. | FR-004 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Mẫu lịch phí | Bộ thiết lập lịch phí dùng chung để áp cho nhiều trẻ. |
| Create / Replace | Chỉ tạo cho trẻ chưa có / thay lịch phí đang có. |
