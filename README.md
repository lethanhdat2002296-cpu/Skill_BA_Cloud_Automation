# BA Docs Automation — khảo sát thô → URD → SRS → Wireframe → Word

Bộ skill cho **Claude Code** tự động đi từ tài liệu khảo sát (biên bản họp, email, ghi chú) tới bộ tài liệu BA hoàn chỉnh, không cần người can thiệp giữa chừng. Thiết kế để chạy trên **Claude Code bản web (cloud session)**; máy local chỉ để dựng và test.

```
projects/<du-an>/Document/Bien_Ban_Khao_Sat/ → brainstorm → write-urd → write-srs → ui-spec → wireframe → render-screens → SRS.docx → branch docs/<du-an> + PR
```

## Cách dùng nhanh

Không cần tự tạo thư mục hay commit — mọi thứ làm ngay trong đoạn chat.

1. Mở session cloud trên repo tại claude.ai/code.
2. **Đưa tài liệu vào chat**: dán text (biên bản họp, email, ghi chú), đính kèm file (`.docx`, `.pdf`, `.xlsx`, ảnh), hoặc gửi link tải. Kèm tên dự án:
   > Thêm tài liệu cho dự án **rma-moc-an**: *(dán nội dung / đính kèm file)*
3. Claude (skill `ba-intake`) tự:
   - chuyển text thành Markdown, lưu file vào `projects/<du-an>/Document/Bien_Ban_Khao_Sat/`, ghi nhật ký `_manifest.md`;
   - commit + push lên GitHub (branch `docs/<du-an>`);
   - nếu dự án đã có tài liệu: **giữ nguyên bản cũ** (bản mới lưu thành `__v2`, `__v3`…), lập bảng khác biệt cũ/mới trong `_changes/`, rồi **hỏi bạn**: merge thành bản tổng hợp, giữ cả hai, hay bạn tự mô tả khác biệt.
4. Gõ **"Làm SRS cho dự án `<du-an>`"** (hoặc gộp luôn: "Làm SRS cho dự án X" + dán/đính kèm tài liệu trong cùng tin nhắn).
   - **Đã có URD / FSD / SRS** (của khách hoặc nhóm khác)? Đính kèm và nói rõ loại: *"Đây là FSD của dự án X, làm SRS"*. Claude nhập tài liệu đó thay vì phân tích lại từ đầu: giữ nguyên ý, đặt mã của repo, lập `Document/doi-chieu-ma.md` (mã gốc ↔ mã mới, script kiểm không sót yêu cầu), chỗ thiếu thành Open Questions, rồi chạy tiếp use case → backlog → wireframe → Word.
5. Đợi Claude chạy xong → Claude hỏi thư mục Drive để đẩy file Word; xem PR, `Diagram/Wireframe/index.html`, danh sách **Open Questions** trong mô tả PR.
6. **Sau mỗi buổi khảo sát / demo** → lặp lại bước 2. Claude hỏi bạn một lần về khác biệt, chọn **"Merge + cập nhật SRS ngay"** → SRS được sửa đúng chỗ trong vài phút (0.3 → 0.3.1), màn hình cần sửa được đánh dấu chờ vẽ. Không vẽ lại, không xuất docx ở bước này.
7. **Khi cần gửi khách** → gõ **"Xuất bản tài liệu dự án `<du-an>`"**: chỉ vẽ lại các màn đang chờ, xuất SRS.docx, lên bản 0.4, mở PR.
8. Cần sửa → comment trực tiếp trên diff của PR, hoặc nhắn tiếp trong session ("Sửa FR-05: …").

Vẫn có thể thả file thẳng vào `projects/<du-an>/Document/Bien_Ban_Khao_Sat/` và commit thủ công như trước.

## Kết quả sinh ra (`projects/<du-an>/`)

| File | Nội dung |
|---|---|
| `Document/Bien_Ban_Khao_Sat/*.md` | Biên bản / tài liệu khảo sát (Markdown), lịch sử nạp, khác biệt cũ ↔ mới |
| `Document/URD/URD.md` (+ `brainstorm.md`) | Phân tích 7 phần; user story theo vai trò + acceptance criteria |
| `Document/SRS/SRS.md` | Đặc tả 9 mục: FR, NFR, tích hợp, Screen Inventory, user flow, ma trận truy vết, AS/OQ |
| `Document/FSD/[Sprint <n>/]*.md` | FSD (dự án lấy FSD làm tài liệu chính, vd. BBA) |
| `Document/Use_Case/UC.md`, `Document/Backlog/backlog.md` | Use case fully-dressed; backlog epic / story / story point |
| `Document/Test_Case/[Sprint <n>/]test-cases.md` | Test case + ma trận phủ AC |
| `Diagram/Flow/*.png` | Sơ đồ Mermaid, swimlane, use case đã render |
| `Diagram/Wireframe/` | `flows.md`, `screens/SCR-xx-<slug>.html`, `png/*.png`, gallery `index.html` |
| `.output/*.docx`, `*.csv` | File Word / CSV xuất ra — không commit, đẩy lên Drive (mỗi lần hỏi thư mục) |

## Cấu trúc repo

