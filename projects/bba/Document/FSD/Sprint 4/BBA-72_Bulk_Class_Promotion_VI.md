# BBA-72 Move whole class up a level (bulk promotion) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Classes |
| Tính năng | Move whole class up a level (bulk promotion) |
| Mã ticket | BBA-72 |
| Mã WBS | 3.1.5.01 |
| Mã tài liệu | FRD-BBA-72 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-72: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc cho cả lớp lên level mới: chọn lớp đích và ngày hiệu lực, xem trước, bỏ chọn trẻ ở lại, xác nhận, cập nhật ghi danh, học phí theo level, danh sách điểm danh và lịch sử. 5 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Cuối mỗi năm học, Centre chuyển cả lớp lên level tiếp theo (ví dụ Nursery 1 lên Nursery 2) cho năm học mới. Thay vì chuyển từng trẻ, Centre Director chọn lớp, chọn lớp đích và ngày hiệu lực, xem trước danh sách trẻ, bỏ chọn trẻ học lại, rồi xác nhận một lần.

Mục tiêu đo được: chuyển xong một lớp trong một lần xác nhận; 100% trẻ được chuyển có lịch sử ghi lớp cũ, lớp mới, ngày hiệu lực và người thực hiện.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Chọn lớp nguồn, level đích, lớp đích, ngày hiệu lực. Xem trước trẻ bị ảnh hưởng, bỏ chọn trẻ học lại, đổi lớp đích cho từng trẻ. Xác nhận: cập nhật ghi danh, học phí theo level, danh sách điểm danh, nhóm trao đổi của lớp. Lịch sử từng trẻ. Đóng lớp cũ khi đã hết trẻ. | Chuyển một trẻ sang lớp khác giữa năm. Tốt nghiệp và rời trường của trẻ K2 (Joining & leaving). Tạo lớp mới cho năm học mới (làm trước ở Classes). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Centre Director | Centre của mình. | Cho lớp lên level mới, đóng lớp cũ (quyền mặc định). |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| School Admin | Centre của mình. | Theo quyền được cấp trong Roles & permissions. |
| Teacher | Lớp của mình. | Xem lớp mới của trẻ từ ngày hiệu lực. |
| Hệ thống | Toàn hệ thống. | Đề xuất level và lớp đích, cập nhật ghi danh, học phí, danh sách điểm danh, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Classes › chi tiết lớp | Cho cả lớp lên level mới. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Cho cả lớp lên level mới

#### User Story

