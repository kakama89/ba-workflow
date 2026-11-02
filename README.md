# Kiro Power — Quy trình BA Agile/Scrum có AI Agent

> File này là **mục lục dành cho người** của power, không phải một skill. Kiro nạp các skill từ thư mục `skills/` (mỗi thư mục con có `SKILL.md`).

Phiên bản: 1.0 · Nguồn: `assets/_archive/sop-v1.0.md`, `assets/_archive/workbook-v1.0.md`, `assets/_archive/prompt-pack-v1.0.md`

## Trạng thái tài liệu nguồn — đọc trước khi dùng

Bốn tài liệu gốc (`01_SOP_BA_Agile_AI.docx`, `02_Bo_Template_BA.xlsx`, `03_Prompt_Pack_BA_AI.md`, `README.md`) **đã bị xoá khỏi thư mục dự án vào 2026-10-30** theo quyết định của chủ tài liệu, và đó là **bản duy nhất** — thư mục này không phải git repo, không có bản sao ở Confluence/SharePoint/Jira.

Toàn bộ nội dung chữ của chúng được lưu tại **`assets/_archive/`**, trích xuất bằng script trực tiếp từ file nhị phân chứ không gõ lại tay. Đã kiểm tra trước khi xoá: cả hai file nhị phân **không chứa** ảnh, media, drawing, textbox, OLE object, comment, footnote, endnote, header/footer, công thức, data validation, conditional formatting, chart hay defined name — nên không mất nội dung nào. Thứ không giữ lại được là định dạng trực quan (font, màu, độ rộng cột, freeze pane) và khả năng mở bằng Word/Excel.

Hệ quả cần biết:
- Bộ skill **tự chủ về nội dung**: 7 quy trình, 7 gate, 6 agent, tên cột của cả 9 sheet, KPI §9, checklist §11, trạng thái §12, RACI §5 và bảng vai trò §4 đều đã nằm trong power này (thư mục `skills/`).
- **Không còn bản gốc có định dạng để đối chiếu.** Nếu cần phục hồi `.docx`/`.xlsx`, nguồn duy nhất là Recycle Bin của máy này.
- Nếu sau này tổ chức công bố SOP trên Confluence/SharePoint, cập nhật các đường dẫn `_archive/` trong bộ skill trỏ về nguồn chính thức đó.

Chi tiết: `assets/_archive/README.md`.

## Vị trí và cách gọi
- **Dạng phân phối**: đây là một **Kiro Power** tự chứa — manifest ở `plugin.json`, hướng dẫn power ở `POWER.md`, 13 skill ở `skills/`, tài liệu nguồn lưu trữ ở `assets/_archive/`, icon ở `assets/icon.png`.
- **Cài đặt**: thêm power vào Kiro qua registry `user-added` — nguồn `local` trỏ tới thư mục này, hoặc nguồn `repo` nếu đẩy lên git remote. Sau khi cài, Kiro sao power vào `~/.kiro/powers/installed/<tên>/`.
- **Gọi tự động**: Kiro khớp yêu cầu với trường `description` của từng skill.
- **Gọi thủ công**: gõ `/` + tên skill, ví dụ `/ba-03-specification`. Chữ sau tên skill được truyền vào làm ngữ cảnh.
- **Custom agent**: skill **không** được nạp mặc định; phải khai báo trong trường `resources` bằng URI `skill://`.

## 7 skill quy trình

| Skill | SOP | Gate | Template (sheet workbook) |
| --- | --- | --- | --- |
| `ba-01-requirement-intake` | BA-01 | G1 | Intake / BA-T01 |
| `ba-02-business-analysis` | BA-02 | G2 | Analysis / BA-T02 |
| `ba-03-specification` | BA-03 | G3 | User Story AC / BA-T03 + RTM / BA-T04 |
| `ba-04-refinement` | BA-04 | DoR tham khảo | — |
| `ba-05-change-management` | BA-05 | Gate thay đổi | Change Log / BA-T05 |
| `ba-06-test-uat` | BA-06 | G4 | UAT Report / BA-T06 + RTM |
| `ba-07-release-handover` | BA-07 | Gate bàn giao | Handover / BA-T07 |

## 6 skill AI Agent

| Skill | Agent (SOP §7) | Prompt gốc | Được gọi từ |
| --- | --- | --- | --- |
| `ba-agent-requirement` | Requirement Agent | Prompt Pack §1 | BA-01 Bước 4 |
| `ba-agent-analysis` | Analysis Agent | Prompt Pack §2 | BA-02 Bước 6 |
| `ba-agent-specification` | Specification Agent | Prompt Pack §3 | BA-03 Bước 5 |
| `ba-agent-qa-review` | QA Review Agent | Prompt Pack §4 | BA-03 Bước 5–6, BA-04 Bước 5 |
| `ba-agent-test-design` | Test Design Agent | Prompt Pack §5 | BA-06 Bước 1, Bước 4 |
| `ba-agent-traceability` | Traceability Agent | Prompt Pack §6 | BA-05 Bước 3/5, BA-06 Bước 1/6 |

## Tài nguyên dùng chung