```
.claude/
  settings.json              quyền chạy sẵn (python, pandoc, mmdc, git, gh pr)
  skills/
    ba-intake/               nhận text/file/link từ chat → projects/<du-an>/Document/Bien_Ban_Khao_Sat/, giữ phiên bản, diff, push, hỏi merge
    srs-pipeline/            tạo mới bản 0.1 — chạy cả chuỗi, commit, mở PR, báo cáo
    srs-update/              cập nhật nhanh sau khảo sát/demo — sửa đúng phân hệ, 0.3 → 0.3.1, đánh dấu màn chờ vẽ
    srs-publish/             xuất bản khi gửi khách — vẽ màn đang chờ, docx, 0.3.x → 0.4, PR
    doc-import/              nhập URD / FSD / SRS có sẵn: dàn ý (import_doc.py), giữ nội dung, bảng đối chiếu mã gốc ↔ mới (check_import.py)
    brainstorm/              phỏng vấn BA 7 phần, tự trả lời từ input
    write-urd/               URD + template-urd.md
    write-usecase/           Use Case fully-dressed (UC-xx) + sơ đồ use case + scripts/check_uc.py (ma trận UC ↔ US ↔ FR)
    write-user-story/        Product backlog: epic, tách story, story point, release + scripts/backlog_csv.py (CSV import Jira)
    write-testcase/          Test case từ AC của SRS (ngoại lệ, biên, trạng thái, phân quyền, NFR) + scripts/check_tc.py (ma trận phủ AC, CSV cho QA)
    drive-sync/              đẩy file Word lên Drive — mỗi lần hỏi thư mục đích (thư mục do user tạo); đọc góp ý
    write-srs/               SRS tách phân hệ (srs/*.md) + template + checklist + scripts/{build_srs,split_srs,check_srs,to_docx}.py
    ui-spec/                 Screen Inventory → flows.md
    wireframe/               design-kit/ (tokens.css, components-*.html, patterns.md) + scripts/build_ui.py
    render-screens/          scripts/shot.py (Playwright) + scripts/render_mermaid.py (mermaid-cli)
CLAUDE.md                    luật chung: phạm vi dự án, thư mục, mã định danh, tiết kiệm token, git
tools/
  ba_paths.py                đường dẫn chuẩn của một dự án (mọi script dùng)
  project.py                 list · find · status · card · new — điểm vào theo dự án
  ba_lint.py                 kiểm câu chữ dùng chung: từ mơ hồ, AC ngoại lệ, thông báo nguyên văn
  docx_style.py              định dạng Word theo project.json của dự án (font, cỡ, giãn dòng, thụt, kẻ bảng, khổ A4)
setup/cloud-setup.sh         setup script cho cloud environment
research/                    ghi chú nghiên cứu (vd. so sánh với OpenBA-Kit) — không nạp tự động
templates/                   reference.docx (tuỳ chọn) — style Word công ty
projects/
  _example/                  bộ input mẫu (Document/Bien_Ban_Khao_Sat/): đổi trả hàng Magento 2 + duyệt trên Odoo
  <du-an>/                   mỗi dự án một thư mục; Drive: thư mục do user tạo, cùng cấu trúc
    PROJECT.md               thẻ dự án: phiên bản, số mã, OQ mở, link Drive, bản đồ file — đọc đầu tiên
    project.json             (tuỳ chọn) quy tắc riêng: tài liệu chính, sprint, định dạng Word, link Drive
    Document/                Bien_Ban_Khao_Sat/ · URD/ · SRS/ · FSD/ · Use_Case/ · Backlog/ · Test_Case/ (+ Sprint <n>/)
    Diagram/                 Flow/ (sơ đồ + swimlanes/*.json) · Wireframe/ (flows.md, screens, png, index.html)
    .output/                 Word / CSV xuất ra (không commit)
    _drive.json              file đã đẩy + thư mục Drive đã dùng
```

## Làm việc theo dự án và tiết kiệm token
- Mỗi câu lệnh nhắc **tên dự án** (gần đúng cũng được: "odoo" → `odoo-mua-hang`). Claude chỉ làm trong `projects/<du-an>/`, không đọc dự án khác.
- "Dự án X đang tới đâu?" → Claude chạy `python tools/project.py status X` (khoảng 10 dòng) thay vì mở tài liệu.
- Mỗi dự án / mỗi việc lớn một phiên chat; xong việc gõ `/clear` (hoặc `/compact` giữa chừng) để lịch sử cũ không bị gửi lại mỗi lượt.
- Tắt connector không dùng (Figma, Gmail…) trong cài đặt — định nghĩa công cụ của connector cũng chiếm ngữ cảnh.
- Cập nhật nhỏ dùng `srs-update` (vài phút); chỉ chạy `srs-publish` khi cần gửi khách — khi có file Word mới, Claude hỏi thư mục Drive để đẩy.
- Xem token đã dùng: `/usage`, `/context`.

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
| Xuất lại Word | `python .claude/skills/write-srs/scripts/to_docx.py <du-an>` (thêm `--src URD.md` / `--src UC.md` cho tài liệu khác) |
| Kiểm tra use case | `python .claude/skills/write-usecase/scripts/check_uc.py <du-an> --write-matrix` |
| Xuất backlog CSV (Jira) | `python .claude/skills/write-user-story/scripts/backlog_csv.py <du-an>` |
| Nhập URD / FSD có sẵn | đính kèm file + "Đây là FSD của dự án `<du-an>`, làm SRS" — xem dàn ý: `python .claude/skills/doc-import/scripts/import_doc.py <du-an> <file>` |
| Viết test case | gõ "Viết test case cho `<du-an>`" — kiểm tra: `python .claude/skills/write-testcase/scripts/check_tc.py <du-an> --write-matrix` |
| Đẩy lên Google Drive | gõ "Đẩy dự án `<du-an>` lên Drive" — Claude hỏi bạn link thư mục đích (bạn tự tạo thư mục trên Drive); file luôn là Word |
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
Tạo scheduled task trên cloud để tự chạy khi có tài liệu mới trong `projects/<du-an>/Document/Bien_Ban_Khao_Sat/` (gõ `/schedule` trong Claude Code).
