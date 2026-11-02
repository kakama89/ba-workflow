# Output schema — Test Design Agent

Tham chiếu: `assets/_archive/prompt-pack-v1.0.md` §5 và "Định dạng chung đề xuất"; `assets/_archive/workbook-v1.0.md` sheet `RTM`; `assets/_archive/sop-v1.0.md` §7, §8.

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
| Summary | Bao nhiêu test case, bao phủ những loại scenario nào, cho AC/Requirement nào |
| Facts with sources | Bảng test case; mỗi dòng trỏ tới `AC ID` hoặc `Business Rule ID` làm căn cứ |
| Findings / Open Questions | AC im lặng ở luồng nào, validation chưa xác định, dữ liệu/môi trường chưa được cấp quyền |
| Suggested actions | Test nên chạy trước, điểm cần BA làm rõ với Business |
| Confidence limitations | Scenario nào thiếu căn cứ, test nào chỉ là đề xuất chưa đối chiếu môi trường thật |
| Status | Luôn là `DRAFT` |

## 2. Định nghĩa từng trường đầu ra

| Trường | Ý nghĩa | Quy tắc |
|---|---|---|
| Test Case ID | Định danh test case | `TC-xxx`; kiểm tra trùng trước khi cấp ID mới |
| Requirement/AC ID | Liên kết truy vết | Bắt buộc; nhiều ID phân tách bằng dấu phẩy |
| Preconditions | Điều kiện tiền đề | Trạng thái hệ thống, dữ liệu nền, quyền truy cập |
| Steps | Các bước thực hiện | Đánh số, mỗi bước một hành động, chạy lại được y hệt |
| Test Data | Dữ liệu thử nghiệm | Giá trị cụ thể hoặc dạng giá trị; boundary nêu tại biên, dưới biên, trên biên |
| Expected Result | Kết quả mong đợi | Quan sát được, đối chiếu `Then` của AC hoặc Business Rule |
| Priority | Độ ưu tiên test | Chỉ điền khi có quy tắc xác định; nếu không → để trống và nêu ở Open Questions |
| Open Questions | Câu hỏi chưa rõ | Mỗi câu hỏi gắn với test case hoặc AC bị ảnh hưởng |

## 3. Phạm vi 6 loại scenario

Chỉ đề xuất scenario khi có căn cứ từ AC hoặc Business Rule:

| Loại | Bao phủ | Căn cứ thường lấy từ |
|---|---|---|
| Happy path | Luồng chính thành công | `Given-When-Then` của AC |
| Negative path | Đầu vào sai, hành động bị từ chối | `Validation/Error Cases`, Business Rule |
| Boundary | Giá trị tại biên, dưới biên, trên biên | Giới hạn đã nêu trong nguồn; không tự đặt ngưỡng |
| Permission | Người dùng có quyền và không có quyền | `Data/Permissions/Integration` |
| Integration | Tương tác giữa các hệ thống | Tích hợp đã nêu trong phân tích |
| Error handling | Hệ thống lỗi, timeout, không có dữ liệu | `Alternative/Error Flows` |

Giới hạn hoặc ngưỡng không có trong nguồn: không tự đặt, chuyển thành Open Question.

## 4. Giá trị enum

- **Loại scenario:** `Happy path | Negative path | Boundary | Permission | Integration | Error handling`
- **Test Result / UAT Result (sheet `RTM`):** mặc định `Not Run` — Agent không ghi giá trị khác
- **Coverage Status (sheet `RTM`):** mặc định `Pending` — Agent không ghi `Covered`
- **Status đầu ra của Agent:** `DRAFT` (cố định)

## 5. Dừng bước khi nào

Dừng và báo lại BA/QA, không tự chế dữ liệu thay thế, khi:

1. AC chưa ở trạng thái đã review.
2. Thiếu `Business Rule ID` cho hành vi mà test bắt buộc phải dựa vào.
3. Dữ liệu hoặc môi trường thử nghiệm cần dùng chưa được cấp quyền.
4. Test cần dữ liệu thật hoặc dữ liệu nhạy cảm chưa được phép xử lý.
5. `Expected Result` không xác định được vì AC mơ hồ.
6. AC thay đổi trong lúc đang thiết kế test.

Khi dừng: nêu rõ test case bị chặn, AC liên quan, lý do và thông tin cần cung cấp.

## 6. Idempotency và audit trail

- Trước khi tạo test case mới, tra theo `Requirement/AC ID` + loại scenario. Nếu đã có test case cho cùng AC và cùng scenario, cập nhật bản nháp hiện có thay vì tạo mới.
- Dòng RTM đề xuất chỉ là nháp; liên kết chính thức do người có thẩm quyền cập nhật theo `skills/ba-03-specification/assets/rtm.md`.
- Mỗi lần chạy ghi lại: prompt version, model/version, AC và Business Rule đầu vào kèm phiên bản, test case tạo thành, người review và quyết định (SOP §8).
