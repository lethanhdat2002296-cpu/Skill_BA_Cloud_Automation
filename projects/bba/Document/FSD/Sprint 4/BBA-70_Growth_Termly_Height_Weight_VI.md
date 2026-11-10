# BBA-70 Growth – termly height & weight entry by class (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Health & allergies (Growth) |
| Tính năng | Growth – termly height & weight entry by class |
| Mã ticket | BBA-70 |
| Mã WBS | 3.1.3.03 |
| Mã tài liệu | FRD-BBA-70 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-70: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả màn nhập chiều cao, cân nặng theo lớp mỗi kỳ, cách tính BMI, cảnh báo số liệu bất thường, phụ huynh xem kết quả và báo cáo theo dõi cho HQ. 5 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Mỗi kỳ, giáo viên đo chiều cao và cân nặng của trẻ trong lớp và ghi vào hệ thống một lần cho cả lớp. Hệ thống tự tính chỉ số BMI và vị trí trên biểu đồ tăng trưởng; phụ huynh xem được trong Parents App; HQ theo dõi Centre nào đã đo đủ.

Mục tiêu đo được: giáo viên nhập xong một lớp trong một lần lưu; 100% số đo đã lưu hiện cho phụ huynh ngay sau khi lưu, không cần duyệt.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Màn nhập theo lớp và kỳ đo: chiều cao, cân nặng, ngày đo. Tính BMI và vị trí trên biểu đồ tăng trưởng. Cảnh báo số liệu bất thường. Nhập cho một trẻ từ hồ sơ trẻ. Biểu đồ tăng trưởng trên hồ sơ trẻ và trong Parents App. Báo cáo theo dõi việc đo cho HQ. | Thiết bị đo kết nối tự động. Nhận xét dinh dưỡng, tư vấn sức khoẻ. Danh sách dị ứng (BBA-69). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Teacher / Senior Teacher | Lớp của mình. | Nhập và sửa số đo của trẻ lớp mình. |
| Centre Director, School Admin | Centre của mình. | Nhập, sửa số đo; theo dõi lớp nào chưa đo. |
| HQ Admin | Mọi Centre. | Cấu hình kỳ đo; xem báo cáo theo dõi. |
| HQ Ops (District Manager, Operations Manager) | Các Centre mình phụ trách. | Xem báo cáo theo dõi. |
| Phụ huynh (Parents App) | Con mình. | Xem số đo và biểu đồ tăng trưởng. |
| Hệ thống | Toàn hệ thống. | Tính tuổi, BMI, vị trí trên biểu đồ; lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Health & allergies › Growth | Nhập số đo theo lớp và kỳ, biểu đồ tăng trưởng, báo cáo theo dõi. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Nhập chiều cao, cân nặng theo lớp mỗi kỳ

#### User Story

