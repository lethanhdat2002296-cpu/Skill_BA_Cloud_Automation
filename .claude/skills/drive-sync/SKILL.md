---
name: drive-sync
description: Đẩy tài liệu dự án lên Google Drive dưới dạng Word (.docx) vào thư mục do user tạo — mỗi lần đẩy hỏi user thư mục đích; đọc comment của khách. Chạy khi có file Word đầu ra mới hoặc user nói "đẩy X lên Drive", "lấy góp ý trên Drive".
allowed-tools: Read, Edit, Glob, Grep, AskUserQuestion, Bash(python *), Bash(python3 *), Bash(pandoc *), Bash(git *), mcp__Google_Drive__search_files, mcp__Google_Drive__create_file, mcp__Google_Drive__get_file_metadata, mcp__Google_Drive__read_file_content
---

# drive-sync — đưa file Word lên Google Drive

Repo (`projects/<du-an>/Document/`, Markdown) là **nguồn gốc**; Drive chứa **file Word** để gửi khách, đọc, góp ý.

## Quy tắc
- **Luôn là Word (.docx) nguyên bản**: `create_file` với `disableConversionToGoogleType: true`, `contentMimeType` docx. Không chuyển Google Doc / Sheet.
- **Thư mục do user tạo** và đưa link. Claude **không tạo thư mục**, không xoá, không di chuyển, không chia sẻ file trên Drive.
- **Mỗi lần đẩy phải hỏi user đẩy vào thư mục nào** (kể cả khi đã có gợi ý). Đây là ngoại lệ được phép của chế độ tự động.
- Khi nào chạy: sau khi skill khác tạo / sửa file Word đầu ra (xuất bản, FSD xong, test case xong…) hoặc khi user yêu cầu.

## Bước 0 — Điều kiện
1. Có công cụ `mcp__Google_Drive__create_file`? Không có → dừng, báo: "Chưa kết nối Google Drive — bật connector Google Drive trong cài đặt claude.ai rồi thử lại."
2. Lệnh Python: `python3` nếu có, không thì `python`.

## Bước 1 — Kế hoạch
```bash
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an>                       # mọi tài liệu Word
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --only "SRS/SRS"     # chỉ tài liệu user nhắc
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --diagrams --wireframe   # + ảnh PNG (khi user yêu cầu)
```
- Tài liệu: URD, SRS, Use Case, Backlog, Test case, mọi FSD (kể cả `Sprint <n>/`), + `project.json` › `drive.docs`. Script xuất `.docx` (định dạng `docx_style` của dự án nếu có) vào `.output/`, nén ảnh nếu > 3 MB.
- Mỗi dòng `create` / `replace`: `key`, tên file trên Drive, `file_ref`, **gợi ý thư mục** (đã dùng cho key này → `project.json` › `drive.folder_hints` → đã dùng cho cùng loại → `drive.root_url`).
- `skip` = không đổi từ lần đẩy trước; user nói "đẩy lại" → `--force`.

## Bước 2 — Hỏi thư mục đích (bắt buộc)
Một lần `AskUserQuestion`, mỗi câu hỏi một tài liệu (tối đa 4; nhiều hơn thì gộp theo loại: "Các FSD Sprint 4 đẩy vào đâu?"):
- Câu hỏi: "Đẩy `<tên file>` vào thư mục Drive nào?"
- Lựa chọn: các thư mục gợi ý từ kế hoạch (nhãn = tên thư mục, mô tả = link), thêm "Không đẩy lần này". User dán link khác qua "Other".
- Dự án chưa có gợi ý nào → hỏi user dán link thư mục (thư mục do user tự tạo trên Drive).
- Lấy ID từ link (`…/folders/<ID>`); tên thư mục: `get_file_metadata` (chỉ metadata, không đọc nội dung).

## Bước 3 — Tải lên
Với mỗi tài liệu user đã chọn thư mục: `mcp__Google_Drive__create_file`
- `title`: tên trong kế hoạch (vd. `[FRS] BBA-45-2.3.1.01_Action_Framework_v0.1.docx`, `SRS — odoo-mua-hang v0.4.docx`).
- `parentId`: ID thư mục user chọn; `contentMimeType`: `application/vnd.openxmlformats-officedocument.wordprocessingml.document`; `disableConversionToGoogleType: true`; `base64Content`: đúng chuỗi `file_ref` (app tự điền nội dung sau khi user duyệt).
- **Mỗi lần một file, đợi kết quả rồi mới gọi file sau** (gọi song song dễ bị "Resource has been exhausted").
- Ghi lại ngay:
  ```bash
  python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --record "<key>" <file_id> <viewUrl> --folder <ID thư mục> --folder-name "<tên thư mục>"
  ```
- `replace`: tải bản mới vào thư mục user chọn; **không** động vào bản cũ trên Drive (thư mục của user — user tự dọn nếu muốn). `--record` giữ bản cũ trong `history` của `_drive.json`.

## Bước 4 — Commit + báo cáo
```bash
python tools/project.py card <du-an>
git add projects/<du-an>/_drive.json projects/<du-an>/PROJECT.md && git commit -m "docs(<du-an>): đẩy Word lên Drive" && git push -u origin HEAD
```
```markdown
## Đã đẩy lên Google Drive (Word)
| Tài liệu | Phiên bản | Thư mục | Link |
|---|---|---|---|
- Bỏ qua (không đổi): … · User chọn không đẩy: …
```

## Bước 5 — Đọc góp ý (khi user nói "lấy góp ý / comment trên Drive")
1. Với từng `file_id` trong `_drive.json`: `mcp__Google_Drive__read_file_content` với `includeComments: true`. Lưu ý: comment đọc được đầy đủ trên Google Doc; file .docx chỉ đọc được nội dung — báo user nếu khách góp ý trong file Word (comment nằm trong file) để tải bản có comment về nạp lại bằng `ba-intake`.
2. Gom comment chưa resolve thành `.intake/gop-y-drive-<YYYYMMDD>.md` (bảng: Tài liệu · Đoạn được comment · Người · Nội dung · Mã liên quan).
3. Nạp bằng `ba-intake` (`--note "Góp ý của khách trên Google Drive"`) → ba-intake hỏi user → `srs-update`.

## Lỗi
- "over the … MB limit" → không tự cắt nội dung; báo user nguyên văn và hỏi hướng xử lý (tách tài liệu, hoặc user tự upload file trong `.output/`).
- `too_big`: nén ảnh vẫn > 3 MB → báo user, đề xuất tách theo phân hệ.
- "Resource has been exhausted": thử lại **một lần**; vẫn lỗi → dừng file đó (không `--record`), báo user chạy lại sau vài phút.
- Thư mục không tồn tại / không có quyền ghi → báo user, hỏi link khác.
