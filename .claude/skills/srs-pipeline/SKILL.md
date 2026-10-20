---
name: srs-pipeline
description: Tạo mới trọn gói bộ tài liệu BA (phiên bản 0.1) cho một dự án CHƯA có SRS — từ tài liệu khảo sát (dán/đính kèm ngay trong chat hoặc có sẵn trong inputs/<du-an>/) ra brainstorm, URD, SRS (tách theo phân hệ trong srs/), wireframe UI, ảnh PNG và SRS.docx, rồi commit + mở PR. Dự án đã có SRS thì chuyển sang srs-update (cập nhật nhanh) hoặc srs-publish (xuất bản). Dùng khi user nói "làm SRS cho dự án X", "làm tài liệu cho X", "làm URD/SRS/wireframe trọn gói", "chạy pipeline tài liệu", kể cả khi kèm text/file trong cùng tin nhắn. Keywords - SRS pipeline, end-to-end BA documentation, requirements document, URD, software requirements specification, wireframe, docx export, Magento, Odoo. Chạy tự động hoàn toàn, không hỏi lại user; thiếu thông tin thì ghi Assumptions & Open Questions.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(pandoc *), Bash(npx mmdc *), Bash(mmdc *), Bash(git *), Bash(gh pr *)
disallowed-tools: AskUserQuestion
---

# srs-pipeline — nhạc trưởng

Bạn là BA lead chạy toàn bộ chuỗi **không có người can thiệp**. Không bao giờ dừng lại hỏi user. Khi gặp điểm mơ hồ: chọn phương án hợp lý nhất, ghi `AS-xx` + `OQ-xx`, đi tiếp.

## Bước 0 — Xác định dự án và nạp tài liệu từ chat

1. Lấy `<du-an>` từ câu lệnh của user (vd. "Làm SRS cho dự án rma-magento" → `rma-magento`).
2. **Tin nhắn có kèm tài liệu** (text dán vào, file đính kèm, ảnh, link) → làm theo `.claude/skills/ba-intake/SKILL.md` ở **chế độ tự động** (không hỏi; khác biệt được tự merge, mâu thuẫn thành OQ) trước khi đi tiếp. Script của skill đó đã chuyển sang branch `docs/<du-an>` và push.
3. Nếu user không nêu tên và không kèm tài liệu: chọn thư mục trong `inputs/` (bỏ qua `_example`) có thời điểm sửa mới nhất mà **chưa có** `outputs/<du-an>/SRS.md`. Nếu không có thư mục nào khác thì dùng `_example`. Ghi lựa chọn vào báo cáo cuối.
4. Không tìm thấy `inputs/<du-an>/` → tìm thư mục gần đúng tên (không phân biệt hoa thường, bỏ dấu). Vẫn không có → báo lỗi ngắn gọn, gợi ý "dán hoặc đính kèm tài liệu vào chat", rồi dừng (đây là trường hợp duy nhất được dừng).
5. **Dự án đã có `outputs/<du-an>/SRS.md`** → KHÔNG chạy lại pipeline. Chuyển sang `.claude/skills/srs-update/SKILL.md` (cập nhật nhanh); nếu user nói thêm "xuất docx / gửi khách / xuất bản" thì sau đó chạy `.claude/skills/srs-publish/SKILL.md`. Kết thúc skill này.
6. Lệnh Python: dùng `python3` nếu có, không thì `python`. Bên dưới viết `python`.

## Bước 1 — Git

```bash
git status --short
git fetch origin
git checkout docs/<du-an> && git pull --ff-only     # branch đã có (local hoặc origin)
git checkout -b docs/<du-an> origin/main            # chưa có
```

- Môi trường cloud có thể ép session làm việc trên branch riêng (vd. `claude/...`). Nếu `git checkout -b` bị chặn hoặc lỗi quyền, ở lại branch hiện tại và ghi chú vào báo cáo.
- Không bao giờ commit lên `main`/`master`.

## Bước 2 — Đọc toàn bộ input

Thứ tự ưu tiên khi đọc `inputs/<du-an>/`:
1. `_tong-hop.md` (nếu có) — bản yêu cầu đã hợp nhất, là **nguồn sự thật hiện hành**.
2. `_manifest.md` — biết thứ tự thời gian các tài liệu; tài liệu nạp sau và bản `__vN` lớn nhất được ưu tiên khi mâu thuẫn.
3. `_changes/*.md` — các khác biệt và quyết định đã chốt.
4. Mọi tài liệu còn lại (cả bản cũ — để hiểu bối cảnh): `.md`, `.txt`, `.csv`, `.json`, `.eml`, ảnh (Read để xem), `.pdf` (Read theo trang), `.docx`/`.xlsx` (đọc bản trích trong `_extracted/`; không có thì `pandoc file.docx -t markdown`, vẫn không được → OQ "không đọc được file X").

Ghi nhớ nguồn của từng thông tin (tên file) để trích dẫn. Mâu thuẫn chưa được chốt trong `_changes/` → `OQ-xx`.

## Bước 3 — Chạy chuỗi skill

Với mỗi bước: đọc `.claude/skills/<skill>/SKILL.md` của **repo này** và làm đúng theo đó (tương đương gọi skill; không dùng skill trùng tên ở nơi khác). Sau mỗi bước, commit.

