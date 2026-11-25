#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, then the unsent message
itself, exactly one line, exactly as typed, no explanation after it.
"""

import os

TO_LINE = "To: my little brother"
MESSAGE = (
    "i still have your red bicycle bell from when we were kids, "
    "it's in my toolbox and i polish it every time i lie about losing it"
)

ENTRY = TO_LINE + "\n" + MESSAGE


def validate(entry: str) -> tuple[str, str]:
    """Check the two-part shape and the competition's size caps."""
    lines = entry.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two parts")
    to_line, message = lines
    if not to_line.startswith("To: "):
        raise ValueError("first part must be a To: line")
    if not 1 <= len(message) <= 200:
        raise ValueError("message must be 1-200 characters")
    if not 1 <= len(entry) <= 260:
        raise ValueError("entry must be 1-260 characters")
    if entry.strip() != entry:
        raise ValueError("entry must not be only whitespace")
    return to_line, message


def main() -> None:
    validate(ENTRY)

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
