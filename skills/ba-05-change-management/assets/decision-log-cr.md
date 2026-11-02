# BA-T05 — Decision Log & Change Request

Template này khớp sheet `Change Log` của `assets/_archive/workbook-v1.0.md` (13 cột).
Dùng cho **hai loại bản ghi**: quyết định làm rõ yêu cầu (Decision) và yêu cầu thay đổi (CR). Đánh dấu loại ở `Decision/CR ID`.

## Bản ghi

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Decision/CR ID | `<CR-000 / DEC-000>` | Kiểm tra trùng trước khi phát hành |
| Date | `<YYYY-MM-DD>` | Ngày ghi nhận, không phải ngày đề xuất |
| Requester | `<tên / vai trò>` | Người nêu câu hỏi hoặc đề xuất thay đổi |
| Current Requirement | `<REQ/US/AC/BR ID + nội dung hiện tại>` | Trích đúng phiên bản đang hiệu lực |
| Proposed Change | `<nội dung đề xuất>` | Tách bạch rõ với hiện trạng |
| Business Reason | `<lý do>` | Ghi theo lời người đề xuất, không tự suy ra |
| Impact Analysis | `<xem bảng bên dưới>` | Bắt buộc với CR; đủ 8 nhóm |
| Options | `<phương án A / B / C + hệ quả>` | Tối thiểu hai phương án khi có thể |
| Decision | `<Pending / Approved / Rejected / Deferred>` | Mặc định `Pending` |
| Approver | `<người có thẩm quyền>` | **BA và AI không tự điền** |
| Effective Version | `<phiên bản tài liệu áp dụng>` | |
| Communication | `<đã thông báo ai, kênh nào, ngày nào>` | Thiếu mục này là không đạt gate thay đổi |
| Status | `<Proposed / Under Review / Approved / Rejected / Implemented>` | Theo SOP §12 |

## Bảng Impact Analysis

| Đối tượng bị ảnh hưởng | ID cụ thể | Mức ảnh hưởng | Hành động cần làm | Owner |
| --- | --- | --- | --- | --- |
| Story / AC | `<US-000 / AC-00>` | `<Không / Nhẹ / Lớn>` | | |
| Business Rules | `<BR-000>` | | | |
| API / interface | `<tên endpoint>` | | | |
| Dữ liệu | `<bảng / trường / migration>` | | | |
| Test Case | `<TC-000>` | | | |
| Tài liệu | `<URD/BRD/Business Rules + phiên bản>` | | | |
| Sprint | `<Sprint hiện tại / kế tiếp>` | | | |
| RTM | `<số dòng cần cập nhật>` | | | |

Nếu AI đề xuất danh sách ảnh hưởng: đánh dấu `[AI đề xuất - chưa xác minh]` cho tới khi BA kiểm tra. Không tính liên kết suy luận là liên kết đã xác nhận.

## Decision Log (câu trả lời làm rõ, không thay đổi yêu cầu)

| Decision ID | Date | Câu hỏi nguyên văn | Người hỏi | Câu trả lời | Nguồn | Người xác nhận |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | `<...>` | `<trích nguyên văn>` | `<...>` | `<...>` | `<URL + vị trí>` | `<BA / Business>` |

Câu trả lời không có nguồn: ghi `[Unknown]` vào `Open Questions` của Story/AC liên quan, không điền vào Decision Log như thể đã xác nhận.

## Không tự điền (chỉ con người có thẩm quyền)
- `Approver`, `Decision` khác `Pending`.
- Thứ tự ưu tiên và cách xử lý Product Backlog — PO quyết định.
- Cách xử lý Sprint Backlog — Scrum Team quyết định.
- Phê duyệt thay đổi liên quan ngân sách, hợp đồng, nghiệm thu chính thức.

## Quy tắc điền
- Mỗi CR phải có `Impact Analysis` và `Communication` trước khi chuyển `Implemented`.
- Không xoá bản ghi `Rejected`; giữ lại để truy vết.
- `Decision = Pending` hoặc `Deferred`: giữ `Status = Under Review` và ghi ngày xem lại.
- Bản ghi thật lưu tại `ba-records/<project>/change-log.md`.
- Sau khi `Approved`: cập nhật Story/AC, Business Rules, RTM và tăng `Effective Version` trong cùng đợt.
- CR bị treo quá lâu mà Sprint vẫn chạy: báo PO, ghi rủi ro, không tự coi là đã duyệt.
