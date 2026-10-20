---
name: ba-intake
description: Nhận tài liệu/thông tin dự án ngay trong đoạn chat (text dán vào, file đính kèm, ảnh chụp, link tải) rồi tự lưu vào inputs/<du-an>/ - text chuyển thành Markdown, file thì copy/tải về - giữ nguyên phiên bản cũ khi có cập nhật, tự commit + push lên GitHub, sau đó mô tả rõ khác biệt giữa thông tin cũ và mới và hỏi người làm muốn merge hay giữ cả hai. Dùng khi user dán biên bản họp, email, yêu cầu, ghi chú vào chat, đính kèm file (docx, pdf, xlsx, ảnh), gửi link tài liệu, hoặc nói "thêm thông tin cho dự án X", "cập nhật yêu cầu dự án X", "lưu tài liệu này", "đây là bản mới". Keywords - intake, upload requirements, attach file, paste notes, save to GitHub, version, update, diff, merge, change request.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, Bash(python *), Bash(python3 *), Bash(pandoc *), Bash(git *)
---

# ba-intake — nạp tài liệu từ chat lên GitHub

Mục tiêu: người làm **không phải tự tạo thư mục hay commit**. Mọi thứ đưa vào chat → nằm trong `inputs/<du-an>/` trên GitHub, không mất thông tin cũ, và khác biệt được nói rõ.

Lệnh Python: `python3` nếu có, không thì `python`. Bên dưới viết `python`.

## Bước 1 — Xác định dự án `<du-an>`

1. Lấy từ câu của user ("dự án rma-moc-an", "cho X"…). Chuẩn hoá: chữ thường, không dấu, nối `-`.
2. Không nêu tên → so khớp nội dung với các thư mục đã có trong `inputs/` (tên khách hàng, tên tính năng, mã đơn…). Khớp rõ một dự án → dùng dự án đó.
3. Không khớp → tạo tên mới từ khách hàng + chủ đề (vd. `moc-an-doi-tra`). **Không hỏi** — ghi rõ tên đã chọn trong báo cáo để user sửa nếu muốn.

## Bước 2 — Gom tài liệu từ chat

| User đưa gì | Làm gì |
|---|---|
| **Text** (dán biên bản, email, yêu cầu, ghi chú) | Chuyển thành Markdown theo mẫu bên dưới, ghi vào `.intake/<chu-de>.md` (thư mục `.intake/` ở gốc repo, đã gitignore). |
| **File đính kèm có đường dẫn** (CLI/desktop: `@"C:\...\file.docx"`, đường dẫn trong tin nhắn; cloud: file đã upload vào workspace) | Truyền đường dẫn vào `--file`. Không đọc-rồi-viết-lại file nhị phân. |
| **Ảnh dán thẳng / file chỉ thấy nội dung, không có đường dẫn** | Không lưu được bản gốc → chép lại nội dung thành Markdown (OCR, mô tả sơ đồ/bảng) vào `.intake/<chu-de>.md`, ghi dòng `> Bản gốc là ảnh/file đính kèm trong chat, không lưu được file gốc.` |
| **Link** (Google Drive chia sẻ công khai, link tải trực tiếp) | Truyền vào `--url`. Link cần đăng nhập (Drive riêng tư, SharePoint) → báo user tải về rồi đính kèm. |
| Lệnh không kèm tài liệu ("làm SRS cho X") | Không phải việc của skill này → dùng `srs-pipeline`. |

**Đặt tên file Markdown từ text:** `<chu-de>.md` theo nội dung, không ngày giờ (vd. `bien-ban-hop-kickoff.md`, `email-bo-sung-cskh.md`). Nếu user gửi **bản sửa** của một tài liệu đã có ("đây là biên bản bản mới", cùng cuộc họp) → dùng **đúng tên cũ** để script tự lưu thành `__v2` và tạo diff. Tài liệu khác chủ đề → tên mới.

### Mẫu Markdown chuyển từ text

```markdown
# <Tiêu đề: loại tài liệu — chủ đề>

| Thuộc tính | Giá trị |
|---|---|
| Nguồn | Chat (<người gửi nếu biết>) |
| Ngày tài liệu | <ngày ghi trong nội dung, hoặc "không ghi"> |
| Ngày nạp | <YYYY-MM-DD> |
| Loại | Biên bản họp / Email / Yêu cầu / Ghi chú / Bảng dữ liệu |

## Tóm tắt
- 3–5 gạch đầu dòng ý chính.

## Nội dung có cấu trúc
<Sắp xếp lại theo mục: Bối cảnh, Yêu cầu, Quy tắc nghiệp vụ, Dữ liệu/tích hợp, Việc cần làm, Câu hỏi còn mở — chỉ những mục có trong nội dung. Bảng/list giữ dạng bảng/list Markdown.>

## Nguyên văn
<Toàn bộ text user gửi, giữ nguyên, trong khối > trích dẫn hoặc ```text```.>
```

