# Health & Allergies List Growth

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
| Ngày | 18/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |

**Mức sẵn sàng:** Đặc tả các thông tin: số đo cả lớp , số đo từng trẻ, biểu đồ tăng trưởng, báo cáo hoàn thành, nhắc nhập.

## 2. Mục tiêu và bối cảnh

Mỗi term, giáo viên đo chiều cao và cân nặng của trẻ trong lớp và ghi vào hệ thống một lần cho cả lớp, thay cho báo cáo “Quarterly Heights & Weight Report” đang giữ trên Taidii. Hệ thống vẽ biểu đồ tăng trưởng theo chuẩn Singapore / Malaysia; dữ liệu cân đo cập nhật tức thời lên app phụ huynh; Centre Director, Admin và Cluster Head theo dõi lớp nào đã đo đủ, vì nhiều Centre quên nhập khiến portfolio bị trống.

Mục tiêu: giáo viên nhập xong một lớp trong một lần lưu; số đo có hiệu lực ngay sau khi lưu, không cần duyệt.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Nhập theo lớp và term; trẻ vắng và tạm nghỉ ở nhóm riêng. Year view và xuất Excel. Biểu đồ tăng trưởng. Cảnh báo số đo bất thường. Nhập cho một trẻ từ hồ sơ trẻ. Sửa, xoá số đo. Biểu đồ và lịch sử đo trên hồ sơ trẻ. Nhắc nhập theo term. Báo cáo completion. | BMI . Thống kê tăng trưởng trong báo cáo). Thiết bị đo kết nối tự động. Nhận xét dinh dưỡng, tư vấn sức khỏe. Danh sách dị ứng (BBA-69). Màn xem số đo trong Parents App (chức năng của Parents App). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ trong lớp / Centre được cấp. | Thêm, sửa, xoá số đo; xem Year view, xuất Excel. |
| Report Viewer | Các Centre được cấp. | Xem báo cáo Height & weight completion. |
| System | Số đo của trẻ; lịch term của brand. | Tính tuổi và vị trí trên biểu đồ, gửi nhắc, ghi lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

Mọi quyền xem và thao tác theo mô hình phân quyền theo vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Health & allergies** | Số đo cả lớp | Nhập, sửa số đo chiều cao, cân nặng của cả lớp theo term; trẻ vắng / tạm nghỉ ở nhóm riêng; lưu một lần; cảnh báo số đo bất thường; xuất Excel. | BBA-70: US-001 |
| **Health & allergies** | Số đo từng trẻ | Thêm, sửa, xoá số đo của một trẻ trên hồ sơ trẻ; lịch sử đo. | BBA-70: US-002 |
| **Health & allergies** | Báo cáo hoàn thành | Tỷ lệ trẻ đã đo theo Centre, lớp, term; lọc, xuất. | BBA-70: US-003 |
| **Health & allergies** | Nhắc nhập | Nhắc nhập số đo giữa tháng cuối mỗi term. | BBA-70: US-004 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-70: US-001 - Số đo cả lớp

#### User Story

