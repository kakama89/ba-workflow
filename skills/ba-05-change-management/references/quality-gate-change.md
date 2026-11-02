# Quality Gate thay đổi — BA-05

SOP không đánh số gate cho BA-05. Điều kiện kiểm soát thay đổi: **có người quyết định, lý do, phiên bản, thông báo và truy vết thay đổi.**

## Checklist bắt buộc

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | Có người quyết định | `Approver` là người đúng thẩm quyền, không để trống | |
| 2 | Có lý do | `Business Reason` ghi rõ, không phải câu chung chung | |
| 3 | Có phiên bản | `Effective Version` xác định được tài liệu áp dụng | |
| 4 | Có thông báo | `Communication` nêu ai, kênh nào, ngày nào | |
| 5 | Truy vết thay đổi | RTM, Story/AC, Business Rules đã cập nhật theo phiên bản mới | |

## Tiêu chí bổ sung nên kiểm tra
- [ ] `Current Requirement` và `Proposed Change` tách bạch, không diễn giải lẫn nhau.
- [ ] `Impact Analysis` liệt kê đủ 8 nhóm đối tượng, mỗi nhóm có ID cụ thể hoặc ghi rõ "không ảnh hưởng".
- [ ] Có tối thiểu hai `Options` khi bài toán cho phép, kèm hệ quả từng phương án.
- [ ] Ảnh hưởng do AI đề xuất đã được BA kiểm tra và bỏ nhãn `[AI đề xuất - chưa xác minh]`.
- [ ] Test Case bị ảnh hưởng đã được xác định và chuyển cho QA.
- [ ] Thay đổi vượt thẩm quyền PO (ngân sách, hợp đồng, nghiệm thu) đã được chuyển đúng cấp.
- [ ] `Status` phản ánh đúng thực tế, không nhảy thẳng sang `Implemented`.

## Quy tắc phân tích ảnh hưởng
Kiểm tra theo thứ tự, dừng lại ở nhóm nào không xác định được thì ghi `Unknown` và hỏi:

1. **Story / AC** — hành vi nào thay đổi, AC nào phải viết lại.
2. **Business Rules** — quy tắc nào bị sửa, bổ sung hoặc huỷ; nguồn mới là gì.
3. **API / interface** — contract nào đổi, có breaking change với hệ thống khác không.
4. **Dữ liệu** — cấu trúc, giá trị hiện có, nhu cầu migration, khả năng rollback.
5. **Test Case** — case nào phải sửa, case nào mất hiệu lực, có cần case mới.
6. **Tài liệu** — URD/BRD, Business Rules Catalog, hướng dẫn sử dụng, FAQ.
7. **Sprint** — Sprint hiện tại có phải dừng việc, Sprint kế tiếp có đổi phạm vi.
8. **RTM** — dòng nào cần cập nhật, có phát sinh `Version Mismatch` hay `Missing Link`.

## Quy tắc dừng bước
Dừng và báo thay vì tiếp tục khi:
1. Không xác định được người có thẩm quyền phê duyệt.
2. Thay đổi chạm dữ liệu production hoặc migration mà chưa có ủy quyền rõ.
3. AI so sánh phiên bản nhưng không truy cập được bản cũ — không tự dựng lại nội dung cũ.
4. Impact Analysis còn mục `Unknown` ở nhóm API hoặc dữ liệu.
5. Bị yêu cầu cập nhật tài liệu trước khi có quyết định.
6. Hai CR mâu thuẫn nhau và chưa có người phân xử.

Khi dừng: giữ `Status = Proposed` hoặc `Under Review`, ghi rõ việc còn thiếu, báo BA và PO. Không cập nhật Story/AC/RTM.

## Lỗi thường gặp
| Lỗi | Vì sao nguy hiểm | Cách xử lý |
| --- | --- | --- |
| Sửa Story trước, ghi CR sau | Mất truy vết, không rollback được | Ghi CR trước khi sửa |
| `Business Reason` viết lại theo suy luận của BA | Sai căn cứ quyết định | Trích theo lời người đề xuất |
| Bỏ sót Test Case trong Impact Analysis | Defect lọt sang UAT | Rà nhóm 5 bằng `ba-agent-traceability` |
| Để `Communication` trống | Bên bị ảnh hưởng không biết | Gate không đạt, chưa chuyển `Implemented` |
| Coi im lặng là đồng ý | Phê duyệt sai thẩm quyền | Lấy xác nhận rõ tên + ngày |
| Xoá CR bị `Rejected` | Mất lịch sử quyết định | Giữ lại, ghi lý do |
| Tin liên kết AI suy luận | Ảnh hưởng bị bỏ sót | BA kiểm tra từng liên kết |

## Người ký gate
BA lập hồ sơ và phân tích ảnh hưởng; PO là người chịu trách nhiệm cuối cùng (A*) trong phạm vi Product Backlog được ủy quyền; Business Owner quyết định khi thay đổi chạm quy tắc nghiệp vụ; cấp cao hơn quyết định khi chạm ngân sách, hợp đồng hoặc nghiệm thu chính thức.
