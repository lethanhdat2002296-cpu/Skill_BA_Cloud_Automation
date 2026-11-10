# BBA-69 Allergies list (most severe first) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Health & allergies |
| Tính năng | Allergies list (most severe first) |
| Mã ticket | BBA-69 |
| Mã WBS | 3.1.3.02 |
| Mã tài liệu | FRD-BBA-69 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-69: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả danh sách dị ứng theo Centre / lớp, thứ tự theo mức độ, lọc, in cho bếp, xuất file và quyền xem. 4 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Giáo viên và bếp cần một danh sách dị ứng của cả lớp hoặc cả Centre, trẻ bị nặng nhất ở trên cùng, để chuẩn bị bữa ăn và xử lý đúng khi trẻ có phản ứng. Nội dung lấy từ Health record do phụ huynh khai; nhân viên không gõ lại.

Mục tiêu đo được: danh sách hiển thị 100% trẻ đang đi học có dị ứng, theo đúng thứ tự mức độ; bản in cho bếp luôn ghi thời điểm in.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách dị ứng theo Centre và lớp, trẻ nặng nhất lên đầu. Các cột: trẻ, lớp, chất gây dị ứng, mức độ, phản ứng, cách xử trí, nơi để thuốc khẩn cấp (EpiPen), ghi chú của nhân viên, ngày phụ huynh cập nhật. Phần riêng cho trẻ chỉ có bệnh hoặc chế độ ăn đặc biệt. Tìm kiếm, lọc, in cho bếp, xuất file. Quyền xem theo vai trò. | Phụ huynh nhập và sửa Health record (Parents App). Cảnh báo đỏ trên hồ sơ trẻ và các danh sách khác (BBA-68). Biểu đồ tăng trưởng (BBA-70). Khai báo và ghi nhận cho trẻ uống thuốc. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Teacher / Senior Teacher | Lớp của mình. | Xem danh sách lớp mình, in cho bếp. |
| Centre Director, School Admin | Centre của mình. | Xem toàn Centre, in, xuất file; liên hệ phụ huynh khi thông tin dị ứng thiếu. |
| HQ Admin | Mọi Centre. | Xem, in, xuất file mọi Centre. |
| HQ Ops (District Manager, Operations Manager) | Các Centre mình phụ trách. | Xem theo quyền được cấp. |
| Bếp | Centre. | Dùng bản in do Centre đưa (AS-01). |
| Phụ huynh (Parents App) | Con mình. | Nguồn duy nhất của thông tin dị ứng. |
| Hệ thống | Toàn hệ thống. | Sắp xếp theo mức độ, ghi thời điểm in, lưu lại các lần xuất file. |

Quy tắc chung: chỉ vai trò được phép xem chi tiết y tế mới mở được danh sách này (mặc định Centre Director, Teacher, School Admin, HQ Admin); mọi lần xuất file được lưu lại (ai xuất, lúc nào).

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Children & families › Health & allergies | Danh sách dị ứng theo Centre / lớp, in cho bếp, xuất file. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Danh sách dị ứng, trẻ nặng nhất lên đầu

#### User Story

