---
name: ba-06-test-uat
description: "BA-06 testing, UAT and business acceptance: review requirement-AC-test case links, support test execution by explaining business rules, classify discrepancies as defect, requirement gap or change request, prepare and run UAT scenarios, update the RTM with evidence, and support the acceptance decision. Use when a build is ready for testing, when UAT must be organised with business users, or when acceptance evidence needs to be consolidated. Tiếng Việt: BA-06 Kiểm thử, UAT và nghiệm thu nghiệp vụ — rà soát liên kết yêu cầu–AC–Test Case, hỗ trợ thực thi kiểm thử bằng cách giải thích quy tắc nghiệp vụ, phân loại sai khác thành defect, requirement gap hoặc change request, chuẩn bị và chạy kịch bản UAT, cập nhật RTM kèm bằng chứng, hỗ trợ quyết định nghiệm thu. Dùng khi có build sẵn sàng để test, khi cần tổ chức UAT với Business User, hoặc khi cần tổng hợp bằng chứng nghiệm thu."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-06, Quality Gate G4"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet UAT Report / BA-T06, sheet RTM / BA-T04"
compatibility: "Cần build test, Test Plan/Case, dữ liệu và môi trường kiểm thử đã được cấp phép, cùng Business User tham gia UAT. Không tự đánh dấu kết quả khi chưa có bằng chứng thực thi."
---

# BA-06 — Kiểm thử, UAT và nghiệm thu nghiệp vụ

## Mục tiêu
Xác minh sản phẩm đáp ứng yêu cầu bằng bằng chứng và hỗ trợ quyết định nghiệm thu.

## Khi nào dùng
- Có build sẵn sàng cho kiểm thử và cần rà soát liên kết yêu cầu–AC–Test Case.
- Cần tổ chức UAT với Business User.
- Cần tổng hợp Pass/Fail/Blocked, defect và rủi ro để ra quyết định nghiệm thu.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| Story / AC | Có | Bản đã xác nhận, đúng phiên bản |
| Business Rules | Có | Để giải thích kết quả mong đợi |
| Build test | Có | Ghi rõ phiên bản build |
| Test Plan / Test Case | Có | Do QA sở hữu; AC còn thiếu Test Case được xử lý ở Bước 1 |
| Tiêu chí nghiệm thu | Có | Nếu chưa có, dừng và hỏi — không tự đặt |
| Môi trường và dữ liệu kiểm thử | Có | Chỉ dùng dữ liệu được phép |

## Rào cản bắt buộc (không được vượt qua)

Áp dụng đầy đủ 10 điều tại mục «Rào cản bắt buộc» trong `POWER.md` (Grounding · Fact/Assumption/Inference/Unknown · không tự tạo Business Rules · không tự phê duyệt · DRAFT · không đoán · Idempotency · Error handling · Data protection · Audit trail).

Riêng ở BA-06: **không bao giờ ghi `Pass` khi chưa có kết quả thực thi thật**, không quyết định Accept/Reject, không tự đặt Severity cho defect.

## Quy trình

### Bước 1 — BA và QA review liên kết yêu cầu–AC–Test Case
- Gọi `ba-agent-traceability` để đối chiếu chuỗi `Requirement → Story → AC → Test Case`.
- Xử lý `Missing Link` và `Orphan` trước khi chạy test.
- AC chưa có Test Case: ghi nhận, BA không viết thay QA. QA có thể gọi `ba-agent-test-design` tạo bản nháp và phải review trước khi dùng.

### Bước 2 — QA thực hiện kiểm thử, BA hỗ trợ
- QA thực hiện; BA giải thích quy tắc nghiệp vụ và kết quả mong đợi, kèm nguồn.
- BA không ghi kết quả thay QA.

### Bước 3 — Phân loại sai khác
Mỗi sai khác xếp vào đúng một loại:
| Loại | Nghĩa | Chuyển tới |
| --- | --- | --- |
| Defect | Code không đúng AC đã duyệt | QA/Dev xử lý |
| Requirement gap | AC/Business Rule chưa mô tả hành vi này | `ba-05-change-management`, rồi quay lại theo Bước 6 của BA-05 |
| Change request | Nghiệp vụ muốn hành vi khác | `ba-05-change-management` |

Không tự quyết định loại khi chưa rõ: ghi `[Unknown]` và hỏi Business Owner.

Vòng sửa lỗi: Dev sửa defect, QA retest trên build mới và ghi bằng chứng, rồi mới đóng defect. Nếu build đổi sau khi đã chạy UAT, người có thẩm quyền quyết định phạm vi chạy lại và ghi vào UAT Report.

