# Quy ước chung — repo sinh tài liệu BA (URD → SRS → Wireframe → Word)

## Ngôn ngữ
- Tài liệu viết **tiếng Việt**, thuật ngữ kỹ thuật giữ **tiếng Anh** (API, endpoint, payload, status, workflow, SKU…).
- Văn phong BA: câu ngắn, khẳng định, đo lường được. Không viết "có thể", "nên" trong acceptance criteria.

## Thư mục
- Input luôn đọc từ `inputs/<du-an>/` (chỉ đọc, không sửa).
- Output luôn ghi vào `outputs/<du-an>/`.
- Tên file cố định:
  - `outputs/<du-an>/brainstorm.md`
  - `outputs/<du-an>/URD.md`
  - `outputs/<du-an>/SRS.md`, `outputs/<du-an>/SRS.docx`
  - `outputs/<du-an>/ui/flows.md`, `outputs/<du-an>/ui/index.html`
  - `outputs/<du-an>/ui/screens/SCR-xx-<slug>.html`
  - `outputs/<du-an>/ui/png/SCR-xx-<slug>.png` (biến thể: `SCR-xx-<slug>--<state>.png`, `SCR-xx-<slug>-mobile.png`)
  - `outputs/<du-an>/ui/diagrams/*.png` (Mermaid đã render)
- `<slug>`: chữ thường, không dấu, nối bằng `-` (vd. `SCR-03-chi-tiet-yeu-cau-doi-tra`).

## Mã định danh
| Loại | Mẫu | Ví dụ |
|---|---|---|
| User story (URD) | `US-xx` | US-01 |
| Yêu cầu chức năng | `FR-xx` | FR-07 |
| Yêu cầu phi chức năng | `NFR-xx` | NFR-02 |
| Màn hình | `SCR-xx` | SCR-04 |
| Giả định | `AS-xx` | AS-03 |
| Câu hỏi mở | `OQ-xx` | OQ-05 |

Số đánh 2 chữ số, tăng dần, **không tái sử dụng** mã đã xóa.

## Chế độ tự động
- Khi user yêu cầu "làm SRS / làm tài liệu / làm URD / làm wireframe cho dự án X" → dùng skill **`srs-pipeline`**.
- Các skill trong chuỗi **không dừng lại hỏi user**. Thiếu thông tin → tạo `AS-xx` (giả định đã chọn) + `OQ-xx` (câu hỏi cần khách hàng xác nhận) trong mục **"Assumptions & Open Questions"**, rồi làm tiếp.
- Skill `brainstorm` của repo này (`.claude/skills/brainstorm/`) là bản **tự trả lời từ input**, khác với các skill brainstorm phỏng vấn user ở nơi khác. Luôn dùng bản của repo.

## Công cụ
- Script viết bằng Python, chạy bằng `python` (Windows) hoặc `python3` (Linux cloud).
- Wireframe: chỉ dùng component trong `.claude/skills/wireframe/design-kit/`, font hệ thống, không ảnh/CDN/Google Fonts.

## Git
- Làm việc trên branch `docs/<du-an>`, commit theo từng bước của pipeline (`docs(<du-an>): brainstorm`, `docs(<du-an>): URD`…).
- Kết thúc bằng mở PR. **Không push thẳng `main`.**
