# BBA-80 Payment schedule – edit per child (program type, amounts, effective period) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › Payment schedule |
| Tính năng | Payment schedule – edit per child (program type, amounts, effective period) |
| Mã ticket | BBA-80 |
| Mã WBS | 3.6.7.01 |
| Mã tài liệu | FRD-BBA-80 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-80: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả lịch phí của từng trẻ: loại chương trình, các khoản tiền, thời gian hiệu lực, trạng thái Set / Not Set, chặn trùng thời gian và ảnh hưởng tới việc tạo hoá đơn. 4 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Mỗi trẻ có một hoặc nhiều lịch phí: trẻ học chương trình nào (Full Day, Half Day…), phí bao nhiêu, được trừ trợ cấp, hỗ trợ tài chính và giảm giá bao nhiêu, thuế GST bao nhiêu, áp dụng từ ngày nào đến ngày nào. Hoá đơn hằng tháng được tạo từ lịch phí này. Finance cần xem và sửa lịch phí của từng trẻ, và biết trẻ nào chưa có lịch phí trước ngày tạo hoá đơn.

Mục tiêu đo được: trước mỗi kỳ tạo hoá đơn, Finance thấy danh sách 100% trẻ đang học chưa có lịch phí cho tháng đó.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Lịch phí của từng trẻ: loại chương trình, tên lịch phí, phí gốc (nett), trợ cấp (subsidy), trợ cấp thêm (additional subsidy), hỗ trợ tài chính (FA), giảm giá, GST, số tiền phải trả, ghi chú, trạng thái Set / Not Set, thời gian hiệu lực. Thêm, sửa, kết thúc lịch phí. Danh sách trẻ Not Set. Lịch sử. | Áp mẫu lịch phí cho nhiều trẻ (BBA-81), cập nhật hàng loạt (BBA-82). Thiết lập trợ cấp của trẻ (BBA-95). Thứ tự tính GST / giảm giá / trợ cấp (BBA-87). Chạy tạo hoá đơn. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Finance | Quốc gia / pháp nhân. | Thêm, sửa, kết thúc lịch phí. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Centre Director, Centre Admin / School Admin | Centre của mình. | Xem lịch phí; không sửa (chỉ Finance đổi phí). |
| Hệ thống | Toàn hệ thống. | Lấy giá theo bảng giá, tính số tiền phải trả, xác định Set / Not Set, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Fees & payments › Settings › Payment schedule | Lịch phí của từng trẻ. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Sửa lịch phí của từng trẻ

#### User Story

