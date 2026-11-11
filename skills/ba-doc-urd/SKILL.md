---
name: ba-doc-urd
description: "Create a User Requirements Document (URD) from analysed requirements: consolidate user profiles, user goals, use cases, user scenarios, UI/UX requirements, usability criteria, user acceptance criteria and accessibility requirements into a formal URD with full source traceability. Use when the analysis has passed gate G2 and the project needs a formal URD to describe requirements from the end-user perspective before or alongside specification. Tiếng Việt: Tạo tài liệu URD (User Requirements Document) từ kết quả phân tích: tổng hợp hồ sơ người dùng, mục tiêu người dùng, use case, kịch bản sử dụng, yêu cầu UI/UX, tiêu chí khả dụng, tiêu chí chấp nhận của người dùng và yêu cầu accessibility thành tài liệu URD chính thức có truy vết nguồn đầy đủ. Dùng khi phân tích đã qua gate G2 và dự án cần URD chính thức để mô tả yêu cầu từ góc nhìn người dùng cuối trước hoặc song song với đặc tả."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-02, BA-03; Quality Gate G2"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet Analysis / BA-T02"
compatibility: "Cần kết quả phân tích nghiệp vụ (Business Analysis Document) đã đạt G2, Stakeholder Map và thông tin Actor, Process Flow đã xác nhận. Cần người dùng đại diện hoặc Business xác nhận nội dung URD trước khi phê duyệt."
---

# BA-DOC-URD — Tạo tài liệu User Requirements Document (URD)

## Mục tiêu
Tổng hợp yêu cầu từ góc nhìn người dùng cuối thành tài liệu URD chính thức, mô tả rõ ai dùng hệ thống, dùng để làm gì, kịch bản sử dụng và tiêu chí chấp nhận từ phía người dùng, phục vụ đặc tả chi tiết và thiết kế UX.

## Khi nào dùng
- Tài liệu phân tích nghiệp vụ (Business Analysis Document) đã đạt Quality Gate G2.
- Dự án yêu cầu có URD chính thức để mô tả yêu cầu từ góc nhìn người dùng.
- Cần tài liệu để thiết kế UI/UX dựa trên nhu cầu thực của người dùng.
- Cần URD để làm cơ sở cho User Acceptance Testing (UAT) ở BA-06.
- Dự án có nhiều nhóm người dùng với nhu cầu khác nhau, cần phân biệt rõ.

Không dùng skill này khi:
- Chưa có kết quả phân tích đạt G2 — quay lại `ba-02-business-analysis`.
- Cần viết User Story/AC chi tiết — đó là `ba-03-specification`.
- Cần tài liệu yêu cầu nghiệp vụ tổng thể — dùng `ba-doc-brd`.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Business Analysis Document | Có | Đã đạt G2, có Stakeholder Map và Actor |
| Stakeholder Map | Có | Vai trò, mối quan tâm, mức ảnh hưởng |
| Process Flow (AS-IS / TO-BE) | Có | Đặc biệt là TO-BE đã được Business xác nhận |
| Functional Requirements (FR) | Có | Mỗi FR có ID và liên kết Requirement ID |
| Intake Record(s) | Có | Để truy vết về yêu cầu gốc |
| Thông tin về người dùng | Có | Vai trò, đặc điểm, bối cảnh sử dụng — từ nguồn hoặc từ trao đổi với Business |
| Tài liệu UI/UX hiện có | Nếu có | Wireframe, mockup, design system, kèm phiên bản |
| Kết quả khảo sát / phỏng vấn người dùng | Nếu có | Biên bản có ngày và người tham gia |

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

Riêng ở BA-DOC-URD: **không tự tạo persona hay user profile giả**, không tự suy diễn hành vi người dùng khi chưa có bằng chứng, không tự đặt tiêu chí usability khi nguồn chưa nêu.

## Quy trình

### Bước 1 — Kiểm tra đầu vào và xác nhận phạm vi
- Xác nhận Business Analysis Document đã đạt G2.
- Kiểm tra URD đã tồn tại cho cùng phạm vi chưa; nếu có, cập nhật và tăng `Version` thay vì tạo mới.
- Xác nhận danh sách nguồn và phiên bản tài liệu đầu vào.
- Xác nhận danh sách Actor từ Business Analysis Document.

