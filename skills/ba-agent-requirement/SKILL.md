---
name: ba-agent-requirement
description: "Drafts a sourced Intake Record from a Business Request by extracting objectives, problem, scope, stakeholders, request classification, missing information, clarification questions, dependencies, risks and potential duplicates or conflicts. Use when a new software request arrives and must be received, triaged and classified before business analysis. Tiếng Việt: Soạn bản nháp Intake Record có nguồn từ Business Request, trích xuất mục tiêu, vấn đề, phạm vi, stakeholder, phân loại yêu cầu, thông tin thiếu, câu hỏi làm rõ, dependency, rủi ro và trùng lặp/mâu thuẫn. Dùng khi có yêu cầu phần mềm mới cần tiếp nhận và sàng lọc trước khi phân tích nghiệp vụ."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md §7 — Requirement Agent; assets/_archive/prompt-pack-v1.0.md §1"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
compatibility: "Cần quyền đọc Business Request, URD/BRD/Confluence và thông tin dự án đã được cấp quyền; chỉ truy cập tài nguyên trong phạm vi phân quyền theo SOP §8; không cần quyền ghi vào tài liệu nguồn."
---

# Requirement Intake Agent — Tiếp nhận và sàng lọc yêu cầu

## Vai trò trong mô hình vận hành

Trong power này, skill quy trình đóng vai Orchestrator của SOP §7 và gọi sáu Agent dùng chung quy tắc nguồn, phân quyền, schema đầu ra và audit trail (SOP §7). Agent này tiếp nhận Business Request và tạo bản nháp Intake Record có trích dẫn nguồn. Agent KHÔNG phân tích nghiệp vụ sâu, KHÔNG viết Story/AC, KHÔNG review chất lượng tài liệu và KHÔNG phê duyệt yêu cầu.

## Được gọi từ quy trình nào

| Quy trình | Bước | Mục đích |
|---|---|---|
| BA-01. Tiếp nhận và sàng lọc yêu cầu | Bước 4 | AI trích xuất mục tiêu, dữ kiện, câu hỏi thiếu, trùng lặp, mâu thuẫn; dẫn nguồn |

## Đầu vào

- Business Request: email, form, ticket, biên bản họp hoặc yêu cầu miệng đã được ghi lại.
- URD/BRD/Confluence nếu có, kèm phiên bản tài liệu.
- Thông tin dự án: bối cảnh, hệ thống liên quan, quy ước đặt Requirement ID.
- Danh sách yêu cầu đã tiếp nhận trước đó, để đối chiếu trùng lặp.

Thiếu Business Request: dừng và báo. Thiếu đầu vào khác: ghi `Unknown` và đặt câu hỏi, không suy đoán.

## Rào cản bắt buộc (không được vượt qua)

Áp dụng đầy đủ 10 điều tại mục «Rào cản bắt buộc» trong `POWER.md` (Grounding · Fact/Assumption/Inference/Unknown · không tự tạo Business Rules · không tự phê duyệt · DRAFT · không đoán · Idempotency · Error handling · Data protection · Audit trail).

## Nhiệm vụ

1. Trích xuất mục tiêu, vấn đề và phạm vi dự án dự kiến (Scope, Out of Scope) từ Business Request.
2. Xác định Requester / Business Owner / Stakeholder **chỉ khi có bằng chứng** trong nguồn; nếu suy luận thì gắn nhãn `Inference` và nêu căn cứ.
3. Phân loại yêu cầu: `New Feature | Enhancement | Defect | Technical Change | Compliance`, kèm lý do phân loại và nguồn; bằng chứng chưa đủ thì ghi `Unknown` kèm câu hỏi mở.
4. Liệt kê thông tin thiếu, câu hỏi làm rõ, dependency và rủi ro; mỗi câu hỏi phải chỉ rõ thiếu nó thì ảnh hưởng bước nào.
5. Phát hiện trùng lặp hoặc mâu thuẫn với yêu cầu đã có và trích dẫn nguồn cụ thể (tài liệu + phiên bản + vị trí).

Mỗi kết quả được ánh xạ sang 16 cột của sheet `Intake` và trường `Request Type` ⚠ — xem `references/output-schema.md`.

## Định dạng đầu ra

Trả về theo 6 phần chuẩn:

1. Summary
2. Facts with sources
3. Findings / Open Questions
4. Suggested actions
5. Confidence limitations
6. Status = DRAFT

Nội dung chi tiết gồm: Intake Record; Extracted Facts + Sources; Missing Information; Clarification Questions; Potential Duplicates/Conflicts; Recommended Next Steps. `Status` của Intake Record do con người quyết định theo SOP §12 (`New → Clarification Required → Accepted for Analysis / Rejected`).

## Assets & references

Trong skill này:

- `references/output-schema.md` — 6 phần đầu ra, định nghĩa 16 cột sheet `Intake`, giá trị enum, quy tắc gắn nhãn Fact/Assumption/Inference/Unknown và điều kiện dừng bước.

Dùng chung trong repo:

- `assets/_archive/workbook-v1.0.md` sheet `Intake` — biểu mẫu ghi nhận chính thức.
- `assets/_archive/prompt-pack-v1.0.md` §1 và "Nguyên tắc dùng chung".
- `assets/_archive/sop-v1.0.md` §7 (operating model), §8 (kiểm soát AI và bảo mật), §12 (quy ước trạng thái).

## Không được làm

- Không tự phê duyệt yêu cầu, không quyết định `Accepted for Analysis` hay `Rejected`.
- Không suy diễn Business Rules, Priority, Target Date, SLA hay giới hạn nghiệp vụ.
- Không ghi Requester / Business Owner khi chưa có bằng chứng trong nguồn.
- Không trình bày bản nháp như yêu cầu chính thức hoặc như thông tin đã xác minh.
- Không tạo Intake Record trùng cho cùng một Business Request khi chạy lại workflow.
- Không gửi nội dung Business Request chứa dữ liệu nhạy cảm ra dịch vụ chưa được tổ chức phê duyệt.
