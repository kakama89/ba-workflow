# Finding table — QA Review Agent

Tham chiếu: `assets/_archive/prompt-pack-v1.0.md` §4; `assets/_archive/workbook-v1.0.md` sheet `AI Review`; `assets/_archive/sop-v1.0.md` §7, §8.

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

Bảng finding đặt trong phần 3, dùng đúng bố cục 7 cột của `assets/_archive/prompt-pack-v1.0.md` §4:

`Finding ID | Category | Severity | Evidence | Requirement Reference | Suggested Action | Owner`

## 2. Định nghĩa từng cột

| Cột | Ý nghĩa | Quy tắc |
|---|---|---|
| Finding ID | Định danh finding | `F-01`, `F-02`... trong phạm vi một lần review; ánh xạ sang `Review ID` (`AIR-xxx`) khi ghi log |
| Category | Nhóm kiểm tra | Đúng một trong 8 giá trị enum ở mục 3; finding thuộc hai nhóm thì tách thành hai dòng |
| Severity | Mức nghiêm trọng | `Critical \| Major \| Minor \| Info`, theo rubric mục 4 |
| Evidence | Bằng chứng | Con trỏ chính xác: AC ID, BR ID, đoạn trích, dòng/cột. Không có Evidence thì không được ghi finding |
| Requirement Reference | Đối tượng bị ảnh hưởng | `Requirement ID`, `Story ID`, `AC ID`, `Document ID` hoặc `Decision/CR ID` |
| Suggested Action | Việc nên làm | Hành động cụ thể; với rủi ro cần xác minh thì ghi rõ xác minh với ai |
| Owner | Vai trò xử lý | `BA \| PO \| QA \| Business Owner` — là vai trò nên xử lý, không phải người đã duyệt |

## 3. Giá trị enum

- **Check Category:** `Completeness | Clarity | Consistency | Testability | Traceability | Negative Cases | NFR | Change Impact`
- **Severity:** `Critical | Major | Minor | Info`
- **Status (khi ghi log):** `Open | In Review | Resolved | Accepted Risk` — Agent chỉ được ghi `Open`
- **Status đầu ra của Agent:** `DRAFT` (cố định)

Ý nghĩa 8 Check Category:

| Category | Kiểm tra điều gì |
|---|---|
| Completeness | Thiếu luồng, thiếu Actor, thiếu validation, thiếu phạm vi |
| Clarity | Từ mơ hồ, đa nghĩa, câu không xác định được hành vi |
| Consistency | Mâu thuẫn giữa AC, giữa Story với Business Rule, giữa các phiên bản tài liệu |
| Testability | Không có dữ liệu đầu vào, hành động hoặc kết quả quan sát được |
| Traceability | Story/AC không truy ngược được Requirement ID hoặc Business Rule ID |
| Negative Cases | Thiếu luồng lỗi, ngoại lệ, trường hợp biên có căn cứ |
| NFR | Thiếu hoặc không kiểm thử được NFR đã nêu trong phân tích |
| Change Impact | Thay đổi chưa được đánh giá tác động lên Story/AC/Test Case/RTM |

## 4. Rubric Severity

| Severity | Tiêu chí |
|---|---|
| Critical | Làm tài liệu không dùng được để phát triển hoặc kiểm thử: thiếu hoàn toàn luồng chính, mâu thuẫn trực tiếp với Business Rule, hoặc thay đổi phạm vi chưa được đánh giá tác động |
| Major | Gây hiểu sai hoặc không kiểm thử được một phần quan trọng: AC mơ hồ, thiếu validation bắt buộc, thiếu liên kết truy vết của Story chính |
| Minor | Ảnh hưởng chất lượng nhưng không chặn công việc: diễn đạt chưa gọn, thiếu chi tiết phụ, liên kết truy vết của trường hợp biên còn thiếu |
| Info | Ghi nhận để cải thiện, không phải lỗi: gợi ý trình bày, điểm nên làm rõ thêm ở vòng sau |

Không hạ Severity để artifact đạt Quality Gate. Khi phân vân giữa hai mức, ghi mức cao hơn và nêu lý do trong `Confidence limitations`, để người review quyết định.

## 5. Lỗi xác định được và rủi ro cần xác minh

- **Lỗi xác định được:** chỉ ra được bằng chứng trực tiếp trong tài liệu (ví dụ AC mâu thuẫn với BR-001). Ghi ở dạng khẳng định.
- **Rủi ro cần xác minh:** dấu hiệu có thể là lỗi nhưng thiếu nguồn kết luận (ví dụ AC im lặng về hành vi khi không có dữ liệu). Ghi ở dạng cần xác minh, nêu rõ xác minh với ai; không khẳng định đó là lỗi.

Hai loại này không được trình bày lẫn lộn trong cùng một finding.

## 6. Dừng bước khi nào

Dừng và báo lại BA, không tự chế nội dung thay thế, khi:

1. Artifact cần review không truy cập được hoặc không có phiên bản.
2. Thiếu nguồn đối chiếu bắt buộc của giai đoạn đang review (xem mục Đầu vào trong `SKILL.md`). Business Rules Catalog chỉ bắt buộc từ BA-03 trở đi.
3. Artifact đang ở trạng thái chưa hoàn thiện đến mức không thể review có ý nghĩa.
4. Phát hiện artifact đã thay đổi trong lúc đang review.
5. Một finding yêu cầu truy cập tài nguyên ngoài phạm vi được cấp quyền.
6. Tài liệu chứa dữ liệu nhạy cảm chưa được phép xử lý bằng công cụ hiện tại.

Khi dừng: nêu rõ phạm vi đã review được, phạm vi bị chặn, lý do và thông tin cần cung cấp.

## 7. Idempotency và audit trail

- Trước khi tạo finding mới, tra log theo `Artifact ID` + `Check Category` + nội dung finding. Nếu đã có, cập nhật dòng hiện có thay vì tạo dòng mới.
- Mỗi lần review ghi lại: prompt version, model/version, artifact kèm phiên bản, danh sách finding, người review và quyết định (SOP §8), theo template `assets/ai-run-log.md` ở gốc power; bản ghi thật tại `ba-records/<project>/ai-run-log.md`.
