# Definition of Readiness — tham khảo cho BA-04

SOP ghi rõ: DoR này **không bắt buộc theo Scrum Guide**, là khung tham khảo nội bộ và cần ánh xạ với quy ước của Team.

## Checklist DoR

| # | Tiêu chí | Cách kiểm tra | Đạt / Không | Người xác nhận |
| --- | --- | --- | --- | --- |
| 1 | Mục tiêu rõ | `So that` trỏ về Business Objective cụ thể | | BA + PO |
| 2 | Có AC | Mỗi hành vi chính có ít nhất một `AC ID` | | BA |
| 3 | AC kiểm thử được | QA xác nhận `Given/When/Then` tái lập và quan sát được | | QA |
| 4 | Câu hỏi quan trọng đã xử lý | Không còn `Open Questions` chặn việc triển khai | | BA |
| 5 | Dependency xác định | Có tên hệ thống/nhóm sở hữu và trạng thái | | Dev/Tech Lead |
| 6 | Testability đủ | Có dữ liệu và môi trường kiểm thử, hoặc biết cách lấy | | QA |
| 7 | Liên kết truy vết | Có dòng RTM cho Story/AC | | BA |
| 8 | Kích thước phù hợp | Team đánh giá hoàn tất được trong một Sprint | | Team |

**Chỉ Team xác nhận tiêu chí 8. Chỉ PO quyết định thứ tự. AI không đánh dấu bất kỳ tiêu chí nào.**

## Tình huống chưa Ready nhưng vẫn bị yêu cầu đưa vào Sprint
Không tự đánh dấu Ready. Ghi rõ:
1. Tiêu chí nào chưa đạt và bằng chứng.
2. Ai là người quyết định chấp nhận rủi ro (PO).
3. Nếu PO chấp nhận, ghi quyết định vào Decision Log — dùng `skills/ba-05-change-management/assets/decision-log-cr.md`.

## Biên bản phiên refinement

| Trường | Giá trị |
| --- | --- |
| Ngày / Sprint | `<...>` |
| Tham dự | `<BA, PO, Dev/Tech Lead, QA, khác>` |
| Story đã rà soát | `<US-000, US-000, …>` |
| Story đạt DoR | `<danh sách + người xác nhận>` |
| Story chưa đạt DoR | `<danh sách + tiêu chí thiếu>` |
| Story bị tách | `<US cũ → US mới; đã cập nhật RTM chưa>` |
| Estimate | `<do Team ghi — BA không điền>` |
| Quyết định thứ tự | `<PO ghi>` |
| Câu hỏi còn mở + owner | `<...>` |
| Hành động tiếp theo | `<việc — người — hạn>` |

## Quy tắc ghi biên bản
- Không ghi estimate hoặc priority thay Team/PO.
- Story bị tách phải kèm hành động cập nhật RTM, nếu không sẽ phát sinh `Missing Link`.
- Mọi quyết định phát sinh trong phiên mà làm thay đổi yêu cầu thì chuyển sang `ba-05-change-management`.
