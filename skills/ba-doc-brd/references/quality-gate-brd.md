# Quality Gate BRD — Tài liệu Business Requirements Document

Gate này đóng lại quá trình tạo BRD. Không đạt gate thì BRD chưa được phê duyệt và phân phối.

## Checklist bắt buộc

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | Yêu cầu có nguồn | Mỗi `FR-xxx` và `NFR-xxx` trỏ được tới nguồn và Requirement ID | |
| 2 | Quy tắc nghiệp vụ có nguồn | Mỗi `BR-xxx` trỏ được tới URL + vị trí trong tài liệu | |
| 3 | Giả định được đánh dấu | Mọi nội dung chưa xác nhận đều gắn `[Assumption]` hoặc `[Unknown]` | |
| 4 | Phạm vi đã xác nhận | Có tên Business Owner và ngày xác nhận trong mục Scope Confirmation | |
| 5 | Success Metrics có nguồn | Mỗi KPI/Metric có nguồn, hoặc được ghi nhận là câu hỏi mở | |
| 6 | Câu hỏi mở có owner | Không còn `Open Questions` để trống người phụ trách | |
| 7 | TO-BE đã xác nhận | Có tên người xác nhận và ngày trong mục TO-BE Confirmation | |
| 8 | Truy vết đầy đủ | Mỗi FR liên kết được tới Requirement ID gốc từ Intake Record | |

## Tiêu chí bổ sung nên kiểm tra
- [ ] Executive Summary phản ánh đúng nội dung chi tiết, không mâu thuẫn.
- [ ] AS-IS chỉ chứa nội dung có bằng chứng, không lẫn đề xuất cải tiến.
- [ ] NFR chỉ gồm nội dung có nguồn hay ràng buộc kỹ thuật; không có ngưỡng tự đặt.
- [ ] Dữ liệu, tích hợp và phân quyền nêu rõ hệ thống và quyền truy cập.
- [ ] Dependency có hệ thống/nhóm sở hữu, không ghi chung chung.
- [ ] Source References ghi tới mục/trang, đủ để người khác mở lại đúng chỗ.
- [ ] Không có mâu thuẫn chưa giải quyết giữa các nguồn; nếu có, đã ghi nhận người phân xử.
- [ ] Rủi ro có tác động và dấu hiệu nhận biết, không tự gán mức chấp nhận.
- [ ] Timeline ghi rõ là mong muốn, không phải cam kết.
- [ ] Decision Log ghi đủ ngày, quyết định, người quyết định.

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
1. Business Analysis Document chưa đạt G2.
2. Business Rule quan trọng không tìm được nguồn và không ai xác nhận.
3. Hai nguồn chính thức mâu thuẫn mà chưa có người phân xử.
4. Business Owner chưa xác nhận phạm vi nhưng đã bị yêu cầu phê duyệt BRD.
5. AI đề xuất yêu cầu, giới hạn hoặc SLA không có trong nguồn — loại bỏ và ghi lại.
6. Không truy cập được tài liệu nghiệp vụ cần đối chiếu.

Khi dừng: ghi lý do, giữ `Review Status = Draft`, chuyển danh sách việc cần xác minh cho BA và Business Owner.

## Lỗi thường gặp ở gate BRD
| Lỗi | Vì sao nguy hiểm | Cách xử lý |
| --- | --- | --- |
| Copy nguyên Business Analysis Document thành BRD | BRD thiếu cấu trúc, thiếu Executive Summary, thiếu phê duyệt | Soạn BRD theo template chuẩn, bổ sung các mục BRD riêng |
| Tự đặt Success Metrics / KPI | Cam kết không có cơ sở | Chuyển thành câu hỏi mở, hỏi Sponsor |
| Ghi nguồn nhưng thiếu phiên bản | Không tái lập được bằng chứng | Yêu cầu URL + phiên bản/ngày |
| Coi TO-BE là đã duyệt vì không ai phản đối | Sai thẩm quyền xác nhận | Lấy xác nhận rõ tên + ngày |
| Để `Open Questions` không owner | Câu hỏi không bao giờ đóng | Gán owner ngay khi ghi nhận |
| BRD và Business Analysis Document mâu thuẫn | Hai nguồn sự thật | Đồng bộ và ghi nhận phiên bản |

## Người ký gate BRD
BA chịu trách nhiệm soạn nội dung BRD; Business Owner / Sponsor phê duyệt; PO xác nhận tính khả thi và ưu tiên.
