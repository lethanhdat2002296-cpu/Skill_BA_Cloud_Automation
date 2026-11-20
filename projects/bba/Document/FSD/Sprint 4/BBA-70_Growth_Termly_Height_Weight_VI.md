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
| Phiên bản | 0.2 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 19/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 19/11/2026 | Business Analysis | Cập nhật theo wireframe: danh sách lớp chỉ xem, Edit class measurements, Change history cho lớp và hồ sơ trẻ; bỏ Year view; thêm kiểm tra ngày đo; báo cáo completion có Total, Export Excel. | HaiNguyen |

**Mức sẵn sàng:** Đặc tả các thông tin: số đo cả lớp, số đo từng trẻ, biểu đồ tăng trưởng, báo cáo hoàn thành, nhắc nhập.

## 2. Mục tiêu và bối cảnh

Mỗi term, giáo viên đo chiều cao và cân nặng của trẻ trong lớp và ghi vào hệ thống một lần cho cả lớp, thay cho báo cáo "Quarterly Heights & Weight Report" đang giữ trên Taidii. Hệ thống vẽ biểu đồ tăng trưởng theo chuẩn Singapore / Malaysia; dữ liệu cân đo cập nhật tức thời lên app phụ huynh; Centre Director, Admin và Cluster Head theo dõi lớp nào đã đo đủ, vì nhiều Centre quên nhập khiến portfolio bị trống.

Mục tiêu: giáo viên nhập xong một lớp trong một lần lưu; số đo có hiệu lực ngay sau khi lưu, không cần duyệt.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Nhập theo lớp và term; trẻ vắng và tạm nghỉ ở nhóm riêng. Lịch sử chỉnh sửa số đo. Biểu đồ tăng trưởng. Cảnh báo số đo bất thường. Nhập cho một trẻ từ hồ sơ trẻ. Sửa, xoá số đo. Biểu đồ và lịch sử đo trên hồ sơ trẻ. Nhắc nhập theo term. Báo cáo completion. | BMI. Thống kê tăng trưởng trong báo cáo. Thiết bị đo kết nối tự động. Nhận xét dinh dưỡng, tư vấn sức khỏe. Danh sách dị ứng (BBA-69). Màn xem số đo trong Parents App (chức năng của Parents App). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ trong lớp / Centre được cấp. | Thêm, sửa, xoá số đo; xem lịch sử chỉnh sửa. |
| Report Viewer | Các Centre được cấp. | Xem báo cáo Height & weight completion. |
| System | Số đo của trẻ; lịch term của brand. | Tính tuổi và vị trí trên biểu đồ, gửi nhắc, ghi lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

Mọi quyền xem và thao tác theo mô hình phân quyền theo vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Health & allergies** | Số đo cả lớp | Nhập, sửa số đo chiều cao, cân nặng của cả lớp theo term; trẻ vắng / tạm nghỉ ở nhóm riêng; lưu một lần; cảnh báo số đo bất thường; lịch sử chỉnh sửa. | BBA-70: US-001 |
| **Health & allergies** | Số đo từng trẻ | Thêm, sửa, xoá số đo của một trẻ trên hồ sơ trẻ; lịch sử đo, lịch sử chỉnh sửa. | BBA-70: US-002 |
| **Health & allergies** | Biểu đồ tăng trưởng | Biểu đồ chiều cao, cân nặng theo tuổi của từng trẻ. | BBA-70: US-003 |
| **Health & allergies** | Báo cáo hoàn thành | Tỷ lệ trẻ đã đo theo Centre, lớp, term; lọc, xuất. | BBA-70: US-004 |
| **Health & allergies** | Nhắc nhập | Nhắc nhập số đo giữa tháng cuối mỗi term. | BBA-70: US-005 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-70: US-001 - Số đo cả lớp

#### User Story

