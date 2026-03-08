from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

LATEST_START = "<!-- AUTO:LatestProblems:start -->"
LATEST_END = "<!-- AUTO:LatestProblems:end -->"
PROBLEMS_START = "<!-- AUTO:Problems:start -->"
PROBLEMS_END = "<!-- AUTO:Problems:end -->"

LC_RE = re.compile(r"^#\s*LC\s*(\d{1,4})\s*—\s*(.+?)\s*$")


@dataclass(frozen=True)
class Problem:
    lc: int
    title: str
    notes_path: str
    ts: int


def read_title(notes: Path) -> tuple[int, str]:
    first_line = notes.read_text(encoding="utf-8").splitlines()[0].strip()
    m = LC_RE.match(first_line)
    if not m:
        raise ValueError(
            f"Invalid title line in {notes}: {first_line!r} (expected '# LC 0020 — Title')"
        )
    return int(m.group(1)), m.group(2)


def last_commit_ts(path: Path) -> int:
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%ct", "--", str(path)],
            text=True,
        ).strip()
        return int(out) if out else 0
    except Exception:
        return 0


def replace_block(text: str, start: str, end: str, body: str) -> str:
    if start not in text or end not in text:
        raise RuntimeError(f"Missing markers: {start} / {end}")
    pre, rest = text.split(start, 1)
    _, post = rest.split(end, 1)
    return pre + start + "\n" + body + end + post


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    index = repo_root / "index.md"
    problems_dir = repo_root / "problems"

    txt = index.read_text(encoding="utf-8")

    notes_files = sorted(problems_dir.glob("**/lc_*/notes.md"))
    problems: list[Problem] = []

    for nf in notes_files:
        lc, title = read_title(nf)
        ts = last_commit_ts(nf)
        problems.append(Problem(lc=lc, title=title, notes_path=nf.relative_to(repo_root).as_posix(), ts=ts))

    latest_sorted = sorted(problems, key=lambda p: (p.ts, p.lc), reverse=True)[:10]
    latest_body = "".join(
        [f"- [LC {p.lc:04d} — {p.title}]({p.notes_path})\n" for p in latest_sorted]
    )

    all_sorted = sorted(problems, key=lambda p: p.lc)
    problems_body = "".join(
        [f"- [LC {p.lc:04d} — {p.title}]({p.notes_path})\n" for p in all_sorted]
    )

    txt = replace_block(txt, LATEST_START, LATEST_END, latest_body)
    txt = replace_block(txt, PROBLEMS_START, PROBLEMS_END, problems_body)

    index.write_text(txt, encoding="utf-8")
    print("Updated index.md")


if __name__ == "__main__":
    main()
