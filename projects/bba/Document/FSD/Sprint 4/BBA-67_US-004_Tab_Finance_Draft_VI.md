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
| Phiên bản | 0.3 (nháp) |
| Trạng thái | BẢN NHÁP ĐỂ RÀ SOÁT |
| Ngày | 11/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 (nháp) | 11/11/2026 | Business Analysis | Bản nháp đầu theo SRS Fees & Payments, Children & Families, Parents App: 9 khối chi tiết. | HaiNguyen |
| 0.2 (nháp) | 11/11/2026 | Business Analysis | Thu gọn thành màn tổng quan. | HaiNguyen |
| 0.3 (nháp) | 11/11/2026 | Business Analysis | Tách khối Tóm tắt và khối Cần chú ý sang backlog (BL-FIN-01, BL-FIN-02), làm sau. Tab còn 4 khối: Invoices, Payment method, Deposit & refunds, Discounts & subsidies. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả màn tổng quan 4 khối, quyền xem theo vai trò, 11 quy tắc, 12 tiêu chí nghiệm thu. 7 điểm chưa chốt ghi thành giả định và câu hỏi ở mục 6.

## 2. Mục đích và phạm vi

| Điểm chính | Căn cứ |
|---|---|
| Tab Finance là **bảng tổng quan** tài chính của một trẻ, khác các màn Billing (xem theo Centre, tháng, đợt). Nhìn vào là biết hoá đơn gần đây, trẻ trả bằng gì, cọc còn bao nhiêu, đang được giảm giá và trợ cấp gì. | SRS Fees & Payments §4 mục 3.1, 3.2 (tr.7); định hướng của BA phụ trách |
| Giúp Centre trả lời nhanh phụ huynh: "sao tháng này hoá đơn cao", "tiền cọc còn bao nhiêu", "sao chưa trừ GIRO". | Định hướng của BA phụ trách |
| Chi tiết (từng dòng hoá đơn, biên lai, credit note, sổ cọc, tài khoản GIRO đầy đủ) xem ở màn Billing của Fees & Payments; mỗi khối có liên kết sang màn tương ứng. | SRS Fees & Payments §4 mục 3.2, 4.1, 5.1, 5.2 (tr.7–10) |
| Tab **chỉ đọc**. Tạo, sửa hoá đơn, credit note, hoàn tiền, tài khoản GIRO làm hoặc duyệt trong Billing bởi Finance. | BR-FEE-007, 008 (tr.12); BR-FEE-027, 041 (tr.13–14) |

**Ngoài phạm vi tab:** khối Tóm tắt và khối Cần chú ý (backlog BL-FIN-01, BL-FIN-02); chi tiết từng dòng hoá đơn; danh sách biên lai; danh sách credit note; sổ biến động cọc; DDA reference và cách đăng ký GIRO; tải hoặc in PDF; mọi thao tác.

## 3. Quyền xem theo vai trò

| Vai trò | Thấy tab Finance | Phạm vi | Căn cứ |
|---|---|---|---|
| HQ Admin, HQ Finance | Có | Mọi Centre | SRS Fees & Payments §2 (tr.3) |
| Centre Director, Centre Admin / School Admin | Có | Centre của mình | SRS Fees & Payments §2 (tr.3) |
| HQ Enrolment | Theo quyền | Mọi Centre | FRD v0.6 mục 4 |
| Teacher | Không (giả định) | — | AS-FIN-04, chờ Q-FIN-04 |
| Enrichment Trainer | Không | — | FRD v0.6 mục 4 |
| Parent | Không dùng tab này; xem trong Parents App | — | SRS Parents App §4 mục 7 |

## 4. Yêu cầu chức năng

### 4.1 US-004 - Tab Finance: tổng quan tài chính của trẻ

#### User Story