Là Centre Director, tôi muốn chuyển cả lớp lên level tiếp theo cho năm học mới trong một lần, bỏ chọn được trẻ học lại, để không phải chuyển từng trẻ và không bỏ sót việc đổi học phí, danh sách điểm danh.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Ở chi tiết lớp, "Move class up" mở màn chuyển lớp với: lớp nguồn (lớp đang xem), level đích (mặc định level kế tiếp), lớp đích (các lớp của level đích, năm học mới, cùng Centre), ngày hiệu lực (mặc định ngày đầu năm học mới). |
| FR-002 | Màn xem trước liệt kê mọi trẻ đang học trong lớp nguồn: tên, level và lớp hiện tại, lớp đích, biểu phí hiện tại và biểu phí theo level mới; mỗi trẻ có ô chọn, mặc định được chọn. |
| FR-003 | Người dùng bỏ chọn trẻ học lại (ở lại level cũ) và đổi lớp đích cho từng trẻ khi cần. |
| FR-004 | Xem trước hiện sĩ số lớp đích sau khi chuyển (ví dụ "18 / 20"); vượt sĩ số tối đa thì cảnh báo, người dùng vẫn tiếp tục được. |
| FR-005 | "Confirm" chuyển mọi trẻ được chọn từ ngày hiệu lực: cập nhật level và lớp trong ghi danh; áp biểu phí theo level mới cho các hoá đơn tạo sau ngày hiệu lực; đưa trẻ vào danh sách điểm danh của lớp đích; chuyển trẻ từ nhóm trao đổi của lớp cũ sang lớp mới. |
| FR-006 | Trẻ bị bỏ chọn ở lại lớp nguồn, không thay đổi gì. |
| FR-007 | Mỗi trẻ được chuyển có một dòng lịch sử: lớp cũ, lớp mới, ngày hiệu lực, người thực hiện, thời điểm xác nhận. |
| FR-008 | Trước ngày hiệu lực, lớp của trẻ trên mọi màn hình vẫn là lớp cũ; từ ngày hiệu lực là lớp mới. |
| FR-009 | Sau khi chuyển, nếu lớp nguồn không còn trẻ nào, hệ thống đề xuất "Close this class"; lớp đã có trẻ chỉ được đóng, không xoá, lịch sử giữ nguyên. |
| FR-010 | Lớp ở level cao nhất của Centre không có nút "Move class up". |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở lớp Nursery 1 · Mickey, chọn Move class up (FR-001).
2. Hệ thống đề xuất level Nursery 2, lớp đích và ngày đầu năm học mới.
3. Centre Director xem trước, bỏ chọn trẻ học lại (FR-002, FR-003, FR-004).
4. Centre Director chọn Confirm; hệ thống chuyển trẻ và ghi lịch sử (FR-005, FR-007).

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

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Level đích chưa có lớp nào cho năm học mới. | Không chuyển; hiện "Create a class for Nursery 2 in the new school year first." (tên level theo lựa chọn). |
| VAL-002 | Ngày hiệu lực trước hôm nay. | Không chuyển; hiện "The effective date cannot be in the past." |
| VAL-003 | Trẻ đã có một lần chuyển lớp chưa đến ngày hiệu lực. | Trẻ bị bỏ chọn, không chọn lại được; ghi "Already has a class change on" kèm ngày. |
| VAL-004 | Không còn trẻ nào được chọn. | Nút Confirm bị mờ. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Move class up — chọn lớp đích và xem trước | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Level đích | Danh sách chọn | Có | Level kế tiếp | VAL-001. | Chỉ các level Centre có mở. |
| Lớp đích | Danh sách chọn | Có | Lớp đầu tiên của level đích | VAL-001. | Đổi được cho từng trẻ (FR-003). |
| Ngày hiệu lực | Ngày | Có | Ngày đầu năm học mới | VAL-002. | — |
| Danh sách trẻ | Bảng có ô chọn | Có | Tất cả được chọn | VAL-003; VAL-004. | FR-002. |
| Sĩ số lớp đích | Chữ | Có | Sau khi chuyển / tối đa | — | Cảnh báo khi vượt (FR-004). |
| Confirm | Nút | Có | — | VAL-004. | FR-005. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi trẻ được chuyển lưu: lớp và level cũ, lớp và level mới, ngày hiệu lực, người thực hiện, thời điểm xác nhận. |
| DATA-002 | Mỗi lần cho lớp lên level lưu: lớp nguồn, số trẻ được chuyển, số trẻ ở lại, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Nursery 1 · Mickey có 16 trẻ, đã có lớp Nursery 2 · Minnie cho năm học mới | Centre Director chọn Move class up | level đích mặc định Nursery 2, lớp đích Minnie, ngày đầu năm học mới; 16 trẻ được chọn sẵn | FR-001; FR-002 |
| AC-002 | 2 trẻ học lại Nursery 1 | Centre Director bỏ chọn 2 trẻ và chọn Confirm | 14 trẻ chuyển sang Minnie từ ngày hiệu lực; 2 trẻ ở lại Mickey | FR-003; FR-005; FR-006 |
| AC-003 | lớp Minnie tối đa 20 trẻ, đã có 8 trẻ | xem trước 14 trẻ chuyển sang | hiện "22 / 20" kèm cảnh báo; vẫn xác nhận được | FR-004; BR-003 |
| AC-004 | ngày hiệu lực 01/01/2027, hoá đơn tháng 1 chưa tạo | Centre Director xác nhận | hoá đơn tháng 1 của 14 trẻ dùng biểu phí Nursery 2 | FR-005; BR-002 |
| AC-005 | ngày hiệu lực 01/01/2027, hôm nay 15/12/2026 | giáo viên mở danh sách điểm danh lớp Mickey ngày 20/12 | 14 trẻ vẫn ở lớp Mickey; từ 01/01/2027 trẻ ở lớp Minnie | FR-008; BR-001 |
| AC-006 | đã xác nhận | Centre Director mở lịch sử một trẻ | có dòng lớp cũ Mickey, lớp mới Minnie, ngày hiệu lực, người thực hiện | FR-007; DATA-001 |
| AC-007 | chưa có lớp Nursery 2 cho năm học mới | Centre Director chọn Move class up | hiện "Create a class for Nursery 2 in the new school year first." | VAL-001 |
| AC-008 | Centre Director chọn ngày hiệu lực hôm qua | chọn Confirm | không chuyển, hiện "The effective date cannot be in the past." | VAL-002 |
| AC-009 | một trẻ đã có lần chuyển lớp hiệu lực 01/01/2027 | xem trước | trẻ đó bị bỏ chọn, ghi "Already has a class change on 01/01/2027" | VAL-003 |
| AC-010 | lớp Mickey không còn trẻ sau khi chuyển | Centre Director chọn Close this class | lớp chuyển trạng thái Closed, lịch sử giữ nguyên | FR-009; BR-004 |
| AC-011 | lớp K2 là level cao nhất | Centre Director mở chi tiết lớp K2 | không có nút Move class up | FR-010 |
| AC-012 | Teacher không có quyền cho lớp lên level | Teacher mở chi tiết lớp | không có nút Move class up | BR-005 |
| AC-013 | Centre Director bỏ chọn tất cả trẻ trong xem trước | nhìn nút Confirm | nút Confirm bị mờ, không xác nhận được | VAL-004 |

