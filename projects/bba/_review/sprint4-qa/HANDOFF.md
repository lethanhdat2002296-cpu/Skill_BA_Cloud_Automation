# Bàn giao phiên — Dự án BBA, Sprint 4 (13/11/2026)

> Đọc file này trước khi làm. Đây là tóm tắt phiên trước (phiên đó mất kết nối Google Drive). Mọi thứ nằm trong repo ở `projects/bba/_review/sprint4-qa/` (gọi tắt **R**): `frd-draft/` (bản nháp US BBA-66 → 79), `wf_body.html` + `BBA-68-79_wireframes.html` (wireframe nguồn), `by-frd/` (brainstorm + wireframe tách theo ticket), `code/` (script), `plane/` (câu trả lời Plane đã tải), `qa/` (file câu hỏi phản hồi dạng JSON / MD).
> Thư mục này là **bản nháp để review**, user cho phép đưa lên Git ngày 13/11/2026. Tệp gốc của khách (PDF / Excel đính kèm trên Plane, file Q&A .xlsx) **không** ở Git — tải lại từ Plane bằng `R/plane/att.py`, hoặc lấy trong file zip bàn giao user giữ.

## 1. Repo và cách chạy

- Repo `lethanhdat2002296-cpu/Skill_BA_Cloud_Automation`, dự án `projects/bba`. Branch của phiên trước: `claude/zealous-allen-urpfkn` (đã push; BBA-71 v0.2 ở commit `1ce34a5`). Phiên mới: lấy branch đó về (`git fetch origin claude/zealous-allen-urpfkn` rồi merge vào branch của phiên mới) trước khi làm.
- Đọc `projects/bba/PROJECT.md`, `projects/bba/project.json`, `projects/bba/templates/HUONG-DAN-FSD.md` (mục 4: quy tắc cập nhật).
- Xuất Word FRD **đúng mẫu "DOTB | FUNCTIONAL REQUIREMENTS SPECIFICATION"** (khổ Letter, header/footer có phiên bản) — luôn chạy đủ 2 bước:
  ```bash
  python3 tools/check_fsd.py bba "FSD/Sprint 4/<file>.md"
  python3 .claude/skills/write-srs/scripts/to_docx.py bba --src "FSD/Sprint 4/<file>.md"
  python3 tools/frs_format.py projects/bba/.output/<file>.docx --product "BBA SMS"
  ```
- Đồng bộ ngược Drive → Git: tải file Drive (file đang chia sẻ theo link tải được bằng `curl -L "https://drive.google.com/uc?export=download&id=<ID>"`), chạy `python3 tools/docx2md_fsd.py <docx> <md gốc> <md ra>`, so khác biệt **về nội dung** (bỏ qua dấu nháy cong, in đậm, dòng trống, `,` ↔ `;`) rồi chỉ sửa đúng các chỗ đó trong md Git — không ghi đè cả file.
- Ảnh trong FRD: chỉ chèn ảnh chính `SCR-xx-<slug>.png`; `to_docx.py` tự chèn các biến thể `SCR-xx-<slug>--<state>.png` (chèn tay sẽ bị trùng).

## 2. Quy tắc user đã chốt (chỉ dự án BBA)

1. Brainstorm từ SRS (`Document/SRS/`), thư mục workflow trên Drive, câu trả lời trên Plane (task "BBA input…" đã Done) **và tệp đính kèm của các task đó**. Không bịa; thiếu bằng chứng thì ghi OQ / AS.
2. Wireframe HTML theo bố cục EMS / BeeHive (tông xám, tên trường hợp lý). Không nhắc prototype trong thân FRD.
3. **Không đẩy Drive / Git khi user chưa nói "update …"**. Bản nháp để user review trước.
4. Drive: cập nhật tài liệu đã có → user thích **"Manage versions → Upload new version" giữ nguyên ID** (link trên Plane không đổi). Nếu buộc phải tạo file mới: chuyển file cũ vào thùng rác trước, rồi mới tải bản mới (cùng tên, cùng thư mục), ghi ID vào `_drive.json`, đổi link trên Plane.
5. Git: thay file cũ, không giữ bản nháp / bản cũ song song.
6. **Đọc Drive trước**: user có thể sửa trực tiếp trên Drive; khi đó Git đồng bộ theo Drive (ví dụ BBA-69: user đổi tiêu đề bỏ "BBA-69", nhật ký phiên bản chỉ còn "0.1 · Khởi tạo", để trống link UI Reference, bỏ ảnh, bỏ bảng giả định).
7. FRD v0.2 có mục **"9. Tài liệu tham khảo"** (bảng STT · Tài liệu · Mục · Trang · Dùng cho; số trang SRS theo bản Word gốc xuất PDF).
8. Tiếng Việt, câu ngắn; xưng "tao / mày" với user. Không in token Plane.

