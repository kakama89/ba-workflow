---
name: ba-02-business-analysis
description: "BA-02 business investigation and analysis: identify stakeholders and actors, describe AS-IS and TO-BE processes from evidence, build a sourced Business Rules Catalog, classify functional and non-functional requirements, map alternative and error flows, data, integrations, dependencies and risks. Use when an intake record has passed gate G1 and the problem, current process and business rules need to be understood and confirmed before specification. Tiếng Việt: BA-02 Khảo sát và phân tích nghiệp vụ — xác định stakeholder và actor, mô tả AS-IS/TO-BE dựa trên bằng chứng, lập Business Rules Catalog có nguồn, phân loại FR và NFR, xác định luồng thay thế và luồng lỗi, dữ liệu, tích hợp, dependency và rủi ro. Dùng khi yêu cầu đã qua gate G1 và cần hiểu rõ vấn đề, quy trình hiện tại, quy tắc nghiệp vụ trước khi đặc tả."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-02, Quality Gate G2"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet Analysis / BA-T02"
compatibility: "Cần quyền đọc tài liệu nghiệp vụ, dữ liệu mẫu và mô tả hệ thống/API đã được cấp phép. Cần lịch trao đổi với Business để xác nhận TO-BE và quy tắc nghiệp vụ."
---

# BA-02 — Khảo sát và phân tích nghiệp vụ

## Mục tiêu
Hiểu vấn đề, quy trình hiện tại, quy trình mong muốn và các quy tắc nghiệp vụ.

## Khi nào dùng
- Intake Record đã đạt Quality Gate G1 và có `Status = Accepted for Analysis`.
- Cần dựng AS-IS/TO-BE và Business Rules Catalog có nguồn trước khi viết Story.
- Có thay đổi lớn làm tài liệu phân tích cũ không còn đúng.

Không dùng skill này để viết User Story/AC — đó là `ba-03-specification`.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Yêu cầu đã sàng lọc | Có | Intake Record đạt G1, `Status = Accepted for Analysis` |
| Tài liệu nghiệp vụ | Có | URD/BRD/quy trình/quy định, kèm phiên bản |
| Dữ liệu mẫu | Nếu có | Chỉ dùng dữ liệu được phép truy cập |
| Hệ thống / API liên quan | Nếu có | Ghi rõ môi trường và quyền truy cập |
| Đầu mối trả lời nghiệp vụ | Có | Người có thẩm quyền xác nhận quy tắc |

## Rào cản bắt buộc (không được vượt qua)

Áp dụng đầy đủ 10 điều tại mục «Rào cản bắt buộc» trong `POWER.md` (Grounding · Fact/Assumption/Inference/Unknown · không tự tạo Business Rules · không tự phê duyệt · DRAFT · không đoán · Idempotency · Error handling · Data protection · Audit trail).

Riêng ở BA-02: **không tự tạo chính sách, giới hạn hoặc SLA**. Mọi Business Rule phải có ID và nguồn.

## Quy trình

### Bước 1 — Xác định Stakeholder, Actor, mục tiêu và phạm vi
- Liệt kê stakeholder theo vai trò, không theo tên cá nhân nếu không cần thiết.
- Xác định Actor tương tác trực tiếp với hệ thống và quyền của từng Actor.
- Chốt `Business Objective` đo lường được và ranh giới `Scope`.

### Bước 2 — Mô tả AS-IS, vấn đề, điểm nghẽn và đề xuất TO-BE
- AS-IS chỉ mô tả những gì có bằng chứng.
- Điểm nghẽn ghi kèm tác động, không ghi cảm nhận.
- TO-BE là **đề xuất** cho tới khi Business xác nhận.

### Bước 3 — Lập Business Rules Catalog và các luồng
- Mỗi quy tắc một ID (workbook dùng dạng `BR-001`) kèm nguồn.
- Xác định luồng chính, luồng thay thế, luồng lỗi và ngoại lệ.
- Quy tắc chưa xác minh được nguồn: gắn `[Unknown]` và tạo câu hỏi mở.

### Bước 4 — Phân loại yêu cầu
- Functional Requirements (`FR-001`…), NFR (`NFR-001`…), dữ liệu, quyền và tích hợp.
- NFR chỉ ghi khi nguồn hoặc ràng buộc kỹ thuật đã nêu; không tự đặt ngưỡng.

### Bước 5 — Đánh giá dependency, rủi ro và ảnh hưởng hệ thống
- Ghi dependency kèm hệ thống/nhóm sở hữu.
- Rủi ro nêu tác động và dấu hiệu nhận biết, không tự đề xuất mức chấp nhận rủi ro.

### Bước 6 — AI đối chiếu và BA xác minh
- Gọi skill `ba-agent-analysis` để đối chiếu tài liệu, gợi ý điểm thiếu và mâu thuẫn.
- BA xác minh lại với Business trước khi đưa vào tài liệu chính thức.
- Gọi `ba-agent-qa-review` để rà soát tài liệu trước khi đóng G2 (bắt buộc).
- Ghi `Review Status = Draft` cho tới khi có xác nhận.

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| Business Analysis Document | `assets/business-analysis-doc.md` — khớp sheet `Analysis` (19 cột) |
| Stakeholder Map | mục `Stakeholders` của tài liệu |
| Process Flow (AS-IS / TO-BE) | mục `AS-IS`, `TO-BE` |
| Business Rules Catalog | mục `Business Rules`, mỗi quy tắc một ID + nguồn |
| Requirements (FR/NFR) | mục `Functional Requirements`, `NFR` |
| Risks / Dependencies / Open Questions | các mục tương ứng |
| Source References | mục `Source References` — URL + vị trí trong tài liệu |

## Quality Gate G2
Chi tiết tại `references/quality-gate-g2.md`. Tóm tắt:
- [ ] Mọi Business Rule đều có nguồn
- [ ] Giả định được đánh dấu rõ ràng
- [ ] Business đã xác nhận TO-BE
- [ ] Mỗi câu hỏi mở đều có owner

Không đạt G2 thì không chuyển sang BA-03.

## RACI
| BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- |
| R | A | C | C | C |

## Assets & references
- `assets/business-analysis-doc.md` — template tài liệu phân tích nghiệp vụ.
- `references/quality-gate-g2.md` — checklist G2, quy tắc gắn nhãn bằng chứng và quy tắc dừng bước.
- Skill liên quan: `ba-agent-analysis` (Bước 6), `ba-agent-qa-review` (Bước 6, bắt buộc).
- Quy trình trước: `ba-01-requirement-intake`. Kế tiếp: `ba-03-specification`.
