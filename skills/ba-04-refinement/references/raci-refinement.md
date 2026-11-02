# RACI trong Refinement và các tình huống ranh giới

Nguồn: SOP §5 (RACI tham khảo). R = thực hiện; A = chịu trách nhiệm cuối cùng; C = tham vấn; I = thông báo.

## RACI gốc cho hoạt động Refinement

| BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- |
| R | A | R | R | C |

Ba vai trò cùng là R: đây là hoạt động chung của Scrum Team, không phải việc riêng của BA.

## Ai quyết định gì

| Vấn đề | Người quyết định | BA/AI được làm gì |
| --- | --- | --- |
| Thứ tự ưu tiên backlog | PO | Cung cấp ngữ cảnh, không đề xuất thứ tự |
| Estimate / Story Point | Scrum Team | Ghi nhận kết quả, không đề xuất con số |
| Story có đạt DoR hay không | Team (theo tiêu chí) + PO (chấp nhận rủi ro) | Trình bày bằng chứng từng tiêu chí |
| Tách hay gộp Story | Team, PO xác nhận thứ tự | Đề xuất phương án kèm lý do |
| Business Rule trong Story | Business/Business Owner | Trích nguồn, không tự tạo |
| Chấp nhận Story chưa Ready vào Sprint | PO | Ghi quyết định vào Decision Log |
| Khả thi kỹ thuật | Dev/Tech Lead | Ghi nhận ràng buộc |
| Testability | QA | Bổ sung AC khi QA yêu cầu |

## Tình huống ranh giới

### 1. PO vắng mặt, Team muốn chốt thứ tự
Không tự chốt. Ghi nhận các phương án, ghi `Chờ PO` vào `Quyết định thứ tự` của biên bản, giữ Story ở `Ready for Refinement`.

### 2. Team không thống nhất được estimate
Ghi rõ hai phương án và lý do bất đồng; không tự chọn một bên. Đề xuất tách Story nếu bất đồng đến từ phạm vi chưa rõ.

### 3. QA nói AC không kiểm thử được
Đây là lỗi G3 còn sót. Quay lại `ba-03-specification`, sửa AC, không hạ tiêu chí DoR cho qua.

### 4. Dev nói cần thay đổi Business Rule để khả thi
Không tự sửa quy tắc. Mở Change Request qua `ba-05-change-management`; Business Owner là người quyết định.

### 5. AI gợi ý Story đã Ready
Gợi ý của AI là đầu vào cho checklist, không phải xác nhận. Team vẫn phải xác nhận từng tiêu chí.

### 6. Business không tham gia dù là vai trò C
Ghi nhận việc thiếu tham vấn và rủi ro đi kèm; nếu câu hỏi nghiệp vụ chưa đóng thì Story chưa đạt DoR tiêu chí 4.

## Ghi chú về A* trong SOP
SOP đánh dấu `A*` cho PO ở hoạt động "Quản lý thay đổi phạm vi": giả định PO được ủy quyền quản lý phạm vi Product Backlog. Ngân sách, hợp đồng và nghiệm thu chính thức vẫn theo thẩm quyền nội bộ của tổ chức, không thuộc phạm vi quyết định ở refinement.
