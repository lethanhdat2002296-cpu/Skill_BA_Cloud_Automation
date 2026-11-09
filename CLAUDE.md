# Quy ước chung — repo sinh tài liệu BA (URD → UC → SRS → Backlog → Wireframe → Word → Drive)

## Ngôn ngữ
- Tài liệu viết **tiếng Việt**, thuật ngữ kỹ thuật giữ **tiếng Anh** (API, endpoint, payload, status, workflow, SKU…).
- Văn phong BA: câu ngắn, khẳng định, đo lường được. Không viết "có thể", "nên" trong acceptance criteria.

## Phạm vi dự án — chỉ làm trong ĐÚNG một dự án
1. Câu lệnh nhắc tới dự án → chạy `python tools/project.py find "<tên>"` lấy đúng slug. Không rõ (in "KHÔNG RÕ") → hỏi user chọn trong danh sách gợi ý; trong skill chạy tự động thì dừng, báo danh sách.
2. Sau đó chỉ đọc / sửa / grep trong `projects/<du-an>/`. **Không** Glob/Grep/Read ở `projects/` gốc hay dự án khác, không so sánh chéo dự án nếu user không yêu cầu.
3. Đọc `projects/<du-an>/PROJECT.md` (thẻ dự án) **trước** mọi tài liệu lớn. Thẻ sinh bằng `python tools/project.py card <du-an>`.
4. Mọi script nhận `<du-an>` (tên gần đúng cũng được) và chỉ làm trong dự án đó.

## Thư mục — giống hệt trên git và Google Drive
```
projects/<du-an>/                    Drive: "BA Projects/<du-an>/"
  PROJECT.md   thẻ dự án (sinh tự động + phần ghi chú viết tay)
  input/       tài liệu khảo sát gốc — KHÔNG sửa/xoá/ghi đè; chỉ thêm qua ba-intake (bản mới: __v2, __v3)
               _manifest.md, _changes/, _extracted/, _tong-hop.md (bản hợp nhất — nguồn ưu tiên)
  docs/        brainstorm.md, URD.md, UC.md, srs/*.md (nguồn SRS, tách phân hệ) → SRS.md (sinh tự động), backlog.md, test-cases.md
  diagrams/    ảnh sơ đồ (srs-NN, flows-NN, uc-NN, swimlane-*) · swimlanes/*.json (nguồn swimlane)
  ui/          flows.md, index.html, _pending.md, screens/SCR-xx-<slug>.html, png/SCR-xx-<slug>[--<state>][-mobile].png
  exports/     SRS.docx, URD.docx, UC.docx, backlog.csv, test-cases.csv — sinh ra, không sửa tay
  _drive.json  ID/link Drive (drive-sync ghi)
```
- Đường dẫn ảnh trong `docs/*.md` tính từ `docs/`: `../ui/png/…`, `../diagrams/…`.
- Mọi script lấy đường dẫn từ `tools/ba_paths.py` — không tự ghép `projects/...`.
- `<slug>`: chữ thường, không dấu, nối bằng `-`. Dự án mới: `python tools/project.py new <du-an>`.

## Mã định danh
| Loại | Mẫu | Loại | Mẫu |
|---|---|---|---|
| User story | `US-xx` | Story tách nhỏ | `US-xx.n` |
| Epic | `EP-xx` | Use case | `UC-xx` |
| Yêu cầu chức năng | `FR-xx` | Phi chức năng | `NFR-xx` |
| Màn hình | `SCR-xx` | Giả định / Câu hỏi mở | `AS-xx` / `OQ-xx` |
| Quy tắc nghiệp vụ | `BR-<số FR>.n` (trong FR) | Test case | `TC-xxx` (3 chữ số) |

Số đánh 2 chữ số, tăng dần, **không tái sử dụng** mã đã xóa.

## Chọn skill
| User nói / làm | Chưa có SRS | Đã có SRS |
|---|---|---|
| Dán text, đính kèm file/ảnh, gửi link; "thêm/cập nhật thông tin dự án X" | `ba-intake` | `ba-intake` → hỏi user → `srs-update` |
| "Làm SRS / làm tài liệu cho X" | `srs-pipeline` (bản 0.1) | `srs-update` |
| "Cập nhật SRS cho X", "sau khảo sát/demo" | `srs-pipeline` | `srs-update` (nhanh, không vẽ, không Word) |
| "Xuất bản / xuất docx / gửi khách" | `srs-pipeline` | `srs-publish` |
| "Viết use case" / "Làm backlog, xuất Jira" | `write-usecase` / `write-user-story` | như bên trái |
| "Viết test case", "file test cho QA" | — (cần SRS trước) | `write-testcase` — chỉ khi user yêu cầu |
| "Đẩy X lên Drive", "lấy góp ý trên Drive", "sửa trên Doc" | `drive-sync` — chỉ khi user yêu cầu | |
| "Dự án X đang tới đâu?" | `python tools/project.py status <du-an>` — không mở tài liệu | |

## Chế độ tự động
- Chỉ `ba-intake` (khi không chạy trong pipeline) được hỏi user — chỉ ở bước xử lý khác biệt, gộp trong **một** lần hỏi.
- Các skill khác **không dừng hỏi**: thiếu thông tin → `AS-xx` + `OQ-xx` trong "Assumptions & Open Questions", làm tiếp.
- `brainstorm` của repo này tự trả lời từ input (khác skill brainstorm phỏng vấn ở nơi khác) — luôn dùng bản của repo; chỉ viết ở bản 0.1.

## Tiết kiệm token
- Hỏi trạng thái → `project.py status`; cần mã nào → `build_srs.py <du-an> --index` hoặc `grep -n "^#### FR-09"`, rồi `Read` có `offset/limit`. Không Read cả SRS/URD/UC khi chỉ cần một mục.
- Sửa bằng `Edit` đúng đoạn; không viết lại cả file.
- Không mở ảnh PNG trừ khi đang review đúng màn đó (`shot.py` chỉ liệt kê ảnh cần xem).
- Script in 1 dòng tổng kết; chi tiết ghi file (vd. `.tmp/drive/plan.json`) — chỉ mở khi cần.
- Công cụ Drive: không đọc cả Doc (`read_file_content`) nếu chỉ cần link/metadata; dùng `_drive.json`.

## Công cụ
- Script Python, chạy bằng `python` (Windows) hoặc `python3` (Linux cloud).
- Wireframe: chỉ dùng component trong `.claude/skills/wireframe/design-kit/`, font hệ thống, không ảnh/CDN/Google Fonts.

## Git
- Branch `docs/<du-an>` (cloud: branch của session). Commit theo bước: `input(<du-an>): …`, `docs(<du-an>): URD`, `docs(<du-an>): v0.3.1 — …`.
- Phiên bản: `srs-pipeline` 0.1 · `srs-update` tăng patch (0.3 → 0.3.1) · `srs-publish` tăng minor (0.3.x → 0.4).
- Kết thúc bằng mở PR. **Không push thẳng `main`.**
