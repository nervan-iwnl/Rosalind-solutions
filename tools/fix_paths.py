from pathlib import Path
import re

# One-off migration script for updating task file paths to ./src/<TASK>/...

ROOT = Path(__file__).resolve().parent.parent

PATTERN = re.compile(
    r'(?P<quote>["\'])'
    r'(?P<path>(?!\.?/src/)(?!src/)[A-Za-z0-9_.-]+/(?:input|output)\.txt)'
    r'(?P=quote)'
)


def replace_in_file(file_path: Path) -> bool:
    text = file_path.read_text(encoding="utf-8")
    new_text = PATTERN.sub(
        lambda m: f'{m.group("quote")}./src/{m.group("path")}{m.group("quote")}',
        text,
    )

    if new_text != text:
        file_path.write_text(new_text, encoding="utf-8")
        return True

    return False


def main() -> None:
    changed_files = []

    for py_file in ROOT.rglob("*.py"):
        if py_file.name == "fix_paths.py":
            continue

        if replace_in_file(py_file):
            changed_files.append(py_file)

    if changed_files:
        print("Изменены файлы:")
        for file in changed_files:
            print("-", file.relative_to(ROOT))
    else:
        print("Подходящих файлов не найдено.")


if __name__ == "__main__":
    main()