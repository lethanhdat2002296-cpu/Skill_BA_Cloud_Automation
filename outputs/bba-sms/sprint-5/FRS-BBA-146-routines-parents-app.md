# Functional Requirements Specification — Routines (Parents App)

**Dự án:** Busy Bees Asia SMS · **Module:** Parents App — Daily life · **Tính năng:** BBA-146 Routines  
**Mã tài liệu:** FRD-4.1.2.01_Routines · **Sprint:** 5 · **Phiên bản:** 0.2 · **Trạng thái:** Bản nháp chờ xác nhận · **Ngày:** 27/11/2026  
**Người soạn:** Business Analysis · **Người review:** HaiNguyen · **Người duyệt:** HaiNguyen

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 26/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 27/11/2026 | Business Analysis | Bỏ Mood (Q-86-01, BBA-78); thêm “Shown to parents”, không thông báo khi sửa, tắt nhóm thông báo Routines; thêm Câu hỏi mở. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu. Đã đối chiếu BBA-78 và bảng câu hỏi Sprint 4; 2 câu hỏi mở ở mục 7.

## 2. Mục đích và bối cảnh

Tài liệu đặc tả màn hình Routines trên Parents App: phụ huynh xem dòng thời gian các hoạt động chăm sóc trong ngày của trẻ đang chọn (bữa ăn, bình sữa, giấc ngủ, thay tã / đi vệ sinh) do giáo viên ghi, lọc theo loại, xem ngày trước, và gửi một ghi chú từ gia đình (Note from home) cho giáo viên mỗi ngày.

Routine được giáo viên ghi trên Teacher App (BBA-148). Parents App chỉ đọc routine; phụ huynh không sửa, không xoá. Note from home do phụ huynh viết trên Parents App và giáo viên đọc trên Teacher App.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Dòng thời gian routine của trẻ đang chọn theo ngày; lọc theo loại routine; chỉ hiện loại routine đang bật “Shown to parents”; chọn ngày; lý do khi ngày không có routine; ảnh kèm routine; thông báo “Daily routines updated” mỗi ngày; viết, sửa Note from home trong ngày. | Ghi, sửa, xoá routine (Teacher App, BBA-148); cấu hình routine bắt buộc theo level và cài đặt “Shown to parents” (SMS, BBA-78); điểm danh, nhiệt độ (Attendance); chọn trẻ (BBA-145); bình luận hay thả cảm xúc trên routine; dịch tự động. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Phụ huynh (Guardian) | Trẻ được liên kết với tài khoản, đang được chọn. | Xem routine; viết, sửa Note from home của ngày hiện tại. |
| Giáo viên (Teacher) | Trẻ thuộc lớp được phân công. | Ghi routine (BBA-148); đọc Note from home. |
| System | Routine, Note from home, điểm danh và lịch Centre. | Cung cấp routine theo trẻ và ngày; xác định lý do ngày trống; gửi thông báo “Daily routines updated”; ghi lịch sử Note from home. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-146 gồm hai User Story trên Parents App, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| Daily life | Xem routine trong ngày | Dòng thời gian routine theo ngày, lọc theo loại, chọn ngày, lý do ngày trống, thông báo cuối ngày. | BBA-146: US-001 |
| Daily life | Note from home | Phụ huynh viết, sửa một ghi chú mỗi ngày cho giáo viên. | BBA-146: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-146: US-001 - Xem routine trong ngày

#### User Story

Là phụ huynh, tôi muốn xem con ăn, uống, ngủ, thay tã thế nào trong ngày ở trường, để nắm được một ngày của con.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải hiển thị các routine của trẻ đang chọn trong ngày đã chọn, sắp theo thời gian, mỗi routine một mục; chỉ gồm các loại routine đang bật “Shown to parents”. |
| FR-002 | Hệ thống phải cho lọc theo loại routine và chọn ngày khác trong khoảng từ ngày bắt đầu học đến hôm nay. |
| FR-003 | Hệ thống phải hiển thị lý do khi ngày đã chọn không có routine. |
| FR-004 | Hệ thống phải gửi mỗi phụ huynh một thông báo “Daily routines updated” mỗi ngày, khi trẻ được check-out. |

#### Functional Flow - Main (Luồng chính)