Quy tắc: **không thêm thông tin không có trong text**, không bỏ sót số liệu/tên/ngày. Phần "Nguyên văn" bắt buộc để không mất gì khi tái cấu trúc.

## Bước 3 — Chạy script nạp

```bash
python .claude/skills/ba-intake/scripts/intake.py <du-an> --file .intake/<chu-de>.md --file "<duong-dan-file-dinh-kem>" --url "<link>" --note "<mô tả 1 dòng>"
```
Dự án **đã có** `inputs/<du-an>/` → thêm `--no-push`: push một lần duy nhất ở Bước 5 sau khi đã điền nhận định (bớt một vòng push).

Script tự làm:
- Chuyển sang branch `docs/<du-an>` (tạo từ `main` nếu chưa có; cloud không cho đổi branch → ở lại branch hiện tại).
- Copy/chuyển file vào `inputs/<du-an>/` (tên không dấu). **Không ghi đè**: trùng tên khác nội dung → `<ten>__v2.<ext>`; trùng nội dung → bỏ qua.
- `.docx/.odt/.rtf` → trích text vào `inputs/<du-an>/_extracted/` (pandoc) để đọc và so sánh.
- Ghi `inputs/<du-an>/_manifest.md` (nhật ký mọi lần nạp).
- Dự án đã có tài liệu → tạo `inputs/<du-an>/_changes/<thoi-diem>.md` (diff tự động của các file có phiên bản mới).
- `git commit` + `git push -u origin HEAD`.
- In dòng `INTAKE_RESULT {json}`: `is_update`, `added`, `versions`, `duplicates`, `change_report`, `pushed`, `warnings`.

Push lỗi (chưa đăng nhập, không có remote) → báo user nguyên nhân + lệnh `git push -u origin HEAD` để tự chạy; không dừng các bước sau.

## Bước 4 — Dự án mới (`is_update = false`)

Báo cáo ngắn (file đã lưu, branch, commit, push) và gợi ý: **"Làm SRS cho dự án `<du-an>`"** (skill `srs-pipeline`). Kết thúc.

## Bước 5 — Dự án đã có tài liệu (`is_update = true`): mô tả khác biệt

1. Đọc `change_report`, các file mới/phiên bản mới, và `inputs/<du-an>/_tong-hop.md` (nếu có). **Không đọc cả SRS** — để biết ảnh hưởng FR/SCR dùng:
   ```bash
   python .claude/skills/write-srs/scripts/build_srs.py <du-an> --index    # mã -> file, FR -> SCR
   grep -rn "<từ khoá>" outputs/<du-an>/srs/ inputs/<du-an>/*.md          # tìm thông tin cũ liên quan
   ```
   Chỉ mở (Read có offset/limit) đúng đoạn cần so.
2. So sánh **theo nghĩa**, không chỉ theo dòng: file mới hoàn toàn (không phải `__v2`) cũng phải so với thông tin cũ trong các file khác.
3. Điền mục **"Nhận định của BA"** trong `change_report`:

   | # | Mục | Thông tin cũ (nguồn) | Thông tin mới (nguồn) | Loại | Ảnh hưởng |
   |---|---|---|---|---|---|
   | 1 | Hạn đổi trả khách VIP | 15 ngày (email-bo-sung-cskh.md) | 30 ngày (email-bo-sung-cskh__v2.md) | Sửa | FR-01, SCR-01 |

   Loại: **Thêm** (thông tin chưa từng có) · **Sửa** (giá trị khác) · **Bỏ** (bản mới không còn nhắc / nói rõ huỷ) · **Mâu thuẫn** (hai nguồn còn hiệu lực nói khác nhau, chưa rõ cái nào đúng). Ảnh hưởng: FR/NFR/SCR/AS/OQ trong SRS, hoặc "—" nếu chưa có SRS.