Là giáo viên, tôi muốn nhập chiều cao và cân nặng của cả lớp trên một màn hình và lưu một lần, để không phải mở từng hồ sơ trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Nhập chiều cao, cân nặng của cả lớp theo kỳ đo và ngày đo. |
| FR-002 | Chia danh sách trẻ của lớp thành 2 nhóm để nhập: có mặt hôm nay; vắng hoặc tạm nghỉ (BR-001). |
| FR-003 | Lưu một lần số đo của cả lớp (BR-002, BR-005). |
| FR-004 | Sửa số đo đã lưu trong kỳ ngay trên màn nhập của lớp. |
| FR-005 | Cảnh báo số đo bất thường trước khi lưu (BR-003). |
| FR-006 | Xem và xuất Excel thông tin số đo của cả lớp. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Growth, chọn lớp, kỳ đo và ngày đo (FR-001).
2. Hệ thống chia trẻ thành 2 nhóm, kèm số đo đã có trong kỳ (FR-002).
3. Giáo viên nhập chiều cao, cân nặng và chọn “Save the whole class” (FR-003; VAL-001, VAL-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ vắng hoặc tạm nghỉ: để trống, nhập vào ngày khác trong kỳ (FR-002; BR-001).
2. Nhập lại số khác trong cùng kỳ: số mới thay số cũ (FR-004).
3. Chọn Year view để xem cả năm của lớp và xuất Excel (FR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Số đo ngoài khoảng hợp lệ: không lưu dòng đó (VAL-001).
2. Chỉ nhập một trong hai số: không lưu dòng đó (VAL-002).
3. Ngày đo sau hôm nay: không lưu.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Đối tượng: mọi trẻ của lớp, kể cả trẻ vắng và tạm nghỉ; trẻ vắng / tạm nghỉ để trống được và nhập sau trong cùng kỳ (BBA-1059 Q2). |
| BR-002 | Lưu cả lớp: chỉ lưu dòng có đủ chiều cao và cân nặng; dòng để trống vẫn là “Not recorded yet”; dòng lỗi chặn các dòng hợp lệ (Q-71-09). Số đo không cần duyệt, có hiệu lực ngay (BR-CHF-026). |
| BR-003 | Chiều cao thấp hơn lần đo trước: hiện cảnh báo “Height is lower than the last measurement. Check before saving.”; người dùng không lưu được. |
| BR-004 | Quyền: thêm, sửa, xoá số đo là một quyền chung (BBA-1059 Q3), cấp theo vai trò — hiện BBA giao cho Centre Director, Admin và mọi giáo viên; người dùng chỉ thao tác trên trẻ trong phạm vi dữ liệu của mình (Q-71-10). Áp cho US-001 và US-002. |
| BR-005 | Dữ liệu được cập nhật lên app |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chiều cao ngoài khoảng hợp lệ (khoảng chờ OQ-01). | Dòng đó không được lưu; ô bị đánh dấu với chữ “Check this value.” |
| VAL-002 | Chỉ nhập chiều cao hoặc chỉ nhập cân nặng. | Dòng đó không được lưu; ô còn trống bị đánh dấu “Enter both height and weight.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Height & weight — Edit nhập theo lớp |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Height & weight — nhập theo lớp** |  |  |  |  |  |
| Height & weight | Tiêu đề màn hình | — | — | — | Màn nhập chiều cao, cân nặng theo lớp. |
| Save the whole class | Nút chính | Có | Chỉ bật khi có ít nhất 1 ô được nhập / sửa | VAL-001; VAL-002. | Lưu một lần số đo của mọi trẻ đã nhập (FR-003). |
| Allergies & conditions · Growth | Tab | — | Growth | — | Tab trong mục Health & allergies. |
| Enter this term · Year view | Chip chọn 1 | Có | Enter this term | — | Chuyển giữa nhập số đo kỳ hiện tại và bảng cả năm (FR-006). |
| Centre | Danh sách chọn | Không | Centre của người dùng | — | Người quản lý nhiều Centre mới đổi được. |
| Class | Danh sách chọn | Có | — | — | Lớp cần nhập; đổi lớp thì danh sách trẻ đổi theo. |
| Term | Danh sách chọn | Có | Kỳ hiện tại, ví dụ “Term 4 · 2026” | — | Theo lịch term của brand. |
| Date measured | Chọn ngày | Có | Hôm nay | — | DD/MM/YYYY; áp cho mọi trẻ được lưu lần này. |
| Term … — x of y recorded | Text | — | — | — | Số trẻ đã có số đo trong kỳ / tổng số trẻ của lớp; cập nhật sau mỗi lần lưu. |
| Reminder sent to the centre on … | Text | — | Ẩn nếu chưa gửi | — | Ngày hệ thống gửi nhắc Centre, DD/MM/YYYY (US-004). |
| Present today / Absent today · Temporary withdrawal | Nhóm | — | — | — | 2 nhóm trẻ (FR-002). |
| Child | Cột | — | — | — | Họ tên đầy đủ của trẻ; không sửa được. |
| Age | Cột | — | — | — | Tuổi tại ngày đo, dạng “4y 9m”; không sửa được. |
| Already recorded this term | Cột (nhãn) | — | “Not recorded yet” khi chưa đo | — | Số đo đã lưu trong kỳ, ví dụ “107 cm · 17.6 kg”; sửa số ở ô bên cạnh rồi lưu là ghi đè (FR-004). |
| Height (cm) | Ô nhập số, 1 chữ số thập phân | Khi nhập dòng | Số đã lưu trong kỳ, nếu có; trống hiện “—” | VAL-001; VAL-002. | Để trống thì không lưu cho trẻ đó. |
| Weight (kg) | Ô nhập số, 1 chữ số thập phân | Khi nhập dòng | Số đã lưu trong kỳ, nếu có; trống hiện “—” | VAL-001; VAL-002. | Để trống thì không lưu cho trẻ đó. |
| Saved n measurements | Thông báo (toast) | — | Tự ẩn | — | Báo lưu thành công kèm số trẻ vừa lưu. |
| **SCR-02 — Height & weight — Year view** |  |  |  |  |  |
| Export (Excel) | Nút | Theo quyền | — | — | Xuất bảng đang xem theo bố cục Year view. |
| Centre, Class, Year | Danh sách chọn | Class, Year: có | Year hiện tại | — | Chọn lớp và năm cần xem. |
| No. / Child / Birthdate / IC / BC No. / Programme | Cột | — | — | — | IC / BC No. che theo vai trò (BBA-66); Programme dạng “N2 full day”. |
| Term 1 – Term 4 · Height cm / Weight kg | Cột hai tầng | — | Kỳ chưa đo hiện “—” | — | Mỗi kỳ 2 cột con. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi số đo lưu: trẻ, kỳ đo, ngày đo, chiều cao (cm), cân nặng (kg), vị trí trên biểu đồ, chuẩn biểu đồ dùng, người nhập, nơi nhập (class entry / child record), thời điểm nhập. |
| AUDIT-001 | Mỗi lần sửa ghi giá trị cũ, giá trị mới, người sửa, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Nursery 1 có 18 trẻ, 17 trẻ có mặt | giáo viên nhập số đo cho 17 trẻ và chọn “Save the whole class” | 17 số đo được lưu cùng lúc, không cần duyệt; trẻ còn lại ở nhóm “Absent today” với “Not recorded yet” | FR-001; FR-002; FR-003; BR-002 |
| AC-002 | Sofia đang tạm nghỉ | giáo viên mở màn nhập lớp của Sofia | Sofia ở nhóm “Absent today · Temporary withdrawal”, ô nhập để trống được | FR-002; BR-001 |
| AC-003 | giáo viên nhập 1000 cm | chọn Save | dòng đó không được lưu, ô hiện “Check this value.” | VAL-001 |
| AC-004 | giáo viên chỉ nhập chiều cao | chọn Save | dòng đó không được lưu, ô cân nặng hiện “Enter both height and weight.” | VAL-002 |
| AC-005 | ngày đo chọn ngày mai | chọn Save | hiện “The measurement date cannot be in the future.” | — |
| AC-006 | lần trước trẻ cao 98 cm | giáo viên nhập 96 cm | hiện cảnh báo chiều cao thấp hơn lần trước; giáo viên vẫn lưu được | FR-005; BR-003 |
| AC-007 | trẻ đã có số đo kỳ này | giáo viên nhập lại số khác trong cùng kỳ | số mới thay số cũ; lịch sử ghi số cũ, người sửa, thời điểm | FR-004; AUDIT-001 |
| AC-008 | số đo vừa được lưu | hệ thống hoàn tất lưu | dữ liệu cân đo được cập nhật tức thời lên app phụ huynh | FR-003; BR-005 |
| AC-009 | Centre thuộc brand Brighton Montessori, lịch 2027 bắt đầu Term 2 ngày 01/04/2027 | giáo viên mở danh sách kỳ đo ngày 10/04/2027 | danh sách có Term 1 đến Term 4 của 2027, mặc định Term 2 | FR-001 |
| AC-010 | lớp N2 · Sunbeams có số đo Term 1–4 năm 2026 | giáo viên chọn Year view, năm 2026 | mỗi trẻ một dòng với ngày sinh, IC / BC No. đã che, chương trình học và Height cm / Weight kg của 4 term; term chưa đo hiện “—” | FR-006 |
| AC-011 | đang ở Year view lớp N2 · Sunbeams năm 2026 | giáo viên chọn Export (Excel) | file có đầu trang Centre, Class, Year, Generated on và các cột như Year view | FR-006 |
| AC-012 | Teacher lớp N2 · Sunbeams | mở màn nhập | chỉ chọn được lớp trong phạm vi của mình | BR-004 |

#### Dependencies (Phụ thuộc)

Danh sách lớp và trẻ (gồm trẻ vắng và tạm nghỉ); lịch term theo brand (HQ Admin); quy tắc che số giấy tờ (BBA-66).

### 6.2 BBA-70: US-002 - Số đo từng trẻ

#### User Story

Là Centre Director, tôi muốn thêm, sửa, xoá số đo của một trẻ trên hồ sơ trẻ để ghi bổ sung hoặc sửa số nhập nhầm.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-007 | Thêm số đo cho một trẻ từ hồ sơ trẻ (BR-006). |
| FR-008 | Sửa một số đo của trẻ (BR-004, BR-007). |
| FR-009 | Hiển thị lịch sử đo của trẻ (BR-008). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở hồ sơ trẻ, tab Health › Growth (FR-009).
2. Người dùng chọn “+ Add measurement”, nhập Term, ngày đo, chiều cao, cân nặng và lưu (FR-007; VAL-001, VAL-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Sửa một lần đo: chọn Edit, sửa và lưu (FR-008).
2. Xoá một lần đo: chọn Delete và xác nhận (FR-008; BR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Số đo không hợp lệ: không lưu (VAL-001, VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-006 | Từ hồ sơ trẻ nhập được số đo vào bất kỳ ngày nào, cho trẻ ở mọi độ tuổi. |
| BR-007 | Xoá cần xác nhận; sau khi xoá, số đo không còn hiện trên app phụ huynh; lịch sử vẫn giữ lần xoá (BBA-1059 Q3). |
| BR-008 | Lịch sử đo sắp theo ngày đo, mới nhất trước; mỗi dòng ghi người nhập và nơi nhập (class entry / child record). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| — | Dùng VAL-001, VAL-002 của US-001. | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record — Health › Growth |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Phần đầu hồ sơ trẻ | Component dùng chung | — | — | — | Ảnh, tên, mã trẻ, trạng thái, Centre / lớp, cảnh báo y tế. |
| Allergies & conditions · Growth | Chip chọn 1 | — | Growth | — | Mục con của tab Health. |
| + Add measurement | Nút chính | Theo quyền | — | VAL-001; VAL-002. | Nhập Term, Date measured, Height, Weight (FR-007). |
| Measurement history · n measurements | Text | — | — | — | Tổng số lần đo của trẻ. |
| Term / Date measured / Height (cm) / Weight (kg) | Cột | — | — | — | Ví dụ “Term 4 · 2026”; DD/MM/YYYY; số 1 chữ số thập phân. |
| Change since last term | Cột | — | Lần đo đầu tiên hiện “—” | — | Ví dụ “+1.5 cm · +0.5 kg”. |
| Recorded by | Cột | — | — | — | Người nhập, vai trò và nơi nhập (BR-008). |
| Edit · Delete | Liên kết | Theo quyền | — | — | Sửa hoặc xoá một lần đo (FR-008). |
| Delete this measurement? | Hộp xác nhận | — | — | — | Hiện tên trẻ, kỳ, chiều cao, cân nặng, ngày đo; Cancel · Delete (BR-007). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| AUDIT-002 | Mỗi lần xóa ghi số đo bị xoá, người xoá, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-013 | Centre Director mở hồ sơ một trẻ | nhập số đo cho riêng trẻ đó | số đo được lưu và hiện trong lịch sử đo của trẻ | FR-007; BR-006 |
| AC-014 | số đo Term 4 của Ethan nhập nhầm | giáo viên chọn Delete và xác nhận | số đo bị xoá, không còn hiện trên app phụ huynh; lịch sử ghi người xoá và thời điểm | FR-008; BR-007; AUDIT-002 |
| AC-015 | Ethan có số đo Term 3 (107,0 cm, 17,6 kg) và Term 4 (108,5 cm, 18,1 kg) | Centre Director mở hồ sơ Ethan, tab Health › Growth | dòng Term 4 ghi “+1.5 cm · +0.5 kg” và người nhập, ở trên dòng Term 3 | FR-009; BR-008 |

#### Dependencies (Phụ thuộc)

Hồ sơ trẻ (tab Health); US-001 (số đo đã lưu).

### 6.3 BBA-70: US-003 - Báo cáo hoàn thành kỳ đo

#### User Story

Là Cluster Head, tôi muốn xem lớp nào đã đo đủ trong kỳ để nhắc Centre còn thiếu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-010 | Báo cáo Height & weight completion theo Centre, lớp, kỳ đo; tìm, lọc, xuất Excel (BR-009). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở báo cáo Height & weight completion, chọn Centre và kỳ đo (FR-010).
2. Người dùng xuất Excel (FR-010).

#### Functional Flow - Alternative (Luồng thay thế)

1. Tìm theo tên Centre hoặc lớp (FR-010).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có kết quả: bảng trống.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-009 | Báo cáo chỉ có số trẻ, số trẻ đã đo, tỷ lệ hoàn thành; không có thống kê tăng trưởng. Người dùng chính: Centre Director, Admin, Cluster Head (BBA-1059 Q5). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-04 - Height & weight completion |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Height & weight completion | Tiêu đề màn hình | — | — | — | Tỉ lệ trẻ đã được đo trong kỳ theo Centre và lớp (BR-009). |
| Export (n) | Nút | Theo quyền | n = số dòng | — | Xuất danh sách đang lọc. |
| Search centre or class | Ô tìm kiếm | Không | Trống | — | Tìm theo tên Centre hoặc lớp. |
| Centre / Term | Danh sách chọn | Không | All centres / kỳ hiện tại | — | Lọc. |
| Centre, Class / Children / Measured / Completed | Cột | — | — | — | Completed = Measured / Children, phần trăm làm tròn số nguyên. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Báo cáo đọc số đo của US-001, US-002; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-016 | lớp N2 · Sunbeams đo 12 / 18 trẻ trong Term 4 | Cluster Head mở báo cáo completion | dòng N2 · Sunbeams hiện 18 trẻ, đã đo 12, hoàn thành 67% | FR-010; BR-009 |

#### Dependencies (Phụ thuộc)

US-001, US-002 (số đo); danh sách lớp.

### 6.4 BBA-70: US-004 - Nhắc nhập số đo

#### User Story

Là HQ Ops, tôi muốn hệ thống tự nhắc Centre nhập chiều cao, cân nặng mỗi term để không Centre nào quên.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-011 | Gửi nhắc nhập chiều cao, cân nặng theo kỳ đo (BR-010). |

#### Functional Flow - Main (Luồng chính)

1. Tới thời điểm nhắc, hệ thống gửi nhắc cho Centre (FR-011).
2. Màn nhập theo lớp hiện “Reminder sent to the centre on …” (FR-011).

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-010 | Nhắc gửi vào giữa tháng cuối mỗi term (tháng 3, 6, 9, 12) cho mọi brand, kể cả Brighton (BBA-529). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Height & weight — nhập theo lớp (dòng “Reminder sent…”) |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Reminder sent to the centre on … | Text | — | Ẩn nếu chưa gửi | — | Ngày gửi nhắc, DD/MM/YYYY (BR-010). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi lần nhắc lưu Centre, kỳ đo, thời điểm gửi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-017 | ngày 15/12/2026 | hệ thống chạy nhắc | Centre nhận nhắc nhập chiều cao, cân nặng; màn nhập hiện “Reminder sent to the centre on 15/12/2026” | FR-011; BR-010; DATA-002 |

#### Dependencies (Phụ thuộc)

Lịch term theo brand; dịch vụ thông báo.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Khoảng hợp lệ của chiều cao, cân nặng và số chữ số thập phân? Đơn vị cm, kg đã chốt (Q-71-05); file mẫu Taidii ghi số nguyên (94 cm, 13 kg). | HQ Ops | Trung bình |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Term (kỳ đo) | Một trong 4 term của năm học (1/1–31/12) theo lịch term của brand do HQ đặt; Centre đo chiều cao, cân nặng cho trẻ một lần mỗi term. |
| Measurement history | Danh sách mọi lần đo của một trẻ theo ngày đo, kèm người nhập. |
| Biểu đồ tăng trưởng | Biểu đồ so sánh chiều cao, cân nặng của trẻ với trẻ cùng tuổi, cùng giới tính, theo chuẩn Singapore (NHG Polyclinics) hoặc Malaysia (Child Health Record Book). |
| Cluster Head | Tên mới của District Manager, cho cả Singapore và Malaysia (BBA-524). |