#### Dependencies (Phụ thuộc)

Classes (lớp của năm học mới, sĩ số tối đa); level của Centre (Organisation); biểu phí theo level (Fees & Payments); danh sách điểm danh; nhóm trao đổi của lớp (Communication).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Việc cho lớp lên level có cần ai duyệt (ví dụ HQ Ops) trước khi có hiệu lực không? | Centre Director / HQ Ops | Trung bình |  |
| OQ-02 | Ngày đầu năm học mới của mỗi quốc gia / brand là ngày nào? | HQ Ops | Cao |  |
| OQ-03 | Trẻ đang tạm nghỉ có được chuyển cùng lớp không? | Centre Director / HQ Ops | Trung bình |  |
| OQ-04 | Phụ huynh có nhận thông báo khi con được lên lớp không; nội dung là gì? | Centre Director / HQ Ops | Thấp |  |
| OQ-05 | Trẻ K2 cuối năm (tốt nghiệp) xử lý ở đâu: Joining & leaving hay một bước riêng ở đây? | Business Owner | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Ngày hiệu lực mặc định là ngày đầu năm học mới. | FR-001 — chờ OQ-02 |
| AS-02 | Không cần duyệt; xác nhận là có hiệu lực theo ngày đã chọn. | FR-005 — chờ OQ-01 |
| AS-03 | Trẻ đang tạm nghỉ có trong danh sách xem trước và được chuyển như trẻ khác. | FR-002 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Level | Cấp lớp theo độ tuổi, ví dụ Playgroup, Nursery 1, Nursery 2, K1, K2. |
| Ngày hiệu lực | Ngày việc chuyển lớp bắt đầu áp dụng. |
| Biểu phí theo level | Mức học phí áp cho trẻ theo level đang học. |
| Học lại | Trẻ ở lại level cũ thêm một năm. |
