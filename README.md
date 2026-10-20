# BA Docs Automation — khảo sát thô → URD → SRS → Wireframe → Word

Bộ skill cho **Claude Code** tự động đi từ tài liệu khảo sát (biên bản họp, email, ghi chú) tới bộ tài liệu BA hoàn chỉnh, không cần người can thiệp giữa chừng. Thiết kế để chạy trên **Claude Code bản web (cloud session)**; máy local chỉ để dựng và test.

```
inputs/<du-an>/ → brainstorm → write-urd → write-srs → ui-spec → wireframe → render-screens → SRS.docx → branch docs/<du-an> + PR
```

## Cách dùng nhanh

Không cần tự tạo thư mục hay commit — mọi thứ làm ngay trong đoạn chat.

1. Mở session cloud trên repo tại claude.ai/code.
2. **Đưa tài liệu vào chat**: dán text (biên bản họp, email, ghi chú), đính kèm file (`.docx`, `.pdf`, `.xlsx`, ảnh), hoặc gửi link tải. Kèm tên dự án:
   > Thêm tài liệu cho dự án **rma-moc-an**: *(dán nội dung / đính kèm file)*
3. Claude (skill `ba-intake`) tự:
   - chuyển text thành Markdown, lưu file vào `inputs/<du-an>/`, ghi nhật ký `_manifest.md`;
   - commit + push lên GitHub (branch `docs/<du-an>`);
   - nếu dự án đã có tài liệu: **giữ nguyên bản cũ** (bản mới lưu thành `__v2`, `__v3`…), lập bảng khác biệt cũ/mới trong `_changes/`, rồi **hỏi bạn**: merge thành bản tổng hợp, giữ cả hai, hay bạn tự mô tả khác biệt.
4. Gõ **"Làm SRS cho dự án `<du-an>`"** (hoặc gộp luôn: "Làm SRS cho dự án X" + dán/đính kèm tài liệu trong cùng tin nhắn).
5. Đợi Claude chạy xong → xem PR: `outputs/<du-an>/SRS.docx`, `ui/index.html`, danh sách **Open Questions** trong mô tả PR.
6. **Sau mỗi buổi khảo sát / demo** → lặp lại bước 2. Claude hỏi bạn một lần về khác biệt, chọn **"Merge + cập nhật SRS ngay"** → SRS được sửa đúng chỗ trong vài phút (0.3 → 0.3.1), màn hình cần sửa được đánh dấu chờ vẽ. Không vẽ lại, không xuất docx ở bước này.
7. **Khi cần gửi khách** → gõ **"Xuất bản tài liệu dự án `<du-an>`"**: chỉ vẽ lại các màn đang chờ, xuất SRS.docx, lên bản 0.4, mở PR.
8. Cần sửa → comment trực tiếp trên diff của PR, hoặc nhắn tiếp trong session ("Sửa FR-05: …").

Vẫn có thể thả file thẳng vào `inputs/<du-an>/` và commit thủ công như trước.

## Kết quả sinh ra (`outputs/<du-an>/`)

| File | Nội dung |
|---|---|
| `brainstorm.md` | Phân tích 7 phần (bối cảnh, mục tiêu, người dùng, phạm vi, quy trình, tích hợp, ràng buộc) + AS/OQ |
| `URD.md` | User story theo vai trò + acceptance criteria |
| `SRS.md` / `SRS.docx` | Đặc tả 9 mục: FR, NFR, tích hợp, Screen Inventory, user flow, ma trận truy vết, AS/OQ — docx có ảnh wireframe |
| `ui/flows.md` | Sitemap + user flow (Mermaid) + mô tả bố cục từng màn |
| `ui/screens/SCR-xx-<slug>.html` | Wireframe HTML tự chứa (tông xám, 1 màu nhấn) |
| `ui/png/*.png` | Ảnh từng màn, từng trạng thái; storefront có thêm bản mobile 390px |
| `ui/diagrams/*.png` | Sơ đồ Mermaid đã render |
| `ui/index.html` | Gallery toàn bộ màn hình |

## Cấu trúc repo

