# BBA-67 US-004 Tab Finance – bản nháp (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Child record |
| Tính năng | 3.1.1.02 Child record tabs – Read views › Tab Finance (US-004) |
| Mã ticket | BBA-67 |
| Mã WBS | 3.1.1.02 |
| Mã tài liệu | FRD-3.1_Child_Record_Read_Tabs — bản nháp US-004 |
| Sprint | 4 |
| Phiên bản | 0.2 (nháp) |
| Trạng thái | BẢN NHÁP ĐỂ RÀ SOÁT |
| Ngày | 11/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 (nháp) | 11/11/2026 | Business Analysis | Bản nháp đầu theo SRS Fees & Payments, Children & Families, Parents App: 9 khối chi tiết. | HaiNguyen |
| 0.2 (nháp) | 11/11/2026 | Business Analysis | Thu gọn thành màn tổng quan: 3 số tóm tắt, mục "Cần chú ý", payment method một dòng mỗi tài khoản, tối đa 6 hoá đơn gần nhất, cọc và hoàn tiền đang xử lý, giảm giá và trợ cấp. Bỏ khỏi tab: chi tiết từng dòng hoá đơn, bảng biên lai, bảng credit note, sổ biến động cọc, DDA reference, cách đăng ký GIRO — xem ở Billing qua liên kết. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả màn tổng quan 6 khối, quyền xem theo vai trò, 15 quy tắc, 15 tiêu chí nghiệm thu. 7 điểm chưa chốt ghi thành giả định và câu hỏi ở mục 6.

## 2. Mục đích và phạm vi

| Điểm chính | Căn cứ |
|---|---|
| Tab Finance là **bảng tổng quan** tài chính của một trẻ: nhìn vào là biết trẻ còn nợ bao nhiêu, có gì cần chú ý, trả bằng gì. Không phải nơi xem sổ sách chi tiết. | Định hướng của BA phụ trách |
| Trả lời nhanh 4 câu phụ huynh hay hỏi: "con còn nợ bao nhiêu", "sao tháng này hoá đơn cao", "tiền cọc còn bao nhiêu", "sao chưa trừ GIRO". | Định hướng của BA phụ trách |
| Chi tiết (từng dòng hoá đơn, biên lai, credit note, sổ cọc, tài khoản GIRO đầy đủ) xem ở màn Billing của Fees & Payments; mỗi khối có liên kết "Open in Billing". | SRS Fees & Payments §4 mục 3.2, 3.4, 4.1, 4.6, 5.1, 5.2 (tr.7–10) |
| Tab **chỉ đọc**. Tạo, sửa hoá đơn, credit note, hoàn tiền, tài khoản GIRO làm hoặc duyệt trong Billing bởi Finance. | BR-FEE-007, 008 (tr.12); BR-FEE-027, 041 (tr.13–14) |
| Các con số dùng cùng cách tính với Parents App (số còn nợ, credit còn lại tách CDA, trạng thái GIRO) để Centre trả lời khớp với những gì phụ huynh thấy. | SRS Parents App §4 mục 7.1, 7.4 (tr.13–14) |

**Ngoài phạm vi tab:** chi tiết từng dòng hoá đơn, danh sách biên lai, danh sách credit note, sổ biến động cọc, DDA reference và cách đăng ký GIRO, lịch sử nhắc nợ đầy đủ, tải hoặc in PDF, mọi thao tác.

## 3. Những gì thay đổi so với bản nháp 0.1

| Khối | Bản nháp 0.1 | Bản nháp 0.2 (tổng quan) |
|---|---|---|
| Tóm tắt | 3 số. | Giữ 3 số. |
| Cần chú ý | Không có. | Thêm: chỉ hiện khi có việc — hoá đơn quá hạn, GIRO trừ thất bại, tài khoản GIRO bị từ chối, hoàn tiền thất bại, nguy cơ mất trợ cấp, chênh lệch GSII chưa xử lý. |
| Payment method | Bảng tài khoản 6 cột. | Một dòng mỗi tài khoản: loại, ngân hàng, 4 số cuối, trạng thái (lý do nếu Rejected). |
| Hoá đơn | Mọi hoá đơn, 10 trường, mở rộng xem từng dòng. | Tối đa 6 hoá đơn: các hoá đơn chưa trả hết và hoá đơn mới nhất; 5 trường; một dòng "What changed from last month" dưới hoá đơn tháng mới nhất. Không mở rộng chi tiết. |
| Biên lai, credit note | Hai bảng riêng. | Bỏ khỏi tab; credit còn lại nằm ở tóm tắt; xem chi tiết ở Billing. |
| Cọc, hoàn tiền | Sổ biến động cọc; bảng hoàn tiền. | Một dòng cọc (số tiền, nguồn, số tháng); hoàn tiền chỉ hiện khi đang xử lý hoặc thất bại. |
| Giảm giá, trợ cấp | Bảng, cảnh báo, GSII. | Một dòng mỗi khoản; cảnh báo trợ cấp và GSII chuyển lên "Cần chú ý". |

