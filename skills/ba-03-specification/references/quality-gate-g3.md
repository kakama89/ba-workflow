# Quality Gate G3 — Đặc tả và xác nhận yêu cầu

Gate này đóng lại BA-03. Không đạt G3 thì Story chưa được đưa vào refinement.

## Checklist bắt buộc

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | AC kiểm thử được | Mỗi AC có `Given` đủ điều kiện, `When` xác định, `Then` quan sát được | |
| 2 | Không che giấu giả định | Mọi nội dung chưa xác nhận gắn `[Assumption]` hoặc `[Unknown]` | |
| 3 | Có xác nhận | Tên người xác nhận (PO/Business) và ngày | |
| 4 | Có phiên bản | `Version` và `Review Status` được cập nhật | |

## Tiêu chí bổ sung nên kiểm tra
- [ ] Mỗi Story có `Epic ID`, `Story ID`, `Requirement IDs` và `Business Rule IDs`.
- [ ] `So that` trỏ về Business Objective thật, không phải câu chung chung.
- [ ] Mỗi luồng chính có ít nhất một `Validation/Error Case`.
- [ ] Quyền truy cập được mô tả rõ: Actor nào bị chặn, thông báo gì.
- [ ] Không có AC trùng lặp trong cùng Story hoặc giữa các Story.
- [ ] NFR chỉ gồm nội dung có nguồn; không có ngưỡng tự đặt.
- [ ] `Open Questions` quan trọng đã có câu trả lời hoặc có owner và hạn.
- [ ] RTM đã có dòng tương ứng cho Story/AC mới (`../assets/rtm.md`).
- [ ] Dev/Tech Lead đã xem khả thi; QA đã xem testability.

## Tiêu chí "AC kiểm thử được"
Một AC **không** đạt nếu:
1. `Then` dùng từ định tính không có ngưỡng từ nguồn: "nhanh", "mượt", "thân thiện", "chính xác", "phù hợp".
2. `Given` thiếu dữ liệu, trạng thái hoặc quyền cần để tái lập.
3. Không xác định được ai/ công cụ nào kiểm chứng và bằng chứng nằm ở đâu.
4. Gộp nhiều hành vi độc lập vào một AC mà mỗi hành vi cần một kết quả riêng.
5. Không trỏ được về `Business Rule ID` hoặc nguồn.

Cách sửa: tách AC, bổ sung điều kiện `Given`, hoặc chuyển phần chưa rõ thành `Open Questions` thay vì viết mơ hồ cho xong.

## Quy tắc dừng bước
Dừng và báo thay vì tiếp tục khi:
1. Business Rule cần cho AC chưa được xác nhận và không ai trả lời.
2. AI thêm quy tắc, giới hạn hoặc hành vi không có trong tài liệu phân tích — loại bỏ phần đó.
3. Story không thể phân rã nhỏ hơn mà vẫn còn thiếu thông tin nền.
4. Mâu thuẫn giữa Business Rules và Process Flow chưa được phân xử.
5. Bị yêu cầu đánh dấu `Ready for Refinement` khi câu hỏi quan trọng còn mở.

Khi dừng: giữ `Review Status = Draft`, ghi lý do vào `Open Questions`, báo BA và PO.

## Lỗi thường gặp ở G3
| Lỗi | Vì sao nguy hiểm | Cách xử lý |
| --- | --- | --- |
| Viết AC theo giải pháp kỹ thuật | Khoá thiết kế, khó kiểm thử hành vi | Viết theo hành vi người dùng quan sát được |
| Bỏ luồng lỗi vì nguồn không nêu | Thiếu negative case, lọt defect | Tạo câu hỏi mở, không tự bịa quy tắc |
| Để AI đặt Priority/Story Point | Vượt thẩm quyền | Xoá, chuyển PO/Team |
| Ghi `Ready for Refinement` khi chưa xác nhận | Vỡ G3, rework trong Sprint | Lấy xác nhận tên + ngày |
| Tạo Story mới mà không thêm dòng RTM | Mất traceability | Cập nhật RTM ngay tại Bước 4 |
| Một AC chứa ba hành vi | Kết quả Pass/Fail không rõ nghĩa | Tách thành ba AC |

## Người ký G3
BA chịu trách nhiệm nội dung đặc tả; Dev/Tech Lead và QA tham vấn; PO hoặc Business xác nhận theo thẩm quyền và là người chịu trách nhiệm cuối cùng (A).
