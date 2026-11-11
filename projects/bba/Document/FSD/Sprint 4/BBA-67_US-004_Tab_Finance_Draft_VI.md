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
| Phiên bản | 0.1 (nháp) |
| Trạng thái | BẢN NHÁP ĐỂ RÀ SOÁT |
| Ngày | 11/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 (nháp) | 11/11/2026 | Business Analysis | Bản nháp riêng cho US-004 theo SRS Fees & Payments v0.1, SRS Children & Families v0.1, SRS Parents App v0.1 và thông tin payment method BBA đã chốt. Quy tắc đánh mã BR-FIN-TAB-xxx; khi gộp vào FRD chính sẽ đổi sang mã BR-0xx và đánh số lại. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả 9 khối thông tin, quyền xem theo vai trò, 22 quy tắc, 20 tiêu chí nghiệm thu. 6 điểm chưa chốt ghi thành giả định và câu hỏi ở mục 6.

## 2. Mục đích và phạm vi

| Điểm chính | Căn cứ |
|---|---|
| Tab Finance là bảng tổng hợp tài chính của **một trẻ**, khác các màn Billing (xem theo Centre, tháng, đợt). | SRS Fees & Payments §4 mục 3.1, 3.2 (tr.7) |
| Mục đích: Centre trả lời phụ huynh "con còn nợ bao nhiêu", "sao tháng này hoá đơn cao", "tiền cọc còn bao nhiêu", "sao chưa trừ GIRO" mà không cần vào Billing. | Định hướng của BA phụ trách |
| Tab **chỉ đọc**. Tạo, sửa hoá đơn, credit note, hoàn tiền, tài khoản GIRO đều làm hoặc duyệt trong Billing bởi Finance. | BR-FEE-007, 008 (tr.12); BR-FEE-027, 041 (tr.13–14) |
| Phụ huynh thấy cùng các con số trong Parents App: số còn nợ, hoá đơn, trạng thái GIRO, credit còn lại (tách phần CDA), hoàn tiền. Tab dùng cùng cách tính để Centre trả lời khớp với những gì phụ huynh thấy. | SRS Parents App §4 mục 7.1, 7.4, 7.5 (tr.13–14) |

**Ngoài phạm vi:** mọi thao tác tạo, sửa, duyệt, void; tải hoặc in PDF và Request correction trên Draft (chờ Q-FIN-06); báo cáo của Fees & Payments.

## 3. Những gì thay đổi so với US-004 hiện tại (FRD v0.6)

| Nội dung | US-004 hiện tại | Bản nháp này |
|---|---|---|
| Tóm tắt | "How this family pays": payment method, citizenship, Bill to, cọc, tổng nợ. | Tóm tắt 3 số: còn nợ, credit còn lại (tách CDA), cọc đang giữ. Payment method tách thành khối riêng. |
| Khối "What needs doing" | Có. | Bỏ; việc cần làm thể hiện ngay trên dòng hoá đơn (Overdue, GIRO deduction failed) và dòng hoàn tiền (Unsuccessful). |
| Hoá đơn | Nhóm theo loại; chưa có GIRO theo hoá đơn, nhắc nợ, chi tiết. | Thêm Bill to, trạng thái GIRO theo hoá đơn, số ngày quá hạn, lịch sử nhắc nợ; chi tiết hoá đơn mở rộng ngay trong dòng, có lý do thay đổi so với tháng trước. |
| Biên lai, credit note, hoàn tiền | Chưa có. | Có 3 khối riêng. |
| Tiền cọc | Ngày, số, số tiền, còn lại. | Thêm nguồn CDA / non-CDA, số tháng cọc, các lần biến động, quy tắc K2. |
| Trợ cấp | Basic / Additional, hết hạn trong 30 ngày (AS-RT-03). | Basic / Additional; cảnh báo điều kiện 1 ngày đi học / tháng; chênh lệch GSII. Bỏ giả định 30 ngày (không có trong SRS). |
| Giảm giá | Có dòng "không áp" kèm lý do (AS-RT-04). | Chỉ giảm giá đang áp: tên, giá trị, hiệu lực. Bỏ giả định "mỗi hoá đơn một giảm giá" (không có trong SRS). |
| Payment schedule | Có. | Bỏ (không thuộc danh sách khối đã chốt). |
| Cọc là trường che theo vai trò | Có (FR-030 hiện tại). | Bỏ; chỉ số tài khoản ngân hàng luôn che. |

## 4. Quyền xem theo vai trò