### Bước 2 — Xây dựng User Profile
- Từ Stakeholder Map và thông tin Actor, lập hồ sơ cho từng nhóm người dùng.
- Mỗi User Profile ghi: vai trò, đặc điểm, bối cảnh sử dụng, tần suất, mục tiêu chính.
- Chỉ ghi thông tin có bằng chứng; thiếu thì tạo câu hỏi mở.
- Không tự tạo persona hư cấu.

### Bước 3 — Xác định User Goals và Use Cases
- Mỗi User Profile liệt kê mục tiêu sử dụng (User Goal) kèm nguồn.
- Mô tả Use Case cho từng mục tiêu: Actor, precondition, luồng chính, luồng thay thế, postcondition.
- Liên kết Use Case với FR và BR tương ứng.
- Luồng chưa rõ thì chuyển thành câu hỏi mở, không tự suy diễn.

### Bước 4 — Mô tả kịch bản sử dụng (User Scenarios)
- Viết kịch bản sử dụng cụ thể cho từng Use Case chính.
- Mỗi kịch bản: bối cảnh, hành động của người dùng, phản hồi hệ thống, kết quả mong đợi.
- Bao gồm kịch bản thành công và kịch bản lỗi/ngoại lệ có căn cứ.

### Bước 5 — Yêu cầu UI/UX, Usability và Accessibility
- Ghi nhận yêu cầu giao diện từ nguồn hoặc trao đổi với Business/UX.
- Ghi tiêu chí khả dụng (usability) — chỉ khi nguồn nêu hoặc có chuẩn áp dụng.
- Ghi yêu cầu accessibility (WCAG hoặc tiêu chuẩn dự án áp dụng) — chỉ khi nguồn nêu.
- Không tự đặt tiêu chí; thiếu thì tạo câu hỏi mở.

### Bước 6 — Tiêu chí chấp nhận của người dùng (User Acceptance Criteria)
- Mỗi Use Case / kịch bản chính có tiêu chí chấp nhận từ góc nhìn người dùng.
- Tiêu chí phải kiểm chứng được, liên kết về FR/BR và nguồn.
- Đây là cơ sở cho UAT ở BA-06.

### Bước 7 — AI đối chiếu và BA xác minh
- Gọi skill `ba-agent-qa-review` để rà soát URD: kiểm tra tính đầy đủ, nhất quán, truy vết nguồn.
- BA đối chiếu kết quả với nguồn gốc, sửa hoặc loại bỏ nội dung không kiểm chứng được.
- Chuyển URD cho người dùng đại diện / Business review.
- Ghi `Review Status = Draft` cho tới khi có xác nhận.

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| User Requirements Document (URD) | `assets/urd-template.md` — template URD chuẩn |
| Traceability (liên kết URD ↔ Use Case ↔ FR ↔ REQ) | Cập nhật RTM tại `skills/ba-03-specification/assets/rtm.md` |
| Open Questions | Mục `Open Questions` trong URD |
| Source References | Mục `Source References` trong URD — URL + vị trí trong tài liệu |

## Quality Gate URD
Chi tiết tại `references/quality-gate-urd.md`. Tóm tắt:
- [ ] Mọi User Profile đều có nguồn xác định
- [ ] Use Case có luồng chính và ít nhất một luồng lỗi/ngoại lệ
- [ ] Tiêu chí chấp nhận kiểm chứng được
- [ ] Giả định được đánh dấu rõ ràng
- [ ] Mỗi câu hỏi mở đều có owner
- [ ] Người dùng đại diện hoặc Business đã review

Không đạt gate thì URD chưa được phê duyệt và phân phối.

## RACI
| BA | PO | Dev/Tech | QA | Business / User đại diện |
| --- | --- | --- | --- | --- |
| R | C | C | C | A |

## Assets & references
- `assets/urd-template.md` — template URD chuẩn.
- `references/quality-gate-urd.md` — checklist gate URD, quy tắc gắn nhãn bằng chứng và quy tắc dừng bước.
- Skill liên quan: `ba-agent-qa-review` (Bước 7, tuỳ chọn).
- Quy trình trước: `ba-02-business-analysis`. Có thể dùng song song hoặc sau: `ba-doc-brd`, `ba-03-specification`.
- Quy trình liên quan: `ba-06-test-uat` (URD là cơ sở cho UAT).
