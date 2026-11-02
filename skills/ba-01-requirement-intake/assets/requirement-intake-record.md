# BA-T01 — Requirement Intake Record

Template này khớp sheet `Intake` của `assets/_archive/workbook-v1.0.md` (16 cột). Mỗi yêu cầu là **một record**.
Sao chép khối bên dưới, điền vào, rồi lưu vào hệ thống quản lý công việc của dự án.

## Record

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Requirement ID | `<REQ-000>` | Duy nhất toàn dự án; kiểm tra trùng trước khi phát hành |
| Request Title | `<tiêu đề ngắn, không diễn giải>` | Lấy theo ngôn ngữ của người yêu cầu |
| Requester | `<tên / bộ phận>` | Nếu không xác định được: `Unknown` + câu hỏi mở |
| Business Owner | `<tên / vai trò>` | Không tự suy diễn từ nội dung yêu cầu |
| Business Problem | `<vấn đề hiện tại>` | Chỉ ghi phần có bằng chứng |
| Business Objective | `<kết quả mong muốn>` | Có thể đo lường được nếu nguồn nêu rõ |
| Scope | `<phạm vi dự kiến>` | Mức sơ bộ, không chốt phạm vi cuối ở BA-01 |
| Out of Scope | `<ngoài phạm vi>` | Ghi rõ nếu nguồn có nêu |
| Priority | `<PO xác định>` | **BA và AI không tự điền** |
| Source Documents + Version | `<URL + phiên bản>` | Mỗi nguồn một dòng; thiếu phiên bản là lỗi G1 |
| Dependencies | `<hệ thống / nhóm / yêu cầu khác>` | Để trống nếu chưa phát hiện, không suy đoán |
| Target Date | `<ngày mong muốn>` | Là mong muốn của requester, không phải cam kết |
| Open Questions | `<danh sách câu hỏi>` | Mỗi câu hỏi gắn một người trả lời dự kiến |
| AI Review Status | `<Draft - cần review / Reviewed / Not used>` | Mặc định `Draft - cần review` khi có dùng AI |
| BA/PO Decision | `<Chưa quyết định / Accepted for Analysis / Rejected>` | Người có thẩm quyền điền |
| Status | `<New / Clarification Required / Accepted for Analysis / Rejected>` | Theo SOP §12 |

## Không tự điền (chỉ con người có thẩm quyền)
- `Priority` — PO xác định.
- `BA/PO Decision` — BA/PO quyết định.
- `Business Owner` khi không có bằng chứng.
- `Target Date` dưới dạng cam kết.

## Quy tắc điền
- Mỗi dữ kiện quan trọng phải trỏ được về `Source Documents + Version`.
- Phân loại nội dung: `[Fact]` có nguồn, `[Assumption]` giả định, `[Inference]` suy luận, `[Unknown]` chưa biết.
- Không xoá câu hỏi mở chưa được trả lời; đánh dấu `Resolved` kèm ngày và người trả lời.
- Khi AI điền bản nháp, giữ nguyên `AI Review Status = Draft - cần review` cho tới khi BA xác minh xong.
