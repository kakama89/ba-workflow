# URD — User Requirements Document

Template này dùng để tạo tài liệu URD chính thức từ kết quả phân tích nghiệp vụ đã đạt gate G2, tập trung vào góc nhìn người dùng cuối.
Sao chép toàn bộ template, điền vào, rồi lưu vào `ba-records/<project>/urd/` hoặc hệ thống quản lý tài liệu đã ánh xạ của dự án.

---

## 1. Thông tin tài liệu

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Document ID | `<URD-000>` | Duy nhất theo dự án; kiểm tra trùng trước khi phát hành |
| Version | `<0.1>` | Tăng theo mỗi lần review có thay đổi nội dung |
| Title | `<tên dự án / tính năng>` | Ngắn gọn, phản ánh đúng phạm vi |
| Owner | `<tên BA phụ trách>` | BA chịu trách nhiệm nội dung |
| Reviewed By | `<người dùng đại diện / Business>` | Người có thẩm quyền review URD |
| Created Date | `<YYYY-MM-DD>` | Ngày tạo bản đầu tiên |
| Last Updated | `<YYYY-MM-DD>` | Ngày cập nhật gần nhất |
| Review Status | `<Draft / In Review / Approved>` | `Draft` cho tới khi người review xác nhận |
| Related Documents | `<BA-DOC-xxx, BRD-xxx, REQ-xxx, …>` | Liên kết tới Business Analysis Document, BRD và Intake Record |

## 2. Tóm tắt (Summary)

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Purpose | `<mục đích của tài liệu>` | URD mô tả yêu cầu từ góc nhìn người dùng cuối |
| System Overview | `<tổng quan hệ thống>` | Mô tả ngắn hệ thống / tính năng mà URD bao phủ |
| Target Users | `<nhóm người dùng chính>` | Liệt kê nhóm người dùng chính; chi tiết ở mục User Profiles |
| Document Scope | `<phạm vi tài liệu>` | Phần nào của hệ thống được mô tả trong URD này |

## 3. User Profiles (Hồ sơ người dùng)

Mỗi nhóm người dùng một bảng. Không tự tạo persona hư cấu — chỉ ghi thông tin có bằng chứng.

### User Profile: `<Tên vai trò>`

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Profile ID | `<UP-001>` | Duy nhất trong tài liệu |
| Role / Vai trò | `<vai trò>` | Vai trò trong hệ thống |
| Description | `<mô tả>` | Đặc điểm, trách nhiệm, bối cảnh sử dụng |
| Technical Proficiency | `<mức độ>` | Kinh nghiệm IT: Thấp / Trung bình / Cao — chỉ khi nguồn nêu |
| Usage Frequency | `<tần suất>` | Hàng ngày / Hàng tuần / Hàng tháng / Không thường xuyên |
| Primary Goals | `<mục tiêu chính>` | Mục tiêu khi sử dụng hệ thống |
| Environment | `<môi trường>` | Thiết bị, trình duyệt, mạng, vị trí sử dụng |
| Source | `<nguồn>` | URL + vị trí trong tài liệu |
| Label | `[Fact] / [Assumption] / [Inference] / [Unknown]` | Nhãn bằng chứng |

> Lặp lại bảng trên cho mỗi nhóm người dùng.

## 4. User Goals (Mục tiêu người dùng)

| Goal ID | User Profile | Mô tả mục tiêu | FR liên kết | Nguồn | Nhãn |
| --- | --- | --- | --- | --- | --- |
| UG-001 | `<UP-xxx>` | `<người dùng muốn …>` | `<FR-xxx>` | `<nguồn>` | `[Fact]` |

## 5. Use Cases

Mỗi Use Case một bảng.

### Use Case: `<UC-001 — Tên Use Case>`

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Use Case ID | `<UC-001>` | Duy nhất trong tài liệu |
| Title | `<tên use case>` | Ngắn gọn, phản ánh hành động chính |
| Actor(s) | `<UP-xxx>` | Liên kết User Profile |
| Goal | `<UG-xxx>` | Liên kết User Goal |
| Preconditions | `<điều kiện tiền đề>` | Trạng thái hệ thống trước khi bắt đầu |
| Trigger | `<sự kiện kích hoạt>` | Hành động hoặc sự kiện bắt đầu use case |
| **Main Flow** | | |
| 1 | `<bước 1>` | Hành động người dùng / phản hồi hệ thống |
| 2 | `<bước 2>` | |
| … | `<…>` | |
| Postconditions | `<kết quả sau khi hoàn tất>` | Trạng thái hệ thống khi kết thúc thành công |
| **Alternative Flows** | | |
| ALT-1 | `<luồng thay thế>` | Kèm điều kiện kích hoạt và bước thay thế |
| **Error / Exception Flows** | | |
| ERR-1 | `<luồng lỗi>` | Kèm điều kiện lỗi và xử lý |
| FR / BR liên kết | `<FR-xxx, BR-xxx>` | Liên kết truy vết |
| Source | `<nguồn>` | URL + vị trí trong tài liệu |

