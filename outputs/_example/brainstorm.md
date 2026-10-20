# Brainstorm — Đổi trả hàng online (Magento 2 + Odoo 17)

> Nguồn đã đọc: `bien-ban-hop-kickoff.md`, `email-bo-sung-cskh.md`, `ghi-chu-kho.txt`. Ngày tạo: 2026-10-20.
> Khách hàng: Mộc An Fashion (dữ liệu giả lập).

## 1. Bối cảnh & vấn đề

**Đã biết**
- Website Magento 2.4.6 (Luma tuỳ biến); vận hành trên Odoo 17 (Sales, Inventory, Accounting). Đơn Magento đồng bộ sang Odoo bằng connector có sẵn, 5 phút/lần. (nguồn: bien-ban-hop-kickoff.md)
- Đổi trả hiện làm thủ công: hotline/fanpage → Google Sheet → ảnh qua Zalo → báo kho. (nguồn: bien-ban-hop-kickoff.md)
- 300–350 yêu cầu/tháng, thời gian phản hồi trung bình 3 ngày; khách khiếu nại vì không biết trạng thái; kế toán hoàn tiền sót/trùng. (nguồn: bien-ban-hop-kickoff.md)
- Hàng trả về để chung kho chính, lộn xộn. (nguồn: ghi-chu-kho.txt)

**Chưa biết**
- OQ-01: Chính sách đổi trả chính thức (đang chờ ban giám đốc duyệt, có thể trễ hạn 10/10).

## 2. Mục tiêu kinh doanh

**Đã biết**
- Khách tự tạo và theo dõi yêu cầu đổi trả online; giảm thao tác thủ công của CSKH, kho, kế toán. (nguồn: bien-ban-hop-kickoff.md)
- Go-live trước 15/11/2026 cho mùa sale cuối năm. (nguồn: bien-ban-hop-kickoff.md)
- Có báo cáo số yêu cầu theo lý do hàng tháng. (nguồn: bien-ban-hop-kickoff.md)

**Giả định**
- AS-01: KPI đề xuất — thời gian phản hồi (tạo → duyệt/từ chối) ≤ 24 giờ cho 90% yêu cầu; 0 trường hợp hoàn tiền trùng.

**Chưa biết**
- OQ-02: KPI mục tiêu chính thức (thời gian phản hồi, tỷ lệ khiếu nại) do khách hàng xác nhận.

## 3. Người dùng & vai trò

| Vai trò | Mô tả | Hệ thống | Việc chính | Nguồn |
|---|---|---|---|---|
| Khách hàng | Khách có tài khoản trên website | Storefront Magento | Tạo, theo dõi, huỷ yêu cầu | kickoff |
| Khách hàng VIP | Customer group "VIP" | Storefront Magento | Như khách hàng, hạn 15 ngày | email |
| Nhân viên CSKH | Xử lý yêu cầu | Odoo | Xem, duyệt, từ chối | kickoff, email |
| Trưởng CSKH | Chị Hạnh | Odoo | Nhận cảnh báo quá 48h, xem báo cáo | email |
| Nhân viên kho | Anh Tùng và team | Odoo (máy tính bàn) | Nhận hàng, kiểm tra tình trạng, chuyển location | kickoff, ghi-chu-kho |
| Kế toán | Chị Linh | Odoo Accounting | Hoàn tiền (credit note) | kickoff |
| Hệ thống | Connector Magento ↔ Odoo | — | Đồng bộ yêu cầu, trạng thái, gửi email | kickoff |

**Giả định**
- AS-02: Khách vãng lai (guest checkout) không tạo yêu cầu online; liên hệ hotline như hiện tại.

## 4. Phạm vi

| In scope | Out of scope | Giai đoạn sau |
|---|---|---|
| Tạo yêu cầu đổi/trả trên website (chọn sản phẩm, SL, lý do, ảnh) | Tích hợp API GHN tạo vận đơn trả (ghi-chu-kho) | Tích hợp GHN |
| Kiểm tra điều kiện: đã giao, 7/15 ngày, hàng sale, SL còn lại | Hoàn tiền tự động qua API VNPay/cổng thẻ (AS-05) | Hoàn tiền tự động qua cổng thanh toán |
| Duyệt/từ chối trên Odoo, email khách | App mobile | |
| Theo dõi trạng thái trên website, huỷ yêu cầu | Đổi sang sản phẩm khác (chỉ đổi size cùng sản phẩm) | |
| Nhận hàng, kiểm tra, chuyển location WH/Returns, WH/Stock, WH/Damaged | | |
| Credit note hoàn tiền; đơn đổi giá 0đ | | |
| Cảnh báo quá 48h; báo cáo theo lý do | | |