### Bước 4 — Chuẩn bị UAT
- BA dựng UAT Scenario từ AC đã duyệt; mỗi Scenario một `Scenario ID` (dạng `UAT-001`) và trỏ về `Story ID` + `AC ID`.
- Gọi `ba-agent-qa-review` để rà soát tài liệu trước UAT (bắt buộc).
- Chuẩn bị dữ liệu và hướng dẫn Business User.
- Chỉ dùng dữ liệu được phép; không đưa dữ liệu nhạy cảm vào môi trường chưa phê duyệt.

### Bước 5 — Business User thực hiện UAT
- BA ghi nhận `Actual Result`, bằng chứng và kết quả theo diễn biến thật.
- Không suy diễn kết quả khi Business User chưa xác nhận.

### Bước 6 — Tổng hợp và cập nhật RTM
- Tổng hợp Pass/Fail/Blocked, defect và rủi ro còn mở.
- Cập nhật RTM tại `ba-records/<project>/rtm.md`: QA ghi `Test Result`; BA ghi `UAT Result`, `Evidence Link` và `Coverage Status`.
- Gọi `ba-agent-traceability` để đối chiếu lại RTM; Agent chỉ đề xuất, không tự cập nhật.
- Gọi `ba-agent-test-design` nếu phát hiện thiếu scenario cho luồng biên có căn cứ.

### Bước 7 — Quyết định nghiệm thu
Người có thẩm quyền quyết định `Accept` / `Reject` / `Conditional Acceptance` nếu được phép.
BA trình bày bằng chứng, không khuyến nghị thay cho người quyết định.

| Quyết định | Việc tiếp theo |
| --- | --- |
| `Accept` | Kiểm tra G4, rồi chuyển BA-07 |
| `Conditional Acceptance` | Ghi từng điều kiện kèm owner và hạn vào `Conditions`; kiểm tra G4, rồi chuyển BA-07 và bàn giao các điều kiện đó |
| `Reject` | Không chuyển BA-07. Phân loại lý do theo Bước 3, xử lý, rồi chạy lại từ Bước 2 hoặc Bước 5 trên build mới với một đợt UAT mới |
| `Pending` | Dừng; chưa đóng G4 |

## Đầu ra
Đường dẫn `assets/` trong bảng là template chỉ đọc; bản ghi thật lưu tại `ba-records/<project>/` (xem mục "Template và bản ghi dự án" trong `POWER.md`).

| Đầu ra | Vị trí |
| --- | --- |
| Test Review | Kết quả Bước 1 |
| RTM | `ba-records/<project>/rtm.md` (template: `skills/ba-03-specification/assets/rtm.md`) |
| UAT Report | `assets/uat-report.md` — khớp sheet `UAT Report` (17 cột) |
| Defect Log | Theo hệ thống của QA; ghi `Defect ID` vào UAT Report |
| Quyết định nghiệm thu | `Decision`, `Approver`, `Approval Date`, `Conditions` ⚠ |

## Quality Gate G4
Chi tiết tại `references/quality-gate-g4.md`. Tóm tắt:
- [ ] Kết quả có bằng chứng
- [ ] Defect nghiêm trọng đã được xử lý hoặc được chấp nhận rủi ro đúng thẩm quyền
- [ ] ⚠ `Decision` là `Accept` hoặc `Conditional Acceptance`, có `Approver` và ngày
- [ ] ⚠ RTM coverage ≥ ngưỡng dự án (mặc định 100 %)
- [ ] ⚠ Pass Rate ≥ ngưỡng dự án (mặc định 100 %)
- [ ] ⚠ Defect Critical/Major còn mở = 0

Không đạt G4 thì không chuyển sang BA-07.

## RACI
| Hoạt động | BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- | --- |
| Thiết kế Test Case | C | I | C | A/R | C |
| UAT và xác nhận nghiệp vụ | C | C | I | R/C | A/R |

## Assets & references
- `assets/uat-report.md` — template UAT Report.
- `references/quality-gate-g4.md` — checklist G4, quy tắc phân loại sai khác, quy tắc dừng bước.
- RTM dùng chung: `skills/ba-03-specification/assets/rtm.md`.
- Skill liên quan: `ba-agent-traceability` (Bước 1, Bước 6), `ba-agent-test-design` (Bước 1, Bước 6), `ba-agent-qa-review` (Bước 4, bắt buộc).
- Quy trình trước: `ba-04-refinement`, qua Sprint. Phát sinh thay đổi: `ba-05-change-management`. Kế tiếp: `ba-07-release-handover`.
