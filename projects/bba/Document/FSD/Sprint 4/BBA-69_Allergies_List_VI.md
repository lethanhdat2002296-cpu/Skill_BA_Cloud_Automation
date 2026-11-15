# Allergies list (most severe first) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Health & allergies |
| Tính năng | Allergies list (most severe first) |
| Mã ticket | BBA-69 |
| Mã WBS | 3.1.3.02 |
| Mã tài liệu | FRD-BBA-69 |
| Sprint | 4 |
| Phiên bản | 0.2 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 15/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả danh sách sức khoẻ theo Centre / lớp với các cột theo prototype BeeHive (From the family, Note from staff, Vaccination, Updated by the family), thứ tự theo mức độ, lọc, in cho bếp, xuất file và quyền xem.

## 2. Mục tiêu và bối cảnh

Giáo viên và bếp cần một danh sách dị ứng của cả lớp hoặc cả Centre, trẻ bị nặng nhất ở trên cùng, để chuẩn bị bữa ăn và xử lý đúng khi trẻ có phản ứng. Nội dung lấy từ Medical Care Assessment do phụ huynh khai và Centre Director / Senior Staff xác nhận; nhân viên không gõ lại. Trên form của BBA, danh sách này gọi là "Medical Overview / Medical Health Alert List".

Mục tiêu đo được: danh sách hiển thị 100% trẻ đang đi học có dị ứng, theo đúng thứ tự mức độ; bản in cho bếp luôn ghi thời điểm in.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách sức khoẻ theo Centre và lớp (dị ứng, bệnh, tiền sử trong cùng một bảng), trẻ dị ứng nặng nhất lên đầu. Các cột: Child, Class, Type, From the family, Note from staff, Vaccination, Updated by the family. Dòng cuối cho trẻ chưa khai thông tin sức khoẻ. Tìm kiếm, lọc, in cho bếp, xuất file. Quyền xem theo vai trò. | Phụ huynh nhập và sửa Medical Care Assessment (Parents App); quy trình đánh giá và đánh giá lại 6 tháng (BBA-68). Cảnh báo đỏ trên hồ sơ trẻ và các danh sách khác (BBA-68). Biểu đồ tăng trưởng (BBA-70). Khai báo và ghi nhận cho trẻ uống thuốc. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ có thông tin sức khoẻ trong phạm vi vai trò và phạm vi dữ liệu hiện có (lớp hoặc Centre). | Xem, lọc, in cho bếp và xuất danh sách khi vai trò được cấp quyền xem chi tiết y tế. |
| System | Medical Care Assessment đã xác nhận của trẻ. | Sắp xếp theo mức độ, tính hạn đánh giá lại, ghi thời điểm in. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi dữ liệu được phép. | Không thấy và không thực hiện được thao tác bị giới hạn; không thay đổi dữ liệu. |

Mọi quyền xem và thao tác theo mô hình phân quyền theo vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng; hệ thống không lưu nhật ký in / xuất (BBA-1058 Q2).

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Children & families › Health & allergies | Danh sách dị ứng theo Centre / lớp (Medical Health Alert List), in cho bếp, xuất file. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Danh sách dị ứng, trẻ nặng nhất lên đầu

#### User Story

