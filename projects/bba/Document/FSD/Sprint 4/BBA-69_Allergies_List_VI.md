# Health & Allergies list

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

**Mức sẵn sàng:** Đặc tả danh sách sức khỏe theo Brand / Centre / lớp, thứ tự theo mức độ, lọc, in cho bếp, xuất file và quyền xem.

## 2. Mục tiêu và bối cảnh

Giáo viên và bếp cần một danh sách dị ứng của cả lớp hoặc cả Centre, trẻ bị nặng nhất ở trên cùng, để chuẩn bị bữa ăn và xử lý đúng khi trẻ có phản ứng. Nội dung lấy từ tab Health ở Child do phụ huynh khai và Giáo viên / Senior Staff xác nhận; nhân viên không gõ lại. Trên form của BBA, danh sách này gọi là "Medical Overview / Medical Health Alert List".

Mục tiêu: danh sách hiển thị 100% trẻ đang đi học có dị ứng, theo đúng thứ tự mức độ; bản in cho bếp luôn ghi thời điểm in.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách sức khỏe theo Centre / lớp (dị ứng, bệnh, tiền sử trong cùng một bảng), trẻ dị ứng nặng nhất lên đầu. Các cột: theo mô tả trong Ux/Ui. Dòng cuối cho trẻ chưa khai thông tin sức khỏe. Tìm kiếm, lọc, in cho bếp, xuất file. Quyền xem theo vai trò. | Phụ huynh nhập và sửa Medical Care Assessment (Parents App); quy trình đánh giá và đánh giá lại 6 tháng (BBA-68). Cảnh báo đỏ trên hồ sơ trẻ và các danh sách khác (BBA-68). Biểu đồ tăng trưởng (BBA-70). Khai báo và ghi nhận cho trẻ uống thuốc. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ có thông tin sức khoẻ trong phạm vi vai trò và phạm vi dữ liệu hiện có (lớp hoặc Centre). | Xem, lọc, in cho bếp và xuất danh sách khi vai trò được cấp quyền xem chi tiết y tế. |
| System | Medical Care Assessment đã xác nhận của trẻ. | Sắp xếp theo mức độ, tính hạn đánh giá lại, ghi thời điểm in. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi dữ liệu được phép. | Không thấy và không thực hiện được thao tác bị giới hạn; không thay đổi dữ liệu. |

Mọi quyền xem và thao tác theo mô hình phân quyền theo vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng; hệ thống không lưu nhật ký in / xuất (BBA-1058 Q2).

## 5. Tổng quan tính năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Children & families › Health & allergies** | Health & allergies | Danh sách dị ứng theo Centre / lớp (Medical Health Alert List), in cho bếp, xuất file. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Danh sách dị ứng, trẻ nặng nhất lên đầu

#### User Story

