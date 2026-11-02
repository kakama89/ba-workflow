# Output schema — Requirement Intake Agent

Tham chiếu: `assets/_archive/prompt-pack-v1.0.md` §1 và "Định dạng chung đề xuất"; `assets/_archive/workbook-v1.0.md` sheet `Intake`; `assets/_archive/sop-v1.0.md` §8, §12.

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
| Summary | 3–6 câu: yêu cầu gì, ai gửi, phân loại nào, còn thiếu gì quan trọng nhất |
| Facts with sources | Dữ kiện trích xuất được, mỗi dòng kèm nguồn (tài liệu + phiên bản + vị trí) |
| Findings / Open Questions | Thông tin thiếu, câu hỏi làm rõ, trùng lặp, mâu thuẫn, dependency, rủi ro |
| Suggested actions | Việc BA nên làm tiếp, kèm người nên làm; không phải quyết định |
| Confidence limitations | Phần nào chưa xác minh, nguồn yếu ở đâu, vì sao chưa kết luận được |
| Status | Luôn là `DRAFT` |

## 2. Ánh xạ Intake Record sang sheet `Intake` (16 cột)

| Cột | Ý nghĩa | Quy tắc điền |
|---|---|---|
| Requirement ID | Định danh yêu cầu | Theo quy ước dự án; kiểm tra trùng trước khi cấp ID mới |
| Request Title | Tên ngắn của yêu cầu | Lấy từ nguồn, không thêm phạm vi mới |
| Requester | Người gửi yêu cầu | Chỉ điền khi có bằng chứng; nếu suy luận thì ghi nhãn `Inference` |
| Business Owner | Người sở hữu nghiệp vụ | Chỉ điền khi có bằng chứng |
| Business Problem | Vấn đề hiện tại | Trích từ nguồn, giữ nguyên ngữ nghĩa |
| Business Objective | Kết quả mong muốn | Chỉ ghi objective có trong nguồn; objective chưa đo lường được → Open Question |
| Scope | Phạm vi dự kiến | Ghi rõ đây là phạm vi *dự kiến*, chưa chốt |
| Out of Scope | Ngoài phạm vi | Chỉ ghi khi nguồn nêu rõ |
| Priority | Độ ưu tiên | **Con người sở hữu** — để trống, ghi `PO xác định` |
| Source Documents + Version | Nguồn và phiên bản | Bắt buộc; mỗi tài liệu kèm phiên bản hoặc ngày truy cập |
| Dependencies | Phụ thuộc hệ thống/dự án | Chỉ liệt kê dependency có căn cứ |
| Target Date | Ngày mong muốn | Chỉ ghi khi nguồn nêu; không tự suy ra |
| Open Questions | Câu hỏi còn mở | Mỗi câu hỏi gắn với phần thông tin thiếu tương ứng |
| AI Review Status | Trạng thái bản nháp AI | Ví dụ: `Draft - cần review` |
| BA/PO Decision | Quyết định của BA/PO | **Con người sở hữu** — để trống hoặc `Chưa quyết định` |
| Status | Trạng thái Intake | **Con người sở hữu** — theo SOP §12 |

## 3. Giá trị enum

- **Phân loại yêu cầu:** `New Feature | Enhancement | Defect | Technical Change | Compliance`
- **Nhãn bằng chứng:** `Fact | Assumption | Inference | Unknown`
- **Status Intake (SOP §12):** `New → Clarification Required → Accepted for Analysis / Rejected`
- **Status đầu ra của Agent:** `DRAFT` (cố định)

## 4. Quy tắc gắn nhãn

| Nhãn | Khi nào dùng |
|---|---|
| Fact | Nguồn nêu trực tiếp, trích dẫn được |
| Assumption | Giả định hợp lý để tiếp tục, cần Business xác nhận |
| Inference | Suy ra từ nhiều nguồn, không có nguồn nào nêu trực tiếp |
| Unknown | Không có căn cứ; phải chuyển thành câu hỏi làm rõ |

Không được chuyển `Assumption`, `Inference` hay `Unknown` thành `Fact` khi chưa xác minh.

## 5. Dừng bước khi nào

Dừng và báo lại BA, không tự chế dữ liệu thay thế, khi gặp một trong các trường hợp:

1. Không truy cập được Business Request hoặc tài liệu nguồn.
2. Nguồn không có phiên bản hoặc không xác định được bản chính thức.
3. Hai nguồn mâu thuẫn và không có nguồn nào được quy định là chính thức.
4. Không xác định được Requester hoặc Business Owner từ bằng chứng.
5. Yêu cầu có dấu hiệu trùng với Intake Record đã tồn tại.
6. Nội dung chứa dữ liệu nhạy cảm hoặc bí mật chưa được phép xử lý bằng công cụ hiện tại.

Khi dừng: nêu rõ bước dừng, lý do, nguồn liên quan và thông tin cần BA cung cấp.

## 6. Idempotency và audit trail

- Trước khi tạo Intake Record mới, tra theo `Request Title` + `Source Documents + Version` + `Requester`. Nếu đã có bản ghi cho cùng Business Request, cập nhật bản nháp hiện có thay vì tạo mới.
- Mỗi lần chạy ghi lại: prompt version, model/version, danh sách tài liệu đầu vào kèm phiên bản, đầu ra tạo thành, người review và quyết định (SOP §8).
