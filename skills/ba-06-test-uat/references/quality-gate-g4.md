# Quality Gate G4 — Kiểm thử, UAT và nghiệm thu nghiệp vụ

Gate này đóng lại BA-06. Không đạt G4 thì không chuyển sang BA-07.

## Checklist bắt buộc

| # | Tiêu chí | Bằng chứng cần có | Đạt / Không |
| --- | --- | --- | --- |
| 1 | Kết quả có bằng chứng | Mỗi dòng `Pass`/`Fail` có `Evidence Link` mở được | |
| 2 | Defect nghiêm trọng được xử lý | Đã sửa và retest, **hoặc** có chấp nhận rủi ro đúng thẩm quyền kèm tên + ngày | |
| 3 ⚠ | Có quyết định nghiệm thu cho phép đi tiếp | `Decision` là `Accept` hoặc `Conditional Acceptance`, có `Approver` và `Approval Date`; `Conditional Acceptance` có `Conditions` kèm owner và hạn | |
| 4 ⚠ | RTM coverage ≥ ngưỡng dự án | Tỷ lệ dòng RTM có `Coverage Status = Covered` so với tổng dòng ≥ ngưỡng do PO chốt (mặc định 100 % cho Standard/Heavy, 100 % phần liên quan cho Express); dòng `Not Applicable` được loại khỏi mẫu số; `Skipped` phải có lý do và người duyệt | |
| 5 ⚠ | Pass Rate ≥ ngưỡng dự án | `Passed / (Passed + Failed + Blocked)` ≥ ngưỡng do PO chốt (mặc định 100 %); `Not Run` không được đếm vào Passed; `Skipped` phải có lý do | |
| 6 ⚠ | Defect Critical/Major còn mở = 0 | Mọi defect `Critical` và `Major` đã đóng hoặc có chấp nhận rủi ro đúng thẩm quyền | |

## Tiêu chí bổ sung nên kiểm tra
- [ ] Mọi AC cần kiểm thử đều có `Test Case ID` trong RTM; không còn `Missing Link`.
- [ ] Không có dòng RTM ở trạng thái `Orphan` chưa được giải thích.
- [ ] `Release/Build` trong UAT Report khớp build thực sự được test.
- [ ] Mỗi `Scenario ID` trỏ về một `Story ID` + `AC ID`.
- [ ] `Blocked` có lý do và tên dependency đang chặn.
- [ ] `Not Run` và `Skipped` không bị đếm vào `Passed`; `Skipped` có lý do và người duyệt.
- [ ] Mọi sai khác đã được phân loại: Defect / Requirement gap / Change request.
- [ ] Requirement gap đã mở CR, không bị bỏ qua.
- [ ] RTM đã cập nhật `Test Result`, `UAT Result`, `Evidence Link`, `Coverage Status`.
- [ ] Dữ liệu dùng cho UAT là dữ liệu được phép, không có thông tin nhạy cảm trong môi trường chưa phê duyệt.
- [ ] `Open Risks` có người theo dõi.

## Quy tắc phân loại sai khác
| Loại | Dấu hiệu | Chuyển tới | Ai quyết định |
| --- | --- | --- | --- |
| Defect | Hành vi khác AC đã duyệt | QA/Dev | QA về severity, PO về thứ tự sửa |
| Requirement gap | AC/Business Rule chưa mô tả hành vi này | `ba-05-change-management`, rồi quay lại theo Bước 6 của BA-05 | Business Owner về nội dung quy tắc |
| Change request | Nghiệp vụ muốn hành vi khác AC đã duyệt | `ba-05-change-management` | PO (A*) / cấp cao hơn nếu vượt thẩm quyền |

Chưa phân loại được: ghi `[Unknown]`, hỏi Business Owner. Không tự xếp loại để đóng gate.

## Quy tắc về bằng chứng
Bằng chứng hợp lệ: kết quả test run có log, ảnh chụp màn hình kèm ngày và build, biên bản UAT có chữ ký hoặc xác nhận điện tử, link hệ thống mở được.

Không hợp lệ:
1. Ghi `Pass` vì "code đã xong" hoặc "dev nói ổn".
2. `Evidence Link` trỏ tới trang rỗng, trang cần quyền mà người review không có.
3. Bằng chứng từ build khác với `Release/Build` trong báo cáo.
4. AI tổng hợp kết quả mà không có dữ liệu thực thi đầu vào.

## Quy tắc dừng bước
Dừng và báo thay vì tiếp tục khi:
1. Thiếu tiêu chí nghiệm thu và không ai cung cấp được.
2. Build test không ổn định tới mức không chạy hết scenario — ghi `Blocked`, không suy đoán kết quả.
3. Defect `Critical` còn mở mà bị yêu cầu nghiệm thu — cần quyết định chấp nhận rủi ro đúng thẩm quyền.
4. Không truy cập được môi trường hoặc dữ liệu UAT được phép.
5. Kết quả do AI đề xuất không có dữ liệu thực thi làm đầu vào.
6. AC và Business Rule mâu thuẫn nhau khiến `Expected Result` không xác định được.

Khi dừng: giữ `Status = Not Run`/`Blocked`, `Decision = Pending`, ghi lý do, báo BA/QA/PO.

## Lỗi thường gặp ở G4
| Lỗi | Vì sao nguy hiểm | Cách xử lý |
| --- | --- | --- |
| Đếm `Not Run` là Pass | Nghiệm thu khống | Tách riêng bốn trạng thái |
| Đóng defect không retest | Lỗi quay lại ở production | Bắt buộc retest kèm bằng chứng |
| Xếp requirement gap thành defect | Sửa code sai, quy tắc vẫn thiếu | Phân loại lại, mở CR |
| Chạy UAT trên build khác build phát hành | Bằng chứng vô hiệu | Khoá `Release/Build` trước khi chạy |
| Để AI tự suy ra `Expected Result` | Lệch AC đã duyệt | Lấy `Expected Result` thẳng từ `Then` của AC |
| Chấp nhận rủi ro không ghi tên người | Không ai chịu trách nhiệm | Ghi `Approver` + ngày |

## Người ký G4
QA thực hiện và chịu trách nhiệm kết quả kiểm thử (A/R cho thiết kế Test Case); Business/Business Owner quyết định nghiệm thu (A/R cho UAT); BA hỗ trợ bằng chứng và truy vết (C); PO tham vấn (C).
