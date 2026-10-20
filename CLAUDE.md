# Quy ước chung — repo sinh tài liệu BA (URD → SRS → Wireframe → Word)

## Ngôn ngữ
- Tài liệu viết **tiếng Việt**, thuật ngữ kỹ thuật giữ **tiếng Anh** (API, endpoint, payload, status, workflow, SKU…).
- Văn phong BA: câu ngắn, khẳng định, đo lường được. Không viết "có thể", "nên" trong acceptance criteria.

## Thư mục
- Input luôn đọc từ `inputs/<du-an>/`. **Không sửa, không xoá, không ghi đè** file trong đó — chỉ thêm file mới hoặc phiên bản `__vN` qua skill `ba-intake`.
- File hệ thống trong `inputs/<du-an>/` (bắt đầu bằng `_`): `_manifest.md` (nhật ký nạp), `_changes/` (khác biệt mỗi lần cập nhật), `_extracted/` (text trích từ docx/pdf), `_tong-hop.md` (bản yêu cầu hợp nhất — nguồn ưu tiên).
- Output luôn ghi vào `outputs/<du-an>/`.
- Tên file cố định:
  - `outputs/<du-an>/brainstorm.md`
  - `outputs/<du-an>/URD.md`
  - `outputs/<du-an>/srs/*.md` — **nguồn của SRS, tách theo phân hệ** (`00-dau-trang.md`, `01-…`, `03-NN-<phan-he>.md`, … `09-gia-dinh-cau-hoi.md`). Sửa SRS = sửa ở đây.
  - `outputs/<du-an>/SRS.md` — **sinh tự động** bởi `build_srs.py` (không sửa tay); `outputs/<du-an>/SRS.docx`
  - `outputs/<du-an>/ui/_pending.md` — màn hình chờ vẽ lại (srs-update ghi, srs-publish xử lý)
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

## Chọn skill
| User nói / làm | Dự án chưa có SRS | Dự án đã có SRS |
|---|---|---|
| Dán text, đính kèm file/ảnh, gửi link; "thêm/cập nhật thông tin dự án X" | `ba-intake` | `ba-intake` → hỏi user → `srs-update` |
| "Làm SRS / làm tài liệu cho X" | `srs-pipeline` (tạo mới v0.1) | `srs-update` |
| "Cập nhật SRS cho X", "cập nhật sau khảo sát/demo" | `srs-pipeline` | `srs-update` (nhanh, không vẽ, không docx) |
| "Xuất bản / xuất docx / gửi khách / phát hành" | `srs-pipeline` | `srs-publish` (vẽ màn đang chờ, docx, PR) |

## Chế độ tự động
- Chỉ `ba-intake` (khi không chạy trong pipeline) được hỏi user — và chỉ ở bước xử lý khác biệt cũ/mới, gộp trong **một** lần hỏi.
- Cập nhật = **sửa đúng chỗ**: tra `build_srs.py --index` để biết mã nằm ở file nào, `Edit` đúng đoạn; không đọc/viết lại cả tài liệu. `brainstorm.md` chỉ viết ở bản 0.1.
- Các skill trong chuỗi **không dừng lại hỏi user**. Thiếu thông tin → tạo `AS-xx` (giả định đã chọn) + `OQ-xx` (câu hỏi cần khách hàng xác nhận) trong mục **"Assumptions & Open Questions"**, rồi làm tiếp.
- Skill `brainstorm` của repo này (`.claude/skills/brainstorm/`) là bản **tự trả lời từ input**, khác với các skill brainstorm phỏng vấn user ở nơi khác. Luôn dùng bản của repo.

## Công cụ
- Script viết bằng Python, chạy bằng `python` (Windows) hoặc `python3` (Linux cloud).
- Wireframe: chỉ dùng component trong `.claude/skills/wireframe/design-kit/`, font hệ thống, không ảnh/CDN/Google Fonts.

## Git
- Làm việc trên branch `docs/<du-an>` (cả input lẫn output), commit theo từng bước (`input(<du-an>): …`, `docs(<du-an>): brainstorm`, `docs(<du-an>): v0.3.1 — …`).
- Phiên bản: `srs-pipeline` 0.1 · `srs-update` tăng patch (0.3 → 0.3.1) · `srs-publish` tăng minor (0.3.x → 0.4).
- Kết thúc bằng mở PR. **Không push thẳng `main`.**
