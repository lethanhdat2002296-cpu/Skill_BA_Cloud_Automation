# GPT — BA Workspace

Thư mục bàn giao tài liệu do GPT hỗ trợ phân tích, review và soạn thảo cho dự án BBA.

## Cách đọc dành cho Claude

- Nhánh: `docs/bba-chat-history`.
- Đọc tài liệu phiên bản mới nhất trong `GPT/BBA/<ticket>/` trước.
- Đối chiếu với backlog gốc và nguồn khảo sát; FRS nháp không phải yêu cầu khách hàng đã phê duyệt.
- Không tự mở rộng scope. Tách các chính sách chưa xác nhận thành Open Questions.
- Đặc tả nghiệp vụ: Functional Requirements, Business Rules, Validation Rules, Functional Flow, Acceptance Criteria; không đưa giải pháp kỹ thuật vào phạm vi nghiệp vụ.
- Giữ các mã yêu cầu còn hiệu lực và không tái sử dụng mã đã loại bỏ. Không chỉnh sửa bản gốc khi chỉ thực hiện review.

## Danh mục

| Task BA | Tính năng | Tài liệu mới nhất | Trạng thái |
|---|---|---|---|
| BBA-729 | BBA-145 — Child Switcher | [FRS v0.2](BBA/BBA-729/FRS-BBA-145-Child-Switcher-v0.2.md) | Bản nháp chờ review |

## Quyết định BA mới nhất — 28/11/2026

- Loại FR-001: Child Card không phải nghiệp vụ độc lập.
- FR-002: Hiển thị danh sách trẻ của phụ huynh.
- Giữ FR-003: Chuyển đổi trẻ để xem thông tin tương ứng.
- Loại FR-004 và FR-005 khỏi FR độc lập: ghi nhớ trẻ và điều hướng từ Notification là hành vi mặc định.
- Chỉ giữ US-001; rà soát lại BR, VAL, AC, flow, dữ liệu, UI reference, dependencies và phạm vi.
- Các chính sách về Brand/Centre/Country, trạng thái ghi danh, lịch sử, thứ tự danh sách và thông tin nhận diện chờ xác nhận.
- Bản v0.2 là đề xuất để BA review; chưa được BBA phê duyệt.

## Lịch sử trao đổi

[BBA-729 — Lịch sử review ban đầu ngày 28/11/2026](../chat-history/bba/BBA-729/2026-11-28_BBA-729_Child-Switcher.md).

Lịch sử cũ giữ nguyên để truy vết; nếu có điểm khác nhau, ưu tiên quyết định BA mới nhất và bản FRS v0.2.

Repository hiện ở chế độ Public. Không đưa đường dẫn nội bộ hoặc dữ liệu cá nhân thật vào các bản bàn giao.
