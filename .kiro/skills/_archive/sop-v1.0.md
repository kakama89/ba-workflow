# SOP — Bộ quy trình BA chuẩn hóa Agile/Scrum có tích hợp AI Agent (v1.0)

> **Bản lưu trữ dạng văn bản.** Trích xuất trực tiếp từ `01_SOP_BA_Agile_AI.docx` (phiên bản 1.0) bằng python-docx, không gõ lại tay.
> File .docx gốc đã bị xoá theo quyết định của chủ tài liệu. Bản này giữ **toàn bộ nội dung chữ**: 234 đoạn văn và 3 bảng (110 ô).
> Đã kiểm tra file gốc không chứa ảnh, media, drawing, textbox, OLE object, comment, footnote, endnote, header hay footer — nên không có nội dung phi văn bản nào bị mất.
> Thứ **không** được giữ: định dạng trực quan (font, cỡ chữ, màu, canh lề, số trang).

---

BỘ QUY TRÌNH BA CHUẨN HÓA
AGILE/SCRUM CÓ TÍCH HỢP AI AGENT

Phiên bản 1.0 | Tài liệu khung áp dụng cho dự án phát triển phần mềm

## 1. Mục đích

Chuẩn hóa hoạt động Business Analysis (BA) từ tiếp nhận yêu cầu đến nghiệm thu; nâng cao tính đầy đủ, rõ ràng, kiểm thử được và truy vết được của yêu cầu; ứng dụng AI Agent để hỗ trợ phân tích và soạn thảo nhưng duy trì kiểm soát của con người.

## 2. Phạm vi áp dụng

- Áp dụng cho dự án phần mềm sử dụng Agile/Scrum.

- Bao gồm tiếp nhận, khảo sát, phân tích, đặc tả, refinement, hỗ trợ phát triển, kiểm thử, UAT, bàn giao và quản lý thay đổi.

- AI Agent chỉ tạo đề xuất/bản nháp và thực hiện tác vụ được cấp quyền; không tự phê duyệt yêu cầu, thay đổi phạm vi hoặc nghiệm thu.

- Các biểu mẫu có thể triển khai trong Jira/Azure DevOps, Confluence, SharePoint hoặc hệ thống tương đương.

## 3. Nguyên tắc vận hành

- Nguồn sự thật: sử dụng tài liệu và hệ thống đã được tổ chức xác định làm nguồn chính thức.

- Không suy diễn: phân biệt Fact, Assumption, Inference và Unknown.

- Human-in-the-loop: BA review nội dung; PO/Business xác nhận theo thẩm quyền.

- Traceability: liên kết Requirement → Story → Acceptance Criteria → Test Case → Test Result/UAT.

- Agile: phân tích theo mức độ cần thiết, lặp lại theo từng Sprint; không yêu cầu hoàn thiện toàn bộ tài liệu trước khi bắt đầu phát triển.

- Bảo mật: chỉ dùng dữ liệu và connector được phê duyệt; không đưa bí mật hoặc dữ liệu nhạy cảm vào dịch vụ chưa được phép.

## 4. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm |
| --- | --- |
| Business User/Stakeholder | Cung cấp nhu cầu, quy tắc nghiệp vụ, dữ liệu mẫu; tham gia xác nhận. |
| Product Owner (PO) | Quản lý Product Backlog, ưu tiên giá trị, quyết định thứ tự công việc và chấp nhận theo thẩm quyền. |
| Business Analyst (BA) | Khảo sát, phân tích, đặc tả, làm rõ, quản lý truy vết và duy trì tính nhất quán. |
| Scrum Master | Hỗ trợ Scrum Team, xử lý trở ngại và cải tiến cách làm việc. |
| Tech Lead/Architect | Đánh giá khả thi, kiến trúc, tích hợp và ràng buộc kỹ thuật. |
| Developer | Thiết kế/triển khai kỹ thuật, unit test và phản hồi khả thi. |
| QA/Tester | Thiết kế và thực hiện kiểm thử, quản lý defect, xác minh bằng chứng. |
| UAT Owner/Business Approver | Tổ chức hoặc thực hiện UAT và quyết định nghiệm thu theo phân quyền. |
| AI Agent | Trích xuất, tạo bản nháp, kiểm tra checklist, tìm mâu thuẫn và hỗ trợ truy vết. |

