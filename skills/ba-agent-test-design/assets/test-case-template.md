# Test Case Template

Biểu mẫu thiết kế test case theo `assets/_archive/prompt-pack-v1.0.md` §5. Mỗi test case một khối hoặc một dòng bảng.

| Test Case ID | Story ID | Requirement/AC ID | Scenario Type | Preconditions | Steps | Test Data | Expected Result | Priority | Open Questions |
|---|---|---|---|---|---|---|---|---|---|
| <TC-xxx> | <US-001> | <REQ-001 / AC-01> | <Happy path \| Negative path \| Boundary \| Permission \| Integration \| Error handling> | <trạng thái hệ thống, dữ liệu nền, quyền cần có> | <1. bước một / 2. bước hai / 3. bước ba> | <giá trị đầu vào cụ thể hoặc dạng giá trị> | <kết quả quan sát được, đối chiếu AC hoặc BR> | <để trống nếu không có quy tắc> | <điểm AC chưa nói rõ> |

## Dòng RTM nháp tương ứng

Ghi theo `skills/ba-03-specification/assets/rtm.md` (sheet `RTM`, 10 cột):

| Requirement ID | Story ID | AC ID | Test Case ID | Test Result | UAT Result | Evidence Link | Version | Coverage Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| <REQ-001> | <US-001> | <AC-01> | <TC-xxx> | Not Run | Not Run | <để trống> | <0.1> | Pending | <test nháp do AI đề xuất, chưa thực thi> |

## Cách điền

- `Test Case ID`: theo quy ước `TC-xxx`; tra danh sách test hiện có của cùng `Story ID` + `AC ID` trước khi cấp ID mới.
- `Story ID`: bắt buộc vì `AC ID` chỉ duy nhất trong một Story.
- `Scenario Type`: đúng một trong 6 loại scenario.
- `Requirement/AC ID`: bắt buộc; mỗi test phải truy ngược được ít nhất một `AC ID` hoặc `Requirement ID`.
- `Preconditions`: dữ liệu nền, trạng thái hệ thống và quyền truy cập cần có trước khi chạy.
- `Steps`: đánh số, mỗi bước một hành động, đủ để người khác chạy lại y hệt.
- `Test Data`: giá trị cụ thể hoặc dạng giá trị; với boundary thì nêu rõ giá trị tại biên, dưới biên và trên biên.
- `Expected Result`: kết quả quan sát được, đối chiếu trực tiếp với `Then` của AC hoặc Business Rule đã nêu.
- `Priority`: chỉ điền khi dự án có quy tắc xác định Priority cho test; nếu không có quy tắc thì để trống và nêu trong `Open Questions`.
- `Open Questions`: hành vi AC chưa nói rõ, validation chưa xác định, dữ liệu/môi trường chưa được cấp quyền.
- Dòng RTM: `Test Result` và `UAT Result` luôn là `Not Run`, `Coverage Status` luôn là `Pending`.

## Không tự điền

Các trường sau thuộc thẩm quyền con người hoặc chỉ có sau khi thực thi, Agent để trống:

- `Evidence Link` — chỉ có sau khi test chạy và có bằng chứng lưu lại.
- `Test Result` và `UAT Result` — không điền giá trị khác `Not Run`; kết quả thật do người thực thi ghi.
- `Coverage Status` — không điền `Covered`; trạng thái này do người có thẩm quyền xác nhận sau khi đối chiếu.
- `Priority` — không tự đặt khi không có quy tắc xác định trong tài liệu dự án.
- Trạng thái Pass/Fail ở bất kỳ trường nào — Agent không tuyên bố test đã chạy.
