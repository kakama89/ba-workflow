---
name: ba-doc-brd
description: "Create a Business Requirements Document (BRD) from analysed requirements: consolidate business objectives, scope, stakeholders, AS-IS/TO-BE, functional and non-functional requirements, business rules, constraints, assumptions, risks, dependencies and success metrics into a formal BRD with full source traceability. Use when the analysis has passed gate G2 and the project needs a formal BRD to communicate business requirements to stakeholders, sponsors and delivery teams. Tiếng Việt: Tạo tài liệu BRD (Business Requirements Document) từ kết quả phân tích: tổng hợp mục tiêu kinh doanh, phạm vi, stakeholder, AS-IS/TO-BE, yêu cầu chức năng và phi chức năng, quy tắc nghiệp vụ, ràng buộc, giả định, rủi ro, phụ thuộc và chỉ số thành công thành tài liệu BRD chính thức có truy vết nguồn đầy đủ. Dùng khi phân tích đã qua gate G2 và dự án cần BRD chính thức để truyền đạt yêu cầu nghiệp vụ tới stakeholder, sponsor và đội triển khai."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-02, BA-03; Quality Gate G2"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet Analysis / BA-T02"
compatibility: "Cần kết quả phân tích nghiệp vụ (Business Analysis Document) đã đạt G2, Business Rules Catalog có nguồn, và quyền đọc tài liệu nghiệp vụ đã được cấp phép. Cần Business Owner hoặc Sponsor xác nhận nội dung BRD trước khi phê duyệt."
---

# BA-DOC-BRD — Tạo tài liệu Business Requirements Document (BRD)

## Mục tiêu
Tổng hợp kết quả phân tích nghiệp vụ thành tài liệu BRD chính thức, có cấu trúc chuẩn, truy vết nguồn đầy đủ, phục vụ truyền đạt yêu cầu nghiệp vụ tới các bên liên quan và làm cơ sở cho đặc tả chi tiết.

## Khi nào dùng
- Tài liệu phân tích nghiệp vụ (Business Analysis Document) đã đạt Quality Gate G2.
- Dự án yêu cầu có BRD chính thức để trình Sponsor, Steering Committee hoặc đội triển khai.
- Cần tài liệu chuẩn để làm baseline cho quản lý thay đổi (BA-05).
- Cần BRD để phục vụ hợp đồng, đấu thầu hoặc báo cáo tuân thủ.

Không dùng skill này khi:
- Chưa có kết quả phân tích đạt G2 — quay lại `ba-02-business-analysis`.
- Cần viết User Story/AC — đó là `ba-03-specification`.
- Cần tài liệu yêu cầu từ góc nhìn người dùng — dùng `ba-doc-urd`.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Business Analysis Document | Có | Đã đạt G2, có `Review Status = Approved` hoặc `In Review` |
| Business Rules Catalog | Có | Mỗi quy tắc có ID (`BR-xxx`) và nguồn |
| Stakeholder Map | Có | Vai trò, mối quan tâm, mức ảnh hưởng |
| Process Flow (AS-IS / TO-BE) | Có | AS-IS có bằng chứng, TO-BE đã được Business xác nhận |
| Functional Requirements (FR) | Có | Mỗi FR có ID (`FR-xxx`) và liên kết Requirement ID |
| Non-Functional Requirements (NFR) | Nếu có | Chỉ ghi NFR có nguồn hoặc ràng buộc kỹ thuật |
| Intake Record(s) | Có | Để truy vết về yêu cầu gốc |
| Tài liệu nghiệp vụ bổ sung | Nếu có | Quy trình, quy định, chính sách kèm phiên bản |

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

Riêng ở BA-DOC-BRD: **không tự tạo yêu cầu mới ngoài phạm vi đã phân tích**, không tự đặt ngưỡng SLA/KPI/Success Metrics khi nguồn chưa nêu, không tự chốt phạm vi thay Business Owner.

## Quy trình

### Bước 1 — Kiểm tra đầu vào và xác nhận phạm vi
- Xác nhận Business Analysis Document đã đạt G2.
- Kiểm tra BRD đã tồn tại cho cùng phạm vi chưa; nếu có, cập nhật và tăng `Version` thay vì tạo mới.
- Xác nhận danh sách nguồn và phiên bản tài liệu đầu vào.
- Chốt phạm vi BRD với Business Owner (AI chỉ đề xuất, người có thẩm quyền xác nhận).