## 5. Quy trình nghiệp vụ

### 5.1 AS-IS
1. Khách gọi hotline / nhắn fanpage.
2. CSKH ghi Google Sheet, xin ảnh qua Zalo.
3. CSKH báo kho; kho nhận hàng, để chung kho chính.
4. Kế toán đọc Sheet và hoàn tiền thủ công.

### 5.2 TO-BE
1. Khách vào "Đơn hàng của tôi" → chọn đơn đủ điều kiện → tạo yêu cầu (sản phẩm, SL, loại đổi/trả, lý do, ảnh, STK nếu COD).
2. Magento đẩy yêu cầu sang Odoo, trạng thái **Chờ duyệt**.
3. CSKH duyệt → email hướng dẫn gửi hàng kèm mã yêu cầu; hoặc từ chối kèm lý do → email.
4. Khách gửi hàng qua bưu cục GHN hoặc mang tới cửa hàng.
5. Kho quét mã yêu cầu, ghi tình trạng từng sản phẩm, hàng về WH/Returns → nguyên vẹn sang WH/Stock, lỗi sang WH/Damaged. Trạng thái **Đã nhận hàng**.
6. Trả hàng: kế toán xác nhận credit note và hoàn tiền. Đổi hàng: hệ thống tạo đơn đổi giá 0đ. Trạng thái **Hoàn tất**.
7. Khách theo dõi trạng thái trên website ở mọi bước.

### 5.3 Ngoại lệ & nhánh rẽ
- Đơn chưa giao / quá hạn 7 ngày (15 ngày với VIP) → không hiện nút tạo yêu cầu.
- Hàng sale > 50% → chỉ được chọn "Đổi size".
- Tổng SL trả vượt SL đã mua (nhiều yêu cầu cho một đơn) → chặn.
- Lý do "Sản phẩm lỗi"/"Giao sai sản phẩm" mà không có ảnh → chặn.
- Khách huỷ khi đang Chờ duyệt.
- Quá 48 giờ chưa duyệt → cảnh báo trưởng CSKH.
- Hàng nhận về thiếu phụ kiện / lỗi do khách → OQ-07.
- Đổi size nhưng size mới hết hàng → OQ-06.
- Khách không gửi hàng sau khi duyệt → OQ-08.

## 6. Tích hợp & dữ liệu

| Hệ thống | Vai trò | Dữ liệu trao đổi | Chiều | Tần suất | Nguồn |
|---|---|---|---|---|---|
| Magento 2.4.6 | Kênh khách tạo/theo dõi yêu cầu | Yêu cầu, dòng sản phẩm, ảnh, STK | M2 → Odoo | Gần realtime (AS-03) | kickoff |
| Odoo 17 | Source of truth của trạng thái yêu cầu, kho, kế toán | Trạng thái, lý do từ chối | Odoo → M2 | Gần realtime (AS-03) | kickoff |
| Connector hiện có | Đồng bộ đơn hàng 5 phút/lần | Đơn hàng, khách hàng | M2 → Odoo | 5 phút | kickoff |
| Email (SMTP Magento) | Thông báo khách | Email duyệt/từ chối/hoàn tất | M2 → khách | Theo sự kiện | kickoff, email |
| GHN | Vận chuyển gửi trả | — | — | Giai đoạn 2 | ghi-chu-kho |

**Giả định**
- AS-03: Đồng bộ yêu cầu và trạng thái qua queue, độ trễ ≤ 5 phút (cùng cơ chế connector hiện có).
- AS-04: Ngày giao = ngày đơn Magento chuyển trạng thái "Complete" (được cập nhật từ phiếu giao hàng Odoo).

**Chưa biết**
- OQ-03: Nguồn chính xác của "ngày giao" (trạng thái Magento hay ngày hoàn tất phiếu xuất Odoo/GHN)?

## 7. Ràng buộc & rủi ro