4. Commit + push **một lần** (gồm cả file vừa nạp): `git add inputs/<du-an> && git commit -m "input(<du-an>): mô tả khác biệt <thoi-diem>" && git push -u origin HEAD`.
5. Trình bày bảng khác biệt trong chat (ngắn gọn, đủ ý), rồi **hỏi người làm** bằng **một** lần gọi AskUserQuestion (gộp tất cả câu hỏi vào cùng một lần gọi, tối đa 4 câu):
   - Câu 1: "Xử lý khác biệt giữa thông tin cũ và mới thế nào?"
     - Dự án **đã có SRS**:
       - `Merge + cập nhật SRS ngay (Recommended)` — gộp vào `_tong-hop.md`, rồi chạy `srs-update` luôn trong lượt này.
       - `Merge, chưa cập nhật SRS` — chỉ gộp `_tong-hop.md`.
       - `Giữ cả hai, chưa merge` — chỉ lưu; lần cập nhật SRS sau coi bản mới là ưu tiên, mâu thuẫn thành OQ.
     - Dự án **chưa có SRS**: `Merge thành bản tổng hợp (Recommended)` / `Giữ cả hai, chưa merge`.
     - User tự mô tả khác biệt qua ô "Other" → ghi nguyên văn vào mục "Quyết định", xử lý theo đó.
   - Câu 2–4 (chỉ khi có dòng **Mâu thuẫn**, tối đa 3 mâu thuẫn quan trọng nhất): "<Mục>: giá trị nào đúng?" với lựa chọn `A — <giá trị> (<nguồn>)` / `B — <giá trị> (<nguồn>)`.

**Chế độ tự động** (skill được gọi từ `srs-pipeline`, hoặc user nói "không cần hỏi"): **không hỏi** — chọn Merge, mâu thuẫn ghi thành `OQ-xx`, ghi "Quyết định: tự động merge (pipeline)" vào change report.

## Bước 6 — Thực hiện quyết định

- **Merge:** tạo/cập nhật `inputs/<du-an>/_tong-hop.md` — bản yêu cầu hợp nhất, là nguồn ưu tiên cho các bước sau:
  ```markdown
  # Tổng hợp yêu cầu — <du-an>
  > Cập nhật lần cuối: <YYYY-MM-DD HH:mm> · Nguồn: xem _manifest.md

  ## <Chủ đề>
  - <Thông tin hiện hành> (nguồn: <file>, cập nhật <ngày>)

  ## Câu hỏi mở
  - <Mâu thuẫn chưa giải quyết> (nguồn A vs nguồn B)

  ## Lịch sử thay đổi
  | Ngày | Mục | Cũ | Mới | Nguồn | Quyết định |
  ```
  Thông tin bị thay thế **không xoá** — chuyển xuống "Lịch sử thay đổi". File gốc cũ/mới trong `inputs/` giữ nguyên.
- **Giữ cả hai:** chỉ ghi quyết định vào change report.
- Ghi mục **"Quyết định"** trong change report, commit: `input(<du-an>): quyết định <thoi-diem>`.
- **Merge + cập nhật SRS ngay** → không push ở đây; làm tiếp theo `.claude/skills/srs-update/SKILL.md` ngay trong lượt này (skill đó commit + push một lần ở cuối). Các lựa chọn khác → `git push` rồi báo cáo.

## Bước 7 — Báo cáo

```markdown
## Đã nạp vào dự án <du-an>
- Branch: <branch> · Commit: <sha> · Push: <OK / lỗi + cách xử lý>
- File mới: … · Phiên bản mới: … (bản cũ giữ nguyên) · Trùng (bỏ qua): …
- Khác biệt: <n> thêm, <n> sửa, <n> bỏ, <n> mâu thuẫn → <quyết định>
- Ảnh hưởng tới SRS: FR-…, SCR-… (nếu đã có SRS)

Bước tiếp: "Cập nhật SRS cho dự án <du-an>" (srs-update, vài phút) — hoặc "Xuất bản tài liệu dự án <du-an>" khi cần gửi khách.
```
Nếu đã chạy `srs-update` trong lượt này → gộp báo cáo của hai skill thành một.

## Nguyên tắc
- Không bao giờ ghi đè hay xoá file trong `inputs/` — mọi thay đổi là file mới hoặc phiên bản mới; git giữ lịch sử.
- File/thư mục bắt đầu bằng `_` trong `inputs/<du-an>/` là của hệ thống (`_manifest.md`, `_changes/`, `_extracted/`, `_tong-hop.md`).
- Không đưa mật khẩu, token, số tài khoản thật của khách vào Markdown; nếu text chứa thông tin nhạy cảm, che bớt (`******6789`) và báo user.
