# `_archive` — Bản lưu trữ tài liệu nguồn của bộ skill BA

Thư mục này **không phải một skill**. Kiro chỉ nạp các thư mục con có `SKILL.md` trong `skills/` của power; thư mục này không có file đó nên được bỏ qua khi quét skill (cùng cơ chế với `README.md` ở gốc power).

## Lý do tồn tại

Bộ 13 skill trong `skills/` là **artifact dẫn xuất** từ 4 tài liệu nguồn. Bốn tài liệu đó đã được xoá khỏi thư mục dự án theo quyết định của chủ tài liệu vào 2026-10-30, và đó là **bản duy nhất** — không có git, không có bản sao ở Confluence/SharePoint/Jira.

Thư mục này giữ lại toàn bộ nội dung của chúng, để:
1. 55 chỗ nêu tên file và 50+ trích dẫn `SOP §n` / `Prompt Pack §n` trong bộ skill không thành tham chiếu treo.
2. Còn cơ sở đối chiếu khi quy trình thay đổi (thêm gate, sửa RACI, đổi cột biểu mẫu).
3. Thoả điều rào cản số 1 của chính bộ skill — *Grounding: kết luận quan trọng phải kèm nguồn* — và yêu cầu *Versioning: lưu tài liệu đầu vào* ở SOP §8.

## Nội dung

| File | Nguồn gốc | Cách tạo |
| --- | --- | --- |
| `sop-v1.0.md` | `01_SOP_BA_Agile_AI.docx` v1.0 | Trích xuất bằng python-docx |
| `workbook-v1.0.md` | `02_Bo_Template_BA.xlsx` v1.0 | Trích xuất bằng openpyxl |
| `prompt-pack-v1.0.md` | `03_Prompt_Pack_BA_AI.md` v1.0 | Sao chép nguyên văn |
| `pack-readme-v1.0.md` | `README.md` v1.0 | Sao chép nguyên văn |

Hai file đầu được sinh **bằng script trực tiếp từ file nhị phân**, không gõ lại tay, để tránh sai lệch do chép.

## Kiểm định đã thực hiện trước khi xoá file gốc

| Kiểm tra | `.docx` | `.xlsx` |
| --- | --- | --- |
| Ảnh / media / drawing | 0 | 0 |
| Textbox / OLE object | 0 | — |
| Comment / footnote / endnote | không có | không có |
| Header / footer | không có | — |
| Công thức | — | 0 |
| Data validation | — | 0 |
| Conditional formatting | — | 0 |
| Chart / defined name | — | không có |

Nội dung thực tế: 234 đoạn văn + 3 bảng (110 ô); 9 sheet chỉ chứa giá trị, freeze pane `A2`.

→ **Không có nội dung phi văn bản nào bị mất** khi chuyển sang markdown.

## Thứ KHÔNG được giữ lại

- Định dạng trực quan — font, cỡ chữ, màu, canh lề, số trang (`.docx`); màu ô, font, độ rộng cột, freeze pane (`.xlsx`).
- Khả năng mở bằng Word/Excel và điền trực tiếp như biểu mẫu. Chức năng này do các file `assets/` dạng markdown trong bộ skill đảm nhận.

## Không sửa thư mục này

Đây là bản lưu trữ **đóng băng ở v1.0** và là bằng chứng cho trạng thái nguồn đã dùng để sinh ra bộ skill. Khi quy trình thay đổi: tạo phiên bản mới (`sop-v1.1.md`, `workbook-v1.1.md`…) rồi cập nhật trích dẫn trong các skill — không sửa đè bản v1.0.

---

## Nhật ký xoá tài liệu nguồn (2026-10-30)

Bốn file dưới đây đã được chuyển vào **Recycle Bin** (không xoá vĩnh viễn) sau khi nội dung được trích xuất vào thư mục này và sau khi bộ skill đã được kiểm định tự chủ (131 liên kết nội bộ, 0 hỏng; 0 trích dẫn treo).

Hash SHA-256 ghi lại để có thể xác minh danh tính file nếu cần phục hồi từ Recycle Bin hoặc đối chiếu với một bản sao khác về sau.

| File | Kích thước (byte) | SHA-256 | Sửa lần cuối | Bản lưu |
| --- | --- | --- | --- | --- |
| `01_SOP_BA_Agile_AI.docx` | 43826 | `6aa9018de4094cc6bf0bed6e2dfcfd57e8e4295610df3629bb38a80b3ea8afce` | 2026-10-29 15:27:48 | `sop-v1.0.md` |
| `02_Bo_Template_BA.xlsx` | 14807 | `0ce6986b1c3221139d35a7d992ace57492112ebf565cb0f7d2d212eef6107857` | 2026-10-29 15:27:48 | `workbook-v1.0.md` |
| `03_Prompt_Pack_BA_AI.md` | 4480 | `436cdcc955a289a9c572161573deae87a45edece3871c2a714c308bdfd315f85` | 2026-10-29 15:27:48 | `prompt-pack-v1.0.md` (nguyên văn) |
| `README.md` | 1227 | `29dcfc2fba8405235d19c799322987c36fab3f4dc5d638e5ade47a0fe8ea3646` | 2026-10-29 15:27:48 | `pack-readme-v1.0.md` (nguyên văn) |

Phục hồi: mở Recycle Bin, chuột phải → **Restore**. Các hash trên dùng để xác nhận đúng file đã phục hồi.
