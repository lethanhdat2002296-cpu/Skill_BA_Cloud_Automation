# [Nháp cập nhật] BBA-67 Child Record Tabs – Read Views — các dòng thay đổi

> Nháp để review, **chưa đưa lên Drive / Git**. Áp trên FRD trên Drive. Nguồn: file câu hỏi phản hồi BBA_SMS_S4 (Q-67-04 đến Q-67-08). Đánh số nối tiếp (FR-040, AC-051, OQ-RT-17).
> Nhãn: *(sửa)* · *(mới)*.

**Tóm tắt**
1. Enrichment (Q-67-05, đã chốt): đang học chưa có End date — **khớp FR-009**. Wireframe tab Enrichment đã có sẵn 2 dòng này — FRD bổ sung cho khớp. Bổ sung cách kết thúc "phụ huynh rút qua app" (không hoàn tiền, ghi ngày và lý do); đổi chương trình = rút + đăng ký mới, báo trước 1 tháng.
2. Attendance (Q-67-06, DOTB tự quyết): BBA đề xuất mặc định tháng hiện tại + bộ chọn khoảng ngày. **Giữ thiết kế đã chốt** của tab (không bộ chọn tháng, theo quyết định trước của user) — không sửa.
3. Communication (Q-67-08, đã chốt): nội dung khớp US-005 hiện có (Announcements, Messages, Inquiries, Surveys + consents, Notifications) — không sửa.
4. Communication nhóm theo Enrolment / Centre — chưa phản hồi (Q-67-04) → OQ mới.

---

## US-002 — Tab Enrichment

### Functional Requirements

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-010 *(sửa)* | Dòng lớp đã kết thúc ghi cách kết thúc: "Removed from the class" (Enrichment team gỡ trẻ, kèm End date); "Class closed" (lớp bị đóng, End date là ngày đóng lớp); "Left the school · enrichment invoices stop after" kèm ngày học cuối (trẻ thôi học ở Centre); **"Withdrawn in the Parents App" kèm lý do và "No refund" (phụ huynh rút qua Parents App, End date là ngày rút) (Q-67-05)**. |
| FR-041 *(mới)* | Trẻ đổi chương trình (ví dụ Piano sang Dance) hiện 2 dòng: lớp cũ ở Past với "Switched to Dance · notice given" kèm ngày báo; lớp mới ở Current với "switched from Piano" và Start date riêng (đổi chương trình = rút lớp cũ + đăng ký lớp mới, báo trước 1 tháng) (Q-67-05). |

### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-052 *(mới)* | phụ huynh rút trẻ khỏi Little Chefs qua Parents App ngày 2026-06-30, lý do "Schedule clash" | School Admin chọn Past | Little Chefs hiện End date 2026-06-30 và "Withdrawn in the Parents App · Schedule clash · No refund" | FR-010 |
| AC-053 *(mới)* | trẻ báo đổi Piano sang Dance ngày 2026-08-01, Piano kết thúc 2026-08-31, Dance bắt đầu 2026-09-01 | School Admin mở tab Enrichment | Past có Piano, End date 2026-08-31, "Switched to Dance · notice given 2026-08-01"; Current có Dance "switched from Piano", Start date 2026-09-01 | FR-041 |

---

## Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Ưu tiên | Ghi chú |
|---|---|---|---|
| OQ-RT-18 *(mới)* | Tab Communication có nhóm theo từng Enrolment / Centre để không trộn lịch sử khi trẻ chuyển Centre không? | Cao | Chưa phản hồi (Q-67-04); Q-74-10 chỉ nói lên lớp tạo thread mới, thread cũ chỉ đọc |
