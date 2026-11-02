# Quality Gate G2 — Khảo sát và phân tích nghiệp vụ

Gate này đóng lại BA-02. Không đạt G2 thì không chuyển sang BA-03.

## Checklist bắt buộc

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | Quy tắc có nguồn | Mỗi `BR-xxx` trỏ được tới URL + vị trí trong tài liệu | |
| 2 | Giả định được đánh dấu | Mọi nội dung chưa xác nhận đều gắn `[Assumption]` hoặc `[Unknown]` | |
| 3 | Business xác nhận TO-BE | Có tên người xác nhận và ngày trong tài liệu | |
| 4 | Câu hỏi mở có owner | Không còn `Open Questions` để trống người phụ trách | |

## Tiêu chí bổ sung nên kiểm tra
- [ ] AS-IS chỉ chứa nội dung có bằng chứng, không lẫn đề xuất cải tiến.
- [ ] Mỗi luồng chính có ít nhất một luồng lỗi hoặc ngoại lệ tương ứng.
- [ ] `Functional Requirements` có ID và trỏ về Business Rule hoặc nguồn.
- [ ] `NFR` chỉ gồm nội dung có nguồn hay ràng buộc kỹ thuật; không có ngưỡng tự đặt.
- [ ] `Data/Integration/Permissions` nêu rõ quyền truy cập và môi trường.
- [ ] Dependency có hệ thống/nhóm sở hữu, không ghi chung chung.
- [ ] `Source References` ghi tới mục/trang, đủ để người khác mở lại đúng chỗ.
- [ ] Không có mâu thuẫn chưa giải quyết giữa các nguồn; nếu có, đã ghi nhận người phân xử.

## Quy tắc gắn nhãn bằng chứng
| Nhãn | Nghĩa | Điều kiện dùng trong tài liệu chính thức |
| --- | --- | --- |
| `[Fact]` | Có nguồn kiểm chứng được | Dùng bình thường |
| `[Assumption]` | Giả định chưa xác nhận | Phải có kế hoạch xác minh và owner |
| `[Inference]` | Suy luận từ nhiều dữ kiện | Phải nêu chuỗi suy luận |
| `[Unknown]` | Chưa biết | Phải thành `Open Questions` |

Nội dung quan trọng mà không gắn được nhãn nào: dừng, không đưa vào tài liệu.

## Quy tắc dừng bước
Dừng và báo thay vì tiếp tục khi:
1. Business Rule quan trọng không tìm được nguồn và không ai xác nhận.
2. Hai nguồn chính thức mâu thuẫn mà chưa có người phân xử.
3. Không tiếp cận được dữ liệu mẫu hoặc API cần cho phân tích.
4. Business chưa xác nhận TO-BE nhưng đã bị yêu cầu chuyển sang đặc tả.
5. AI đề xuất quy tắc, giới hạn hoặc SLA không có trong nguồn — loại bỏ và ghi lại.

Khi dừng: ghi lý do, giữ `Review Status = Draft`, chuyển danh sách việc cần xác minh cho BA và PO.

## Lỗi thường gặp ở G2
| Lỗi | Vì sao nguy hiểm | Cách xử lý |
| --- | --- | --- |
| Viết quy tắc từ kinh nghiệm chung | Tạo chính sách không tồn tại | Xoá hoặc chuyển thành `[Assumption]` + câu hỏi |
| Ghi link tài liệu nhưng không ghi vị trí | Không kiểm chứng được | Bổ sung mục/trang/dòng |
| Coi TO-BE là đã duyệt vì không ai phản đối | Sai thẩm quyền xác nhận | Lấy xác nhận rõ tên + ngày |
| Để `Open Questions` không owner | Câu hỏi không bao giờ đóng | Gán owner ngay khi ghi nhận |
| Gộp rủi ro và giả định | Mất dấu việc cần xác minh | Tách hai mục riêng |

## Người ký G2
BA chịu trách nhiệm nội dung phân tích; Business/Business Owner xác nhận TO-BE và quy tắc nghiệp vụ; PO là người chịu trách nhiệm cuối cùng (A).
