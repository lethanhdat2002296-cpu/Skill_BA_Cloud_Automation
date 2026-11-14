# Quy ước chung — repo sinh tài liệu BA (URD → UC → SRS → Backlog → Wireframe → Word → Drive)

## Ngôn ngữ
- Tài liệu viết **tiếng Việt**, thuật ngữ kỹ thuật giữ **tiếng Anh** (API, endpoint, payload, status, workflow, SKU…).
- Văn phong BA: câu ngắn, khẳng định, đo lường được. Không viết "có thể", "nên" trong acceptance criteria.

## Phạm vi dự án — chỉ làm trong ĐÚNG một dự án
1. Câu lệnh nhắc tới dự án → chạy `python tools/project.py find "<tên>"` lấy đúng slug. Không rõ (in "KHÔNG RÕ") → hỏi user chọn trong danh sách gợi ý; trong skill chạy tự động thì dừng, báo danh sách.
2. Sau đó chỉ đọc / sửa / grep trong `projects/<du-an>/`. **Không** Glob/Grep/Read ở `projects/` gốc hay dự án khác, không so sánh chéo dự án nếu user không yêu cầu.
3. Đọc `projects/<du-an>/PROJECT.md` (thẻ dự án) **trước** mọi tài liệu lớn. Thẻ sinh bằng `python tools/project.py card <du-an>`.
4. Mọi script nhận `<du-an>` (tên gần đúng cũng được) và chỉ làm trong dự án đó.
5. **Quy tắc riêng của dự án:** có `projects/<du-an>/project.json` → đọc nó và file `guide` nó trỏ tới (vd. BBA: `templates/HUONG-DAN-FSD.md`) trước khi làm. Quy tắc riêng **thắng** quy tắc chung (tài liệu chính, ngôn ngữ, sprint, định dạng Word, gợi ý thư mục Drive).

## Thư mục — nhiều dự án trong một repo, cấu trúc giống nhau trên Git và Drive
```
projects/                                      Drive: thư mục do user tạo (gắn link vào project.json › drive.root_url)
  <du-an>/
    PROJECT.md     thẻ dự án (sinh tự động + phần ghi chú viết tay)
    project.json   (tuỳ chọn) quy tắc riêng: tài liệu chính, sprint, định dạng Word, link Drive
    Document/
      Bien_Ban_Khao_Sat/  biên bản / tài liệu khảo sát (Markdown) — KHÔNG sửa/xoá/ghi đè; chỉ thêm qua ba-intake (__v2, __v3)
                          _manifest.md, _changes/, _extracted/, _tong-hop.md (bản hợp nhất — nguồn ưu tiên)
      URD/                URD.md, brainstorm.md
      SRS/                srs/*.md (nguồn, tách phân hệ) → SRS.md (sinh tự động)
      FSD/                FSD *.md — dự án chạy sprint: FSD/Sprint <n>/
      Use_Case/  Backlog/ UC.md · backlog.md
      Test_Case/          test-cases.md — dự án chạy sprint: Test_Case/Sprint <n>/
      doi-chieu-ma.md     mã gốc ↔ mã mới (khi nhập URD/FSD có sẵn)
    Diagram/
      Flow/               ảnh sơ đồ (srs-NN, flows-NN, uc-NN, swimlane-*) · swimlanes/*.json
      Wireframe/          flows.md, index.html, _pending.md, screens/SCR-xx-<slug>.html, png/SCR-xx-<slug>[--<state>][-mobile].png
    _drive.json    file đã đẩy + thư mục Drive đã dùng (drive-sync ghi)
    .output/       Word / CSV xuất ra — KHÔNG commit, chỉ đẩy lên Drive
```
- **Git chỉ lưu Markdown** trong `Document/` (+ ảnh / HTML trong `Diagram/`). File gốc của khách (.docx, .pdf, ảnh…) và `_goc/` bị `.gitignore` — bản gốc ở Drive.
- Dự án chạy theo sprint (`project.json` › `sprint.enabled`, `sprint.current`): tài liệu theo sprint nằm trong `<Loại>/Sprint <n>/`.
- Đường dẫn ảnh trong tài liệu tính từ thư mục của tài liệu: `Document/SRS/SRS.md` → `../../Diagram/Wireframe/png/…`, `../../Diagram/Flow/…`.
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
| Đưa **URD / FSD / SRS có sẵn** ("đây là FSD của dự án X") | `ba-intake` → `srs-pipeline` (bước `doc-import`: giữ nội dung, đối chiếu mã gốc, bỏ qua brainstorm/URD) | `ba-intake` → so khác biệt → `srs-update` |
| "Cập nhật SRS cho X", "sau khảo sát/demo" | `srs-pipeline` | `srs-update` (nhanh, không vẽ, không Word) |
| "Xuất bản / xuất docx / gửi khách" | `srs-pipeline` | `srs-publish` |
| "Viết use case" / "Làm backlog, xuất Jira" | `write-usecase` / `write-user-story` | như bên trái |
| "Viết test case", "file test cho QA" | — (cần SRS trước) | `write-testcase` — chỉ khi user yêu cầu |
| "Viết FSD" (dự án có `project.json` `main_doc: fsd`, vd. BBA) | theo `templates/HUONG-DAN-FSD.md` của dự án — không chạy chuỗi SRS | |
| Có file Word đầu ra mới (xuất bản, FSD xong, test case xong) / "đẩy X lên Drive", "lấy góp ý trên Drive" | `drive-sync` — **luôn Word (.docx)**, **mỗi lần hỏi user thư mục Drive đích** (thư mục do user tạo, dán link); không tự tạo / xoá / di chuyển trên Drive | |
| "Dự án X đang tới đâu?" | `python tools/project.py status <du-an>` — không mở tài liệu | |

## Chế độ tự động
- Chỉ hai chỗ được hỏi user: `ba-intake` (khi không chạy trong pipeline) ở bước xử lý khác biệt, và `drive-sync` hỏi thư mục Drive đích — mỗi chỗ gộp trong **một** lần hỏi.
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