Là Centre Director hoặc School Admin, tôi muốn nhìn vào hồ sơ trẻ là thấy các hoá đơn gần đây và trạng thái GIRO, trẻ trả bằng gì, cọc còn bao nhiêu, đang được giảm giá và trợ cấp gì, để trả lời phụ huynh ngay mà không phải vào Billing.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-022 | Tab Finance là màn tổng quan, chỉ hiển thị; không có thao tác. Mỗi khối có liên kết mở màn tương ứng của Fees & Payments đã lọc theo trẻ: "View all invoices" (Invoices), "Open in GIRO accounts", "Open in Deposit ledger", "Open in Billing" (Discounts) (AS-FIN-06). |
| FR-023 | Khối **Invoices** hiện tối đa 6 hoá đơn: mọi hoá đơn chưa trả hết, rồi các hoá đơn mới nhất cho đủ 6 (AS-FIN-07). Mỗi dòng: tháng, loại (School fees / Enrichment / Registration / Ad hoc), số tiền, số dư, trạng thái ("Due 5 Nov", "Overdue · 34 days", "Paid", "Draft"), trạng thái GIRO nếu có ("GIRO deduction scheduled · 5 Nov", "Being collected by GIRO", "GIRO deduction failed"), nhãn CDA nếu là hoá đơn CDA. Tab không mở chi tiết từng dòng hoá đơn. |
| FR-024 | Dưới danh sách hoá đơn có một dòng "What changed from last month" cho hoá đơn học phí tháng mới nhất, lấy từ change report của đợt tính phí (ví dụ "Additional subsidy ended 30 Sep"); không có thay đổi thì không hiện dòng này. |
| FR-025 | Khối **Payment method**: phương thức của trẻ (GIRO, GIRO CDA hoặc PayNow), Bill to (Parent / tên công ty), mỗi tài khoản GIRO một dòng: loại (GIRO / CDA), ngân hàng, số tài khoản che chỉ còn 4 số cuối, trạng thái (Pending with bank / Active / Rejected kèm lý do). |
| FR-026 | Khối **Deposit & refunds**: một dòng cọc (số tiền đang giữ, nguồn CDA / non-CDA, số tháng cọc, ghi "+1 month, not on GIRO" khi trẻ không trả bằng GIRO); hoàn tiền chỉ hiện khi chưa xong (Pending approval, Approved, Processing) hoặc thất bại (Unsuccessful, Void kèm lý do): số tiền, trạng thái, nơi nhận (CDA / PayNow). |
| FR-027 | Khối **Discounts & subsidies**: mỗi giảm giá đang áp một dòng (tên, giá trị, đến ngày); trợ cấp Basic / Additional một dòng (số tiền mỗi tháng). |
| FR-028 | Trẻ ở Centre Singapore chỉ thấy SGD và phương thức của Singapore; trẻ ở Centre Malaysia chỉ thấy MYR và phương thức của Malaysia, không có tài khoản GIRO / CDA, trợ cấp ECDA. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở tab Finance; hệ thống hiển thị Invoices, Payment method, Deposit & refunds, Discounts & subsidies (FR-023 đến FR-027).
2. Người dùng đọc trạng thái hoá đơn, trạng thái GIRO và dòng "What changed from last month" để trả lời phụ huynh (FR-023, FR-024).
3. Cần xem chi tiết hoặc thao tác: người dùng chọn liên kết của khối để sang màn Fees & Payments (FR-022).

#### Functional Flow - Alternative (Luồng thay thế)

