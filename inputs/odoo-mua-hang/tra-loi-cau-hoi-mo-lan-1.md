# Trả lời câu hỏi mở lần 1 — Quy trình mua hàng Odoo

| Thuộc tính | Giá trị |
|---|---|
| Nguồn | Chat (BA dự án, trả lời Open Questions của SRS v0.2) |
| Ngày tài liệu | không ghi |
| Ngày nạp | 2026-10-20 |
| Loại | Ghi chú (trả lời câu hỏi mở) |

## Tóm tắt
- Odoo phiên bản 17, "bản mua Account".
- Quy trình hiện tại làm thủ công, cần cải thiện.
- Không gộp nhiều Yêu cầu mua hàng cùng vendor vào một RFQ.
- Gửi 1 email cho nhiều vendor; nội dung email là danh sách sản phẩm theo phiếu.
- Đơn mua hàng không có ngưỡng duyệt; bị từ chối thì về trạng thái Nháp và báo user qua email.

## Nội dung có cấu trúc

### Bối cảnh / hệ thống
- Phiên bản Odoo: 17 — "Bản mua Account".
- Quy trình hiện tại: đều đang làm thủ công → cần cải thiện quy trình.

### Quy tắc nghiệp vụ
- Không cho phép gộp nhiều Yêu cầu mua hàng (YCMH) cùng vendor vào một RFQ.
- Gửi 1 email cho nhiều vendor; nội dung email là 1 danh sách sản phẩm theo phiếu.
- Đơn mua hàng không có ngưỡng (người làm ghi: "Hiện tại là vậy").
- Bị từ chối → quay lại trạng thái Nháp và thông báo cho user qua email.

### Ghi chú
- Người làm: "Trước mắt tao trả lời vậy đã" — đây là câu trả lời bước đầu, chưa đủ cho mọi câu hỏi mở.

## Nguyên văn

```text
* Phiên bản Odoo - Ver 17 - Bản mua Account
* QUy trình hiện tại đều đang thủ công -> cần cải thiện quy trình 
* Không cho phép gộm nhiều YCMH cùng vendor vào một RFQ
* Gửi 1 email cho nhiều vendor, nội dùng Email sẽ là 1 list sản phẩm theo phiếu
* Đơn mua hàng sẽ không có ngưỡng nhé (Hiện tại là dị)
* Nếu bị từ trối sẽ back lại trạng thái nháp và thông báo cho user lại qua Email 

Trước mawtys tao trả lời dị đã
```
