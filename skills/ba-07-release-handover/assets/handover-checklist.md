# BA-T07 — Handover Checklist & Handover Pack

Template này khớp sheet `Handover` của `assets/_archive/workbook-v1.0.md` (7 cột, HO-001…HO-008). Bản ghi thật lưu tại `ba-records/<project>/handover/`.

## Checklist bàn giao

| Checklist ID | Hạng mục | Status | Evidence/Link | Owner | Due Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| HO-001 | Danh sách Story phát hành được xác nhận | `Not Started` | `<link RTM bản chốt>` | BA | | Đối chiếu từng Story với Test/UAT Result |
| HO-002 | URD/BRD và Business Rules đúng phiên bản | `Not Started` | `<link + version>` | BA | | Kiểm tra `Version Mismatch` trước |
| HO-003 | Release Notes và Known Issues cập nhật | `Not Started` | `<link>` | BA/PO | | Known Issues cần mức tác động |
| HO-004 | Test Result và UAT Result được lưu trữ | `Not Started` | `<link bằng chứng>` | QA/BA | | Bằng chứng phải mở được |
| HO-005 | CR chưa thực hiện đã được bàn giao | `Not Started` | `<link Change Log>` | BA/PO | | Ghi rõ `Status` từng CR |
| HO-006 | Vấn đề còn mở có người phụ trách | `Not Started` | `<link>` | Owner | | Không có owner là lỗi gate |
| HO-007 | AI output đã review trước khi xuất bản | `Not Started` | `<link bản review>` | BA | | Ghi prompt version + model |
| HO-008 | Đầu mối hỗ trợ sau phát hành đã xác định | `Not Started` | `<tên / kênh liên hệ>` | PO/Business | | SOP §6 BA-T07: "Support owner identified" |

Giá trị `Status` hợp lệ: `Not Started` | `In Progress` | `Done` | `Blocked` | `N/A`. Mặc định khi tạo: `Not Started`.

## Biên bản Handover Pack

| Trường | Giá trị |
| --- | --- |
| Project / Release | `<...>` |
| Phiên bản tài liệu bàn giao | `<...>` |
| Ngày bàn giao | `<YYYY-MM-DD>` |
| Người bàn giao | `<BA>` |
| **Người nhận bàn giao** | `<tên / bộ phận>` — bắt buộc, thiếu là không đạt gate |
| Phạm vi phát hành | `<danh sách Story/AC>` |
| Kết quả kiểm thử | `<Passed / Failed / Blocked / Not Run>` — lấy từ UAT Report |
| Quyết định nghiệm thu | `<Accept / Conditional Acceptance + Approver + ngày>` |
| Điều kiện nghiệm thu ⚠ | `<điều kiện — owner — hạn>`; bắt buộc khi `Conditional Acceptance` |
| Known Issues | `<vấn đề — tác động — xử lý tạm — owner>` |
| CR còn mở | `<CR ID — Status — người theo dõi>` |
| Đầu mối hỗ trợ | `<tên / kênh / giờ làm việc>` |
| Action Items từ Retrospective | `<việc — owner — hạn>` |

## Không tự điền (chỉ con người có thẩm quyền)
- `Status = Done` khi chưa có `Evidence/Link`.
- Người nhận bàn giao.
- Quyết định nghiệm thu và `Approver`.
- Mức tác động của Known Issues.
- Nội dung bài học/FAQ do AI dự thảo khi BA chưa review.

## Quy tắc điền
- Mỗi dòng `Done` phải có bằng chứng mở được; nếu không, giữ `In Progress` hoặc `Blocked`.
- `N/A` phải ghi lý do trong `Notes`, không dùng để bỏ qua hạng mục.
- HO-007 là điều kiện gate: mọi tài liệu xuất bản có phần do AI dự thảo đều phải ghi lại prompt version, model/version và người review.
- Sau khi đóng checklist, lưu bản đã duyệt vào Knowledge Base và khoá phiên bản.