| Vai trò | Thấy tab Finance | Phạm vi | Ghi chú | Căn cứ |
|---|---|---|---|---|
| HQ Admin | Có | Mọi Centre | Mọi khối. | SRS Fees & Payments §2 (tr.3) |
| HQ Finance | Có | Mọi Centre | Mọi khối. | §2 (tr.3) |
| Centre Director | Có | Centre của mình | Mọi khối; hoá đơn của Centre. | §2 (tr.3) |
| Centre Admin / School Admin | Có | Centre của mình | Mọi khối; hoá đơn của Centre. | §2 (tr.3) |
| HQ Enrolment | Theo quyền | Mọi Centre | Theo cấu hình Roles & permissions. | FRD v0.6 mục 4 |
| Teacher | Không (giả định) | — | Chờ Q-FIN-04. | AS-FIN-04 |
| Enrichment Trainer | Không | — | Chỉ thấy tab Enrichment. | FRD v0.6 mục 4 |
| Parent | Không dùng tab này | — | Xem tài chính trong Parents App. | SRS Parents App §4 mục 7 |

## 5. Yêu cầu chức năng

### 5.1 US-004 - Tab Finance: tổng hợp tài chính của trẻ

#### User Story

Là Centre Director hoặc School Admin, tôi muốn xem trên hồ sơ trẻ trẻ còn nợ bao nhiêu, vì sao hoá đơn tháng này khác tháng trước, tiền cọc còn bao nhiêu và vì sao GIRO chưa trừ, để trả lời phụ huynh mà không phải vào module Billing.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-022 | Tab Finance chỉ hiển thị; không có thao tác tạo, sửa, duyệt hay void. Mỗi khối có liên kết "Open in Billing" mở màn tương ứng của Fees & Payments (Invoices, Receipts, Credit notes, GIRO accounts, Deposit ledger, Refunds) đã lọc theo trẻ (AS-FIN-06). |
| FR-023 | Khối **Tóm tắt** gồm 3 số: Outstanding (tổng số dư các hoá đơn Billed chưa trả hết), Credit remaining (tổng credit chưa dùng, ghi riêng phần CDA), Deposit held (tổng tiền cọc đang giữ, ghi riêng phần CDA). |
| FR-024 | Khối **Payment method**: phương thức của trẻ (GIRO, GIRO CDA hoặc PayNow); Bill to (Parent / Company); bảng tài khoản GIRO (tối đa 2 dòng: GIRO và CDA) với loại, ngân hàng, số tài khoản che chỉ còn 4 số cuối, DDA reference, trạng thái (Pending with bank / Active / Rejected kèm lý do), cách đăng ký (Paper form / e-GIRO), Pays by GIRO. |
| FR-025 | Khối **Invoices**: mỗi hoá đơn một dòng, mới nhất trước, phân trang 20 / 50 / 100: số, tháng, loại (School fees / Enrichment / Registration / Ad hoc), số tiền, số dư, due date, trạng thái (Draft, Billed, Partially paid, Paid, Overdue kèm số ngày quá hạn, Void), Bill to, payment method, tài khoản CDA / non-CDA, trạng thái GIRO theo hoá đơn ("GIRO deduction scheduled · ngày", "Being collected by GIRO", "GIRO deduction failed · ngày · lý do ngân hàng"), nhắc nợ đã gửi (ngày 15, 25). |
| FR-026 | Chọn một hoá đơn thì dòng đó mở rộng ngay trong tab (không chuyển màn hình) để hiện chi tiết chỉ đọc: các dòng học phí, enrichment, giảm giá, trợ cấp Basic / Additional, credit đã trừ, pro-rate (tháng cuối của trẻ thôi học); các lần thanh toán và biên lai; với hoá đơn tháng, lý do thay đổi so với tháng trước lấy từ change report (đổi chương trình, đổi trợ cấp, giảm giá hết hạn bị gỡ). |
| FR-027 | Khối **Receipts**: số, số tiền, phương thức (GIRO, GIRO CDA, PayNow, bank transfer, AXS, cheque), ngày, các hoá đơn đã thanh toán, người phát hành. |
| FR-028 | Khối **Credit notes**: số, hoá đơn gốc, phạm vi (Half month / Full month), số tiền, trạng thái duyệt, đã trừ vào hoá đơn nào (hoá đơn gốc và phần dư). |
| FR-029 | Khối **Deposit**: số tiền đang giữ, nguồn (CDA / non-CDA), số tháng cọc (kèm ghi chú "+1 month, not on GIRO" khi trẻ không trả bằng GIRO), booking fee đã trừ trên hoá đơn đầu; danh sách biến động (nhận cọc, bù trừ hoá đơn, chuyển Centre, hoàn tiền) với ngày, số tiền, hoá đơn hoặc hoàn tiền liên quan. Trẻ K2 có ghi chú "K2: up to 2 months of fees can be offset". |
| FR-030 | Khối **Refunds**: số, số tiền, trạng thái (Pending approval, Approved, Rejected, Processing, Successful, Unsuccessful, Void), nguồn (CDA / non-CDA), nơi nhận (CDA hoặc PayNow), phụ huynh đã xác nhận tài khoản chưa (Yes / No; tài khoản che), lý do thất bại nếu Unsuccessful. |
| FR-031 | Khối **Discounts & subsidies**: giảm giá đang áp (tên, giá trị số tiền hoặc %, từ ngày → đến ngày); trợ cấp Basic / Additional (số tiền mỗi tháng, hiệu lực); với trẻ Singapore: cảnh báo khi đã qua ngày kiểm tra (mặc định ngày 18) mà trẻ chưa có ngày đi học nào trong tháng; chênh lệch đối soát GSII của trẻ (tháng, loại chênh lệch, quyết định) nếu có. |
| FR-032 | Hoá đơn, biên lai, credit note thuộc tháng đã đóng sổ có nhãn "Closed month"; không có thao tác nào trên tab. |
| FR-033 | Trẻ ở Centre Singapore chỉ thấy SGD và phương thức của Singapore; trẻ ở Centre Malaysia chỉ thấy MYR và phương thức của Malaysia, không có tài khoản GIRO / CDA, trợ cấp ECDA, GSII. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Finance; hệ thống hiển thị Tóm tắt, Payment method, Invoices, Receipts, Credit notes, Deposit, Refunds, Discounts & subsidies (FR-023 đến FR-031).
2. Người dùng chọn một hoá đơn; dòng mở rộng hiện chi tiết và lý do thay đổi so với tháng trước (FR-026).
3. Cần thao tác: người dùng chọn "Open in Billing" ở khối tương ứng (FR-022).

