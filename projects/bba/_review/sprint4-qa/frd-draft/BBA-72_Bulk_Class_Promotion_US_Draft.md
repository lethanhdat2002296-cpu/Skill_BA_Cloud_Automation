# [Nháp] BBA-72 Move whole class up a level (bulk promotion) — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + SRS Children & Families (BR-CHF-048) + prototype SMS (Joining & leaving › Graduation). Không có câu trả lời Plane cho ticket này; prototype chưa có màn lên lớp.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-72/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. Gần như giữ nguyên — SRS chỉ có 1 quy tắc (BR-CHF-048) và FRD đã khớp.
2. Lớp ở level cao nhất (K2): gợi ý xử lý ở Joining & leaving › Graduation (đã có trong prototype) → cập nhật OQ-05.
3. Ngày trong ví dụ đổi sang năm học 2027: 01/01/2027 = ngày bắt đầu Term 1 năm 2027 của mọi brand (file "Centre Terms Setup.xlsx", Plane BBA-489). Dùng làm mặc định vẫn là giả định AS-01, chờ OQ-02.

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Ticket này là **annual promotion** (cuối năm, cả lớp lên level kế). Infant promotion (từng trẻ, 18 tháng tuổi) và class change (đổi lớp cùng level) là luồng khác; **K2 graduation là mass withdrawal**, chỉ K2 rời vào tháng 12 (Q-74-01, Q-74-06) → BR-007, đóng OQ-05.
- Chỉ trong cùng Centre; khác Centre / brand là Transfer (Q-74-02) → BR-006.
- Chọn cả cohort, bỏ tick ngoại lệ; trẻ ở lại giữ lớp hoặc chuyển lớp khác cùng level (Q-74-03) → FR-003.
- Capacity linh hoạt, CD cấu hình sĩ số từng lớp (Q-74-08); hoá đơn đã phát hành sửa bằng credit note (Q-74-09) — khớp.
- Lên lớp → thread trao đổi mới cho lớp mới, thread cũ chỉ đọc (Q-74-10) → FR-005.
- DOTB tự quyết: preview, lỗi từng phần, chạy lại (Q-74-11, 12, 13).
- Ngày hiệu lực mặc định: dùng ngày bắt đầu Term 1 năm sau theo lịch brand (Q-71-03, Q-74-07) — giả định AS-01.

---

## US-001 - Cho cả lớp lên level mới

#### User Story

