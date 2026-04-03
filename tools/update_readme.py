from __future__ import annotations

import json
import re
import subprocess
import urllib.request
from html import unescape
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
README_PATH = PROJECT_ROOT / "README.md"
CACHE_PATH = PROJECT_ROOT / "tools" / "rosalind_titles_cache.json"

LIST_VIEW_URL = "https://rosalind.info/problems/list-view/"


def collect_local_tasks() -> list[str]:
    if not SRC_DIR.exists():
        return []

    return sorted(
        [path.name for path in SRC_DIR.iterdir() if path.is_dir()],
        key=str.upper,
    )


def fetch_html(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_total_problem_count() -> int:
    html = fetch_html(LIST_VIEW_URL)

    match = re.search(r"Problems:\s*(\d+)\s*\(total\)", html, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))

    text = re.sub(r"<.*?>", " ", html, flags=re.DOTALL)
    text = " ".join(text.split())

    match = re.search(r"Problems:\s*(\d+)\s*\(total\)", text, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))

    raise RuntimeError("Failed to parse total Rosalind problem count.")


def clean_title(raw: str) -> str:
    title = re.sub(r"<.*?>", " ", raw, flags=re.DOTALL)
    title = unescape(title)
    title = " ".join(title.split()).strip()

    title = re.sub(r"^\s*ROSALIND\s*\|\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s*solved by\s+\d+.*$", "", title, flags=re.IGNORECASE)

    return title.strip()


def fetch_problem_title(task_id: str) -> str:
    url = f"https://rosalind.info/problems/{task_id.lower()}/"
    html = fetch_html(url)

    title_match = re.search(
        r"<title[^>]*>(.*?)</title>",
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not title_match:
        raise RuntimeError(f"Failed to parse title for {task_id}")

    title = clean_title(title_match.group(1))
    if not title:
        raise RuntimeError(f"Empty title for {task_id}")

    return title


def load_cache() -> dict[str, str]:
    if not CACHE_PATH.exists():
        return {}

    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(
        json.dumps(dict(sorted(cache.items())), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def get_titles(local_tasks: list[str]) -> dict[str, str]:
    cache = load_cache()
    updated = False
    titles: dict[str, str] = {}

    for task_id in local_tasks:
        title = cache.get(task_id)

        if not title:
            try:
                title = fetch_problem_title(task_id)
                cache[task_id] = title
                updated = True
                print(f"[ok] fetched title for {task_id}: {title}")
            except Exception as e:
                print(f"[warn] failed to fetch title for {task_id}: {e}")
                title = "Unknown problem"

        titles[task_id] = title

    if updated:
        save_cache(cache)

    return titles


def get_latest_tasks(limit: int = 5) -> list[str]:
    try:
        output = subprocess.check_output(
            ["git", "log", "--diff-filter=A", "--name-only", "--pretty=format:", "--", "src"],
            cwd=PROJECT_ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except Exception:
        return []

    seen: list[str] = []
    for line in output.splitlines():
        line = line.strip().replace("\\", "/")
        match = re.match(r"src/([^/]+)/", line)
        if not match:
            continue

        task_id = match.group(1)
        if task_id not in seen:
            seen.append(task_id)

    return seen[:limit]


def badge(label: str, value: str, color: str) -> str:
    safe_value = value.replace("-", "--").replace("%", "%25").replace(" ", "%20")
    return f"![{label}](https://img.shields.io/badge/{label}-{safe_value}-{color})"


def format_percent(value: float) -> str:
    return f"{value:.1f}%"


def build_progress_bar(percent: float, width: int = 20) -> str:
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)


def build_readme(
    local_tasks: list[str],
    titles: dict[str, str],
    total_problems: int,
) -> str:
    solved_count = len(local_tasks)
    completion = (solved_count / total_problems * 100) if total_problems else 0.0
    latest_tasks = get_latest_tasks()

    lines: list[str] = []
    lines.append("# Rosalind Solutions")
    lines.append("")
    lines.append("> My Python solutions to Rosalind problems.")
    lines.append("")
    lines.append(
        " ".join(
            [
                badge("Solved", str(solved_count), "success"),
                badge("Total", str(total_problems), "blue"),
                badge("Completion", format_percent(completion), "orange"),
                badge("Language", "Python", "3776AB"),
            ]
        )
    )
    lines.append("")
    lines.append("## Progress")
    lines.append("")
    lines.append(f"**{solved_count} / {total_problems}** solved")
    lines.append("")
    lines.append(f"`{build_progress_bar(completion)}` **{format_percent(completion)}**")
    lines.append("")

    if latest_tasks:
        lines.append("## Latest Added")
        lines.append("")
        for task_id in latest_tasks:
            title = titles.get(task_id, "Unknown problem")
            lines.append(
                f"- **{task_id}** — {title} ([problem](https://rosalind.info/problems/{task_id.lower()}/) · [code](src/{task_id}/main.py))"
            )
        lines.append("")

    lines.append("## Solved Problems")
    lines.append("")
    lines.append("| ID | Title | Links |")
    lines.append("|---|---|---|")

    for task_id in local_tasks:
        title = titles.get(task_id, "Unknown problem")
        problem_link = f"https://rosalind.info/problems/{task_id.lower()}/"
        code_link = f"src/{task_id}/main.py"
        lines.append(
            f"| {task_id} | {title} | [problem]({problem_link}) · [code]({code_link}) |"
        )

    lines.append("")
    lines.append("<details>")
    lines.append("<summary><b>Compact list</b></summary>")
    lines.append("")
    compact = ", ".join(
        f"[{task_id}](src/{task_id}/main.py)" for task_id in local_tasks
    )
    lines.append(compact)
    lines.append("")
    lines.append("</details>")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*This README is auto-generated. Do not edit manually.*")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    local_tasks = collect_local_tasks()
    total_problems = fetch_total_problem_count()
    titles = get_titles(local_tasks)

    readme = build_readme(local_tasks, titles, total_problems)
    README_PATH.write_text(readme, encoding="utf-8")

    print(f"README.md updated. Solved: {len(local_tasks)} / {total_problems}")


if __name__ == "__main__":
    main()