#### Functional Flow - Alternative (Luồng thay thế)

1. Hoá đơn trong đợt 1ST DD chưa có kết quả: dòng hiện "Being collected by GIRO" (FR-025; BR-FIN-TAB-007).
2. GIRO trừ thất bại: dòng hiện "GIRO deduction failed" kèm lý do ngân hàng; hoá đơn vẫn chưa trả (FR-025; BR-FIN-TAB-007).
3. Credit note lớn hơn số dư hoá đơn gốc: khối Credit notes ghi phần dư đã trừ vào hoá đơn còn mở cũ nhất (FR-028; BR-FIN-TAB-011).
4. Trẻ đã chuyển Centre: hoá đơn và cọc của Centre cũ vẫn hiển thị, ghi Centre và pháp nhân; biến động cọc có dòng chuyển Centre (FR-025; FR-029; AS-FIN-05).
5. Trẻ ở Centre Malaysia: không có tài khoản GIRO / CDA, trợ cấp ECDA, GSII (FR-033; VAL-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò không được xem tab Finance: không có tab (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-FIN-TAB-001 | Tab chỉ đọc. Tạo, sửa hoá đơn, credit note, hoàn tiền, tài khoản GIRO làm hoặc duyệt trong Billing bởi Finance (BR-FEE-007, 008, 027, 041). |
| BR-FIN-TAB-002 | Outstanding = tổng số dư các hoá đơn Billed chưa trả hết (Billed, Partially paid, Overdue); không tính Draft và Void (BR-FEE-006; SRS Parents App §4 mục 7.1). |
| BR-FIN-TAB-003 | Partially paid và Overdue được tính từ thanh toán và ngày đến hạn (mặc định ngày 5 của tháng hoá đơn), không đặt tay (BR-FEE-003, 006). |
| BR-FIN-TAB-004 | Payment method thuộc hồ sơ trẻ: GIRO, GIRO CDA hoặc PayNow; ngoài ra trả tay bằng bank transfer, AXS, cheque. Mỗi hoá đơn mang theo phương thức để Finance lọc (thông tin BBA đã chốt; BR-FEE-037). |
| BR-FIN-TAB-005 | Một trẻ có tối đa 2 tài khoản GIRO: CDA và non-CDA. CDA chỉ dùng cho khoản được trừ CDA; CDA và non-CDA xuất hoá đơn riêng (thông tin BBA đã chốt; BR-FEE-030 — chờ Q-FIN-01). |
| BR-FIN-TAB-006 | Số tài khoản ngân hàng và tài khoản nhận hoàn tiền luôn che, chỉ hiện 4 số cuối (SRS Fees & Payments §4 mục 4.1 Mask account number; SRS Parents App §4 mục 7.5). |
| BR-FIN-TAB-007 | Hoá đơn trong đợt 1ST DD chưa có kết quả hiện "Being collected by GIRO"; dòng GIRO thất bại giữ hoá đơn chưa trả và ghi lý do của ngân hàng (BR-FEE-033, 034). |
| BR-FIN-TAB-008 | Phụ huynh có hoá đơn Billed chưa trả được nhắc trong app ngày 15 và 25, tối đa 2 lần nhắc tự động mỗi kỳ (BR-FEE-004). |
| BR-FIN-TAB-009 | Học phí và enrichment là hai hoá đơn riêng (BR-FEE-011). |
| BR-FIN-TAB-010 | Mỗi hoá đơn có tối đa 1 credit note, phạm vi nửa tháng hoặc cả tháng; mọi credit note được duyệt trong Finance approvals trước khi phát hành (BR-FEE-025, 026, 027). |
| BR-FIN-TAB-011 | Credit note đã duyệt trừ vào hoá đơn gốc trước; phần dư trừ vào hoá đơn còn mở cũ nhất của trẻ; không trừ thêm vào hoá đơn tháng sau (BR-FEE-028). |
| BR-FIN-TAB-012 | Nguồn của mọi khoản cọc (CDA / non-CDA) được ghi lại. Trẻ không trả bằng GIRO cọc thêm 1 tháng; số tháng cọc cài theo brand và Centre. Hoá đơn đầu gồm phí đăng ký và cọc, trừ booking fee đã trả (BR-FEE-020, 021, 022). |
| BR-FIN-TAB-013 | Cọc được bù trừ vào hoá đơn chưa trả trước, trừ khi Finance chọn hoàn đủ. Cọc của trẻ K2 bù trừ được tối đa 2 tháng học phí và enrichment (BR-FEE-023, 024). |
| BR-FIN-TAB-014 | Tiền trả từ CDA chỉ hoàn về CDA. Chỉ phụ huynh đặt hoặc đổi tài khoản nhận hoàn. Hoàn tiền thất bại tự void; yêu cầu mới được tạo khi phụ huynh cập nhật tài khoản (BR-FEE-042, 043, 044). |
| BR-FIN-TAB-015 | Trạng thái hoàn tiền: Pending approval, Approved, Rejected, Processing, Successful, Unsuccessful, Void (BR-FEE-040). |
| BR-FIN-TAB-016 | Giảm giá hết hạn được gỡ tự động ở đợt tính phí sau và ghi trong change report (BR-FEE-018; SRS Fees & Payments §4 mục 3.1 View change report). |
| BR-FIN-TAB-017 | Trẻ Singapore cần ít nhất 1 ngày đi học trong tháng để giữ trợ cấp; ngày kiểm tra (mặc định ngày 18) hệ thống liệt kê trẻ chưa có ngày đi học nào (BR-OPS-025; SRS Daily Operations §4 mục 2.2). |
| BR-FIN-TAB-018 | Chênh lệch GSII không bao giờ tự áp; chênh lệch với hoá đơn được sửa bằng credit note hoặc ad hoc invoice qua Finance approvals (BR-FEE-048, 049). |
| BR-FIN-TAB-019 | Tháng đã đóng sổ chỉ xem; mọi điều chỉnh làm bằng credit note ở tháng còn mở (BR-FEE-052). |
| BR-FIN-TAB-020 | Centre Singapore không hiện phương thức hay tiền tệ của Malaysia, và ngược lại (BR-FEE-038; chiều Malaysia theo thông tin BBA). |
| BR-FIN-TAB-021 | Hoá đơn giữ tên, địa chỉ, số đăng ký của pháp nhân tại thời điểm phát hành (BR-FEE-009). |
| BR-FIN-TAB-022 | Bill to là Parent hoặc Company; hoá đơn của công ty được gửi email, các hoá đơn khác chỉ hiện trong Parents App (BR-FEE-010; SRS Fees & Payments §4 mục 2.4). |

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
| Tóm tắt | Ô số liệu | Có | — | — | FR-023. |
| Payment method | Khối | Có | — | VAL-003. | FR-024. |
| Invoices | Danh sách | Có | Mới nhất trước; 20 dòng mỗi trang | — | FR-025; chọn dòng để mở rộng (FR-026). |
| Receipts, Credit notes, Deposit, Refunds | Danh sách | Có | Mới nhất trước | — | FR-027 đến FR-030. |
| Discounts & subsidies | Khối | Có | — | VAL-003. | FR-031. |
| Open in Billing | Liên kết | Theo quyền | — | — | FR-022. |

**Đặc tả trường theo khối**

a) Tóm tắt

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Outstanding | Số tiền, nổi bật | Fees & Payments › Invoices | Tổng số dư hoá đơn Billed / Partially paid / Overdue; không tính Draft, Void (BR-FIN-TAB-002). |
| Credit remaining | Số tiền + dòng "of which CDA" | Fees & Payments › Credit notes, Transactions (unused credit) | Như Parents App "View credit remaining" (SRS PA §4 mục 7.4). |
| Deposit held | Số tiền + dòng "of which CDA" | Fees & Payments › Deposit ledger | Tổng cọc đang giữ của trẻ (SRS F&P §4 mục 5.1). |

b) Payment method và tài khoản GIRO

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Payment method | Text | Hồ sơ trẻ | GIRO, GIRO CDA hoặc PayNow (BR-FIN-TAB-004); chỉ đọc (AS-FIN-02). |
| Bill to | Text | Fees & Payments › Corporate accounts | Parent hoặc tên công ty (BR-FIN-TAB-022). |
| Account type | Text | Fees & Payments › GIRO accounts | GIRO hoặc CDA; tối đa 2 dòng (BR-FIN-TAB-005). |
| Bank | Text | GIRO accounts | Ví dụ DBS, OCBC, UOB. |
| Account number | Text che | GIRO accounts | Chỉ 4 số cuối, ví dụ "••••4021" (BR-FIN-TAB-006). |
| DDA reference | Text | GIRO accounts | — |
| Status | Nhãn | GIRO accounts | Pending with bank / Active / Rejected; Rejected kèm lý do. |
| Application method | Text | GIRO accounts | Paper form / e-GIRO. |
| Pays by GIRO | Yes / No | GIRO accounts | — |

