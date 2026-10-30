# Gate bàn giao, KPI và checklist tổng thể

## 1. Quality Gate bàn giao (BA-07)

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | Đúng phiên bản | URD/BRD, Business Rules, Story/AC, RTM cùng một phiên bản phát hành | |
| 2 | Có người nhận bàn giao | Tên/bộ phận trong biên bản Handover Pack | |
| 3 | Tài liệu AI đã review | HO-007 `Done`, kèm prompt version, model/version, người review | |
| 4 | Vấn đề mở có owner | Không còn dòng nào trống owner (HO-006) | |

### Tiêu chí bổ sung
- [ ] Mọi Story phát hành đều có `Test Result` và `UAT Result` trong RTM, không còn `Missing Link`.
- [ ] Không còn `Version Mismatch` giữa tài liệu và RTM.
- [ ] Known Issues có mức tác động và cách xử lý tạm.
- [ ] CR còn mở đã được bàn giao kèm `Status` và người theo dõi.
- [ ] Đầu mối hỗ trợ sau bàn giao đã xác định (HO-008).
- [ ] Action Items từ Retrospective có owner và hạn.
- [ ] Không có dữ liệu nhạy cảm trong tài liệu đưa lên Knowledge Base chưa được phê duyệt.

### Quy tắc dừng bước
Dừng và báo khi: chưa có quyết định nghiệm thu; RTM còn `Missing Link` ở Story phát hành; không xác định được người nhận bàn giao; tài liệu AI chưa review nhưng bị yêu cầu xuất bản.

---

## 2. KPI khởi điểm (SOP §9)

| KPI | Cách đo | Mục tiêu ban đầu | Quy trình liên quan |
| --- | --- | --- | --- |
| Requirement Completeness | Yêu cầu đạt checklist / yêu cầu được review | Thử nghiệm ≥95% | BA-01, BA-02, BA-03 |
| AC Testability | AC có thể kiểm thử / AC được review | Thử nghiệm ≥95% | BA-03, BA-04 |
| Traceability Coverage | Yêu cầu cần test có liên kết test phù hợp / tổng yêu cầu cần test | Thử nghiệm ≥95% | BA-03, BA-06 |
| Rework Rate | Yêu cầu phải sửa lớn do phân tích thiếu/sai / yêu cầu triển khai | Đo baseline, sau đó giảm | BA-02, BA-03, BA-05 |
| Clarification Response Time | Thời gian từ câu hỏi đến câu trả lời được xác nhận | Theo SLA dự án | BA-01, BA-02, BA-05 |
| AI Acceptance Rate | Đầu ra AI được chấp nhận với ít hoặc không cần sửa lớn / đầu ra được review | Đo baseline | Mọi quy trình dùng AI |
| AI Unsupported Claim Rate | Kết luận quan trọng không được nguồn hỗ trợ / kết luận được kiểm tra | Hướng tới 0 | Mọi quy trình dùng AI |

SOP ghi rõ: các mục tiêu này là **ngưỡng khởi điểm đề xuất**, không phải chuẩn bắt buộc của Scrum. Đo baseline trong 2–4 Sprint trước khi điều chỉnh. `Traceability Coverage` lấy trực tiếp từ cột `Coverage Status` của RTM.

---

## 3. Checklist tổng thể (SOP §11)

Dùng khi đóng một Release để soát lại toàn chuỗi:

- [ ] Có Requirement ID và nguồn tài liệu → `ba-01`
- [ ] Xác định Business Owner và mục tiêu → `ba-01`
- [ ] Ghi nhận câu hỏi còn thiếu → `ba-01`, `ba-02`
- [ ] Có phạm vi và Stakeholder → `ba-02`
- [ ] Đã phân tích luồng chính và ngoại lệ → `ba-02`
- [ ] Business Rules có nguồn xác nhận → `ba-02`
- [ ] Đã xem xét dependency và rủi ro → `ba-02`
- [ ] User Story/đặc tả phù hợp đã được tạo → `ba-03`
- [ ] Acceptance Criteria kiểm chứng được → `ba-03`
- [ ] Đã review tính nhất quán → `ba-03`, `ba-04`
- [ ] Có liên kết Requirement ID → `ba-03`
- [ ] Thay đổi được ghi nhận và truy vết → `ba-05`
- [ ] Test Case liên kết với AC → `ba-06`
- [ ] Kết quả kiểm thử có bằng chứng → `ba-06`
- [ ] Có UAT Result và quyết định đúng thẩm quyền → `ba-06`
- [ ] Tài liệu đúng phiên bản → `ba-07`
- [ ] Vấn đề còn mở có owner → `ba-07`
- [ ] AI output đã được review trước khi xuất bản → `ba-07` (HO-007)

---

## 4. Chuỗi gate toàn quy trình

| Gate | Cuối quy trình | Điều kiện cốt lõi | Không đạt thì |
| --- | --- | --- | --- |
| G1 | BA-01 | ID, mục tiêu, nguồn, người phụ trách; tách bạch AI | Không vào BA-02 |
| G2 | BA-02 | Rule có nguồn; giả định được đánh dấu; Business xác nhận TO-BE; câu hỏi mở có owner | Không vào BA-03 |
| G3 | BA-03 | AC kiểm thử được; không giấu giả định; có xác nhận và phiên bản | Không vào refinement |
| DoR | BA-04 | 8 tiêu chí DoR tham khảo | Story chưa `Ready for Refinement` |
| Gate thay đổi | BA-05 | Người quyết định, lý do, phiên bản, thông báo, truy vết | Không chuyển `Implemented` |
| G4 | BA-06 | Kết quả có bằng chứng; defect nghiêm trọng đã xử lý hoặc chấp nhận rủi ro đúng thẩm quyền | Không vào BA-07 |
| Gate bàn giao | BA-07 | Đúng phiên bản, người nhận, tài liệu AI đã review, vấn đề mở có owner | Không đóng Release |