Là giáo viên, tôi muốn xem và in danh sách dị ứng của lớp mình, trẻ bị nặng nhất ở trên cùng, để tôi và bếp biết ngay trẻ nào cần tránh món gì và xử lý ra sao khi trẻ có phản ứng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Danh sách có một dòng cho mỗi trẻ có thông tin sức khoẻ (dị ứng, bệnh, tiền sử) với các cột: Child (ảnh hoặc chữ viết tắt và họ tên), Class, Type (Food, Environmental, Medication, Insect, Medical condition, Medical history), From the family (nguyên văn phụ huynh khai trong Medical Care Assessment — chất gây dị ứng, triệu chứng, cách xử trí — bản đã được Centre xác nhận), Note from staff, Vaccination, Updated by the family. Các cột Child, Class, Type, Vaccination, Updated by the family sắp xếp được (prototype BeeHive — wireframe 15/11/2026). |
| FR-002 | Thứ tự mặc định: trẻ có mức dị ứng nặng nhất ở trên cùng (Severe — tương ứng "Life Threatening" trên form của BBA — rồi Moderate, rồi Mild, rồi bệnh và tiền sử); cùng mức thì xếp theo lớp, rồi theo tên trẻ. Mức độ lấy từ Medical Care Assessment, không hiển thị thành cột riêng; dị ứng chưa chọn mức độ được xếp cùng nhóm Severe. |
| FR-003 | Trẻ chỉ có bệnh hoặc tiền sử (không có dị ứng) nằm chung bảng với Type Medical condition hoặc Medical history; không có phần riêng (thay cho phần "Other conditions and diet" trước đây). |
| FR-004 | Tìm theo tên trẻ; lọc theo Centre, Class, Type, Vaccination và Updated (khoảng ngày phụ huynh cập nhật); các bộ lọc dùng kết hợp được; Total là số trẻ khớp tìm kiếm và bộ lọc. |
| FR-005 | Bộ lọc mặc định: Centre là Centre của người dùng, Class là All classes; danh sách chỉ gồm trẻ trong phạm vi dữ liệu của người dùng. |
| FR-007 | "Print for the kitchen" in theo bộ lọc đang chọn: tiêu đề "Allergies — {phạm vi}" (tên Centre, tên lớp hoặc "All my centres"), số trẻ, ngày in (ví dụ "Printed 24/11/2026"); cột Child, Class, Allergies (nội dung From the family); chỉ in trẻ có Type Food, Environmental, Medication, Insect; không có ảnh trẻ, không có chân trang. |
| FR-008 | "Export (n)" xuất danh sách theo bộ lọc đang chọn ra Excel; n là số trẻ đang hiển thị. Hệ thống không lưu nhật ký in / xuất. |
| FR-009 | Chọn tên trẻ mở tab Health trong hồ sơ trẻ. |
| FR-010 | Danh sách chỉ gồm trẻ đang đi học; trẻ đang tạm nghỉ, đã thôi học hoặc đã tốt nghiệp không có trong danh sách. |
| FR-011 | Trẻ mà phụ huynh chưa ký đồng ý cho hiện tên và ảnh trên danh sách y tế (Medical Care Assessment Checklist) không có trong danh sách và bản in. |
| FR-012 | Trẻ chưa khai Medical Care Assessment được phân biệt với trẻ đã khai không có dị ứng: dòng của trẻ luôn ở cuối danh sách, ô From the family và Note from staff gộp lại hiện câu thông báo và "Contact the family"; dòng ẩn khi lớp đang lọc không có trẻ nào chưa khai. Trẻ chưa sinh không nằm trong nhóm này (Q-70-09). |
| FR-014 | Khi phụ huynh sửa thông tin sức khoẻ trong Parents App, danh sách và bản in giữ thông tin đã được xác nhận gần nhất; cột Updated by the family hiện nhãn "Awaiting assessment" cho tới khi CD / Admin hoàn tất đánh giá (BBA-1058 Q1). |
| FR-015 | Cột Vaccination hiện tình trạng tiêm chủng của trẻ: Up to date (nhãn viền liền), Not up to date hoặc Not provided (nhãn viền đứt) (wireframe 15/11/2026; nguồn dữ liệu chờ OQ-10). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Children & families › Health & allergies; danh sách mặc định lọc theo lớp của mình (FR-005).
2. Hệ thống hiển thị trẻ có thông tin sức khoẻ, trẻ dị ứng nặng nhất lên đầu, trẻ chưa khai ở cuối (FR-001, FR-002, FR-012).
3. Giáo viên chọn "Print for the kitchen" và đưa bản in cho bếp (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Centre Director lọc toàn Centre theo Type hoặc Vaccination để rà soát (FR-004, FR-015).
2. Centre Director, School Admin hoặc giáo viên xuất danh sách ra Excel (FR-008).
3. Người dùng chọn tên trẻ để xem đủ Health record (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có trẻ nào: hiện thông báo trống (VAL-001).
2. Vai trò không được xem chi tiết y tế: không mở được danh sách (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Phụ huynh khai thông tin dị ứng (Medical Care Assessment); Centre Director hoặc Senior Staff kiểm tra và xác nhận (Appendix 1 tr. 3, BBA-1058 Q1). Danh sách chỉ đọc; nhân viên chỉ thêm "Note from staff" ở tab Health. |
| BR-002 | Trẻ nặng nhất luôn ở trên cùng; dị ứng chưa chọn mức độ được coi như Severe. |
| BR-003 | Bản in luôn ghi ngày giờ in, để bếp biết bản nào là bản mới nhất. |
| BR-004 | Người dùng có quyền xem chi tiết y tế (Authorised User) được xem, in và xuất danh sách; không lưu nhật ký in / xuất (BBA-1058 Q2). |
| BR-005 | Một trẻ không bị giới hạn số dị ứng hoặc bệnh (Q-70-02). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có trẻ nào. | Hiện "No children with allergies match these filters."; nút in và xuất file bị mờ. |
| VAL-002 | Người dùng không có quyền xem chi tiết y tế mở danh sách. | Không có mục Health & allergies trong menu; mở bằng đường dẫn thì hiện "You do not have access to medical details." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Allergies & conditions (Medical Health Alert List) |  |
| SCR-02 - Print for the kitchen |  |



#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **SCR-01 — Allergies & conditions (Medical Health Alert List)** | | | | | |
| Breadcrumb | Đường dẫn | — | Health & allergies › Allergies & conditions | — | Mục menu "Health & allergies" được tô sáng. |
| Allergies & conditions | Tiêu đề màn hình | — | — | — | Tên màn hình = Medical Health Alert List; dòng mô tả: dữ liệu lấy từ Medical Care Assessment của từng trẻ, đã được Centre xác nhận. |
| Export (n) | Nút | Theo quyền | n = số trẻ đang hiển thị | VAL-001. | Xuất danh sách đang lọc (FR-008). |
| Print for the kitchen | Nút chính | Theo quyền | — | VAL-001. | Mở bản in theo bộ lọc đang chọn (FR-007; SCR-02). |
| Allergies & conditions · Growth | Tab | — | Allergies & conditions | — | Badge = số trẻ; tab Growth là BBA-70. |
| Search child | Ô tìm kiếm | Không | Trống | — | Tìm theo tên trẻ. |
| Total | Số | — | — | — | Số trẻ khớp tìm kiếm và bộ lọc. |
| Centre | Bộ lọc | Không | Centre của người dùng | — | FR-005. |
| Class | Bộ lọc | Không | All classes | — | Chọn một lớp thì ô lọc có viền nhấn. |
| Type | Bộ lọc | Không | All | — | Lọc theo cột Type. |
| Vaccination | Bộ lọc | Không | Any | — | Lọc theo cột Vaccination. |
| Updated | Bộ lọc | Không | Any time | — | Lọc theo khoảng ngày của cột Updated by the family. |
| Child | Cột | — | — | — | Avatar (ảnh hoặc chữ viết tắt) và họ tên; sắp xếp được; chọn tên mở tab Health (FR-009). |
| Class | Cột | — | — | — | Level · tên lớp hiện tại; sắp xếp được. |
| Type | Cột | — | — | — | Food, Environmental, Medication, Insect, Medical condition, Medical history; sắp xếp được. |
| From the family | Cột | — | — | — | Nguyên văn phụ huynh khai trong Medical Care Assessment (chất gây dị ứng, triệu chứng, cách xử trí…); hiển thị bản đã được Centre xác nhận (BR-001). |
| Note from staff | Cột | — | "—" khi không có | — | Ghi chú nội bộ của Centre. |
| Vaccination | Cột (nhãn) | — | — | — | Tình trạng tiêm chủng: Up to date — nhãn viền liền; Not up to date / Not provided — nhãn viền đứt; sắp xếp được. |
| Updated by the family | Cột | — | — | — | Lần cuối phụ huynh cập nhật (DD/MM/YYYY HH:mm); sắp xếp được; bản cập nhật chưa được đánh giá có nhãn "Awaiting assessment" bên dưới (FR-014). |
| Dòng trẻ chưa khai thông tin | Dòng cuối bảng | Khi có | — | — | Trẻ chưa điền Medical Care Assessment, luôn ở cuối danh sách; ô From the family và Note from staff gộp lại, hiện câu thông báo và "Contact the family"; ẩn khi lớp đang lọc không có trẻ nào chưa khai (FR-012). |
| Pager | Phân trang | — | 20 dòng / trang | — | "1–n of n", chọn số dòng mỗi trang. |
| **SCR-02 — Print for the kitchen** | | | | | |
| Allergies — {phạm vi} | Tiêu đề bản in | — | — | — | Phạm vi đang lọc khi bấm in: tên Centre, tên lớp, hoặc "All my centres" nếu người dùng xem nhiều Centre. |
| n children | Text | — | — | — | Số trẻ trên bản in, dưới tiêu đề. |
| Printed … | Text | — | Ngày in | — | Căn phải, cùng hàng với số trẻ; bên dưới là đường kẻ đậm ngăn phần đầu với bảng (BR-003). |
| Child | Cột in | — | — | — | Họ tên in đậm. |
| Class | Cột in | — | — | — | Level · tên lớp. |
| Allergies | Cột in | — | — | — | Nội dung cột From the family; chỉ trẻ có Type là Food, Environmental, Medication, Insect. |
| Kiểu bảng in | Định dạng | — | — | — | Không kẻ dọc; kẻ đậm dưới tiêu đề cột, kẻ mảnh giữa các dòng; không có ảnh trẻ, không có chân trang. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Danh sách đọc từ Medical Care Assessment đã xác nhận: loại (Type), nội dung phụ huynh khai (From the family), mức độ dị ứng (để sắp xếp), đồng ý hiện tên và ảnh, ngày phụ huynh cập nhật, trạng thái chờ đánh giá; "Note from staff"; tình trạng tiêm chủng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Sunbeams có Ethan (hải sản và hạt, Severe) và một trẻ dị ứng trứng mức Mild | giáo viên mở danh sách và lọc lớp Sunbeams | Ethan ở dòng trên, trẻ dị ứng trứng ở dưới; mỗi dòng có Child, Class, Type, From the family, Note from staff, Vaccination, Updated by the family | FR-001; FR-002; BR-002 |
| AC-002 | một trẻ dị ứng trứng chưa chọn mức độ | danh sách hiển thị | trẻ được xếp cùng nhóm Severe | FR-002; BR-002 |
| AC-003 | Rayyan chỉ có hen suyễn, không có dị ứng | danh sách hiển thị | Rayyan nằm chung bảng, Type "Medical condition", xếp dưới các trẻ có dị ứng | FR-002; FR-003 |
| AC-005 | giáo viên đang lọc lớp Sunbeams | giáo viên chọn "Print for the kitchen" | bản in có tiêu đề "Allergies — N2 · Sunbeams", số trẻ, ngày in; cột Child, Class, Allergies; không có trẻ chỉ có Medical condition / Medical history | FR-007; BR-003 |
| AC-006 | giáo viên lọc lớp Sunbeams | giáo viên chọn Export | file Excel có đúng các trẻ đang hiện; không có bản ghi nhật ký xuất | FR-008; BR-004 |
| AC-007 | Centre Director của Small Wonder Tampines | mở danh sách | bộ lọc Centre là Small Wonder Tampines, Class là All classes | FR-005 |
| AC-008 | một trẻ dị ứng đang tạm nghỉ | Centre Director mở danh sách toàn Centre | trẻ đó không có trong danh sách | FR-010 |
| AC-009 | HQ Finance không được xem chi tiết y tế | HQ Finance mở đường dẫn danh sách | hiện "You do not have access to medical details." | VAL-002; BR-004 |
| AC-010 | lớp không có trẻ dị ứng | giáo viên mở danh sách | hiện "No children with allergies match these filters."; nút in và xuất file bị mờ | VAL-001 |
| AC-011 | đang xem danh sách | giáo viên chọn tên Ethan | mở tab Health trong hồ sơ Ethan | FR-009; BR-001 |
| AC-012 | phụ huynh của Caleb chưa ký đồng ý cho hiện trên danh sách y tế | giáo viên mở danh sách và in cho bếp | Caleb không có trong danh sách và bản in | FR-011 |
| AC-013 | phụ huynh của Mia chưa khai Medical Care Assessment | Centre Director mở danh sách toàn Centre | dòng của Mia ở cuối danh sách, có câu thông báo và "Contact the family" | FR-012 |
| AC-016 | mẹ của Ethan sửa triệu chứng trong Parents App, CD chưa đánh giá | giáo viên mở danh sách | dòng Ethan vẫn hiện nội dung đã xác nhận ở From the family; cột Updated by the family có nhãn "Awaiting assessment" | FR-014 |
| AC-017 | Lucas khai 5 chất gây dị ứng | danh sách hiển thị | ô From the family của Lucas hiện đủ 5 chất như phụ huynh khai | BR-005; FR-001 |
| AC-018 | Lucas có tình trạng tiêm chủng "Not up to date" | Centre Director lọc Vaccination: Not up to date | Lucas có trong kết quả, nhãn viền đứt "Not up to date" | FR-004; FR-015 |
| AC-019 | mẹ của Ethan cập nhật thông tin ngày 23/11/2026 | Centre Director lọc Updated: tuần này | Ethan có trong kết quả, cột Updated by the family ghi "23/11/2026 18:42" | FR-004; FR-001 |

#### Dependencies (Phụ thuộc)

Medical Care Assessment (phụ huynh khai trong Parents App, Centre Director / Admin hoàn tất đánh giá — BBA-68); đánh giá lại 6 tháng (BBA-68); quyền xem chi tiết y tế (Roles & permissions); hồ sơ trẻ; BBA-68 (quy tắc mức cảnh báo).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Phản ứng, cách xử trí và nơi để thuốc khẩn cấp có thành trường riêng không? | Centre Director / HQ Ops | Cao | Form Medical Care Assessment Checklist có trường riêng Symptoms, Steps to follow, Medication for immediate administration → đã tách cột. Nơi để thuốc chuyển sang OQ-02. |
| OQ-02 | Nơi để thuốc khẩn cấp có cần ghi không, ai ghi? Form chỉ có "Medication Held On Site Form Has Been Completed? Yes / Not Applicable". | Centre Director / HQ Ops | Cao |  |
| OQ-03 | Bếp dùng bản in hay có tài khoản xem trên máy; được xem dữ liệu nhận dạng nào? | Centre Director / HQ Ops | Trung bình |  |
| OQ-04 | Bản in cho bếp chỉ có cột Child, Class, Allergies (theo wireframe); có cần thêm Can tolerate, traces of eggs / nuts, Menu modifications không? | Centre Director / HQ Ops | Thấp |  |
| OQ-05 | "Chưa ký đồng ý thì không hiện" áp cho toàn bộ thông tin sức khoẻ (giáo viên cũng không thấy) hay chỉ tên / ảnh trên danh sách và bản in? Ẩn toàn bộ có rủi ro an toàn. | Centre Director / HQ Ops | Cao |  |
| OQ-06 | Thang mức độ có cần cấu hình theo brand / Centre ngay Phase 1 không? | HQ Ops | Trung bình |  |
| OQ-07 | Medical condition, medical history nằm chung danh sách dị ứng hay nhóm riêng? Form vừa có "Medical Condition" trong Type of Allergies, vừa có mục "Medical Conditions & History" riêng. FRD đang để chung bảng, phân biệt bằng cột Type. | Centre Director / HQ Ops | Trung bình |  |
| OQ-08 | Can tolerate, traces of eggs / nuts, menu modifications do phụ huynh khai trong Parents App hay Centre ghi khi đánh giá ("Menu reviewed with parents")? | Centre Director / HQ Ops | Trung bình |  |
| OQ-09 | Tên màn hình dùng "Allergies & conditions" hay theo form "Medical Health Alert List"? | HQ Ops | Thấp |  |
| OQ-10 | Tình trạng tiêm chủng (Vaccination) lấy từ đâu (vaccination record phụ huynh khai trong Parents App?), các giá trị Up to date / Not up to date / Not provided do ai xác định? | Centre Director / HQ Ops | Trung bình |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Medical Care Assessment | Form thông tin sức khoẻ của trẻ (Medical Care Assessment Checklist): loại dị ứng, chất gây dị ứng, mức độ, triệu chứng, điều kiện dung nạp, yêu cầu chăm sóc hằng ngày, kế hoạch xử trí, thuốc, bác sĩ, đồng ý của phụ huynh. Phụ huynh khai, Centre Director hoặc Senior Staff kiểm tra và xác nhận. |
| Medical Health Alert List | Tên danh sách y tế trên form của BBA ("Medical Overview / Medical Health Alert List"); trong hệ thống là màn Allergies & conditions. |
| Mức độ dị ứng | Mild (nhẹ), Moderate (vừa), Severe (nặng — tương ứng "Life Threatening" trên form của BBA). |
| Can tolerate | Điều kiện trẻ vẫn dùng được chất gây dị ứng (ví dụ ăn được bánh nướng có trứng nhưng không ăn trứng luộc). |
| EpiPen | Bút tiêm adrenaline dùng khi trẻ bị sốc phản vệ. |
| Ghi chú của nhân viên | Ghi chú do nhân viên Centre thêm ở tab Health, tách khỏi thông tin phụ huynh khai. |
| Vaccination | Tình trạng tiêm chủng của trẻ: Up to date, Not up to date, Not provided. |

## 9. Tài liệu tham khảo

Số trang của SRS tính theo bản Word gốc khi xuất PDF. Form của BBA tính theo trang của file PDF đính kèm trên Plane.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | BBA-SMS-SRS-Children-and-Families-v0.1 | §2 Who uses it | 3 | Mục 4 — vai trò và quyền. |
| 2 | BBA-SMS-SRS-Children-and-Families-v0.1 | §3 P2 Health information and allergy alerts (bước 5: in hoặc xuất danh sách dị ứng theo lớp cho bếp) | 4 | Mục 2; FR-007. |
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.3 Health & allergies (Show allergy alert, Print allergy list, Export allergy list) | 6–7 | FR-007, FR-008. |
| 4 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Business rules › Health and allergies (BR-CHF-021 đến BR-CHF-025) | 9 | FR-002, BR-001, BR-002, BR-004, VAL-002 — thang mức độ, chỉ phụ huynh sửa thông tin đã khai, vai trò được xem chi tiết y tế. |
| 5 | BBA-SMS-SRS-Children-and-Families-v0.1 | §7 Reports & exports (Allergy list by class) | 11 | FR-007, FR-008; Mục 4 — bếp. |
| 6 | BBA-SMS-SRS-Teacher-App-v0.1 | §2.3 Allergy view | 7 | FR-001, FR-003, FR-004 — cột, tìm kiếm, lọc, trẻ có bệnh không kèm dị ứng. |
| 7 | BBA-SMS-SRS-Teacher-App-v0.1 | §5 Business rules (BR-TCH-015) | 12 | FR-003 — nhóm riêng cho trẻ có bệnh không kèm dị ứng. |
| 8 | BBA — Appendix 1 Medical Care Assessment Checklist (đính kèm Plane BBA-1058) | Child's details; Medical conditions & history; Allergies & food tolerances; Daily care requirements for allergies; Emergency action plan | 1–2 | FR-001, FR-003, FR-004, FR-007, DATA-001 — các cột của danh sách và bản in. |
| 9 | BBA — Appendix 1 Medical Care Assessment Checklist (đính kèm Plane BBA-1058) | Parent's acknowledgement; For Centre's use; Note for Centre | 3 | FR-011, BR-001 — đồng ý hiện tên và ảnh, Centre Director / Senior Staff xác nhận, tên "Medical Health Alert List". |
| 10 | BBA — Appendix 3 Medical Care Assessment Review Record 2025 (SOP14, đính kèm Plane BBA-1058) | Review sheet (Date of Review, Date of Next Review) | 1 | Tham khảo — đánh giá lại 6 tháng thuộc BBA-68; cột Next review đã bỏ khỏi danh sách theo wireframe 15/11/2026. |
| 11 | Plane — BBA-1058 "BBA input: Health changes in the system, 6-monthly review, printing the allergy list" | Q1 (áp dụng sau đánh giá, nhắc trước 1 tháng); Q2 (vai trò in / xuất, không lưu nhật ký, trẻ chưa đồng ý không hiện) | — | FR-008, FR-011, FR-014, BR-004. |
| 12 | BBA_SMS_S4 — Tổng hợp câu hỏi phản hồi, sheet "Tổng hợp" | Đã chốt: Q-70-02, Q-70-03, Q-70-09, Q-70-10 · DOTB quyết định: Q-70-01, Q-70-04, Q-70-11 · Chưa phản hồi: Q-70-05, Q-70-06, Q-70-07, Q-70-12 | — | BR-005, FR-002, FR-012, BR-001; AS-02, AS-04, FR-008; OQ-01, OQ-02, OQ-03, OQ-07. |
| 13 | Plane — dự án BBA Phase 1, ticket BBA-69 (WBS 3.1.3.02) | Allergies list (most severe first) | — | Phạm vi tính năng. |
| 14 | Wireframe BBA-69 do DOTB cập nhật (15/11/2026), theo prototype BeeHive (emsv3) | Allergies & conditions; Print for the kitchen | — | FR-001 đến FR-005, FR-007, FR-008, FR-012, FR-014, FR-015; UI Components. |