c) Invoices

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Invoice no. | Text | Fees & Payments › Invoices | Mới nhất trước. |
| Month | Tháng / năm | Invoices | — |
| Type | Nhãn | Invoices | School fees / Enrichment / Registration / Ad hoc (BR-FIN-TAB-009). |
| Amount, Balance | Số tiền | Invoices | Tiền tệ theo quốc gia Centre (BR-FIN-TAB-020). |
| Due date | Ngày | Invoices | Mặc định ngày 5 của tháng hoá đơn (BR-FEE-003). |
| Status | Nhãn | Invoices | Draft, Billed, Partially paid, Paid, Overdue (kèm "n days"), Void (BR-FIN-TAB-003); Draft theo AS-FIN-03. |
| Bill to | Text | Invoices | Parent / Company. |
| Payment method | Text | Invoices | Phương thức hoá đơn mang theo (BR-FIN-TAB-004). |
| Account | Nhãn | Invoices | CDA / non-CDA. |
| GIRO state | Text | GIRO collection runs | "GIRO deduction scheduled · 5 Nov", "Being collected by GIRO", "GIRO deduction failed · 12 Oct · Insufficient funds" (BR-FIN-TAB-007). |
| Reminders | Danh sách ngày | Outstanding & reminders | Ví dụ "Reminded 15 Oct, 25 Oct" (BR-FIN-TAB-008). |
| Centre · legal entity | Text | Invoices | Hiện khi trẻ có hoá đơn ở hơn một Centre (AS-FIN-05; BR-FIN-TAB-021). |
| Closed month | Nhãn | Month-end close | FR-032; BR-FIN-TAB-019. |

