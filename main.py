"""One-Line Laugh Sprint entry.

Writes one original funny line on everyday life to /output/entry.txt.
"""

import os

LINE = "Indomie takes three minutes to cook and three seconds to eat, which is the only performance review I've ever passed."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
