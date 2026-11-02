# BA-T04 — Requirement Traceability Matrix (RTM)

Template chỉ đọc, dùng chung của bộ skill BA. Khớp sheet `RTM` của `assets/_archive/workbook-v1.0.md` (10 cột). RTM thật của dự án lưu tại `ba-records/<project>/rtm.md`.

**Nơi tham chiếu file này:**
- `skills/ba-03-specification/SKILL.md` — tạo dòng nháp ở Bước 4, bỏ ghi chú nháp khi Story/AC được xác nhận ở Bước 6.
- `skills/ba-06-test-uat/SKILL.md` — cập nhật `Test Case ID`, `Test Result`, `UAT Result`, `Evidence Link`.
- `skills/ba-07-release-handover/SKILL.md` — đối chiếu phạm vi phát hành với RTM.
- `skills/ba-agent-test-design/SKILL.md` — liên kết Test Case với AC.
- `skills/ba-agent-traceability/SKILL.md` — phát hiện liên kết thiếu và orphan records.

## Chuỗi liên kết
```
Requirement ID → Story ID → AC ID → Test Case ID → Test Result → UAT Result → Evidence Link
```
Mỗi yêu cầu cần kiểm thử phải đi hết chuỗi này. Liên kết bị suy luận **không** được tính là đã xác nhận.

## Bảng RTM

| Requirement ID | Story ID | AC ID | Test Case ID | Test Result | UAT Result | Evidence Link | Version | Coverage Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | US-001 | AC-01 | TC-001 | Not Run | Not Run | `<URL bằng chứng>` | 0.1 | Pending | |
| REQ-001 | US-001 | AC-02 | | Not Run | Not Run | | 0.1 | Missing Link | Chưa có Test Case |

## Giá trị hợp lệ

| Cột | Giá trị |
| --- | --- |
| Test Result | `Not Run` \| `Pass` \| `Fail` \| `Blocked` \| `N/A` |
| UAT Result | `Not Run` \| `Pass` \| `Fail` \| `Blocked` \| `Not Run - Out of Scope` |
| Coverage Status | `Pending` \| `Covered` \| `Missing Link` \| `Orphan` \| `Version Mismatch` \| `Blocked` |
| Version | Phiên bản tài liệu yêu cầu tại thời điểm ghi nhận |

Giá trị mặc định khi tạo dòng mới: `Test Result = Not Run`, `UAT Result = Not Run`. `Coverage Status` là `Missing Link` khi chưa có Test Case và `Pending` khi đã có.

Giá trị `Not Run - Out of Scope` của `UAT Result` tương ứng với `Status = Skipped` trong UAT Report.

## Ý nghĩa Coverage Status
| Trạng thái | Nghĩa | Hành động |
| --- | --- | --- |
| `Pending` | Có Test Case nhưng chưa đủ kết quả, hoặc còn `Fail` chờ retest | Chờ QA/UAT thực thi |
| `Covered` | Có Test Case; `Test Result = Pass` (hoặc `N/A` đã được duyệt); `UAT Result = Pass` (hoặc `Not Run - Out of Scope` đã được duyệt); có `Evidence Link` | Không cần hành động |
| `Missing Link` | Thiếu một mắt xích trong chuỗi | Bổ sung Test Case hoặc liên kết |
| `Orphan` | Test Case/Story không trỏ về Requirement nào | Xác minh nguồn hoặc loại bỏ |
| `Version Mismatch` | Tài liệu hai đầu khác phiên bản | Đối chiếu phiên bản, cập nhật |
| `Blocked` | Không kiểm thử được vì phụ thuộc | Ghi lý do vào `Notes`, báo PO |

## Không tự điền
- `Test Result`, `UAT Result` — chỉ điền khi **có kết quả thực thi thật** kèm `Evidence Link`. Không bao giờ đặt `Pass` suy đoán.
- `Evidence Link` — phải trỏ tới bằng chứng có thật (test run, log, biên bản UAT).
- Quyết định chấp nhận yêu cầu không có test (`N/A`) — cần người có thẩm quyền.

## Quy tắc cập nhật
- Mỗi thay đổi yêu cầu (xem `ba-05-change-management`) phải rà lại toàn bộ dòng RTM liên quan.
- Không xoá dòng lịch sử khi thay đổi phiên bản; tăng `Version` và ghi `Notes`.
- Kiểm tra trùng trước khi thêm dòng: cùng bộ `Requirement ID + Story ID + AC ID + Test Case ID + Version` là một dòng.
- Gắn Test Case đầu tiên cho dòng còn trống `Test Case ID` trong cùng `Version`: cập nhật dòng đó. Test Case tiếp theo của cùng AC: thêm dòng mới.
- Khi đổi phiên bản: thêm dòng mới với `Version` mới, đặt lại `Test Result` và `UAT Result` về `Not Run` nếu AC thay đổi, và ghi `Notes` ở dòng cũ là `Superseded by <Version>`.
- Người cập nhật: QA ghi `Test Case ID`, `Test Result`; BA ghi `UAT Result`, `Evidence Link` theo kết quả Business User xác nhận; BA ghi `Coverage Status` sau khi đối chiếu. Agent chỉ đề xuất.
- KPI `Traceability Coverage` (SOP §9) đếm dòng đã có liên kết Test Case phù hợp, tức dòng cần test không ở trạng thái `Missing Link` hoặc `Orphan`; không đòi hỏi đã chạy test.
