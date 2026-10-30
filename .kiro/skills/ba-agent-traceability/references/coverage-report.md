# Coverage report — Traceability Agent

Tham chiếu: `.kiro/skills/_archive/prompt-pack-v1.0.md` §6 và "Định dạng chung đề xuất"; `.kiro/skills/_archive/workbook-v1.0.md` sheet `RTM` (10 cột) và `Change Log` (13 cột); `.kiro/skills/_archive/sop-v1.0.md` §7, §8, §12.

## 1. Định dạng đầu ra chuẩn

Mọi phản hồi trả về đủ 6 phần, theo đúng thứ tự:

```
1. Summary
2. Facts with sources
3. Findings / Open Questions
4. Suggested actions
5. Confidence limitations
6. Status = DRAFT
```

| Phần | Nội dung |
|---|---|
| Summary | Độ bao phủ tổng thể, số liên kết thiếu, số orphan, số tác động nghi ngờ |
| Facts with sources | Coverage Summary và các liên kết đã xác nhận, kèm Source Evidence |
| Findings / Open Questions | Missing Links, orphan records, Suspected Impact, tài liệu lệch phiên bản |
| Suggested actions | Suggested Owner/Action cho từng mục, theo thứ tự nên xử lý |
| Confidence limitations | Liên kết nào chỉ ở mức `Inferred`, nguồn nào không đọc được |
| Status | Luôn là `DRAFT` |

## 2. Chuỗi đối chiếu

`Requirement ID → Story ID → AC ID → Test Case ID → Test Result / UAT Result`

Đối chiếu **hai chiều**:

- Xuôi: mỗi `Requirement ID` có Story, mỗi Story có AC, mỗi AC có Test Case hay không.
- Ngược: mỗi Test Case, AC, Story có truy ngược được về `Requirement ID` hay không.

Bản ghi chỉ có liên kết một chiều được tính là orphan record, không được tính là đã bao phủ.

## 3. Năm khối đầu ra chi tiết

### Coverage Summary

Bảng đếm theo từng tầng liên kết: tổng số bản ghi, số đã liên kết, số thiếu liên kết, số orphan. Nêu rõ đơn vị đếm (Requirement, Story, AC, Test Case) và phiên bản RTM dùng để đếm.

### Missing Links

Mỗi dòng nêu: bản ghi bị thiếu liên kết, tầng liên kết bị đứt, hướng đứt (xuôi/ngược), và nguồn cho thấy đáng lẽ phải có liên kết.

### Suspected Impact

Từ Change Log hoặc phiên bản tài liệu mới, liệt kê Story/AC/Test Case/dòng RTM có khả năng bị ảnh hưởng. Mọi dòng gắn nhãn `Suspected` và nêu căn cứ nghi ngờ. Không khẳng định tác động khi chưa có bằng chứng.

### Source Evidence

Với mỗi kết luận: tài liệu, phiên bản và vị trí cụ thể đã dùng. Kết luận không có Source Evidence thì phải chuyển sang `Confidence limitations` hoặc thành câu hỏi mở.

### Suggested Owner/Action

Mỗi Missing Link và Suspected Impact kèm một hành động đề xuất và vai trò nên xử lý (`BA | PO | QA | Business Owner`). Đây là đề xuất, không phải quyết định.

## 4. Confirmed và Inferred — quy tắc bắt buộc

**Một liên kết suy luận KHÔNG phải là một liên kết đã xác nhận.**

| Nhãn | Khi nào dùng | Có được tính vào coverage không |
|---|---|---|
| Confirmed | Liên kết ghi rõ trong RTM hoặc trong tài liệu nguồn, trích dẫn được | Có |
| Inferred | Suy ra từ tên gọi, nội dung tương tự hoặc vị trí gần nhau, không có ghi nhận tường minh | Không |

Liên kết `Inferred` phải được liệt kê riêng, nêu căn cứ suy luận và nêu rõ cần ai xác nhận. Không gộp `Inferred` vào số liệu coverage, không trình bày `Inferred` như `Confirmed`.

## 5. Giá trị enum

- **Nhãn liên kết:** `Confirmed | Inferred`
- **Nhãn tác động:** `Suspected` (Agent không dùng nhãn tác động đã xác nhận)
- **Nhãn bằng chứng:** `Fact | Assumption | Inference | Unknown`
- **Test Result / UAT Result (sheet `RTM`):** mặc định `Not Run` — Agent không ghi giá trị khác
- **Coverage Status (sheet `RTM`):** mặc định `Pending` — Agent không ghi `Covered`
- **Change Request (SOP §12):** `Proposed → Under Review → Approved / Rejected → Implemented` — do con người quyết định
- **Status đầu ra của Agent:** `DRAFT` (cố định)

## 6. Dừng bước khi nào

Dừng và báo lại BA, không tự chế dữ liệu thay thế, khi:

1. Không truy cập được RTM hoặc RTM không có phiên bản.
2. Thiếu một trong các nguồn của chuỗi đối chiếu (danh sách Requirement, Story/AC, Test Case).
3. Hai nguồn cho hai phiên bản RTM khác nhau và không xác định được bản chính thức.
4. Phát hiện RTM thay đổi trong lúc đang đối chiếu.
5. Test Result/UAT Result cần đối chiếu nằm ngoài phạm vi được cấp quyền.
6. Tài liệu chứa dữ liệu nhạy cảm chưa được phép xử lý bằng công cụ hiện tại.

Khi dừng: nêu rõ phần chuỗi đã đối chiếu được, phần bị chặn, lý do và nguồn cần cung cấp. Không đưa ra con số coverage cho phần chưa đối chiếu.

## 7. Idempotency và audit trail

- Báo cáo coverage gắn với một phiên bản RTM và một thời điểm; chạy lại trên cùng phiên bản thì cập nhật báo cáo hiện có thay vì tạo báo cáo mới.
- Agent chỉ đề xuất dòng RTM; việc cập nhật RTM chính thức do người có thẩm quyền thực hiện theo `.kiro/skills/ba-03-specification/assets/rtm.md`.
- Mỗi lần chạy ghi lại: prompt version, model/version, danh sách nguồn kèm phiên bản, báo cáo tạo thành, người review và quyết định (SOP §8).
