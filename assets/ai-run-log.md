# AI Run Log

Template audit trail dùng chung cho cả 6 agent và phần AI hỗ trợ ở BA-07 Bước 4 (SOP §8: Versioning, Audit trail). Mở rộng ⚠: workbook v1.0 chưa có sheet này.

File này là template chỉ đọc. Bản ghi thật lưu tại `ba-records/<project>/ai-run-log.md`. Mỗi lần chạy một dòng; finding chi tiết của QA Review vẫn ghi ở `ai-review-log.md`.

| Run ID | Agent | Process/Step | Requested By | Run Date | Prompt Version | Model/Version | Input Documents + Version | Output Artifact | Reviewer | Review Decision | Review Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| <RUN-001> | <ba-agent-requirement> | <BA-01 Bước 4> | <người yêu cầu chạy> | <YYYY-MM-DD> | <1.0> | <giá trị thật từ hệ thống; không có thì để trống> | <tài liệu + phiên bản> | <REQ-001 nháp> | <để trống> | <để trống> | <để trống> |

## Cách điền

- `Run ID`: tăng tuần tự; chạy lại cùng đầu vào và cùng đầu ra thì cập nhật dòng cũ, không tạo dòng mới.
- `Prompt Version`: phiên bản prompt đã dùng; bộ prompt gốc là `1.0`.
- `Model/Version`: chỉ ghi giá trị do hệ thống cung cấp, không suy đoán.
- `Input Documents + Version`: mỗi tài liệu kèm phiên bản, hoặc ngày và người ghi nhận nếu nguồn không đánh phiên bản.

## Không tự điền

`Reviewer`, `Review Decision` và `Review Date` do người review điền. Giá trị hợp lệ của `Review Decision`: `Accepted` | `Accepted with Changes` | `Rejected`.
