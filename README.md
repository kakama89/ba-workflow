# Quy trình BA Agile/Scrum có AI Agent

> Bộ công cụ gồm **15 skill** dùng trong Kiro: 7 quy trình chính, 2 tài liệu chính thức, và 6 AI agent hỗ trợ. Mọi đầu ra của AI đều là bản nháp — con người luôn là người duyệt cuối cùng.

---

## Mục lục

- [Cài đặt](#cài-đặt)
- [Cách gọi skill](#cách-gọi-skill)
- [7 Skill quy trình](#7-skill-quy-trình)
  - [ba-01-requirement-intake — Tiếp nhận yêu cầu](#ba-01-requirement-intake--tiếp-nhận-yêu-cầu)
  - [ba-02-business-analysis — Phân tích nghiệp vụ](#ba-02-business-analysis--phân-tích-nghiệp-vụ)
  - [ba-03-specification — Viết đặc tả](#ba-03-specification--viết-đặc-tả)
  - [ba-04-refinement — Làm mịn backlog](#ba-04-refinement--làm-mịn-backlog)
  - [ba-05-change-management — Quản lý thay đổi](#ba-05-change-management--quản-lý-thay-đổi)
  - [ba-06-test-uat — Kiểm thử và nghiệm thu](#ba-06-test-uat--kiểm-thử-và-nghiệm-thu)
  - [ba-07-release-handover — Bàn giao phát hành](#ba-07-release-handover--bàn-giao-phát-hành)
- [2 Skill tài liệu chính thức](#2-skill-tài-liệu-chính-thức)
  - [ba-doc-brd — Tạo BRD](#ba-doc-brd--tạo-brd)
  - [ba-doc-urd — Tạo URD](#ba-doc-urd--tạo-urd)
- [6 Skill AI Agent](#6-skill-ai-agent)
  - [ba-agent-requirement — Trích xuất yêu cầu](#ba-agent-requirement--trích-xuất-yêu-cầu)
  - [ba-agent-analysis — Phân tích nghiệp vụ tự động](#ba-agent-analysis--phân-tích-nghiệp-vụ-tự-động)
  - [ba-agent-specification — Viết User Story và AC](#ba-agent-specification--viết-user-story-và-ac)
  - [ba-agent-qa-review — Rà soát chất lượng](#ba-agent-qa-review--rà-soát-chất-lượng)
  - [ba-agent-test-design — Thiết kế test case](#ba-agent-test-design--thiết-kế-test-case)
  - [ba-agent-traceability — Kiểm tra truy vết](#ba-agent-traceability--kiểm-tra-truy-vết)
- [3 đường đi theo mức độ](#3-đường-đi-theo-mức-độ)
- [Luồng gọi điển hình](#luồng-gọi-điển-hình)
- [Tài nguyên dùng chung](#tài-nguyên-dùng-chung)
- [Quy ước chung](#quy-ước-chung)
- [Cài đặt chi tiết](#cài-đặt-chi-tiết)
- [Ghi chú kỹ thuật](#ghi-chú-kỹ-thuật)

---

## Cài đặt

### Cách nhanh nhất

1. Mở **Kiro IDE** → vào **Powers** → chọn **Install from local**.
2. Trỏ tới thư mục chứa file `plugin.json` này.
3. Xong. Các skill sẽ hiện trong danh sách, gọi bằng `/` + tên skill.

Chi tiết các cách cài khác xem phần [Cài đặt chi tiết](#cài-đặt-chi-tiết) ở cuối tài liệu.

## Cách gọi skill

| Cách gọi | Mô tả |
|---|---|
| **Tự động** | Gõ yêu cầu bằng ngôn ngữ tự nhiên — Kiro tự chọn skill phù hợp dựa vào mô tả của skill |
| **Thủ công** | Gõ `/ba-01-requirement-intake` (thay tên skill tương ứng). Chữ sau tên skill là ngữ cảnh truyền vào |
| **Trong custom agent** | Khai báo skill trong trường `resources` bằng URI `skill://` |

---

## 7 Skill quy trình

Skill quy trình **điều phối con người** — hướng dẫn BA, PO, Dev, QA làm từng bước. Không skill nào tự đóng gate.

---

### ba-01-requirement-intake — Tiếp nhận yêu cầu

**Mục đích:** Tiếp nhận yêu cầu từ business, cấp mã Requirement ID, phân loại, sàng lọc và ghi nhận đầy đủ thông tin ban đầu.

**Khi nào dùng:**
- Có yêu cầu mới từ business, khách hàng, hoặc các bên liên quan.
- Cần phân loại yêu cầu: New Feature, Enhancement, Defect, Technical Change, Compliance, hoặc Unknown.
- Bắt đầu một vòng đời yêu cầu mới.

**Cách dùng:**
```
/ba-01-requirement-intake [mô tả yêu cầu hoặc link tài liệu]
```

**Các bước chính:**
1. Tạo mã Requirement ID, ghi nguồn và người yêu cầu.
2. Phân loại yêu cầu (New Feature / Enhancement / Defect / ...).
3. Kiểm tra tài liệu, phiên bản, phạm vi, phụ thuộc, quyền truy cập.
4. Gọi `ba-agent-requirement` để AI trích xuất thông tin từ tài liệu.
5. BA xác minh bản nháp, PO quyết định bước tiếp theo.

**Đầu vào cần có:** Yêu cầu nghiệp vụ, nguồn tài liệu (có phiên bản), người yêu cầu, chủ sở hữu nghiệp vụ.

**Đầu ra:** Bản ghi tiếp nhận yêu cầu (16 cột), danh sách câu hỏi mở, danh sách nguồn.

**Quality Gate — G1:** Có mã yêu cầu, có mục tiêu, có nguồn + phiên bản, có chủ sở hữu, nội dung AI tách biệt rõ ràng với nội dung đã xác nhận.

**Bước tiếp theo:** → `ba-02-business-analysis`

---

### ba-02-business-analysis — Phân tích nghiệp vụ

**Mục đích:** Điều tra và phân tích nghiệp vụ toàn diện — xác định bên liên quan, mô tả quy trình hiện tại (AS-IS) và kỳ vọng (TO-BE), xây dựng danh mục Business Rules, phân loại yêu cầu chức năng (FR) và phi chức năng (NFR).

**Khi nào dùng:**
- Sau khi yêu cầu đã qua G1 (tiếp nhận xong).
- Cần hiểu rõ nghiệp vụ trước khi viết đặc tả chi tiết.
- Cần xác định rủi ro, phụ thuộc, tác động hệ thống.

**Cách dùng:**
```
/ba-02-business-analysis [tên yêu cầu hoặc mã Requirement ID]
```

**Các bước chính:**
1. Xác định bên liên quan, tác nhân, mục tiêu, phạm vi.
2. Mô tả quy trình AS-IS, điểm đau (pain points), đề xuất TO-BE.
3. Xây dựng danh mục Business Rules (BR-xxx) có mã và nguồn.
4. Phân loại yêu cầu chức năng (FR-xxx) và phi chức năng (NFR-xxx).
5. Đánh giá phụ thuộc, rủi ro, tác động hệ thống.
6. Gọi `ba-agent-analysis` + `ba-agent-qa-review` (bắt buộc), BA xác minh với Business.

**Đầu vào cần có:** Bản ghi tiếp nhận đã qua G1, tài liệu nghiệp vụ, dữ liệu mẫu, thông tin hệ thống liên quan.

**Đầu ra:** Tài liệu phân tích nghiệp vụ (19 cột), bản đồ bên liên quan, sơ đồ quy trình, danh mục Business Rules, FR/NFR, rủi ro và câu hỏi mở.

**Quality Gate — G2:** Mọi Business Rule có nguồn, giả định được đánh dấu rõ, Business đã xác nhận TO-BE, mỗi câu hỏi mở có người chịu trách nhiệm.

**Bước tiếp theo:** → `ba-03-specification` (và có thể song song `ba-doc-brd`, `ba-doc-urd`)

---

### ba-03-specification — Viết đặc tả

**Mục đích:** Phân rã yêu cầu thành Epic / Feature / User Story, viết Acceptance Criteria (AC) theo Given-When-Then có thể kiểm thử được, tạo liên kết truy vết (RTM).

**Khi nào dùng:**
- Sau khi phân tích nghiệp vụ đã qua G2.
- Cần chuyển yêu cầu nghiệp vụ thành đặc tả kỹ thuật mà Dev và QA hiểu được.
- Cần tạo RTM (Requirement Traceability Matrix) để theo dõi yêu cầu.

**Cách dùng:**
```
/ba-03-specification [tên feature hoặc mã Requirement ID]
```

**Các bước chính:**
1. Phân rã Epic → Feature → User Story.
2. Viết User Story (As a / I want / So that) và AC (Given / When / Then, mỗi AC có mã AC ID).
3. Chi tiết hành vi: validation, dữ liệu, trạng thái, phân quyền, thông báo, lỗi, NFR.
4. Tạo liên kết truy vết + dòng RTM đầu tiên.
5. Gọi `ba-agent-specification` + `ba-agent-qa-review`, BA rà soát.
6. Dev/Tech Lead xem tính khả thi, QA xem tính kiểm thử được, PO/Business xác nhận.

**Đầu vào cần có:** Tài liệu phân tích đã qua G2, danh mục Business Rules, sơ đồ quy trình, Product Goal.

**Đầu ra:** User Story + AC (18 cột), RTM (10 cột, dùng chung), cập nhật BRD/URD nếu có.

**Quality Gate — G3:** AC kiểm thử được, không có giả định ẩn, đã được người có thẩm quyền xác nhận, tài liệu có phiên bản, 0 câu hỏi mở mức Critical/Major.

**Bước tiếp theo:** → `ba-04-refinement`

---

### ba-04-refinement — Làm mịn backlog

**Mục đích:** Chuẩn bị backlog cho Sprint — BA chuẩn bị nội dung, PO làm rõ giá trị và thứ tự, Dev đánh giá tính khả thi, QA đánh giá tính kiểm thử, team ước lượng và chia story.

**Khi nào dùng:**
- Trước mỗi Sprint, khi cần đưa story vào Sprint Backlog.
- Cần kiểm tra story đã đủ điều kiện vào Sprint chưa (Definition of Ready — DoR).
- Team cần thống nhất ước lượng và chia story lớn.

**Cách dùng:**
```
/ba-04-refinement [tên story hoặc danh sách story cần refinement]
```

**Các bước chính:**
1. BA chuẩn bị nội dung và câu hỏi mở.
2. PO làm rõ giá trị và thứ tự ưu tiên.
3. Dev/Tech Lead + QA đánh giá tính khả thi và kiểm thử.
4. Team chia story và ước lượng.
5. Gọi `ba-agent-qa-review` kiểm tra DoR + `ba-agent-traceability` nếu story bị chia.

**Đầu vào cần có:** Product Backlog đã qua G3, Story/AC, phụ thuộc, Product Goal, năng lực team.

**Đầu ra:** Backlog đã làm rõ, ước lượng đã thống nhất, checklist DoR.

**Quality Gate — DoR:** Story đạt DoR khi Team + PO đồng ý đủ điều kiện → chuyển sang `Ready for Sprint`.

**Bước tiếp theo:** → Sprint → `ba-06-test-uat`

---

### ba-05-change-management — Quản lý thay đổi

**Mục đích:** Kiểm soát thay đổi trong quá trình phát triển — trả lời câu hỏi từ nguồn xác nhận, ghi nhận quyết định, tạo Change Request (CR) với phân tích tác động, giữ RTM nhất quán.

**Khi nào dùng:**
- Dev hoặc QA hỏi về yêu cầu trong Sprint.
- Business yêu cầu thay đổi scope, logic, hoặc quy tắc nghiệp vụ.
- Phát hiện yêu cầu mâu thuẫn hoặc thiếu sót cần sửa.
- Cần ghi nhận bất kỳ quyết định nào ảnh hưởng đến yêu cầu.

> **Lưu ý:** Skill này là **theo sự kiện**, không phải giai đoạn cố định. Có thể gọi bất cứ lúc nào từ BA-03 trở đi.

**Cách dùng:**
```
/ba-05-change-management [mô tả thay đổi hoặc câu hỏi cần xử lý]
```

**Các bước chính:**
1. Trả lời câu hỏi + ghi nhận quyết định.
2. Tạo CR (CR-xxx), ghi hiện trạng và đề xuất thay đổi.
3. Phân tích tác động qua `ba-agent-traceability` (Story, AC, BR, API, dữ liệu, test case, tài liệu, Sprint, RTM).
4. PO quyết định, BA ghi nhận người duyệt và phiên bản có hiệu lực.
5. BA cập nhật tài liệu, gọi `ba-agent-traceability` + `ba-agent-qa-review` (tùy chọn).
6. **Quay lại đúng điểm kiểm soát** — bảng trong skill chỉ rõ loại thay đổi nào quay về skill/bước nào.

**Đầu vào cần có:** Sprint Backlog, Story/AC đã xác nhận, câu hỏi hoặc yêu cầu thay đổi, RTM hiện tại.

**Đầu ra:** Nhật ký quyết định, Change Request (13 cột), phân tích tác động, tài liệu đã cập nhật.

**Quality Gate — Gate thay đổi:** Có người quyết định, có lý do, có phiên bản hiệu lực, đã thông báo bên bị ảnh hưởng, truy vết đã cập nhật.

---

### ba-06-test-uat — Kiểm thử và nghiệm thu

**Mục đích:** Rà soát liên kết yêu cầu–AC–test case, hỗ trợ chạy test, phân loại sai lệch (defect / thiếu yêu cầu / thay đổi), chuẩn bị UAT, cập nhật RTM với bằng chứng, hỗ trợ quyết định nghiệm thu.

**Khi nào dùng:**
- Sprint kết thúc, cần kiểm thử và nghiệm thu (UAT).
- Cần kiểm tra chuỗi truy vết Requirement → Story → AC → Test Case → Kết quả.
- Business cần chạy UAT và ra quyết định chấp nhận.

**Cách dùng:**
```
/ba-06-test-uat [tên feature hoặc Sprint cần kiểm thử]
```

**Các bước chính:**
1. BA + QA rà soát chuỗi truy vết qua `ba-agent-traceability`.
2. QA chạy test, BA hỗ trợ giải thích quy tắc nghiệp vụ.
3. Phân loại sai lệch: defect, thiếu yêu cầu, hay cần Change Request.
4. Chuẩn bị kịch bản UAT (UAT-xxx) từ AC đã duyệt, gọi `ba-agent-qa-review` (bắt buộc).
5. Business Users chạy UAT.
6. Tổng hợp kết quả, cập nhật RTM, gọi `ba-agent-traceability` + `ba-agent-test-design` (tùy chọn).
7. Quyết định nghiệm thu: Accept / Reject / Conditional Acceptance / Pending.

**Đầu vào cần có:** Story/AC đã xác nhận, Business Rules, bản build (có phiên bản), Test Plan/Cases, môi trường test.

**Đầu ra:** Báo cáo rà soát test, RTM đã cập nhật, báo cáo UAT (17 cột), danh sách defect, quyết định nghiệm thu.

**Quality Gate — G4:** Kết quả có bằng chứng, defect nghiêm trọng đã xử lý hoặc chấp nhận rủi ro, có người duyệt + ngày, coverage ≥ ngưỡng, pass rate ≥ ngưỡng, 0 defect Critical/Major còn mở.

**Bước tiếp theo:** → `ba-07-release-handover`

---

### ba-07-release-handover — Bàn giao phát hành

**Mục đích:** Đối chiếu phạm vi phát hành với kết quả thực tế, cập nhật tài liệu hướng ra ngoài (release notes, user guide, FAQ), ghi nhận vấn đề còn mở, rút bài học kinh nghiệm, lưu trữ tài liệu.

**Khi nào dùng:**
- Sau khi đạt G4, chuẩn bị phát hành.
- Cần bàn giao cho vận hành, hỗ trợ, hoặc khách hàng.
- Cần lưu trữ tài liệu và rút kinh nghiệm.

**Cách dùng:**
```
/ba-07-release-handover [tên release hoặc Sprint]
```

**Các bước chính:**
1. Đối chiếu phạm vi phát hành qua `ba-agent-traceability`.
2. Cập nhật release notes, user guide, FAQ (tùy chọn gọi `ba-agent-qa-review`).
3. Ghi nhận vấn đề còn mở với người chịu trách nhiệm + hạn.
4. AI soạn bản nháp bài học kinh nghiệm + FAQ (Status = DRAFT).
5. Lưu trữ vào Knowledge Base, tham gia Retrospective, tổng hợp KPI.

**Đầu vào cần có:** Kết quả UAT đã qua G4, Release Notes, Known Issues, tài liệu yêu cầu, RTM.

**Đầu ra:** Gói bàn giao (handover checklist), Release Notes, Known Issues, RTM cuối, Action Items, KPI.

**Quality Gate — Gate bàn giao:** Đúng phiên bản, có người nhận, tài liệu AI đã được rà soát, vấn đề mở có người chịu trách nhiệm.

**Kết thúc vòng đời.** Yêu cầu mới → quay lại `ba-01`.

---

## 2 Skill tài liệu chính thức

Hai skill này tạo tài liệu nghiệp vụ chính thức, chạy sau khi phân tích qua G2. Có thể chạy song song với nhau hoặc song song với `ba-03`.

---

### ba-doc-brd — Tạo BRD

**Mục đích:** Tạo tài liệu **Business Requirements Document (BRD)** — mô tả yêu cầu nghiệp vụ từ góc nhìn tổ chức: mục tiêu kinh doanh, phạm vi, bên liên quan, AS-IS/TO-BE, FR/NFR, quy tắc nghiệp vụ, ràng buộc, rủi ro, chỉ số thành công.

**Khi nào dùng:**
- Dự án cần tài liệu yêu cầu nghiệp vụ chính thức cho phê duyệt, đấu thầu, hoặc ký hợp đồng.
- Track **Heavy** bắt buộc có BRD.
- Cần tài liệu tổng quan cho Ban lãnh đạo hoặc Sponsor.

**Cách dùng:**
```
/ba-doc-brd [tên dự án hoặc mã Requirement ID]
```

**Các bước chính:**
1. Xác minh đầu vào và phạm vi.
2. Tổng hợp bối cảnh, vấn đề, mục tiêu, chỉ số thành công, phạm vi, giả định, ràng buộc.
3. Tổng hợp bên liên quan + quy trình.
4. Tổng hợp yêu cầu (FR, NFR, BR, dữ liệu, tích hợp, phân quyền).
5. Tổng hợp rủi ro, phụ thuộc, timeline.
6. Gọi `ba-agent-qa-review` (tùy chọn) + BA và Business Owner rà soát.

**Đầu vào cần có:** Tài liệu phân tích đã qua G2, danh mục Business Rules, bản đồ bên liên quan, sơ đồ quy trình, FR, NFR.

**Đầu ra:** BRD theo template chuẩn, liên kết truy vết BRD↔FR↔BR↔REQ trong RTM.

**Quality Gate — Gate BRD:** Mọi FR/NFR có nguồn + liên kết Requirement ID, BR có nguồn, giả định đánh dấu, phạm vi có Business Owner xác nhận.

---

### ba-doc-urd — Tạo URD

**Mục đích:** Tạo tài liệu **User Requirements Document (URD)** — mô tả yêu cầu từ góc nhìn người dùng: hồ sơ người dùng, mục tiêu, use case, kịch bản sử dụng, yêu cầu UI/UX, tiêu chí khả dụng, tiêu chí nghiệm thu, yêu cầu trợ năng (accessibility).

**Khi nào dùng:**
- Dự án cần tài liệu yêu cầu từ góc nhìn người dùng cuối.
- Track **Heavy** bắt buộc có URD.
- Cần cơ sở cho UAT scenarios ở `ba-06-test-uat`.
- Cần tài liệu cho thiết kế UI/UX.

**Cách dùng:**
```
/ba-doc-urd [tên dự án hoặc mã Requirement ID]
```

**Các bước chính:**
1. Xác minh đầu vào và phạm vi.
2. Xây dựng hồ sơ người dùng (vai trò, đặc điểm, ngữ cảnh, tần suất, mục tiêu).
3. Xác định mục tiêu người dùng + use case (tác nhân, tiền điều kiện, luồng chính, luồng thay thế, hậu điều kiện).
4. Viết kịch bản người dùng (ngữ cảnh, hành động, phản hồi hệ thống, kết quả mong đợi).
5. Yêu cầu UI/UX, khả dụng, trợ năng.
6. Tiêu chí nghiệm thu cho từng use case.
7. Gọi `ba-agent-qa-review` (tùy chọn) + BA và đại diện người dùng rà soát.

**Đầu vào cần có:** Tài liệu phân tích đã qua G2, bản đồ bên liên quan, sơ đồ quy trình, FR, thông tin người dùng.

**Đầu ra:** URD theo template chuẩn, liên kết truy vết URD↔Use Case↔FR↔REQ trong RTM.

**Quality Gate — Gate URD:** Mọi hồ sơ người dùng có nguồn, use case có luồng lỗi/ngoại lệ, tiêu chí nghiệm thu kiểm thử được, đại diện người dùng đã rà soát.

---

## 6 Skill AI Agent

Skill AI Agent **chỉ tạo bản nháp** (Status = DRAFT). Mọi đầu ra phải được con người rà soát trước khi sử dụng chính thức. Không agent nào tự duyệt, tự đóng gate, hay tự sửa tài liệu gốc.

Đầu ra agent luôn theo **6 phần chuẩn:** Summary → Facts with sources → Findings/Open Questions → Suggested actions → Confidence limitations → Status = DRAFT.

---

### ba-agent-requirement — Trích xuất yêu cầu

**Mục đích:** AI đọc tài liệu yêu cầu nghiệp vụ và trích xuất thông tin thành bản nháp Intake Record — mục tiêu, vấn đề, phạm vi, bên liên quan, phân loại, thông tin thiếu, câu hỏi cần làm rõ, phụ thuộc, rủi ro, trùng lặp.

**Khi nào dùng:**
- Được `ba-01-requirement-intake` gọi tự động ở Bước 4.
- Khi có tài liệu yêu cầu cần trích xuất nhanh.

**Cách dùng:** Thường không gọi trực tiếp — `ba-01` sẽ gọi tự động. Nếu cần gọi riêng:
```
/ba-agent-requirement [nội dung hoặc link tài liệu yêu cầu]
```

**Đầu vào:** Yêu cầu nghiệp vụ, tài liệu tham khảo (URD/BRD/Confluence nếu có), danh sách yêu cầu hiện có.

**Đầu ra:** Bản nháp Intake Record (16 cột + Request Type), đánh dấu rõ nội dung AI suy luận vs. nội dung có nguồn.

**Giới hạn:** Không tự duyệt, không suy luận Business Rules/Priority/SLA, không tạo trùng Intake Record.

---

### ba-agent-analysis — Phân tích nghiệp vụ tự động

**Mục đích:** AI xây dựng bản nháp phân tích nghiệp vụ đầy đủ — bên liên quan, tác nhân, mục tiêu, phạm vi, AS-IS/TO-BE, danh mục Business Rules có mã, FR, NFR, luồng thay thế/lỗi, dữ liệu, tích hợp, phụ thuộc, rủi ro.

**Khi nào dùng:**
- Được `ba-02-business-analysis` gọi tự động ở Bước 6.
- Khi cần AI hỗ trợ xây dựng tài liệu phân tích từ nhiều nguồn.

**Cách dùng:** Thường không gọi trực tiếp — `ba-02` sẽ gọi tự động. Nếu cần gọi riêng:
```
/ba-agent-analysis [mã Requirement ID hoặc link tài liệu]
```

**Đầu vào:** Intake Record đã qua G1, tài liệu nghiệp vụ (có phiên bản), danh mục Business Rules hiện có, thông tin hệ thống/tích hợp.

**Đầu ra:** Bản nháp phân tích nghiệp vụ (19 cột), theo 6 phần chuẩn.

**Giới hạn:** Không tự tạo chính sách/SLA, không gán mã BR nếu không có nguồn, không quyết định phạm vi, không thăng cấp giả định thành sự thật.

---

### ba-agent-specification — Viết User Story và AC

**Mục đích:** AI viết bản nháp User Story và Acceptance Criteria (Given-When-Then) từ yêu cầu đã rà soát — liên kết với Requirement ID và Business Rule ID, bao gồm luồng chính, ngoại lệ, validation, edge case có bằng chứng.

**Khi nào dùng:**
- Được `ba-03-specification` gọi tự động ở Bước 5.
- Khi cần AI hỗ trợ viết story/AC từ tài liệu phân tích.

**Cách dùng:** Thường không gọi trực tiếp — `ba-03` sẽ gọi tự động. Nếu cần gọi riêng:
```
/ba-agent-specification [mã Requirement ID hoặc tên feature]
```

**Đầu vào:** Tài liệu phân tích/yêu cầu đã rà soát + Requirement ID, danh mục Business Rules + BR ID, NFR, quy ước Story/AC của team.

**Đầu ra:** Bản nháp User Story + AC (18 cột), bao gồm tự rà soát về clarity/consistency/testability/duplication.

**Giới hạn:** Không tạo yêu cầu mới để lấp khoảng trống, không quyết định Priority/Story Point, không duyệt DoR, không viết AC cho hành vi chưa có nguồn.

---

### ba-agent-qa-review — Rà soát chất lượng

**Mục đích:** AI rà soát tài liệu yêu cầu theo 8 tiêu chí: Đầy đủ, Rõ ràng, Nhất quán, Kiểm thử được, Truy vết, Trường hợp phủ định, NFR, Tác động thay đổi. Báo cáo finding có bằng chứng.

**Khi nào dùng:**
- **Bắt buộc** ở: BA-02 (Bước 6), BA-03 (Bước 5), BA-04 (Bước 5), BA-06 (Bước 4).
- **Tùy chọn** ở: BA-01 (Bước 5), BA-05 (Bước 5), BA-07 (Bước 2), ba-doc-brd, ba-doc-urd.
- Bất cứ khi nào cần AI rà soát chất lượng tài liệu yêu cầu.

**Cách dùng:** Thường được skill quy trình gọi tự động. Nếu cần gọi riêng:
```
/ba-agent-qa-review [link hoặc nội dung tài liệu cần rà soát]
```

**Đầu vào:** Tài liệu cần rà soát (URD/BRD, phân tích, Story/AC, RTM, hoặc CR) có phiên bản + nguồn so sánh.

**Đầu ra:** Bảng finding (7 cột: Finding ID, Category, Severity, Evidence, Requirement Reference, Suggested Action, Owner). Severity: Critical / Major / Minor / Info. Đề xuất dòng ghi vào `ai-review-log.md` (15 cột).

**Giới hạn:** Không sửa tài liệu gốc, không tự duyệt, không tạo finding không có bằng chứng, không hạ mức severity, không đánh dấu Resolved/Accepted Risk.

---

### ba-agent-test-design — Thiết kế test case

**Mục đích:** AI đề xuất kịch bản và test case cho happy path, negative path, boundary, phân quyền, tích hợp, xử lý lỗi — mỗi case liên kết với AC ID hoặc Requirement ID, kèm tiền điều kiện, bước thực hiện, dữ liệu test, kết quả mong đợi.

**Khi nào dùng:**
- Được `ba-06-test-uat` gọi tự động ở Bước 1 và 6.
- Khi cần AI gợi ý test case từ AC đã duyệt.
- Khi cần bổ sung coverage cho test plan.

**Cách dùng:** Thường không gọi trực tiếp — `ba-06` sẽ gọi tự động. Nếu cần gọi riêng:
```
/ba-agent-test-design [mã Story ID hoặc danh sách AC cần thiết kế test]
```

**Đầu vào:** AC đã rà soát + AC ID + Story ID, danh mục Business Rules, dữ liệu/môi trường test cho phép, Requirement IDs.

**Đầu ra:** Test Case (10 cột: Test Case ID, Story ID, Requirement/AC ID, Scenario Type, Preconditions, Steps, Test Data, Expected Result, Priority, Open Questions). Dòng RTM nháp với Test Result = Not Run, UAT Result = Not Run.

**Giới hạn:** Không khẳng định test đã chạy/đạt/lỗi, không điền Test Result/UAT Result, không dùng dữ liệu thật/nhạy cảm, không thiết kế test cho AC chưa rà soát.

---

### ba-agent-traceability — Kiểm tra truy vết

**Mục đích:** AI đối chiếu chuỗi Requirement → Story → AC → Test Case → Kết quả test/UAT. Báo cáo coverage, liên kết thiếu, bản ghi mồ côi, nghi ngờ bị ảnh hưởng bởi thay đổi, lệch phiên bản — tất cả có bằng chứng.

**Khi nào dùng:**
- Được gọi tự động từ nhiều skill: BA-04 (Bước 5), BA-05 (Bước 3, 5), BA-06 (Bước 1, 6), BA-07 (Bước 1).
- Khi cần kiểm tra RTM có đầy đủ và nhất quán không.
- Khi story bị chia, thay đổi xảy ra, hoặc chuẩn bị phát hành.

**Cách dùng:** Thường được skill quy trình gọi tự động. Nếu cần gọi riêng:
```
/ba-agent-traceability [link RTM hoặc mô tả phạm vi cần kiểm tra]
```

**Đầu vào:** RTM hiện tại (có phiên bản), tài liệu phân tích + Requirement IDs, Story/AC, Test Cases + kết quả (nếu có), Change Log.

**Đầu ra:** Coverage Summary, Missing Links, Suspected Impact, Source Evidence, Suggested Owner/Action. Liên kết suy luận đánh dấu `Inferred` (không bao giờ `Confirmed`).

**Giới hạn:** Không coi liên kết suy luận là xác nhận, không cập nhật RTM/Story/Change Log chính thức, không điền Test Result/UAT Result, không duyệt thay đổi phạm vi, không xóa bản ghi mồ côi, không khẳng định sẵn sàng phát hành nếu chưa xác minh.

---

## 3 đường đi theo mức độ

PO chọn đường đi (track) tại Bước 5 của BA-01 dựa vào loại yêu cầu.

| Track | Áp dụng cho | Quy trình | Gate |
|---|---|---|---|
| **Express** | Defect lệch AC đã duyệt; Technical Change không đổi hành vi | BA-01 → BA-06 (chỉ retest) | G1, G4 |
| **Standard** | New Feature, Enhancement, Compliance; Technical Change có đổi hành vi | BA-01 → BA-07 đầy đủ | G1–G4 + Gate thay đổi + Gate bàn giao |
| **Heavy** | Feature lớn, compliance phức tạp, hợp đồng/đấu thầu | Standard + BRD/URD bắt buộc | Tất cả + Gate BRD + Gate URD |

> `Defect` chưa có AC và `Unknown` không được vào Express.

---

## Luồng gọi điển hình

```
Yêu cầu mới
  → /ba-01-requirement-intake       → G1
  → /ba-02-business-analysis        → G2
  → /ba-doc-brd  (tùy chọn/Heavy)   → Gate BRD
  → /ba-doc-urd  (tùy chọn/Heavy)   → Gate URD
  → /ba-03-specification            → G3 + tạo RTM
  → /ba-04-refinement               → DoR
  → Sprint
  → /ba-06-test-uat                 → G4
  → /ba-07-release-handover         → Gate bàn giao

Theo sự kiện (từ BA-03 trở đi):
  → /ba-05-change-management        → Gate thay đổi
    → quay lại BA-02, BA-03, BA-04 hoặc BA-06 tùy loại thay đổi
```

Nguyên tắc: **Skill quy trình điều phối con người, skill agent chỉ tạo bản nháp.** Không skill nào tự đóng gate.

---

## Tài nguyên dùng chung

| File | Được dùng bởi | Mô tả |
|---|---|---|
| `skills/ba-03-specification/assets/rtm.md` | ba-03, ba-06, ba-07, ba-agent-test-design, ba-agent-traceability | Template RTM (10 cột) — nơi tạo dòng truy vết đầu tiên |
| `skills/ba-05-change-management/assets/decision-log-cr.md` | ba-04, ba-05, ba-06 | Template nhật ký quyết định và Change Request |
| `assets/ai-run-log.md` | Cả 6 agent, BA-07 | Template ghi nhận lịch sử chạy AI |

> Các file trên là **template chỉ đọc**. Bản ghi thật lưu tại `ba-records/<project>/` trong repo dự án.

---

## Quy ước chung

- **Mô tả song ngữ:** Tiếng Anh trước (có `Use when …`), rồi `Tiếng Việt:` — để Kiro khớp cả hai ngôn ngữ.
- **Nội dung tiếng Việt**, giữ nguyên thuật ngữ tiếng Anh như SOP.
- **10 rào cản bắt buộc** nằm tại `POWER.md` — tất cả 15 skill đều tuân theo.
- **Đầu ra agent** theo 6 phần chuẩn: Summary → Facts with sources → Findings/Open Questions → Suggested actions → Confidence limitations → Status = DRAFT.
- **Cột biểu mẫu** khớp tên cột trong `assets/_archive/workbook-v1.0.md`. Trường thêm đánh dấu ⚠.
- **Kiểm tra sau khi sửa:** `python scripts/validate_power.py`.

---

## Cài đặt chi tiết

### Cách 1 — Cài từ thư mục local

1. Mở **Kiro IDE** → vào phần **Powers**.
2. Chọn **Install from local**.
3. Trỏ tới thư mục chứa `plugin.json` và `POWER.md`.
4. Kiro sẽ sao power vào `~/.kiro/powers/installed/ba-agile-ai/`.
5. Các skill xuất hiện trong danh sách — gọi bằng `/` + tên skill.

### Cách 2 — Cài từ git repo

1. Push thư mục lên git remote (GitHub, GitLab, CodeCommit, …).
2. Mở **Kiro IDE** → **Powers** → **Add Power** → **Repository**.
3. Dán URL repo → Kiro clone và cài tự động.

### Cách 3 — Kiro CLI

```bash
# Từ thư mục local
kiro power install --source local --path /đường/dẫn/tới/Bo_Quy_Trinh_BA_Agile_AI

# Từ git repo
kiro power install --source repo --url https://github.com/<user>/Bo_Quy_Trinh_BA_Agile_AI
```

### Sau khi cài

| Cách gọi | Chi tiết |
|---|---|
| Tự động | Kiro khớp yêu cầu với `description` của skill, tự chọn skill phù hợp |
| Thủ công | Gõ `/` + tên skill. Chữ sau tên skill là ngữ cảnh |
| Custom agent | Khai báo trong trường `resources` bằng URI `skill://` |

---

## Ghi chú kỹ thuật

### Trạng thái tài liệu nguồn

Bốn tài liệu gốc (`01_SOP_BA_Agile_AI.docx`, `02_Bo_Template_BA.xlsx`, `03_Prompt_Pack_BA_AI.md`, `README.md`) đã bị xóa khỏi thư mục dự án vào 2026-10-30. Nội dung chữ được lưu tại `assets/_archive/`, trích xuất bằng script từ file nhị phân. Bộ skill **tự chủ về nội dung** — toàn bộ quy trình, gate, template đều nằm trong `skills/`.

Chi tiết: `assets/_archive/README.md`.

### Khác biệt giữa SOP và workbook

| Template | Mục SOP có nhưng sheet thiếu | Xử lý |
|---|---|---|
| BA-T02 / Analysis | `owner`, `Success Metrics`, `Out of Scope`, `Decision Log`, `Review & Approval` | Thêm vào assets, đánh dấu ⚠ |
| BA-T06 / UAT Report | Cột gộp `Scope & Acceptance Criteria`, ô tổng, `Open Risks`, `Approver/Date` | Tách thành phần riêng trong assets |

### Mở rộng so với SOP/workbook v1.0

Các phần mở rộng (đánh dấu ⚠ tại chỗ dùng): Request Type trong Intake, đường đi theo Request Type, Version/Confirmed By trong Story, Ready for Sprint, DoR tiêu chí 7-8, Bước 6 của BA-05, G4 tiêu chí 3, ai-run-log.md.

### Việc cần làm trước khi áp dụng

1. Review và điều chỉnh quy trình theo chính sách tổ chức.
2. Thay ví dụ minh họa bằng dữ liệu dự án thực tế.
3. Chốt nguồn tài liệu chính thức và quy tắc versioning.
4. Thử nghiệm 2–4 Sprint, đo baseline trước khi đặt KPI.
5. Chỉ tích hợp AI Agent với Jira/Confluence sau khi được phê duyệt bảo mật.
6. Không dùng đầu ra AI chưa review làm yêu cầu chính thức.

### Dạng phân phối

Đây là một **Kiro Power** tự chứa: manifest ở `plugin.json`, hướng dẫn power ở `POWER.md`, 15 skill ở `skills/`, tài liệu lưu trữ ở `assets/_archive/`, icon ở `assets/icon.png`.
