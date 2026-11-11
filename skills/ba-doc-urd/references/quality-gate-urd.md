# Quality Gate URD — Tài liệu User Requirements Document

Gate này đóng lại quá trình tạo URD. Không đạt gate thì URD chưa được phê duyệt và phân phối.

## Checklist bắt buộc

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | User Profile có nguồn | Mỗi `UP-xxx` trỏ được tới nguồn xác định vai trò và bối cảnh | |
| 2 | Use Case đầy đủ luồng | Mỗi Use Case có luồng chính và ít nhất một luồng lỗi/ngoại lệ | |
| 3 | Use Case liên kết FR/BR | Mỗi Use Case trỏ được tới `FR-xxx` hoặc `BR-xxx` | |
| 4 | Tiêu chí chấp nhận kiểm chứng được | Mỗi `UAC-xxx` có điều kiện đầu vào, hành động và kết quả quan sát được | |
| 5 | Giả định được đánh dấu | Mọi nội dung chưa xác nhận đều gắn `[Assumption]` hoặc `[Unknown]` | |
| 6 | Câu hỏi mở có owner | Không còn `Open Questions` để trống người phụ trách | |
| 7 | Người dùng đại diện đã review | Có tên người review và ngày trong `Review & Approval` | |
| 8 | Truy vết đầy đủ | Mỗi User Profile liên kết về Actor trong Business Analysis Document | |

## Tiêu chí bổ sung nên kiểm tra
- [ ] Summary phản ánh đúng nội dung chi tiết, không mâu thuẫn.
- [ ] User Scenarios bao phủ cả kịch bản thành công và kịch bản lỗi.
- [ ] Yêu cầu UI chỉ chứa nội dung từ nguồn hoặc trao đổi với Business/UX; không tự thiết kế.
- [ ] Yêu cầu usability có tiêu chí đo lường và nguồn; không có ngưỡng tự đặt.
- [ ] Yêu cầu accessibility ghi rõ chuẩn áp dụng và mức tuân thủ.
- [ ] Source References ghi tới mục/trang, đủ để người khác mở lại đúng chỗ.
- [ ] Không có mâu thuẫn chưa giải quyết giữa các nguồn; nếu có, đã ghi nhận người phân xử.
- [ ] User Acceptance Criteria liên kết về FR và nguồn, đủ để dùng cho UAT.
- [ ] Mỗi User Goal liên kết ít nhất một Use Case.

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
2. Không có thông tin về Actor hoặc người dùng — không thể lập User Profile.
3. Hai nguồn mâu thuẫn về hành vi người dùng mà chưa có người phân xử.
4. Người dùng đại diện chưa review nhưng đã bị yêu cầu phê duyệt URD.
5. AI tự tạo persona hoặc hành vi người dùng không có trong nguồn — loại bỏ và ghi lại.
6. Không truy cập được tài liệu UI/UX hoặc kết quả khảo sát người dùng cần đối chiếu.

Khi dừng: ghi lý do, giữ `Review Status = Draft`, chuyển danh sách việc cần xác minh cho BA và Business.

## Lỗi thường gặp ở gate URD
| Lỗi | Vì sao nguy hiểm | Cách xử lý |
| --- | --- | --- |
| Tự tạo persona không có bằng chứng | User Profile sai, dẫn đến yêu cầu sai | Chỉ ghi User Profile từ nguồn; thiếu thì hỏi |
| Use Case thiếu luồng lỗi | Hệ thống không xử lý ngoại lệ | Mỗi luồng chính cần ít nhất một luồng lỗi |
| Tiêu chí chấp nhận không kiểm chứng được | UAT không thể thực hiện | Viết lại với điều kiện, hành động, kết quả cụ thể |
| Tự đặt tiêu chí usability | Cam kết không có cơ sở | Chuyển thành câu hỏi mở, hỏi UX/Business |
| Ghi nguồn nhưng thiếu phiên bản | Không tái lập được bằng chứng | Yêu cầu URL + phiên bản/ngày |
| Để `Open Questions` không owner | Câu hỏi không bao giờ đóng | Gán owner ngay khi ghi nhận |
| User Profile không liên kết về Actor | Mất truy vết | Mỗi UP phải trỏ về Actor trong BA Document |

## Người ký gate URD
BA chịu trách nhiệm soạn nội dung URD; người dùng đại diện / Business review tính chính xác của yêu cầu; PO xác nhận tính khả thi và ưu tiên.
