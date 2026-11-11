# BRD — Business Requirements Document

Template này dùng để tạo tài liệu BRD chính thức từ kết quả phân tích nghiệp vụ đã đạt gate G2.
Sao chép toàn bộ template, điền vào, rồi lưu vào `ba-records/<project>/brd/` hoặc hệ thống quản lý tài liệu đã ánh xạ của dự án.

---

## 1. Thông tin tài liệu

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Document ID | `<BRD-000>` | Duy nhất theo dự án; kiểm tra trùng trước khi phát hành |
| Version | `<0.1>` | Tăng theo mỗi lần review có thay đổi nội dung |
| Title | `<tên dự án / tính năng>` | Ngắn gọn, phản ánh đúng phạm vi |
| Owner | `<tên BA phụ trách>` | BA chịu trách nhiệm nội dung |
| Sponsor / Business Owner | `<tên người phê duyệt>` | Người có thẩm quyền phê duyệt BRD |
| Created Date | `<YYYY-MM-DD>` | Ngày tạo bản đầu tiên |
| Last Updated | `<YYYY-MM-DD>` | Ngày cập nhật gần nhất |
| Review Status | `<Draft / In Review / Approved>` | `Draft` cho tới khi Sponsor xác nhận |
| Related Documents | `<BA-DOC-xxx, REQ-xxx, …>` | Liên kết tới Business Analysis Document và Intake Record |

## 2. Tóm tắt điều hành (Executive Summary)

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Business Context | `<bối cảnh kinh doanh>` | Tóm tắt tình hình hiện tại và lý do cần thay đổi |
| Business Problem | `<vấn đề kinh doanh>` | Chỉ phần có bằng chứng |
| Proposed Solution | `<giải pháp đề xuất>` | Mô tả tổng quan giải pháp; là đề xuất tới khi được phê duyệt |
| Expected Benefits | `<lợi ích mong đợi>` | Gắn với Success Metrics nếu có nguồn |

## 3. Mục tiêu kinh doanh và chỉ số thành công

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Business Objectives | `<mục tiêu đo lường được>` | Mỗi mục tiêu một dòng, kèm nguồn |
| Success Metrics / KPI | `<chỉ số + ngưỡng>` | Chỉ ghi khi nguồn xác định; thiếu thì tạo câu hỏi mở |
| Alignment | `<chiến lược / mục tiêu tổ chức>` | Ghi cách dự án phục vụ chiến lược nếu nguồn nêu |

## 4. Phạm vi

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| In Scope | `<trong phạm vi>` | Liệt kê rõ ràng các chức năng, quy trình, hệ thống nằm trong phạm vi |
| Out of Scope | `<ngoài phạm vi>` | Liệt kê rõ ràng những gì KHÔNG nằm trong phạm vi |
| Scope Confirmation | `<người xác nhận — ngày>` | Business Owner xác nhận phạm vi |

## 5. Stakeholders

| Vai trò | Tên / Bộ phận | Mối quan tâm | Mức ảnh hưởng | Nguồn |
| --- | --- | --- | --- | --- |
| `<vai trò>` | `<tên / bộ phận>` | `<mối quan tâm chính>` | `<Cao / Trung bình / Thấp>` | `<nguồn>` |

## 6. Hiện trạng và mục tiêu (AS-IS / TO-BE)

### 6.1. AS-IS — Hiện trạng
| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Current Process | `<mô tả quy trình hiện tại>` | Chỉ mô tả phần có bằng chứng |
| Pain Points | `<điểm nghẽn, vấn đề>` | Kèm tác động, không ghi cảm nhận |
| Current Systems | `<hệ thống hiện tại>` | Nêu hệ thống, công cụ đang sử dụng |

### 6.2. TO-BE — Mục tiêu
| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Target Process | `<mô tả quy trình mục tiêu>` | Là **đề xuất** tới khi Business xác nhận |
| Key Changes | `<thay đổi chính>` | So sánh với AS-IS, nêu rõ điểm khác biệt |
| Impact on Stakeholders | `<tác động tới từng nhóm>` | Mỗi nhóm stakeholder một dòng |
| TO-BE Confirmation | `<người xác nhận — ngày>` | Business xác nhận TO-BE tại đây |

## 7. Yêu cầu chức năng (Functional Requirements)

| FR ID | Mô tả | Business Rule liên kết | Requirement ID | Nguồn | Nhãn |
| --- | --- | --- | --- | --- | --- |
| FR-001 | `<mô tả yêu cầu>` | `<BR-xxx>` | `<REQ-xxx>` | `<URL + vị trí>` | `[Fact]` |

## 8. Quy tắc nghiệp vụ (Business Rules Catalog)

| Rule ID | Nội dung quy tắc | Nguồn | Trạng thái xác nhận | Nhãn |
| --- | --- | --- | --- | --- |
| BR-001 | `<quy tắc>` | `<URL + vị trí>` | `<Chưa / Đã xác nhận bởi …>` | `[Fact]` |