Là giáo viên, tôi muốn nhập chiều cao và cân nặng của cả lớp trên một màn hình và lưu một lần, để không phải mở từng hồ sơ trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hiển thị số đo của cả lớp theo Centre, lớp và kỳ đo: số đo, trạng thái của từng trẻ và số trẻ đã đo (BR-001, BR-003). |
| FR-002 | Sửa cả lớp: nhập, sửa chiều cao, cân nặng của mọi trẻ trong lớp trên một màn hình, trẻ chia 2 nhóm có mặt hôm nay; vắng hoặc tạm nghỉ (BR-002, BR-003). |
| FR-003 | Lưu một lần số đo của cả lớp (BR-004, BR-009). |
| FR-004 | Số đo đã lưu trong kỳ được điền sẵn; sửa và lưu thì số mới thay số cũ (BR-005). |
| FR-005 | Cảnh báo số đo bất thường trước khi lưu (BR-006). |
| FR-006 | Xem lịch sử chỉnh sửa số đo của lớp trong kỳ đang xem, lọc theo trẻ (BR-008). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Health & allergies › Growth, chọn Centre, lớp và kỳ đo; hệ thống hiển thị số đo và trạng thái của từng trẻ (FR-001).
2. Giáo viên chọn Edit; màn "Edit class measurements" mở ra với số đo đã lưu điền sẵn (FR-002, FR-004).
3. Giáo viên chọn ngày đo, nhập chiều cao, cân nặng và chọn Save changes (FR-003; VAL-001 đến VAL-005).
4. Hệ thống lưu các dòng hợp lệ, hiện "Saved n measurements." và quay lại danh sách lớp (FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ vắng hoặc tạm nghỉ: để trống, nhập bổ sung vào ngày khác trong cùng kỳ (FR-002; BR-003).
2. Chọn Cancel: bỏ các thay đổi vừa nhập, quay lại danh sách lớp.
3. Chọn Change history: xem các lần thêm, sửa, xoá số đo trong kỳ; lọc theo trẻ; chọn Back to class list để quay lại (FR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Số đo ngoài khoảng hợp lệ hoặc chỉ nhập một trong hai số: dòng đó không được lưu, giữ lại để sửa và lưu tiếp (VAL-001, VAL-002).
2. Ngày đo không hợp lệ, sau hôm nay hoặc trước ngày sinh của trẻ: không lưu (VAL-003, VAL-004, VAL-005).
3. Chiều cao thấp hơn lần đo trước: không lưu (BR-006).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Kỳ đo theo lịch term do Người dùng cấu hình cho từng brand (BBA-489); Centre không sửa. Brighton Montessori đo theo học kỳ, tức 2 trong 4 term (BBA-529; term nào chờ OQ-03). |
| BR-002 | Ngày đo: mặc định ngày hiện tại; áp cho các dòng có số đo thay đổi trong lần lưu đó. |
| BR-003 | Đối tượng: mọi trẻ của lớp, kể cả trẻ vắng và tạm nghỉ; trẻ vắng / tạm nghỉ để trống được và nhập bổ sung trong cùng kỳ (BBA-1059 Q2). |
| BR-004 | Lưu cả lớp: chỉ lưu dòng có đủ chiều cao và cân nặng; dòng để trống vẫn là "Not recorded yet"; dòng lỗi không chặn các dòng hợp lệ và được giữ lại để sửa (Q-71-09). Save changes chỉ bật khi có số đo thay đổi. Số đo không cần duyệt, có hiệu lực ngay (BR-CHF-026). |
| BR-005 | Mỗi trẻ một số đo cho mỗi kỳ; nhập lại trong cùng kỳ thì số mới thay số cũ, số cũ giữ trong lịch sử chỉnh sửa. |
| BR-006 | Chiều cao thấp hơn lần đo trước: hiện cảnh báo "Height is lower than the last measurement. Check before saving."; người dùng không lưu được. |
| BR-007 | Quyền: thêm, sửa, xoá số đo là một quyền chung (BBA-1059 Q3), cấp theo vai trò — hiện BBA giao cho Centre Director, Admin và mọi giáo viên; người dùng chỉ thao tác trên trẻ trong phạm vi dữ liệu của mình (Q-71-10). Áp cho US-001 và US-002. |
| BR-008 | Lịch sử chỉnh sửa: mỗi lần thêm, sửa, xoá số đo ghi một dòng gồm thời điểm, người thực hiện và vai trò, trẻ, kỳ đo, thao tác (Added / Updated / Deleted), nơi nhập (Class entry / Child record), ngày đo và số đo trước và sau. Khi xoá, cột trước vẫn giữ số đo cũ. Lịch sử của lớp chỉ gồm kỳ đang xem, lọc được theo trẻ; lịch sử của trẻ gồm mọi kỳ và cả hai nơi nhập. Lịch sử mới nhất trước. |
| BR-009 | Dữ liệu cân đo được cập nhật tức thời lên app phụ huynh (BBA-1059 Q4). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chiều cao hoặc cân nặng ngoài khoảng hợp lệ (khoảng chờ OQ-01). | Dòng đó không được lưu; ô bị đánh dấu với chữ "Check this value." |
| VAL-002 | Chỉ nhập chiều cao hoặc chỉ nhập cân nặng. | Dòng đó không được lưu; hiện "Enter both height and weight." |
| VAL-003 | Ngày đo trống hoặc không đúng định dạng. | Không lưu; hiện "Enter a valid measurement date." |
| VAL-004 | Ngày đo sau hôm nay. | Không lưu; hiện "The measurement date cannot be in the future." |
| VAL-005 | Ngày đo trước ngày sinh của trẻ. | Không lưu; hiện "Check the measurement date. It is before the child's date of birth." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Height & weight — danh sách lớp |  |
| Height & weight — Edit class measurements |  |
| Height & weight — Change history |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Danh sách lớp** | | | | | |
| Height & weight | Tiêu đề màn hình | — | — | — | Phụ đề "Term measurements by class." |
| Change history | Nút | — | — | — | Mở lịch sử chỉnh sửa của lớp trong kỳ đang xem (FR-006). |
| Edit | Nút chính | Theo quyền | — | — | Mở màn sửa số đo cho mọi trẻ của lớp trong kỳ đang xem (FR-002). |
| Allergies & conditions · Growth | Tab | — | Growth | — | Tab trong mục Health & allergies. |
| Centre · Class · Term | Danh sách chọn | Có | Centre của người dùng; kỳ hiện tại, vd. "Term 4 · 2026" | — | Kỳ theo lịch term của brand; Brighton dùng học kỳ (BR-001). |
| x of y recorded | Text | — | — | — | Số trẻ đã có số đo trên tổng số trẻ của lớp trong kỳ. |
| Present today / Absent today · Temporary withdrawal | Nhóm | — | — | — | 2 nhóm trẻ (BR-003). |
| Child · Age | Cột | — | — | — | Họ tên và tuổi của trẻ, dạng "4y 9m". |
| Date measured | Cột | — | Chưa đo hiện "—" | — | Ngày đo đã lưu, DD/MM/YYYY. |
| Height (cm) · Weight (kg) | Cột chỉ đọc | — | Chưa đo hiện "—" | — | Số đo đã lưu trong kỳ. |
| Status | Cột | — | — | — | Recorded / Not recorded yet. |
| **Edit class measurements** | | | | | |
| Edit class measurements | Tiêu đề | — | — | — | Hiện Centre · lớp · kỳ đang sửa. |
| Date measured | Chọn ngày | Có | Hôm nay | VAL-003; VAL-004; VAL-005. | DD/MM/YYYY; áp cho các dòng có số đo thay đổi (BR-002). |
| Child · Age · Last measured | Cột chỉ đọc | — | — | — | Họ tên, tuổi, ngày đo đã lưu của từng trẻ. |
| Height (cm) · Weight (kg) | Ô nhập số, 1 chữ số thập phân | Khi nhập dòng | Số đã lưu trong kỳ, nếu có | VAL-001; VAL-002. | Nhập đủ hai số cho mỗi dòng cần lưu; để trống thì không lưu cho trẻ đó (FR-004). |
| Present today / Absent today · Temporary withdrawal | Nhóm | — | — | — | Trẻ vắng / tạm nghỉ nhập bổ sung được trong cùng kỳ. |
| Save changes | Nút chính | — | Chỉ bật khi có số đo thay đổi | VAL-001 đến VAL-005. | Lưu các dòng hợp lệ; dòng lỗi giữ lại để sửa (FR-003; BR-004). |
| Cancel | Nút phụ | — | — | — | Bỏ thay đổi, quay lại danh sách lớp. |
| Saved n measurements. | Thông báo (toast) | — | Tự ẩn | — | Báo lưu thành công kèm số trẻ vừa lưu. |
| **Change history** | | | | | |
| Change history | Tiêu đề | — | — | — | Hiện lớp · kỳ đang xem; nút Back to class list. |
| Child | Danh sách chọn | Không | All children | — | Lọc theo trẻ trong kỳ đang xem. |
| Changed at / by | Cột | — | Mới nhất trước | — | Thời điểm, người thực hiện, vai trò (BR-008). |
| Child / term | Cột | — | — | — | Trẻ và kỳ đo. |
| Action / source | Cột | — | — | — | Added / Updated / Deleted; Class entry / Child record. |
| Before · After | Cột | — | Thêm mới: Before hiện "—" | — | Số đo và ngày đo trước và sau, dạng "108.0 cm · 18.1 kg" và DD/MM/YYYY. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi số đo lưu: trẻ, kỳ đo, ngày đo, chiều cao (cm), cân nặng (kg), vị trí trên biểu đồ, chuẩn biểu đồ dùng, người nhập, nơi nhập (class entry / child record), thời điểm nhập. |
| AUDIT-001 | Mỗi lần thêm, sửa số đo ghi một dòng lịch sử chỉnh sửa theo BR-008. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp N2 · Sunbeams Term 4 · 2026 có 4 trẻ, 2 trẻ đã đo | giáo viên mở Growth, chọn lớp và kỳ | danh sách hiện "2 of 4 recorded"; trẻ đã đo có ngày đo, số đo, Status Recorded; trẻ chưa đo hiện "—" và Not recorded yet | FR-001; BR-003 |
| AC-002 | lớp Nursery 1 có 18 trẻ, 17 trẻ có mặt | giáo viên chọn Edit, nhập số đo cho 17 trẻ và chọn Save changes | 17 số đo được lưu cùng lúc, không cần duyệt; hiện "Saved 17 measurements."; trẻ còn lại ở nhóm "Absent today · Temporary withdrawal" với Not recorded yet | FR-002; FR-003; BR-004 |
| AC-003 | Sofia đang tạm nghỉ | giáo viên mở Edit class measurements | Sofia ở nhóm "Absent today · Temporary withdrawal", ô nhập để trống được | FR-002; BR-003 |
| AC-004 | Ethan đã có số đo Term 4 (108,0 cm, 18,1 kg) | giáo viên mở Edit | ô của Ethan điền sẵn 108.0 và 18.1; Save changes chưa bật tới khi có số thay đổi | FR-004; BR-004 |
| AC-005 | giáo viên nhập 1000 cm | chọn Save changes | dòng đó không được lưu, ô hiện "Check this value."; các dòng hợp lệ vẫn được lưu | VAL-001; BR-004 |
| AC-006 | giáo viên chỉ nhập chiều cao | chọn Save changes | dòng đó không được lưu, hiện "Enter both height and weight." | VAL-002 |
| AC-007 | ô Date measured để trống | giáo viên chọn Save changes | không lưu, hiện "Enter a valid measurement date." | VAL-003 |
| AC-008 | ngày đo chọn ngày mai | chọn Save changes | không lưu, hiện "The measurement date cannot be in the future." | VAL-004; BR-002 |
| AC-009 | trẻ sinh 14/02/2022 | giáo viên chọn ngày đo 01/01/2022 và lưu | không lưu, hiện "Check the measurement date. It is before the child's date of birth." | VAL-005 |
| AC-010 | lần trước trẻ cao 98 cm | giáo viên nhập 96 cm và chọn Save changes | hiện cảnh báo "Height is lower than the last measurement. Check before saving."; số đo không được lưu | FR-005; BR-006 |
| AC-011 | Ethan có số đo Term 4 là 108,0 cm | giáo viên sửa thành 108,5 cm và lưu | số mới thay số cũ; Change history có dòng Updated · Class entry, Before "108.0 cm · 18.1 kg", After "108.5 cm · 18.1 kg", người sửa và thời điểm | FR-004; FR-006; BR-005; BR-008; AUDIT-001 |
| AC-012 | Change history của lớp N2 · Sunbeams Term 4 có dòng của 2 trẻ | giáo viên chọn Child = Ethan Lim | chỉ còn dòng của Ethan | FR-006; BR-008 |
| AC-013 | số đo vừa được lưu | hệ thống hoàn tất lưu | dữ liệu cân đo được cập nhật tức thời lên app phụ huynh | FR-003; BR-009 |
| AC-014 | Centre thuộc brand Brighton Montessori, lịch 2027 bắt đầu Term 2 ngày 01/04/2027 | giáo viên mở danh sách kỳ đo ngày 10/04/2027 | danh sách có Term 1 đến Term 4 của 2027, mặc định Term 2 | FR-001; BR-001 |
| AC-015 | Teacher lớp N2 · Sunbeams | mở Growth | chỉ chọn được lớp trong phạm vi của mình | BR-007 |

#### Dependencies (Phụ thuộc)

Danh sách lớp và trẻ (gồm trẻ vắng và tạm nghỉ); ngày sinh của trẻ; lịch term theo brand.

### 6.2 BBA-70: US-002 - Số đo từng trẻ

#### User Story

Là Centre Director, tôi muốn thêm, sửa, xoá số đo của một trẻ trên hồ sơ trẻ để ghi bổ sung hoặc sửa số nhập nhầm.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-007 | Thêm số đo cho một trẻ từ hồ sơ trẻ (BR-010). |
| FR-008 | Sửa, xoá một số đo của trẻ (BR-007, BR-011). |
| FR-009 | Hiển thị lịch sử đo và lịch sử chỉnh sửa số đo của trẻ (BR-008, BR-012). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở hồ sơ trẻ, tab Health › Growth; hệ thống hiển thị biểu đồ và Measurement history (FR-009).
2. Người dùng chọn "+ Add measurement", chọn Term, ngày đo, nhập chiều cao, cân nặng và chọn Save measurement (FR-007; VAL-001 đến VAL-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Kỳ đã chọn đã có số đo: form hiện "This term already has a measurement. Saving changes will update that record."; lưu thì số mới thay số cũ (FR-007; BR-005).
2. Sửa một lần đo: chọn Edit, sửa và chọn Save measurement (FR-008).
3. Xoá một lần đo: chọn Delete, xác nhận Delete measurement; hiện "Measurement deleted. The previous values are in Change history." (FR-008; BR-011).
4. Chọn Change history: xem mọi lần thêm, sửa, xoá số đo của trẻ; chọn Back to child record để quay lại (FR-009; BR-008).
5. Chọn Cancel: không lưu.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Số đo hoặc ngày đo không hợp lệ: không lưu (VAL-001 đến VAL-005).
2. Chiều cao thấp hơn lần đo trước: không lưu (BR-006).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-010 | Từ hồ sơ trẻ nhập được số đo cho bất kỳ kỳ đo nào, cho trẻ ở mọi độ tuổi; ngày đo tối đa là hôm nay. |
| BR-011 | Xoá cần xác nhận; sau khi xoá, số đo không còn hiện trên hồ sơ trẻ và app phụ huynh; lịch sử chỉnh sửa vẫn giữ số đo trước khi xoá (BBA-1059 Q3). |
| BR-012 | Measurement history sắp theo ngày đo, mới nhất trước; mỗi kỳ một số đo hiện hành; mỗi dòng ghi người nhập, vai trò và nơi nhập (Class entry / Child record). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| — | Dùng VAL-001 đến VAL-005 của US-001. | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record — Health › Growth |  |
| Child record — Add / Edit measurement |  |
| Child record — Delete measurement |  |
| Child record — Change history |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Tab Health › Growth** | | | | | |
| Phần đầu hồ sơ trẻ | Component dùng chung | — | — | — | Ảnh, tên, mã trẻ, trạng thái, Centre / lớp, cảnh báo y tế. |
| Allergies & conditions · Growth | Chip chọn 1 | — | Growth | — | Mục con của tab Health. |
| Growth | Tiêu đề | — | — | — | Phụ đề "Measurements by term." |
| Change history | Nút | — | — | — | Mở lịch sử chỉnh sửa của trẻ (FR-009). |
| + Add measurement | Nút chính | Theo quyền | — | — | Mở form thêm số đo (FR-007). |
| Measurement history · n measurements | Text | — | — | — | Tổng số lần đo của trẻ. |
| Term / Date measured / Height (cm) / Weight (kg) | Cột | — | — | — | Vd. "Term 4 · 2026"; DD/MM/YYYY; số 1 chữ số thập phân. |
| Change since last term | Cột | — | Lần đo đầu tiên hiện "—" | — | Vd. "+1.5 cm · +0.5 kg". |
| Recorded by | Cột | — | — | — | Người nhập, vai trò và nơi nhập (BR-012). |
| Actions: Edit · Delete | Liên kết | Theo quyền | — | — | Sửa hoặc xoá một lần đo (FR-008). |
| **Add / Edit measurement** | | | | | |
| Add measurement / Edit measurement | Tiêu đề | — | — | — | Kèm tên trẻ. |
| Term | Danh sách chọn | Có | Kỳ hiện tại | — | Kỳ đã có số đo thì hiện "This term already has a measurement. Saving changes will update that record." |
| Date measured | Chọn ngày | Có | Hôm nay | VAL-003; VAL-004; VAL-005. | DD/MM/YYYY. |
| Height (cm) · Weight (kg) | Ô nhập số, 1 chữ số thập phân | Có | Edit: số đo đang có | VAL-001; VAL-002. | Nhập đủ hai số. |
| Save measurement · Cancel | Nút chính · nút phụ | — | — | — | Lưu (ghi lịch sử chỉnh sửa) hoặc huỷ. |
| **Delete measurement** | | | | | |
| Delete this measurement? | Hộp xác nhận | — | — | — | Hiện tên trẻ · kỳ · chiều cao · cân nặng · ngày đo; "The measurement will be removed from the child record. Change history keeps a copy." (BR-011). |
| Cancel · Delete measurement | Nút phụ · nút chính | — | — | — | Huỷ hoặc xác nhận xoá. |
| **Change history** | | | | | |
| Change history | Bảng | — | Mới nhất trước | — | Cùng cột với lịch sử của lớp (US-001), gồm mọi kỳ và cả hai nơi nhập; nút Back to child record (BR-008). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| AUDIT-002 | Mỗi lần xoá ghi một dòng lịch sử chỉnh sửa theo BR-008, giữ số đo bị xoá, người xoá, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-016 | Centre Director mở hồ sơ một trẻ | thêm số đo cho riêng trẻ đó | số đo được lưu và hiện trong Measurement history, Recorded by ghi "Child record" | FR-007; BR-010; BR-012 |
| AC-017 | Ethan đã có số đo Term 4 · 2026 | Centre Director chọn + Add measurement, Term 4 · 2026 | form hiện "This term already has a measurement. Saving changes will update that record."; lưu thì số mới thay số cũ | FR-007; BR-005 |
| AC-018 | số đo Term 4 của Ethan nhập nhầm | giáo viên chọn Delete và xác nhận Delete measurement | số đo bị xoá khỏi hồ sơ trẻ và app phụ huynh; hiện "Measurement deleted. The previous values are in Change history."; Change history có dòng Deleted giữ số đo cũ | FR-008; BR-011; AUDIT-002 |
| AC-019 | Ethan có số đo Term 3 (107,0 cm, 17,6 kg) và Term 4 (108,5 cm, 18,1 kg) | Centre Director mở hồ sơ Ethan, tab Health › Growth | dòng Term 4 ghi "+1.5 cm · +0.5 kg" và người nhập, ở trên dòng Term 3 | FR-009; BR-012 |
| AC-020 | Ethan có số đo nhập từ cả danh sách lớp và hồ sơ trẻ ở nhiều kỳ | Centre Director chọn Change history trên hồ sơ Ethan | lịch sử có mọi kỳ và cả hai nơi nhập (Class entry, Child record), mới nhất trước | FR-009; BR-008 |

#### Dependencies (Phụ thuộc)

Hồ sơ trẻ (tab Health); US-001 (số đo đã lưu).

### 6.3 BBA-70: US-003 - Biểu đồ tăng trưởng

#### User Story

Là Centre Director, tôi muốn xem biểu đồ chiều cao, cân nặng theo tuổi của trẻ để biết trẻ phát triển so với chuẩn.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-010 | Hiển thị biểu đồ chiều cao, cân nặng theo tuổi của trẻ trên tab Health › Growth (BR-013). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Health › Growth của trẻ; hệ thống hiển thị biểu đồ chiều cao (FR-010).
2. Người dùng chuyển sang biểu đồ cân nặng (FR-010).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ chưa có số đo: biểu đồ trống, hiện "No measurements yet."

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ thiếu ngày sinh hoặc giới tính: không vẽ được vị trí, hiện "Add date of birth and gender to see the chart."

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-013 | Biểu đồ theo tuổi và giới tính. Singapore: nghiên cứu nhân trắc của Singapore National Healthcare Group Polyclinics. Malaysia: Child Health Record Book (BBA-1059 Q1). Vị trí do hệ thống tính, người dùng không sửa. Không tính BMI. Đường percentile chờ OQ-04. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-03 - Child record — Health › Growth |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Height for age · Height / Weight | Biểu đồ đường, chip chọn 1 | — | Height | — | Số đo đã lưu của trẻ theo tháng tuổi (trục ngang: tháng tuổi; trục dọc: cm / kg) (BR-013). |
| Ghi chú chuẩn tham chiếu | Text phụ | — | — | — | Vd. "Measured values · Singapore."; nguồn đường chuẩn theo quốc gia của Centre (BR-013; OQ-04). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Bảng chuẩn biểu đồ theo quốc gia, giới tính, tháng tuổi (Singapore NHG Polyclinics; Malaysia Child Health Record Book). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-021 | Ethan (Centre Singapore, nam, 4 tuổi 9 tháng) cao 108,5 cm, nặng 18,1 kg | số đo được lưu và Centre Director mở tab Growth | biểu đồ của Ethan có điểm mới theo chuẩn Singapore; không có BMI | FR-010; BR-013; DATA-002 |
| AC-022 | Mia chưa có số đo | người dùng mở tab Growth của Mia | biểu đồ trống, hiện "No measurements yet." | FR-010 |

#### Dependencies (Phụ thuộc)

Hồ sơ trẻ (ngày sinh, giới tính); chuẩn biểu đồ Singapore / Malaysia.

### 6.4 BBA-70: US-004 - Báo cáo hoàn thành kỳ đo

#### User Story

Là Cluster Head, tôi muốn xem lớp nào đã đo đủ trong kỳ để nhắc Centre còn thiếu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-011 | Báo cáo Height & weight completion theo Centre, lớp, kỳ đo; tìm, lọc, xuất Excel (BR-014). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở báo cáo Height & weight completion, chọn Centre và kỳ đo (FR-011).
2. Người dùng xuất Excel (FR-011).

#### Functional Flow - Alternative (Luồng thay thế)

1. Tìm theo tên Centre hoặc lớp (FR-011).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có kết quả: bảng trống.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-014 | Báo cáo chỉ có số trẻ, số trẻ đã đo, tỷ lệ hoàn thành; không có thống kê tăng trưởng. Người dùng chính: Centre Director, Admin, Cluster Head (BBA-1059 Q5). |

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
| Height & weight completion | Tiêu đề màn hình | — | — | — | Phụ đề "Children measured this term, by centre and class." (BR-014). |
| Export Excel (n) | Nút | Theo quyền | n = số dòng | — | Xuất Excel danh sách đang lọc. |
| Search centre or class | Ô tìm kiếm | Không | Trống | — | Tìm theo tên Centre hoặc lớp. |
| Centre / Term | Danh sách chọn | Không | All centres / kỳ hiện tại | — | Lọc. |
| Total | Số | — | — | — | Số dòng kết quả. |
| Centre, Class / Children / Measured / Completed | Cột | — | — | — | Completed = Measured / Children, phần trăm làm tròn số nguyên. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Báo cáo đọc số đo của US-001, US-002; không lưu dữ liệu riêng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-023 | lớp N2 · Sunbeams đo 12 / 18 trẻ trong Term 4 | Cluster Head mở báo cáo completion | dòng N2 · Sunbeams hiện 18 trẻ, đã đo 12, hoàn thành 67% | FR-011; BR-014 |

#### Dependencies (Phụ thuộc)

US-001, US-002 (số đo); danh sách lớp.

### 6.5 BBA-70: US-005 - Nhắc nhập số đo

#### User Story

Là HQ Ops, tôi muốn hệ thống tự nhắc Centre nhập chiều cao, cân nặng mỗi term để không Centre nào quên.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-012 | Gửi nhắc nhập chiều cao, cân nặng theo kỳ đo (BR-015). |

#### Functional Flow - Main (Luồng chính)

1. Tới thời điểm nhắc, hệ thống gửi nhắc cho Centre (FR-012).
2. Màn nhập theo lớp hiện "Reminder sent to the centre on …" (FR-012).

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-015 | Nhắc gửi vào giữa tháng cuối mỗi term (tháng 3, 6, 9, 12) cho mọi brand, kể cả Brighton (BBA-529). Người nhận và kênh chờ OQ-02. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Height & weight — danh sách lớp (dòng "Reminder sent…") |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Reminder sent to the centre on … | Text | — | Ẩn nếu chưa gửi | — | Ngày gửi nhắc, DD/MM/YYYY (BR-015). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi lần nhắc lưu Centre, kỳ đo, thời điểm gửi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-024 | ngày 15/12/2026 | hệ thống chạy nhắc | Centre nhận nhắc nhập chiều cao, cân nặng; màn nhập hiện "Reminder sent to the centre on 15/12/2026" | FR-012; BR-015; DATA-003 |

#### Dependencies (Phụ thuộc)

Lịch term theo brand; dịch vụ thông báo.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Khoảng hợp lệ của chiều cao, cân nặng và số chữ số thập phân? Đơn vị cm, kg đã chốt (Q-71-05); file mẫu Taidii ghi số nguyên (94 cm, 13 kg). | HQ Ops | Trung bình |  |
| OQ-02 | Nhắc nhập gửi cho ai (Centre Director, Admin, giáo viên lớp) và qua kênh nào? | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Brighton Montessori đo theo học kỳ nhưng dùng Term 1–4: đo ở term nào? Báo cáo completion có bỏ qua các term Brighton không đo không? | HQ Ops | Trung bình |  |
| OQ-04 | Biểu đồ có hiện đường percentile không? Q-71-02 (09/11) bỏ BMI và percentile; SRS Children & Families §4 mục 1.3 ghi "against percentile curves"; Taidii vẽ 3 đường 3rd / 50th / 97th; BBA-1059 Q1 gửi chuẩn Singapore / Malaysia. | HQ Ops | Cao |  |
| OQ-05 | "Health observations" (Parent App Requirements mục 19b) thuộc tính năng nào, có trong BBA-70 không? | HQ Ops | Thấp |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Term (kỳ đo) | Một trong 4 term của năm học (1/1–31/12) theo lịch term của brand do HQ đặt; Centre đo chiều cao, cân nặng cho trẻ một lần mỗi term. |
| Measurement history | Danh sách mọi lần đo của một trẻ theo ngày đo, kèm người nhập. |
| Change history | Lịch sử mọi lần thêm, sửa, xoá số đo, kèm số đo trước và sau. |
| Class entry / Child record | Nơi nhập số đo: màn sửa cả lớp / hồ sơ trẻ. |
| Biểu đồ tăng trưởng | Biểu đồ so sánh chiều cao, cân nặng của trẻ với trẻ cùng tuổi, cùng giới tính, theo chuẩn Singapore (NHG Polyclinics) hoặc Malaysia (Child Health Record Book). |
| BMI | Chỉ số khối cơ thể; không dùng trong Phase 1 (SRS Children & Families §1.2). |
| Cluster Head | Tên mới của District Manager, cho cả Singapore và Malaysia (BBA-524). |

## 9. Tài liệu tham khảo

Số trang của SRS tính theo bản Word gốc khi xuất PDF. Tệp của BBA là tệp đính kèm trên Plane.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | BBA-SMS-SRS-Children-and-Families-v0.1 | §1.1 In scope; §1.2 Not in Phase 1 (BMI) | 3 | Mục 3 — phạm vi, bỏ BMI. |
| 2 | BBA-SMS-SRS-Children-and-Families-v0.1 | §3 P7 Height and weight | 5 | US-001, US-003. |
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.3 Health & allergies (Record height and weight, Bulk record height and weight, View growth chart) | 7 | US-001, US-002, US-003; OQ-04. |
| 4 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Business rules › Health and allergies (BR-CHF-026) | 9 | BR-004 — ghi trực tiếp, không cần duyệt. |
| 5 | BBA-SMS-SRS-Children-and-Families-v0.1 | §8 Acceptance criteria (AC-CHF-011 Bulk height and weight) | 12 | AC-002. |
| 6 | BBA-SMS-SRS-Parents-App-v0.1 | §4.1 Health (View height and weight, View measurement history) | 9 | BR-009 — dữ liệu cập nhật tức thời lên app phụ huynh. |
| 7 | Plane — BBA-1059 "BBA input: Height and weight – growth chart, absent children, deleting, parent view, HQ report" | Q1 chuẩn biểu đồ; Q2 trẻ vắng / tạm nghỉ; Q3 xoá số đo, một quyền chung (CD, Admin, mọi giáo viên); Q4 phụ huynh thấy ngay; Q5 báo cáo completion (CD, Admin, Cluster Head) | — | BR-003; BR-007; BR-009; BR-011; BR-013; BR-014. |
| 8 | Plane — BBA-1059, tệp đính kèm "Taidii - Center Staff Role permissions.xlsx" | Sheet "Center Staff Role", dòng 14 "Update Height and Weight" | — | BR-007. |
| 9 | Plane — BBA-1059, tệp đính kèm "Parent App Requirements Provided to DotB (30 July 2026).pdf" | Mục 19 Child Health Records | 3–4 | OQ-05. |
| 10 | Plane — BBA-1059, ảnh Taidii Parents App "Height & Weight" | Biểu đồ chiều cao theo tuổi, 3 đường 3rd / 50th / 97th, chuẩn WHO | — | BR-013; OQ-04. |
| 11 | Plane — BBA-529 "BBA input: Height and weight records today" | Brighton đo theo học kỳ; nhắc giữa tháng cuối quý cho mọi brand | — | BR-001; BR-015; OQ-03. |
| 12 | Plane — BBA-529, tệp đính kèm "Student_quarterly_height_weight_2026-sample.xlsx" | Quarterly Heights & Weight Report (Brighton Montessori Frankel, Class N2) | — | OQ-01; OQ-03. |
| 13 | Plane — BBA-489, tệp đính kèm "Centre Terms Setup.xlsx" | Sheet "Term Setup" (ngày bắt đầu Term 1–4 năm 2027 theo brand) | — | BR-001. |
| 14 | Plane — BBA-524 "BBA input: Approval matrix" | District Manager đổi tên thành Cluster Head | — | Mục 2; BR-014. |
| 15 | BBA_SMS_S4 — Tổng hợp câu hỏi phản hồi, sheet "Tổng hợp" | Đã chốt: Q-71-02, Q-71-03, Q-71-06, Q-71-07, Q-71-10 · Một phần: Q-71-05, Q-71-08 · DOTB quyết định: Q-71-09 · Chưa phản hồi: Q-71-04, Q-71-11, Q-71-12 | — | BR-001; BR-004; BR-007; OQ-01; OQ-04. |
| 16 | Plane — dự án BBA Phase 1, ticket BBA-70 (WBS 3.1.3.03) | Growth – termly height & weight entry by class | — | Phạm vi tính năng. |
