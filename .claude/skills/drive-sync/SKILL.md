---
name: drive-sync
description: Đẩy tài liệu dự án lên Google Drive (SRS/URD/UC → Google Doc, backlog/test case → Sheet; tuỳ chọn sơ đồ, ảnh, input) vào "BA Projects/<du-an>/" cùng cấu trúc thư mục với git, chỉ giữ bản mới nhất; đọc comment của khách; sửa nhanh trên Doc. CHỈ chạy khi user yêu cầu ("đẩy X lên Drive", "lấy góp ý trên Drive", "sửa trên Doc").
allowed-tools: Read, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(pandoc *), Bash(git *), mcp__Google_Drive__search_files, mcp__Google_Drive__create_file, mcp__Google_Drive__update_file, mcp__Google_Drive__get_file_metadata, mcp__Google_Drive__read_file_content, mcp__Google_Docs__read_doc, mcp__Google_Docs__update_doc
---

# drive-sync — quản lý output trên Google Drive

Repo (`projects/<du-an>/`) là **nguồn gốc**; Drive là **bản phát hành để đọc / góp ý**. Không sửa nội dung trên Drive mà không sửa trong repo.

Chỉ chạy khi user yêu cầu (không tự chạy sau `srs-update` / `srs-publish`) — **trừ** dự án có `project.json` › `drive.auto_upload: true` (vd. BBA): chạy ngay sau mỗi lần tạo / sửa tài liệu đầu ra. Không hỏi user, trừ khi công cụ Drive báo lỗi cần người quyết (xem "Lỗi").

## Bước 0 — Điều kiện
1. Có công cụ `mcp__Google_Drive__create_file` (connector Google Drive đã kết nối)? Không có → dừng, báo: "Chưa kết nối Google Drive — bật connector Google Drive trong cài đặt claude.ai rồi thử lại." Không tìm cách khác.
2. Có `projects/<du-an>/docs/SRS.md` (hoặc ít nhất `URD.md`). Không có → dừng, gợi ý chạy `srs-pipeline`.
3. Lệnh Python: `python3` nếu có, không thì `python`.

## Bước 1 — Kế hoạch
```bash
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an>                 # mặc định: tài liệu (srs, urd, uc, backlog, tc)
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --only srs      # user chỉ nói "đẩy SRS"
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --diagrams      # + ảnh sơ đồ (user nói "đẩy cả sơ đồ")
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --ui --input --exports   # + ảnh wireframe / input / file gốc
```
Dự án có `project.json` › `drive.docs` (danh sách `src` Markdown trong `docs/`, cho phép `*`): các tài liệu đó cũng nằm trong kế hoạch, xuất `.docx` theo `docx_style` của dự án rồi đẩy thành Google Doc (định dạng font, giãn dòng, thụt, kẻ bảng được giữ khi chuyển đổi). Mục có `parent: "sprint"` + `convert: false` (FSD của BBA) đi vào thư mục Sprint của khách dưới dạng **.docx nguyên bản** — dòng kế hoạch ghi rõ `GIỮ .docx` và `parent=<id Sprint>`; gọi `create_file` với `disableConversionToGoogleType: true`.
Mặc định **chỉ đẩy tài liệu**: mỗi file là một lần gọi công cụ và có thể phải bấm duyệt, nên ảnh/input/exports chỉ đẩy khi user yêu cầu.
Script tự xuất `.docx` khi cũ hơn `.md`, nén ảnh docx nếu > 3,0 MB (giới hạn mỗi lần gọi Drive), so `sha256` nguồn với `_drive.json`. Màn hình chỉ in mục `create` / `replace` (kèm `parent` và `file_ref`) và mục lỗi; kế hoạch đầy đủ ở `.tmp/drive/plan.json` — **không cần mở file đó** trừ khi cần trường `current` của mục `replace`.

| action | Làm gì |
|---|---|
| `create` | Chưa có trên Drive → tạo mới (Bước 3) |
| `replace` | Nguồn đã đổi → tạo bản mới, bản cũ vào `_luu-tru/` (Bước 3–4) |
| `skip` | Không đổi → bỏ qua (user nói "đẩy lại" thì chạy với `--force`) |
| `missing` | Chưa có tài liệu (vd. chưa có `UC.md`) → bỏ qua, ghi báo cáo |
| `too_big` / `error` | Không đẩy; báo user nguyên văn lỗi (Bước "Lỗi") |

