# Bộ Template BA — cấu trúc workbook (v1.0)

> **Bản lưu trữ dạng văn bản.** Trích xuất trực tiếp từ `02_Bo_Template_BA.xlsx` (phiên bản 1.0) bằng openpyxl, không gõ lại tay.
> File .xlsx gốc đã bị xoá theo quyết định của chủ tài liệu.
> Đã kiểm tra file gốc: **0 công thức, 0 data validation, 0 conditional formatting, không chart, không ảnh, không comment, không defined name** — nên toàn bộ nội dung đều được giữ lại bên dưới.
> Thứ **không** được giữ: màu ô, font, độ rộng cột, freeze pane (mọi sheet đều freeze tại `A2`).

Danh sách sheet: `README`, `Intake`, `Analysis`, `User Story AC`, `RTM`, `Change Log`, `UAT Report`, `Handover`, `AI Review`

---

## Sheet `README`

Kích thước: 5 dòng x 2 cột · freeze pane: `A2`

| BỘ TEMPLATE BA AGILE/SCRUM CÓ AI AGENT |   |
| --- | --- |
| Phiên bản | 1.0 |
| Hướng dẫn | Mỗi sheet là một biểu mẫu có thể điền trực tiếp. Thay các giá trị ví dụ bằng dữ liệu dự án thực tế. |
| Lưu ý | AI tạo bản nháp; BA/PO/Business xác nhận theo thẩm quyền trước khi dùng làm nguồn chính thức. |
| Sheets | Intake, Analysis, User Story AC, RTM, Change Log, UAT Report, Handover, AI Review |

## Sheet `Intake`

Kích thước: 2 dòng x 16 cột · freeze pane: `A2`

| Requirement ID | Request Title | Requester | Business Owner | Business Problem | Business Objective | Scope | Out of Scope | Priority | Source Documents + Version | Dependencies | Target Date | Open Questions | AI Review Status | BA/PO Decision | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | Tra cứu thông tin doanh nghiệp | Tên người yêu cầu | Business Owner | Mô tả vấn đề hiện tại | Kết quả mong muốn | Phạm vi dự kiến | Ngoài phạm vi | PO xác định | URL tài liệu và phiên bản |   |   | Nguồn dữ liệu nào là chính thức? | Draft - cần review | Chưa quyết định | Clarification Required |

Số cột: **16**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.

## Sheet `Analysis`

Kích thước: 2 dòng x 19 cột · freeze pane: `A2`

| Document ID | Version | Business Problem | Business Objective | Scope | Stakeholders | AS-IS | TO-BE | Functional Requirements | Business Rules | NFR | Data/Integration/Permissions | Alternative/Error Flows | Assumptions | Risks | Dependencies | Open Questions | Source References | Review Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BA-DOC-001 | 0.1 | Mô tả vấn đề | Mục tiêu đo lường được | Trong phạm vi | Stakeholder liên quan | Mô tả hiện trạng | Mô tả mục tiêu | FR-001... | BR-001... | NFR-001... | API/dữ liệu/quyền | Ngoại lệ | Ghi rõ giả định | Rủi ro | Dependency | Câu hỏi mở | URL + vị trí | Draft |

Số cột: **19**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.

## Sheet `User Story AC`

Kích thước: 2 dòng x 18 cột · freeze pane: `A2`

| Epic ID | Story ID | Title | As a | I want | So that | Business Value | Requirement IDs | Business Rule IDs | AC ID | Given | When | Then | Validation/Error Cases | Data/Permissions/Integration | NFR | Open Questions | Review Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPIC-001 | US-001 | Tra cứu thông tin doanh nghiệp | Nhân viên nghiệp vụ | Tra cứu theo mã số thuế | Xác minh thông tin nhanh hơn | Mô tả giá trị | REQ-001 | BR-001 | AC-01 | Người dùng có quyền và nhập mã hợp lệ | Gửi yêu cầu tra cứu | Trả về dữ liệu theo nguồn đã thống nhất |   | Cần xác nhận quy tắc validation |   | Nguồn dữ liệu nào là chính thức? | Draft |

Số cột: **18**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.

## Sheet `RTM`

Kích thước: 2 dòng x 10 cột · freeze pane: `A2`

| Requirement ID | Story ID | AC ID | Test Case ID | Test Result | UAT Result | Evidence Link | Version | Coverage Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | US-001 | AC-01 | TC-001 | Not Run | Not Run |   | 0.1 | Pending | Ví dụ minh họa |

Số cột: **10**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.

## Sheet `Change Log`

Kích thước: 2 dòng x 13 cột · freeze pane: `A2`

| Decision/CR ID | Date | Requester | Current Requirement | Proposed Change | Business Reason | Impact Analysis | Options | Decision | Approver | Effective Version | Communication | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR-001 |   | Tên người yêu cầu | Mô tả hiện tại | Đề xuất thay đổi | Lý do | Story/API/Data/Test/Sprint impact | Các phương án | Pending | Người có thẩm quyền |   |   | Proposed |

Số cột: **13**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.

## Sheet `UAT Report`

Kích thước: 2 dòng x 17 cột · freeze pane: `A2`

| Project | Release/Build | Environment | UAT Date | Business Owner | Participants | Scenario ID | Scenario Description | Expected Result | Actual Result | Status | Defect ID | Severity | Evidence Link | Decision | Approver | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tên dự án | v1.0 | UAT |   | Business Owner | Người tham gia | UAT-001 | Mô tả kịch bản | Kết quả mong đợi | Kết quả thực tế | Not Run |   |   |   | Pending |   | Ví dụ minh họa |

Số cột: **17**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.

## Sheet `Handover`

Kích thước: 9 dòng x 7 cột · freeze pane: `A2`

| Checklist ID | Hạng mục | Status | Evidence/Link | Owner | Due Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| HO-001 | Danh sách Story phát hành được xác nhận | Not Started |   | BA |   |   |
| HO-002 | URD/BRD và Business Rules đúng phiên bản | Not Started |   | BA |   |   |
| HO-003 | Release Notes và Known Issues cập nhật | Not Started |   | BA/PO |   |   |
| HO-004 | Test Result và UAT Result được lưu trữ | Not Started |   | QA/BA |   |   |
| HO-005 | CR chưa thực hiện đã được bàn giao | Not Started |   | BA/PO |   |   |
| HO-006 | Vấn đề còn mở có người phụ trách | Not Started |   | Owner |   |   |
| HO-007 | AI output đã review trước khi xuất bản | Not Started |   | BA |   |   |
| HO-008 | Đầu mối hỗ trợ sau phát hành đã xác định | Not Started |   | PO/Business |   |   |

Số cột: **7**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.

## Sheet `AI Review`

Kích thước: 2 dòng x 15 cột · freeze pane: `A2`

| Review ID | Artifact Type | Artifact ID | Source References | Check Category | Finding | Severity | Evidence | Suggested Action | Owner | Status | Reviewer | Prompt Version | Model/Version | Review Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AIR-001 | User Story | US-001 | URL + vị trí | Testability | AC chưa xác định hành vi khi không có dữ liệu | Major | AC-03 | Xác minh quy tắc với Business | BA | Open |   | 1.0 |   |   |

Số cột: **15**. Dòng 2 là dòng ví dụ minh hoạ — thay bằng dữ liệu dự án thực tế.