1. Phụ huynh mở Routines từ Home, All features hoặc từ thông báo “Daily routines updated”.
2. Hệ thống hiển thị routine của trẻ đang chọn cho ngày hôm nay (mở từ thông báo thì cho ngày của thông báo), sắp theo thời gian (FR-001).
3. Phụ huynh chọn loại routine để lọc hoặc chọn ngày khác (FR-002). Hệ thống hiển thị routine khớp điều kiện.
4. Phụ huynh chạm ảnh của một routine để xem toàn màn hình.

#### Functional Flow - Alternative (Luồng thay thế)

1. Ngày đã chọn không có routine: hiển thị lý do theo BR-005 (FR-003).
2. Bộ lọc không có kết quả: hiển thị “No <loại routine> recorded on <ngày>.”
3. Trẻ được check-out: hệ thống gửi thông báo “Daily routines updated” cho mỗi phụ huynh (FR-004; BR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không tải được dữ liệu: hiển thị lỗi theo hành vi chuẩn và nút Try again.
2. Trẻ đang tạm nghỉ: hiển thị “Not attending at the moment”, không có routine.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Routine chỉ đọc với phụ huynh: không có thao tác sửa, xoá, bình luận. Phụ huynh chỉ thấy routine của trẻ thuộc tài khoản. |
| BR-002 | Phase 1 có 4 loại routine (Q-86-01, BBA-78): Meal – giờ, bữa (Breakfast / Morning snack / Lunch / Afternoon snack / Late snack), lượng ăn (All / Most / Some / None), món; Bottle – giờ, ml pha, ml uống; Nap – giờ bắt đầu, giờ kết thúc, thời lượng, chất lượng (Slept well / Disrupted sleep), “Sleeping” khi chưa có giờ kết thúc; Nappy / toilet – giờ, hình thức (Diaper / Potty / Accident), kết quả (Wet / BM / Dry). Mọi loại có ghi chú và ảnh khi giáo viên nhập. |
| BR-003 | Bộ lọc: All, Meals, Bottles, Naps, Nappy & toilet. Chỉ hiện chip của loại đang bật “Shown to parents”. Mặc định All. |
| BR-004 | Routine giáo viên đã xoá không hiển thị. Routine đã sửa hiển thị giá trị mới nhất; sửa một routine phụ huynh đã thấy không gửi thông báo mới (BBA-78 AS-03). Không hiển thị tên giáo viên ghi routine. |
| BR-005 | Lý do ngày trống theo thứ tự ưu tiên: Closure, Public holiday, On leave, Absent; ngày hiện tại chưa có routine thì hiển thị “Nothing recorded yet”. |
| BR-006 | Mỗi phụ huynh nhận đúng một thông báo “Daily routines updated” mỗi ngày cho mỗi trẻ, gửi khi bản ghi check-out của trẻ tới SMS; không gửi theo từng routine. Thông báo thuộc nhóm Routines; phụ huynh tắt nhóm Routines thì không nhận push, thông báo vẫn có trong Notifications (Q-86-09). |
| BR-007 | Ngày, giờ hiển thị theo múi giờ của Centre, định dạng dd/MM/yyyy và 24 giờ. |
| BR-013 | Loại routine bị HQ Admin tắt “Shown to parents” trên SMS (BBA-78 FR-007) không hiện trong Parents App: không có mục, không có chip lọc. Dữ liệu vẫn được ghi; bật lại thì phụ huynh thấy lại cả dữ liệu cũ (BBA-78 BR-004). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Phụ huynh chọn ngày sau hôm nay hoặc trước ngày bắt đầu học. | Không cho chọn; ngày ngoài khoảng bị mờ trên bộ chọn ngày. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-146: UI-US-001 - Routines (dòng thời gian) | https://bba-parents.lovable.app/routines |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Bộ chọn ngày | Chọn ngày | Có | Hôm nay | FR-002;VAL-001 | Đổi ngày; vuốt trái / phải để sang ngày trước / sau. |
| Bộ lọc loại | Chip | Không | All | FR-002;BR-003;BR-013 | Lọc theo loại routine đang bật. |
| Mục routine | Danh sách | — | Sắp theo giờ | FR-001;BR-002;BR-004;BR-013 | Biểu tượng loại, giờ, nội dung theo BR-002, ghi chú, ảnh. |
| Ảnh routine | Ảnh / mở | — | Ảnh thu nhỏ | BR-002 | Chạm để xem toàn màn hình. |
| Trạng thái trống | Thông điệp | — | Ẩn | FR-003;BR-005 | Lý do ngày trống hoặc “No … recorded on …”. |
| Try again | Thao tác | — | Ẩn | — | Hiện khi lỗi tải; tải lại. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Đọc routine theo trẻ và ngày từ dữ liệu Teacher App ghi (BBA-148), trừ routine đã xoá và loại routine đang tắt “Shown to parents” (BBA-78). Xem routine không tạo hay thay đổi dữ liệu. |
| DATA-002 | Ghi nhận đã gửi thông báo “Daily routines updated” theo trẻ, phụ huynh, ngày để không gửi lần hai trong ngày. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Giáo viên ghi Lunch “Most” lúc 11:45 và Nap 12:30–14:05 cho Emma hôm nay | Sarah mở Routines | hiện 2 mục theo giờ; Nap hiện thời lượng 1h 35m | FR-001;BR-002 |
| AC-002 | Emma có Lunch và Nap hôm nay | Sarah chọn chip Naps | chỉ hiện mục Nap | FR-002;BR-003 |
| AC-003 | Hôm nay Emma không có Bottle | Sarah chọn chip Bottles | hiện “No bottles recorded on <ngày hôm nay>.” | FR-002 |
| AC-004 | 25/12/2026 là Public holiday | Sarah chọn ngày 25/12/2026 | hiện “Public holiday”, không có mục nào | FR-003;BR-005 |
| AC-005 | Giáo viên đã xoá Bottle 10:00 của Emma | Sarah mở Routines | không có Bottle 10:00 | BR-004 |
| AC-006 | Emma được check-out lúc 17:30 | bản ghi check-out tới SMS | mỗi phụ huynh của Emma nhận đúng một thông báo “Daily routines updated”; chạm vào mở Routines của Emma ngày đó | FR-004;BR-006 |
| AC-007 | Sarah đang xem Routines | Sarah tìm thao tác sửa hoặc xoá một mục | không có thao tác sửa, xoá | BR-001 |
| AC-008 | Hôm nay là 26/11/2026 | Sarah mở bộ chọn ngày | không chọn được ngày sau 26/11/2026 | VAL-001 |
| AC-015 | HQ Admin tắt “Nappy & toilet” cho phụ huynh; giáo viên đã ghi Nappy 10:30 cho Emma | Sarah mở Routines | không có mục Nappy và không có chip Nappy & toilet | FR-001;BR-003;BR-013 |
| AC-016 | Sarah đã thấy Lunch “Most” của Emma; giáo viên sửa thành “Some” | Sarah mở lại Routines | Lunch hiện “Some”; Sarah không nhận thông báo mới | BR-004 |
| AC-017 | Sarah tắt nhóm thông báo Routines | Emma được check-out | Sarah không nhận push; thông báo “Daily routines updated” vẫn có trong Notifications | BR-006 |

#### Dependencies (Phụ thuộc)

Routine do Teacher App ghi (BBA-148); check-out (Attendance App, BBA-150); lịch Closure / Public holiday; nghỉ phép; chọn trẻ (BBA-145); cài đặt thông báo Parents App. Cài đặt “Shown to parents” (SMS, BBA-78).

### 6.2 BBA-146: US-002 - Note from home

#### User Story

Là phụ huynh, tôi muốn gửi giáo viên một ghi chú về con trong ngày (ngủ, ăn, tâm trạng), để giáo viên chăm con phù hợp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Hệ thống phải cho phụ huynh viết một Note from home cho trẻ trong ngày hiện tại. |
| FR-006 | Hệ thống phải cho phụ huynh sửa Note from home của ngày hiện tại và ghi lịch sử mỗi lần sửa. |

#### Functional Flow - Main (Luồng chính)

1. Phụ huynh mở Routines ngày hôm nay và chọn Add note.
2. Phụ huynh nhập ghi chú và chọn Save (FR-005). Hệ thống kiểm tra (VAL-002, VAL-003), lưu ghi chú và hiển thị kèm tên người viết, giờ lưu.
3. Giáo viên của lớp thấy ghi chú trên Teacher App (BBA-148).

#### Functional Flow - Alternative (Luồng thay thế)

1. Đã có Note from home hôm nay (của phụ huynh này hoặc phụ huynh còn lại): hiển thị ghi chú với thao tác Edit; phụ huynh sửa và Save (FR-006).
2. Phụ huynh chọn Cancel: không lưu.
3. Ngày đã chọn không phải hôm nay: hiển thị ghi chú (nếu có) ở dạng chỉ xem.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không lưu được: báo lỗi theo hành vi chuẩn, giữ nội dung đang nhập.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Mỗi trẻ có tối đa một Note from home mỗi ngày. Ghi chú thuộc về trẻ: mọi phụ huynh của trẻ thấy và sửa được ghi chú trong ngày. |
| BR-009 | Chỉ viết, sửa ghi chú cho ngày hiện tại (theo múi giờ của Centre), đến 23:59. Ghi chú các ngày trước chỉ xem. |
| BR-010 | Ghi chú dài 1–500 ký tự. |
| BR-011 | Nhân viên không sửa, không xoá Note from home. |
| BR-012 | Mỗi lần lưu ghi lịch sử: nội dung, người viết / sửa, thời điểm. Màn hình hiển thị người lưu gần nhất và thời điểm. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Ghi chú trống. | Nút Save không dùng được. |
| VAL-003 | Ghi chú quá 500 ký tự. | Không cho nhập thêm; hiện bộ đếm “500/500”. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-146: UI-US-002 - Khối Note from home trên Routines | https://bba-parents.lovable.app/routines |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Add note / Edit | Thao tác | — | Add note khi chưa có; Edit khi đã có; ẩn với ngày trước | FR-005;FR-006;BR-009 | Mở ô nhập ghi chú. |
| Note | Ô nhập nhiều dòng | Có | Trống hoặc nội dung hiện có | VAL-002;VAL-003;BR-010 | Nhập ghi chú; bộ đếm ký tự. |
| Người viết / thời điểm | Hiển thị | — | Theo lần lưu gần nhất | BR-012 | Ví dụ “Sarah · 07:45”. |
| Save / Cancel | Thao tác | — | Save mờ khi trống | VAL-002 | Lưu hoặc huỷ. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Lưu Note from home theo trẻ và ngày: nội dung, người viết, thời điểm; lịch sử mỗi lần sửa theo BR-012. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-009 | Emma chưa có ghi chú hôm nay | Sarah nhập “She slept late last night” và Save | ghi chú hiển thị với “Sarah · <giờ lưu>” | FR-005;BR-012 |
| AC-010 | Sarah đã viết ghi chú hôm nay | David mở Routines của Emma | David thấy ghi chú của Sarah và thao tác Edit, không có Add note | BR-008 |
| AC-011 | David sửa ghi chú lúc 08:10 | Sarah mở Routines | hiện nội dung mới với “David · 08:10”; lịch sử có cả hai lần lưu | FR-006;BR-012 |
| AC-012 | Emma có ghi chú hôm qua | Sarah chọn ngày hôm qua | ghi chú chỉ xem, không có Add note hay Edit | BR-009 |
| AC-013 | Sarah mở ô nhập và để trống | Sarah xem nút Save | Save không dùng được | VAL-002 |
| AC-014 | Sarah đã nhập 500 ký tự | Sarah gõ thêm | không nhập thêm được; bộ đếm hiện 500/500 | VAL-003 |

#### Dependencies (Phụ thuộc)

US-001; Teacher App đọc Note from home (BBA-148).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Nguồn | Giả định đang dùng | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Routine thêm hoặc sửa sau khi trẻ check-out có gửi lại thông báo cho phụ huynh không? | Q-86-09; BBA-78 OQ-03 | Không gửi lại; phụ huynh thấy giá trị mới khi mở Routines (BR-004). |  |
| OQ-02 | “Shown to parents” cấu hình theo level, Centre hay brand; ai được đổi? | Q-86-08; BBA-78 OQ-01 | HQ Admin cấu hình theo level (BBA-78 AS-01). |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Routine | Một hoạt động chăm sóc giáo viên ghi cho một trẻ. Phase 1: Meal, Bottle, Nap, Nappy / toilet. |
| Dòng thời gian | Danh sách routine của một ngày, sắp theo giờ. |
| Note from home | Ghi chú phụ huynh gửi giáo viên trong ngày; mỗi trẻ một ghi chú mỗi ngày. |
| Daily routines updated | Thông báo gửi phụ huynh một lần mỗi ngày khi trẻ được check-out. |
| Shown to parents | Cài đặt trên SMS bật / tắt từng loại routine hiện cho phụ huynh (BBA-78). |