## Bước 2 — Thư mục: giống hệt git, chỉ bản mới nhất
```
My Drive/BA Projects/              (root)       ⇔ projects/
  <du-an>/                         (project)    ⇔ projects/<du-an>/   — link gửi khách: thư mục này
    docs/      SRS, URD, Use Case (Google Doc), Backlog, Test case (Google Sheet — QA ghi kết quả chạy test ngay trên Sheet)
    diagrams/  ảnh sơ đồ (khi --diagrams)
    ui/        ảnh wireframe trạng thái mặc định (khi --ui)
    exports/   file .docx/.csv gốc ≤ 3 MB (khi --exports)
    input/     tài liệu khảo sát gốc (khi --input; bỏ file hệ thống "_")
    _luu-tru/  (archive) bản cũ, khoá chỉ đọc
```
- Dòng cuối của `drive_pack.py` báo "thiếu ID thư mục: …" → chỉ tạo đúng các thư mục đó:
  `search_files` (`title = '<tên>' and mimeType = 'application/vnd.google-apps.folder' and parentId = '<id cha>'`); không có thì `create_file` (`contentMimeType: application/vnd.google-apps.folder`, `parentId`). Root tìm với `parentId = 'root'`.
- Ghi lại (một lệnh cho nhiều thư mục):
  ```bash
  python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --folders root=<id> project=<id> archive=<id> docs=<id> diagrams=<id> ui=<id> exports=<id> input=<id>
  ```
- Thư mục đã có ID → không tìm lại.

## Bước 3 — Tải lên
Với mỗi mục `create` / `replace`, gọi `mcp__Google_Drive__create_file`:
- `title`: tên trong kế hoạch (tài liệu: "SRS — <du-an>"…; ảnh / file: tên file); `parentId`: `parent` của mục (chạy lại `drive_pack.py` sau Bước 2 nếu `parent=CHƯA CÓ`).
- `contentMimeType`: mime của mục. Tài liệu (docx → Google Doc, csv → Google Sheet) và `.md/.txt` để Drive tự chuyển; ảnh, pdf, xlsx, file trong `exports/` đặt `disableConversionToGoogleType: true`.
- `base64Content`: đúng chuỗi `file_ref` (dạng `sha256:<hex>:<đường dẫn>`) — app tự điền nội dung sau khi user duyệt. Không tự mã hoá base64.
- **Mỗi lần gọi một file, đợi kết quả rồi mới gọi file sau** — gọi song song dễ bị Drive báo "Resource has been exhausted".
Ghi lại ngay sau mỗi file (key đúng như kế hoạch in, vd. `srs`, `diagrams/uc-01.png`):
```bash
python .claude/skills/drive-sync/scripts/drive_pack.py <du-an> --record <key> <file_id> <viewUrl>
```
(`--record` tự chuyển bản cũ của key đó vào mục `archived` trong `_drive.json`.)

## Bước 4 — Lưu trữ bản cũ (chỉ với `replace`)
Với `current.file_id` của mục vừa thay: `mcp__Google_Drive__update_file`
- `parentId`: ID `archive` (`_luu-tru`); `title`: `<title cũ> (v<current.version> — lưu trữ <dd/mm/yyyy>)`; `readOnly: true`, `readOnlyReason: "Bản cũ — xem bản mới trong thư mục <du-an>"`.

Không xoá bản cũ: comment của khách trên bản cũ vẫn đọc được (Bước 6).

## Bước 5 — Commit + báo cáo
```bash
python tools/project.py card <du-an>     # cập nhật link Drive trong PROJECT.md
git add projects/<du-an>/_drive.json projects/<du-an>/PROJECT.md && git commit -m "docs(<du-an>): đồng bộ Google Drive" && git push -u origin HEAD
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
1. Sửa **nguồn trong repo trước** (`docs/srs/*.md` → `build_srs.py`, hoặc `URD.md`), commit như bình thường.
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
