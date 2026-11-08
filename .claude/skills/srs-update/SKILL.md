---
name: srs-update
description: Cập nhật nhanh SRS sau khảo sát/demo: chỉ sửa đúng FR/US/UC/story bị ảnh hưởng, tăng 0.3 → 0.3.1, đánh dấu màn chờ vẽ; không vẽ, không xuất Word. Dùng khi dự án đã có SRS và user nói "cập nhật SRS cho X" hoặc sau ba-intake.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(git *)
disallowed-tools: AskUserQuestion
---

# srs-update — cập nhật nhanh sau khảo sát / demo

Nguyên tắc tốc độ: **thời gian phải tỉ lệ với lượng thay đổi, không tỉ lệ với độ dài tài liệu.**
- Không đọc lại toàn bộ `input/` hay toàn bộ SRS. Chỉ đọc tài liệu mới + phần SRS bị ảnh hưởng.
- Không viết lại file. Chỉ `Edit` đúng đoạn.
- Không đụng `brainstorm.md` (chỉ dùng cho lần đầu). `URD.md` chỉ sửa khi user story thêm mới / đổi mục tiêu.
- Không vẽ wireframe, không chụp PNG, không render Mermaid, không xuất docx → ghi vào `ui/_pending.md` cho `srs-publish`.
- Không hỏi user (câu hỏi về khác biệt đã được `ba-intake` hỏi trước đó).

Lệnh Python: `python3` nếu có, không thì `python`. Bên dưới viết `python`.

## Bước 0 — Điều kiện

1. Tin nhắn có kèm tài liệu mới → chạy `ba-intake` trước (skill đó hỏi user cách xử lý khác biệt, rồi quay lại đây).
2. Chưa có `projects/<du-an>/docs/SRS.md` → đây là dự án mới, dùng `srs-pipeline`.
3. Có `SRS.md` nhưng **chưa có thư mục `docs/srs/`** (dự án tạo bằng phiên bản cũ) → chuyển đổi **một lần**:
   ```bash
   grep -nE '^#{3,4} +FR-' projects/<du-an>/docs/SRS.md
   python .claude/skills/write-srs/scripts/split_srs.py <du-an> --modules "<Phân hệ A>=FR-01..FR-04,FR-22; <Phân hệ B>=FR-05..FR-08; ..."
   ```
   Gom FR theo phân hệ nghiệp vụ (mỗi phân hệ 3–8 FR, tên tiếng Việt ngắn). Script cảnh báo nếu ma trận truy vết viết tay lệch với dòng "Truy vết" của FR → sửa dòng "Truy vết" cho đúng. Commit riêng: `docs(<du-an>): chuyển SRS sang cấu trúc srs/`.
4. Branch: `docs/<du-an>` (`ba-intake` đã chuyển sẵn; nếu chưa: `git fetch origin && git checkout docs/<du-an> && git pull --ff-only`).
   **Cloud** (session chỉ được push lên branch được chỉ định, vd. `claude/...`) → ở lại branch hiện tại, không checkout `docs/<du-an>`.

## Bước 1 — Xác định thay đổi chưa xử lý

- Thay đổi chưa xử lý = các `projects/<du-an>/input/_changes/<thoi-diem>.md` **chưa xuất hiện** trong cột "Nguồn" của bảng "Lịch sử phiên bản" (`projects/<du-an>/docs/srs/00-dau-trang.md`).
- Với mỗi change report: đọc mục **"Nhận định của BA"** và **"Quyết định"**, cùng file tài liệu mới được nhắc tới. Không đọc tài liệu cũ trừ khi cần tra một chi tiết cụ thể.
- Không có change report nào chưa xử lý nhưng user nói "cập nhật" kèm nội dung → coi nội dung trong chat là thay đổi (đã qua `ba-intake`).

## Bước 2 — Lập kế hoạch tác động (trước khi sửa)

```bash
python .claude/skills/write-srs/scripts/build_srs.py <du-an> --index
```
Dòng `INDEX {json}` cho biết mỗi FR/NFR/SCR/AS/OQ nằm ở file nào trong `docs/srs/`, FR nào gắn SCR nào.

Phân loại từng ý thay đổi và ghi bảng **"Kế hoạch cập nhật"** vào cuối change report:

| # | Ý thay đổi | Loại | Sửa ở đâu | Màn hình |
|---|---|---|---|---|
| 1 | Bỏ trạng thái Waiting PO | Sửa FR | docs/srs/03-03-don-mua-hang.md (FR-09) | SCR-04 → pending |