```
.claude/
  settings.json              quyền chạy sẵn (python, pandoc, mmdc, git, gh pr)
  skills/
    ba-intake/               nhận text/file/link từ chat → inputs/, giữ phiên bản, diff, push, hỏi merge
    srs-pipeline/            tạo mới bản 0.1 — chạy cả chuỗi, commit, mở PR, báo cáo
    srs-update/              cập nhật nhanh sau khảo sát/demo — sửa đúng phân hệ, 0.3 → 0.3.1, đánh dấu màn chờ vẽ
    srs-publish/             xuất bản khi gửi khách — vẽ màn đang chờ, docx, 0.3.x → 0.4, PR
    brainstorm/              phỏng vấn BA 7 phần, tự trả lời từ input
    write-urd/               URD + template-urd.md
    write-srs/               SRS tách phân hệ (srs/*.md) + template + checklist + scripts/{build_srs,split_srs,check_srs,to_docx}.py
    ui-spec/                 Screen Inventory → flows.md
    wireframe/               design-kit/ (tokens.css, components-*.html, patterns.md) + scripts/build_ui.py
    render-screens/          scripts/shot.py (Playwright) + scripts/render_mermaid.py (mermaid-cli)
CLAUDE.md                    luật chung: ngôn ngữ, tên file, mã định danh, git
setup/cloud-setup.sh         setup script cho cloud environment
templates/                   reference.docx (tuỳ chọn) — style Word công ty
inputs/_example/             bộ input mẫu: đổi trả hàng Magento 2 + duyệt trên Odoo
outputs/                     kết quả
```

## Thiết lập lần đầu

### Cloud (claude.ai/code)
1. Tạo repo GitHub **private**, push code lên.
2. Trên claude.ai/code: kết nối GitHub (cài Claude GitHub App cho repo).
3. Tạo / sửa cloud environment: dán nội dung `setup/cloud-setup.sh` vào **Setup script**; bật network access cho pip, npm, apt và domain tải Chromium của Playwright (xem comment trong file).
4. Chạy thử: mở session, gõ **"Làm SRS cho dự án _example"**.

### Local (Windows / macOS / Linux) — để dựng & test
Cần: Python 3.10+, Node.js 18+, pandoc, git (và `gh` nếu muốn mở PR từ máy).
```bash
pip install -r requirements.txt
```
```bash
python -m playwright install chromium
```
```bash
npm install -g @mermaid-js/mermaid-cli
```
Windows cài nhanh bằng winget: `winget install Python.Python.3.12 OpenJS.NodeJS.LTS JohnMacFarlane.Pandoc Git.Git GitHub.cli`.

## Chạy từng bước (khi cần)

| Muốn | Gõ trong Claude Code |
|---|---|
| Chỉ phân tích input | "Brainstorm dự án `<du-an>`" |
| Chỉ URD | "Viết URD cho `<du-an>`" |
| Vẽ lại một màn | "Vẽ lại SCR-03 của `<du-an>`, thêm cột Ngày giao" |
| Ghép SRS.md từ srs/ | `python .claude/skills/write-srs/scripts/build_srs.py <du-an>` |
| Tra mã nằm ở file nào | `python .claude/skills/write-srs/scripts/build_srs.py <du-an> --index` |
| Chuyển dự án cũ sang srs/ | `python .claude/skills/write-srs/scripts/split_srs.py <du-an> --modules "Phân hệ A=FR-01..FR-05; Phân hệ B=FR-06..FR-09"` |
| Xuất lại Word | `python .claude/skills/write-srs/scripts/to_docx.py <du-an>` |
| Kiểm tra SRS | `python .claude/skills/write-srs/scripts/check_srs.py <du-an> --final` |
| Chụp lại ảnh | `python .claude/skills/render-screens/scripts/shot.py <du-an> --only SCR-03` |

## Tuỳ biến
- **Template SRS công ty:** đặt `templates/template-srs-company.md` (giữ đủ 9 mục — xem `templates/README.md`).
- **Style Word:** `templates/reference.docx`.
- **Design kit:** sửa `.claude/skills/wireframe/design-kit/tokens.css` (đổi `--wf-accent` để đổi màu nhấn) và thêm markup mẫu vào `components-*.html`.

## Quy tắc quan trọng
- Skill nằm trong `.claude/skills/` của repo (cloud không đọc `~/.claude/skills/`), không đóng gói plugin.
- Skill **không hỏi lại**; thiếu thông tin → **Assumptions & Open Questions** (`AS-xx`, `OQ-xx`). Review kỹ mục này trước khi gửi khách.
- Không push thẳng `main` — mọi kết quả đi qua PR trên branch `docs/<du-an>`.

## Về sau
Tạo scheduled task trên cloud để tự chạy khi có thư mục mới trong `inputs/` (gõ `/schedule` trong Claude Code).
