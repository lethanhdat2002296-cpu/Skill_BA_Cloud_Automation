# BBA-82 Batch update schedules (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › Payment schedule |
| Tính năng | Batch update schedules |
| Mã ticket | BBA-82 |
| Mã WBS | 3.6.7.03 |
| Mã tài liệu | FRD-BBA-82 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-82: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc cập nhật một trường của lịch phí cho nhiều trẻ từ một ngày hiệu lực, có xem trước giá trị cũ và mới. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Khi phí thay đổi (ví dụ phí mới từ tháng 1), Finance cần cập nhật lịch phí của nhiều trẻ cùng lúc. Finance chọn nhóm trẻ, chọn trường cần đổi và giá trị mới, ngày hiệu lực, xem trước từng trẻ rồi xác nhận.

Mục tiêu đo được: cập nhật xong một nhóm trẻ trong một lần xác nhận; không hoá đơn đã phát hành nào bị thay đổi.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Chọn trẻ theo Centre, lớp, level, quốc tịch, loại chương trình. Chọn trường cần đổi (nett, tên lịch phí, ghi chú, hiệu lực đến) và giá trị mới. Ngày hiệu lực. Xem trước giá trị cũ → mới. Xác nhận, kết quả, lịch sử. | Áp mẫu lịch phí (BBA-81). Đổi trợ cấp (BBA-95, BBA-97). Đổi bảng giá chung. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Cập nhật hàng loạt. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Hệ thống | Toàn hệ thống. | Tạo phiên bản lịch phí mới từ ngày hiệu lực, tính lại amount, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Payment schedule › Batch update | Cập nhật hàng loạt lịch phí. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Cập nhật hàng loạt lịch phí

#### User Story

Là nhân viên Finance, tôi muốn đổi phí của cả nhóm trẻ từ một ngày hiệu lực và xem trước từng trẻ, để áp phí mới cho năm sau mà không phải sửa từng lịch phí.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Batch update" cho chọn trẻ theo Centre, lớp, level, quốc tịch, loại chương trình (kết hợp được); chỉ lịch phí còn hiệu lực vào ngày hiệu lực được đưa vào. |
| FR-002 | Chọn trường cần đổi: nett, tên lịch phí, ghi chú, hoặc hiệu lực đến; nhập giá trị mới và ngày hiệu lực. |
| FR-003 | Xem trước: mỗi lịch phí một dòng gồm trẻ, loại chương trình, giá trị cũ, giá trị mới, amount cũ, amount mới do hệ thống tính; mỗi dòng có ô chọn. |
| FR-004 | "Confirm" với mỗi lịch phí được chọn: kết thúc phiên bản hiện tại vào ngày trước ngày hiệu lực và tạo phiên bản mới với giá trị mới từ ngày hiệu lực. Riêng đổi "hiệu lực đến" thì sửa trực tiếp ngày kết thúc. |
| FR-005 | Sau khi xác nhận hiện kết quả: số lịch phí đã cập nhật, số bị bỏ qua kèm lý do. |
| FR-006 | Mỗi lịch phí được cập nhật có dòng lịch sử: trường, giá trị cũ, giá trị mới, ngày hiệu lực, người thực hiện, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Finance chọn Batch update, lọc Centre và level N2, loại chương trình Full Day (FR-001).
2. Finance chọn trường nett, giá trị mới, hiệu lực 01/01/2027 (FR-002).
3. Finance xem trước, chọn Confirm (FR-003, FR-004, FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Đổi ghi chú hoặc tên lịch phí cho nhiều trẻ (FR-002).
2. Kết thúc lịch phí của một nhóm trẻ vào một ngày (hiệu lực đến) (FR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngày hiệu lực trong tháng đã khoá sổ: không thực hiện (VAL-001).
2. Giá trị mới không hợp lệ (nett âm): không thực hiện (VAL-002).
3. Không có lịch phí nào phù hợp: không có xem trước (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Đổi phí là phiên bản mới từ ngày hiệu lực; hoá đơn đã phát hành không bị thay đổi. |
| BR-002 | Tháng đã khoá sổ không thay đổi được. |
| BR-003 | Mọi thay đổi có lịch sử. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Ngày hiệu lực trong tháng đã khoá sổ. | Không thực hiện; hiện "This month is closed." |
| VAL-002 | Nett âm hoặc không phải số. | Không thực hiện; hiện "Enter an amount of 0 or more." |
| VAL-003 | Bộ lọc không có lịch phí nào. | Hiện "No schedules match these filters." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Batch update — chọn trẻ, giá trị mới và xem trước | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Bộ lọc trẻ | Bộ lọc | Centre: có | — | VAL-003. | FR-001. |
| Trường cần đổi | Danh sách chọn | Có | Nett | — | FR-002. |
| Giá trị mới | Theo trường | Có | — | VAL-002. | — |
| Ngày hiệu lực | Ngày | Có | Ngày đầu tháng sau | VAL-001. | — |
| Xem trước | Bảng có ô chọn | Có | Tất cả được chọn | — | FR-003. |
| Confirm | Nút | Có | — | — | FR-004; FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần cập nhật hàng loạt lưu: bộ lọc, trường, giá trị mới, ngày hiệu lực, số lịch phí cập nhật / bỏ qua, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | 30 trẻ N2 Full Day ở Centre A | Finance đổi nett sang giá mới từ 01/01/2027 | xem trước 30 dòng với nett cũ, nett mới, amount cũ, amount mới | FR-001; FR-002; FR-003 |
| AC-002 | xem trước như AC-001 | Finance chọn Confirm | 30 lịch phí cũ kết thúc 31/12/2026, phiên bản mới từ 01/01/2027; kết quả "30 updated, 0 skipped" | FR-004; FR-005; BR-001 |
| AC-003 | hoá đơn tháng 12 đã phát hành | cập nhật nett từ 01/01/2027 | hoá đơn tháng 12 không đổi | BR-001 |
| AC-004 | tháng 10 đã khoá sổ | ngày hiệu lực 01/10 | không thực hiện, hiện "This month is closed." | VAL-001; BR-002 |
| AC-005 | Finance nhập nett -100 | xem trước | không thực hiện, hiện "Enter an amount of 0 or more." | VAL-002 |
| AC-006 | đã cập nhật | Finance mở lịch sử một lịch phí | thấy trường nett, giá trị cũ, giá trị mới, ngày hiệu lực, người thực hiện | FR-006; BR-003; DATA-001 |
| AC-007 | bộ lọc không có lịch phí nào | xem | hiện "No schedules match these filters." | VAL-003 |

#### Dependencies (Phụ thuộc)

Lịch phí từng trẻ (BBA-80); thứ tự tính (BBA-87); khoá sổ tháng.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Ngoài nett, tên, ghi chú, hiệu lực đến, Finance cần đổi hàng loạt những trường nào khác (ví dụ loại chương trình)? | BBA Finance | Trung bình |  |
| OQ-02 | Trẻ có nett riêng (sửa tay) có bị đổi theo cập nhật hàng loạt không? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Trường đổi được: nett, tên lịch phí, ghi chú, hiệu lực đến. | FR-002 — chờ OQ-01 |
| AS-02 | Trẻ có nett riêng vẫn hiện trong xem trước để Finance tự bỏ chọn. | FR-003 — chờ OQ-02 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Phiên bản lịch phí | Mỗi lần đổi phí tạo một phiên bản mới có ngày hiệu lực; phiên bản cũ giữ nguyên. |
