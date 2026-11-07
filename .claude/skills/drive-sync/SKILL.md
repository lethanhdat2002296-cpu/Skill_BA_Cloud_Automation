---
name: drive-sync
description: Đẩy bộ tài liệu của một dự án (SRS, URD, Use Case thành Google Doc; backlog thành Google Sheet) lên Google Drive của người làm, giữ đúng một bản mới nhất trong thư mục "BA Outputs/<du-an>/" (bản cũ chuyển vào _luu-tru/ và khoá chỉ đọc), ghi ID/link vào outputs/<du-an>/_drive.json; đọc góp ý (comment) của khách trên Doc để nạp lại qua ba-intake; sửa nhanh trực tiếp trên Doc khi được yêu cầu. CHỈ chạy khi user yêu cầu - "đẩy dự án X lên Drive", "đồng bộ Drive", "cập nhật Doc trên Drive", "lấy góp ý trên Drive", "sửa trên Doc". Keywords - Google Drive, Google Docs, Google Sheets, upload, sync, share with client, comments, feedback.
allowed-tools: Read, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(pandoc *), Bash(git *), mcp__Google_Drive__search_files, mcp__Google_Drive__create_file, mcp__Google_Drive__update_file, mcp__Google_Drive__get_file_metadata, mcp__Google_Drive__read_file_content, mcp__Google_Docs__read_doc, mcp__Google_Docs__update_doc
---

# drive-sync — quản lý output trên Google Drive

Repo (`outputs/<du-an>/`) là **nguồn gốc**; Drive là **bản phát hành để đọc / góp ý**. Không sửa nội dung trên Drive mà không sửa trong repo.

Chỉ chạy khi user yêu cầu (không tự chạy sau `srs-update` / `srs-publish`). Không hỏi user, trừ khi công cụ Drive báo lỗi cần người quyết (xem "Lỗi").

## Bước 0 — Điều kiện
1. Có công cụ `mcp__Google_Drive__create_file` (connector Google Drive đã kết nối)? Không có → dừng, báo: "Chưa kết nối Google Drive — bật connector Google Drive trong cài đặt claude.ai rồi thử lại." Không tìm cách khác.
2. Có `outputs/<du-an>/SRS.md` (hoặc ít nhất `URD.md`). Không có → dừng, gợi ý chạy `srs-pipeline`.
3. Lệnh Python: `python3` nếu có, không thì `python`.

## Bước 1 — Kế hoạch
```bash
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an>            # mặc định: srs, urd, uc, backlog
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --only srs # user chỉ nói "đẩy SRS"
```
Script tự xuất `.docx` khi cũ hơn `.md` (dùng `write-srs/scripts/to_docx.py`), nén ảnh nếu file > 3,0 MB (giới hạn mỗi lần gọi công cụ Drive), so `sha256` nguồn với `_drive.json`, rồi in `DRIVE_PLAN {json}`:

| action | Làm gì |
|---|---|
| `create` | Chưa có trên Drive → tạo mới (Bước 3) |
| `replace` | Nguồn đã đổi → tạo bản mới, bản cũ vào `_luu-tru/` (Bước 3–4) |
| `skip` | Không đổi → bỏ qua (user nói "đẩy lại" thì chạy với `--force`) |
| `missing` | Chưa có tài liệu (vd. chưa có `UC.md`) → bỏ qua, ghi báo cáo |
| `too_big` / `error` | Không đẩy; báo user nguyên văn lỗi (Bước "Lỗi") |

## Bước 2 — Thư mục (chỉ bản mới nhất)
```
My Drive/BA Outputs/                  (root)
  <du-an>/                            (project) — link chia sẻ cho khách: luôn là thư mục này
    SRS — <du-an>                     Google Doc
    URD — <du-an>                     Google Doc
    Use Case — <du-an>                Google Doc
    Backlog — <du-an>                 Google Sheet
    _luu-tru/                         (archive) bản cũ, khoá chỉ đọc
```
- `folders` trong DRIVE_PLAN đã có ID → dùng luôn, không tìm lại.
- Chưa có: `search_files` với `title = 'BA Outputs' and mimeType = 'application/vnd.google-apps.folder' and parentId = 'root'`; không có thì `create_file` (`contentMimeType: application/vnd.google-apps.folder`). Tương tự `<du-an>` trong root và `_luu-tru` trong project. Ghi lại:
  ```bash
  python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --folders <root_id> <project_id> <archive_id>
  ```

## Bước 3 — Tải lên
Với mỗi mục `create` / `replace`, gọi `mcp__Google_Drive__create_file`:
- `title`: `title` của mục; `parentId`: ID thư mục project.
- `contentMimeType`: `mime` của mục (docx → Drive tự chuyển thành Google Doc có bảng, ảnh; csv → Google Sheet). **Không** đặt `disableConversionToGoogleType`.
- `base64Content`: đúng chuỗi `file_ref` của mục (dạng `sha256:<hex>:<đường dẫn>`) — app tự điền nội dung file sau khi user duyệt. Không tự mã hoá base64, không gõ nội dung.
- **Mỗi lần gọi một file, đợi kết quả rồi mới gọi file sau** — gọi song song dễ bị Drive báo "Resource has been exhausted". Mỗi file có thể cần user bấm duyệt.
Ghi lại ngay sau mỗi file:
```bash
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --record <key> <file_id> <viewUrl>
```
(`--record` tự chuyển bản cũ của key đó vào mục `archived` trong `_drive.json`.)