d) Chi tiết hoá đơn (dòng mở rộng, chỉ đọc)

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Lines | Bảng dòng | Invoice detail | Học phí, enrichment, giảm giá, trợ cấp Basic / Additional, credit đã trừ, pro-rate; mỗi dòng có số tiền. |
| Payments | Danh sách | Invoice detail, Receipts | Ngày, phương thức, số tiền, số biên lai. |
| What changed from last month | Danh sách | Billing run change report | Chỉ với hoá đơn tháng; ví dụ "Additional subsidy ended 30 Sep", "Programme changed to Full day", "Expired discount removed" (BR-FIN-TAB-016). |

e) Receipts

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Receipt no., Amount, Date | Text, số tiền, ngày | Fees & Payments › Receipts | Mới nhất trước. |
| Method | Text | Receipts | GIRO, GIRO CDA, PayNow, bank transfer, AXS, cheque. |
| Invoices paid | Danh sách số hoá đơn | Receipts | — |
| Issued by | Text | Receipts | Biên lai trả tay chỉ do Finance hoặc HQ Admin phát hành (BR-FEE-037). |

f) Credit notes

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Credit note no. | Text | Fees & Payments › Credit notes | — |
| Invoice | Số hoá đơn | Credit notes | Tối đa 1 credit note mỗi hoá đơn (BR-FIN-TAB-010). |
| Scope | Nhãn | Credit notes | Half month / Full month. |
| Amount | Số tiền | Credit notes | — |
| Approval status | Nhãn | Finance approvals | Pending approval / Approved / Rejected. |
| Applied to | Danh sách hoá đơn và số tiền | Credit notes | Hoá đơn gốc trước, phần dư vào hoá đơn còn mở cũ nhất (BR-FIN-TAB-011). |

g) Deposit

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Amount held | Số tiền | Fees & Payments › Deposit ledger | — |
| Source | Nhãn | Deposit ledger | CDA / non-CDA (BR-FIN-TAB-012). |
| Deposit months | Số | Fee scheme, hồ sơ trẻ | Ghi "+1 month, not on GIRO" khi không trả bằng GIRO. |
| Booking fee deducted | Số tiền + số hoá đơn đầu | Invoices (first invoice) | BR-FIN-TAB-012. |
| Movements | Danh sách | Deposit ledger | Nhận cọc, bù trừ hoá đơn, chuyển Centre, hoàn tiền: ngày, số tiền, chứng từ liên quan. |
| K2 offset note | Ghi chú | Hồ sơ trẻ (level K2) | Tối đa 2 tháng học phí và enrichment (BR-FIN-TAB-013). |

