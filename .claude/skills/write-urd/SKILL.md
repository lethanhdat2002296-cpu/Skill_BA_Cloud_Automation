---
name: write-urd
description: Viết URD (User Requirements Document) theo vai trò người dùng, dạng user story + acceptance criteria (Given/When/Then), từ brainstorm.md và input của dự án. Dùng sau bước brainstorm trong srs-pipeline, hoặc khi user yêu cầu "viết URD", "viết user story", "liệt kê yêu cầu người dùng", "user requirements". Keywords - URD, user requirements, user stories, acceptance criteria, Given When Then, personas, roles, MoSCoW priority. Output outputs/<du-an>/URD.md theo template-urd.md. Không hỏi user; thiếu thông tin thì ghi Assumptions & Open Questions.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# write-urd — User Requirements

## Input
- `outputs/<du-an>/brainstorm.md` (bắt buộc — chưa có thì chạy skill `brainstorm` trước).
- `inputs/<du-an>/` để tra lại chi tiết.

## Cách làm

1. Đọc `template-urd.md` trong thư mục skill này. Giữ nguyên cấu trúc mục, thay toàn bộ phần `{{...}}`.
2. Lấy danh sách vai trò từ mục 3 của brainstorm. Mỗi vai trò một mục con.
3. Với mỗi vai trò, viết user story cho **mọi** hoạt động trong phạm vi (mục 4 + quy trình TO-BE mục 5 của brainstorm):
   - Mẫu: **Là** <vai trò>, **tôi muốn** <hành động>, **để** <giá trị kinh doanh>.
   - Mã `US-xx` liên tục toàn tài liệu (không đánh lại theo vai trò).
   - Độ ưu tiên MoSCoW: `Must` / `Should` / `Could` / `Won't (lần này)`.
   - Nguồn: tên file input hoặc `AS-xx`.
4. Mỗi user story có **2–5 acceptance criteria** dạng Given/When/Then, cụ thể, kiểm thử được:
   - Có ít nhất một tiêu chí cho luồng chính và một cho ngoại lệ (dữ liệu sai, quá hạn, không có quyền…) nếu có ý nghĩa.
   - Không dùng từ mơ hồ ("nhanh", "dễ dùng", "phù hợp") — thay bằng ngưỡng cụ thể; nếu không có ngưỡng trong input → dùng giá trị đề xuất + `AS-xx`.
5. Ngoại lệ trong quy trình (mục 5.3 brainstorm) phải được phủ bởi ít nhất một user story hoặc acceptance criterion.
6. Kế thừa `AS-xx`/`OQ-xx` từ brainstorm, đánh tiếp số mới nếu phát sinh. Mục cuối URD liệt kê **toàn bộ** AS/OQ (cũ + mới).

## Kiểm tra trước khi lưu
- [ ] Mọi vai trò trong brainstorm đều có ít nhất 1 user story (hoặc ghi rõ "không tương tác hệ thống").
- [ ] Mọi bước TO-BE có user story tương ứng.
- [ ] Không còn `{{` trong file.
- [ ] Mã US không trùng, không nhảy cóc.

## Output
`outputs/<du-an>/URD.md`
