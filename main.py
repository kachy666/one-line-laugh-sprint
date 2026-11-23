#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes one original funny line on everyday life to /output/entry.txt.
"""

import os

LINE = "Indomie takes three minutes to cook and three seconds to eat, which is the only performance review I've ever passed."

MAX_CHARS = 200


def main() -> None:
    # Validate the entry before writing it: one non-empty line, at most 200 chars.
    assert LINE, "entry line must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"entry must be at most {MAX_CHARS} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