| File | Được tham chiếu bởi |
| --- | --- |
| `skills/ba-03-specification/assets/rtm.md` | `ba-03`, `ba-06`, `ba-07`, `ba-agent-test-design`, `ba-agent-traceability` |
| `skills/ba-05-change-management/assets/decision-log-cr.md` | `ba-04` (PO chấp nhận rủi ro), `ba-06` (requirement gap / CR) |

RTM đặt ở `ba-03` vì đó là nơi dòng truy vết đầu tiên được tạo (SOP BA-03 liệt kê RTM trong đầu ra). Các skill khác chỉ tham chiếu theo đường dẫn, không tạo bản sao.

## Luồng gọi điển hình

```
Yêu cầu mới
  → /ba-01-requirement-intake      (gọi ba-agent-requirement ở Bước 4)   → G1
  → /ba-02-business-analysis       (gọi ba-agent-analysis ở Bước 6)      → G2
  → /ba-03-specification           (gọi ba-agent-specification, ba-agent-qa-review) → G3 + tạo RTM
  → /ba-04-refinement              (gọi ba-agent-qa-review)              → DoR
  → [Sprint] /ba-05-change-management (gọi ba-agent-traceability)        → Gate thay đổi
  → /ba-06-test-uat                (gọi ba-agent-traceability, ba-agent-test-design) → G4
  → /ba-07-release-handover        (gọi ba-agent-traceability)           → Gate bàn giao
```

Nguyên tắc: **skill quy trình điều phối con người, skill agent chỉ tạo bản nháp.** Không skill nào tự đóng gate.

## Quy ước chung của cả 13 skill
- `description` song ngữ: tiếng Anh trước (có mệnh đề `Use when …`) rồi tới `Tiếng Việt:` — để Kiro khớp được cả hai ngôn ngữ.
- Thân skill viết tiếng Việt, giữ nguyên thuật ngữ tiếng Anh như SOP.
- Khối **"Rào cản bắt buộc"** 10 điều giống hệt nhau ở cả 13 skill (Grounding · Fact/Assumption/Inference/Unknown · không tự tạo Business Rules · không tự phê duyệt · DRAFT · không đoán · Idempotency · Error handling · Data protection · Audit trail).
- Đầu ra agent theo 6 phần: Summary · Facts with sources · Findings/Open Questions · Suggested actions · Confidence limitations · `Status = DRAFT`.
- Cột biểu mẫu khớp đúng tên cột trong `assets/_archive/workbook-v1.0.md`.

## Khác biệt giữa SOP §6 và workbook — đã xử lý trong assets

| Template | Mục SOP §6 có nhưng sheet thiếu | Xử lý |
| --- | --- | --- |
| BA-T02 / sheet `Analysis` | `owner`, `Success Metrics`, `Out of Scope`, `Decision Log`, `Review & Approval` | Thêm vào `skills/ba-02-business-analysis/assets/business-analysis-doc.md`, đánh dấu ⚠ |
| BA-T06 / sheet `UAT Report` | Cột gộp `Scope & Acceptance Criteria`, các ô tổng `Total/Passed/Failed/Blocked/Not Run`, `Open Risks`, `Approver / Date` | Tách thành "Phần 3 — Tổng hợp và quyết định" trong `skills/ba-06-test-uat/assets/uat-report.md` |
| BA-T07 / sheet `Handover` | `Support owner identified` | Thêm dòng `HO-008` ⚠ trong `skills/ba-07-release-handover/assets/handover-checklist.md` |

BA-T01, BA-T03, BA-T04, BA-T05: sheet workbook đầy đủ hơn hoặc bằng SOP, không cần bổ sung.

Workbook gốc đã bị xoá; cấu trúc của nó được lưu tại `assets/_archive/workbook-v1.0.md`. Nếu tổ chức ban hành workbook phiên bản mới, đối chiếu lại với bản archive đó rồi cập nhật các file `assets/` tương ứng.

## Việc cần làm trước khi áp dụng (theo README của bộ tài liệu, bản lưu tại `assets/_archive/pack-readme-v1.0.md`)
1. Review và điều chỉnh quy trình theo chính sách, công cụ và phân quyền của tổ chức.
2. Thay ví dụ minh hoạ bằng dữ liệu dự án thực tế.
3. Chốt nguồn tài liệu chính thức và quy tắc versioning.
4. Thử nghiệm 2–4 Sprint; đo baseline trước khi đặt KPI chính thức.
5. Chỉ tích hợp AI Agent với Jira/Confluence sau khi được cấp quyền và phê duyệt bảo mật.
6. Không dùng đầu ra AI chưa review làm yêu cầu chính thức.

Kế hoạch triển khai tham khảo (SOP §10): Tuần 1–2 chốt SOP/RACI/Gate/template → Tuần 3–4 dựng Requirement Intake, Specification, QA Review Agent → Tuần 5–6 tích hợp Jira/Confluence nếu được duyệt, thiết lập RTM/approval/versioning/audit trail → Tuần 7–8 đo KPI, đánh giá lỗi AI, cải tiến prompt và quyết định mở rộng.
