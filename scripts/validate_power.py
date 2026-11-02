#!/usr/bin/env python3
"""Kiểm định tính nhất quán của power. Chạy từ bất kỳ đâu: python scripts/validate_power.py

Chỉ dùng thư viện chuẩn. Thoát với mã 1 nếu có lỗi.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))
PROCESS = [p for p in SKILLS if p.parent.name.startswith("ba-0")]
AGENTS = [p for p in SKILLS if p.parent.name.startswith("ba-agent-")]
ERRORS = []

# Hai file lưu nguyên văn, hash lấy từ assets/_archive/README.md.
FROZEN = {
    "assets/_archive/prompt-pack-v1.0.md": "436cdcc955a289a9c572161573deae87a45edece3871c2a714c308bdfd315f85",
    "assets/_archive/pack-readme-v1.0.md": "29dcfc2fba8405235d19c799322987c36fab3f4dc5d638e5ade47a0fe8ea3646",
}
SHEET_TEMPLATES = {
    "Intake": "skills/ba-01-requirement-intake/assets/requirement-intake-record.md",
    "Analysis": "skills/ba-02-business-analysis/assets/business-analysis-doc.md",
    "User Story AC": "skills/ba-03-specification/assets/user-story-ac.md",
    "RTM": "skills/ba-03-specification/assets/rtm.md",
    "Change Log": "skills/ba-05-change-management/assets/decision-log-cr.md",
    "UAT Report": "skills/ba-06-test-uat/assets/uat-report.md",
    "Handover": "skills/ba-07-release-handover/assets/handover-checklist.md",
    "AI Review": "skills/ba-agent-qa-review/assets/ai-review-log.md",
}


def read(path):
    return Path(path).read_text(encoding="utf-8").replace("\r\n", "\n")


def rel(path):
    return Path(path).relative_to(ROOT).as_posix()


def error(check, message):
    ERRORS.append(f"[{check}] {message}")


def check_counts():
    if len(PROCESS) != 7 or len(AGENTS) != 6:
        error("counts", f"cần 7 skill quy trình và 6 agent, thấy {len(PROCESS)} và {len(AGENTS)}")


def check_guardrails():
    blocks = {}
    for path in [ROOT / "POWER.md", *SKILLS]:
        match = re.search(r"^## Rào cản bắt buộc.*?\n(.*?)(?=^## |^Mười điều|^Riêng ở)", read(path), re.M | re.S)
        if not match:
            error("guardrails", f"{rel(path)}: không có khối rào cản")
            continue
        items = re.findall(r"^\d+\. .*$", match.group(1), re.M)
        blocks.setdefault(tuple(items), []).append(rel(path))
    if len(blocks) > 1:
        error("guardrails", f"có {len(blocks)} phiên bản khác nhau: {list(blocks.values())}")
    for items in blocks:
        if len(items) != 10:
            error("guardrails", f"cần 10 điều, thấy {len(items)}")


def check_references():
    pattern = re.compile(r"`((?:\.\./)?(?:assets|references|skills)/[^`\s<>*]+?\.md)`")
    for path in [ROOT / "POWER.md", ROOT / "README.md", *(ROOT / "skills").rglob("*.md")]:
        parts = path.relative_to(ROOT).parts
        skill_dir = ROOT / parts[0] / parts[1] if parts[0] == "skills" else ROOT
        for ref in pattern.findall(read(path)):
            bases = (path.parent, skill_dir, ROOT)
            if not any((base / ref).exists() for base in bases):
                error("references", f"{rel(path)}: không tìm thấy {ref}")


def check_frozen():
    for name, expected in FROZEN.items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != expected:
            error("frozen", f"{name}: hash lệch ({actual[:12]}…)")


def check_template_columns():
    workbook = read(ROOT / "assets/_archive/workbook-v1.0.md")
    for sheet, template in SHEET_TEMPLATES.items():
        lines = workbook.split(f"## Sheet `{sheet}`\n", 1)[1].splitlines()
        header = next(line for line in lines if line.startswith("|"))
        columns = [c.strip() for c in header.strip("|").split("|")]
        text = read(ROOT / template)
        for column in columns:
            if column not in text:
                error("columns", f"{template}: thiếu cột `{column}` của sheet {sheet}")


def parse_step_list(text):
    """'BA-04 Bước 5; BA-05 Bước 3, 5' -> {('BA-04', 5), ('BA-05', 3), ('BA-05', 5)}"""
    calls = set()
    for chunk in text.split(";"):
        match = re.search(r"(BA-0\d) Bước ([\d, ]+)", chunk)
        if match:
            calls |= {(match.group(1), int(n)) for n in re.findall(r"\d+", match.group(2))}
    return calls


def check_agent_matrix():
    names = [p.parent.name for p in AGENTS]
    sources = {}
    for doc in ("POWER.md", "README.md"):
        for name in names:
            row = next((l for l in read(ROOT / doc).splitlines() if l.startswith(f"| `{name}` |")), None)
            if row is None:
                error("agent-matrix", f"{doc}: thiếu dòng {name}")
                continue
            sources.setdefault(name, {})[doc] = parse_step_list(row.rstrip(" |").rsplit("|", 1)[1])
    for path in AGENTS:
        rows = re.findall(r"^\| (BA-0\d)\.[^|]*\| Bước (\d+) \|", read(path), re.M)
        sources.setdefault(path.parent.name, {})[rel(path)] = {(ba, int(step)) for ba, step in rows}
    bodies = {name: set() for name in names}
    for path in PROCESS:
        ba = "BA-" + path.parent.name[3:5]
        body = re.search(r"^## Quy trình\n(.*?)^## ", read(path), re.M | re.S).group(1)
        for step, content in re.findall(r"^### Bước (\d+).*?\n(.*?)(?=^### |\Z)", body, re.M | re.S):
            for name in set(re.findall(r"ba-agent-[a-z-]+", content)):
                bodies[name].add((ba, int(step)))
    for name in names:
        sources.setdefault(name, {})["thân skill quy trình"] = bodies[name]
        distinct = {frozenset(v) for v in sources[name].values()}
        if len(distinct) > 1:
            detail = {k: sorted(v) for k, v in sources[name].items()}
            error("agent-matrix", f"{name} không khớp: {detail}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    for check in (check_counts, check_guardrails, check_references, check_frozen, check_template_columns, check_agent_matrix):
        check()
    if ERRORS:
        print("\n".join(ERRORS))
        print(f"\nKHÔNG ĐẠT: {len(ERRORS)} lỗi")
        return 1
    print("ĐẠT: số skill, rào cản, tham chiếu, file đóng băng, cột template, ma trận gọi agent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