## 9. Yêu cầu phi chức năng (Non-Functional Requirements)

| NFR ID | Loại | Mô tả | Ngưỡng / Tiêu chí | Nguồn | Nhãn |
| --- | --- | --- | --- | --- | --- |
| NFR-001 | `<Performance / Security / Usability / …>` | `<mô tả>` | `<ngưỡng>` | `<nguồn>` | `[Fact]` |

> Không tự đặt ngưỡng SLA, hiệu năng hay giới hạn khi nguồn chưa nêu.

## 10. Dữ liệu, tích hợp và phân quyền

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Data Requirements | `<yêu cầu dữ liệu>` | Loại dữ liệu, khối lượng, nguồn dữ liệu |
| Integration Points | `<điểm tích hợp>` | Hệ thống, API, giao thức, môi trường |
| Access & Permissions | `<quyền truy cập>` | Actor, quyền, phạm vi |

## 11. Giả định và ràng buộc

| Loại | Mô tả | Nguồn / Người xác nhận | Nhãn |
| --- | --- | --- | --- |
| Assumption | `<giả định>` | `<nguồn hoặc người cần xác nhận>` | `[Assumption]` |
| Constraint | `<ràng buộc>` | `<nguồn>` | `[Fact]` |

## 12. Rủi ro

| Risk ID | Mô tả rủi ro | Tác động | Dấu hiệu nhận biết | Nguồn | Nhãn |
| --- | --- | --- | --- | --- | --- |
| RISK-001 | `<rủi ro>` | `<tác động>` | `<dấu hiệu>` | `<nguồn>` | `[Fact]` |

> Không tự đề xuất mức chấp nhận rủi ro — thuộc thẩm quyền Business Owner / Sponsor.

## 13. Phụ thuộc (Dependencies)

| Dep ID | Mô tả | Hệ thống / Nhóm sở hữu | Tác động nếu không đáp ứng | Nguồn |
| --- | --- | --- | --- | --- |
| DEP-001 | `<phụ thuộc>` | `<hệ thống / nhóm>` | `<tác động>` | `<nguồn>` |

## 14. Timeline và Milestone

| Milestone | Ngày dự kiến | Ghi chú | Nguồn |
| --- | --- | --- | --- |
| `<milestone>` | `<YYYY-MM-DD>` | `<ghi chú>` | `<nguồn>` |

> Timeline là mong muốn, không phải cam kết; PO/PM quyết định.

## 15. Câu hỏi mở (Open Questions)

| # | Câu hỏi | Mục liên quan | Owner | Hạn trả lời | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| 1 | `<câu hỏi>` | `<mục trong BRD>` | `<người phụ trách>` | `<ngày>` | `<Open / Resolved>` |

> **Mỗi câu hỏi phải có owner.** Không xoá câu hỏi chưa đóng; đánh dấu `Resolved` kèm ngày và người trả lời.

## 16. Quyết định đã có (Decision Log)

| # | Ngày | Quyết định | Người quyết định | Bối cảnh |
| --- | --- | --- | --- | --- |
| 1 | `<YYYY-MM-DD>` | `<quyết định>` | `<tên>` | `<bối cảnh>` |

## 17. Nguồn tham chiếu (Source References)

| # | Tài liệu | Phiên bản | Vị trí | URL |
| --- | --- | --- | --- | --- |
| 1 | `<tên tài liệu>` | `<phiên bản / ngày>` | `<mục / trang / dòng>` | `<URL>` |

> Ghi tới mục/trang, đủ để người khác mở lại đúng chỗ.

## 18. Phê duyệt (Review & Approval)

| Vai trò | Tên | Ngày | Chữ ký / Xác nhận |
| --- | --- | --- | --- |
| BA (soạn) | `<tên>` | `<ngày>` | |
| Business Owner / Sponsor (phê duyệt) | `<tên>` | `<ngày>` | |
| PO (xác nhận) | `<tên>` | `<ngày>` | |

---

## Không tự điền (chỉ con người có thẩm quyền)
- `Review Status = Approved` — Sponsor / Business Owner.
- `Scope Confirmation`, `TO-BE Confirmation`.
- Ngưỡng NFR, SLA, Success Metrics chưa có trong nguồn.
- Mức chấp nhận rủi ro.
- Timeline dưới dạng cam kết.
- `Review & Approval` — chữ ký / xác nhận.

## Quy tắc điền
- Nhãn bằng chứng: `[Fact]` có nguồn · `[Assumption]` giả định · `[Inference]` suy luận · `[Unknown]` chưa biết.
- Mỗi FR nên trỏ về ít nhất một BR hoặc một nguồn; FR không nguồn là điểm phải hỏi.
- Mỗi mục trong BRD phải truy vết được về nguồn trong `Source References`.
- Không xoá `Open Questions` chưa đóng; đánh dấu `Resolved` kèm ngày và người trả lời.