| # | Skill | Output chính | Commit message |
|---|---|---|---|
| 1 | `brainstorm` | `brainstorm.md` | `docs(<du-an>): brainstorm` |
| 2 | `write-urd` | `URD.md` | `docs(<du-an>): URD` |
| 3 | `write-srs` | `srs/*.md` (tách phân hệ) → `SRS.md` | `docs(<du-an>): SRS draft` |
| 4 | `ui-spec` | `ui/flows.md` | `docs(<du-an>): UI spec & flows` |
| 5 | `wireframe` | `ui/screens/*.html`, `ui/index.html` | `docs(<du-an>): wireframes` |
| 6 | `render-screens` | `ui/png/*.png`, `ui/diagrams/*.png` | `docs(<du-an>): render screens` |

Commit:
```bash
git add outputs/<du-an>
git commit -m "docs(<du-an>): <bước>"
```

Nếu một bước phát hiện lỗi ở bước trước (vd. wireframe thấy SCR thiếu trường trong Screen Inventory) → **sửa ngược lại file nguồn** (`srs/*.md`, rồi chạy `build_srs.py`), không để hai tài liệu lệch nhau.

## Bước 4 — Xuất Word

```bash
python .claude/skills/write-srs/scripts/to_docx.py <du-an>
```

Script tự render Mermaid trong SRS.md, nhúng ảnh `ui/png/*.png`, dùng `templates/reference.docx` nếu có, và in số ảnh đã nhúng. Nếu báo ảnh thiếu → chạy lại `render-screens` cho màn đó, hoặc sửa đường dẫn trong SRS.md. Nếu không có pandoc → ghi rõ vào báo cáo, không dừng các bước còn lại.

## Bước 5 — Tự review

1. Chạy kiểm tra tự động:
   ```bash
   python .claude/skills/write-srs/scripts/check_srs.py <du-an> --final
   python .claude/skills/wireframe/scripts/build_ui.py <du-an>
   ```
   `--final`: thiếu ảnh/HTML/docx tính là `ERROR`. Nếu PNG/docx không tạo được do thiếu công cụ (đã ghi báo cáo) thì các lỗi đó được chấp nhận, mọi lỗi khác phải sửa.
2. Đọc `.claude/skills/write-srs/checklist.md`, đi từng mục, sửa mọi lỗi tìm thấy (SRS, URD, wireframe).
3. Lặp lại bước 1–2 tới khi `check_srs.py` không còn `ERROR` (tối đa 3 vòng; còn lỗi thì ghi vào báo cáo).
4. Nếu đã sửa `srs/*.md` hoặc HTML → chạy lại `render-screens` (chỉ màn bị sửa) và `to_docx.py`.
5. Commit: `docs(<du-an>): self-review fixes` + `docs(<du-an>): export SRS.docx`.

## Bước 6 — Push + PR

```bash
git push -u origin HEAD
gh pr create --base main --title "docs(<du-an>): URD + SRS + wireframe" --body-file outputs/<du-an>/.tmp/pr-body.md
```

- Nội dung PR body = báo cáo tóm tắt ở Bước 7 (ghi tạm vào `outputs/<du-an>/.tmp/pr-body.md`, thư mục `.tmp` đã được `.gitignore`).
- Không có `gh` hoặc `gh` chưa đăng nhập → chỉ push branch, ghi vào báo cáo: "Mở PR từ giao diện (nút Create PR)". Không có remote → bỏ qua push, ghi vào báo cáo.

## Bước 7 — Báo cáo tóm tắt (tin nhắn cuối cho user)

```markdown
## Kết quả: <du-an>
- Branch: docs/<du-an> · PR: <link hoặc lý do chưa có>
- URD: <n> user story · SRS: <n> FR, <n> NFR · <n> màn hình (<n> storefront, <n> backend)
- Ảnh: <n> PNG · SRS.docx: <có/không> (<n> ảnh nhúng)
- Kiểm tra: check_srs.py <PASS/n lỗi> · checklist <n/n mục đạt>

### Open Questions cần khách hàng trả lời
| Mã | Câu hỏi | Ảnh hưởng tới |
|---|---|---|
| OQ-01 | … | FR-03, SCR-02 |

### Giả định đã áp dụng
- AS-01 …

### Chưa đạt / cần lưu ý
- … (công cụ thiếu, bước bị bỏ qua, lỗi còn tồn tại)
```

Danh sách Open Questions lấy nguyên từ `srs/09-gia-dinh-cau-hoi.md`. Không bỏ sót mục nào.

## Sau phiên bản 0.1

Mọi thông tin mới (khảo sát, demo, khách trả lời câu hỏi) đi theo 2 nhịp, **không chạy lại pipeline này**:
- **Cập nhật nhanh** (`srs-update`, vài phút): sửa đúng file phân hệ bị ảnh hưởng, 0.1 → 0.1.1, đánh dấu màn cần vẽ lại.
- **Xuất bản** (`srs-publish`, khi gửi khách): vẽ lại màn đang chờ, xuất docx, 0.1.x → 0.2, PR.

`brainstorm.md` chỉ viết một lần ở đây; các lần sau không cập nhật (kiến thức hiện hành nằm ở `inputs/<du-an>/_tong-hop.md` và `srs/`).

## Nguyên tắc xuyên suốt
- Không hỏi user. Không chờ xác nhận giữa các bước.
- Không bịa số liệu cụ thể (giá, SLA, số lượng) mà input không có — dùng giá trị đề xuất kèm `AS-xx` và `OQ-xx`.
- Mã định danh, tên file, ngôn ngữ: theo `CLAUDE.md`.
- Lỗi công cụ (pandoc, Playwright, mmdc thiếu) không làm dừng chuỗi: làm hết phần làm được, báo cáo phần thiếu kèm lệnh cài (`setup/cloud-setup.sh`).
