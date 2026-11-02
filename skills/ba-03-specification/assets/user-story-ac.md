# BA-T03 — User Story & Acceptance Criteria

Template này khớp sheet `User Story AC` của `assets/_archive/workbook-v1.0.md` (18 cột). Trường và cột ⚠ là phần thêm mà G3 hoặc truy vết cần, sheet chưa có.
Mỗi Story là một khối thông tin; mỗi AC là một dòng trong bảng AC.

## Khối Story

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Epic ID | `<EPIC-000>` | Mỗi Story thuộc đúng một Epic |
| Story ID | `<US-000>` | Duy nhất; kiểm tra trùng trước khi phát hành |
| Title | `<tiêu đề ngắn>` | Nói rõ hành vi, không nói giải pháp kỹ thuật |
| As a | `<Actor / vai trò>` | Lấy từ Stakeholder Map, không bịa vai trò mới |
| I want | `<nhu cầu>` | Một nhu cầu; nếu có hai thì cân nhắc tách Story |
| So that | `<giá trị nghiệp vụ>` | Phải trỏ về Business Objective |
| Business Value | `<mô tả giá trị>` | Không tự gán mức giá trị hoặc Priority |
| Requirement IDs | `<REQ-000>` | Bắt buộc, lấy từ BA-01 |
| Business Rule IDs | `<BR-000>` | Bắt buộc nếu Story hiện thực hoá quy tắc |
| Validation/Error Cases | `<trường hợp validation và lỗi>` | Tối thiểu một trường hợp cho mỗi luồng chính |
| Data/Permissions/Integration | `<dữ liệu / quyền / hệ thống>` | Ghi rõ Actor nào bị chặn khi thiếu quyền |
| NFR | `<NFR-000>` | Chỉ ghi khi có nguồn hoặc ràng buộc kỹ thuật |
| Open Questions | `<câu hỏi — owner>` | Câu hỏi quan trọng chưa đóng thì Story chưa `Ready for Refinement` |
| Review Status | `<Draft / In Review / Ready for Refinement / …>` | Theo SOP §12 |
| Version ⚠ | `<0.1>` | Tăng khi nội dung Story/AC thay đổi |
| Confirmed By / Date ⚠ | `<PO hoặc Business — YYYY-MM-DD>` | **BA và AI không tự điền**; điều kiện G3 |

## Bảng Acceptance Criteria

| AC ID | Given | When | Then | Nguồn / BR liên kết ⚠ | Test Case ID ⚠ |
| --- | --- | --- | --- | --- | --- |
| AC-01 | `<điều kiện đầu vào, trạng thái, quyền>` | `<hành động>` | `<kết quả quan sát được>` | `<BR-000 / URL>` | `<TC-000 hoặc trống>` |
| AC-02 | `<trường hợp ngoại lệ>` | `<hành động>` | `<thông báo lỗi / hành vi>` | `<BR-000>` | |

## Checklist AC kiểm thử được
Mỗi AC cần trả lời được:
- [ ] `Given` nêu đủ dữ liệu, trạng thái và quyền để tái lập.
- [ ] `When` là một hành động xác định, không mơ hồ.
- [ ] `Then` quan sát và đo được; không dùng từ như "nhanh", "thân thiện", "chính xác" mà không có ngưỡng từ nguồn.
- [ ] Có nguồn hoặc `Business Rule ID` cho hành vi được mô tả.
- [ ] Không trùng với AC khác trong cùng Story hoặc Story khác.

## Không tự điền (chỉ con người có thẩm quyền)
- `Priority`, Story Point, estimate — thuộc PO và Scrum Team ở `ba-04-refinement`.
- Phê duyệt DoR.
- `Business Value` ở mức định lượng khi nguồn không nêu.
- `Test Case ID` khi chưa có Test Case thực tế (xem `ba-06-test-uat`).
- Ngưỡng NFR chưa có trong nguồn.

## Quy tắc điền
- Story chưa đủ nhỏ để hoàn tất trong một Sprint: đề xuất tách, kèm lý do, không tự quyết.
- AC suy ra từ trao đổi miệng phải ghi `[Assumption]` và tạo câu hỏi mở cho tới khi Business xác nhận.
- Khi AI tạo bản nháp, giữ `Review Status = Draft`.
- `AC ID` chỉ duy nhất trong một Story; khi tham chiếu từ nơi khác phải ghi kèm `Story ID`.
- Tạo dòng RTM nháp ở Bước 4 trong `ba-records/<project>/rtm.md`; bỏ ghi chú nháp sau khi Story được xác nhận.
