---
name: ba-04-refinement
description: "BA-04 backlog refinement and Sprint preparation: prepare stories and open questions, have the PO clarify value and order, have Dev/Tech Lead assess feasibility and dependencies and QA assess testability, split and estimate as a team, then run an AI checklist review. Use when stories that passed gate G3 need to be made ready for a Sprint, when a Definition of Readiness check is required, or when a story is too large to finish in one Sprint. Tiếng Việt: BA-04 Refinement và chuẩn bị Sprint — BA chuẩn bị nội dung và câu hỏi mở, PO làm rõ giá trị và thứ tự ưu tiên, Dev/Tech Lead đánh giá khả thi và dependency, QA đánh giá testability, Team chia nhỏ và ước lượng, sau đó AI rà soát checklist. Dùng khi Story đã qua gate G3 cần đưa vào Sprint, khi cần kiểm tra Definition of Readiness, hoặc khi Story quá lớn không hoàn tất được trong một Sprint."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-04 (DoR tham khảo), §5 RACI"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
compatibility: "Cần Product Backlog, Story/AC đã đạt G3, Product Goal và thông tin năng lực dự kiến của Team. Cần phiên refinement có BA, PO, Dev/Tech Lead và QA."
---

# BA-04 — Refinement và chuẩn bị Sprint

## Mục tiêu
Giúp Scrum Team hiểu yêu cầu, chia nhỏ công việc và đánh giá khả năng hoàn thành.

## Khi nào dùng
- Story đã đạt G3 và cần đưa vào Sprint.
- Story quá lớn, không hoàn tất được trong một Sprint.
- Cần rà soát Definition of Readiness trước Sprint Planning.
- Dependency mới phát hiện làm thay đổi thứ tự công việc.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Product Backlog | Có | Story đã đạt G3 |
| Story / AC | Có | Theo `skills/ba-03-specification/assets/user-story-ac.md` |
| Dependency | Có | Dependency chưa chốt là rủi ro cho Sprint |
| Product Goal | Có | Để PO làm rõ giá trị và thứ tự |
| Năng lực dự kiến | Có | Do Team cung cấp, không do BA suy đoán |

## Rào cản bắt buộc (không được vượt qua)

1. **Grounding** — mọi kết luận quan trọng phải kèm nguồn; nếu chưa xác minh thì ghi rõ "chưa xác minh".
2. **Fact / Assumption / Inference / Unknown** — phân loại tường minh, không trộn lẫn.
3. **Không tự tạo Business Rules**, không tự đặt Priority, Story Point, SLA hay giới hạn nghiệp vụ.
4. **Không tự phê duyệt** — DoR, nghiệm thu, thay đổi phạm vi đều thuộc thẩm quyền con người.
5. **Mọi đầu ra là DRAFT** cho đến khi người có thẩm quyền review.
6. **Thiếu đầu vào thì hỏi, không đoán.**
7. **Idempotency** — kiểm tra bản ghi đã tồn tại trước khi tạo mới; không sinh Story/Comment/Record trùng khi chạy lại.
8. **Error handling** — nguồn lỗi, schema sai hoặc thiếu dữ liệu: dừng bước và báo, không tự chế dữ liệu thay thế.
9. **Data protection** — không gửi bí mật hoặc dữ liệu nhạy cảm tới dịch vụ chưa được tổ chức phê duyệt.
10. **Audit trail** — ghi lại prompt version, model/version, tài liệu đầu vào, đầu ra, người review và quyết định.

Riêng ở BA-04: **BA và AI không ước lượng, không quyết định Priority, không tuyên bố Story đã Ready.** Estimate do Team thống nhất; thứ tự do PO quyết định.

## Quy trình

### Bước 1 — BA chuẩn bị nội dung và câu hỏi còn mở
- Rà soát Story/AC, gom các `Open Questions` chưa đóng.
- Chuẩn bị ngữ cảnh nghiệp vụ và nguồn để trả lời nhanh trong phiên.
- Đánh dấu Story có dấu hiệu quá lớn hoặc phụ thuộc chéo.

### Bước 2 — PO làm rõ giá trị và thứ tự ưu tiên
- PO trình bày giá trị và lý do xếp thứ tự.
- Ghi nhận thay đổi thứ tự; BA không tự điều chỉnh.

### Bước 3 — Dev/Tech Lead và QA đánh giá
- Dev/Tech Lead: khả thi, ràng buộc kiến trúc, dependency kỹ thuật.
- QA: testability của từng AC, dữ liệu và môi trường kiểm thử cần có.
- Ghi lại các điểm không khả thi để điều chỉnh Story.

### Bước 4 — Team chia nhỏ Story và ước lượng
- Chia nhỏ theo cách Team thống nhất; mỗi Story mới phải giữ liên kết `Requirement ID` và `AC ID`.
- Ước lượng theo phương pháp của Team. BA ghi nhận, không đề xuất con số.
- Sau khi chia, cập nhật `ba-records/<project>/rtm.md` theo template `skills/ba-03-specification/assets/rtm.md`.

### Bước 5 — AI rà soát checklist
Gọi `ba-agent-qa-review` để rà DoR và gợi ý câu hỏi; gọi `ba-agent-traceability` nếu có Story bị tách để kiểm tra liên kết.
Con người xác nhận từng gợi ý; AI không tự đánh dấu Ready.

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| Backlog được làm rõ | Cập nhật Story/AC trong hệ thống backlog |
| Estimate do Team thống nhất | Do Team ghi; BA không điền thay |
| Dependency và trạng thái sẵn sàng | `assets/dor-checklist.md` |

Story vào BA-04 ở `Ready for Refinement` và chuyển sang `Ready for Sprint` ⚠ khi Team và PO kết luận đạt DoR. Không đạt thì giữ `Ready for Refinement`, trừ khi PO chấp nhận rủi ro và ghi Decision Log. Việc chuyển sang `Selected for Sprint` diễn ra ở Sprint Planning.

## Definition of Readiness
BA-04 **không có Quality Gate đánh số** trong SOP; thay vào đó dùng DoR tham khảo.
Chi tiết và cách áp dụng tại `assets/dor-checklist.md`.

SOP ghi rõ DoR này **không bắt buộc theo Scrum Guide** — chỉ là khung tham khảo nội bộ, cần ánh xạ với quy ước của Team.

## RACI
| BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- |
| R | A | R | R | C |

Xem phân giải chi tiết tại `references/raci-refinement.md`.

## Assets & references
- `assets/dor-checklist.md` — Definition of Readiness tham khảo và biên bản phiên refinement.
- `references/raci-refinement.md` — ai quyết định gì trong refinement, các tình huống ranh giới.
- Skill liên quan: `ba-agent-qa-review` (Bước 5), `ba-agent-traceability` (Bước 5, khi có Story bị tách).
- Quy trình trước: `ba-03-specification`. Kế tiếp: Sprint, rồi `ba-06-test-uat` khi có build. Phát sinh câu hỏi hoặc thay đổi: `ba-05-change-management`.
