# Backlog — Tab Finance trên hồ sơ trẻ (BBA-67, US-004)

> Hai khối tách ra khỏi bản nháp US-004 ngày 11/11/2026 để làm sau. Chỉ lưu trên Git, chưa đưa lên Drive, chưa nằm trong FRD.
> Nguồn: bản nháp `FSD/Sprint 4/BBA-67_US-004_Tab_Finance_Draft_VI.md` v0.2 (commit ae9879e), SRS Fees & Payments v0.1, SRS Parents App v0.1, SRS Daily Operations v0.1.

| Mã | Hạng mục | Trạng thái | Ưu tiên | Ghi chú |
|---|---|---|---|---|
| BL-FIN-01 | Khối Tóm tắt (3 số) | Để sau | Chưa xếp | Tách khỏi US-004 v0.3. |
| BL-FIN-02 | Khối Cần chú ý (Needs attention) | Để sau | Chưa xếp | Tách khỏi US-004 v0.3. |

## BL-FIN-01 — Khối Tóm tắt

**Mô tả:** đầu tab Finance có 3 số: Outstanding (tổng số dư các hoá đơn Billed chưa trả hết), Credit remaining (credit chưa dùng, ghi riêng phần CDA), Deposit held (cọc đang giữ, ghi riêng phần CDA).

**Vì sao cần:** trả lời ngay câu "con còn nợ bao nhiêu", dùng cùng cách tính với Parents App để Centre và phụ huynh thấy cùng một con số.

| Tên trường | Kiểu hiển thị | Nguồn dữ liệu | Quy tắc / ghi chú |
|---|---|---|---|
| Outstanding | Số tiền | Fees & Payments › Invoices | Tổng số dư hoá đơn Billed, Partially paid, Overdue; không tính Draft, Void. |
| Credit remaining | Số tiền + "of which CDA" | Fees & Payments (unused credit) | Như Parents App "View credit remaining". |
| Deposit held | Số tiền + "of which CDA" | Fees & Payments › Deposit ledger | — |

**Quy tắc liên quan**
- Outstanding = tổng số dư các hoá đơn Billed chưa trả hết (Billed, Partially paid, Overdue); không tính Draft và Void (BR-FEE-006; SRS Parents App §4 mục 7.1, tr.13).
- Credit còn lại hiển thị riêng phần CDA (SRS Parents App §4 mục 7.4, tr.14).

**Tiêu chí nghiệm thu dự kiến**

| Given | When | Then |
|---|---|---|
| hôm nay 2026-11-08; Ethan có 3 hoá đơn Billed chưa trả hết: 300.00, 270.00 và 57.58; 1 hoá đơn Draft 460.00 | Centre Director mở tab Finance | Outstanding hiện SGD 627.58; Draft không tính vào |
| Ethan còn credit 30.00, toàn bộ từ CDA | Centre Director mở tab Finance | Credit remaining hiện SGD 30.00, "of which CDA SGD 30.00" |

**Câu hỏi khi làm:** có tính hoá đơn của Centre cũ (trẻ đã chuyển Centre) vào Outstanding không (liên quan Q-FIN-05).

## BL-FIN-02 — Khối Cần chú ý (Needs attention)

**Mô tả:** khối chỉ hiện khi có ít nhất một việc; mỗi việc một dòng ngắn kèm liên kết sang màn Billing.

| Việc | Nội dung dòng | Nguồn dữ liệu | Căn cứ |
|---|---|---|---|
| Hoá đơn quá hạn | Số hoá đơn, số ngày quá hạn, số tiền, các ngày đã nhắc (15, 25) | Invoices; Outstanding & reminders | BR-FEE-003, 004, 006 |
| GIRO trừ thất bại | Hoá đơn, ngày, lý do ngân hàng | GIRO collection runs | BR-FEE-033 |
| Tài khoản GIRO bị Rejected | Loại tài khoản, lý do | GIRO accounts | SRS Fees & Payments §4 mục 4.1 |
| Hoàn tiền Unsuccessful | Số tiền, lý do | Refunds | BR-FEE-044 |
| Nguy cơ mất trợ cấp | Trẻ Singapore đã qua ngày kiểm tra (mặc định ngày 18) chưa có ngày đi học nào trong tháng | Daily Operations ("No attendance this month") | BR-OPS-025 |
| Chênh lệch GSII chưa xử lý | Tháng, loại chênh lệch | GSII reconciliation | BR-FEE-048, 049 |

**Vì sao cần:** gom các cảnh báo về một chỗ để trả lời nhanh "sao chưa trừ GIRO", "con có bị mất trợ cấp không" mà không phải đọc từng khối.

**Tiêu chí nghiệm thu dự kiến**

| Given | When | Then |
|---|---|---|
| hoá đơn học phí tháng 10 của Ethan còn 57.58, quá hạn 34 ngày, đã nhắc 15 và 25 Oct | Centre Director mở tab Finance | có dòng "34 days overdue · SGD 57.58 · reminded 15 Oct, 25 Oct" |
| ngày 19/10/2026 Ava (công dân Singapore) chưa có ngày đi học nào trong tháng 10 | Centre Director mở tab Finance | có dòng nguy cơ mất trợ cấp tháng 10 |
| đối soát GSII tháng 9 có chênh lệch trợ cấp của Ethan chưa được Centre quyết định | Centre Director mở tab Finance | có dòng chênh lệch GSII tháng 9; liên kết mở màn GSII |
| không có việc nào ở trên | Centre Director mở tab Finance | không hiện khối Cần chú ý |

**Câu hỏi khi làm:** thứ tự ưu tiên các dòng khi có nhiều việc (Parents App chỉ hiện 1 nhắc phí theo thứ tự GIRO failed → overdue, BR-PAR-010); có cần hiện khối này cho mọi vai trò được xem tab không.
