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

**Mức sẵn sàng:** Đặc tả các thông tin: số đo cả lớp (kèm nhắc nhập), số đo từng trẻ, báo cáo hoàn thành.

## 2. Mục tiêu và bối cảnh

Mỗi term, giáo viên đo chiều cao và cân nặng của trẻ trong lớp và ghi vào hệ thống một lần cho cả lớp, thay cho báo cáo "Quarterly Heights & Weight Report" đang giữ trên Taidii. dữ liệu cân đo cập nhật tức thời lên app phụ huynh;

Mục tiêu: giáo viên nhập xong một lớp trong một lần lưu; số đo có hiệu lực ngay sau khi lưu, không cần duyệt.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Nhập theo lớp và term; trẻ vắng và tạm nghỉ ở nhóm riêng. Lịch sử chỉnh sửa số đo. Cảnh báo số đo bất thường. Nhập cho một trẻ từ hồ sơ trẻ. Sửa, xoá số đo. Lịch sử đo trên hồ sơ trẻ. Nhắc nhập theo term. Báo cáo completion. | BMI. Biểu đồ tăng trưởng (thuộc Parents App, BBA-1059 Q1). Thống kê tăng trưởng trong báo cáo. Thiết bị đo kết nối tự động. Nhận xét dinh dưỡng, tư vấn sức khỏe. Danh sách dị ứng (BBA-69). Màn xem số đo trong Parents App (chức năng của Parents App). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ trong lớp / Centre được cấp. | Thêm, sửa, xoá số đo; xem lịch sử chỉnh sửa. |
| Report Viewer | Các Centre được cấp. | Xem báo cáo Height & weight completion. |
| System | Số đo của trẻ; lịch term của brand. | Tính tuổi, gửi nhắc, ghi lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

Mọi quyền xem và thao tác theo mô hình phân quyền theo vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Health & allergies** | Số đo cả lớp | Nhập, sửa số đo chiều cao, cân nặng của cả lớp theo term; trẻ vắng / tạm nghỉ ở nhóm riêng; lưu một lần; cảnh báo số đo bất thường; lịch sử chỉnh sửa; nhắc nhập giữa tháng cuối mỗi kỳ. | BBA-70: US-001 |
| **Health & allergies** | Số đo từng trẻ | Thêm, sửa, xoá số đo của một trẻ trên hồ sơ trẻ; lịch sử đo, lịch sử chỉnh sửa. | BBA-70: US-002 |
| **Health & allergies** | Báo cáo hoàn thành | Tỷ lệ trẻ đã đo theo Centre, lớp, term; lọc, xuất. | BBA-70: US-004 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-70: US-001 - Số đo cả lớp

#### User Story