## 4. Quyền xem theo vai trò

| Vai trò | Thấy tab Finance | Phạm vi | Căn cứ |
|---|---|---|---|
| HQ Admin, HQ Finance | Có | Mọi Centre | SRS Fees & Payments §2 (tr.3) |
| Centre Director, Centre Admin / School Admin | Có | Centre của mình | SRS Fees & Payments §2 (tr.3) |
| HQ Enrolment | Theo quyền | Mọi Centre | FRD v0.6 mục 4 |
| Teacher | Không (giả định) | — | AS-FIN-04, chờ Q-FIN-04 |
| Enrichment Trainer | Không | — | FRD v0.6 mục 4 |
| Parent | Không dùng tab này; xem trong Parents App | — | SRS Parents App §4 mục 7 |

## 5. Yêu cầu chức năng

### 5.1 US-004 - Tab Finance: tổng quan tài chính của trẻ

#### User Story

Là Centre Director hoặc School Admin, tôi muốn nhìn vào hồ sơ trẻ là biết trẻ còn nợ bao nhiêu, có việc gì cần chú ý (quá hạn, GIRO thất bại, nguy cơ mất trợ cấp), trẻ trả bằng gì và cọc còn bao nhiêu, để trả lời phụ huynh ngay mà không phải vào Billing.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-022 | Tab Finance là màn tổng quan, chỉ hiển thị; không có thao tác. Mỗi khối có liên kết "Open in Billing" mở màn tương ứng của Fees & Payments đã lọc theo trẻ (Invoices, GIRO accounts, Deposit ledger, Refunds, Discounts, GSII) (AS-FIN-06). |
| FR-023 | Khối **Tóm tắt** gồm 3 số: Outstanding (tổng số dư các hoá đơn Billed chưa trả hết), Credit remaining (credit chưa dùng, ghi riêng phần CDA), Deposit held (cọc đang giữ, ghi riêng phần CDA). |
| FR-024 | Khối **Cần chú ý** chỉ hiện khi có ít nhất một việc; mỗi việc một dòng ngắn kèm liên kết sang màn Billing: hoá đơn quá hạn (số hoá đơn, số ngày quá hạn, số tiền, các ngày đã nhắc); GIRO trừ thất bại (hoá đơn, ngày, lý do ngân hàng); tài khoản GIRO bị Rejected (lý do); hoàn tiền Unsuccessful (lý do); trẻ Singapore đã qua ngày kiểm tra (mặc định ngày 18) mà chưa có ngày đi học nào trong tháng; chênh lệch GSII chưa xử lý. |
| FR-025 | Khối **Payment method**: phương thức của trẻ (GIRO, GIRO CDA hoặc PayNow), Bill to (Parent / tên công ty), mỗi tài khoản GIRO một dòng: loại (GIRO / CDA), ngân hàng, số tài khoản che chỉ còn 4 số cuối, trạng thái (Pending with bank / Active / Rejected kèm lý do). |
| FR-026 | Khối **Invoices** hiện tối đa 6 hoá đơn: mọi hoá đơn chưa trả hết, rồi các hoá đơn mới nhất cho đủ 6 (AS-FIN-07). Mỗi dòng: tháng, loại (School fees / Enrichment / Registration / Ad hoc), số tiền, số dư, trạng thái ("Due 5 Nov", "Overdue · 34 days", "Paid", "Draft"), trạng thái GIRO nếu có ("GIRO deduction scheduled · 5 Nov", "Being collected by GIRO", "GIRO deduction failed"), nhãn CDA nếu là hoá đơn CDA. Liên kết "View all invoices" mở Fees & Payments › Invoices. Tab không mở chi tiết từng dòng hoá đơn. |
| FR-027 | Dưới hoá đơn học phí tháng mới nhất có một dòng "What changed from last month" lấy từ change report của đợt tính phí (ví dụ "Additional subsidy ended 30 Sep"); không có thay đổi thì không hiện dòng này. |
| FR-028 | Khối **Deposit & refunds**: một dòng cọc (số tiền đang giữ, nguồn CDA / non-CDA, số tháng cọc, ghi "+1 month, not on GIRO" khi trẻ không trả bằng GIRO); hoàn tiền chỉ hiện khi chưa xong (Pending approval, Approved, Processing) hoặc thất bại: số tiền, trạng thái, nơi nhận (CDA / PayNow). |
| FR-029 | Khối **Discounts & subsidies**: mỗi giảm giá đang áp một dòng (tên, giá trị, đến ngày); trợ cấp Basic / Additional một dòng (số tiền mỗi tháng). |
| FR-030 | Trẻ ở Centre Singapore chỉ thấy SGD và phương thức của Singapore; trẻ ở Centre Malaysia chỉ thấy MYR và phương thức của Malaysia, không có tài khoản GIRO / CDA, trợ cấp ECDA, GSII. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Finance; hệ thống hiển thị Tóm tắt, Cần chú ý (nếu có), Payment method, Invoices, Deposit & refunds, Discounts & subsidies (FR-023 đến FR-029).
2. Người dùng đọc số còn nợ và việc cần chú ý để trả lời phụ huynh (FR-023, FR-024).
3. Cần xem chi tiết hoặc thao tác: người dùng chọn "Open in Billing" hoặc "View all invoices" (FR-022, FR-026).

