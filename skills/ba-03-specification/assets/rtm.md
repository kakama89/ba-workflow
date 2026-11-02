# BA-T04 — Requirement Traceability Matrix (RTM)

Template dùng chung của bộ skill BA. Khớp sheet `RTM` của `assets/_archive/workbook-v1.0.md` (10 cột).

**Nơi tham chiếu file này:**
- `skills/ba-03-specification/SKILL.md` — tạo dòng RTM khi Story/AC được xác nhận.
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

Giá trị mặc định khi tạo dòng mới: `Test Result = Not Run`, `UAT Result = Not Run`, `Coverage Status = Pending`.

## Ý nghĩa Coverage Status
| Trạng thái | Nghĩa | Hành động |
| --- | --- | --- |
| `Pending` | Chưa có kết quả kiểm thử | Chờ QA/UAT thực thi |
| `Covered` | Có Test Case và kết quả phù hợp | Không cần hành động |
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
- Kiểm tra trùng trước khi thêm dòng: cùng bộ `Requirement ID + Story ID + AC ID + Test Case ID` là một dòng.
- RTM là đầu vào chính của KPI `Traceability Coverage` (SOP §9).