h) Refunds

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Refund no., Amount | Text, số tiền | Fees & Payments › Refunds | — |
| Status | Nhãn | Refunds | BR-FIN-TAB-015. |
| Source, Destination | Nhãn | Refunds | Tiền CDA chỉ về CDA (BR-FIN-TAB-014). |
| Account confirmed by parent | Yes / No + tài khoản che | Refunds | Không hỏi tài khoản cho phần CDA (SRS PA §3 P6). |
| Failure reason | Text | Refunds | Khi Unsuccessful; hoàn tiền tự void, chờ phụ huynh cập nhật. |

i) Discounts & subsidies

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Discount name, value, period | Text | Fees & Payments › Discounts | Chỉ giảm giá đang áp; giá trị là số tiền hoặc %; từ ngày → đến ngày. |
| Subsidy (Basic / Additional) | Text + số tiền mỗi tháng | Hồ sơ trẻ, invoice subsidy lines | Chỉ Singapore (VAL-003). |
| Subsidy attendance warning | Cảnh báo | Daily Operations ("No attendance this month") | BR-FIN-TAB-017. |
| GSII differences | Danh sách | Fees & Payments › GSII reconciliation | Tháng, loại chênh lệch, quyết định (BR-FIN-TAB-018). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Tab đọc payment method từ hồ sơ trẻ; đọc từ Fees & Payments: invoices (number, month, type, amount, balance, due date, status, bill to, payment method, account CDA / non-CDA, legal entity, centre, closed month), invoice lines, change report rows, GIRO accounts, GIRO batch results, reminders log, receipts, credit notes và phần đã áp, deposit ledger, refunds, discounts, subsidy lines, GSII differences; từ Daily Operations: danh sách "No attendance this month". Tab không ghi dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-027 | hôm nay 2026-11-08; Ethan có 3 hoá đơn Billed chưa trả hết: 300.00, 270.00 (Overdue 34 ngày) và 57.58 (Overdue 34 ngày); 1 hoá đơn Draft 460.00 | Centre Director mở tab Finance | Outstanding hiện SGD 627.58; hai hoá đơn tháng 10 hiện "Overdue · 34 days"; Draft không tính vào Outstanding | FR-023; FR-025; BR-FIN-TAB-002; BR-FIN-TAB-003 |
| AC-028 | hoá đơn enrichment tháng 10 của Ethan trừ GIRO thất bại ngày 12 Oct, lý do "Insufficient funds" | School Admin mở tab Finance | dòng hoá đơn hiện "GIRO deduction failed · 12 Oct · Insufficient funds", trạng thái vẫn chưa trả, có "Reminded 15 Oct, 25 Oct" | FR-025; BR-FIN-TAB-007; BR-FIN-TAB-008 |
| AC-029 | hoá đơn học phí tháng 11 của Ethan đang trong đợt 1ST DD chưa có kết quả | School Admin mở tab Finance | dòng hoá đơn hiện "Being collected by GIRO" | FR-025; BR-FIN-TAB-007 |
| AC-030 | hoá đơn tháng 10 của Ethan cao hơn tháng 9 vì Additional subsidy hết ngày 30 Sep | School Admin chọn hoá đơn tháng 10 | dòng mở rộng ngay trong tab, hiện các dòng học phí, giảm giá, trợ cấp và mục "What changed from last month: Additional subsidy ended 30 Sep" | FR-026; BR-FIN-TAB-016 |
| AC-031 | credit note CN-SW-TAM-202611-0003 (Half month) được duyệt 308.40 cho hoá đơn INV-SW-TAM-202611-0002 còn dư 228.40; hoá đơn còn mở cũ nhất của trẻ là INV-SW-TAM-202610-0041 | HQ Finance mở tab Finance | khối Credit notes hiện "Applied to: 228.40 on INV-SW-TAM-202611-0002; 80.00 on INV-SW-TAM-202610-0041"; hoá đơn tháng 12 không bị trừ | FR-028; BR-FIN-TAB-010; BR-FIN-TAB-011 |
| AC-032 | cọc 500.00 của Mia trả từ CDA; Mia thôi học, có yêu cầu hoàn tiền | Centre Director mở khối Refunds | nơi nhận hiện "CDA", phần tài khoản xác nhận của phụ huynh không áp cho phần CDA | FR-030; BR-FIN-TAB-014 |
| AC-033 | hoàn tiền PayNow của Lucas thất bại, lý do "Invalid account" | HQ Finance mở khối Refunds | dòng hiện Unsuccessful rồi Void, lý do "Invalid account", phụ huynh chưa cập nhật tài khoản | FR-030; BR-FIN-TAB-014; BR-FIN-TAB-015 |
| AC-034 | Lucas chuyển từ Small Wonder Tampines sang Bukit Timah ngày 2026-06-01; cọc được chuyển theo | HQ Finance mở tab Finance | hoá đơn của cả hai Centre đều hiện, mỗi dòng ghi Centre và pháp nhân; khối Deposit có biến động "Transferred to Small Wonder Bukit Timah · 2026-06-01" | FR-025; FR-029; BR-FIN-TAB-021 |
| AC-035 | Chloe không trả bằng GIRO, cọc 2 tháng + 1 tháng, booking fee 200.00 đã trừ trên hoá đơn đầu | School Admin mở khối Deposit | hiện số tháng cọc kèm "+1 month, not on GIRO" và "Booking fee 200.00 deducted on" số hoá đơn đầu | FR-029; BR-FIN-TAB-012 |
| AC-036 | Ethan có tài khoản GIRO DBS 072-311-4021 Active, đăng ký Paper form | School Admin mở khối Payment method | hiện "DBS · ••••4021", DDA reference, Active, Paper form; không có thao tác sửa | FR-024; BR-FIN-TAB-006; BR-FIN-TAB-001 |
| AC-037 | Ava là công dân Singapore, ngày 19/10/2026 chưa có ngày đi học nào trong tháng 10 | Centre Director mở khối Discounts & subsidies | có cảnh báo cần ít nhất 1 ngày đi học trong tháng để giữ trợ cấp | FR-031; BR-FIN-TAB-017 |
| AC-038 | hoá đơn tháng 9 của Ethan thuộc tháng đã đóng sổ | School Admin mở tab Finance | dòng hoá đơn có nhãn "Closed month"; không có thao tác nào | FR-032; BR-FIN-TAB-019 |
| AC-039 | Iman thuộc Centre Malaysia | HQ Finance mở tab Finance | tiền tệ MYR; không có tài khoản GIRO / CDA, trợ cấp ECDA, GSII | FR-033; VAL-003; BR-FIN-TAB-020 |
| AC-040 | Teacher không được xem tab Finance | Teacher mở hồ sơ Ethan | không có tab Finance | VAL-004 |
| AC-041 | Ethan có khoản Staff child discount 50% đang áp từ 2026-01-01, không có ngày kết thúc | School Admin mở khối Discounts & subsidies | hiện "Staff child discount · 50% · 2026-01-01 → —"; liên kết "Open in Billing" mở Fees & Payments › Discounts đã lọc theo Ethan | FR-031; FR-022 |
| AC-042 | Ethan trả bằng GIRO, có tài khoản GIRO (DBS) và CDA (OCBC); học phí tháng 11 có phần trừ CDA; Ethan học enrichment | School Admin mở khối Invoices | học phí tháng 11 là 2 hoá đơn riêng, một ghi CDA, một ghi non-CDA, mỗi hoá đơn ghi payment method; enrichment là hoá đơn riêng loại Enrichment | FR-024; FR-025; BR-FIN-TAB-004; BR-FIN-TAB-005; BR-FIN-TAB-009 |
| AC-043 | phụ huynh Ethan trả 322.42 bằng PayNow cho hoá đơn INV-SW-TAM-202610-0041 ngày 2026-10-04 | School Admin mở khối Receipts | có dòng biên lai 322.42, PayNow, 2026-10-04, hoá đơn đã thanh toán INV-SW-TAM-202610-0041 | FR-027; DATA-004 |
| AC-044 | Noah học K2, có cọc 1,180.00 | School Admin mở khối Deposit | có ghi chú "K2: up to 2 months of fees can be offset" | FR-029; BR-FIN-TAB-013 |
| AC-045 | đối soát GSII tháng 9 có chênh lệch trợ cấp của Ethan, Centre chọn "Keep profile" với lý do | Centre Director mở khối Discounts & subsidies | hiện chênh lệch tháng 9, loại chênh lệch, quyết định "Keep profile" và lý do; không có số nào tự thay đổi | FR-031; BR-FIN-TAB-018 |
| AC-046 | học phí của Zoe do công ty ABC Pte Ltd trả | School Admin mở tab Finance | Bill to hiện "ABC Pte Ltd" ở khối Payment method và trên từng hoá đơn | FR-024; FR-025; BR-FIN-TAB-022 |

