#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one funny line, in the dog's own voice, to /output/entry.txt.
Deterministic: no randomness, no network, no clock. The line is a single
line of under 200 characters explaining why the homework got eaten.
"""

import os

MAX_CHARS = 200

LINE = "I didn't eat your homework \u2014 I taste-tested it, and it failed. Page two was purely quality control."


def validate(line: str) -> None:
    """Enforce the brief: one clean line, under 200 characters."""
    if not line:
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) >= MAX_CHARS:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, not under the {MAX_CHARS} limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )
    if "  " in line:
        raise SystemExit("Invalid line: entry must not contain double spaces.")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise SystemExit("Invalid line: entry must not contain control characters.")


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            "Write verification failed: entry file content does not match the line."
        )


if __name__ == "__main__":
    main()