## 3. Drive và Plane

- Thư mục Drive Sprint 4: `1vqr-4orVQTgkA0oXESBlLpo5pVwl1PlV` · thư mục TA (tiếng Anh): `1KqkgghHymUu7T9_xco51AIjnoSufVg7_`. ID từng file: `projects/bba/_drive.json`.
- Plane: `https://plane.bba.dotb.vn/api/v1/workspaces/bba/projects/b3a74ce6-a01c-4d94-8287-7d03dd13e84e`, header `X-API-Key`. **Key không nằm trong gói này** — user đính kèm lại file CSV secret key; đọc bằng `tail -1 <csv> | awk -F, '{print $NF}'`, không in ra.
- Link tài liệu chỉ gắn trên subtask **[BA]** (seq Plane): 66→591, 67→593, 68→595, 69→597, 70→599, 71→601, 72→603, 73→605, 74→607, 75→609, 76→611, 77→613, 78→615, 79→617. Danh sách đầy đủ + issue id: `R/plane/ba_subtasks.json`, link hiện có: `R/plane/links.json`.
- Tải tệp đính kèm của một issue: `R/plane/att.py <issue_id> <thư mục ra>` (issue id của task "BBA input…" ở `R/plane/done.json`) (đặt biến `KF=<đường dẫn CSV key>`).

## 4. Tình trạng từng ticket

| Ticket | Git | Drive | Còn làm |
|---|---|---|---|
| BBA-66 Child Record Overview | v0.3 (`4a334e2`) | v0.3 `11Lv9lKo…` | Nháp delta theo Q&A: `R/frd-draft/BBA-66_Child_Record_Overview_Update_Draft.md` (payment method GIRO / GIRO CDA / PayNow, khoá định danh giấy khai sinh / hộ chiếu, OQ-OVW-16/17). Chờ user duyệt. Drive còn bản trùng tên v0.2 `1P0IpDAN…` — hỏi user có xoá không. |
| BBA-67 Read tabs | v0.7 trên Drive | `1XvEUZcj…` | Nháp delta: `R/frd-draft/BBA-67_Child_Record_Tabs_Update_Draft.md` (Withdrawn in the Parents App, Switched to …, OQ-RT-18). Chờ duyệt. |
| BBA-68 Medical alert banner | v0.2 | `1w3Q0W9J…` | Nháp US: `R/frd-draft/BBA-68_…`. **Chưa đối chiếu tệp đính kèm BBA-1058** (Appendix 1 / Appendix 3 — tải từ Plane issue BBA-1058 bằng `R/plane/att.py`): đánh giá lại 6 tháng, chỉ áp dụng sau đánh giá. Mâu thuẫn Q-69-08 ↔ BBA-1058 Q1 (theo Plane). |
| BBA-69 Allergies list | **v0.2 = bản Drive** (`ea517de`) | v0.2 `1N7O0j6u…` (user đã tải) | Xong. Còn: 3 chỗ nhắc AS-01/02/04 trong khi bảng giả định đã bỏ (giữ như Drive — hỏi user). Ghi comment tóm tắt v0.2 lên Plane [BA] 597 nếu user muốn. |
| BBA-70 Growth | v0.2 (`10b7dde`) | **vẫn v0.1** `1ztmuemed…` | Tải bản Word v0.2 lên Drive (Upload new version, giữ ID) → `_drive.json` 0.2. User hỏi có trình bày giống BBA-69 (nhật ký "Khởi tạo", để trống link, bỏ ảnh, bỏ AS) không — chưa trả lời. |
| BBA-71 Consent | **v0.2** (`1ce34a5`, gồm wireframe `consent-status-sprint4.html` + 6 PNG) | **vẫn v0.1** `1uQ4Ms_s…` | Tải bản Word v0.2 lên Drive (Upload new version, giữ ID) → `_drive.json` 0.2. OQ-10 mới (file Consent Types: "Accuracy of Information", "Outing"). |
| BBA-72 | **v0.2** (14/11/2026) | v0.2 `1ZA2NCYv…` (file mới, cũ đã vào thùng rác); Plane [BA] 603 In Review, đã tag Hai.Nguyen | Chờ Hai.Nguyen review. |
| BBA-73 | **v0.2** (14/11/2026) | v0.2 `167sUtxA…` (file mới, cũ đã vào thùng rác); Plane [BA] 605 In Review, đã tag Hai.Nguyen | Chờ Hai.Nguyen review. |
| BBA-74 → BBA-79 | v0.1 | v0.1 | Nháp US đã cập nhật theo file câu hỏi phản hồi: `R/frd-draft/BBA-7x_…_US_Draft.md`. User đang đi **từng file**: với mỗi file, kiểm tra Plane "BBA input…" liên quan **và tệp đính kèm**, chỉnh wireframe, rồi khi user gửi file Word mẫu → làm v0.2 đủ mục (1–9) theo mẫu, như BBA-69/70/71. Script mẫu: `R/code/final_70.py`, `final_71.py` (tham số: thư mục chứa `frd-draft/`, `by-frd/`, `png/` và `projects/bba`). |
| BBA-50 Approval delegation | v0.2 VI + EN | VI `1k4Qh7c_…`, EN `12GGYhBz…` | Drive còn bản cũ VI `1EhPKlTj…` và EN `1k2lwwOe…` — hỏi user có xoá không. |