| Loại | Sửa ở đâu |
|---|---|
| Trả lời OQ / xác nhận AS | `09-gia-dinh-cau-hoi.md`: OQ → "**Đã trả lời (nguồn):** …"; AS được xác nhận → "Đã xác nhận"; AS bị bác → sửa FR liên quan. Không xoá dòng. |
| Sửa FR (quy tắc, AC, input/output) | File phân hệ chứa FR (theo index). Sửa BR/AC đúng chỗ, ghi nguồn mới. |
| FR mới | Cuối file phân hệ phù hợp (hoặc file phân hệ mới `03-NN-<slug>.md`), mã tiếp theo, đủ trường + dòng "Truy vết". |
| Bỏ FR | Giữ heading, thêm `**[Đã bỏ — v<ver>]**` + lý do; dòng Truy vết → `Màn hình: Không có UI (đã bỏ)`. |
| Chỉ UI (nhãn, bố cục, thứ tự trường) | Không sửa văn FR. Sửa dòng SCR trong `06-man-hinh.md` nếu danh sách trường/hành động/trạng thái đổi. Thêm vào `ui/_pending.md`. |
| NFR / tích hợp / mapping | `04-phi-chuc-nang.md` / `05-tich-hop.md`. |
| Quy trình / luồng nghiệp vụ | `07-user-flow.md` (Mermaid) và/hoặc `diagrams/swimlanes/<so-do>.json` (sơ đồ Activity – Swimlane). Chỉ sửa đặc tả, không render — `srs-publish` vẽ lại. |
| Ngoài phạm vi / giai đoạn sau | `01-gioi-thieu.md` mục Phạm vi. |
| User story mới / đổi mục tiêu | `URD.md` — chỉ US đó, mã tiếp theo; tăng phiên bản URD. Rồi sửa UC liên quan trong `UC.md` và story trong `backlog.md` (story mới: ước lượng; story không đổi: không ước lượng lại). |
| Đổi kịch bản / ngoại lệ của một tương tác | `UC.md` — nhánh `3a…` của UC liên quan (tra ma trận mục 5 của UC.md). |
| Mâu thuẫn chưa chốt | `OQ-xx` mới trong `09`. |

## Bước 3 — Sửa đúng chỗ

- Tìm vị trí: `grep -n "FR-09" projects/<du-an>/docs/srs/03-03-don-mua-hang.md`, rồi `Read` với `offset/limit` quanh đó. Không Read cả thư mục.
- Sửa bằng `Edit` từng đoạn. Không `Write` lại file (trừ file phân hệ mới).
- Mã không đổi, không đánh lại số. Mã mới = mã lớn nhất + 1 (xem index).
- Đổi trường / hành động / trạng thái của màn hình → sửa dòng SCR trong `06-man-hinh.md` và ghi `ui/_pending.md`.
- Màn hình mới → thêm dòng trong bảng 6.1, thêm mục `#### SCR-xx — Tên` + dòng ảnh `![...](../ui/png/SCR-xx-<slug>.png)` trong 6.2, ghi `ui/_pending.md` với việc "Vẽ mới".

### `projects/<du-an>/ui/_pending.md`

```markdown
# Màn hình cần vẽ lại

| SCR | Việc cần làm | Lý do / nguồn | Từ phiên bản |
|---|---|---|---|
| SCR-04 | Bỏ nút "Waiting PO" khỏi statusbar; thêm cột "YCMH gốc" | _changes/20261020-093008.md #1 | 0.3.1 |

## Đã xử lý
| SCR | Việc | Phát hành |
|---|---|---|
```
Một SCR đã có dòng chờ → gộp việc vào dòng đó, không thêm dòng trùng.

## Bước 4 — Phiên bản

Trong `docs/srs/00-dau-trang.md`:
- Tăng **patch**: 0.3 → 0.3.1 → 0.3.2 (bản phát hành 0.4 do `srs-publish` đặt).
- Thêm dòng **Lịch sử phiên bản**: `| 0.3.1 | <YYYY-MM-DD> | <tóm tắt 1 câu> | _changes/<thoi-diem>.md | FR-09, FR-27, OQ-33; SCR-04 (chờ vẽ) |`.
- Ghi "Kế hoạch cập nhật" xong → đánh dấu change report đã xử lý: thêm dòng `> Đã cập nhật vào SRS v0.3.1` dưới mục "Quyết định".

## Bước 5 — Ghép, kiểm tra, push

```bash
python .claude/skills/write-srs/scripts/build_srs.py <du-an>
python .claude/skills/write-srs/scripts/check_srs.py <du-an>
python .claude/skills/write-usecase/scripts/check_uc.py <du-an> --write-matrix   # nếu có UC.md
python .claude/skills/write-user-story/scripts/backlog_csv.py <du-an>         # nếu có backlog.md
```
- `check_srs` không `--final` (ảnh/HTML của màn chờ vẽ được phép thiếu). Mọi `ERROR` khác phải sửa.
- Commit **một lần** + push **một lần**:
  ```bash
  python tools/project.py card <du-an>   # cập nhật thẻ dự án
  git add projects/<du-an>
  git commit -m "docs(<du-an>): v0.3.1 — <tóm tắt>"
  git push -u origin HEAD
  ```

## Bước 6 — Báo cáo (ngắn)

```markdown
## Đã cập nhật <du-an> → v0.3.1
| # | Thay đổi | Mã bị ảnh hưởng | File |
|---|---|---|---|
- OQ đã trả lời: OQ-33, … · OQ mới: … · FR mới: … · FR bỏ: …
- Màn hình chờ vẽ lại: SCR-04, SCR-12 (tổng <n> trong ui/_pending.md)
- SRS.docx và ảnh wireframe **chưa** cập nhật → gõ "Xuất bản tài liệu dự án <du-an>" khi cần gửi khách.
```
