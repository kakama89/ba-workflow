---
name: ba-07-release-handover
description: "BA-07 release, handover and improvement: reconcile release scope against stories, AC, test results and UAT, update release notes, user guides, business rules and FAQ, record open issues with owners, have AI draft lessons learned for BA review, then archive approved documents to the knowledge base. Use when a release has been accepted and documentation, decisions and business knowledge must be handed over at the correct version. Tiếng Việt: BA-07 Release, bàn giao và cải tiến — đối chiếu phạm vi phát hành với Story, AC, Test Result và UAT, cập nhật Release Notes, hướng dẫn sử dụng, Business Rules và FAQ, ghi nhận vấn đề còn mở kèm owner, để AI dự thảo bài học kinh nghiệm cho BA review, sau đó lưu tài liệu đã duyệt vào Knowledge Base. Dùng khi bản phát hành đã được nghiệm thu và cần bàn giao tài liệu, quyết định và kiến thức nghiệp vụ đúng phiên bản."
metadata:
  version: "1.0"
  sop_ref: "assets/_archive/sop-v1.0.md — BA-07 (Quality Gate bàn giao), §9 KPI, §11 Checklist"
  pack: "Bo_Quy_Trinh_BA_Agile_AI"
  template: "assets/_archive/workbook-v1.0.md — sheet Handover / BA-T07"
compatibility: "Cần UAT Result đã nghiệm thu, Release Notes, Known Issues và quyền ghi vào Knowledge Base của dự án. Không xuất bản tài liệu do AI dự thảo khi BA chưa review."
---

# BA-07 — Release, bàn giao và cải tiến

## Mục tiêu
Bảo đảm tài liệu, quyết định và kiến thức nghiệp vụ được bàn giao đúng phiên bản.

## Khi nào dùng
- Bản phát hành đã có quyết định nghiệm thu từ BA-06.
- Cần đối chiếu phạm vi phát hành với tài liệu yêu cầu và kết quả kiểm thử.
- Cần đóng gói Handover Pack và chuyển giao cho bộ phận vận hành/hỗ trợ.
- Kết thúc Sprint/Release và cần tổng kết bài học.

## Đầu vào
| Đầu vào | Bắt buộc | Ghi chú |
| --- | --- | --- |
| UAT Result | Có | Đã đạt G4, có `Approver` |
| Release Notes | Có | Bản dự thảo hoặc bản đã có |
| Known Issues | Có | Kèm mức tác động và cách xử lý tạm |
| Tài liệu yêu cầu | Có | URD/BRD, Business Rules, Story/AC đúng phiên bản |
| Quyết định nghiệm thu | Có | Nếu chưa có, dừng — không bàn giao |
| RTM | Có | `skills/ba-03-specification/assets/rtm.md` |

## Rào cản bắt buộc (không được vượt qua)

1. **Grounding** — mọi kết luận quan trọng phải kèm nguồn; nếu chưa xác minh thì ghi rõ "chưa xác minh".
2. **Fact / Assumption / Inference / Unknown** — phân loại tường minh, không trộn lẫn.
3. **Không tự tạo Business Rules**, không tự đặt Priority, Story Point, SLA hay giới hạn nghiệp vụ.
4. **Không tự phê duyệt** — DoR, nghiệm thu, thay đổi phạm vi đều thuộc thẩm quyền con người.
5. **Mọi đầu ra là DRAFT** cho đến khi người có thẩm quyền review.
6. **Thiếu đầu vào thì hỏi, không đoán.**
7. **Idempotency** — kiểm tra bản ghi đã tồn tại trước khi tạo mới; không sinh Story/Comment/Record trùng khi chạy lại.
8. **Error handling** — nguồn lỗi, schema sai hoặc thiếu dữ liệu: dừng bước và báo, không tự chế dữ liệu thay thế.
9. **Data protection** — không gửi bí mật hoặc dữ liệu nhạy cảm tới dịch vụ chưa được tổ chức phê duyệt.
10. **Audit trail** — ghi lại prompt version, model/version, tài liệu đầu vào, đầu ra, người review và quyết định.

Riêng ở BA-07: **không xuất bản tài liệu AI dự thảo khi BA chưa review**, không tuyên bố phạm vi phát hành khớp tài liệu khi chưa đối chiếu từng dòng.

## Quy trình

### Bước 1 — Đối chiếu phạm vi phát hành
- So sánh danh sách Story/AC phát hành với `Test Result`, `UAT Result` trong RTM.
- Gọi `ba-agent-traceability` để phát hiện `Version Mismatch`, `Missing Link`, `Orphan`.
- Story phát hành mà không có bằng chứng kiểm thử: ghi nhận, báo PO — không tự cho qua.

### Bước 2 — Cập nhật tài liệu hướng ra ngoài
- Release Notes, hướng dẫn sử dụng, Business Rules Catalog, FAQ.
- Chỉ ghi hành vi đã được xác nhận; phần chưa rõ chuyển thành Known Issues hoặc câu hỏi mở.

### Bước 3 — Ghi nhận vấn đề còn mở
- Mỗi vấn đề: mô tả, mức tác động, cách xử lý tạm, **owner**, hạn.
- Xác định đầu mối hỗ trợ sau bàn giao.
- Vấn đề không có owner là lỗi gate.

### Bước 4 — AI tổng kết bài học và FAQ
- AI dự thảo; BA review từng mục trước khi xuất bản.
- Loại bỏ kết luận không có bằng chứng từ Sprint/Release vừa rồi.

### Bước 5 — Lưu Knowledge Base và Retrospective
- Lưu tài liệu **đã duyệt**, đúng phiên bản, kèm người nhận bàn giao.
- Tham gia Retrospective, ghi Action Items có owner.

## Đầu ra
| Đầu ra | Vị trí |
| --- | --- |
| Handover Pack | `assets/handover-checklist.md` — khớp sheet `Handover` |
| Release Notes | Tài liệu phát hành của dự án |
| Known Issues | Kèm trong Handover Pack |
| RTM | Bản chốt, đúng phiên bản phát hành |
| Action Items | Từ Retrospective, có owner và hạn |

## Quality Gate bàn giao
Chi tiết tại `references/release-kpi-checklist.md`. Tóm tắt:
- [ ] Đúng phiên bản
- [ ] Có người nhận bàn giao
- [ ] Tài liệu AI đã review
- [ ] Vấn đề mở có owner

## RACI
| BA | PO | Dev/Tech | QA | Business |
| --- | --- | --- | --- | --- |
| A/R | C | C | C | I |

BA là người chịu trách nhiệm cuối cùng cho hoạt động bàn giao tài liệu nghiệp vụ — đây là hoạt động duy nhất trong RACI mà BA giữ vai A/R.

## Assets & references
- `assets/handover-checklist.md` — checklist bàn giao HO-001…HO-008 và biên bản Handover Pack.
- `references/release-kpi-checklist.md` — gate bàn giao, 7 KPI khởi điểm (SOP §9) và checklist tổng thể (SOP §11).
- RTM dùng chung: `skills/ba-03-specification/assets/rtm.md`.
- Skill liên quan: `ba-agent-traceability` (Bước 1), `ba-agent-qa-review` (rà soát tài liệu trước khi xuất bản).
- Quy trình trước: `ba-06-test-uat`. Đây là quy trình cuối; quay lại `ba-01-requirement-intake` cho yêu cầu mới.
