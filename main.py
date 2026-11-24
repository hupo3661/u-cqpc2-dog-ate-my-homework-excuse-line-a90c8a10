#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one funny excuse line, in the dog's own voice, to
/output/entry.txt. The competition's gate accepts a single line of
UTF-8 text, 1 to 200 characters, not only white space; the line below
is 99 characters and ends with a period.

The program is deterministic: no randomness, no network, no clock.
It validates the line against the brief, writes it, then reads the
file back and verifies the content matches before exiting.
"""

import os

MIN_CHARS = 1
MAX_CHARS = 200

LINE = "I didn't eat your homework \u2014 I taste-tested it, and it failed. Page two was purely quality control."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the brief: one clean line of 1-200 characters.

    Raises SystemExit with a plain-language reason when the line
    breaks any rule, so a bad edit fails loudly instead of shipping
    an entry the gate would refuse.
    """
    if not line:
        raise SystemExit("Invalid line: entry must be non-empty.")
    if not line.strip():
        raise SystemExit("Invalid line: entry must not be only white space.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if not MIN_CHARS <= len(line) < MAX_CHARS:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} character limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )
    if not line.endswith("."):
        raise SystemExit("Invalid line: entry must end with a period.")
    if "  " in line:
        raise SystemExit("Invalid line: entry must not contain double spaces.")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise SystemExit("Invalid line: entry must not contain control characters.")


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
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
