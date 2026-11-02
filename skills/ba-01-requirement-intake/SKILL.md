---
name: ba-01-requirement-intake
description: "BA-01 requirement intake and triage for Agile/Scrum software projects: issue a unique Requirement ID, record source and owner, classify the request, verify document version, preliminary scope, dependencies and access rights, then run AI extraction followed by BA verification. Use when a new business request, ticket, email, URD or BRD arrives and must be logged and screened before analysis, or when an existing request still has no Requirement ID. Tiếng Việt: BA-01 Tiếp nhận và sàng lọc yêu cầu — tạo Requirement ID duy nhất, ghi nguồn và người phụ trách, phân loại yêu cầu, kiểm tra phiên bản tài liệu, phạm vi sơ bộ, dependency và quyền truy cập, sau đó AI trích xuất và BA xác minh. Dùng khi có yêu cầu nghiệp vụ mới cần ghi nhận và sàng lọc trước khi phân tích."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-01, Quality Gate G1, §12"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet Intake / BA-T01"
compatibility: "Cần quyền đọc nguồn yêu cầu đã được cấp phép (Jira, Azure DevOps, Confluence, SharePoint, email, URD/BRD). Không cần quyền ghi; bản ghi chính thức do BA tạo và PO quyết định."
---

# BA-01 — Tiếp nhận và sàng lọc yêu cầu

## Mục tiêu
Ghi nhận yêu cầu đúng nguồn, có người phụ trách và xác định đủ thông tin ban đầu.

## Khi nào dùng
- Có Business Request mới: ticket, email, trao đổi trực tiếp, URD/BRD/Confluence.
- Yêu cầu đã tồn tại nhưng chưa có Requirement ID hoặc chưa được phân loại.
- Cần quyết định có đưa vào phân tích hay không trước khi chuyển sang BA-02.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Business Request | Có | Nội dung thô từ người yêu cầu |
| Nguồn (email / ticket / URD / BRD / Confluence) | Có | Ghi URL hoặc nơi lưu và phiên bản; nguồn không đánh phiên bản (email, trao đổi trực tiếp đã ghi biên bản) ghi ngày và người ghi nhận |
| Requester | Có | Nếu thiếu, ghi `Unknown` và tạo câu hỏi mở |
| Business Owner | Có | Không tự suy diễn |
| Mục tiêu và thời hạn mong muốn | Nếu có | Thời hạn là mong muốn; PO quyết định ưu tiên |
| Quyền truy cập tài liệu | Có | Không đọc được nguồn thì dừng bước, không đoán nội dung |

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

Riêng ở BA-01: **không tự phê duyệt hoặc suy diễn quy tắc nghiệp vụ**, không ghi Requester/Business Owner khi chưa có bằng chứng trong nguồn, không phân loại yêu cầu khi bằng chứng chưa đủ.

## Quy trình

### Bước 1 — Tạo Requirement ID và ghi nhận nguồn
- Phát hành Requirement ID duy nhất theo quy ước dự án (workbook dùng dạng `REQ-001`).
- Ghi: nguồn, người yêu cầu, Business Owner, phiên bản tài liệu.
- Kiểm tra trùng ID và trùng nội dung trước khi tạo mới.

### Bước 2 — Phân loại yêu cầu
Chọn đúng một loại: `New Feature` | `Enhancement` | `Defect` | `Technical Change` | `Compliance`.
Bằng chứng chưa đủ để phân loại thì ghi `Unknown` kèm câu hỏi mở. Ghi kết quả vào trường `Request Type` ⚠ của record.

### Bước 3 — Kiểm tra tài liệu, phiên bản, phạm vi sơ bộ, dependency và quyền truy cập
- Xác nhận tài liệu là bản chính thức và đúng phiên bản.
- Ghi `Scope` và `Out of Scope` ở mức sơ bộ, không chốt phạm vi cuối.
- Liệt kê dependency và quyền truy cập còn thiếu.

### Bước 4 — AI trích xuất
Gọi skill `ba-agent-requirement` để trích xuất mục tiêu, dữ kiện, câu hỏi thiếu, trùng lặp và mâu thuẫn, kèm dẫn nguồn.
Đầu ra AI là bản nháp: đặt `AI Review Status = Draft - cần review`.

### Bước 5 — BA xác minh và chuyển quyết định
- BA đối chiếu từng dữ kiện với nguồn gốc; sửa hoặc loại bỏ nội dung không kiểm chứng được.
- Trao đổi với người yêu cầu để đóng các câu hỏi mở.
- Tuỳ chọn: gọi `ba-agent-qa-review` để rà soát record trước khi đóng G1.
- PO hoặc người có thẩm quyền quyết định bước tiếp theo, ghi vào `BA/PO Decision`.

### Đường đi sau quyết định ⚠

`Rejected`: giữ record, ghi lý do, báo người yêu cầu rồi kết thúc; không xoá record.

`Accepted for Analysis`: PO chọn đường đi theo `Request Type` và ghi vào `BA/PO Decision`.

| Request Type | Đường đi |
| --- | --- |
| `New Feature`, `Enhancement`, `Compliance` | Đầy đủ BA-02 → BA-07 |
| `Defect` lệch AC đã duyệt | QA/Dev sửa, rồi retest ở BA-06; không qua BA-02, BA-03 |
| `Defect` chưa có AC mô tả hành vi | Coi là requirement gap, mở CR ở BA-05 |
| `Technical Change` không đổi hành vi nghiệp vụ | Tech Lead xác nhận điều đó; BA-02 chỉ làm dependency và ảnh hưởng; vào BA-03 nếu cần Story |
| `Technical Change` có đổi hành vi nghiệp vụ | Đầy đủ BA-02 → BA-07 |
| `Unknown` | Giữ `Clarification Required`; chưa được đi tiếp |

Bảng này là đề xuất mở rộng theo nguyên tắc "phân tích theo mức độ cần thiết" (SOP §3), chưa có trong SOP v1.0; chủ quy trình phải chốt trước khi thí điểm. Đường rút gọn không bỏ G1 và G4.

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| Requirement Intake Record | `assets/requirement-intake-record.md` — khớp sheet `Intake` (16 cột), thêm `Request Type` ⚠ |
| Open Questions | cột `Open Questions` của cùng record |
| Danh sách nguồn và trạng thái | cột `Source Documents + Version`, `Status` |

Chuỗi trạng thái Intake (SOP §12): `New` → `Clarification Required` → `Accepted for Analysis` / `Rejected`.

## Quality Gate G1
Chi tiết tại `references/quality-gate-g1.md`. Tóm tắt:
- [ ] Có Requirement ID
- [ ] Có mục tiêu
- [ ] Có nguồn kèm phiên bản
- [ ] Có người phụ trách
- [ ] Phân biệt rõ bản nháp AI với nội dung đã xác nhận

Chỉ chuyển sang BA-02 khi đạt G1 **và** `Status = Accepted for Analysis`.

## RACI
| BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- |
| R | A | I | I | C |

## Assets & references
- `assets/requirement-intake-record.md` — template Intake Record.
- `references/quality-gate-g1.md` — checklist G1 chi tiết, quy tắc dừng bước và lỗi thường gặp.
- Skill liên quan: `ba-agent-requirement` (Bước 4), `ba-agent-qa-review` (Bước 5, tuỳ chọn).
- Quy trình kế tiếp: `ba-02-business-analysis`.