Là giáo viên, tôi muốn nhập chiều cao và cân nặng của cả lớp trên một màn hình và lưu một lần, để không phải mở từng hồ sơ trẻ và phụ huynh thấy ngay sự phát triển của con.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Màn "Height & weight" cho chọn lớp, kỳ đo (theo danh sách kỳ do HQ Admin thiết lập) và ngày đo (mặc định hôm nay, không được sau hôm nay). |
| FR-002 | Bảng có một dòng cho mỗi trẻ đang học trong lớp: tên, tuổi (năm và tháng tại ngày đo), số đo lần trước (chiều cao, cân nặng, ngày đo), ô nhập chiều cao (cm) và cân nặng (kg). Trẻ vắng hôm nay có chữ "Vắng hôm nay". |
| FR-003 | "Save" lưu một lần mọi dòng đã nhập đủ cả chiều cao và cân nặng; dòng để trống không được lưu và vẫn là "Chưa đo" trong kỳ. Số đo có hiệu lực ngay, không cần duyệt. |
| FR-004 | Hệ thống tính BMI = cân nặng (kg) chia bình phương chiều cao (m), làm tròn 1 chữ số thập phân, và vị trí của trẻ trên biểu đồ tăng trưởng theo tuổi và giới tính, theo chuẩn tăng trưởng BBA chọn. |
| FR-005 | Số đo ngoài khoảng hợp lệ bị chặn (VAL-001). Chiều cao thấp hơn lần đo trước hiện cảnh báo "Height is lower than the last measurement. Check before saving."; người dùng vẫn lưu được. |
| FR-006 | Một trẻ chỉ có một số đo cho mỗi kỳ; nhập lại trong cùng kỳ thì số mới thay số cũ, số cũ giữ trong lịch sử kèm người sửa và thời điểm. |
| FR-007 | Từ hồ sơ trẻ, người dùng có quyền nhập được số đo cho riêng một trẻ, bất kỳ ngày nào, cho trẻ ở mọi độ tuổi. |
| FR-008 | Hồ sơ trẻ và mục Health & growth trong Parents App hiển thị chiều cao, cân nặng, ngày đo, BMI và biểu đồ tăng trưởng; số đo mới hiện ngay sau khi lưu. |
| FR-009 | Báo cáo theo dõi cho HQ: theo Centre, lớp và kỳ đo — số trẻ đã đo, số trẻ chưa đo, tỷ lệ đã đo; xuất ra Excel. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Growth, chọn lớp, kỳ đo và ngày đo (FR-001).
2. Hệ thống hiển thị trẻ trong lớp kèm số đo lần trước (FR-002).
3. Giáo viên nhập chiều cao, cân nặng cho trẻ có mặt và chọn Save (FR-003; VAL-001, VAL-002).
4. Hệ thống tính BMI, vị trí trên biểu đồ (FR-004) và hiện cho phụ huynh (FR-008).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ vắng hôm đo: để trống, nhập vào ngày khác trong kỳ (FR-002, FR-003).
2. Nhập sai: nhập lại trong cùng kỳ, số cũ vào lịch sử (FR-006).
3. Nhập cho một trẻ từ hồ sơ trẻ (FR-007).
4. HQ xem báo cáo Centre nào chưa đo đủ (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Số đo ngoài khoảng hợp lệ: không lưu dòng đó (VAL-001).
2. Chỉ nhập một trong hai số: không lưu dòng đó (VAL-002).
3. Ngày đo sau hôm nay: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Số đo do nhân viên ghi trực tiếp, không cần duyệt. |
| BR-002 | Mỗi trẻ một số đo cho mỗi kỳ; số mới thay số cũ, lịch sử được giữ. |
| BR-003 | BMI và vị trí trên biểu đồ do hệ thống tính, người dùng không sửa tay. |
| BR-004 | Phụ huynh chỉ xem số đo của con mình. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chiều cao hoặc cân nặng ngoài khoảng hợp lệ (AS-02). | Dòng đó không được lưu; ô bị đánh dấu với chữ "Check this value." |
| VAL-002 | Chỉ nhập chiều cao hoặc chỉ nhập cân nặng. | Dòng đó không được lưu; ô còn trống bị đánh dấu "Enter both height and weight." |
| VAL-003 | Ngày đo sau hôm nay. | Không lưu; hiện "The measurement date cannot be in the future." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Growth — nhập theo lớp | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Lớp | Danh sách chọn | Có | Lớp đầu tiên của giáo viên | — | Giáo viên chỉ thấy lớp mình. |
| Kỳ đo | Danh sách chọn | Có | Kỳ hiện tại | — | Danh sách do HQ Admin thiết lập. |
| Ngày đo | Ngày | Có | Hôm nay | VAL-003. | — |
| Chiều cao (cm) | Số, 1 chữ số thập phân | Khi nhập dòng | Trống | VAL-001; VAL-002. | — |
| Cân nặng (kg) | Số, 1 chữ số thập phân | Khi nhập dòng | Trống | VAL-001; VAL-002. | — |
| Save | Nút | Có | — | — | FR-003. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi số đo lưu: trẻ, kỳ đo, ngày đo, chiều cao, cân nặng, BMI, vị trí trên biểu đồ, người nhập, thời điểm nhập. |
| DATA-002 | Mỗi lần sửa lưu giá trị cũ, giá trị mới, người sửa và thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Nursery 1 có 18 trẻ, 17 trẻ có mặt | giáo viên nhập số đo cho 17 trẻ và chọn Save | 17 số đo được lưu cùng lúc, không cần duyệt; trẻ còn lại là "Chưa đo" và có chữ "Vắng hôm nay" | FR-001; FR-002; FR-003; BR-001 |
| AC-002 | trẻ cao 100 cm, nặng 16 kg | số đo được lưu | BMI hiện 16,0 | FR-004; BR-003 |
| AC-003 | giáo viên nhập 1000 cm | chọn Save | dòng đó không được lưu, ô hiện "Check this value." | VAL-001 |
| AC-004 | giáo viên chỉ nhập chiều cao | chọn Save | dòng đó không được lưu, ô cân nặng hiện "Enter both height and weight." | VAL-002 |
| AC-005 | lần trước trẻ cao 98 cm | giáo viên nhập 96 cm | hiện cảnh báo chiều cao thấp hơn lần trước; giáo viên vẫn lưu được | FR-005 |
| AC-006 | trẻ đã có số đo kỳ này | giáo viên nhập lại số khác trong cùng kỳ | số mới thay số cũ; lịch sử ghi số cũ, người sửa, thời điểm | FR-006; BR-002; DATA-002 |
| AC-007 | số đo vừa được lưu | phụ huynh mở Health & growth | thấy chiều cao, cân nặng, ngày đo, BMI và điểm mới trên biểu đồ | FR-008; BR-004 |
| AC-008 | ngày đo chọn ngày mai | chọn Save | hiện "The measurement date cannot be in the future." | VAL-003 |
| AC-009 | Centre A đo 15 / 20 trẻ trong kỳ | HQ Admin mở báo cáo theo dõi | Centre A hiện đã đo 15, chưa đo 5, tỷ lệ 75% | FR-009 |
| AC-010 | Centre Director mở hồ sơ một trẻ | nhập số đo cho riêng trẻ đó | số đo được lưu và biểu đồ của trẻ cập nhật | FR-007 |

#### Dependencies (Phụ thuộc)

Danh sách lớp và trẻ đang học; hồ sơ trẻ (ngày sinh, giới tính); Parents App (Health & growth); danh sách kỳ đo.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Các kỳ đo trong năm học là kỳ nào, bắt đầu và kết thúc ngày nào? | HQ Ops | Cao |  |
| OQ-02 | Biểu đồ tăng trưởng dùng chuẩn nào (ví dụ chuẩn của Tổ chức Y tế Thế giới hay chuẩn quốc gia Singapore / Malaysia)? | HQ Ops | Cao |  |
| OQ-03 | Khoảng hợp lệ của chiều cao và cân nặng theo độ tuổi là bao nhiêu? | HQ Ops | Trung bình |  |
| OQ-04 | Báo cáo theo dõi cho HQ cần thêm gì ngoài số trẻ đã đo / chưa đo (ví dụ trẻ có BMI bất thường)? | HQ Ops | Trung bình |  |
| OQ-05 | Có nhắc giáo viên khi gần hết kỳ mà lớp chưa đo đủ không; nhắc ai, lúc nào? | Centre Director / HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | HQ Admin thiết lập danh sách kỳ đo. | FR-001 — chờ OQ-01 |
| AS-02 | Khoảng hợp lệ tạm thời: chiều cao 40–150 cm, cân nặng 2–50 kg, cho tới khi BBA chốt. | VAL-001 — chờ OQ-03 |
| AS-03 | Chiều cao và cân nặng nhập 1 chữ số thập phân. | FR-002 |
| AS-04 | Báo cáo theo dõi đếm số trẻ đã đo / chưa đo theo kỳ. | FR-009 — chờ OQ-04 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Kỳ đo | Khoảng thời gian trong năm học mà Centre phải đo chiều cao, cân nặng cho trẻ một lần. |
| BMI | Chỉ số khối cơ thể, tính từ chiều cao và cân nặng. |
| Biểu đồ tăng trưởng | Biểu đồ so sánh chiều cao, cân nặng của trẻ với trẻ cùng tuổi, cùng giới tính. |