#### Dependencies (Phụ thuộc)

Fees & Payments (Invoices, change report, GIRO accounts, GIRO collection runs, Receipts, Credit notes, Deposit ledger, Refunds, Discounts, GSII reconciliation, Month-end close); hồ sơ trẻ (payment method, citizenship, level); Daily Operations ("No attendance this month"); Roles & permissions.

## 6. Điểm chưa chốt

### Giả định của BA

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-FIN-01 | Tài khoản GIRO / CDA thuộc trẻ (theo thông tin BBA), mỗi trẻ tối đa 1 GIRO và 1 CDA. | FR-024; BR-FIN-TAB-005 — chờ Q-FIN-01 |
| AS-FIN-02 | Payment method trên tab chỉ hiển thị; sửa ở nơi khác. | FR-024 — chờ Q-FIN-02 |
| AS-FIN-03 | Hoá đơn Draft hiển thị với nhãn Draft cho vai trò Centre và Finance, không tính vào Outstanding. | FR-025; BR-FIN-TAB-002 — chờ Q-FIN-03 |
| AS-FIN-04 | Teacher không thấy tab Finance. | Mục 4; VAL-004 — chờ Q-FIN-04 |
| AS-FIN-05 | Trẻ chuyển Centre: hoá đơn và cọc của Centre cũ vẫn hiển thị, ghi Centre và pháp nhân. | FR-025; FR-029 — chờ Q-FIN-05 |
| AS-FIN-06 | Tab có liên kết "Open in Billing" theo quyền; không có tải PDF, in, Request correction trên tab. | FR-022 — chờ Q-FIN-06 |

