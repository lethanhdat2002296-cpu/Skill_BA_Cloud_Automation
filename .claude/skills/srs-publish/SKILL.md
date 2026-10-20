---
name: srs-publish
description: Xuất bản bộ tài liệu khi cần gửi khách - chỉ vẽ lại và chụp lại các màn hình đang chờ trong ui/_pending.md (song song nếu nhiều), render sơ đồ, ghép SRS từ srs/*.md, xuất SRS.docx, tự review, đặt phiên bản phát hành (0.3.x → 0.4), commit + push + mở PR. Dùng khi user nói "xuất bản tài liệu dự án X", "xuất SRS/docx cho X", "chuẩn bị gửi khách", "phát hành bản mới", "vẽ lại các màn đang chờ". Keywords - publish, release, export docx, regenerate wireframes, pending screens, PR.
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Bash(python *), Bash(python3 *), Bash(pandoc *), Bash(npx mmdc *), Bash(mmdc *), Bash(git *), Bash(gh pr *)
disallowed-tools: AskUserQuestion
---

# srs-publish — xuất bản khi cần gửi khách

Chỉ làm lại phần **đã thay đổi** từ lần phát hành trước. Không hỏi user.

Lệnh Python: `python3` nếu có, không thì `python`.

## Bước 0 — Chuẩn bị
1. Branch `docs/<du-an>`: `git fetch origin && git checkout docs/<du-an> && git pull --ff-only`. **Cloud** (session chỉ được push lên branch được chỉ định, vd. `claude/...`) → ở lại branch hiện tại.
2. Chưa có `outputs/<du-an>/srs/` → chạy Bước 0.3 của `srs-update` (tách SRS) trước.
3. `python .claude/skills/write-srs/scripts/build_srs.py <du-an>`.
4. Đọc `outputs/<du-an>/ui/_pending.md` (không có file / bảng rỗng → không có màn nào cần vẽ, nhảy tới Bước 3).
5. User nói "chỉ xuất docx" / "không vẽ lại" → bỏ Bước 1–2, ghi trong báo cáo các màn có ảnh cũ.

## Bước 1 — Vẽ lại các màn đang chờ

Với mỗi SCR trong `_pending.md`:
- Cập nhật mục `### SCR-xx` trong `ui/flows.md` (chỉ mục đó; màn mới → thêm mục + node trong sitemap).
- Sửa `ui/screens/SCR-xx-<slug>.html` theo cột "Việc cần làm" — **Edit đúng vùng**, không vẽ lại cả file nếu thay đổi nhỏ. Màn mới → tạo file theo skill `wireframe` (khung file, kit, `patterns.md`).
- Chỉ đọc: dòng SCR trong `srs/06-man-hinh.md`, các FR liên quan (theo `build_srs.py --index`), `wireframe/design-kit/patterns.md`, khối markup cần dùng trong `components-*.html`.

**Song song:** ≥ 4 màn chờ và có công cụ Agent → chia thành nhóm 2–3 màn, mỗi nhóm một subagent. Brief cho subagent gồm: đường dẫn repo, danh sách SCR + "Việc cần làm", đường dẫn kit (`tokens.css`, `components-*.html`, `patterns.md`), quy tắc khung file trong `.claude/skills/wireframe/SKILL.md`, "chỉ sửa ui/screens/<file của mình> và mục SCR tương ứng trong ui/flows.md, không commit". Đợi tất cả xong rồi làm tiếp.

## Bước 2 — Chụp và review chỉ các màn đó
```bash
python .claude/skills/wireframe/scripts/build_ui.py <du-an>
python .claude/skills/render-screens/scripts/shot.py <du-an> --only SCR-04 SCR-12
```
- Mở xem (Read) ảnh default desktop của từng màn vừa vẽ (+ mobile nếu storefront). Sửa lỗi layout/thiếu trường, chụp lại màn đó. Tối đa 2 vòng/màn.
- Không mở lại ảnh của màn không đổi.

## Bước 3 — Sơ đồ, Word, kiểm tra
```bash
python .claude/skills/render-screens/scripts/render_mermaid.py <du-an>
python .claude/skills/render-screens/scripts/swimlane.py <du-an>      # chỉ khi có ui/swimlanes/*.json
python .claude/skills/write-srs/scripts/to_docx.py <du-an>
python .claude/skills/write-srs/scripts/check_srs.py <du-an> --final
```
Sửa mọi `ERROR` (trong `srs/*.md`, rồi chạy lại). Thiếu công cụ (pandoc/Playwright/mmdc) → ghi báo cáo, không dừng.

## Bước 4 — Phiên bản phát hành
- `srs/00-dau-trang.md`: phiên bản → **minor tiếp theo** (0.3.2 → 0.4), trạng thái "Phát hành cho khách review".
- Thêm dòng Lịch sử phiên bản: `| 0.4 | <ngày> | Phát hành — gộp 0.3.1–0.3.2: <tóm tắt> | — | SCR vẽ lại: … |`.
- `ui/_pending.md`: chuyển các dòng đã vẽ xuống bảng "Đã xử lý" kèm phiên bản `0.4`.
- `build_srs.py` lần cuối (để SRS.md có phiên bản mới) → `to_docx.py` lại nếu đã xuất trước khi đổi phiên bản.

## Bước 5 — Commit, push, PR
```bash
git add outputs/<du-an>
git commit -m "docs(<du-an>): phát hành v0.4"
git push -u origin HEAD
gh pr create --base main --title "docs(<du-an>): v0.4" --body-file outputs/<du-an>/.tmp/pr-body.md
```
Không có `gh` → dùng công cụ GitHub sẵn có (MCP) hoặc đưa link `https://github.com/<owner>/<repo>/compare/main...<branch hiện tại>`. PR đã tồn tại → chỉ push (PR tự cập nhật).

PR body = báo cáo dưới đây.

## Bước 6 — Báo cáo
```markdown
## Phát hành <du-an> v0.4
- Thay đổi từ v0.3: <tóm tắt từ Lịch sử phiên bản các bản 0.3.x>
- Màn vẽ lại: SCR-04, SCR-12 (<n> ảnh) · Màn không đổi giữ ảnh cũ
- SRS.docx: <n> ảnh nhúng · check_srs --final: PASS
- Open Questions còn mở: <n> (liệt kê mã + câu hỏi)
- PR: <link>
```