Liên quan Plane khác: BBA-528 (staff clock-in → BBA-79), BBA-488 (consent), BBA-489 (term dates — tệp đính kèm "Centre Terms Setup.xlsx"), BBA-524 (District Manager → Cluster Head), BBA-529 / BBA-1059 (growth, có tệp đính kèm).

## 5. Wireframe BBA-68 → BBA-79 (nguồn chung)

- Nguồn: `R/wf_body.html` (hàm từng màn + mảng `SCREENS`) + phần `<head>` của `projects/bba/Diagram/Wireframe/_child-overview-lead-sprint4.template.html`. Dựng lại:
  ```python
  src=open('projects/bba/Diagram/Wireframe/_child-overview-lead-sprint4.template.html',encoding='utf-8').read()
  head=src[:src.index('</style>')].replace('<title>Child Record Overview — from Lead</title>','<title>BBA-68 to BBA-79 wireframes</title>',1)
  R='projects/bba/_review/sprint4-qa'
  open(R+'/BBA-68-79_wireframes.html','w',encoding='utf-8').write(head+open(R+'/wf_body.html',encoding='utf-8').read())
  ```
- Chụp PNG: `cd R && node shots.js` (Playwright có sẵn) → `R/png/<mã>--<state>.png` (PNG không lưu Git, chụp lại khi cần). Kiểm tra lỗi JS từng ticket: `node R/code/t5.js $PWD/R`.
- Tách theo ticket: `python3 R/code/split.py R` → `R/by-frd/BBA-xx/{brainstorm.md, wireframe.html}`.
- Khi một ticket xong: copy `by-frd/BBA-xx/wireframe.html` → `projects/bba/Diagram/Wireframe/<slug>-sprint4.html`; PNG nén (PIL quantize 128 màu) → `Diagram/Wireframe/png/SCR-xx-<slug>[--state].png`.

## 6. Tài liệu phân tích

- `R/BBA-66-79_brainstorm_QA.md`: brainstorm file câu hỏi phản hồi (105 câu, sheet "Tổng hợp", header dòng 8). Mapping: Q-66=BBA-66, Q-67=BBA-67, Q-69=68, Q-70=69, Q-71=70, Q-73=71, Q-74=72, Q-75=73, Q-76=74, Q-77=75, Q-80=76, Q-81=77, Q-86=78, Q-90=79. Mâu thuẫn với Plane (mới hơn) → theo Plane, ghi OQ.
- `R/BBA-68-79_brainstorm.md`: brainstorm trước đó (SRS + workflow + Plane).
- `R/qa/qa.json`, `R/qa/qa.md`: nội dung file câu hỏi phản hồi.
- `R/plane/done.md`: 26 task "BBA input…" đã Done (mô tả + comment).

## 7. Việc đầu tiên ở phiên mới

1. Kiểm tra công cụ Google Drive có trong phiên (`mcp__Google_Drive__*`).
2. Hỏi user: BBA-70, BBA-71 đã tải v0.2 lên Drive chưa (nếu Drive có công cụ thì làm luôn khi user đồng ý).
3. Tiếp tục BBA-72 theo quy trình ở mục 4.
