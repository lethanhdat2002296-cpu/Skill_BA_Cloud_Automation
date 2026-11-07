# Product Backlog — {{Tên dự án}}

| Thuộc tính | Giá trị |
|---|---|
| Mã dự án | {{du-an}} |
| Phiên bản | {{0.1 — cùng phiên bản SRS}} |
| Ngày | {{YYYY-MM-DD}} |
| Nguồn | {{URD.md v…; UC.md v…; SRS.md v…}} |
| Thang điểm | Fibonacci 1, 2, 3, 5, 8, 13 — story mốc 3 điểm: {{US-xx — tên}} |

## 1. Quy ước
- Story point đo **độ lớn tương đối** (khối lượng + độ phức tạp + rủi ro), không đo giờ.
- Story > 8 điểm phải tách trước khi đưa vào sprint; 13 điểm chỉ chấp nhận tạm ở release sau.
- Ưu tiên MoSCoW lấy từ URD; thứ tự trong release theo phụ thuộc rồi ưu tiên.

## 2. Epic

| Epic | Tên | Mục tiêu (đo được) | User story | Release | Tổng điểm |
|---|---|---|---|---|---|
| EP-01 | {{…}} | {{…}} | {{US-01, US-02}} | R1 | {{8}} |

## 3. Story theo epic

### EP-01 — {{Tên epic}}

#### US-01 — {{Tên story}}
- **Story:** Là {{vai trò}}, tôi muốn {{hành động}}, để {{giá trị}}.
- **Epic:** EP-01 · **Ưu tiên:** {{Must}} · **Story point:** {{5}} · **Release:** {{R1}}
- **Căn cứ ước lượng:** {{1 form mới, 4 quy tắc, 1 tích hợp email}}
- **Truy vết:** {{UC-01 · FR-01, FR-24 · SCR-01, SCR-02}}
- **Phụ thuộc:** {{US-22 | Không có}}
- **Acceptance criteria:**
  1. **Given** {{…}} **When** {{…}} **Then** {{…}}.

#### US-07 — {{Story lớn đã tách}}
- **Story:** Là {{…}}, tôi muốn {{…}}, để {{…}}.
- **Epic:** EP-01 · **Ưu tiên:** {{Must}} · **Release:** {{R1}}
- **Đã tách thành:** US-07.1, US-07.2

#### US-07.1 — {{Lát mỏng thứ nhất}}
- **Story:** Là {{…}}, tôi muốn {{…}}, để {{…}}.
- **Tách từ:** US-07 — {{luồng theo lát mỏng end-to-end}}
- **Epic:** EP-01 · **Ưu tiên:** {{Must}} · **Story point:** {{3}} · **Release:** {{R1}}
- **Truy vết:** {{UC-03 · FR-06 · SCR-05}}
- **Phụ thuộc:** {{Không có}}
- **Acceptance criteria:**
  1. **Given** {{…}} **When** {{…}} **Then** {{…}}.

## 4. Kế hoạch phát hành

| Release | Mục tiêu | Epic | Story | Tổng điểm |
|---|---|---|---|---|
| R1 (MVP) | {{chạy được luồng … end-to-end}} | {{EP-01, EP-02}} | {{n}} | {{…}} |

## 5. Definition of Ready / Definition of Done

**Ready** (đưa vào sprint khi đủ):
- Story theo mẫu Là / tôi muốn / để; có ≥ 2 AC Given/When/Then, có ít nhất 1 AC ngoại lệ.
- Có truy vết FR (và SCR nếu có UI); wireframe màn liên quan đã được khách xem.
- Story point ≤ 8; phụ thuộc đã xong hoặc cùng sprint.
- Không còn OQ chặn story (OQ liên quan đã trả lời hoặc có AS được chấp nhận).

**Done:**
- Mọi AC đạt khi kiểm thử trên môi trường test; không còn lỗi mức nghiêm trọng.
- Code review xong; có dữ liệu mẫu và hướng dẫn cấu hình (nếu có).
- Tài liệu (SRS / hướng dẫn sử dụng) cập nhật nếu hành vi khác đặc tả.
- PO / khách hàng xác nhận demo.

## 6. Assumptions & Open Questions (phát sinh khi lập backlog)

### 6.1 Giả định
| Mã | Giả định | Lý do chọn | Liên quan |
|---|---|---|---|
| {{AS-xx}} | {{…}} | {{…}} | {{EP-xx, US-xx}} |

### 6.2 Câu hỏi mở
| Mã | Câu hỏi | Người cần trả lời | Liên quan |
|---|---|---|---|
| {{OQ-xx}} | {{…}} | {{…}} | {{US-xx}} |
