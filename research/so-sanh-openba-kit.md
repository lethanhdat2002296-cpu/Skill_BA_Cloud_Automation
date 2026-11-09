# So sánh bộ skill BA của repo này với OpenBA-Kit

> Ngày: 2026-11-09 · Nguồn: OpenBA-Kit (bản `main`, giấy phép MIT) — 56 skill, 19 rules, 47 template, 6 script.
> Mục đích: tìm điều đáng học để nâng cấp bộ skill của repo. File này không được nạp tự động (không tốn token mỗi phiên).

## 1. Hai cách thiết kế

| Tiêu chí | Repo này | OpenBA-Kit |
|---|---|---|
| Đơn vị làm việc | **Dự án** `projects/<du-an>/` (input → docs → ui → exports → Drive) | **Tính năng** `docs/{feature}/…` |
| Gọi skill | Câu tự nhiên → bảng "Chọn skill" trong CLAUDE.md; chuỗi tự động (`srs-pipeline`) | Lệnh `/tên` từng bước, người dùng tự xâu chuỗi |
| Tri thức đặt ở | `SKILL.md` + `template-*.md` + `references.md` của từng skill | `rules/` dùng chung (19 file) + `_templates/` (47 file) |
| Kiểm tra chất lượng | **Script**: `check_srs`, `check_uc`, `backlog_csv`, `build_ui`, `shot` (mã trùng, truy vết, ảnh, layout) | Checklist chữ trong skill; không có script kiểm tra tài liệu |
| Tự động | Không hỏi user (trừ `ba-intake`), thiếu → AS/OQ | `/brainstorm` phỏng vấn; `diagram-design` hỏi chọn style lần đầu |
| Mã định danh | Phẳng `FR-01`, `BR-01.1` trong FR | Phân cấp `FR-AUTH-LGN-001`, `BR-SEC-001`, `ERR-AUTH-401-01` |
| Đầu ra cho khách | Word (pandoc, nhúng ảnh), Google Doc/Sheet, wireframe PNG, sơ đồ Mermaid/swimlane PNG | Markdown, HTML/SVG sơ đồ, `preview.html` |
| Quản lý thay đổi | `ba-intake` (giữ bản cũ, diff, hỏi merge) → `srs-update` (patch) → `srs-publish` (minor) | `/cr` phân tích tác động 4 góc rồi sửa |
| Phạm vi | Vòng yêu cầu: brainstorm → URD → UC → SRS → backlog → UI → Word → Drive | Rộng hơn: + API (7), test (3), Jira/Confluence, doc-drift với code, user guide |
| Chi phí token cố định | 14 skill, mô tả ngắn | 56 skill, phần mô tả khoảng 3.800 ký tự mỗi phiên |

## 2. Điểm mạnh / yếu quan sát được ở OpenBA-Kit
- **Mạnh:** bộ quy chuẩn rõ ràng (BR dạng KHI–THÌ–TRỪ KHI, ma trận lỗi, ma trận trạng thái, RBAC, từ điển dữ liệu, bộ lọc từ mơ hồ, AC ≥ 3 kịch bản, RTM tới test case, CR 4 góc tác động); phủ cả giai đoạn test và bàn giao.
- **Yếu:**
  - Phần lớn skill khoảng 35 dòng và dùng chung một khuôn.
  - Nhiều template rỗng: `11-business-rules`, `12-error-matrix`, `42-test-checklist`, `43-test-cases` và `48-meeting-minutes` chỉ có khung "Mục 1/2/3".
  - Danh sách rules trong 55 SKILL.md bị dính ký tự `\n`.
  - `render_diagrams.py` chỉ vẽ đúng `sequenceDiagram` và `stateDiagram`. Mọi loại khác, kể cả flowchart, rơi vào hàm vẽ sequence nên ra sai.
  - Sơ đồ HTML tải Google Fonts.
  - Không có kiểm tra tự động nào cho tài liệu.

## 3. Đã học và áp dụng (lần nâng cấp này)