| Loại | Nội dung | Mức độ | Giảm thiểu |
|---|---|---|---|
| Thời gian | Go-live trước 15/11/2026 | Cao | Ưu tiên Must; báo cáo để sau nếu trễ |
| Chính sách | Chính sách chính thức chưa có (OQ-01) | Cao | Tham số hoá hạn ngày, lý do, % sale trong cấu hình |
| Pháp lý | STK ngân hàng là dữ liệu cá nhân | Trung bình | Mã hoá, phân quyền chỉ kế toán xem đầy đủ |
| Kỹ thuật | Connector hiện có đồng bộ batch 5 phút | Trung bình | Dùng chung queue, xử lý retry |
| Vận hành | Kho chỉ dùng máy tính bàn | Thấp | Màn kho tối ưu desktop + máy quét mã vạch |

**Giả định**
- AS-05: Hoàn tiền thẻ/VNPay do kế toán thực hiện thủ công trên cổng thanh toán; Odoo chỉ ghi nhận credit note và đánh dấu đã hoàn.
- AS-06: Phí ship gửi trả: lý do "Đổi ý" khách chịu; lý do khác shop chịu bằng cách cộng phí ship (theo biên nhận bưu cục, tối đa 50.000₫) vào số tiền hoàn.
- AS-07: Với đơn COD, khách nhập STK ngân hàng ngay trên form tạo yêu cầu.

**Chưa biết**
- OQ-04: Phí ship gửi trả xử lý cụ thể thế nào ("tuỳ trường hợp")? Mức trần?
- OQ-05: Ai nhập STK cho đơn COD — khách trên website hay CSKH khi gọi xác nhận?

## Đề xuất của BA (chưa phải yêu cầu)
- In phiếu yêu cầu (PDF có mã vạch) để khách dán ngoài gói hàng — giúp kho quét mã (ghi-chu-kho nêu việc quét mã).
- Cấu hình hạn đổi trả theo customer group thay vì hard-code 7/15 ngày.

## Assumptions & Open Questions

| Mã | Nội dung | Loại | Liên quan |
|---|---|---|---|
| AS-01 | KPI đề xuất: phản hồi ≤ 24h cho 90% yêu cầu; 0 hoàn tiền trùng | AS | Mục tiêu |
| AS-02 | Guest không tạo yêu cầu online | AS | Vai trò |
| AS-03 | Đồng bộ yêu cầu/trạng thái qua queue, trễ ≤ 5 phút | AS | Tích hợp |
| AS-04 | Ngày giao = ngày đơn Magento "Complete" | AS | Điều kiện đổi trả |
| AS-05 | Hoàn tiền thẻ/VNPay thủ công trên cổng; Odoo ghi nhận credit note | AS | Hoàn tiền |
| AS-06 | "Đổi ý" khách chịu ship; lý do khác shop hoàn phí ship tối đa 50.000₫ | AS | Hoàn tiền |
| AS-07 | Đơn COD: khách nhập STK trên form tạo yêu cầu | AS | Hoàn tiền |
| AS-08 | Hàng sale > 50% = (giá gốc − giá bán thực tế dòng đơn) / giá gốc > 50% | AS | Điều kiện đổi trả |
| AS-09 | Mỗi yêu cầu có một loại (Trả hàng hoặc Đổi size) cho mọi dòng | AS | Tạo yêu cầu |
| AS-10 | Cảnh báo 48h tính theo giờ thực, không trừ ngày nghỉ | AS | Cảnh báo |
| OQ-01 | Chính sách đổi trả chính thức (hạn, lý do, điều kiện)? | OQ | Toàn bộ |
| OQ-02 | KPI mục tiêu chính thức? | OQ | Mục tiêu |
| OQ-03 | Nguồn của "ngày giao"? | OQ | Điều kiện đổi trả |
| OQ-04 | Quy tắc phí ship gửi trả và mức trần? | OQ | Hoàn tiền |
| OQ-05 | Ai nhập STK cho đơn COD? | OQ | Hoàn tiền |
| OQ-06 | Đổi size mà size mới hết hàng thì xử lý thế nào (chờ / chuyển sang trả hàng)? | OQ | Đổi hàng |
| OQ-07 | Hàng nhận về thiếu phụ kiện / lỗi do khách: từ chối hay hoàn một phần? | OQ | Nhận hàng |
| OQ-08 | Sau khi duyệt, khách có hạn gửi hàng không (vd. 7 ngày) — quá hạn thì tự huỷ? | OQ | Quy trình |
