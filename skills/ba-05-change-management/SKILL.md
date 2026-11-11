---
name: ba-05-change-management
description: "BA-05 development support and change control: answer Dev/QA/Business questions from confirmed sources, record decisions, log Change Requests with impact analysis across stories, AC, APIs, data, test cases, documentation and Sprints, and keep the traceability matrix consistent. Use when a question arises during a Sprint, when a requirement changes mid-flight, or when an impact analysis and an approved decision record are needed. Tiếng Việt: BA-05 Hỗ trợ phát triển và quản lý thay đổi — trả lời câu hỏi của Dev/QA/Business dựa trên nguồn đã xác nhận, ghi nhận quyết định, lập Change Request kèm phân tích ảnh hưởng tới Story, AC, API, dữ liệu, Test Case, tài liệu và Sprint, giữ RTM nhất quán. Dùng khi phát sinh câu hỏi trong Sprint, khi yêu cầu thay đổi giữa chừng, hoặc khi cần phân tích ảnh hưởng và bản ghi quyết định có phê duyệt."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-05 (Quality Gate thay đổi), §5 RACI, §12"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet Change Log / BA-T05"
compatibility: "Cần quyền đọc Story/AC, tài liệu yêu cầu các phiên bản và RTM. Cần người có thẩm quyền phê duyệt thay đổi. Không tự sửa tài liệu nguồn khi chưa có quyết định."
---

# BA-05 — Hỗ trợ phát triển và quản lý thay đổi

## Mục tiêu
Bảo đảm cách hiểu nghiệp vụ nhất quán và thay đổi được kiểm soát.

## Khi nào dùng
- Dev/QA/Business đặt câu hỏi nghiệp vụ trong lúc đang phát triển.
- Có yêu cầu thay đổi phạm vi, quy tắc hoặc hành vi sau khi Story đã được xác nhận.
- Cần phân tích ảnh hưởng trước khi quyết định.
- Cần ghi nhận một quyết định để truy vết về sau.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Sprint Backlog | Có | Xác định Story đang bị ảnh hưởng |
| Story / AC | Có | Bản đã xác nhận, đúng phiên bản |
| Câu hỏi từ Dev/QA/Business | Có | Ghi nguyên văn, không diễn giải lại |
| Change Request | Nếu có | Kèm người đề xuất và lý do |
| RTM hiện hành | Có | `ba-records/<project>/rtm.md` (template: `skills/ba-03-specification/assets/rtm.md`) |

## Rào cản bắt buộc (không được vượt qua)

Áp dụng đầy đủ 10 điều tại mục «Rào cản bắt buộc» trong `POWER.md` (Grounding · Fact/Assumption/Inference/Unknown · không tự tạo Business Rules · không tự phê duyệt · DRAFT · không đoán · Idempotency · Error handling · Data protection · Audit trail).

Riêng ở BA-05: **không tự phê duyệt thay đổi**, không sửa Story/AC/tài liệu nguồn khi chưa có quyết định của người có thẩm quyền, không tự quyết định cách xử lý Sprint.

## Quy trình

### Bước 1 — Trả lời câu hỏi và ghi nhận quyết định
- Chỉ trả lời dựa trên nguồn đã xác nhận; trích dẫn cụ thể.
- Câu hỏi chưa có nguồn: trả lời `Unknown` kèm hành động xác minh, ghi vào `Open Questions` của Story/AC liên quan, **không đoán**.
- Mọi câu trả lời làm rõ hành vi đều ghi vào Decision Log.

### Bước 2 — Ghi nhận Change Request và phân tích ảnh hưởng
- Tạo `Decision/CR ID` (dạng `CR-001`); kiểm tra trùng trước khi tạo.
- Ghi `Current Requirement` và `Proposed Change` tách bạch rõ.
- Ghi `Business Reason` theo lời người đề xuất, không tự suy ra lý do.
- CR mới có `Status = Proposed`.

### Bước 3 — Xác định phạm vi ảnh hưởng
Chuyển CR sang `Under Review`. Liệt kê cụ thể, mỗi mục kèm ID:
- Story và AC bị ảnh hưởng
- Business Rules
- API / interface
- Dữ liệu (cấu trúc, giá trị hiện có, migration)
- Test Case đã viết
- Tài liệu (URD/BRD, Business Rules, hướng dẫn)
- Sprint đang chạy và Sprint kế tiếp
- Dòng RTM

