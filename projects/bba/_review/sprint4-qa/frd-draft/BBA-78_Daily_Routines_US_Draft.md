# [Nháp] BBA-78 Daily routines – view & edit (web) — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + câu trả lời của BBA (Plane BBA-494) + SRS Daily Operations, Centre Director App, Teacher App + prototype SMS `/operations/routines` và CD app `/more/routines`.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-78/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. ~~Thêm Mood~~ → **bỏ lại**: BBA chốt 4 loại theo Taidii (Q-86-01). Mood chuyển sang OQ-05.
2. Mỗi mục ghi rõ **ai ghi, lúc nào, trên app nào** (prototype: "recorded by Grace Tan in the Teacher app").
3. Phụ huynh nhận thông báo routines **mỗi ngày một lần khi trẻ được trả** (SRS Daily Operations).
4. Bật / tắt từng loại cho phụ huynh (FR-007) **không có trong SRS** → giữ, chờ OQ-04.
5. Routines chạy được khi mất mạng là việc của Teacher App (BBA-494), không thuộc màn web này.

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Danh mục: Taidii và file export của BBA có **4 loại: Bottle, Food, Nap, Potty** (Q-86-01) → FR-001 bỏ Mood.
- Trường dữ liệu dùng lại như Taidii (Q-86-02); lỗi từng phần khi ghi cả lớp: DOTB tự quyết (Q-86-05).
- Ghi cả lớp: chỉnh ngoại lệ "cả 2" — trước và sau khi lưu (Q-86-04) → FR-003.
- Thông báo theo category, có Routines, phụ huynh chọn category muốn nhận (Q-86-09) → FR-012.
- Chưa phản hồi: backdated / future (Q-86-06), cài đặt hiện cho phụ huynh (Q-86-08), ghi chú từ gia đình (Q-86-10).

---

## US-001 - Xem và sửa sinh hoạt hằng ngày trên SMS web

#### User Story

Là Centre Director, tôi muốn xem sinh hoạt trong ngày của cả lớp, sửa khi giáo viên ghi nhầm và biết trẻ nào còn thiếu mục bắt buộc, để phụ huynh nhận được thông tin đầy đủ và đúng về ngày của con.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | Màn Daily routines chọn lớp và ngày (mặc định hôm nay); mỗi trẻ một dòng gồm 4 loại theo Taidii (Q-86-01, Q-86-02): Food (bữa, All / Most / Some / None, món ăn), Bottle (ml pha, ml uống), Nap (giờ bắt đầu, giờ kết thúc, thời gian ngủ, chất lượng), Potty (Diaper, Potty, Accident; Wet, BM, Dry); ghi chú từ gia đình. |
| FR-002 | Tìm theo tên trẻ; lọc theo lớp, mục còn thiếu, app đã ghi; sắp xếp theo tên trẻ hoặc giờ ghi gần nhất. |
| FR-003 *(sửa)* | "Record for the whole class" ghi một mục cho nhiều trẻ cùng lúc; người dùng bỏ chọn trẻ ngoại lệ trước khi lưu và chỉnh riêng từng trẻ sau khi lưu (Q-86-04). |
| FR-004 | Thời gian ngủ do hệ thống tính từ giờ bắt đầu và giờ kết thúc. |
| FR-005 | Sửa một mục ("Change time" hoặc mở chi tiết): đổi giờ hoặc chi tiết; lịch sử lưu giá trị cũ, giá trị mới, người sửa, thời điểm. |
| FR-006 | Mục bắt buộc được đặt theo level (mặc định Infant và Playgroup); trẻ còn thiếu mục bắt buộc trong ngày hiện chữ "Missing" kèm tên mục. |
| FR-007 *(chờ OQ-04)* | Cài đặt "Shown to parents": với mỗi loại sinh hoạt có bật / tắt hiện cho phụ huynh; loại bị tắt vẫn được ghi nhưng không hiện trong Parents App. |
| FR-008 | Phụ huynh chỉ thấy sinh hoạt của con mình, theo ngày, và chỉ các loại đang bật. Sửa một mục đã hiện cho phụ huynh thì phụ huynh thấy giá trị mới. |
| FR-009 | Xuất sinh hoạt theo khoảng ngày và lớp ra Excel. |
| FR-010 | Chỉ sửa được sinh hoạt trong giới hạn số ngày cho phép (AS-02); ngày sau hôm nay không ghi được. |
| FR-011 *(mới)* | Mỗi mục hiển thị giờ, người ghi và app đã ghi (SMS web, Teacher App, CD app), ví dụ "11:50 · recorded by Aisyah Rahman in the Teacher app". |
| FR-012 *(mới)* | Phụ huynh nhận thông báo "Daily routines updated" trong app mỗi ngày một lần, khi trẻ được trả; thông báo thuộc category Routines, phụ huynh tắt được category này (Q-86-09). |
| FR-013 *(mới)* | "Parent view" mở bản xem trước đúng như phụ huynh của một trẻ thấy trong Parents App. |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở Daily routines, chọn lớp và ngày (FR-001).
2. Centre Director lọc mục còn thiếu, thấy trẻ thiếu bữa trưa (FR-002, FR-006).
3. Centre Director nhắc giáo viên ghi bổ sung; giáo viên ghi trên màn này hoặc Teacher App.