1. Hoá đơn tháng mới nhất không khác tháng trước: không hiện dòng "What changed from last month" (FR-024).
2. Không có hoàn tiền đang xử lý hay thất bại: khối Deposit & refunds chỉ có dòng cọc (FR-026).
3. Trẻ ở Centre Malaysia: không có tài khoản GIRO / CDA, trợ cấp ECDA (FR-028; VAL-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò không được xem tab Finance: không có tab (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-FIN-TAB-001 | Tab chỉ đọc. Tạo, sửa hoá đơn, credit note, hoàn tiền, tài khoản GIRO làm hoặc duyệt trong Billing bởi Finance (BR-FEE-007, 008, 027, 041). |
| BR-FIN-TAB-002 | Partially paid và Overdue tính từ thanh toán và ngày đến hạn (mặc định ngày 5 của tháng hoá đơn), không đặt tay (BR-FEE-003, 006). |
| BR-FIN-TAB-003 | Payment method thuộc hồ sơ trẻ: GIRO, GIRO CDA hoặc PayNow; ngoài ra trả tay bằng bank transfer, AXS, cheque. Mỗi hoá đơn mang theo phương thức để Finance lọc (thông tin BBA đã chốt; BR-FEE-037). |
| BR-FIN-TAB-004 | Một trẻ có tối đa 2 tài khoản GIRO: CDA và non-CDA; CDA và non-CDA xuất hoá đơn riêng (thông tin BBA đã chốt; BR-FEE-030 — chờ Q-FIN-01). |
| BR-FIN-TAB-005 | Số tài khoản ngân hàng luôn che, chỉ hiện 4 số cuối (SRS Fees & Payments §4 mục 4.1 Mask account number). |
| BR-FIN-TAB-006 | Hoá đơn trong đợt 1ST DD chưa có kết quả hiện "Being collected by GIRO"; GIRO thất bại giữ hoá đơn chưa trả (BR-FEE-033, 034). |
| BR-FIN-TAB-007 | Học phí và enrichment là hai hoá đơn riêng (BR-FEE-011). |
| BR-FIN-TAB-008 | Nguồn của mọi khoản cọc (CDA / non-CDA) được ghi. Trẻ không trả bằng GIRO cọc thêm 1 tháng; số tháng cọc cài theo brand và Centre (BR-FEE-021, 022). |
| BR-FIN-TAB-009 | Tiền trả từ CDA chỉ hoàn về CDA; hoàn tiền thất bại tự void và chờ phụ huynh cập nhật tài khoản (BR-FEE-042, 044). |
| BR-FIN-TAB-010 | Giảm giá hết hạn được gỡ tự động ở đợt tính phí sau và ghi trong change report (BR-FEE-018; SRS Fees & Payments §4 mục 3.1 View change report). |
| BR-FIN-TAB-011 | Centre Singapore không hiện phương thức hay tiền tệ của Malaysia, và ngược lại (BR-FEE-038; chiều Malaysia theo thông tin BBA). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Trẻ thuộc Centre Malaysia. | Không hiển thị tài khoản GIRO / CDA, trợ cấp ECDA; tiền tệ MYR. |
| VAL-004 | Vai trò không được xem tab Finance. | Không hiển thị tab Finance. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-04 - Tab Finance | Wireframe: Diagram/Wireframe/finance-draft-sprint4.html |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Invoices | Danh sách gọn | Có | Tối đa 6 dòng; chưa trả trước | — | FR-023; FR-024; "View all invoices". |
| Payment method | Khối gọn | Có | — | VAL-003. | FR-025. |
| Deposit & refunds | Khối gọn | Có | — | — | FR-026. |
| Discounts & subsidies | Khối gọn | Có | — | VAL-003. | FR-027. |

**Đặc tả trường theo khối**

| Khối | Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|---|
| Invoices | Month, Type, Amount, Balance | Text, số tiền | Fees & Payments › Invoices | BR-FIN-TAB-007. |
| Invoices | Status | Nhãn | Invoices | Due / Overdue · n days / Paid / Draft (BR-FIN-TAB-002; AS-FIN-03). |
| Invoices | GIRO state | Text nhỏ | GIRO collection runs | BR-FIN-TAB-006. |
| Invoices | CDA | Nhãn | Invoices | Chỉ hiện với hoá đơn CDA (BR-FIN-TAB-004). |
| Invoices | What changed from last month | Một dòng | Billing run change report | FR-024; BR-FIN-TAB-010. |
| Payment method | Payment method, Bill to | Text | Hồ sơ trẻ; Corporate accounts | BR-FIN-TAB-003. |
| Payment method | GIRO account | Một dòng mỗi tài khoản | GIRO accounts | Loại, ngân hàng, "••••4021", trạng thái; Rejected kèm lý do (BR-FIN-TAB-004, 005). |
| Deposit & refunds | Deposit | Một dòng | Deposit ledger, fee scheme | Số tiền, nguồn, số tháng (BR-FIN-TAB-008). |
| Deposit & refunds | Refund | Một dòng | Refunds | Chỉ khi chưa xong hoặc thất bại: số tiền, trạng thái, nơi nhận (BR-FIN-TAB-009). |
| Discounts & subsidies | Discount | Một dòng | Discounts | Tên, giá trị, đến ngày. |
| Discounts & subsidies | Subsidy | Một dòng | Hồ sơ trẻ, subsidy lines | Basic / Additional, số tiền mỗi tháng; chỉ Singapore. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Tab đọc payment method từ hồ sơ trẻ; đọc từ Fees & Payments: tối đa 6 hoá đơn (tháng, loại, số tiền, số dư, trạng thái, trạng thái GIRO, CDA), dòng change report của hoá đơn học phí tháng mới nhất, tài khoản GIRO (loại, ngân hàng, 4 số cuối, trạng thái, lý do), cọc đang giữ (số tiền, nguồn, số tháng), hoàn tiền chưa xong hoặc thất bại, giảm giá đang áp, trợ cấp. Tab không ghi dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-027 | hôm nay 2026-11-08; hoá đơn học phí tháng 10 của Ethan còn 57.58, hạn 2026-10-05 | Centre Director mở tab Finance | dòng hoá đơn tháng 10 hiện số dư 57.58 và "Overdue · 34 days" | FR-023; BR-FIN-TAB-002 |
| AC-028 | hoá đơn enrichment tháng 10 trừ GIRO thất bại ngày 12 Oct | School Admin mở tab Finance | dòng hoá đơn loại Enrichment ghi "GIRO deduction failed" và vẫn còn số dư; học phí và enrichment là hai dòng riêng | FR-023; BR-FIN-TAB-006; BR-FIN-TAB-007 |
| AC-029 | hoá đơn học phí tháng 11 phần CDA đang trong đợt 1ST DD chưa có kết quả | School Admin mở tab Finance | dòng hoá đơn có nhãn CDA và "Being collected by GIRO" | FR-023; BR-FIN-TAB-004; BR-FIN-TAB-006 |
| AC-030 | hoá đơn tháng 10 cao hơn tháng 9 vì Additional subsidy hết ngày 30 Sep | School Admin mở tab Finance | có dòng "What changed from last month: Additional subsidy ended 30 Sep"; không có bảng chi tiết từng dòng hoá đơn | FR-024; BR-FIN-TAB-010 |
| AC-031 | Ethan có 9 hoá đơn, 3 hoá đơn chưa trả hết | School Admin mở tab Finance | khối Invoices hiện 6 dòng: 3 hoá đơn chưa trả hết và 3 hoá đơn mới nhất còn lại; "View all invoices" mở Fees & Payments › Invoices đã lọc theo Ethan | FR-023; FR-022 |
| AC-032 | Ethan trả bằng GIRO; tài khoản GIRO DBS ••••4021 Active, CDA OCBC ••••7730 Active | School Admin mở tab Finance | Payment method hiện "GIRO", Bill to "Parent" và 2 dòng "GIRO · DBS · ••••4021 · Active", "CDA · OCBC · ••••7730 · Active"; không có DDA reference hay nút sửa | FR-025; BR-FIN-TAB-001; BR-FIN-TAB-003; BR-FIN-TAB-005 |
| AC-033 | tài khoản CDA của Zoe bị ngân hàng từ chối, lý do "Signature mismatch" | School Admin mở tab Finance | dòng tài khoản CDA hiện "Rejected · Signature mismatch" | FR-025 |
| AC-034 | Chloe không trả bằng GIRO, cọc 3 tháng (2 + 1) từ nguồn non-CDA | School Admin mở tab Finance | Deposit hiện số tiền, "non-CDA", "3 months (+1 month, not on GIRO)" | FR-026; BR-FIN-TAB-008 |
| AC-035 | cọc 500.00 của Mia trả từ CDA, có yêu cầu hoàn tiền đang Pending approval | Centre Director mở tab Finance | Deposit & refunds có dòng "Refund 500.00 · Pending approval · to CDA" | FR-026; BR-FIN-TAB-009 |
| AC-036 | Ethan có Staff child discount 50% đang áp, Basic subsidy SGD 300 mỗi tháng | School Admin mở tab Finance | Discounts & subsidies hiện "Staff child discount · 50%" và "Basic subsidy · SGD 300.00 / month" | FR-027; DATA-004 |
| AC-037 | Iman thuộc Centre Malaysia | HQ Finance mở tab Finance | tiền tệ MYR; không có tài khoản GIRO / CDA, trợ cấp ECDA | FR-028; VAL-003; BR-FIN-TAB-011 |
| AC-038 | Teacher không được xem tab Finance | Teacher mở hồ sơ Ethan | không có tab Finance | VAL-004 |

#### Dependencies (Phụ thuộc)

Fees & Payments (Invoices, change report, GIRO accounts, GIRO collection runs, Deposit ledger, Refunds, Discounts); hồ sơ trẻ (payment method); Roles & permissions.

## 5. Backlog liên quan

| Mã | Hạng mục | Nơi lưu |
|---|---|---|
| BL-FIN-01 | Khối Tóm tắt (Outstanding, Credit remaining, Deposit held) | Document/Backlog/Sprint 4/BBA-67_Finance_Tab_Backlog_VI.md (chỉ trên Git) |
| BL-FIN-02 | Khối Cần chú ý (quá hạn, GIRO thất bại, tài khoản bị từ chối, hoàn tiền thất bại, nguy cơ mất trợ cấp, chênh lệch GSII) | như trên |

## 6. Điểm chưa chốt

### Giả định của BA

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-FIN-01 | Tài khoản GIRO / CDA thuộc trẻ (theo thông tin BBA), mỗi trẻ tối đa 1 GIRO và 1 CDA. | FR-025; BR-FIN-TAB-004 — chờ Q-FIN-01 |
| AS-FIN-02 | Payment method trên tab chỉ hiển thị. | FR-025 — chờ Q-FIN-02 |
| AS-FIN-03 | Hoá đơn Draft hiển thị với nhãn Draft. | FR-023 — chờ Q-FIN-03 |
| AS-FIN-04 | Teacher không thấy tab Finance. | Mục 3; VAL-004 — chờ Q-FIN-04 |
| AS-FIN-05 | Trẻ chuyển Centre: hoá đơn của Centre cũ vẫn có trong khối Invoices và "View all invoices". | FR-023 — chờ Q-FIN-05 |
| AS-FIN-06 | Tab có liên kết sang Fees & Payments theo quyền; không có tải PDF, in, Request correction trên tab. | FR-022 — chờ Q-FIN-06 |
| AS-FIN-07 | Khối Invoices hiện tối đa 6 dòng (mọi hoá đơn chưa trả hết, rồi hoá đơn mới nhất). | FR-023 — chờ Q-FIN-07 |

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
| 2 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §2 Who uses it | 3 | Mục 3. |
| 3 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §3 P2 Monthly billing cycle, P3 GIRO collection | 4 | FR-023. |
| 4 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 3.1 Billing runs (change report), 3.2 Invoices | 7 | FR-023, FR-024. |
| 5 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 4.1 GIRO accounts, 4.2 GIRO collection runs | 8–9 | FR-023, FR-025. |
| 6 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §4 mục 5.1 Deposit ledger, 5.2 Refunds | 10–11 | FR-026. |
| 7 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-003 đến 011 | 12 | BR-FIN-TAB-001, 002, 007. |
| 8 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-018 đến 038 | 13 | BR-FIN-TAB-003 đến 006, 008, 010, 011. |
| 9 | BBA-SMS-SRS-Fees-and-Payments-v0.1 | §5 BR-FEE-041 đến 044 | 14 | BR-FIN-TAB-001, 009. |