Gọi `ba-agent-traceability` để so sánh phiên bản và đề xuất liên kết bị ảnh hưởng. BA kiểm tra danh sách AI đề xuất và loại bỏ liên kết suy đoán **trước khi** trình quyết định.

### Bước 4 — Quyết định và xử lý
- PO quyết định ưu tiên và cách xử lý Product Backlog.
- Scrum Team xử lý Sprint theo Scrum; BA không tự điều chỉnh Sprint Backlog.
- Ghi `Decision`, `Approver`, `Effective Version`. `Deferred` hoặc `Pending`: giữ `Status = Under Review` và ghi ngày xem lại.
- Thay đổi liên quan ngân sách, hợp đồng hoặc nghiệm thu chính thức: vượt thẩm quyền PO, phải chuyển đúng cấp theo quy định nội bộ.

### Bước 5 — BA kiểm tra và cập nhật
- Cập nhật Story/AC, Business Rules, RTM và tài liệu theo `Effective Version`.
- Gọi `ba-agent-traceability` để đối chiếu lại RTM sau cập nhật. Tuỳ chọn: gọi `ba-agent-qa-review` để rà soát tài liệu đã đổi.
- Thực hiện `Communication` tới các bên liên quan.

### Bước 6 ⚠ — Quay lại đúng điểm kiểm soát
Áp dụng mọi dòng khớp với thay đổi đã duyệt:

| Thay đổi | Quay lại | Việc phải làm |
| --- | --- | --- |
| Chỉ làm rõ, không đổi hành vi (Decision) | Không quay lại | Ghi Decision Log |
| Business Rule hoặc TO-BE | `ba-02-business-analysis` | Business xác nhận lại phần đổi, đóng lại G2 cho phần đó |
| Story hoặc AC | `ba-03-specification` Bước 5–6 | Story về `In Review`, đóng lại G3 cho phần đổi |
| Story đã qua DoR | `ba-04-refinement` | Team và PO rà lại DoR trước khi tiếp tục |
| Test Case | `ba-06-test-uat` | QA cập nhật Test Case, dòng RTM mới về `Not Run`, retest |

CR chỉ chuyển `Implemented` khi các điểm kiểm soát trên đã xong.

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| Decision Log | `assets/decision-log-cr.md` — phần Decision |
| Change Request | `assets/decision-log-cr.md` — khớp sheet `Change Log` (13 cột) |
| Impact Analysis | cột `Impact Analysis` của CR |
| Tài liệu cập nhật | Story/AC, Business Rules, RTM theo phiên bản mới |

Chuỗi trạng thái CR (SOP §12): `Proposed` → `Under Review` → `Approved` / `Rejected` → `Implemented`.

## Quality Gate thay đổi
Chi tiết tại `references/quality-gate-change.md`. Tóm tắt — một thay đổi chỉ được coi là đã kiểm soát khi có đủ:
- [ ] Người quyết định
- [ ] Lý do
- [ ] Phiên bản hiệu lực
- [ ] Thông báo tới các bên bị ảnh hưởng
- [ ] Truy vết thay đổi (RTM và tài liệu đã cập nhật)

## RACI
| BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- |
| R | A* | C | C | C |

`A*` — SOP giả định PO được ủy quyền quản lý phạm vi Product Backlog. Ngân sách, hợp đồng và nghiệm thu chính thức vẫn tuân thủ thẩm quyền nội bộ.

## Assets & references
- `assets/decision-log-cr.md` — template Decision Log và Change Request.
- `references/quality-gate-change.md` — gate thay đổi, quy tắc phân tích ảnh hưởng và quy tắc dừng bước.
- RTM dùng chung: `skills/ba-03-specification/assets/rtm.md`.
- Skill liên quan: `ba-agent-traceability` (Bước 3, Bước 5), `ba-agent-qa-review` (Bước 5, tuỳ chọn).
- Đây là luồng theo sự kiện, không phải một chặng cố định: gọi được từ BA-03 trở đi khi có câu hỏi hoặc thay đổi; không có thay đổi thì bỏ qua. Sau khi xong, quay lại theo Bước 6.