Là Centre Director, tôi muốn chuyển cả lớp lên level tiếp theo cho năm học mới trong một lần, bỏ chọn được trẻ học lại, để không phải chuyển từng trẻ và không bỏ sót việc đổi học phí, danh sách điểm danh.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Ở chi tiết lớp, "Move class up" mở màn chuyển lớp với: lớp nguồn (lớp đang xem), level đích (mặc định level kế tiếp), lớp đích (các lớp của level đích, năm học mới, cùng Centre), ngày hiệu lực (mặc định ngày đầu năm học mới). |
| FR-002 | Màn xem trước liệt kê mọi trẻ đang học trong lớp nguồn: tên, level và lớp hiện tại, lớp đích, biểu phí hiện tại và biểu phí theo level mới; mỗi trẻ có ô chọn, mặc định được chọn. |
| FR-003 *(sửa)* | Người dùng bỏ chọn trẻ ngoại lệ (học lại, rút, gia hạn) và đổi lớp đích cho từng trẻ khi cần; trẻ bị bỏ chọn giữ lớp cũ hoặc được chuyển sang lớp khác cùng level bằng luồng class change (Q-74-03). |
| FR-004 | Xem trước hiện sĩ số lớp đích sau khi chuyển (ví dụ "18 of 20 after the move"); vượt sĩ số tối đa thì cảnh báo, người dùng vẫn tiếp tục được. |
| FR-005 *(sửa)* | "Confirm move" chuyển mọi trẻ được chọn từ ngày hiệu lực: cập nhật level và lớp trong ghi danh; áp biểu phí theo level mới cho các hoá đơn tạo sau ngày hiệu lực; đưa trẻ vào danh sách điểm danh của lớp đích; tạo thread trao đổi mới cho lớp mới, thread lớp cũ chuyển chỉ đọc và giữ tới khi trẻ rời trường (Q-74-10). |
| FR-006 | Trẻ bị bỏ chọn ở lại lớp nguồn, không thay đổi gì. |
| FR-007 | Mỗi trẻ được chuyển có một dòng lịch sử: lớp cũ, lớp mới, ngày hiệu lực, người thực hiện, thời điểm xác nhận. |
| FR-008 | Trước ngày hiệu lực, lớp của trẻ trên mọi màn hình vẫn là lớp cũ; từ ngày hiệu lực là lớp mới. |
| FR-009 | Sau khi chuyển, nếu lớp nguồn không còn trẻ nào, hệ thống đề xuất "Close this class"; lớp đã có trẻ chỉ được đóng, không xoá, lịch sử giữ nguyên. |
| FR-010 *(sửa)* | Lớp ở level cao nhất của Centre không có nút "Move class up"; K2 tốt nghiệp đi qua Joining & leaving › Graduation (mass withdrawal, reason graduation, chỉ K2 rời vào tháng 12) (Q-74-01). |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở lớp N2 · Sunbeams, chọn Move class up (FR-001).
2. Hệ thống đề xuất level K1, lớp đích và ngày đầu năm học mới.
3. Centre Director xem trước, bỏ chọn trẻ học lại (FR-002, FR-003, FR-004).
4. Centre Director chọn Confirm move; hệ thống chuyển trẻ và ghi lịch sử (FR-005, FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lớp đích vượt sĩ số: cảnh báo, Centre Director vẫn xác nhận được (FR-004).
2. Một số trẻ chuyển sang lớp đích khác (FR-003).
3. Lớp nguồn hết trẻ: Centre Director đóng lớp (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Chưa có lớp nào ở level đích cho năm học mới: không chuyển được (VAL-001).
2. Ngày hiệu lực trước hôm nay: không chuyển được (VAL-002).
3. Trẻ đã có một lần chuyển lớp chờ hiệu lực: trẻ bị bỏ chọn và ghi lý do (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Việc lên lớp có ngày hiệu lực; mọi thay đổi (lớp, level, học phí, điểm danh, nhóm trao đổi) bắt đầu từ ngày đó. |
| BR-002 | Hoá đơn đã phát hành không bị sửa; học phí theo level mới chỉ áp cho hoá đơn tạo sau ngày hiệu lực. |
| BR-003 | Vượt sĩ số tối đa chỉ cảnh báo, không chặn. |
| BR-004 | Lớp đã có trẻ không bị xoá, chỉ được đóng; lịch sử giữ nguyên. |
| BR-005 | Quyền cho lớp lên level theo Roles & permissions; mặc định Centre Director và HQ Admin. |
| BR-006 *(mới)* | Chỉ chuyển trong cùng Centre; khác Centre hoặc khác brand đi luồng Transfer (Q-74-02). |
| BR-007 *(mới)* | Màn này chỉ dùng cho annual promotion; Infant promotion và class change là luồng riêng (Q-74-01). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Level đích chưa có lớp nào cho năm học mới. | Không chuyển; hiện "Create a class for K1 in the new school year first." (tên level theo lựa chọn). |
| VAL-002 | Ngày hiệu lực trước hôm nay. | Không chuyển; hiện "The effective date cannot be in the past." |
| VAL-003 | Trẻ đã có một lần chuyển lớp chưa đến ngày hiệu lực. | Trẻ bị bỏ chọn, không chọn lại được; ghi "Already has a class change on" kèm ngày. |
| VAL-004 | Không còn trẻ nào được chọn. | Nút Confirm move bị mờ. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Target level | Danh sách chọn | Có | Level kế tiếp | VAL-001. | Chỉ các level Centre có mở. |
| Target class | Danh sách chọn | Có | Lớp đầu tiên của level đích | VAL-001. | Đổi được cho từng trẻ (FR-003); hiện sĩ số sau khi chuyển (FR-004). |
| Effective date | Ngày | Có | Ngày đầu năm học mới | VAL-002. | — |
| Danh sách trẻ | Bảng có ô chọn | Có | Tất cả được chọn | VAL-003; VAL-004. | Cột: Child, Current class, Target class, Fee schedule now, Fee schedule from (ngày hiệu lực) (FR-002). |
| Confirm move | Nút | Có | — | VAL-004. | FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi trẻ được chuyển lưu: lớp và level cũ, lớp và level mới, ngày hiệu lực, người thực hiện, thời điểm xác nhận. |
| DATA-002 | Mỗi lần cho lớp lên level lưu: lớp nguồn, số trẻ được chuyển, số trẻ ở lại, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 *(sửa)* | lớp N2 · Sunbeams có 16 trẻ, đã có lớp K1 · Honeycombs cho năm học 2027 | Centre Director chọn Move class up | level đích mặc định K1, lớp đích Honeycombs, ngày đầu năm học 2027; 16 trẻ được chọn sẵn | FR-001; FR-002 |
| AC-002 *(sửa)* | 2 trẻ học lại N2 | Centre Director bỏ chọn 2 trẻ và chọn Confirm move | 14 trẻ chuyển sang Honeycombs từ ngày hiệu lực; 2 trẻ ở lại Sunbeams | FR-003; FR-005; FR-006 |
| AC-003 *(sửa)* | lớp Honeycombs tối đa 20 trẻ, đã có 8 trẻ | xem trước 14 trẻ chuyển sang | hiện "22 of 20 after the move" kèm cảnh báo; vẫn xác nhận được | FR-004; BR-003 |
| AC-004 *(sửa)* | ngày hiệu lực 01/01/2027, hoá đơn tháng 1 chưa tạo | Centre Director xác nhận | hoá đơn tháng 1 của 14 trẻ dùng biểu phí K1 | FR-005; BR-002 |
| AC-005 *(sửa)* | ngày hiệu lực 01/01/2027, hôm nay 15/12/2026 | giáo viên mở danh sách điểm danh lớp Sunbeams ngày 20/12 | 14 trẻ vẫn ở lớp Sunbeams; từ 01/01/2027 trẻ ở lớp Honeycombs | FR-008; BR-001 |
| AC-006 | đã xác nhận | Centre Director mở lịch sử một trẻ | có dòng lớp cũ, lớp mới, ngày hiệu lực, người thực hiện | FR-007; DATA-001 |
| AC-007 | chưa có lớp K1 cho năm học mới | Centre Director chọn Move class up | hiện "Create a class for K1 in the new school year first." | VAL-001 |
| AC-008 | Centre Director chọn ngày hiệu lực hôm qua | chọn Confirm move | không chuyển, hiện "The effective date cannot be in the past." | VAL-002 |
| AC-009 | một trẻ đã có lần chuyển lớp hiệu lực 01/01/2027 | xem trước | trẻ đó bị bỏ chọn, ghi "Already has a class change on 01/01/2027" | VAL-003 |
| AC-010 | lớp Sunbeams không còn trẻ sau khi chuyển | Centre Director chọn Close this class | lớp chuyển trạng thái Closed, lịch sử giữ nguyên | FR-009; BR-004 |
| AC-011 | lớp K2 là level cao nhất | Centre Director mở chi tiết lớp K2 | không có nút Move class up | FR-010 |
| AC-012 | Teacher không có quyền cho lớp lên level | Teacher mở chi tiết lớp | không có nút Move class up | BR-005 |
| AC-013 | Centre Director bỏ chọn tất cả trẻ trong xem trước | nhìn nút Confirm move | nút bị mờ, không xác nhận được | VAL-004 |
| AC-014 *(mới)* | 14 trẻ đã chuyển sang Honeycombs từ 01/01/2027 | phụ huynh của một trẻ mở Messages ngày 05/01/2027 | thấy thread lớp Honeycombs mới; thread Sunbeams chỉ đọc | FR-005 |

#### Dependencies (Phụ thuộc)

Classes (lớp của năm học mới, sĩ số tối đa); level của Centre (Organisation); biểu phí theo level (Fees & Payments); danh sách điểm danh; nhóm trao đổi của lớp (Communication); Joining & leaving › Graduation (lớp K2).

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 | Việc cho lớp lên level có cần ai duyệt trước khi có hiệu lực không? | Mở |
| OQ-02 | Ngày hiệu lực mặc định, có cho lên lịch và huỷ trước ngày hiệu lực không? | Mở — Q-74-07 mới có bối cảnh (năm học 1–12, lập lớp tháng 11–12); ngày term theo file BBA-489 |
| OQ-03 | Trẻ đang tạm nghỉ (tối đa 3 tháng, vẫn trong hệ thống) có được chuyển cùng lớp không; trạng thái nào đủ điều kiện? | Mở — Q-74-06 chưa nói |
| OQ-04 | Phụ huynh / giáo viên có nhận thông báo khi lên lớp không; lớp cũ tự đóng hay đóng tay? | Mở — Q-74-15 chưa trả lời phần này |
| OQ-05 | Trẻ K2 cuối năm xử lý ở đâu? | **Đã chốt:** mass graduation qua withdrawal (Q-74-01) |
| OQ-06 *(mới)* | Biểu phí level mới áp từ ngày hiệu lực hay từ đầu tháng sau? | Mở (Q-74-09) |
| OQ-07 *(mới)* | Danh sách điểm danh chuyển ngay khi xác nhận hay tại ngày hiệu lực? | Mở (Q-74-10) |
| AS-01 *(sửa)* | Ngày hiệu lực mặc định là ngày bắt đầu Term 1 năm sau theo lịch term của brand (Q-71-03). | Chờ OQ-02 |
| AS-02 | Không cần duyệt. | Chờ OQ-01 |
| AS-03 | Trẻ đang tạm nghỉ có trong xem trước và được chuyển như trẻ khác. | Chờ OQ-03 |
