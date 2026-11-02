# BA-T06 — UAT Report

Template này khớp sheet `UAT Report` của `assets/_archive/workbook-v1.0.md` (17 cột).
Gồm ba phần: thông tin đợt UAT (6 cột đầu), bảng kịch bản (9 cột) và phần tổng hợp, trong đó có 2 cột `Decision`, `Approver`. Trường ⚠ là phần thêm.

## Phần 1 — Thông tin đợt UAT

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Project | `<tên dự án>` | |
| Release/Build | `<vX.Y / build số>` | Phải khớp build thực sự được test |
| Environment | `<UAT / Staging / …>` | Ghi rõ, không để trống |
| UAT Date | `<YYYY-MM-DD hoặc khoảng ngày>` | |
| Business Owner | `<tên / vai trò>` | Người chịu trách nhiệm nghiệp vụ |
| Participants | `<danh sách người thực hiện>` | Ghi đủ người đã thực sự chạy scenario |

## Phần 2 — Bảng kịch bản UAT

| Scenario ID | Scenario Description | Expected Result | Actual Result | Status | Defect ID | Severity | Evidence Link | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UAT-001 | `<mô tả kịch bản>` | `<kết quả mong đợi theo AC>` | `<kết quả thực tế>` | `Not Run` | | | `<URL bằng chứng>` | `<AC/BR liên kết>` |
| UAT-002 | | | | `Not Run` | | | | |

## Phần 3 — Tổng hợp và quyết định

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Total Scenarios | `<số>` | Đếm từ bảng trên |
| Passed | `<số>` | Chỉ đếm khi `Status = Pass` và có `Evidence Link` |
| Failed | `<số>` | |
| Blocked | `<số>` | Ghi lý do block vào `Notes` |
| Not Run | `<số>` | Không được tính là Pass |
| Skipped ⚠ | `<số>` | Ngoài phạm vi đợt UAT; có lý do và người duyệt. Tổng năm trạng thái phải bằng `Total Scenarios` |
| Open Risks | `<rủi ro còn mở>` | Kèm mức tác động theo đánh giá của người có thẩm quyền |
| Decision | `<Pending / Accept / Reject / Conditional Acceptance>` | Mặc định `Pending` |
| Approver | `<người có thẩm quyền>` | **BA và AI không tự điền** |
| Approval Date | `<YYYY-MM-DD>` | SOP §6 BA-T06 `Approver / Date` |
| Conditions ⚠ | `<điều kiện — owner — hạn>` | Bắt buộc khi `Decision = Conditional Acceptance` |

## Giá trị hợp lệ

| Cột | Giá trị |
| --- | --- |
| Status | `Not Run` \| `Pass` \| `Fail` \| `Blocked` \| `Skipped` |
| Severity | Theo thang của dự án; workbook ví dụ dùng `Critical` \| `Major` \| `Minor` |
| Decision | `Pending` \| `Accept` \| `Reject` \| `Conditional Acceptance` |

Giá trị mặc định khi tạo dòng mới: `Status = Not Run`, `Decision = Pending`.

## Không tự điền (chỉ con người có thẩm quyền)
- `Status = Pass` khi chưa có kết quả thực thi thật.
- `Evidence Link` trỏ tới bằng chứng không tồn tại.
- `Severity` — do QA/dự án xác định theo thang đã thống nhất.
- `Decision` và `Approver` — người có thẩm quyền nghiệm thu.
- `Expected Result` suy ra từ ý BA thay vì từ AC đã duyệt.

## Quy tắc điền
- Mỗi Scenario phải trỏ về một `Story ID` + `AC ID` (ghi trong `Notes`) để giữ truy vết.
- Sai khác phát hiện được phân loại ngay: `Defect` / `Requirement gap` / `Change request` — xem `../references/quality-gate-g4.md`.
- `Blocked` phải ghi lý do và dependency đang chặn.
- Sau khi điền xong, cập nhật `ba-records/<project>/rtm.md`: `UAT Result`, `Evidence Link`, `Coverage Status`. `Skipped` tương ứng với `Not Run - Out of Scope` trong RTM.
- Không sửa `Actual Result` sau khi Business User đã xác nhận; nếu cần đính chính, thêm dòng mới và ghi chú.
