# Output schema — Specification Agent

Tham chiếu: `assets/_archive/prompt-pack-v1.0.md` §3 và "Định dạng chung đề xuất"; `assets/_archive/workbook-v1.0.md` sheet `User Story AC`; `assets/_archive/sop-v1.0.md` §8, §12.

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
| Summary | Story nào được tạo, phân rã từ đâu, dựa trên Requirement ID nào |
| Facts with sources | Story/AC kèm Source Links, Requirement ID, Business Rule ID |
| Findings / Open Questions | Điểm mơ hồ, luồng còn thiếu, nghi ngờ trùng lặp, mâu thuẫn với nguồn |
| Suggested actions | Việc BA/PO cần làm trước khi đưa vào refinement |
| Confidence limitations | Phần AC chưa đủ căn cứ, phần tự review chưa kết luận được |
| Status | Luôn là `DRAFT` |

Self-review Findings được trình bày trong phần 3, mỗi finding nêu rõ tiêu chí (`Clarity | Consistency | Testability | Duplicate`), bằng chứng và đề xuất.

## 2. Ánh xạ sang sheet `User Story AC` (18 cột)

| Cột | Ý nghĩa | Quy tắc điền |
|---|---|---|
| Epic ID | Epic cha | Kế thừa từ tài liệu phân tích; không tự tạo Epic mới |
| Story ID | Định danh Story | Theo quy ước team; kiểm tra trùng trước khi cấp ID mới |
| Title | Tên Story | Ngắn, nêu được Actor và nhu cầu |
| As a | Actor | Phải khớp Actor đã xác định trong phân tích |
| I want | Nhu cầu | Không nhét giải pháp kỹ thuật khi nguồn chưa nêu |
| So that | Giá trị | Lấy từ Business Objective/Business Value có nguồn |
| Business Value | Giá trị nghiệp vụ | Ghi theo nguồn; nếu nguồn chưa nêu → Open Question |
| Requirement IDs | Requirement liên kết | Bắt buộc; nhiều ID phân tách bằng dấu phẩy |
| Business Rule IDs | Business Rule áp dụng | Chỉ liên kết BR đã có trong Business Rules Catalog |
| AC ID | Định danh AC | `AC-01`, `AC-02`... chỉ duy nhất trong phạm vi Story; tham chiếu từ nơi khác phải kèm `Story ID` |
| Given | Bối cảnh | Nêu điều kiện tiền đề và quyền truy cập |
| When | Hành động | Một hành động xác định, không mơ hồ |
| Then | Kết quả mong đợi | Phải kiểm thử được; không dùng từ không đo được |
| Validation/Error Cases | Validation và luồng lỗi | Chỉ ghi trường hợp có căn cứ từ nguồn hoặc Business Rule |
| Data/Permissions/Integration | Dữ liệu, quyền, tích hợp | Liệt kê theo tài liệu phân tích |
| NFR | NFR áp dụng | Liên kết `NFR-xxx` đã có; không tự đặt ngưỡng |
| Open Questions | Câu hỏi mở | Mỗi câu hỏi gắn với AC hoặc phần Story bị chặn |
| Review Status | Trạng thái review | **Con người sở hữu** — Agent ghi `Draft` |
| Version ⚠ | Phiên bản Story | Trường thêm; bản nháp AI bắt đầu ở `0.1` |
| Confirmed By / Date ⚠ | Người xác nhận và ngày | Trường thêm; **con người sở hữu** — Agent để trống |

## 3. Quy tắc viết Story và AC

- Story: đủ Actor, nhu cầu, giá trị; một Story một mục đích; phân rã khi Story bao gồm nhiều luồng nghiệp vụ độc lập.
- AC: mỗi AC kiểm thử được một hành vi; `Given` nêu bối cảnh và quyền, `When` nêu một hành động, `Then` nêu kết quả quan sát được.
- Tránh từ mơ hồ: nhanh, thân thiện, dễ dùng, chính xác, phù hợp — trừ khi nguồn định nghĩa được bằng con số.
- Mỗi AC phải truy ngược được tới `Requirement ID` hoặc `Business Rule ID`. AC không truy ngược được → không tạo, chuyển thành Open Question.

## 4. Checklist tự review

| Tiêu chí | Câu hỏi kiểm tra |
|---|---|
| Clarity | Có từ mơ hồ, đa nghĩa, thiếu chủ ngữ không? |
| Consistency | AC có mâu thuẫn với nhau, với Business Rule hoặc với Requirement không? |
| Testability | Có dữ liệu đầu vào, hành động và kết quả quan sát được để viết test không? |
| Duplicate | Story/AC có trùng với bản ghi đã tồn tại không? |

Tự review chỉ tạo finding, không tự kết luận Story đạt chất lượng.

## 5. Dừng bước khi nào

Dừng và báo lại BA, không tự chế nội dung thay thế, khi:

1. Requirement hoặc tài liệu phân tích chưa ở trạng thái đã review.
2. Thiếu `Business Rule ID` cho hành vi mà AC bắt buộc phải dựa vào.
3. Actor chưa được xác định hoặc hai nguồn nêu hai Actor khác nhau.
4. Không xác định được Business Value từ nguồn.
5. Phát hiện Story đã tồn tại cho cùng `Requirement IDs` và cùng phạm vi.
6. Tài liệu nguồn không có phiên bản hoặc không xác định được bản chính thức.

Khi dừng: nêu rõ Story/AC bị chặn, lý do, nguồn liên quan và thông tin cần cung cấp.

## 6. Idempotency và audit trail

- Trước khi tạo Story mới, tra theo `Requirement IDs` + `Title` + `Epic ID`. Nếu đã có Story cho cùng phạm vi, cập nhật bản nháp hiện có thay vì tạo mới.
- Mỗi lần chạy ghi lại: prompt version, model/version, tài liệu đầu vào kèm phiên bản, Story/AC tạo thành, người review và quyết định (SOP §8), theo template `assets/ai-run-log.md` ở gốc power; bản ghi thật tại `ba-records/<project>/ai-run-log.md`.
- Sau khi Story được tạo, liên kết `Requirement ID → Story ID → AC ID` cần được ghi vào `ba-records/<project>/rtm.md` theo template `skills/ba-03-specification/assets/rtm.md`.