## 5. RACI tham khảo

| Hoạt động | BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- | --- |
| Tiếp nhận và phân loại yêu cầu | R | A | I | I | C |
| Khảo sát nghiệp vụ | R | A | C | C | C |
| Đặc tả yêu cầu | R | A | C | C | C |
| Ưu tiên Product Backlog | C | A/R | C | C | C |
| Refinement | R | A | R | R | C |
| Thiết kế giải pháp kỹ thuật | C | I | A/R | C | I |
| Thiết kế Test Case | C | I | C | A/R | C |
| UAT và xác nhận nghiệp vụ | C | C | I | R/C | A/R |
| Quản lý thay đổi phạm vi | R | A* | C | C | C |
| Bàn giao tài liệu nghiệp vụ | A/R | C | C | C | I |

R = thực hiện; A = chịu trách nhiệm cuối cùng; C = tham vấn; I = thông báo. A* giả định PO được ủy quyền quản lý phạm vi Product Backlog; tuân thủ thẩm quyền nội bộ đối với ngân sách, hợp đồng và nghiệm thu chính thức.

## BA-01. Tiếp nhận và sàng lọc yêu cầu

Mục tiêu: ghi nhận yêu cầu đúng nguồn, có người phụ trách và xác định đủ thông tin ban đầu.

- Đầu vào: Business Request, email/ticket, URD/BRD/Confluence, mục tiêu và thời hạn mong muốn.

- Bước 1: tạo Requirement ID duy nhất và ghi nhận nguồn, người yêu cầu, Business Owner.

- Bước 2: phân loại New Feature, Enhancement, Defect, Technical Change hoặc Compliance.

- Bước 3: kiểm tra tài liệu, phiên bản, phạm vi sơ bộ, dependency và quyền truy cập.

- Bước 4: AI trích xuất mục tiêu, dữ kiện, câu hỏi thiếu, trùng lặp và mâu thuẫn; dẫn nguồn.

- Bước 5: BA xác minh; trao đổi với người yêu cầu; PO/người có thẩm quyền quyết định bước tiếp theo.

- Đầu ra: Requirement Intake Record, Open Questions, danh sách nguồn và trạng thái.

- Quality Gate G1: có ID, mục tiêu, nguồn, người phụ trách; phân biệt rõ bản nháp AI với nội dung đã xác nhận.

## BA-02. Khảo sát và phân tích nghiệp vụ

Mục tiêu: hiểu vấn đề, quy trình hiện tại, quy trình mong muốn và các quy tắc nghiệp vụ.

- Đầu vào: yêu cầu đã sàng lọc, tài liệu, dữ liệu mẫu, hệ thống/API liên quan.

- Bước 1: xác định Stakeholder, Actor, mục tiêu và phạm vi.

- Bước 2: mô tả AS-IS, vấn đề và điểm nghẽn; đề xuất TO-BE.

- Bước 3: lập Business Rules Catalog; xác định luồng chính, thay thế, lỗi và ngoại lệ.

- Bước 4: phân loại Functional Requirements, NFR, dữ liệu, quyền và tích hợp.

- Bước 5: đánh giá dependency, rủi ro và ảnh hưởng hệ thống.

- Bước 6: AI đối chiếu tài liệu và gợi ý điểm thiếu/mâu thuẫn; BA xác minh với Business.

- Đầu ra: Stakeholder Map, Process Flow, Business Rules, requirements, risks, dependencies.

- Quality Gate G2: quy tắc có nguồn; giả định được đánh dấu; Business xác nhận TO-BE; câu hỏi mở có owner.

## BA-03. Đặc tả và xác nhận yêu cầu

Mục tiêu: chuyển nhu cầu thành yêu cầu rõ ràng, có thể phát triển và kiểm thử.

- Đầu vào: kết quả phân tích, Business Rules, Process Flow và mục tiêu Product.

- Bước 1: phân rã Epic/Feature/User Story khi phù hợp.

- Bước 2: viết User Story và Acceptance Criteria kiểm chứng được.

- Bước 3: mô tả validation, dữ liệu, trạng thái, quyền, thông báo, lỗi và NFR khi áp dụng.

- Bước 4: liên kết Requirement ID, Business Rule ID và nguồn.