Là giáo viên, tôi muốn xem và in danh sách dị ứng của lớp mình, trẻ bị nặng nhất ở trên cùng, để tôi và bếp biết trẻ nào cần tránh món gì và xử lý ra sao khi trẻ có phản ứng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Mỗi một dòng tương ứng cho mỗi trẻ có thông tin sức khoẻ (dị ứng, bệnh, tiền sử) với thông tin hiển thị ở các cột được mô tả ở Ux/Ui |
| FR-002 | Sắp xếp danh sách mặc định theo mức độ nghiêm trọng (most severe first) theo thang 3 mức trên form chính thức của BBA: Life Threatening → Moderate → Mild; thang có thể tuỳ chỉnh theo brand / Centre (OQ-06). Cho phép sắp xếp theo cột (BR-004). |
| FR-003 | Tìm kiếm theo tên trẻ, lọc danh sách và hiển thị tổng số trẻ khớp điều kiện (BR-007). |
| FR-004 | In danh sách dị ứng cho bếp (Print for the kitchen) theo bộ lọc đang chọn (BR-008, BR-009). |
| FR-005 | Mở tab Health trong hồ sơ trẻ khi chọn tên trẻ. |
| FR-006 | Báo hiệu thông tin sức khỏe phụ huynh vừa cập nhật nhưng chưa được đánh giá (BR-010). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Children & families › Health & allergies; danh sách mặc định lọc theo lớp của mình (FR-005).
2. Hệ thống hiển thị trẻ có thông tin sức khỏe, trẻ dị ứng nặng nhất lên đầu, trẻ chưa khai ở cuối (FR-001, FR-002, FR-012).
3. Giáo viên chọn "Print for the kitchen" (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Giáo viên lọc toàn Centre theo Type hoặc Vaccination để rà soát (FR-004, FR-015).
2. Giáo viên, School Admin hoặc giáo viên xuất danh sách ra Excel (FR-008).
3. Người dùng chọn tên trẻ để xem chi tiết thông tin tại Tab Health (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có trẻ nào: hiện thông báo trống (VAL-001).
2. Vai trò không được xem chi tiết y tế: không mở được danh sách (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Nguồn và quyền sửa: phụ huynh khai Medical Care Assessment; Centre Director hoặc Senior Staff kiểm tra, xác nhận. Danh sách chỉ đọc; nhân viên chỉ thêm Note from staff ở tab Health (Appendix 1 tr. 3, BBA-1058 Q1). |
| BR-002 | Đối tượng: chỉ trẻ đang đi học; trẻ tạm nghỉ, đã thôi học hoặc đã tốt nghiệp không có trong danh sách. |
| BR-003 | Đồng ý của phụ huynh: trẻ chưa ký đồng ý hiện tên và ảnh trên danh sách y tế (Medical Care Assessment Checklist) không có trong danh sách và bản in (BBA-1058 Q2; phạm vi ẩn chờ OQ-05). |
| BR-004 | Thứ tự mặc định: Life Threatening → Moderate → Mild → Medical condition / Medical history; cùng mức xếp theo lớp, rồi tên trẻ. Dị ứng chưa chọn mức độ được coi như Life Threatening. Mức độ chỉ dùng để sắp xếp, không hiển thị thành cột. Các cột sắp xếp được: Child, Class, Type, Vaccination, Updated by the family. |
| BR-005 | Trẻ chỉ có bệnh hoặc tiền sử (không có dị ứng), phân biệt bằng Type Medical condition / Medical history; |
| BR-006 | Một trẻ không bị giới hạn số dị ứng hoặc bệnh; ô From the family hiển thị đủ nội dung phụ huynh khai (Q-70-02). |
| BR-007 | Tìm kiếm và lọc: bộ lọc gồm Centre, Class, Type dùng kết hợp được. Mặc định Centre = Centre của người dùng, Class = All classes. Total = số trẻ khớp tìm kiếm và bộ lọc. |
| BR-008 | Bản in cho bếp: theo bộ lọc đang chọn; chỉ gồm trẻ có Type Food, Environmental, Medication, Insect; chỉ có cột Child, Class, Allergies (= From the family); không có ảnh trẻ, không có chân trang. Tiêu đề "Allergies — {phạm vi}" (tên Centre, tên lớp hoặc "All my centres"). |
| BR-009 | Bản in luôn ghi ngày in và số trẻ, để bếp biết bản nào mới nhất. |
| BR-010 | Khi phụ huynh sửa thông tin sức khỏe trong Parents App, danh sách và bản in giữ bản đã xác nhận gần nhất; cột Updated by the family hiện nhãn "Awaiting assessment" cho tới khi CD / Admin hoàn tất đánh giá. |
| BR-012 | Health Info / Allergies là bắt buộc: phụ huynh phải acknowledge và declare. Hồ sơ chưa khai báo khác hồ sơ đã khai báo không có dị ứng. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có trẻ nào. | Hiện "No children with allergies match these filters."; nút in và xuất file bị mờ. |
| VAL-002 | Người dùng không có quyền xem chi tiết y tế mở danh sách. | Không có mục Health & allergies trong menu; mở bằng đường dẫn thì hiện "You do not have access to medical details." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Allergies & conditions (Medical Health Alert List) |  |
| Print for the kitchen |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Header** | | | | | |
| Allergies & conditions | Tiêu đề màn hình | — | — | — | Tên màn hình = Medical Health Alert List; dòng mô tả: dữ liệu lấy từ Medical Care Assessment của từng trẻ, đã được Centre xác nhận. |
| Export (n) | Nút | Theo quyền | n = số trẻ đang hiển thị | VAL-001. | Xuất danh sách đang lọc (FR-008). |
| Print for the kitchen | Nút chính | Theo quyền | — | VAL-001. | Mở bản in theo bộ lọc đang chọn (FR-007; SCR-02). |
| **Filter** | | | | | |
| Search child | Ô tìm kiếm | Không | Trống | — | Tìm theo tên trẻ. |
| Total | Số | — | — | — | Số trẻ khớp tìm kiếm và bộ lọc. |
| Centre | Bộ lọc | Không | Centre của người dùng | — | FR-005. |
| Class | Bộ lọc | Không | All classes | — | Chọn một lớp thì ô lọc có viền nhấn. |
| Type | Bộ lọc | Không | All | — | Lọc theo cột Type. |
| **Allergies & conditions (Medical Health Alert List)** | | | | | |
| Child | Cột | — | — | — | Avatar (ảnh hoặc chữ viết tắt) và họ tên; sắp xếp được; chọn tên mở tab Health (FR-009). |
| Class | Cột | — | — | — | Level · tên lớp hiện tại; sắp xếp được. |
| Type | Cột | — | — | — | Food, Environmental, Medication, Insect, Medical condition, Medical history; sắp xếp được. |
| From the family | Cột | — | — | — | Nguyên văn phụ huynh khai trong Medical Care Assessment (chất gây dị ứng, triệu chứng, cách xử trí…); hiển thị bản đã được Centre xác nhận (BR-001). |
| Note from staff | Cột | — | "—" khi không có | — | Ghi chú nội bộ của Centre. |
| Vaccination | Cột (nhãn) | — | — | — | Tình trạng tiêm chủng: Up to date — nhãn viền liền; Not up to date / Not provided — nhãn viền đứt; sắp xếp được. |
| Updated by the family | Cột | — | — | — | Lần cuối phụ huynh cập nhật (DD/MM/YYYY HH:mm); sắp xếp được; bản cập nhật chưa được đánh giá có nhãn "Awaiting assessment" bên dưới (FR-014). |
| Pager | Phân trang | — | 20 dòng / trang | — | "1–n of n", chọn số dòng mỗi trang. |
| **Print for the kitchen** | | | | | |
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
| DATA-001 | Đọc từ Medical Care Assessment đã xác nhận: Type (Food, Environmental, Medication, Insect, Medical condition, Medical history); From the family (chất gây dị ứng, triệu chứng, cách xử trí — nguyên văn phụ huynh khai); mức độ dị ứng (Mild / Moderate / Life Threatening, chỉ dùng sắp xếp; danh mục có thể tùy chỉnh theo brand / Centre); đồng ý hiện tên và ảnh; ngày giờ phụ huynh cập nhật (DD/MM/YYYY HH:mm); trạng thái chờ đánh giá. |
| DATA-002 | Note from staff: ghi chú nội bộ do nhân viên Centre nhập ở tab Health; trống hiện "—". Thông tin trẻ: ảnh / chữ viết tắt, họ tên, Level · lớp hiện tại, trạng thái đi học. |
| DATA-003 | Vaccination: Up to date, Not up to date / Not provided (nhãn viền đứt); |
| DATA-004 | Trạng thái khai báo sức khoẻ của trẻ: Đã khai báo (có hoặc không có dị ứng) / Chưa khai báo / Chưa cung cấp (chỉ cho trẻ unborn). |
| AUDIT-001 | Không lưu nhật ký in (BBA-1058 Q2). Danh sách chỉ đọc nên không phát sinh bản ghi thay đổi dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Sunbeams có Ethan (hải sản và hạt, Life Threatening) và một trẻ dị ứng trứng mức Mild | giáo viên mở danh sách và lọc lớp Sunbeams | Ethan ở dòng trên, trẻ dị ứng trứng ở dưới; mỗi dòng có Child, Class, Type, From the family, Note from staff, Vaccination, Updated by the family | FR-001; FR-002; BR-004 |
| AC-002 | một trẻ dị ứng trứng chưa chọn mức độ | danh sách hiển thị | trẻ được xếp cùng nhóm Life Threatening | FR-002; BR-004 |
| AC-003 | Rayyan chỉ có hen suyễn, không có dị ứng | danh sách hiển thị | Rayyan nằm chung bảng, Type "Medical condition", xếp dưới các trẻ có dị ứng | FR-002; BR-005 |
| AC-005 | giáo viên đang lọc lớp Sunbeams | giáo viên chọn "Print for the kitchen" | bản in có tiêu đề "Allergies — N2 · Sunbeams", số trẻ, ngày in; cột Child, Class, Allergies; không có trẻ chỉ có Medical condition / Medical history | FR-004; BR-008; BR-009 |
| AC-007 | Centre Director của Small Wonder Tampines | mở danh sách | bộ lọc Centre là Small Wonder Tampines, Class là All classes | FR-003; BR-007 |
| AC-008 | một trẻ dị ứng đang tạm nghỉ | Centre Director mở danh sách toàn Centre | trẻ đó không có trong danh sách | FR-001; BR-002 |
| AC-009 | lớp không có trẻ dị ứng | giáo viên mở danh sách | hiện "No children with allergies match these filters."; nút in bị mờ | VAL-001 |
| AC-010 | đang xem danh sách | giáo viên chọn tên Ethan | mở tab Health trong hồ sơ Ethan | FR-005; BR-001 |
| AC-011 | phụ huynh của Caleb chưa ký đồng ý cho hiện trên danh sách y tế | giáo viên mở danh sách và in cho bếp | Caleb không có trong danh sách và bản in | FR-001; BR-003 |
| AC-012 | mẹ của Ethan sửa triệu chứng trong Parents App, CD chưa đánh giá | giáo viên mở danh sách | dòng Ethan vẫn hiện nội dung đã xác nhận ở From the family; cột Updated by the family có nhãn "Awaiting assessment" | FR-006; BR-010 |
| AC-013 | Lucas khai 5 chất gây dị ứng | danh sách hiển thị | ô From the family của Lucas hiện đủ 5 chất như phụ huynh khai | FR-001; BR-006 |
| AC-014 | Lucas có tình trạng tiêm chủng "Not up to date" | Centre Director lọc Vaccination: Not up to date | Lucas có trong kết quả, nhãn viền đứt "Not up to date" | FR-003; DATA-003 |
| AC-015 | mẹ của Ethan cập nhật thông tin ngày 23/11/2026 | Centre Director lọc Updated: tuần này | Ethan có trong kết quả, cột Updated by the family ghi "23/11/2026 18:42" | FR-003; BR-007; DATA-001 |

#### Dependencies (Phụ thuộc)

Medical Care Assessment (phụ huynh khai trong Parents App, Giáo viên / Admin hoàn tất đánh giá — BBA-68); đánh giá lại 6 tháng (BBA-68); quyền xem chi tiết y tế (Roles & permissions); hồ sơ trẻ; BBA-68 (quy tắc mức cảnh báo).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Bếp dùng bản in hay có tài khoản xem trên máy; được xem dữ liệu nhận dạng nào? | Centre Director / HQ Ops | Trung bình |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Medical Care Assessment | Form thông tin sức khoẻ của trẻ (Medical Care Assessment Checklist): loại dị ứng, chất gây dị ứng, mức độ, triệu chứng, điều kiện dung nạp, yêu cầu chăm sóc hằng ngày, kế hoạch xử trí, thuốc, bác sĩ, đồng ý của phụ huynh. Phụ huynh khai, Giáo viên hoặc Senior Staff kiểm tra và xác nhận. |
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
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.3 Health & allergies (Show allergy alert, Print allergy list, Export allergy list) | 6–7 | FR-007; FR-008. |
| 4 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Business rules › Health and allergies (BR-CHF-021 đến BR-CHF-025) | 9 | FR-002, BR-001, BR-002, BR-004, VAL-002 — thang mức độ, chỉ phụ huynh sửa thông tin đã khai, vai trò được xem chi tiết y tế. |
| 5 | BBA-SMS-SRS-Children-and-Families-v0.1 | §7 Reports & exports (Allergy list by class) | 11 | FR-007, FR-008; Mục 4 — bếp. |
| 6 | BBA-SMS-SRS-Teacher-App-v0.1 | §2.3 Allergy view | 7 | FR-001, FR-003, FR-004 — cột, tìm kiếm, lọc, trẻ có bệnh không kèm dị ứng. |
| 7 | BBA-SMS-SRS-Teacher-App-v0.1 | §5 Business rules (BR-TCH-015) | 12 | FR-003 — nhóm riêng cho trẻ có bệnh không kèm dị ứng. |
| 8 | BBA — Appendix 1 Medical Care Assessment Checklist (đính kèm Plane BBA-1058) | Child's details; Medical conditions & history; Allergies & food tolerances; Daily care requirements for allergies; Emergency action plan | 1–2 | FR-001, FR-003, FR-004, FR-007, DATA-001 — các cột của danh sách và bản in. |
| 9 | BBA — Appendix 1 Medical Care Assessment Checklist (đính kèm Plane BBA-1058) | Parent's acknowledgement; For Centre's use; Note for Centre | 3 | FR-011, BR-001 — đồng ý hiện tên và ảnh, Giáo viên / Senior Staff xác nhận, tên "Medical Health Alert List". |
| 10 | BBA — Appendix 3 Medical Care Assessment Review Record 2025 (SOP14, đính kèm Plane BBA-1058) | Review sheet (Date of Review, Date of Next Review) | 1 | Tham khảo — đánh giá lại 6 tháng thuộc BBA-68; cột Next review đã bỏ khỏi danh sách theo wireframe 15/11/2026. |
| 11 | Plane — BBA-1058 "BBA input: Health changes in the system, 6-monthly review, printing the allergy list" | Q1 (áp dụng sau đánh giá, nhắc trước 1 tháng); Q2 (vai trò in / xuất, không lưu nhật ký, trẻ chưa đồng ý không hiện) | — | FR-008; FR-011; FR-014; BR-004. |
| 12 | BBA_SMS_S4 — Tổng hợp câu hỏi phản hồi, sheet "Tổng hợp" | Đã chốt: Q-70-02, Q-70-03, Q-70-09, Q-70-10 · DOTB quyết định: Q-70-01, Q-70-04, Q-70-11 · Chưa phản hồi: Q-70-05, Q-70-06, Q-70-07, Q-70-12 | — | BR-005; FR-002; FR-012; BR-001; AS-02; AS-04; FR-008; OQ-01; OQ-02; OQ-03; OQ-07. |
| 13 | Plane — dự án BBA Phase 1, ticket BBA-69 (WBS 3.1.3.02) | Allergies list (most severe first) | — | Phạm vi tính năng. |
| 14 | Wireframe BBA-69 do DOTB cập nhật (15/11/2026), theo prototype BeeHive (emsv3) | Allergies & conditions; Print for the kitchen | — | FR-001 đến FR-005, FR-007, FR-008, FR-012, FR-014, FR-015; UI Components. |