#### Functional Flow - Alternative (Luồng thay thế)

1. Không có việc cần chú ý: không hiện khối Cần chú ý (FR-024).
2. Hoá đơn tháng mới nhất khác tháng trước: hiện dòng "What changed from last month" (FR-027).
3. Trẻ ở Centre Malaysia: không có tài khoản GIRO / CDA, trợ cấp ECDA, GSII (FR-030; VAL-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò không được xem tab Finance: không có tab (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-FIN-TAB-001 | Tab chỉ đọc. Tạo, sửa hoá đơn, credit note, hoàn tiền, tài khoản GIRO làm hoặc duyệt trong Billing bởi Finance (BR-FEE-007, 008, 027, 041). |
| BR-FIN-TAB-002 | Outstanding = tổng số dư các hoá đơn Billed chưa trả hết (Billed, Partially paid, Overdue); không tính Draft và Void (BR-FEE-006; SRS Parents App §4 mục 7.1). |
| BR-FIN-TAB-003 | Overdue tính từ ngày đến hạn (mặc định ngày 5 của tháng hoá đơn) và thanh toán, không đặt tay (BR-FEE-003, 006). |
| BR-FIN-TAB-004 | Payment method thuộc hồ sơ trẻ: GIRO, GIRO CDA hoặc PayNow; ngoài ra trả tay bằng bank transfer, AXS, cheque. Mỗi hoá đơn mang theo phương thức để Finance lọc (thông tin BBA đã chốt; BR-FEE-037). |
| BR-FIN-TAB-005 | Một trẻ có tối đa 2 tài khoản GIRO: CDA và non-CDA; CDA và non-CDA xuất hoá đơn riêng (thông tin BBA đã chốt; BR-FEE-030 — chờ Q-FIN-01). |
| BR-FIN-TAB-006 | Số tài khoản ngân hàng luôn che, chỉ hiện 4 số cuối (SRS Fees & Payments §4 mục 4.1 Mask account number). |
| BR-FIN-TAB-007 | Hoá đơn trong đợt 1ST DD chưa có kết quả hiện "Being collected by GIRO"; GIRO thất bại giữ hoá đơn chưa trả và có lý do của ngân hàng (BR-FEE-033, 034). |
| BR-FIN-TAB-008 | Phụ huynh có hoá đơn Billed chưa trả được nhắc trong app ngày 15 và 25, tối đa 2 lần mỗi kỳ (BR-FEE-004). |
| BR-FIN-TAB-009 | Học phí và enrichment là hai hoá đơn riêng (BR-FEE-011). |
| BR-FIN-TAB-010 | Nguồn của mọi khoản cọc (CDA / non-CDA) được ghi. Trẻ không trả bằng GIRO cọc thêm 1 tháng; số tháng cọc cài theo brand và Centre (BR-FEE-021, 022). |
| BR-FIN-TAB-011 | Tiền trả từ CDA chỉ hoàn về CDA; hoàn tiền thất bại tự void và chờ phụ huynh cập nhật tài khoản (BR-FEE-042, 044). |
| BR-FIN-TAB-012 | Giảm giá hết hạn được gỡ tự động ở đợt tính phí sau và ghi trong change report (BR-FEE-018; SRS Fees & Payments §4 mục 3.1 View change report). |
| BR-FIN-TAB-013 | Trẻ Singapore cần ít nhất 1 ngày đi học trong tháng để giữ trợ cấp; ngày kiểm tra mặc định là ngày 18 (BR-OPS-025). |
| BR-FIN-TAB-014 | Chênh lệch GSII không bao giờ tự áp; Centre quyết định ở màn GSII (BR-FEE-048, 049). |
| BR-FIN-TAB-015 | Centre Singapore không hiện phương thức hay tiền tệ của Malaysia, và ngược lại (BR-FEE-038; chiều Malaysia theo thông tin BBA). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Trẻ thuộc Centre Malaysia. | Không hiển thị tài khoản GIRO / CDA, trợ cấp ECDA, GSII; tiền tệ MYR. |
| VAL-004 | Vai trò không được xem tab Finance. | Không hiển thị tab Finance. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-04 - Tab Finance | Wireframe: Diagram/Wireframe/finance-draft-sprint4.html |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tóm tắt | 3 ô số | Có | — | — | FR-023. |
| Cần chú ý | Danh sách cảnh báo | Khi có việc | Ẩn khi không có | — | FR-024; mỗi dòng là liên kết. |
| Payment method | Khối gọn | Có | — | VAL-003. | FR-025. |
| Invoices | Danh sách gọn | Có | Tối đa 6 dòng | — | FR-026; FR-027; "View all invoices". |
| Deposit & refunds | Khối gọn | Có | — | — | FR-028. |
| Discounts & subsidies | Khối gọn | Có | — | VAL-003. | FR-029. |

**Đặc tả trường theo khối**

| Khối | Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|---|
| Tóm tắt | Outstanding | Số tiền | Fees & Payments › Invoices | BR-FIN-TAB-002. |
| Tóm tắt | Credit remaining | Số tiền + "of which CDA" | Fees & Payments (unused credit) | Như Parents App §4 mục 7.4. |
| Tóm tắt | Deposit held | Số tiền + "of which CDA" | Fees & Payments › Deposit ledger | — |
| Cần chú ý | Overdue invoice | Một dòng | Invoices, Outstanding & reminders | "INV-… · 34 days overdue · SGD 57.58 · reminded 15 Oct, 25 Oct" (BR-FIN-TAB-003, 008). |
| Cần chú ý | GIRO deduction failed | Một dòng | GIRO collection runs | Hoá đơn, ngày, lý do ngân hàng (BR-FIN-TAB-007). |
| Cần chú ý | GIRO account rejected | Một dòng | GIRO accounts | Loại tài khoản, lý do. |
| Cần chú ý | Refund unsuccessful | Một dòng | Refunds | Số tiền, lý do (BR-FIN-TAB-011). |
| Cần chú ý | Subsidy at risk | Một dòng | Daily Operations ("No attendance this month") | Chỉ Singapore (BR-FIN-TAB-013). |
| Cần chú ý | GSII difference | Một dòng | GSII reconciliation | Chỉ chênh lệch chưa có quyết định (BR-FIN-TAB-014). |
| Payment method | Payment method, Bill to | Text | Hồ sơ trẻ; Corporate accounts | BR-FIN-TAB-004. |
| Payment method | GIRO account | Một dòng mỗi tài khoản | GIRO accounts | Loại, ngân hàng, "••••4021", trạng thái; Rejected kèm lý do (BR-FIN-TAB-005, 006). |
| Invoices | Month, Type, Amount, Balance | Text, số tiền | Invoices | BR-FIN-TAB-009. |
| Invoices | Status | Nhãn | Invoices | Due / Overdue · n days / Paid / Draft (AS-FIN-03). |
| Invoices | GIRO state | Text nhỏ | GIRO collection runs | BR-FIN-TAB-007. |
| Invoices | CDA | Nhãn | Invoices | Chỉ hiện với hoá đơn CDA. |
| Invoices | What changed from last month | Một dòng | Billing run change report | FR-027; BR-FIN-TAB-012. |
| Deposit & refunds | Deposit | Một dòng | Deposit ledger, fee scheme | Số tiền, nguồn, số tháng (BR-FIN-TAB-010). |
| Deposit & refunds | Refund in progress | Một dòng | Refunds | Số tiền, trạng thái, nơi nhận (BR-FIN-TAB-011). |
| Discounts & subsidies | Discount | Một dòng | Discounts | Tên, giá trị, đến ngày. |
| Discounts & subsidies | Subsidy | Một dòng | Hồ sơ trẻ, subsidy lines | Basic / Additional, số tiền mỗi tháng; chỉ Singapore. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Tab đọc payment method từ hồ sơ trẻ; đọc từ Fees & Payments: số dư hoá đơn, credit chưa dùng, cọc đang giữ (tách CDA), tối đa 6 hoá đơn (tháng, loại, số tiền, số dư, trạng thái, trạng thái GIRO, CDA), dòng change report của hoá đơn tháng mới nhất, tài khoản GIRO (loại, ngân hàng, 4 số cuối, trạng thái, lý do), hoàn tiền chưa xong hoặc thất bại, giảm giá đang áp, trợ cấp, chênh lệch GSII chưa xử lý, ngày đã nhắc; từ Daily Operations: danh sách "No attendance this month". Tab không ghi dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-027 | hôm nay 2026-11-08; Ethan có 3 hoá đơn Billed chưa trả hết: 300.00, 270.00 và 57.58; 1 hoá đơn Draft 460.00 | Centre Director mở tab Finance | Outstanding hiện SGD 627.58; Draft không tính vào | FR-023; BR-FIN-TAB-002 |
| AC-028 | hoá đơn học phí tháng 10 của Ethan còn 57.58, quá hạn 34 ngày, đã nhắc 15 và 25 Oct | Centre Director mở tab Finance | Cần chú ý có dòng "34 days overdue · SGD 57.58 · reminded 15 Oct, 25 Oct" | FR-024; BR-FIN-TAB-003; BR-FIN-TAB-008 |
| AC-029 | hoá đơn enrichment tháng 10 trừ GIRO thất bại ngày 12 Oct, lý do "Insufficient funds" | School Admin mở tab Finance | Cần chú ý có dòng "GIRO deduction failed · 12 Oct · Insufficient funds"; dòng hoá đơn ghi "GIRO deduction failed" và vẫn còn số dư | FR-024; FR-026; BR-FIN-TAB-007; BR-FIN-TAB-009 |
| AC-030 | hoá đơn học phí tháng 11 phần CDA đang trong đợt 1ST DD chưa có kết quả | School Admin mở tab Finance | dòng hoá đơn có nhãn CDA và "Being collected by GIRO" | FR-026; BR-FIN-TAB-005; BR-FIN-TAB-007 |
| AC-031 | hoá đơn tháng 10 cao hơn tháng 9 vì Additional subsidy hết ngày 30 Sep | School Admin mở tab Finance | dưới hoá đơn tháng 10 có dòng "What changed from last month: Additional subsidy ended 30 Sep"; không có bảng chi tiết từng dòng hoá đơn | FR-027; BR-FIN-TAB-012 |
| AC-032 | Ethan có 9 hoá đơn, 3 hoá đơn chưa trả hết | School Admin mở tab Finance | khối Invoices hiện 6 dòng: 3 hoá đơn chưa trả hết và 3 hoá đơn mới nhất còn lại; "View all invoices" mở Fees & Payments › Invoices đã lọc theo Ethan | FR-026; FR-022 |
| AC-033 | Ethan trả bằng GIRO; tài khoản GIRO DBS ••••4021 Active, CDA OCBC ••••7730 Active | School Admin mở tab Finance | Payment method hiện "GIRO", Bill to "Parent" và 2 dòng "GIRO · DBS · ••••4021 · Active", "CDA · OCBC · ••••7730 · Active"; không có DDA reference hay nút sửa | FR-025; BR-FIN-TAB-004; BR-FIN-TAB-006; BR-FIN-TAB-001 |
| AC-034 | tài khoản CDA của Zoe bị ngân hàng từ chối, lý do "Signature mismatch" | School Admin mở tab Finance | dòng tài khoản hiện "Rejected · Signature mismatch"; Cần chú ý có dòng tương ứng | FR-024; FR-025 |
| AC-035 | Chloe không trả bằng GIRO, cọc 3 tháng (2 + 1) từ nguồn non-CDA | School Admin mở tab Finance | Deposit hiện số tiền, "non-CDA", "3 months (+1 month, not on GIRO)" | FR-028; BR-FIN-TAB-010 |
| AC-036 | cọc 500.00 của Mia trả từ CDA, có yêu cầu hoàn tiền đang Pending approval | Centre Director mở tab Finance | Deposit & refunds có dòng "Refund 500.00 · Pending approval · to CDA" | FR-028; BR-FIN-TAB-011 |
| AC-037 | hoàn tiền PayNow của Lucas thất bại, lý do "Invalid account" | HQ Finance mở tab Finance | Cần chú ý có dòng "Refund unsuccessful · Invalid account" | FR-024; BR-FIN-TAB-011 |
| AC-038 | ngày 19/10/2026 Ava (công dân Singapore) chưa có ngày đi học nào trong tháng 10 | Centre Director mở tab Finance | Cần chú ý có dòng nguy cơ mất trợ cấp tháng 10 | FR-024; BR-FIN-TAB-013 |
| AC-039 | đối soát GSII tháng 9 có chênh lệch trợ cấp của Ethan chưa được Centre quyết định | Centre Director mở tab Finance | Cần chú ý có dòng chênh lệch GSII tháng 9; liên kết mở màn GSII | FR-024; FR-022; BR-FIN-TAB-014 |
| AC-040 | Ethan có Staff child discount 50% đang áp, Basic subsidy SGD 300 mỗi tháng; không có việc cần chú ý khác | School Admin mở tab Finance | Discounts & subsidies hiện "Staff child discount · 50%" và "Basic subsidy · SGD 300.00 / month" | FR-029; DATA-004 |
| AC-041 | Iman thuộc Centre Malaysia | HQ Finance mở tab Finance | tiền tệ MYR; không có tài khoản GIRO / CDA, trợ cấp ECDA, GSII | FR-030; VAL-003; BR-FIN-TAB-015 |
| AC-042 | Teacher không được xem tab Finance | Teacher mở hồ sơ Ethan | không có tab Finance | VAL-004 |

#### Dependencies (Phụ thuộc)

Fees & Payments (Invoices, change report, GIRO accounts, GIRO collection runs, Outstanding & reminders, Deposit ledger, Refunds, Discounts, GSII reconciliation); hồ sơ trẻ (payment method); Daily Operations ("No attendance this month"); Roles & permissions.

## 6. Điểm chưa chốt

### Giả định của BA

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-FIN-01 | Tài khoản GIRO / CDA thuộc trẻ (theo thông tin BBA), mỗi trẻ tối đa 1 GIRO và 1 CDA. | FR-025; BR-FIN-TAB-005 — chờ Q-FIN-01 |
| AS-FIN-02 | Payment method trên tab chỉ hiển thị. | FR-025 — chờ Q-FIN-02 |
| AS-FIN-03 | Hoá đơn Draft hiển thị với nhãn Draft, không tính vào Outstanding. | FR-026; BR-FIN-TAB-002 — chờ Q-FIN-03 |
| AS-FIN-04 | Teacher không thấy tab Finance. | Mục 4; VAL-004 — chờ Q-FIN-04 |
| AS-FIN-05 | Trẻ chuyển Centre: hoá đơn của Centre cũ vẫn tính vào Outstanding và vẫn có trong "View all invoices". | FR-023; FR-026 — chờ Q-FIN-05 |
| AS-FIN-06 | Tab có liên kết "Open in Billing" theo quyền; không có tải PDF, in, Request correction trên tab. | FR-022 — chờ Q-FIN-06 |
| AS-FIN-07 | Khối Invoices hiện tối đa 6 dòng (mọi hoá đơn chưa trả hết, rồi hoá đơn mới nhất). | FR-026 — chờ Q-FIN-07 |

### Câu hỏi cần làm rõ với BBA

| Question ID | Priority | Topic | Câu hỏi | Vì sao cần làm rõ |
|---|---|---|---|---|
| Q-FIN-01 | P0 | Tài khoản GIRO | Tài khoản GIRO / CDA thuộc cấp Child hay Family? BBA nói thuộc Child, nhưng SRS BR-FEE-030 ghi "a family can have one GIRO (bank) account and one CDA account". | Quyết định cách lưu dữ liệu và anh chị em có dùng chung tài khoản không. |
| Q-FIN-02 | P0 | Payment method | Payment method trên tab chỉ hiển thị hay được sửa? Nếu sửa, ai được sửa và có cần duyệt không? (Q-66-10 chưa có trả lời) | Ảnh hưởng tới quy tắc tab chỉ đọc và hoá đơn tháng sau. |
| Q-FIN-03 | P1 | Hoá đơn Draft | Có hiển thị hoá đơn Draft (tạo ngày 24) trên tab không? Nếu có, cho vai trò nào? | Draft chưa gửi phụ huynh; Centre có thể báo số chưa chốt. |
| Q-FIN-04 | P1 | Quyền xem | Teacher có xem tab Finance không, hay chỉ Centre Director, Centre / School Admin, HQ, Finance? | Dữ liệu tài chính gia đình là dữ liệu nhạy cảm. |
| Q-FIN-05 | P1 | Chuyển Centre / brand | Trẻ chuyển Centre hoặc brand (pháp nhân khác): có hiện hoá đơn và cọc của Centre cũ không? Nhân viên Centre mới có được xem không? | Phạm vi xem và dữ liệu của pháp nhân khác. |
| Q-FIN-06 | P1 | Liên kết và tải tài liệu | Có cho tải / in PDF hoá đơn, biên lai và liên kết sang màn Billing (ví dụ Request correction trên Draft) cho người có quyền không? | Tab chỉ là nơi xem hay còn là lối tắt sang thao tác. |
| Q-FIN-07 | P1 | Số hoá đơn hiển thị | Khối Invoices hiện bao nhiêu hoá đơn: 6 dòng như đề xuất, hay theo số tháng (ví dụ 3 tháng gần nhất)? | Giữ tab ở mức tổng quan mà vẫn đủ để trả lời phụ huynh. |

## 7. Tài liệu tham khảo

Số trang tính theo bản Word gốc của SRS khi xuất PDF khổ A4.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | Plane — ticket BBA-67 (WBS 3.1.1.02) | Description: finance (invoices, balances, GIRO), each linking to the module screen | — | Phạm vi US-004. |
| 2 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §2 Who uses it | 3 | Mục 4. |
| 3 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §3 P2 Monthly billing cycle, P3 GIRO collection | 4 | FR-024, FR-026. |
| 4 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 3.1 Billing runs (change report), 3.2 Invoices | 7 | FR-026, FR-027. |
| 5 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 4.1 GIRO accounts, 4.2 GIRO collection runs | 8–9 | FR-025, FR-026. |
| 6 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 4.7 Outstanding & reminders | 9–10 | FR-024. |
| 7 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 5.1 Deposit ledger, 5.2 Refunds | 10–11 | FR-028. |
| 8 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 6.1 GSII reconciliation | 11 | FR-024. |
| 9 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-003 đến 011 | 12 | BR-FIN-TAB-001 đến 003, 008, 009. |
| 10 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-018 đến 038 | 13 | BR-FIN-TAB-004 đến 007, 010, 012, 015. |
| 11 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-041 đến 049 | 14 | BR-FIN-TAB-001, 011, 014. |
| 12 | BBA-SMS-SRS-Parents-App-v0.1 | §4 mục 7.1 Invoices, 7.4 Credits | 13–14 | FR-023. |
| 13 | BBA-SMS-SRS-Daily-Operations-v0.1 | §5 BR-OPS-025 | 10 | BR-FIN-TAB-013. |
