# Quality Gate G1 — Tiếp nhận và sàng lọc yêu cầu

Gate này đóng lại BA-01. Chỉ chuyển sang BA-02 khi đạt G1 **và** PO hoặc người có thẩm quyền đã đặt `Status = Accepted for Analysis`.

## Checklist bắt buộc

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | Có Requirement ID | ID duy nhất, không trùng bản ghi hiện có | |
| 2 | Có mục tiêu | `Business Objective` không trống, không phải câu chung chung | |
| 3 | Có nguồn | `Source Documents + Version` liệt kê URL hoặc nơi lưu **và** phiên bản; nguồn không đánh phiên bản ghi ngày và người ghi nhận | |
| 4 | Có người phụ trách | `Requester` và `Business Owner` xác định được | |
| 5 | Tách bạch AI và nội dung đã xác nhận | `AI Review Status` phản ánh đúng thực tế review | |

## Tiêu chí bổ sung nên kiểm tra
- [ ] `Request Type` ⚠ là đúng một trong: `New Feature`, `Enhancement`, `Defect`, `Technical Change`, `Compliance`, hoặc `Unknown` kèm câu hỏi mở.
- [ ] `Scope` và `Out of Scope` ở mức sơ bộ, không phát biểu vượt quá nguồn.
- [ ] Mỗi `Open Questions` đều có người trả lời dự kiến.
- [ ] `Priority` và `BA/PO Decision` do con người điền, không phải AI.
- [ ] Không có dữ liệu nhạy cảm hoặc bí mật trong record nếu hệ thống đích chưa được phê duyệt.

## Quy tắc dừng bước
Dừng và báo thay vì tiếp tục khi:
1. Không truy cập được nguồn tài liệu, hoặc nguồn không phải bản chính thức.
2. Không xác định được Business Owner và không ai trả lời câu hỏi mở.
3. AI trả về dữ kiện không trích được nguồn.
4. Phát hiện trùng lặp với Requirement ID đã có nhưng chưa rõ nên gộp hay tách.
5. Yêu cầu mâu thuẫn với tài liệu đã duyệt mà chưa có người phân xử.

Khi dừng: ghi lý do vào `Open Questions`, đặt `Status = Clarification Required`, chuyển về BA kèm danh sách việc cần xác minh. Không tự điền giá trị thay thế.

## Lỗi thường gặp ở G1
| Lỗi | Vì sao nguy hiểm | Cách xử lý |
| --- | --- | --- |
| Ghi nguồn nhưng thiếu phiên bản | Không tái lập được bằng chứng | Yêu cầu URL + phiên bản/ngày |
| Suy ra Business Owner từ người gửi email | Sai thẩm quyền xác nhận | Ghi `Unknown`, hỏi trực tiếp |
| Để AI đặt Priority | Vượt thẩm quyền, lệch backlog | Xoá, chuyển PO |
| Gộp `Assumption` vào `Business Problem` | Giả định bị coi là sự thật | Gắn nhãn `[Assumption]` |
| Tạo record mới cho yêu cầu đã có | Trùng lặp, vỡ traceability | Kiểm tra trùng trước Bước 1 |

## Người ký G1
BA xác nhận tính đầy đủ; PO hoặc người có thẩm quyền quyết định `Accepted for Analysis` / `Rejected`.