#### Functional Flow - Alternative (Luồng thay thế)

1. Ghi bữa trưa cho cả lớp rồi chỉnh trẻ ăn ít (FR-003).
2. Sửa giờ ngủ ghi nhầm (FR-004, FR-005).
3. HQ Admin tắt một loại sinh hoạt khỏi Parents App cho một level (FR-007 — chờ OQ-04).
4. *(mới)* Centre Director xem trước những gì phụ huynh thấy (FR-013).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Giờ kết thúc ngủ trước giờ bắt đầu: không lưu (VAL-001).
2. Sữa uống nhiều hơn sữa pha: không lưu (VAL-002).
3. Ngày ngoài giới hạn sửa: chỉ xem (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mỗi mục ghi lưu người ghi; mỗi lần sửa lưu người sửa. |
| BR-002 | Phụ huynh chỉ thấy sinh hoạt của con mình. |
| BR-003 | Mục bắt buộc theo level; trẻ thiếu mục bắt buộc được đánh dấu trên màn lớp. |
| BR-004 | Tắt hiện cho phụ huynh không xoá dữ liệu; bật lại thì phụ huynh thấy lại. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Giờ kết thúc ngủ trước giờ bắt đầu. | Không lưu; hiện "The nap end time must be after the start time." |
| VAL-002 | Lượng sữa uống lớn hơn lượng sữa pha. | Không lưu; hiện "Amount drunk cannot be more than amount prepared." |
| VAL-003 | Ngày sau hôm nay hoặc ngoài giới hạn sửa. | Chỉ xem; không có nút ghi và sửa. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Class, Day | Danh sách chọn, ngày | Có | Lớp của người dùng, hôm nay | VAL-003. | — |
| Bảng sinh hoạt *(sửa)* | Bảng | Có | Mỗi trẻ một dòng | — | Cột: Child, Food, Bottle, Nap, Potty (FR-001; FR-006; FR-011). |
| Record for the whole class | Nút | Theo quyền | — | — | Chọn loại, giờ, chi tiết, trẻ (mặc định mọi trẻ đã đến) (FR-003). |
| Nap start / end | Giờ | Khi ghi giấc ngủ | — | VAL-001. | Tính thời gian ngủ (FR-004). |
| Milk prepared / drunk (ml) | Số | Khi ghi sữa | — | VAL-002. | — |
| Shown to parents *(chờ OQ-04)* | Bật / tắt theo loại | Có | Bật | — | FR-007. |
| Parent view *(mới)* | Nút | — | — | — | FR-013. |
| Export | Nút | Theo quyền | — | — | FR-009. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 *(sửa)* | Mỗi mục sinh hoạt lưu: trẻ, ngày, loại, chi tiết, giờ, người ghi, app đã ghi, thời điểm ghi. |
| DATA-002 | Mỗi lần sửa lưu giá trị cũ, giá trị mới, người sửa, thời điểm; mỗi lần đổi cài đặt hiển thị lưu người đổi và thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 *(sửa)* | lớp Bumblebees hôm nay có 16 trẻ | Centre Director mở Daily routines | mỗi trẻ một dòng với Food, Bottle, Nap, Potty, ghi chú từ gia đình | FR-001 |
| AC-002 | giáo viên ghi bữa trưa "All" cho cả lớp | giáo viên chỉnh Caleb thành "Some" | 15 trẻ "All", Caleb "Some" | FR-003 |
| AC-003 | giờ ngủ 13:00 đến 14:30 | lưu | thời gian ngủ hiện 1h 30m | FR-004 |
| AC-004 | Centre Admin sửa giờ ngủ từ 13:00 thành 13:15 | lưu | lịch sử ghi 13:00 → 13:15, người sửa, thời điểm | FR-005; BR-001; DATA-002 |
| AC-005 *(sửa)* | Playgroup bắt buộc ghi bữa trưa, Caleb chưa có | Centre Director lọc mục còn thiếu | Caleb hiện "Missing: Lunch" | FR-002; FR-006; BR-003 |
| AC-006 | HQ Admin tắt "Nappy and toilet" cho phụ huynh | phụ huynh mở sinh hoạt của con | không thấy mục thay tã; giáo viên vẫn ghi được | FR-007; BR-004 |
| AC-007 | phụ huynh của Caleb mở Parents App | xem sinh hoạt hôm nay | chỉ thấy sinh hoạt của Caleb | FR-008; BR-002 |
| AC-008 | giờ kết thúc ngủ 12:50, bắt đầu 13:00 | lưu | không lưu, hiện "The nap end time must be after the start time." | VAL-001 |
| AC-009 | sữa pha 150 ml | nhập sữa uống 180 ml | không lưu, hiện "Amount drunk cannot be more than amount prepared." | VAL-002 |
| AC-010 | ngày ngoài giới hạn sửa | Centre Admin mở ngày đó | chỉ xem, không có nút ghi và sửa | FR-010; VAL-003 |
| AC-011 | Centre Admin chọn lớp Bumblebees, tuần trước | chọn Export | file Excel có sinh hoạt của lớp trong tuần đó | FR-009 |
| AC-012 *(mới)* | Aisyah ghi bữa trưa của Mia lúc 11:50 trên Teacher App | Centre Director mở Daily routines | mục bữa trưa của Mia ghi "11:50 · recorded by Aisyah Rahman in the Teacher app" | FR-011; DATA-001 |
| AC-013 *(mới)* | Mia được trả lúc 17:30 | lượt trả được lưu | phụ huynh của Mia nhận một thông báo "Daily routines updated" trong ngày | FR-012 |

#### Dependencies (Phụ thuộc)

Teacher App (ghi sinh hoạt, chạy được khi mất mạng — BBA-494); CD app; ghi chú từ gia đình (Parents App); danh sách lớp; lượt trả trẻ (BBA-73); Parents App (xem sinh hoạt).

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 | Cài đặt "Shown to parents" đặt theo level, theo Centre hay toàn brand; ai được đổi? | Mở — phụ thuộc OQ-04 |
| OQ-02 | Được sửa sinh hoạt lùi về tối đa bao nhiêu ngày? | Mở |
| OQ-03 | Thêm / sửa routines sau khi trả trẻ có báo lại phụ huynh không? | Mở (Q-86-09 chưa trả lời phần này) |
| OQ-04 *(mới)* | Có cần bật / tắt từng loại sinh hoạt cho phụ huynh không; cấu hình theo cấp nào? SRS chỉ nói phụ huynh thấy routines của con theo ngày. | Mở — cao (Q-86-08 chưa trả lời) |
| OQ-05 *(mới)* | Mood: SRS CD app và prototype có, Taidii và file export của BBA không có (Q-86-01). Bỏ Mood ở Phase 1? | Mở |
| OQ-06 *(mới)* | Ghi cả lớp: trẻ vắng / nghỉ phép có được áp không? | Mở (Q-86-04 trả lời chưa rõ) |
| OQ-07 *(mới)* | Có cho ghi routines ngày trước / ngày sau không? | Mở (Q-86-06) |
| OQ-08 *(mới)* | Ghi chú từ gia đình có hiện trên màn lớp và gắn với ngày không? | Mở (Q-86-10) |
| AS-01 | HQ Admin đặt "Shown to parents" theo level. | Chờ OQ-01, OQ-04 |
| AS-02 | Sửa được sinh hoạt trong 7 ngày gần nhất. | Chờ OQ-02 |
| AS-03 | Sửa mục đã hiện cho phụ huynh không gửi thông báo. | Chờ OQ-03 |
| AS-04 *(mới)* | Nút "Parent view" trên prototype là bản xem trước như phụ huynh thấy (FR-013). | Chờ xác nhận |