## Bước 4 — Lưu trữ bản cũ (chỉ với `replace`)
Với `current.file_id` của mục vừa thay: `mcp__Google_Drive__update_file`
- `parentId`: ID `_luu-tru`; `title`: `<title cũ> (v<current.version> — lưu trữ <dd/mm/yyyy>)`; `readOnly: true`, `readOnlyReason: "Bản cũ — xem bản mới trong thư mục <du-an>"`.

Không xoá bản cũ: comment của khách trên bản cũ vẫn đọc được (Bước 6).

## Bước 5 — Commit + báo cáo
```bash
git add outputs/<du-an>/_drive.json && git commit -m "docs(<du-an>): đồng bộ Google Drive" && git push -u origin HEAD
```
Báo cáo:
```markdown
## Đã đẩy <du-an> lên Google Drive
- Thư mục (gửi khách link này): <link thư mục project>
| Tài liệu | Phiên bản | Link | Ghi chú |
|---|---|---|---|
| SRS — <du-an> | 0.3 | <link> | Ảnh đã nén để vừa giới hạn upload |
- Bỏ qua (không đổi): … · Chưa có: … · Bản cũ đã chuyển vào _luu-tru: …
```

## Bước 6 — Đọc góp ý trên Drive (khi user nói "lấy góp ý / comment trên Drive")
1. Với từng `file_id` trong `_drive.json` (`files` và `archived` chưa xử lý): `mcp__Google_Drive__read_file_content` với `includeComments: true`.
2. Gom comment chưa resolve thành file Markdown `.intake/gop-y-drive-<YYYYMMDD>.md`: mỗi comment một dòng bảng `| Tài liệu | Đoạn được comment (trích ngắn) | Người comment | Nội dung | Mã liên quan (FR/US/SCR nếu đoán được) |`. Không thêm diễn giải.
3. Nạp bằng `ba-intake` (file vừa tạo, `--note "Góp ý của khách trên Google Drive"`) → ba-intake mô tả khác biệt, hỏi user, rồi `srs-update`.
4. Trả lời / resolve comment trên Drive **chỉ khi user yêu cầu** (đó là thao tác khách nhìn thấy).

## Bước 7 — Sửa nhanh trực tiếp trên Doc (khi user yêu cầu sửa một câu/giá trị trên Drive)
1. Sửa **nguồn trong repo trước** (`srs/*.md` → `build_srs.py`, hoặc `URD.md`), commit như bình thường.
2. Rồi sửa Doc tại chỗ bằng `mcp__Google_Docs__update_doc` với `replaceAllText` (`containsText.text` = câu cũ đúng nguyên văn, `matchCase: true`). Doc đã chia sẻ cho khách → `writeControl.writeMode: "SUGGEST"` để khách thấy đề xuất thay đổi; user nói "sửa thẳng" → `EDIT`.
3. Kiểm tra `occurrencesChanged` ≥ 1; = 0 → câu trên Doc khác nguồn (vd. khác định dạng) → báo user, không đoán.
4. Không cập nhật `source_sha256` trong `_drive.json` (lần đẩy sau sẽ thay cả file bằng bản chuẩn từ repo).
Thay đổi lớn (nhiều mục, bảng, ảnh) → không sửa tay trên Doc; chạy lại Bước 1–5.

## Lỗi
- Công cụ báo vượt giới hạn dung lượng ("over the … MB limit") → **không** tự cắt bớt nội dung hay thử cách khác; báo user nguyên văn và hỏi hướng xử lý (vd. tách tài liệu theo phân hệ, hoặc user tự upload `SRS.docx`).
- Lỗi quyền / không tìm thấy thư mục trong `_drive.json` (bị xoá trên Drive) → tìm lại theo tên (Bước 2); không có thì tạo mới và ghi đè `folders`.
- `too_big`: tài liệu quá lớn kể cả khi nén ảnh → báo user; đề xuất tách theo phân hệ.
- "Resource has been exhausted (e.g. check quota)": giới hạn tần suất / dung lượng chuyển đổi của Drive. Thử lại **một lần**; vẫn lỗi → dừng file đó (không `--record`), làm tiếp file nhỏ hơn, báo user chạy lại sau vài phút bằng `drive_pack.py <du-an> --only <key> --force`.
- Chỉ sửa công cụ xuất (vd. `to_docx.py`) mà nguồn `.md` không đổi → kế hoạch báo `skip`; dùng `--force` để đẩy lại.

## Nguyên tắc
- Không chia sẻ (share) file/thư mục cho ai nếu user không yêu cầu rõ người nhận và quyền.
- Không xoá file trên Drive; bản cũ chỉ chuyển vào `_luu-tru/`.
- `_drive.json` chỉ chứa ID, link, phiên bản, mã băm — không chứa token.