| Ý tưởng OpenBA (rule) | Áp dụng trong repo | Khác biệt so với bản gốc |
|---|---|---|
| Bộ lọc từ mơ hồ (16) | `tools/ba_lint.py` + cảnh báo trong `check_srs` (AC, BR, NFR của SRS; AC của URD), `backlog_csv`, `check_tc` | Tự động bằng script; bỏ qua chữ trong "ngoặc kép" (dữ liệu, thông báo) và từ dễ nhầm ("tồn kho an toàn", "trở nên") |
| AC ≥ 3 kịch bản: thành công / lỗi / biên (08) | `write-srs`: FR Must có AC thành công + lỗi + biên khi có ngưỡng; `check_srs` cảnh báo FR Must chưa có AC lỗi | Chỉ bắt buộc AC lỗi (đo được bằng script); biên khi có ngưỡng |
| Ma trận lỗi tổng hợp ERR (03, 11) | **SRS 8.2 Danh mục thông báo** sinh tự động từ `hiện lỗi "…"` trong AC; `check_srs` cảnh báo `hiện lỗi` chưa có nguyên văn | Không đặt mã ERR viết tay (tránh trùng / lệch); một nguồn duy nhất là AC |
| BR dạng WHEN–THEN–UNLESS (02) | `BR-xx.n: KHI … THÌ … (TRỪ KHI …)` trong template FR | Giữ mã BR gắn với FR |
| Ma trận chuyển trạng thái (12) | SRS `3.0 Mô hình trạng thái`: `stateDiagram-v2` + bảng nguồn / sự kiện / điều kiện / đích / ai / tác động / FR | — |
| Ma trận phân quyền RBAC (17) | SRS 2.2: bảng đối tượng × vai trò (Tạo / Xem / Sửa / Duyệt, Của mình / Nhóm mình) | Hợp với nhóm quyền + record rule của Odoo |
| Từ điển dữ liệu (09) | SRS `5.4 Từ điển dữ liệu`: chỉ model / trường thêm mới | Không liệt kê model chuẩn của nền tảng |
| IEEE 830 — ràng buộc (05) | SRS 2.3 thêm "Ràng buộc" (phiên bản/edition, hosting, trình duyệt, pháp lý) | Không đổi số mục (giữ 9 mục) |
| RTM tới test case (14) + `/test-cases` | Skill mới **`write-testcase`** + `check_tc.py`: mỗi AC ≥ 1 TC, ma trận phủ FR → AC → TC, CSV cho QA (cột Trạng thái / Kết quả thực tế), đẩy lên Drive thành Sheet | OpenBA chỉ có template rỗng; ở đây có script kiểm tra trỏ AC/BR sai, AC chưa phủ |
| Phân tích tác động CR 4 góc (15) | `ba-intake` Bước 5: bảng Tác động (tài liệu / kỹ thuật / kiểm thử / kế hoạch) trước khi hỏi user merge | Tra bằng grep theo mã, không đọc cả tài liệu |
| `/gap` — tìm lỗ hổng | `write-srs/checklist.md`: rà huỷ giữa chừng, timeout, lỗi tích hợp, sai quyền, dữ liệu biên, thao tác đồng thời | — |
| `/meet` — biên bản họp | `ba-intake`: input là biên bản họp → thêm "Quyết định đã chốt" và "Việc cần làm (người, hạn)" | — |

## 4. Không áp dụng (và lý do)

| Ý tưởng | Lý do không áp dụng |
|---|---|
| Mã phân cấp `FR-AUTH-LGN-001` | Dự án đang chạy dùng `FR-01`; đổi giữa chừng phá truy vết, docx, Drive, backlog |
| Thư mục `rules/` dùng chung | Claude phải mở thêm file mỗi lần → tốn token; nội dung đã nằm trong template + script |
| Frontmatter YAML + `/kg` knowledge graph | `PROJECT.md` + `project.py status` + `build_srs --index` đã cho tra cứu nhanh hơn |
| `diagram-design` / `render-diagrams` (HTML/SVG) | Tải Google Fonts, hỏi user chọn style, `render_diagrams.py` chỉ vẽ đúng sequence/state; repo đã render Mermaid + swimlane ra PNG cho Word |
| `/preview` trang HTML tổng hợp | Google Drive (thư mục dự án) + `ui/index.html` đã thay vai trò này |
| `/brainstorm` dạng phỏng vấn | Repo chọn chế độ tự động (thiếu → AS/OQ); hỏi user chỉ ở `ba-intake` |
| Nhóm API (7 skill), `/playwright-gen`, `/confluence`, `/doc-drift`, `/code-to-srs` | Chưa có nhu cầu trong dự án Odoo cấu hình hiện tại; cân nhắc khi có dự án tích hợp API hoặc có code để đối chiếu |

## 5. Gợi ý bước sau
1. Áp dụng chuẩn mới cho dự án đang chạy: "Cập nhật SRS `odoo-mua-hang` theo chuẩn mới". Phạm vi gồm:
   - Bổ sung AC lỗi cho FR-13, FR-14, FR-27.
   - Ghi nguyên văn thông báo của FR-11 AC4.
   - Thêm ma trận phân quyền, mô hình trạng thái và từ điển dữ liệu.
   - Tách `docs/srs/` để mục 8.2 được sinh tự động.
2. "Viết test case cho `odoo-mua-hang`", sau khi khách duyệt SRS.
3. Khi có dự án tích hợp API: viết skill `write-api-spec` dựa trên rule 10 (API contract) của OpenBA, kèm script kiểm tra.