Là giáo viên, tôi muốn xem và in danh sách dị ứng của lớp mình, trẻ bị nặng nhất ở trên cùng, để tôi và bếp biết ngay trẻ nào cần tránh món gì và xử lý ra sao khi trẻ có phản ứng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Danh sách có một dòng cho mỗi trẻ có ít nhất một dị ứng, gồm: ảnh và tên trẻ, lớp, các chất gây dị ứng (mỗi chất kèm mức độ Mild / Moderate / Severe), phản ứng, cách xử trí, nơi để thuốc khẩn cấp (EpiPen), ghi chú của nhân viên, ngày phụ huynh cập nhật lần cuối. |
| FR-002 | Thứ tự mặc định: trẻ có mức nặng nhất ở trên cùng (Severe, rồi Moderate, rồi Mild); cùng mức thì xếp theo lớp, rồi theo tên trẻ. Dị ứng chưa chọn mức độ được xếp cùng nhóm Severe và ghi "Chưa chọn mức độ". |
| FR-003 | Bên dưới danh sách dị ứng có phần riêng "Tình trạng khác và chế độ ăn" cho trẻ không có dị ứng nhưng có bệnh (da, hô hấp, tiền sử bệnh) hoặc chế độ ăn đặc biệt. |
| FR-004 | Tìm theo tên trẻ hoặc chất gây dị ứng; lọc theo Centre, lớp, mức độ và loại (dị ứng, bệnh, chế độ ăn); các bộ lọc dùng kết hợp được. |
| FR-005 | Giáo viên mở danh sách thì mặc định lọc theo lớp của mình; Centre Director và School Admin mặc định thấy toàn Centre. |
| FR-006 | Trẻ mức Severe chưa có phản ứng, cách xử trí hoặc nơi để thuốc khẩn cấp hiện chữ "Chưa có thông tin" màu đỏ ở ô còn thiếu, để Centre Director liên hệ phụ huynh bổ sung. |
| FR-007 | "Print for the kitchen" in danh sách theo bộ lọc đang chọn (một lớp hoặc cả Centre), đầu trang ghi tên Centre, lớp, ngày giờ in và người in (ví dụ "Printed on 24/11/2026 08:15 by Aisyah Rahman") và số trẻ trong bản in. |
| FR-008 | "Export" xuất danh sách theo bộ lọc đang chọn ra Excel; hệ thống lưu lại người xuất, thời điểm và bộ lọc. |
| FR-009 | Chọn tên trẻ mở tab Health trong hồ sơ trẻ. |
| FR-010 | Danh sách chỉ gồm trẻ đang đi học; trẻ đang tạm nghỉ, đã thôi học hoặc đã tốt nghiệp không có trong danh sách. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Children & families › Health & allergies; danh sách mặc định lọc theo lớp của mình (FR-005).
2. Hệ thống hiển thị trẻ có dị ứng, trẻ nặng nhất lên đầu (FR-001, FR-002), và phần "Tình trạng khác và chế độ ăn" (FR-003).
3. Giáo viên chọn "Print for the kitchen" và đưa bản in cho bếp (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Centre Director lọc toàn Centre theo mức Severe để rà soát trẻ thiếu cách xử trí (FR-004, FR-006).
2. Centre Director xuất danh sách ra Excel (FR-008).
3. Người dùng chọn tên trẻ để xem đủ Health record (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Lớp không có trẻ dị ứng: hiện thông báo trống (VAL-001).
2. Vai trò không được xem chi tiết y tế: không mở được danh sách (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Phụ huynh là nguồn duy nhất của thông tin dị ứng; danh sách chỉ đọc, nhân viên chỉ thêm ghi chú của nhân viên ở tab Health. |
| BR-002 | Trẻ nặng nhất luôn ở trên cùng; dị ứng chưa chọn mức độ được coi như Severe. |
| BR-003 | Bản in luôn ghi thời điểm in và người in, để bếp biết bản nào là bản mới nhất. |
| BR-004 | Chỉ vai trò được phép xem chi tiết y tế mới xem, in và xuất danh sách; mọi lần xuất file được lưu lại. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có trẻ nào. | Hiện "No children with allergies match these filters."; nút in và xuất file bị mờ. |
| VAL-002 | Người dùng không có quyền xem chi tiết y tế mở danh sách. | Không có mục Health & allergies trong menu; mở bằng đường dẫn thì hiện "You do not have access to medical details." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Health & allergies — danh sách dị ứng | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tìm kiếm | Ô nhập | Không | Trống | — | Tên trẻ, chất gây dị ứng. |
| Centre, Lớp, Mức độ, Loại | Bộ lọc | Không | Theo vai trò (FR-005) | VAL-001. | FR-004. |
| Danh sách dị ứng | Bảng | Có | Nặng nhất lên đầu | — | FR-001; FR-002; FR-006. |
| Tình trạng khác và chế độ ăn | Bảng | Khi có | — | — | FR-003. |
| Print for the kitchen | Nút | Có | — | VAL-001. | FR-007. |
| Export | Nút | Theo quyền | — | VAL-001. | FR-008. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Danh sách đọc từ Health record: chất gây dị ứng, mức độ, phản ứng, cách xử trí, nơi để thuốc khẩn cấp, bệnh, chế độ ăn, ngày cập nhật; ghi chú của nhân viên. |
| DATA-002 | Mỗi lần in và xuất file được lưu lại: người thực hiện, thời điểm, bộ lọc, số trẻ. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Sunbeams có Ethan (hải sản và hạt, Severe) và một trẻ dị ứng trứng mức Mild | giáo viên lớp Sunbeams mở danh sách | Ethan ở dòng đầu, trẻ dị ứng trứng ở dưới; mỗi chất gây dị ứng ghi kèm mức độ | FR-001; FR-002; BR-002 |
| AC-002 | một trẻ dị ứng trứng chưa chọn mức độ | danh sách hiển thị | trẻ nằm trong nhóm Severe và ghi "Chưa chọn mức độ" | FR-002; BR-002 |
| AC-003 | Rayyan chỉ có hen suyễn, không có dị ứng | danh sách hiển thị | Rayyan nằm ở phần "Tình trạng khác và chế độ ăn" | FR-003 |
| AC-004 | Ethan mức Severe chưa có cách xử trí | Centre Director lọc mức Severe | ô cách xử trí của Ethan hiện "Chưa có thông tin" màu đỏ | FR-004; FR-006 |
| AC-005 | giáo viên đang lọc lớp Sunbeams | giáo viên chọn "Print for the kitchen" | bản in chỉ có trẻ lớp Sunbeams, đầu trang ghi Centre, lớp, ngày giờ in, người in và số trẻ | FR-007; BR-003 |
| AC-006 | Centre Director lọc toàn Centre | Centre Director chọn Export | file Excel có đúng các trẻ đang hiện; hệ thống lưu người xuất, thời điểm, bộ lọc | FR-008; BR-004; DATA-002 |
| AC-007 | giáo viên lớp Sunbeams | giáo viên mở danh sách | bộ lọc lớp mặc định là Sunbeams | FR-005 |
| AC-008 | một trẻ dị ứng đang tạm nghỉ | Centre Director mở danh sách toàn Centre | trẻ đó không có trong danh sách | FR-010 |
| AC-009 | HQ Finance không được xem chi tiết y tế | HQ Finance mở đường dẫn danh sách | hiện "You do not have access to medical details." | VAL-002; BR-004 |
| AC-010 | lớp không có trẻ dị ứng | giáo viên mở danh sách | hiện "No children with allergies match these filters."; nút in và xuất file bị mờ | VAL-001 |
| AC-011 | đang xem danh sách | giáo viên chọn tên Ethan | mở tab Health trong hồ sơ Ethan | FR-009; BR-001 |

#### Dependencies (Phụ thuộc)

Health record (phụ huynh khai trong Parents App); quyền xem chi tiết y tế (Roles & permissions); hồ sơ trẻ; BBA-68 (quy tắc mức cảnh báo).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Phản ứng, cách xử trí và nơi để thuốc khẩn cấp có thành trường riêng trong Health record không, hay vẫn là chữ phụ huynh ghi chung trong mục dị ứng? | Centre Director / HQ Ops | Cao |  |
| OQ-02 | Ai ghi "nơi để thuốc khẩn cấp" (ví dụ "ở phòng y tế", "trong cặp của trẻ"): phụ huynh hay Centre? | Centre Director / HQ Ops | Cao |  |
| OQ-03 | Bếp dùng bản in, hay nhân viên bếp có tài khoản để xem trên máy? | Centre Director / HQ Ops | Trung bình |  |
| OQ-04 | Bản in cho bếp cần đủ các cột hay chỉ trẻ, lớp, chất gây dị ứng, mức độ, chế độ ăn? Mỗi lớp một trang? | Centre Director / HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Bếp nhận bản in do Centre đưa; nhân viên bếp không có tài khoản. | Mục 4 — chờ OQ-03 |
| AS-02 | Mỗi trẻ một dòng; trẻ có nhiều dị ứng thì liệt kê các chất trong cùng dòng. | FR-001 |
| AS-03 | Trẻ đang tạm nghỉ không có trong danh sách vì không đến trường. | FR-010 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Health record | Thông tin sức khoẻ phụ huynh khai trong Parents App: dị ứng (kèm mức độ), bệnh, chế độ ăn, ghi chú của gia đình. |
| Mức độ dị ứng | Mild (nhẹ), Moderate (vừa), Severe (nặng). |
| EpiPen | Bút tiêm adrenaline dùng khi trẻ bị sốc phản vệ. |
| Ghi chú của nhân viên | Ghi chú do nhân viên Centre thêm, tách khỏi chữ phụ huynh ghi. |