Là nhân viên Finance, tôi muốn xem và sửa lịch phí của từng trẻ theo chương trình và thời gian hiệu lực, và biết trẻ nào chưa có lịch phí, để hoá đơn hằng tháng tính đúng và không trẻ nào bị sót.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Danh sách lịch phí theo năm: trẻ, Centre, lớp, loại chương trình, tên lịch phí, nett, subsidy, additional subsidy, FA, discount, GST, amount, trạng thái, hiệu lực từ – đến, ghi chú. Tìm theo tên trẻ; lọc theo Centre, lớp, loại chương trình, trạng thái. |
| FR-002 | Loại chương trình gồm: Full Day, Half Day AM, Half Day PM, Flexi Care, Emergency, Sessions, Extended, Holiday và các loại khác Finance thêm vào danh sách. |
| FR-003 | Thêm lịch phí cho một trẻ: chọn loại chương trình, hiệu lực từ (bắt buộc), hiệu lực đến (không bắt buộc); nett lấy mặc định từ bảng giá theo brand, level, chương trình và quốc tịch của trẻ. |
| FR-004 | Subsidy, additional subsidy và FA lấy từ thiết lập trợ cấp của trẻ (BBA-95) và chỉ hiển thị ở đây. Discount lấy từ giảm giá đã duyệt của trẻ. |
| FR-005 | Amount do hệ thống tính từ nett, discount, subsidy, additional subsidy, FA và GST theo thứ tự tính trong General settings (BBA-87); người dùng không sửa tay. |
| FR-006 | Finance sửa được nett của một trẻ khác với bảng giá; khi đó ghi chú là bắt buộc. |
| FR-007 | Trẻ có trạng thái "Set" cho một tháng khi có ít nhất một lịch phí còn hiệu lực trong tháng đó; ngược lại là "Not Set". Bộ lọc "Not Set for" kèm tháng liệt kê trẻ đang học chưa có lịch phí. |
| FR-008 | Thay đổi phí là tạo lịch phí mới có ngày hiệu lực; lịch phí cũ kết thúc vào ngày trước đó. Lịch phí đã dùng để phát hành hoá đơn không bị xoá. |
| FR-009 | Lịch sử mỗi lịch phí: thêm, sửa, kết thúc, giá trị cũ, giá trị mới, người thực hiện, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Finance lọc "Not Set for" tháng sau, thấy trẻ chưa có lịch phí (FR-007).
2. Finance mở trẻ, thêm lịch phí Full Day từ ngày đầu tháng (FR-003).
3. Hệ thống lấy nett từ bảng giá, trợ cấp từ thiết lập trợ cấp, tính amount (FR-004, FR-005); trẻ chuyển "Set".

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ đổi từ Half Day sang Full Day từ tháng sau: tạo lịch phí mới, lịch cũ tự kết thúc (FR-008).
2. Phí riêng cho một trẻ: sửa nett, nhập ghi chú (FR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Hai lịch phí cùng loại chương trình trùng thời gian: không lưu (VAL-001).
2. Hiệu lực đến trước hiệu lực từ: không lưu (VAL-002).
3. Sửa nett không có ghi chú: không lưu (VAL-003).
4. Ngày hiệu lực rơi vào tháng đã khoá sổ: không lưu (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Chỉ Finance và HQ Admin đổi phí; Centre chỉ xem. |
| BR-002 | Đổi phí là lịch phí mới có ngày hiệu lực; không sửa lùi lịch phí đã dùng cho hoá đơn đã phát hành. |
| BR-003 | Một trẻ không có hai lịch phí cùng loại chương trình trùng thời gian. |
| BR-004 | Trẻ Not Set cho tháng nào thì không có hoá đơn học phí tháng đó và được liệt kê trong báo cáo thay đổi của kỳ tạo hoá đơn. |
| BR-005 | Tháng đã khoá sổ không thay đổi được. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Lịch phí mới trùng thời gian với lịch phí cùng loại chương trình của trẻ. | Không lưu; hiện "This child already has a Full Day schedule in this period." (theo loại chương trình). |
| VAL-002 | Hiệu lực đến trước hiệu lực từ. | Không lưu; hiện "The end date must be after the start date." |
| VAL-003 | Nett khác bảng giá mà không có ghi chú. | Không lưu; hiện "Enter a remark for the changed fee." |
| VAL-004 | Ngày hiệu lực trong tháng đã khoá sổ. | Không lưu; hiện "This month is closed." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Payment schedule — danh sách và chi tiết | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Loại chương trình | Danh sách chọn | Có | — | VAL-001. | FR-002. |
| Tên lịch phí | Ô nhập | Có | Theo loại chương trình | — | — |
| Nett | Số tiền | Có | Theo bảng giá | VAL-003. | FR-006. |
| Subsidy, additional subsidy, FA, discount | Số tiền | — | Theo thiết lập | — | Chỉ hiển thị (FR-004). |
| GST, amount | Số tiền | — | Hệ thống tính | — | FR-005. |
| Hiệu lực từ / đến | Ngày | Từ: có | — | VAL-002; VAL-004. | — |
| Ghi chú | Ô nhập | Khi sửa nett | Trống | VAL-003. | — |
| Not Set for | Bộ lọc tháng | Không | Tháng sau | — | FR-007. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lịch phí lưu: trẻ, loại chương trình, tên, nett, nguồn nett (bảng giá / sửa tay), các khoản trừ, GST, amount, hiệu lực từ – đến, ghi chú, người tạo. |
| DATA-002 | Mọi thay đổi lưu giá trị cũ, giá trị mới, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | trẻ mới chưa có lịch phí cho tháng 12 | Finance lọc "Not Set for" tháng 12 | trẻ có trong danh sách | FR-001; FR-007 |
| AC-002 | bảng giá Full Day N2 cho công dân Singapore có giá | Finance thêm lịch phí Full Day cho trẻ N2 công dân Singapore | nett điền sẵn theo bảng giá; subsidy, FA lấy từ thiết lập trợ cấp; amount do hệ thống tính; trẻ chuyển Set | FR-002; FR-003; FR-004; FR-005 |
| AC-003 | trẻ có Full Day từ 01/01/2027 không có ngày kết thúc | Finance thêm Full Day thứ hai từ 01/03/2027 | không lưu, hiện thông báo trùng thời gian | VAL-001; BR-003 |
| AC-004 | trẻ Half Day đến hết tháng 12 | Finance thêm Full Day từ 01/01/2027 | Half Day kết thúc 31/12/2026, Full Day bắt đầu 01/01/2027 | FR-008; BR-002 |
| AC-005 | Finance đổi nett khác bảng giá, để trống ghi chú | lưu | không lưu, hiện "Enter a remark for the changed fee." | FR-006; VAL-003 |
| AC-006 | trẻ Not Set cho tháng 12 | chạy tạo hoá đơn tháng 12 | trẻ không có hoá đơn học phí và có trong báo cáo thay đổi kèm lý do "No payment schedule" | BR-004 |
| AC-007 | tháng 10 đã khoá sổ | Finance tạo lịch phí hiệu lực từ 15/10 | không lưu, hiện "This month is closed." | VAL-004; BR-005 |
| AC-008 | Centre Director mở lịch phí của trẻ | xem | thấy đủ thông tin, không có nút sửa | BR-001 |
| AC-009 | lịch phí đã sửa nett | Finance mở lịch sử | thấy giá trị cũ, giá trị mới, người sửa, thời điểm | FR-009; DATA-002 |
| AC-010 | Finance nhập hiệu lực đến 01/01 trước hiệu lực từ 01/02 | lưu | không lưu, hiện "The end date must be after the start date." | VAL-002 |

#### Dependencies (Phụ thuộc)

Bảng giá (Fee items & prices); thiết lập trợ cấp (BBA-95); giảm giá đã duyệt (BBA-86); thứ tự tính (BBA-87); chạy tạo hoá đơn; khoá sổ tháng.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Danh sách đầy đủ các loại chương trình (dấu "…" trong yêu cầu) là gì? | BBA Finance | Cao |  |
| OQ-02 | Một trẻ có được học hai chương trình cùng lúc (ví dụ Full Day và Holiday) không? | BBA Finance | Trung bình |  |
| OQ-03 | Finance có được sửa nett riêng cho một trẻ không, hay phải tạo giảm giá? | BBA Finance | Cao |  |
| OQ-04 | Subsidy, FA hiển thị ở lịch phí là số theo tháng hay theo kỳ? | BBA Finance | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Hai loại chương trình khác nhau được trùng thời gian; cùng loại thì không. | BR-003 — chờ OQ-02 |
| AS-02 | Finance sửa được nett riêng cho một trẻ, có ghi chú bắt buộc. | FR-006 — chờ OQ-03 |
| AS-03 | Subsidy, additional subsidy, FA chỉ sửa ở thiết lập trợ cấp, không sửa ở lịch phí. | FR-004 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lịch phí (payment schedule) | Thiết lập phí của một trẻ cho một chương trình trong một thời gian; là cơ sở tạo hoá đơn. |
| Nett | Phí gốc trước các khoản trừ và thuế. |
| Subsidy / additional subsidy | Trợ cấp cơ bản / trợ cấp thêm của nhà nước cho trẻ. |
| FA (financial assistance) | Hỗ trợ tài chính cho gia đình. |
| GST | Thuế hàng hoá và dịch vụ. |
| Khoá sổ tháng | Tháng đã đóng; không tạo, sửa hay huỷ gì trong tháng đó. |
