# Output schema — Business Analysis Agent

Tham chiếu: `assets/_archive/prompt-pack-v1.0.md` §2 và "Định dạng chung đề xuất"; `assets/_archive/workbook-v1.0.md` sheet `Analysis`; `assets/_archive/sop-v1.0.md` §8, §12.

## 1. Định dạng đầu ra chuẩn

Mọi phản hồi trả về đủ 6 phần, theo đúng thứ tự:

```
1. Summary
2. Facts with sources
3. Findings / Open Questions
4. Suggested actions
5. Confidence limitations
6. Status = DRAFT
```

| Phần | Nội dung |
|---|---|
| Summary | Phạm vi phân tích, nguồn đã dùng, kết quả chính, điểm chưa chốt |
| Facts with sources | Stakeholder, AS-IS/TO-BE, Business Rules, FR/NFR — mỗi dòng kèm nguồn và nhãn |
| Findings / Open Questions | Nội dung thiếu, mâu thuẫn giữa các nguồn, rủi ro, dependency |
| Suggested actions | Việc BA cần xác minh với Business, theo thứ tự ưu tiên |
| Confidence limitations | Nguồn yếu, phần suy luận, phần chưa tiếp cận được |
| Status | Luôn là `DRAFT` |

## 2. Ánh xạ sang sheet `Analysis` (19 cột)

| Cột | Ý nghĩa | Quy tắc điền |
|---|---|---|
| Document ID | Định danh tài liệu phân tích | Theo quy ước dự án; kiểm tra trùng trước khi cấp ID mới |
| Version | Phiên bản bản nháp | Bản nháp AI bắt đầu ở `0.1` |
| Business Problem | Vấn đề nghiệp vụ | Kế thừa Intake Record, có nguồn |
| Business Objective | Mục tiêu | Chỉ ghi objective có trong nguồn; nếu chưa đo lường được → Open Question |
| Scope | Trong phạm vi | Ghi rõ trạng thái là dự kiến hay đã được Business xác nhận |
| Stakeholders | Stakeholder liên quan | Kèm vai trò và nguồn xác định |
| AS-IS | Hiện trạng | Chỉ mô tả phần có bằng chứng |
| TO-BE | Mục tiêu | Phần suy luận phải gắn nhãn `Inference` |
| Functional Requirements | Danh sách FR | `FR-xxx`, mỗi FR liên kết Requirement ID và nguồn |
| Business Rules | Danh sách BR | `BR-xxx`, bắt buộc có nguồn; không có nguồn → không tạo |
| NFR | Yêu cầu phi chức năng | `NFR-xxx`; không tự đặt ngưỡng SLA hay giới hạn hiệu năng |
| Data/Integration/Permissions | Dữ liệu, tích hợp, quyền | Liệt kê hệ thống, API, quyền truy cập đã được nêu trong nguồn |
| Alternative/Error Flows | Luồng thay thế và luồng lỗi | Chỉ ghi luồng có căn cứ; luồng chưa rõ → Open Question |
| Assumptions | Giả định | Ghi rõ giả định và người cần xác nhận |
| Risks | Rủi ro | Kèm tác động và dấu hiệu nhận biết, không tự gán mức ưu tiên |
| Dependencies | Phụ thuộc | Nêu phụ thuộc hệ thống, dự án, dữ liệu, phê duyệt |
| Open Questions | Câu hỏi mở | Mỗi câu hỏi gắn với mục phân tích còn thiếu |
| Source References | Nguồn | Tài liệu + phiên bản + vị trí cụ thể |
| Review Status | Trạng thái review | **Con người sở hữu** — Agent ghi `Draft` |

## 3. Quy tắc đặt ID

| Loại | Dạng | Ghi chú |
|---|---|---|
| Business Rule | `BR-xxx` | Chỉ cấp khi rule có nguồn; một rule một ID, không gộp |
| Functional Requirement | `FR-xxx` | Mỗi FR liên kết ít nhất một Requirement ID |
| NFR | `NFR-xxx` | Không tự đặt con số ngưỡng khi nguồn chưa nêu |
| Document | `BA-DOC-xxx` | Theo quy ước dự án |

ID do Agent đề xuất là ID nháp; BA xác nhận trước khi dùng chính thức.

## 4. Quy tắc gắn nhãn

| Nhãn | Khi nào dùng |
|---|---|
| Fact | Nguồn nêu trực tiếp, trích dẫn được |
| Assumption | Giả định hợp lý để tiếp tục, cần Business xác nhận |
| Inference | Suy ra từ nhiều nguồn, không nguồn nào nêu trực tiếp |
| Unknown | Không có căn cứ; chuyển thành Open Question |

## 5. Dừng bước khi nào

Dừng và báo lại BA, không tự chế dữ liệu thay thế, khi:

1. Intake Record chưa ở trạng thái `Accepted for Analysis`.
2. Không truy cập được tài liệu nghiệp vụ cần đối chiếu.
3. Nguồn không có phiên bản hoặc không xác định được bản chính thức.
4. Hai nguồn mâu thuẫn về Business Rule và không có nguồn nào được quy định là chính thức.
5. Business Rule cần thiết cho phân tích chỉ tồn tại dưới dạng lời nói chưa được ghi nhận.
6. Tài liệu chứa dữ liệu nhạy cảm chưa được phép xử lý bằng công cụ hiện tại.

Khi dừng: nêu rõ bước dừng, lý do, nguồn liên quan, mục phân tích bị chặn và thông tin cần cung cấp.

## 7. AI Review Status

Mọi đầu ra của agent kèm `AI Review Status = Draft - cần review`. Giá trị hợp lệ: `Draft - cần review` | `Reviewed - Accepted` | `Reviewed - Accepted with Changes` | `Reviewed - Rejected`. Người review cập nhật giá trị này; agent không tự chuyển ra khỏi `Draft - cần review`. Giá trị đồng bộ với cột `Review Decision` trong `ba-records/<project>/ai-run-log.md`.

## 6. Idempotency và audit trail

- Trước khi tạo tài liệu phân tích mới, tra theo `Document ID`, `Scope` và `Source References`. Nếu đã có bản nháp cho cùng phạm vi, cập nhật và tăng `Version` thay vì tạo mới.
- Mỗi lần chạy ghi lại: prompt version, model/version, danh sách nguồn kèm phiên bản, đầu ra tạo thành, người review và quyết định (SOP §8), theo template `assets/ai-run-log.md` ở gốc power; bản ghi thật tại `ba-records/<project>/ai-run-log.md`.
