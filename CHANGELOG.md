# Changelog

Mọi thay đổi đáng chú ý của power BA Agile/Scrum AI được ghi tại đây.
Quy ước: breaking change → major; thêm bước/agent/gate → minor; sửa typo/diễn đạt → patch.

## [1.1.0] — 2025-07-15

### Thêm mới
- **Process Tracks (Đường đi theo mức độ)** — ba track chính thức: Express, Standard, Heavy. PO chọn track tại BA-01 Bước 5, ghi vào `BA/PO Decision`. Express áp dụng cho Defect lệch AC và Technical Change không đổi hành vi (BA-01 → BA-06); Standard đi đầy đủ BA-01 → BA-07; Heavy thêm BRD/URD bắt buộc. `POWER.md`, `README.md`, `ba-01-requirement-intake/SKILL.md`.
- **Tiêu chí định lượng cho G3** — thêm tiêu chí bắt buộc: tỷ lệ AC testable = 100 %, câu hỏi mở Critical/Major = 0. `quality-gate-g3.md`, `ba-03-specification/SKILL.md`.
- **Tiêu chí định lượng cho G4** — thêm tiêu chí bắt buộc: RTM coverage ≥ ngưỡng dự án (mặc định 100 %), Pass Rate ≥ ngưỡng, Defect Critical/Major còn mở = 0. `quality-gate-g4.md`, `ba-06-test-uat/SKILL.md`.
- **AI Review Status chuẩn hóa** — mọi agent output kèm `AI Review Status` với 4 giá trị: `Draft - cần review | Reviewed - Accepted | Reviewed - Accepted with Changes | Reviewed - Rejected`, đồng bộ với `ai-run-log.md`. `POWER.md` và 6 output-schema/reference files.
- **CI/CD** — `.github/workflows/validate.yml` chạy `validate_power.py` trên mỗi PR và push main.
- **CHANGELOG.md** — file này.

### Thay đổi
- **Rào cản bắt buộc — dedup** — 15 SKILL.md không còn nhúng 10 điều giống nhau; thay bằng 1 dòng tham chiếu về `POWER.md` (nguồn chính thức duy nhất). Giảm ~150 dòng lặp, sửa 1 chỗ thay vì 16. `POWER.md`, 15 `SKILL.md`.
- **ba-agent-qa-review bắt buộc ở BA-02 và BA-06** — trước đây tuỳ chọn, nay bắt buộc tại BA-02 Bước 6 (trước G2) và BA-06 Bước 4 (trước UAT). Bắt buộc tại: BA-02, BA-03, BA-04, BA-06. Tuỳ chọn tại: BA-01, BA-05, BA-07. `POWER.md`, `README.md`, `ba-02-business-analysis/SKILL.md`, `ba-06-test-uat/SKILL.md`.
- **validate_power.py** — thêm check `frontmatter` (YAML hợp lệ, có name + description); cập nhật check `guardrails` cho cấu trúc tham chiếu mới (POWER.md là nguồn, skill là tham chiếu).
- **plugin.json** — version 1.0.0 → 1.1.0.
- **README.md** — version 1.0 → 1.1; cập nhật quy ước rào cản, thêm mục Process Tracks, cập nhật ghi chú qa-review bắt buộc.

### Cần làm thủ công
- **Khôi phục file gốc .docx/.xlsx** — `01_SOP_BA_Agile_AI.docx` và `02_Bo_Template_BA.xlsx` đã bị xoá, chỉ còn trong Recycle Bin. Cần restore và commit vào git (khuyến nghị Git LFS) để xoá single point of failure.

## [1.0.0] — 2025-07-14

Phiên bản đầu tiên: 7 quy trình (BA-01…BA-07), 2 tài liệu (BRD, URD), 6 AI agent, 7 quality gate, bộ template và archive.
