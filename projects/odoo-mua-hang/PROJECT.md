# Quy trình mua hàng trên Odoo (`odoo-mua-hang`)

<!-- card:start -->
> Sinh bởi `python tools/project.py card odoo-mua-hang` — không sửa tay đoạn này. Đọc thẻ này TRƯỚC khi mở tài liệu lớn.

- Phiên bản: SRS 0.3 · URD 0.3 · UC 0.3 · backlog 0.3
- Mã: 27 US · 19 UC · 27 FR · 10 NFR · 12 SCR · 50 AS · 41 OQ
- OQ mở (29): OQ-03, OQ-10, OQ-12, OQ-13, OQ-14, OQ-15, OQ-17, OQ-18, OQ-19, OQ-20, OQ-21, OQ-22, OQ-24, OQ-25, OQ-26, OQ-27, OQ-28, OQ-29, OQ-30, OQ-31, OQ-32, OQ-34, OQ-35, OQ-36, OQ-37, OQ-38, OQ-39, OQ-40, OQ-41 · trả lời một phần: OQ-02, OQ-05, OQ-07, OQ-08, OQ-09, OQ-23
- Lần cập nhật cuối: 0.3 (2026-10-20) — Trả lời câu hỏi mở lần 1: Odoo 17 Odoo.sh/on-premise; không gộp YCMH; đơn mua không ngưỡng; YCMH bị từ chối về Nháp + email. Khảo sát lần 3 — Yêu cầu báo giá: D
- Màn chờ vẽ lại: không
- Drive: chưa gắn link thư mục gốc · 12 file đã đẩy
- File: Document/SRS/SRS.md (964 dòng), Document/URD/URD.md (421 dòng), Document/Use_Case/UC.md (706 dòng), Document/Backlog/backlog.md (382 dòng), Diagram/Wireframe/flows.md (229 dòng) — SRS chưa tách srs/
- Commit cuối: 2026-11-09 refactor: nhiều dự án một repo — projects/<du-an>/Document/<loại>/ + Diagram/; Drive luôn Word, hỏi thư mục m

## Bản đồ file

| Cần | Mở | Ghi chú |
|---|---|---|
| Biên bản / tài liệu khảo sát | `Document/Bien_Ban_Khao_Sat/` (`_tong-hop.md` là bản hợp nhất — nguồn ưu tiên) | Lịch sử nạp: `_manifest.md`, `_changes/` — đọc change report mới nhất |
| URD (+ brainstorm) | `Document/URD/` | `grep -n "^#### US-07"` rồi Read đoạn đó |
| SRS | `Document/SRS/SRS.md` (nguồn `Document/SRS/srs/*.md`) | Tra mã → file: `build_srs.py <du-an> --index`; Read theo offset |
| FSD | `Document/FSD/` (theo sprint: `FSD/Sprint <n>/`) | `grep -n "^#### "` để xem mục |
| Use case / Backlog | `Document/Use_Case/UC.md`, `Document/Backlog/backlog.md` | |
| Test case | `Document/Test_Case/` (theo sprint: `Test_Case/Sprint <n>/`) | Ma trận phủ ở mục 6 |
| Mã gốc của khách (nếu nhập URD/FSD) | `Document/doi-chieu-ma.md` | `grep -n "REQ-012"` → mã mới |
| Sơ đồ | `Diagram/Flow/` (`swimlanes/*.json` là nguồn) | |
| Màn hình | `Diagram/Wireframe/flows.md`, `screens/SCR-xx-*.html` | Chỉ mở ảnh `png/` khi cần review |
| File Word / CSV xuất ra | `.output/` (không commit) | Đẩy lên Drive: hỏi link thư mục mỗi lần |

## Google Drive

- Backlog/backlog: https://docs.google.com/spreadsheets/d/1adOzG2a-ytG_RZHqpYfsegqXU2HtSkSJI7hVE0m9_Ho/edit
- Diagram/Flow/swimlane-01-yeu-cau-mua-hang.png: https://drive.google.com/file/d/1Zd24FmUpYtKqxpGSCjjViDFMNg2aDnS_/view
- Diagram/Flow/swimlane-02-yeu-cau-bao-gia-po.png: https://drive.google.com/file/d/1XwNBAhnNLvM348XXWnLM1sSelisJNMQf/view
- Diagram/Flow/swimlane-03-dich-vu.png: https://drive.google.com/file/d/1EC23PV83uAZnzEE6ufta3eW_ZwTJaKwH/view
- Diagram/Flow/uc-01.png: https://drive.google.com/file/d/1L17q4pBVK44awShIxkQBu2MXEmpif0sX/view
- Diagram/Flow/uc-02.png: https://drive.google.com/file/d/1Rp4oeXb90NDoDH5nSrp5pM8BW8fn1lgE/view
- Diagram/Flow/uc-03.png: https://drive.google.com/file/d/1-hd1oEGARw81R1jfXJp2uh6KAInf6Xo8/view
- Diagram/Flow/uc-04.png: https://drive.google.com/file/d/1l3pg5A1Wpa_gu44rxvWxwHWwbl4Mb2UJ/view
- Diagram/Flow/uc-05.png: https://drive.google.com/file/d/1wUauJyugBYGq1uVWi-yHDfHKr6KTdD3A/view
- SRS/SRS: https://docs.google.com/document/d/1S25a37GVKYYSSZtl1bKr_IsBpqnW_yFplYplyYy-_kg/edit
- URD/URD: https://docs.google.com/document/d/1MZNt5WJV8ojA-_PdewIwQBTxsxWAuURA0C_SeJvaJOQ/edit
- Use_Case/UC: https://docs.google.com/document/d/1CpzMgFVcUjgtdQ6kjVUQYajHib7f8EDTY76fQTUwlbM/edit

<!-- card:end -->

## Ghi chú (viết tay — giữ nguyên khi sinh lại thẻ)

-
