# AI Review Log

Template chỉ đọc, khớp 15 cột sheet `AI Review` của `assets/_archive/workbook-v1.0.md`. Log thật lưu tại `ba-records/<project>/ai-review-log.md`. Mỗi finding một dòng.

| Review ID | Artifact Type | Artifact ID | Source References | Check Category | Finding | Severity | Evidence | Suggested Action | Owner | Status | Reviewer | Prompt Version | Model/Version | Review Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <AIR-xxx> | <User Story \| URD \| BRD \| Analysis \| RTM \| Change Request> | <US-001> | <URL tài liệu + vị trí> | <Completeness \| Clarity \| Consistency \| Testability \| Traceability \| Negative Cases \| NFR \| Change Impact> | <mô tả finding, một câu, có căn cứ> | <Critical \| Major \| Minor \| Info> | <AC-03 / đoạn trích / dòng-cột> | <việc cần làm để khắc phục> | <BA \| PO \| QA \| Business Owner> | <Open \| In Review \| Resolved \| Accepted Risk> | <để trống> | <1.0> | <giá trị thật từ hệ thống; không có thì để trống> | <để trống> |

## Cách điền

- `Review ID`: theo quy ước `AIR-xxx`, tăng tuần tự; tra log hiện có trước khi cấp ID mới để tránh trùng.
- `Artifact Type` và `Artifact ID`: ghi đúng loại và ID của artifact được review, không ghi tên chung chung.
- `Source References`: URL hoặc đường dẫn tài liệu kèm phiên bản và vị trí đã đọc.
- `Check Category`: chọn đúng một trong 8 giá trị enum; nếu finding thuộc hai category, tách thành hai dòng.
- `Finding`: mô tả vấn đề quan sát được, không kèm suy đoán về nguyên nhân khi chưa có bằng chứng.
- `Severity`: áp dụng rubric trong `../references/finding-table.md`.
- `Evidence`: con trỏ chính xác tới chỗ có vấn đề (AC ID, Business Rule ID, dòng, cột, đoạn trích).
- `Suggested Action`: đề xuất hành động; với finding là rủi ro cần xác minh thì ghi rõ cần xác minh với ai.
- `Owner`: vai trò nên xử lý, không phải người đã duyệt.
- `Status`: Agent luôn ghi `Open`.
- `Prompt Version`: ghi phiên bản prompt đã dùng. `Model/Version`: chỉ ghi khi hệ thống cung cấp giá trị thật. Cả hai phục vụ audit trail (SOP §8).

## Không tự điền

Các trường sau thuộc thẩm quyền con người, Agent để trống:

- `Reviewer` — người review là con người, không phải Agent.
- `Review Date` — ngày review chính thức do người review xác nhận.
- `Model/Version` — chỉ điền khi hệ thống cung cấp giá trị thật; không suy đoán.
- `Status` khác `Open` (`In Review`, `Resolved`, `Accepted Risk`) — do người có thẩm quyền quyết định.
- `Severity` không được tự hạ xuống để artifact đạt Quality Gate.