### Câu hỏi cần làm rõ với BBA

| Question ID | Priority | Topic | Câu hỏi | Vì sao cần làm rõ |
|---|---|---|---|---|
| Q-FIN-01 | P0 | Tài khoản GIRO | Tài khoản GIRO / CDA thuộc cấp Child hay Family? BBA nói thuộc Child, nhưng SRS BR-FEE-030 ghi "a family can have one GIRO (bank) account and one CDA account". | Quyết định cách lưu dữ liệu, cách lọc đợt GIRO và anh chị em dùng chung tài khoản hay không. |
| Q-FIN-02 | P0 | Payment method | Payment method trên tab chỉ hiển thị hay được sửa? Nếu sửa, ai được sửa và có cần duyệt không? (Q-66-10 chưa có trả lời) | Ảnh hưởng tới quy tắc "tab chỉ đọc" và tới hoá đơn tháng sau. |
| Q-FIN-03 | P1 | Hoá đơn Draft | Có hiển thị hoá đơn Draft (tạo ngày 24) trên tab không? Nếu có, cho vai trò nào? | Draft chưa gửi phụ huynh; hiển thị sai đối tượng có thể khiến Centre báo số chưa chốt. |
| Q-FIN-04 | P1 | Quyền xem | Teacher có xem tab Finance không, hay chỉ Centre Director, Centre / School Admin, HQ, Finance? | Dữ liệu tài chính gia đình là dữ liệu nhạy cảm. |
| Q-FIN-05 | P1 | Chuyển Centre / brand | Trẻ chuyển Centre hoặc brand (pháp nhân khác): có hiện hoá đơn và cọc của Centre cũ không? Nhân viên Centre mới có được xem không? | Phạm vi xem của nhân viên Centre và dữ liệu của pháp nhân khác. |
| Q-FIN-06 | P1 | Liên kết và tải tài liệu | Có cho tải / in PDF hoá đơn, biên lai và liên kết sang màn Billing tương ứng (ví dụ Request correction trên Draft) cho người có quyền không? | Quyết định tab chỉ là nơi xem hay còn là lối tắt sang thao tác. |

## 7. Tài liệu tham khảo

Số trang tính theo bản Word gốc của SRS khi xuất PDF khổ A4.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | Plane — ticket BBA-67 (WBS 3.1.1.02) | Description: finance (invoices, balances, GIRO), each linking to the module screen | — | Phạm vi US-004. |
| 2 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §2 Who uses it | 3 | Mục 4. |
| 3 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §3 P1 đến P5 (first invoice, monthly cycle, GIRO, PayNow, refund) | 4–5 | FR-025, FR-029, FR-030. |
| 4 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 2.3 Discounts, 2.4 Corporate accounts | 6 | FR-024, FR-031. |
| 5 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 3.1 Billing runs (change report), 3.2 Invoices | 7 | FR-025, FR-026. |
| 6 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 3.4 Credit notes, 4.1 GIRO accounts, 4.2 GIRO collection runs | 8–9 | FR-024, FR-025, FR-028. |
| 7 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 4.6 Receipts, 4.7 Outstanding & reminders | 9–10 | FR-025, FR-027. |
| 8 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 5.1 Deposit ledger, 5.2 Refunds | 10–11 | FR-029, FR-030. |
| 9 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 6.1 GSII reconciliation; 8.2 Month-end close | 11–12 | FR-031, FR-032. |
| 10 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-001 đến 012 | 12 | BR-FIN-TAB-001 đến 003, 008, 009, 021, 022. |
| 11 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-013 đến 038 | 13 | BR-FIN-TAB-004 đến 007, 010 đến 013, 016, 020. |
| 12 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-039 đến 053 | 14 | BR-FIN-TAB-014, 015, 018, 019. |
| 13 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §8 AC-FEE-004, 008, 009, 011, 013, 015, 020 | 15–16 | Dữ liệu ví dụ cho AC. |
| 14 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.1 View child profile (tab Billing read-only) | 6 | Mục 2. |
| 15 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 BR-CHF-017 (billing contact) | 9 | FR-024. |
| 16 | BBA-SMS-SRS-Parents-App-v0.1 | §4 mục 7.1 Invoices | 13 | FR-023, FR-025. |
| 17 | BBA-SMS-SRS-Parents-App-v0.1 | §4 mục 7.4 Credits, 7.5 Refunds | 14 | FR-023, FR-030. |
| 18 | BBA-SMS-SRS-Daily-Operations-v0.1 | §5 BR-OPS-025 | 10 | BR-FIN-TAB-017. |