- Bước 5: AI tạo bản nháp và kiểm tra mơ hồ, thiếu luồng, trùng lặp, mâu thuẫn.

- Bước 6: BA review; Dev/Tech Lead/QA tham gia; PO/Business xác nhận theo thẩm quyền.

- Đầu ra: URD/BRD hoặc đặc tả phù hợp, Story, AC, RTM, Decision Log.

- Quality Gate G3: AC kiểm thử được; không che giấu giả định; có xác nhận và phiên bản.

## BA-04. Refinement và chuẩn bị Sprint

Mục tiêu: giúp Scrum Team hiểu yêu cầu, chia nhỏ công việc và đánh giá khả năng hoàn thành.

- Đầu vào: Product Backlog, Story/AC, dependency, Product Goal và năng lực dự kiến.

- Bước 1: BA chuẩn bị nội dung và câu hỏi còn mở.

- Bước 2: PO làm rõ giá trị và thứ tự ưu tiên.

- Bước 3: Dev/Tech Lead đánh giá khả thi và dependency; QA đánh giá testability.

- Bước 4: Scrum Team chia nhỏ Story và ước lượng theo cách nhóm thống nhất.

- Bước 5: AI rà soát checklist và gợi ý câu hỏi; con người xác nhận.

- Đầu ra: Backlog được làm rõ, estimate do Team thống nhất, dependency và trạng thái sẵn sàng.

- DoR tham khảo (không bắt buộc theo Scrum Guide): mục tiêu rõ, AC, câu hỏi quan trọng đã xử lý, dependency xác định, testability đủ.

## BA-05. Hỗ trợ phát triển và quản lý thay đổi

Mục tiêu: bảo đảm cách hiểu nghiệp vụ nhất quán và thay đổi được kiểm soát.

- Đầu vào: Sprint Backlog, Story/AC, câu hỏi từ Dev/QA/Business, Change Request.

- Bước 1: BA trả lời câu hỏi dựa trên nguồn đã xác nhận và ghi nhận quyết định.

- Bước 2: khi thay đổi yêu cầu, ghi nhận CR và phân tích ảnh hưởng.

- Bước 3: xác định Story, AC, API, dữ liệu, Test Case, tài liệu và Sprint bị ảnh hưởng.

- Bước 4: PO quyết định ưu tiên và cách xử lý Product Backlog; Team xử lý Sprint theo Scrum.

- Bước 5: AI so sánh phiên bản và đề xuất liên kết bị ảnh hưởng; BA kiểm tra.

- Đầu ra: Decision Log, Change Request, Impact Analysis, tài liệu cập nhật.

- Quality Gate: có người quyết định, lý do, phiên bản, thông báo và truy vết thay đổi.

## BA-06. Kiểm thử, UAT và nghiệm thu nghiệp vụ

Mục tiêu: xác minh sản phẩm đáp ứng yêu cầu bằng bằng chứng và hỗ trợ quyết định nghiệm thu.

- Đầu vào: Story/AC, Business Rules, build test, Test Plan/Case, tiêu chí nghiệm thu.

- Bước 1: BA và QA review liên kết yêu cầu–AC–Test Case.

- Bước 2: QA thực hiện kiểm thử; BA giải thích quy tắc nghiệp vụ và kết quả mong đợi.

- Bước 3: phân loại sai khác thành defect, requirement gap hoặc change request.

- Bước 4: chuẩn bị UAT Scenario, dữ liệu và hướng dẫn Business User.

- Bước 5: Business User thực hiện UAT; BA ghi nhận bằng chứng và kết quả.

- Bước 6: tổng hợp Pass/Fail/Blocked, defect và rủi ro; cập nhật RTM.

- Bước 7: người có thẩm quyền quyết định Accept/Reject/Conditional Acceptance nếu được phép.

- Đầu ra: Test Review, RTM, UAT Report, Defect Log và quyết định nghiệm thu.

- Quality Gate G4: kết quả có bằng chứng; defect nghiêm trọng được xử lý hoặc chấp nhận rủi ro đúng thẩm quyền.

## BA-07. Release, bàn giao và cải tiến

Mục tiêu: bảo đảm tài liệu, quyết định và kiến thức nghiệp vụ được bàn giao đúng phiên bản.

