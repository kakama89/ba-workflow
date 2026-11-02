# BA-T02 — Business Analysis Document

Template này khớp sheet `Analysis` của `assets/_archive/workbook-v1.0.md` (19 cột), bổ sung một số trường của BA-T02 trong SOP §6 mà sheet chưa có (đánh dấu ⚠).

## Thông tin tài liệu

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Document ID | `<BA-DOC-000>` | Duy nhất theo dự án |
| Version | `<0.1>` | Tăng theo mỗi lần review có thay đổi nội dung |
| Owner ⚠ | `<tên BA phụ trách>` | Sheet `Analysis` chưa có cột này |
| Business Problem | `<mô tả vấn đề>` | Chỉ phần có bằng chứng |
| Business Objective | `<mục tiêu đo lường được>` | Gắn chỉ số nếu nguồn nêu |
| Success Metrics ⚠ | `<chỉ số + ngưỡng>` | Sheet chưa có; chỉ ghi khi nguồn xác định |
| Scope | `<trong phạm vi>` | |
| Out of Scope ⚠ | `<ngoài phạm vi>` | Sheet gộp vào `Scope`; nên tách riêng |
| Review Status | `<Draft / In Review / Approved>` | `Draft` cho tới khi Business xác nhận |

## Phân tích

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Stakeholders | `<vai trò — mối quan tâm — mức ảnh hưởng>` | Mỗi stakeholder một dòng |
| AS-IS | `<mô tả hiện trạng>` | Kèm bằng chứng; không suy diễn |
| TO-BE | `<mô tả mục tiêu>` | Là đề xuất tới khi Business xác nhận |
| Functional Requirements | `<FR-001 …>` | Mỗi FR một dòng, trỏ về Business Rule nếu có |
| Business Rules | `<BR-001 …>` | **Bắt buộc kèm nguồn** |
| NFR | `<NFR-001 …>` | Chỉ ghi khi có nguồn hoặc ràng buộc kỹ thuật |
| Data/Integration/Permissions | `<API / bảng dữ liệu / quyền>` | Ghi môi trường và quyền truy cập |
| Alternative/Error Flows | `<luồng thay thế, luồng lỗi, ngoại lệ>` | Tối thiểu một luồng lỗi cho mỗi luồng chính |

## Rủi ro và câu hỏi

| Trường | Giá trị | Hướng dẫn điền |
| --- | --- | --- |
| Assumptions | `<[Assumption] …>` | Gắn nhãn rõ; giả định chưa xác nhận không được coi là sự thật |
| Risks | `<rủi ro — tác động — dấu hiệu>` | Không tự đề xuất mức chấp nhận rủi ro |
| Dependencies | `<hệ thống / nhóm sở hữu>` | |
| Open Questions | `<câu hỏi — owner — hạn trả lời>` | **Mỗi câu hỏi phải có owner** (điều kiện G2) |
| Source References | `<URL + vị trí trong tài liệu>` | Ghi tới mục/trang, không chỉ link chung |
| Decision Log ⚠ | `<ngày — quyết định — người quyết định>` | Sheet chưa có; dùng kèm BA-T05 khi có thay đổi |
| Review & Approval ⚠ | `<người xác nhận — ngày>` | Sheet chưa có; Business xác nhận TO-BE tại đây |

## Business Rules Catalog (mẫu)

| Rule ID | Nội dung quy tắc | Nguồn | Trạng thái xác nhận | Nhãn |
| --- | --- | --- | --- | --- |
| BR-001 | `<quy tắc>` | `<URL + vị trí>` | `<Chưa / Đã xác nhận bởi …>` | `[Fact]` |
| BR-002 | `<quy tắc suy ra từ trao đổi>` | `<biên bản ngày …>` | `<Chưa>` | `[Inference]` |

## Không tự điền (chỉ con người có thẩm quyền)
- Xác nhận TO-BE — Business/Business Owner.
- `Review & Approval`, `Review Status = Approved`.
- Ngưỡng NFR, SLA, giới hạn nghiệp vụ chưa có trong nguồn.
- Mức chấp nhận rủi ro.

## Quy tắc điền
- Nhãn bằng chứng: `[Fact]` có nguồn · `[Assumption]` giả định · `[Inference]` suy luận · `[Unknown]` chưa biết.
- Mỗi FR nên trỏ về ít nhất một BR hoặc một nguồn; FR không nguồn là điểm phải hỏi.
- Không xoá `Open Questions` chưa đóng; đánh dấu `Resolved` kèm ngày và người trả lời.