Là giáo viên, tôi muốn nhập chiều cao và cân nặng của cả lớp trên một màn hình và lưu một lần, để không phải mở từng hồ sơ trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hiển thị danh sách số đo theo lớp và kỳ đo của Centre (BR-001, BR-002). |
| FR-002 | Nhập, sửa chiều cao, cân nặng của mọi trẻ trong một lớp và kỳ đo trên một màn hình (BR-003, BR-004, BR-005). |
| FR-003 | Lưu một lần số đo của cả lớp (BR-006, BR-007, BR-012). |
| FR-004 | Cảnh báo và không lưu khi chiều cao thấp hơn kỳ trước (BR-008). |
| FR-005 | Xem lịch sử chỉnh sửa số đo theo lớp, kỳ và trẻ (BR-010). |
| FR-006 | Nhắc Centre nhập chiều cao, cân nặng theo kỳ đo (BR-013). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Health & allergies › Growth; hệ thống hiển thị danh sách phiếu đo theo lớp và kỳ (FR-001).
2. Giáo viên chọn tên lớp trên một dòng, hoặc chọn Edit rồi chọn lớp và kỳ; màn "Edit class measurements" mở ra với số đo đã lưu điền sẵn (FR-002).
3. Giáo viên chọn ngày đo, nhập chiều cao, cân nặng và chọn Save changes (FR-003; VAL-001 đến VAL-004).
4. Hệ thống lưu, hiện "Saved n measurements." và quay lại danh sách (FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Nhập kỳ chưa có phiếu: chọn Edit, chọn lớp và kỳ đó; lưu lần đầu thì tạo phiếu mới (FR-002; BR-001).
2. Trẻ vắng hoặc tạm nghỉ: để trống, nhập bổ sung vào ngày khác trong cùng kỳ (FR-002; BR-005).
3. Đổi lớp, đổi kỳ hoặc chọn Cancel khi còn thay đổi chưa lưu: hệ thống hỏi "Discard unsaved measurements?"; đồng ý thì bỏ thay đổi (BR-004).
4. Chọn Change history: xem các lần thêm, sửa, xoá số đo; lọc theo lớp, kỳ, trẻ; chọn Back to class list để quay lại (FR-005).
5. Tới giữa tháng cuối của kỳ, hệ thống gửi nhắc cho Centre; màn Edit hiện "Reminder sent to the centre on …" sau dòng "x of y recorded" (FR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Có ít nhất một lỗi (chiều cao thấp hơn kỳ trước, chỉ nhập một trong hai số, ngày đo không hợp lệ hoặc sau hôm nay): không lưu số đo nào; các ô lỗi được đánh dấu để sửa (BR-006; VAL-001 đến VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Danh sách: mỗi phiếu đo là một dòng, ứng với một lớp và một kỳ; phiếu được tạo khi lưu số đo lần đầu cho lớp trong kỳ. Date là ngày tạo phiếu. Children measured là số trẻ có đủ chiều cao và cân nặng trong phiếu, mỗi trẻ tính một lần. Chọn tên lớp mở màn Edit của phiếu đó. |
| BR-002 | Kỳ đo lấy theo lịch term đã cấu hình cho brand. Số kỳ một lớp đo trong năm không ảnh hưởng chức năng: vd. Brighton Montessori đo theo học kỳ thì lớp chỉ có số đo ở 2 kỳ thay vì 4 (BBA-529). |
| BR-003 | Màn Edit chọn lớp và kỳ, kể cả kỳ chưa có số đo; số đo đã lưu của kỳ được điền sẵn; hiện "x of y recorded" (số trẻ đã có số đo / tổng số trẻ của lớp). |
| BR-004 | Rời màn Edit (đổi lớp, đổi kỳ, Cancel) khi còn thay đổi chưa lưu: hỏi "Discard unsaved measurements?" trước khi bỏ thay đổi. |
| BR-005 | Đối tượng: mọi trẻ của lớp, chia 2 nhóm Present today và Absent today / Temporary withdrawal; trẻ vắng / tạm nghỉ để trống được và nhập bổ sung trong cùng kỳ (BBA-1059 Q2). |
| BR-006 | Lưu: chỉ cần có một lỗi thì không lưu số đo nào; dòng để trống không phải lỗi và vẫn là chưa đo. Save changes chỉ bật khi có số đo thay đổi. Số đo không cần duyệt, có hiệu lực ngay (BR-CHF-026). |
| BR-007 | Ngày đo: mặc định ngày hiện tại; áp cho các dòng có số đo thay đổi trong lần lưu đó. |
| BR-008 | Chiều cao thấp hơn số đo kỳ trước của trẻ: cảnh báo và không lưu. Cân nặng không kiểm tra tăng / giảm vì thay đổi nhiều. |
| BR-009 | Mỗi trẻ một số đo cho mỗi kỳ. Số đo dùng chung cho danh sách lớp (US-001) và hồ sơ trẻ (US-002): sửa ở nơi nào thì nơi kia hiển thị số mới; số cũ giữ trong lịch sử chỉnh sửa. |
| BR-010 | Lịch sử chỉnh sửa dùng chung cho lớp và hồ sơ trẻ: mỗi lần thêm, sửa, xoá ghi một dòng gồm thời điểm, người thực hiện và vai trò, trẻ, kỳ, thao tác (Added / Updated / Deleted), nơi nhập (Class entry / Child record), ngày đo và số đo trước và sau. Lịch sử của lớp lọc theo lớp, kỳ, trẻ; mới nhất trước. |
| BR-011 | Quyền: thêm, sửa, xoá số đo là một quyền chung (BBA-1059 Q3), cấp theo vai trò — hiện BBA giao cho Centre Director, Admin và mọi giáo viên; người dùng chỉ thao tác trên trẻ trong phạm vi dữ liệu của mình (Q-71-10). Áp cho US-001 và US-002. |
| BR-012 | Dữ liệu cân đo được cập nhật tức thời lên app phụ huynh (BBA-1059 Q4). |
| BR-013 | Nhắc nhập gửi vào giữa tháng cuối mỗi kỳ (tháng 3, 6, 9, 12) cho mọi brand, kể cả Brighton (BBA-529). Người nhận và kênh chờ OQ-01. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chiều cao thấp hơn số đo kỳ trước của trẻ. | Không lưu; ô chiều cao hiện "Height is lower than the last measurement. Check before saving." |
| VAL-002 | Chỉ nhập chiều cao hoặc chỉ nhập cân nặng. | Không lưu; hiện "Enter both height and weight." |
| VAL-003 | Ngày đo trống hoặc không đúng định dạng. | Không lưu; hiện "Enter a valid measurement date." |
| VAL-004 | Ngày đo sau hôm nay. | Không lưu; hiện "The measurement date cannot be in the future." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Height & weight — danh sách |  |
| Height & weight — Edit class measurements |  |
| Height & weight — Change history |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Danh sách** | | | | | |
| Height & weight | Tiêu đề màn hình | — | — | — | Kèm tên Centre đang xem. |
| Change history | Nút | — | — | — | Mở lịch sử chỉnh sửa (FR-005). |
| Edit | Nút chính | Theo quyền | — | — | Mở màn nhập, sửa số đo, kể cả kỳ chưa có dữ liệu (FR-002). |
| Allergies & conditions · Growth | Tab | — | Growth | — | Tab trong mục Health & allergies. |
| Date | Cột | — | — | — | Ngày tạo phiếu đo của lớp trong kỳ, DD/MM/YYYY (BR-001). |
| Class | Cột, liên kết | — | — | — | Chọn tên lớp để mở Edit của phiếu. |
| Term | Cột | — | — | — | Kỳ và năm, vd. "Term 4 · 2026". |
| Children measured | Cột | — | — | — | Số trẻ có đủ chiều cao và cân nặng, mỗi trẻ tính một lần. |
| **Edit class measurements** | | | | | |
| Edit class measurements | Tiêu đề | — | — | — | Kèm tên Centre; nút Cancel, Save changes. |
| Class · Term | Danh sách chọn | Có | Lớp, kỳ của dòng đã chọn | — | Đổi lớp / kỳ thì hiện danh sách trẻ và số đo đã lưu tương ứng (BR-003, BR-004). |
| Date measured | Chọn ngày | Có | Hôm nay | VAL-003; VAL-004. | DD/MM/YYYY; áp cho các dòng có số đo thay đổi (BR-007). |
| x of y recorded | Text | — | — | — | Số trẻ đã có số đo / tổng số trẻ của lớp trong kỳ; kèm "Reminder sent to the centre on …" (DD/MM/YYYY) khi đã gửi nhắc; ẩn nếu chưa gửi (BR-013). |
| Present today / Absent today · Temporary withdrawal | Nhóm | — | — | — | 2 nhóm trẻ (BR-005). |
| Child · Age · Last measured | Cột chỉ đọc | — | — | — | Họ tên, tuổi dạng "4y 9m"; Last measured là ngày cập nhật số đo gần nhất của trẻ trong kỳ ("—" khi chưa đo). |
| Height (cm) · Weight (kg) | Ô nhập số, 1 chữ số thập phân | Khi nhập dòng | Số đã lưu trong kỳ, nếu có | VAL-001; VAL-002. | Nhập đủ hai số cho mỗi dòng cần lưu; để trống thì không lưu cho trẻ đó. |
| Save changes | Nút chính | — | Chỉ bật khi có số đo thay đổi | VAL-001 đến VAL-004. | Có lỗi thì không lưu (BR-006). |
| Cancel | Nút phụ | — | — | — | Bỏ thay đổi, quay lại danh sách (BR-004). |
| Discard unsaved measurements? | Hộp xác nhận | — | — | — | Hiện khi rời màn Edit còn thay đổi chưa lưu (BR-004). |
| Saved n measurements. | Thông báo (toast) | — | Tự ẩn | — | Báo lưu thành công kèm số trẻ vừa lưu. |
| **Change history** | | | | | |
| Change history | Tiêu đề | — | — | — | Hiện lớp · kỳ đang xem; nút Back to class list. |
| Class · Term · Child | Danh sách chọn | Không | Lớp, kỳ đang xem; All children | — | Lọc lịch sử (BR-010). |
| Changed at / by | Cột | — | Mới nhất trước | — | Thời điểm, người thực hiện, vai trò. |
| Child / term | Cột | — | — | — | Trẻ và kỳ đo. |
| Action / source | Cột | — | — | — | Added / Updated / Deleted; Class entry / Child record. |
| Before · After | Cột | — | Thêm mới: Before hiện "—" | — | Số đo và ngày đo trước và sau, vd. "108.0 cm · 18.1 kg" và DD/MM/YYYY. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi số đo lưu: trẻ, kỳ đo, ngày đo, chiều cao (cm), cân nặng (kg), người nhập, nơi nhập (Class entry / Child record), thời điểm nhập. Một bản ghi dùng chung cho US-001 và US-002. |
| DATA-002 | Mỗi lần nhắc lưu Centre, kỳ đo, thời điểm gửi. |
| AUDIT-001 | Mỗi lần thêm, sửa số đo ghi một dòng lịch sử chỉnh sửa theo BR-010. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | phiếu N2 · Sunbeams Term 4 · 2026 tạo ngày 17/11/2026, 2 trẻ đã đo | giáo viên mở Growth | danh sách có dòng Date 17/11/2026, Class N2 · Sunbeams, Term 4 · 2026, Children measured 2 | FR-001; BR-001 |
| AC-002 | danh sách có dòng N2 · Sunbeams · Term 4 · 2026 | giáo viên chọn tên lớp trên dòng đó | màn Edit mở ra với lớp N2 · Sunbeams, kỳ Term 4 · 2026, số đo đã lưu điền sẵn, "2 of 4 recorded" | FR-002; BR-001; BR-003 |
| AC-003 | lớp N1 · Butterflies chưa có số đo Term 3 · 2026 | giáo viên chọn Edit, chọn N1 · Butterflies, Term 3 · 2026 | danh sách trẻ hiện với ô trống, nhập được | FR-002; BR-003 |
| AC-004 | lớp Brighton Montessori chỉ đo Term 2 và Term 4 · 2026 | giáo viên mở Growth | danh sách chỉ có 2 phiếu của lớp đó; không có cảnh báo thiếu kỳ | FR-001; BR-002 |
| AC-005 | lớp Nursery 1 có 18 trẻ, 17 trẻ có mặt | giáo viên nhập số đo hợp lệ cho 17 trẻ và chọn Save changes | 17 số đo được lưu cùng lúc, không cần duyệt; hiện "Saved 17 measurements."; trẻ còn lại vẫn chưa đo | FR-003; BR-006 |
| AC-006 | Sofia đang tạm nghỉ | giáo viên mở Edit class measurements | Sofia ở nhóm "Absent today · Temporary withdrawal", ô nhập để trống được | FR-002; BR-005 |
| AC-007 | giáo viên nhập đúng 16 dòng và 1 dòng chỉ có chiều cao | chọn Save changes | không số đo nào được lưu; dòng lỗi hiện "Enter both height and weight." | BR-006; VAL-002 |
| AC-008 | kỳ trước trẻ cao 98 cm | giáo viên nhập 96 cm và chọn Save changes | không lưu; ô chiều cao hiện "Height is lower than the last measurement. Check before saving." | FR-004; BR-008; VAL-001 |
| AC-009 | kỳ trước trẻ nặng 16 kg | giáo viên nhập 15,5 kg và chiều cao không thấp hơn kỳ trước | số đo được lưu; không có cảnh báo về cân nặng | BR-008 |
| AC-010 | ô Date measured để trống | giáo viên chọn Save changes | không lưu, hiện "Enter a valid measurement date." | VAL-003 |
| AC-011 | ngày đo chọn ngày mai | giáo viên chọn Save changes | không lưu, hiện "The measurement date cannot be in the future." | VAL-004; BR-007 |
| AC-012 | giáo viên đã nhập số đo nhưng chưa lưu | giáo viên đổi sang lớp khác | hệ thống hỏi "Discard unsaved measurements?"; chọn huỷ thì giữ nguyên số đã nhập | BR-004 |
| AC-013 | Ethan có số đo Term 4 là 108,0 cm | giáo viên sửa thành 108,5 cm và lưu | số mới thay số cũ, hồ sơ Ethan cũng hiện 108,5 cm; Change history có dòng Updated · Class entry, Before "108.0 cm · 18.1 kg", After "108.5 cm · 18.1 kg" | FR-005; BR-009; BR-010; AUDIT-001 |
| AC-014 | Change history của N2 · Sunbeams Term 4 có dòng của 2 trẻ | giáo viên chọn Child = Ethan Lim | chỉ còn dòng của Ethan | FR-005; BR-010 |
| AC-015 | số đo vừa được lưu | hệ thống hoàn tất lưu | dữ liệu cân đo được cập nhật tức thời lên app phụ huynh | FR-003; BR-012 |
| AC-016 | Teacher lớp N2 · Sunbeams | mở Growth | chỉ thấy và chọn được lớp trong phạm vi của mình | BR-011 |
| AC-017 | ngày 15/12/2026 | hệ thống chạy nhắc | Centre nhận nhắc nhập chiều cao, cân nặng; màn Edit class measurements hiện "Reminder sent to the centre on 15/12/2026" | FR-006; BR-013; DATA-002 |

#### Dependencies (Phụ thuộc)

Danh sách lớp và trẻ (gồm trẻ vắng và tạm nghỉ); lịch term theo brand; dịch vụ thông báo.

### 6.2 BBA-70: US-002 - Số đo từng trẻ

#### User Story

Là Centre Director, tôi muốn thêm, sửa, xoá số đo của một trẻ trên hồ sơ trẻ để ghi bổ sung hoặc sửa số nhập nhầm.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-007 | Thêm số đo cho một trẻ từ hồ sơ trẻ (BR-009, BR-014). |
| FR-008 | Sửa, xoá một số đo của trẻ (BR-009, BR-011, BR-015). |
| FR-009 | Hiển thị lịch sử đo và lịch sử chỉnh sửa số đo của trẻ (BR-010, BR-016). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở hồ sơ trẻ, tab Health › Growth; hệ thống hiển thị Measurement history (FR-009).
2. Người dùng chọn "+ Add measurement", chọn Term, ngày đo, nhập chiều cao, cân nặng và chọn Save measurement (FR-007; VAL-001 đến VAL-004).
3. Hệ thống lưu; số đo hiện trên hồ sơ trẻ và trên danh sách lớp của kỳ đó (US-001); lịch sử chỉnh sửa ghi nơi nhập Child record (BR-009, BR-010).

#### Functional Flow - Alternative (Luồng thay thế)

1. Kỳ đã chọn đã có số đo: form hiện "This term already has a measurement. Saving changes will update that record."; lưu thì số mới thay số cũ (FR-007; BR-009).
2. Sửa một lần đo: chọn Edit, sửa và chọn Save measurement (FR-008).
3. Xoá một lần đo: chọn Delete, xác nhận Delete measurement; hiện "Measurement deleted. The previous values are in Change history." (FR-008; BR-015).
4. Chọn Change history: xem mọi lần thêm, sửa, xoá số đo của trẻ; chọn Back to child record để quay lại (FR-009; BR-010).
5. Chọn Cancel: không lưu.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Chỉ nhập một trong hai số, chiều cao thấp hơn kỳ trước, ngày đo không hợp lệ hoặc sau hôm nay: không lưu (VAL-001 đến VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-014 | Từ hồ sơ trẻ nhập được số đo cho bất kỳ kỳ đo nào, cho trẻ ở mọi độ tuổi. Áp cùng kiểm tra với nhập theo lớp: phải có đủ chiều cao và cân nặng; chiều cao không thấp hơn kỳ trước (BR-008); ngày đo tối đa là hôm nay. |
| BR-015 | Xoá cần xác nhận; sau khi xoá, số đo không còn hiện trên hồ sơ trẻ, danh sách lớp và app phụ huynh; lịch sử chỉnh sửa vẫn giữ số đo trước khi xoá (BBA-1059 Q3). |
| BR-016 | Measurement history sắp theo ngày đo, mới nhất trước; mỗi kỳ một số đo hiện hành; mỗi dòng ghi người nhập, vai trò và nơi nhập (Class entry / Child record). Lịch sử chỉnh sửa của trẻ gồm mọi kỳ và cả hai nơi nhập; thay đổi từ hồ sơ trẻ cũng hiện trong lịch sử của lớp (BR-010). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| — | Dùng VAL-001 đến VAL-004 của US-001. | — |

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
| Recorded by | Cột | — | — | — | Người nhập, vai trò và nơi nhập (BR-016). |
| Actions: Edit · Delete | Liên kết | Theo quyền | — | — | Sửa hoặc xoá một lần đo (FR-008). |
| **Add / Edit measurement** | | | | | |
| Add measurement / Edit measurement | Tiêu đề | — | — | — | Kèm tên trẻ. |
| Term | Danh sách chọn | Có | Kỳ hiện tại | — | Kỳ đã có số đo thì hiện "This term already has a measurement. Saving changes will update that record." |
| Date measured | Chọn ngày | Có | Hôm nay | VAL-003; VAL-004. | DD/MM/YYYY. |
| Height (cm) · Weight (kg) | Ô nhập số, 1 chữ số thập phân | Có | Edit: số đo đang có | VAL-001; VAL-002. | Nhập đủ hai số. |
| Save measurement · Cancel | Nút chính · nút phụ | — | — | — | Lưu (ghi lịch sử chỉnh sửa) hoặc huỷ. |
| **Delete measurement** | | | | | |
| Delete this measurement? | Hộp xác nhận | — | — | — | Hiện tên trẻ · kỳ · chiều cao · cân nặng · ngày đo; "The measurement will be removed from the child record. Change history keeps a copy." (BR-015). |
| Cancel · Delete measurement | Nút phụ · nút chính | — | — | — | Huỷ hoặc xác nhận xoá. |
| **Change history** | | | | | |
| Change history | Bảng | — | Mới nhất trước | — | Cùng cột với lịch sử của lớp (US-001), gồm mọi kỳ và cả hai nơi nhập; nút Back to child record (BR-010, BR-016). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| AUDIT-002 | Mỗi lần thêm, sửa, xoá từ hồ sơ trẻ ghi một dòng lịch sử chỉnh sửa theo BR-010, nơi nhập Child record; dòng này hiện cả trong lịch sử của trẻ và lịch sử của lớp. Xoá giữ số đo bị xoá ở cột Before. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-018 | Centre Director mở hồ sơ Ethan (lớp N2 · Sunbeams) | thêm số đo Term 4 · 2026 cho Ethan | số đo hiện trong Measurement history của Ethan và trên Edit class measurements của N2 · Sunbeams, Term 4 · 2026; Recorded by ghi Child record | FR-007; BR-009; BR-016 |
| AC-019 | Ethan đã có số đo Term 4 · 2026 | Centre Director chọn + Add measurement, Term 4 · 2026 | form hiện "This term already has a measurement. Saving changes will update that record."; lưu thì số mới thay số cũ ở cả hồ sơ trẻ và danh sách lớp | FR-007; BR-009 |
| AC-020 | Centre Director chỉ nhập chiều cao | chọn Save measurement | không lưu, hiện "Enter both height and weight." | BR-014; VAL-002 |
| AC-021 | Term 3 Ethan cao 107,0 cm | Centre Director thêm Term 4 với 106,0 cm | không lưu, hiện "Height is lower than the last measurement. Check before saving." | BR-014; VAL-001 |
| AC-022 | Centre Director sửa số đo Term 4 của Ethan trên hồ sơ trẻ | lưu thành công | Change history của Ethan và Change history của lớp N2 · Sunbeams Term 4 đều có dòng Updated · Child record với Before và After | FR-008; BR-010; AUDIT-002 |
| AC-023 | số đo Term 4 của Ethan nhập nhầm | giáo viên chọn Delete và xác nhận Delete measurement | số đo bị xoá khỏi hồ sơ trẻ, danh sách lớp và app phụ huynh; hiện "Measurement deleted. The previous values are in Change history."; Change history có dòng Deleted giữ số đo cũ | FR-008; BR-015; AUDIT-002 |
| AC-024 | Ethan có số đo Term 3 (107,0 cm, 17,6 kg) và Term 4 (108,5 cm, 18,1 kg) | Centre Director mở hồ sơ Ethan, tab Health › Growth | dòng Term 4 ghi "+1.5 cm · +0.5 kg" và người nhập, ở trên dòng Term 3 | FR-009; BR-016 |

#### Dependencies (Phụ thuộc)

Hồ sơ trẻ (tab Health); US-001 (cùng dữ liệu số đo và lịch sử chỉnh sửa).

### 6.3 BBA-70: US-004 - Báo cáo hoàn thành kỳ đo

#### User Story

Là Cluster Head, tôi muốn xem lớp nào đã đo đủ trong kỳ để nhắc Centre còn thiếu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-010 | Báo cáo Height & weight completion theo Centre, lớp, kỳ đo; tìm, lọc, xuất Excel (BR-017). |

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
| BR-017 | Báo cáo chỉ có số trẻ, số trẻ đã đo, tỷ lệ hoàn thành; không có thống kê tăng trưởng. Người dùng chính: Centre Director, Admin, Cluster Head (BBA-1059 Q5). |

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
| Height & weight completion | Tiêu đề màn hình | — | — | — | Phụ đề "Children measured this term, by centre and class." (BR-017). |
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
| AC-025 | lớp N2 · Sunbeams đo 12 / 18 trẻ trong Term 4 | Cluster Head mở báo cáo completion | dòng N2 · Sunbeams hiện 18 trẻ, đã đo 12, hoàn thành 67% | FR-010; BR-017 |

#### Dependencies (Phụ thuộc)

US-001, US-002 (số đo); danh sách lớp.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Nhắc nhập gửi cho ai (Centre Director, Admin, giáo viên lớp) và qua kênh nào? | Centre Director / HQ Ops | Trung bình |  |
| OQ-02 | "Health observations" (Parent App Requirements mục 19b) thuộc tính năng nào, có trong BBA-70 không? | HQ Ops | Thấp |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Term (kỳ đo) | Một trong 4 term của năm học (1/1–31/12) theo lịch term của brand do HQ đặt; Centre đo chiều cao, cân nặng cho trẻ một lần mỗi term. |
| Measurement history | Danh sách mọi lần đo của một trẻ theo ngày đo, kèm người nhập. |
| Change history | Lịch sử mọi lần thêm, sửa, xoá số đo, kèm số đo trước và sau. |
| Class entry / Child record | Nơi nhập số đo: màn sửa cả lớp / hồ sơ trẻ. |
| BMI | Chỉ số khối cơ thể; không dùng trong Phase 1 (SRS Children & Families §1.2). |
| Cluster Head | Tên mới của District Manager, cho cả Singapore và Malaysia (BBA-524). |

## 9. Tài liệu tham khảo

Số trang của SRS tính theo bản Word gốc khi xuất PDF. Tệp của BBA là tệp đính kèm trên Plane.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | BBA-SMS-SRS-Children-and-Families-v0.1 | §1.1 In scope; §1.2 Not in Phase 1 (BMI) | 3 | Mục 3 — phạm vi, bỏ BMI. |
| 2 | BBA-SMS-SRS-Children-and-Families-v0.1 | §3 P7 Height and weight | 5 | US-001. |
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.3 Health & allergies (Record height and weight, Bulk record height and weight, View growth chart) | 7 | US-001, US-002. |
| 4 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Business rules › Health and allergies (BR-CHF-026) | 9 | BR-006 — ghi trực tiếp, không cần duyệt. |
| 5 | BBA-SMS-SRS-Children-and-Families-v0.1 | §8 Acceptance criteria (AC-CHF-011 Bulk height and weight) | 12 | AC-005. |
| 6 | BBA-SMS-SRS-Parents-App-v0.1 | §4.1 Health (View height and weight, View measurement history) | 9 | BR-012 — dữ liệu cập nhật tức thời lên app phụ huynh. |
| 7 | Plane — BBA-1059 "BBA input: Height and weight – growth chart, absent children, deleting, parent view, HQ report" | Q1 chuẩn biểu đồ; Q2 trẻ vắng / tạm nghỉ; Q3 xoá số đo, một quyền chung (CD, Admin, mọi giáo viên); Q4 phụ huynh thấy ngay; Q5 báo cáo completion (CD, Admin, Cluster Head) | — | BR-005; BR-011; BR-012; BR-015; BR-017. |
| 8 | Plane — BBA-1059, tệp đính kèm "Taidii - Center Staff Role permissions.xlsx" | Sheet "Center Staff Role", dòng 14 "Update Height and Weight" | — | BR-011. |
| 9 | Plane — BBA-1059, tệp đính kèm "Parent App Requirements Provided to DotB (30 July 2026).pdf" | Mục 19 Child Health Records | 3–4 | OQ-02. |
| 11 | Plane — BBA-529 "BBA input: Height and weight records today" | Brighton đo theo học kỳ; nhắc giữa tháng cuối quý cho mọi brand | — | BR-002; BR-013. |
| 12 | Plane — BBA-529, tệp đính kèm "Student_quarterly_height_weight_2026-sample.xlsx" | Quarterly Heights & Weight Report (Brighton Montessori Frankel, Class N2) | — | Mục 2 — mẫu báo cáo Taidii. |
| 13 | Plane — BBA-489, tệp đính kèm "Centre Terms Setup.xlsx" | Sheet "Term Setup" (ngày bắt đầu Term 1–4 năm 2027 theo brand) | — | BR-002. |
| 14 | Plane — BBA-524 "BBA input: Approval matrix" | District Manager đổi tên thành Cluster Head | — | Mục 2; BR-017. |
| 15 | BBA_SMS_S4 — Tổng hợp câu hỏi phản hồi, sheet "Tổng hợp" | Đã chốt: Q-71-02, Q-71-03, Q-71-06, Q-71-07, Q-71-10 · Một phần: Q-71-05, Q-71-08 · DOTB quyết định: Q-71-09 · Chưa phản hồi: Q-71-04, Q-71-11, Q-71-12 | — | BR-002; BR-006; BR-011. |
| 16 | Plane — dự án BBA Phase 1, ticket BBA-70 (WBS 3.1.3.03) | Growth – termly height & weight entry by class | — | Phạm vi tính năng. |