- Đầu vào: UAT Result, Release Notes, Known Issues, tài liệu và quyết định nghiệm thu.

- Bước 1: đối chiếu phạm vi phát hành với Story, AC, Test Result và UAT.

- Bước 2: cập nhật Release Notes, hướng dẫn sử dụng, Business Rules và FAQ.

- Bước 3: ghi nhận vấn đề còn mở, rủi ro, owner và đầu mối hỗ trợ.

- Bước 4: AI hỗ trợ tổng kết bài học/FAQ; BA review trước khi xuất bản.

- Bước 5: lưu tài liệu đã duyệt vào Knowledge Base và tham gia Retrospective.

- Đầu ra: Handover Pack, Release Notes, Known Issues, RTM và Action Items.

- Quality Gate: đúng phiên bản, có người nhận bàn giao, tài liệu AI đã review, vấn đề mở có owner.

## 6. Bộ template và biểu mẫu

### BA-T01 Requirement Intake

- Requirement ID

- Request Title

- Requester

- Business Owner

- Business Problem

- Business Objective

- Scope / Out of Scope

- Priority (PO xác định)

- Source Documents + version

- Dependencies

- Target Date

- Open Questions

- AI Review Status

- BA/PO Decision

### BA-T02 Business Analysis Document

- Document ID / version / owner

- Background & Business Problem

- Objective & Success Metrics

- Scope / Out of Scope

- Stakeholder & Actor

- AS-IS / TO-BE

- Functional Requirements

- Business Rules

- NFR

- Data / Integration / Permission

- Alternative & Error Flows

- Assumptions / Risks / Dependencies

- Open Questions / Decision Log

- Review & Approval

### BA-T03 User Story & AC

- Story ID / Epic ID

- Title

- As a / I want / So that

- Business Value

- Requirement IDs

- Business Rule IDs

- Acceptance Criteria ID

- Given / When / Then

- Validation / Error Cases

- Data / Permission / Integration

- NFR

- Open Questions

- Review Status

### BA-T04 RTM

- Requirement ID

- Story ID

- AC ID

- Test Case ID

- Test Result

- UAT Result

- Evidence Link

- Version

- Coverage Status

- Notes

### BA-T05 Decision Log & Change Request

- Decision/CR ID

- Date

- Requester

- Current Requirement

- Proposed Change

- Business Reason

- Impact Analysis

- Options

- Decision

- Approver

- Effective Version

- Communication

- Status

### BA-T06 UAT Report

- Project / Release / Build

- Environment

- UAT Date

- Business Owner / Participants

- Scope & Acceptance Criteria

- Total Scenarios

- Passed

- Failed

- Blocked

- Not Run

- Defect ID / Severity / Evidence

- Open Risks

- Decision

- Approver / Date

### BA-T07 Handover Checklist

- Release scope confirmed

- Requirements and Business Rules versioned

- Release Notes and Known Issues updated

- Test/UAT evidence archived

- Open CRs handed over

- Open issues have owners

- AI drafts reviewed before publishing

- Support owner identified

## 7. AI Agent operating model

Mô hình đề xuất: Orchestrator điều phối Requirement Agent, Analysis Agent, Specification Agent, QA Review Agent, Test Design Agent và Traceability Agent. Các Agent dùng chung quy tắc nguồn, phân quyền, schema đầu ra và audit trail.

- Requirement Agent: trích xuất mục tiêu, phạm vi, câu hỏi thiếu, trùng lặp và mâu thuẫn.

- Analysis Agent: tạo bản nháp AS-IS/TO-BE, Business Rules, requirements, risks và dependencies có nguồn.

- Specification Agent: tạo Story/AC từ yêu cầu đã review; không tự thêm quy tắc.

- QA Review Agent: kiểm tra completeness, clarity, consistency, testability và traceability.

- Test Design Agent: gợi ý Test Scenario/Test Case; không tự đánh dấu Pass nếu chưa chạy test.

- Traceability Agent: phát hiện liên kết thiếu và hỗ trợ Impact Analysis.

## 8. Kiểm soát AI và bảo mật

- Grounding: kết luận quan trọng phải có nguồn hoặc ghi rõ chưa xác minh.

- Human approval: không tự phê duyệt nghiệp vụ, nghiệm thu hoặc thay đổi phạm vi.