> Lặp lại bảng trên cho mỗi Use Case. Mỗi luồng chính cần ít nhất một luồng lỗi/ngoại lệ.

## 6. User Scenarios (Kịch bản sử dụng)

| Scenario ID | Use Case | Bối cảnh | Hành động người dùng | Phản hồi hệ thống | Kết quả | Loại | Nhãn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCN-001 | `<UC-xxx>` | `<bối cảnh>` | `<hành động>` | `<phản hồi>` | `<kết quả>` | `Success / Error` | `[Fact]` |

## 7. Yêu cầu giao diện (UI Requirements)

| UI ID | Mô tả | Use Case liên kết | Nguồn | Nhãn |
| --- | --- | --- | --- | --- |
| UI-001 | `<yêu cầu giao diện>` | `<UC-xxx>` | `<nguồn>` | `[Fact]` |

> Chỉ ghi yêu cầu giao diện từ nguồn hoặc trao đổi với Business/UX. Không tự thiết kế giao diện.

## 8. Yêu cầu khả dụng (Usability Requirements)

| Usability ID | Mô tả | Tiêu chí đo lường | Nguồn | Nhãn |
| --- | --- | --- | --- | --- |
| USA-001 | `<yêu cầu usability>` | `<tiêu chí>` | `<nguồn>` | `[Fact]` |

> Không tự đặt tiêu chí usability khi nguồn chưa nêu. Thiếu thì tạo câu hỏi mở.

## 9. Yêu cầu Accessibility

| A11Y ID | Mô tả | Chuẩn áp dụng | Mức tuân thủ | Nguồn | Nhãn |
| --- | --- | --- | --- | --- | --- |
| A11Y-001 | `<yêu cầu accessibility>` | `<WCAG 2.1 / …>` | `<A / AA / AAA>` | `<nguồn>` | `[Fact]` |

> Chỉ ghi khi dự án có yêu cầu accessibility; không tự áp dụng chuẩn khi nguồn chưa nêu.

## 10. Tiêu chí chấp nhận của người dùng (User Acceptance Criteria)

| UAC ID | Use Case / Scenario | Tiêu chí chấp nhận | FR liên kết | Nguồn | Nhãn |
| --- | --- | --- | --- | --- | --- |
| UAC-001 | `<UC-xxx / SCN-xxx>` | `<tiêu chí kiểm chứng được>` | `<FR-xxx>` | `<nguồn>` | `[Fact]` |

> Tiêu chí phải kiểm chứng được. Đây là cơ sở cho UAT ở BA-06.

## 11. Giả định và ràng buộc

| Loại | Mô tả | Nguồn / Người xác nhận | Nhãn |
| --- | --- | --- | --- |
| Assumption | `<giả định về người dùng hoặc bối cảnh>` | `<nguồn hoặc người cần xác nhận>` | `[Assumption]` |
| Constraint | `<ràng buộc>` | `<nguồn>` | `[Fact]` |

## 12. Câu hỏi mở (Open Questions)

| # | Câu hỏi | Mục liên quan | Owner | Hạn trả lời | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| 1 | `<câu hỏi>` | `<mục trong URD>` | `<người phụ trách>` | `<ngày>` | `<Open / Resolved>` |

> **Mỗi câu hỏi phải có owner.** Không xoá câu hỏi chưa đóng; đánh dấu `Resolved` kèm ngày và người trả lời.

## 13. Nguồn tham chiếu (Source References)

| # | Tài liệu | Phiên bản | Vị trí | URL |
| --- | --- | --- | --- | --- |
| 1 | `<tên tài liệu>` | `<phiên bản / ngày>` | `<mục / trang / dòng>` | `<URL>` |

> Ghi tới mục/trang, đủ để người khác mở lại đúng chỗ.

## 14. Phê duyệt (Review & Approval)

| Vai trò | Tên | Ngày | Chữ ký / Xác nhận |
| --- | --- | --- | --- |
| BA (soạn) | `<tên>` | `<ngày>` | |
| User đại diện (review) | `<tên>` | `<ngày>` | |
| Business / PO (phê duyệt) | `<tên>` | `<ngày>` | |

---

## Không tự điền (chỉ con người có thẩm quyền)
- `Review Status = Approved` — người dùng đại diện / Business.
- Tiêu chí usability, accessibility chưa có trong nguồn.
- User Profile hư cấu (persona) không có bằng chứng.
- Mức chấp nhận rủi ro liên quan đến trải nghiệm người dùng.
- `Review & Approval` — chữ ký / xác nhận.

## Quy tắc điền
- Nhãn bằng chứng: `[Fact]` có nguồn · `[Assumption]` giả định · `[Inference]` suy luận · `[Unknown]` chưa biết.
- Mỗi Use Case liên kết ít nhất một FR hoặc một nguồn; Use Case không nguồn là điểm phải hỏi.
- Mỗi User Profile phải truy vết được về Actor trong Business Analysis Document.
- User Acceptance Criteria phải kiểm chứng được và có nguồn.
- Không xoá `Open Questions` chưa đóng; đánh dấu `Resolved` kèm ngày và người trả lời.
