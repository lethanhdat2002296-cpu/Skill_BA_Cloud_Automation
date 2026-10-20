---
name: brainstorm
description: Phân tích tài liệu khảo sát thô trong inputs/<du-an>/ theo khung phỏng vấn BA 7 phần (bối cảnh, mục tiêu, người dùng, phạm vi, quy trình, tích hợp, ràng buộc) nhưng TỰ TRẢ LỜI từ input, không hỏi user; phần thiếu dữ liệu ghi thành Open Question. Dùng làm bước đầu của srs-pipeline, hoặc khi user muốn "phân tích input", "tổng hợp khảo sát", "brainstorm yêu cầu từ biên bản họp" trước khi viết URD/SRS. Keywords - brainstorm, requirements elicitation, discovery, BA interview, meeting notes analysis, gap analysis, open questions. Output outputs/<du-an>/brainstorm.md.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# brainstorm — phỏng vấn BA tự trả lời

Mục tiêu: biến tài liệu khảo sát rời rạc thành một bức tranh có cấu trúc, **chỉ ra rõ cái gì đã biết, cái gì đang giả định, cái gì chưa biết**. Không hỏi user.

## Input
- Toàn bộ file trong `inputs/<du-an>/` (đã đọc ở bước trước của pipeline; nếu chạy riêng thì đọc hết).

## Cách làm

1. Với mỗi phần trong 7 phần dưới đây, tự đặt các câu hỏi phỏng vấn gợi ý, rồi trả lời **chỉ bằng dữ kiện trong input**.
2. Mỗi câu trả lời ghi nguồn: `(nguồn: bien-ban-hop-01.md)`. Nhiều nguồn mâu thuẫn → ghi cả hai + tạo OQ.
3. Câu hỏi không có dữ kiện:
   - Nếu có phương án mặc định hợp lý theo thông lệ ngành (Magento/Odoo/e-commerce) → ghi `AS-xx` với phương án đó **và** `OQ-xx` để xác nhận.
   - Nếu không có phương án hợp lý → chỉ ghi `OQ-xx`.
4. Không sáng tác tính năng ngoài input. Ý tưởng "nên có" thì đưa vào mục **Đề xuất của BA** (đánh dấu rõ là đề xuất, chưa phải yêu cầu).

## 7 phần và câu hỏi gợi ý

1. **Bối cảnh & vấn đề** — Doanh nghiệp là ai, bán gì, kênh nào? Vấn đề hiện tại là gì, ai chịu ảnh hưởng, hậu quả đo được (thời gian, chi phí, khiếu nại)? Vì sao làm bây giờ?
2. **Mục tiêu kinh doanh** — Thành công trông như thế nào? KPI nào, mục tiêu số bao nhiêu, đo khi nào? Deadline / mốc go-live?
3. **Người dùng & vai trò** — Có những nhóm người dùng nào (khách hàng, CSKH, kho, kế toán, quản lý, admin)? Mỗi nhóm làm gì, trên hệ thống nào (storefront / backend), quyền gì? Tần suất sử dụng?
4. **Phạm vi (in / out)** — Tính năng nào chắc chắn có trong đợt này? Cái gì loại trừ rõ ràng? Cái gì để giai đoạn sau?
5. **Quy trình nghiệp vụ: hiện tại vs mong muốn** — AS-IS từng bước (ai, làm gì, công cụ gì, mất bao lâu). TO-BE từng bước. Điểm thay đổi, ngoại lệ (huỷ, từ chối, quá hạn, hoàn tiền một phần).
6. **Tích hợp & dữ liệu** — Hệ thống nào tham gia (Magento 2, Odoo, cổng thanh toán, đơn vị vận chuyển, email/SMS)? Chiều đồng bộ, tần suất, realtime hay batch? Đối tượng dữ liệu chính và trường quan trọng? Nguồn sự thật (source of truth) của từng đối tượng?
7. **Ràng buộc & rủi ro** — Pháp lý (chính sách đổi trả, hoá đơn, dữ liệu cá nhân), kỹ thuật (version, hosting, module có sẵn), ngân sách, thời gian, hiệu năng, bảo mật. Rủi ro và cách giảm thiểu.

## Output: `outputs/<du-an>/brainstorm.md`

```markdown
# Brainstorm — <Tên dự án>

> Nguồn đã đọc: <danh sách file>. Ngày tạo: <YYYY-MM-DD>.

## 1. Bối cảnh & vấn đề
**Đã biết**
- … (nguồn: …)
**Giả định**
- AS-01: … → xác nhận ở OQ-01
**Chưa biết**
- OQ-02: …

## 2. Mục tiêu kinh doanh
… (cùng cấu trúc Đã biết / Giả định / Chưa biết)

## 3. Người dùng & vai trò
| Vai trò | Mô tả | Hệ thống | Việc chính | Nguồn |
|---|---|---|---|---|

## 4. Phạm vi
| In scope | Out of scope | Giai đoạn sau |
|---|---|---|

## 5. Quy trình nghiệp vụ
### 5.1 AS-IS
1. …
### 5.2 TO-BE
1. …
### 5.3 Ngoại lệ & nhánh rẽ
- …

## 6. Tích hợp & dữ liệu
| Hệ thống | Vai trò | Dữ liệu trao đổi | Chiều | Tần suất | Nguồn |
|---|---|---|---|---|---|

## 7. Ràng buộc & rủi ro
| Loại | Nội dung | Mức độ | Giảm thiểu |
|---|---|---|---|

## Đề xuất của BA (chưa phải yêu cầu)
- …

## Assumptions & Open Questions
| Mã | Nội dung | Loại (AS/OQ) | Liên quan |
|---|---|---|---|
```

## Quy tắc
- Đánh mã `AS-xx`, `OQ-xx` liên tục từ 01; các bước sau (URD, SRS) **kế thừa** và đánh tiếp, không đánh lại từ đầu.
- Mục nào hoàn toàn trống dữ liệu vẫn phải có, kèm ít nhất một `OQ-xx`.
- Độ dài mục tiêu: 1–3 trang. Ngắn gọn, dạng bảng/gạch đầu dòng.