### Bước 2 — Tổng hợp thông tin tổng quan
- Ghi nhận bối cảnh dự án, vấn đề kinh doanh và mục tiêu kinh doanh từ nguồn.
- Xác định Success Metrics/KPI — chỉ ghi khi nguồn có nêu; thiếu thì tạo câu hỏi mở.
- Ghi rõ phạm vi (Scope) và ngoài phạm vi (Out of Scope).
- Liệt kê giả định và ràng buộc có nguồn.

### Bước 3 — Tổng hợp Stakeholder và quy trình
- Chuyển Stakeholder Map từ Business Analysis Document sang mục tương ứng của BRD.
- Mô tả AS-IS và TO-BE; chỉ có nội dung có bằng chứng trong AS-IS, TO-BE ghi rõ trạng thái xác nhận.
- Mô tả tác động của thay đổi tới từng nhóm stakeholder.

### Bước 4 — Tổng hợp yêu cầu
- Chuyển Functional Requirements (FR) với ID, mô tả, nguồn và liên kết Business Rule.
- Chuyển Non-Functional Requirements (NFR) với ID, mô tả và nguồn; không tự đặt ngưỡng.
- Chuyển Business Rules Catalog nguyên vẹn với ID và nguồn.
- Ghi nhận yêu cầu dữ liệu, tích hợp và phân quyền.

### Bước 5 — Tổng hợp rủi ro, phụ thuộc và kế hoạch
- Chuyển danh sách rủi ro với tác động và dấu hiệu nhận biết.
- Chuyển danh sách phụ thuộc (dependency) với hệ thống/nhóm sở hữu.
- Ghi timeline và milestone mong muốn (nếu nguồn có nêu); không tự cam kết thời hạn.
- Liệt kê các quyết định đã có và câu hỏi mở còn lại.

### Bước 6 — AI đối chiếu và BA xác minh
- Gọi skill `ba-agent-qa-review` để rà soát BRD: kiểm tra tính đầy đủ, nhất quán, truy vết nguồn.
- BA đối chiếu kết quả với nguồn gốc, sửa hoặc loại bỏ nội dung không kiểm chứng được.
- Chuyển BRD cho Business Owner / Sponsor review.
- Ghi `Review Status = Draft` cho tới khi có xác nhận.

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| Business Requirements Document (BRD) | `assets/brd-template.md` — template BRD chuẩn |
| Traceability Matrix (liên kết BRD ↔ FR ↔ BR ↔ REQ) | Cập nhật RTM tại `skills/ba-03-specification/assets/rtm.md` |
| Open Questions | Mục `Open Questions` trong BRD |
| Source References | Mục `Source References` trong BRD — URL + vị trí trong tài liệu |

## Quality Gate BRD
Chi tiết tại `references/quality-gate-brd.md`. Tóm tắt:
- [ ] Mọi yêu cầu (FR/NFR) đều có nguồn và liên kết Requirement ID
- [ ] Business Rules có nguồn đầy đủ
- [ ] Giả định được đánh dấu rõ ràng
- [ ] Phạm vi đã được Business Owner xác nhận
- [ ] Success Metrics có nguồn hoặc được ghi nhận là câu hỏi mở
- [ ] Mỗi câu hỏi mở đều có owner

Không đạt gate thì BRD chưa được phê duyệt và phân phối.

## RACI
| BA | PO | Dev/Tech | QA | Business/Sponsor |
| --- | --- | --- | --- | --- |
| R | C | C | C | A |

## Assets & references
- `assets/brd-template.md` — template BRD chuẩn.
- `references/quality-gate-brd.md` — checklist gate BRD, quy tắc gắn nhãn bằng chứng và quy tắc dừng bước.
- Skill liên quan: `ba-agent-qa-review` (Bước 6, tuỳ chọn).
- Quy trình trước: `ba-02-business-analysis`. Có thể dùng song song hoặc sau: `ba-doc-urd`, `ba-03-specification`.