- Versioning: lưu phiên bản prompt, model, tài liệu đầu vào, đầu ra và quyết định review.

- Access control: Agent chỉ được truy cập tài nguyên đã cấp quyền.

- Audit trail: ghi nhận người yêu cầu, Agent, thời điểm, reviewer và quyết định.

- Idempotency: tránh tạo Story/Comment trùng khi chạy lại workflow.

- Error handling: nếu nguồn lỗi, schema sai hoặc thiếu dữ liệu, dừng bước và chuyển xử lý.

- Data protection: không gửi dữ liệu nhạy cảm đến dịch vụ chưa được tổ chức phê duyệt.

## 9. KPI khởi điểm

| KPI | Cách đo | Mục tiêu ban đầu |
| --- | --- | --- |
| Requirement Completeness | Yêu cầu đạt checklist / yêu cầu được review | Mục tiêu thử nghiệm ≥95% |
| AC Testability | AC có thể kiểm thử / AC được review | Mục tiêu thử nghiệm ≥95% |
| Traceability Coverage | Yêu cầu cần test có liên kết test phù hợp / tổng yêu cầu cần test | Mục tiêu thử nghiệm ≥95% |
| Rework Rate | Yêu cầu phải sửa lớn do phân tích thiếu/sai / yêu cầu triển khai | Đo baseline, sau đó giảm |
| Clarification Response Time | Thời gian từ câu hỏi đến câu trả lời được xác nhận | Theo SLA dự án |
| AI Acceptance Rate | Đầu ra AI được chấp nhận với ít hoặc không cần sửa lớn / đầu ra được review | Đo baseline |
| AI Unsupported Claim Rate | Kết luận quan trọng không được nguồn hỗ trợ / kết luận được kiểm tra | Hướng tới 0 |

Các mục tiêu là ngưỡng khởi điểm đề xuất, không phải chuẩn bắt buộc của Scrum. Đo baseline trong 2–4 Sprint trước khi điều chỉnh.

## 10. Kế hoạch triển khai tham khảo

- Tuần 1–2: chốt SOP, RACI, Quality Gate, template và chọn dự án thí điểm.

- Tuần 3–4: triển khai Requirement Intake, Specification và QA Review Agent; kiểm thử bằng bộ tài liệu chuẩn.

- Tuần 5–6: tích hợp Jira/Confluence nếu được phê duyệt; thiết lập RTM, approval, versioning và audit trail.

- Tuần 7–8: đo KPI, đánh giá lỗi AI, cải tiến prompt/workflow và quyết định mở rộng.

## 11. Checklist tổng thể

☐ Có Requirement ID và nguồn tài liệu

☐ Xác định Business Owner và mục tiêu

☐ Ghi nhận câu hỏi còn thiếu

☐ Có phạm vi và Stakeholder

☐ Đã phân tích luồng chính và ngoại lệ

☐ Business Rules có nguồn xác nhận

☐ Đã xem xét dependency và rủi ro

☐ User Story/đặc tả phù hợp đã được tạo

☐ Acceptance Criteria kiểm chứng được

☐ Đã review tính nhất quán

☐ Có liên kết Requirement ID

☐ Thay đổi được ghi nhận và truy vết

☐ Test Case liên kết với AC

☐ Kết quả kiểm thử có bằng chứng

☐ Có UAT Result và quyết định đúng thẩm quyền

☐ Tài liệu đúng phiên bản

☐ Vấn đề còn mở có owner

☐ AI output đã được review trước khi xuất bản

## 12. Quy ước trạng thái gợi ý

Intake: New → Clarification Required → Accepted for Analysis / Rejected. Story: Draft → In Review → Ready for Refinement → Selected for Sprint → In Progress → Done (theo quy ước của Team). Change Request: Proposed → Under Review → Approved / Rejected → Implemented. Các trạng thái cụ thể cần ánh xạ với workflow hiện có của tổ chức.

## 13. Tài liệu tham chiếu

Bộ tài liệu này là khung thực hành nội bộ đề xuất. Khi triển khai, cần đối chiếu Scrum Guide hiện hành, chính sách quản lý thay đổi, bảo mật dữ liệu, quy định phê duyệt và hệ thống quản lý công việc của tổ chức.
