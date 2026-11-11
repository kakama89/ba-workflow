---
name: ba-03-specification
description: "BA-03 requirement specification and confirmation: break down Epic/Feature/User Story, write testable Acceptance Criteria in Given-When-Then, cover validation, data, states, permissions, messages and NFR, link Requirement IDs and Business Rule IDs, then run AI drafting and human review. Use when analysis has passed gate G2 and requirements must be turned into developable, testable stories with a traceability matrix. Tiếng Việt: BA-03 Đặc tả và xác nhận yêu cầu — phân rã Epic/Feature/User Story, viết Acceptance Criteria kiểm chứng được theo Given-When-Then, mô tả validation, dữ liệu, trạng thái, quyền, thông báo và NFR, liên kết Requirement ID và Business Rule ID, sau đó AI tạo bản nháp và con người review. Dùng khi phân tích đã qua gate G2 và cần chuyển nhu cầu thành Story phát triển và kiểm thử được, kèm ma trận truy vết."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-03, Quality Gate G3, §12"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet User Story AC / BA-T03, sheet RTM / BA-T04"
compatibility: "Cần tài liệu phân tích đã đạt G2, Business Rules Catalog có nguồn, và quyền ghi vào hệ thống quản lý backlog. Cần Dev/Tech Lead và QA tham gia review."
---

# BA-03 — Đặc tả và xác nhận yêu cầu

## Mục tiêu
Chuyển nhu cầu thành yêu cầu rõ ràng, có thể phát triển và kiểm thử.

## Khi nào dùng
- Tài liệu phân tích đã đạt Quality Gate G2.
- Cần phân rã Epic/Feature thành Story và viết Acceptance Criteria.
- Story cũ viết lại vì không kiểm thử được hoặc thiếu luồng ngoại lệ.
- Quay lại từ BA-05 sau khi CR được duyệt: chạy Bước 5–6 và G3 cho phần Story/AC thay đổi.

Không dùng skill này để ước lượng Story Point hay xếp thứ tự ưu tiên — việc đó thuộc `ba-04-refinement` và thẩm quyền của Team/PO.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Kết quả phân tích | Có | Business Analysis Document đạt G2 |
| Business Rules Catalog | Có | Mỗi quy tắc có ID và nguồn |
| Process Flow | Có | AS-IS/TO-BE đã được Business xác nhận |
| Mục tiêu Product | Có | Để kiểm tra Story có phục vụ đúng mục tiêu |
| Requirement ID từ BA-01 | Có | Dùng để liên kết truy vết |

## Rào cản bắt buộc (không được vượt qua)

Áp dụng đầy đủ 10 điều tại mục «Rào cản bắt buộc» trong `POWER.md` (Grounding · Fact/Assumption/Inference/Unknown · không tự tạo Business Rules · không tự phê duyệt · DRAFT · không đoán · Idempotency · Error handling · Data protection · Audit trail).

Riêng ở BA-03: **không tự tạo yêu cầu mới ngoài phạm vi đã phân tích**, không quyết định Priority/Story Point, không phê duyệt DoR.

## Quy trình

### Bước 1 — Phân rã Epic / Feature / User Story
- Chỉ phân rã khi cần; Story phải đủ nhỏ để hoàn tất trong một Sprint.
- Mỗi Story thuộc đúng một Epic; ghi `Epic ID`.
- Nếu phải tách Story vì thiếu thông tin, ghi lý do vào `Open Questions`.

### Bước 2 — Viết User Story và Acceptance Criteria
- Story theo dạng `As a / I want / So that`, thể hiện Actor, nhu cầu và giá trị.
- AC theo `Given / When / Then` khi phù hợp; mỗi AC một `AC ID` (dạng `AC-01`).
- AC phải **kiểm chứng được**: có điều kiện đầu vào, hành động và kết quả quan sát được.

### Bước 3 — Mô tả chi tiết hành vi
Bao phủ khi áp dụng: validation, dữ liệu, trạng thái, quyền, thông báo, lỗi và NFR.
Mỗi luồng chính cần ít nhất một trường hợp lỗi hoặc ngoại lệ có căn cứ.

### Bước 4 — Liên kết truy vết
- Gắn `Requirement IDs` và `Business Rule IDs` cho từng Story/AC.
- Ghi nguồn cho các AC suy ra từ quy tắc nghiệp vụ.
- Tạo dòng RTM **nháp** trong `ba-records/<project>/rtm.md` theo template `assets/rtm.md`, ghi `Notes = Nháp - chờ xác nhận`.

### Bước 5 — AI tạo bản nháp và kiểm tra
Gọi skill `ba-agent-specification`. Agent kiểm tra mơ hồ, thiếu luồng, trùng lặp và mâu thuẫn, nhưng **không tự thêm quy tắc**.
Sau đó gọi `ba-agent-qa-review` để rà soát độc lập trước khi đưa ra Team.

### Bước 6 — Review và xác nhận
- BA review toàn bộ nội dung AI tạo, rồi chuyển Story sang `In Review`.
- Dev/Tech Lead đánh giá khả thi; QA đánh giá testability.
- PO/Business xác nhận theo thẩm quyền; cập nhật `Version` ⚠, `Confirmed By / Date` ⚠ và `Review Status`.
- Bỏ ghi chú nháp ở dòng RTM tương ứng.

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| User Story + AC | `assets/user-story-ac.md` — khớp sheet `User Story AC` (18 cột), thêm các trường ⚠ |
| RTM | `assets/rtm.md` — khớp sheet `RTM` (10 cột), dùng chung với BA-06/BA-07 |
| URD/BRD hoặc đặc tả phù hợp | Cập nhật từ Business Analysis Document |
| Decision Log | Dùng BA-T05 qua skill `ba-05-change-management` khi có quyết định thay đổi |

Chuỗi trạng thái Story (SOP §12, thêm `Ready for Sprint` ⚠): `Draft` → `In Review` → `Ready for Refinement` → `Ready for Sprint` → `Selected for Sprint` → `In Progress` → `Done`. Người chuyển từng trạng thái: xem `POWER.md`.

## Quality Gate G3
Chi tiết tại `references/quality-gate-g3.md`. Tóm tắt:
- [ ] AC kiểm thử được
- [ ] Không che giấu giả định
- [ ] Có xác nhận của người có thẩm quyền
- [ ] Có phiên bản tài liệu
- [ ] ⚠ Tỷ lệ AC testable = 100 %
- [ ] ⚠ Câu hỏi mở Critical/Major = 0

Đạt G3 thì Story chuyển `Ready for Refinement`. Không đạt G3 thì Story chưa được vào refinement.

## RACI
| BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- |
| R | A | C | C | C |

## Assets & references
- `assets/user-story-ac.md` — template Story và Acceptance Criteria.
- `assets/rtm.md` — template Requirement Traceability Matrix; **dùng chung**, được `ba-06-test-uat`, `ba-07-release-handover`, `ba-agent-test-design` và `ba-agent-traceability` tham chiếu.
- `references/quality-gate-g3.md` — checklist G3, tiêu chí AC kiểm thử được và quy tắc dừng bước.
- Skill liên quan: `ba-agent-specification` (Bước 5), `ba-agent-qa-review` (Bước 5).
- Quy trình trước: `ba-02-business-analysis`. Kế tiếp: `ba-04-refinement`.
