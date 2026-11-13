# [Nháp cập nhật] BBA-66 Child Record Overview — các dòng thay đổi

> Nháp để review, **chưa đưa lên Drive / Git**. Áp trên FRD trên Drive v0.3. Nguồn: file câu hỏi phản hồi BBA_SMS_S4 (Q-66-09 đến Q-66-14). Đánh số nối tiếp v0.3 (FR-029, AC-037, OQ-OVW-15).
> Nhãn: *(sửa)* · *(mới)*.

**Tóm tắt**
1. Payment method **thuộc hồ sơ trẻ**: GIRO, GIRO CDA hoặc PayNow; một trẻ có thể có 2 tài khoản GIRO (CDA và non-CDA), invoice CDA và non-CDA xuất riêng (Q-66-09, đã chốt).
2. Định danh trẻ = **số giấy khai sinh hoặc hộ chiếu** (Q-66-14); khi trùng chặn hay chỉ cảnh báo — chưa trả lời.
3. Biểu tượng cảnh báo y tế: ai cũng thấy (Q-66-12) — khớp FR-006.
4. Owner: BBA chưa hiểu câu hỏi (Q-66-11) → hỏi lại kèm ảnh.
5. Payment method sửa được hay chỉ hiển thị — chưa trả lời (Q-66-10).

---

## US-002 — Khối Identity

### Functional Requirements

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-013 *(sửa)* | Payment method là thông tin của hồ sơ trẻ, chỉ đọc trên tab Overview (chờ OQ-OVW-16); có ghi chú "Carried on every invoice for this child."; mỗi invoice của trẻ mang phương thức này để Finance lọc hàng loạt (Q-66-09). |
| FR-014 *(sửa)* | Danh mục payment method của Centre Singapore: GIRO, GIRO CDA, PayNow (Q-66-09); Centre Singapore không hiện phương thức của Malaysia. Danh mục của Malaysia chờ OQ-OVW-08. |
| FR-030 *(mới)* | Trẻ có cả tài khoản GIRO non-CDA và GIRO CDA thì Payment method hiện cả hai, ví dụ "GIRO · GIRO CDA"; invoice CDA và non-CDA của trẻ xuất riêng (Q-66-09). |

### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-038 *(mới)* | Ethan có tài khoản GIRO non-CDA và GIRO CDA | School Admin mở tab Overview | Payment method hiện "GIRO · GIRO CDA" với ghi chú "Carried on every invoice for this child." | FR-013; FR-030 |
| AC-039 *(mới)* | trẻ thuộc Centre Singapore | Finance xem danh mục payment method của trẻ | danh mục gồm GIRO, GIRO CDA, PayNow | FR-014 |

---

## US-004 — Sửa Identity có change record

### Functional Requirements

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-026 *(sửa)* | Khi tạo hoặc sửa hồ sơ trẻ: trùng **số giấy khai sinh hoặc số hộ chiếu** với trẻ khác (khoá định danh, Q-66-14) hiển thị cảnh báo trùng (chặn hay cho tiếp tục chờ OQ-OVW-17); trùng tên và ngày sinh hiển thị cảnh báo, không chặn. |

### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-040 *(mới)* | đã có trẻ với số giấy khai sinh "T2600011B" | School Admin lưu một trẻ khác cùng số giấy khai sinh | hệ thống hiện cảnh báo trùng và liên kết tới hồ sơ kia | FR-026 |

---

## Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Ưu tiên | Ghi chú |
|---|---|---|---|
| OQ-OVW-03 *(sửa)* | "Owner" trên header là primary contact hay người khác? | Trung bình | BBA chưa hiểu câu hỏi (Q-66-11) — hỏi lại kèm ảnh header |
| OQ-OVW-08 *(sửa)* | Danh mục payment method của Malaysia; nguồn khi sửa. | Cao | Singapore đã chốt GIRO, GIRO CDA, PayNow; thuộc hồ sơ trẻ (Q-66-09) |
| OQ-OVW-16 *(mới)* | Payment method trên Overview chỉ hiển thị hay sửa được; sửa thì module nào là nguồn chính? | Trung bình | Chưa phản hồi (Q-66-10) |
| OQ-OVW-17 *(mới)* | Trùng số giấy khai sinh / hộ chiếu: chặn tạo hay chỉ cảnh báo? | Cao | Q-66-14 mới có khoá định danh |
