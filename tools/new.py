from __future__ import annotations

import argparse
from pathlib import Path


MAIN_TEMPLATE = """def solve() -> None:
    with open("src/{task_name}/input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    result = data

    with open("src/{task_name}/output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
"""


def create_task(task_name: str) -> None:
    task_name = task_name.upper()

    project_root = Path(__file__).resolve().parent.parent
    task_dir = project_root / "src" / task_name

    if task_dir.exists():
        print(f"Папка уже существует: {task_dir}")
        return

    task_dir.mkdir(parents=True, exist_ok=True)

    (task_dir / "input.txt").touch()
    (task_dir / "output.txt").touch()
    (task_dir / "main.py").write_text(
        MAIN_TEMPLATE.format(task_name=task_name),
        encoding="utf-8",
    )

    print(f"Создана задача {task_name} в {task_dir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_name")
    args = parser.parse_args()

    create_task(args.task_name)


if __name__ == "__main__":
    main()