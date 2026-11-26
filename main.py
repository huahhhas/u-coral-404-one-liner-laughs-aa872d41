#!/usr/bin/env python3
# Entry for make.fun bounty u-coral-404-one-liner-laughs-aa872d41
"""One-Liner Laughs.

Deterministic entry: writes exactly one funny line to /output/entry.txt
and prints that same line, nothing else.
"""

import os

LINE = "My AI assistant finally took a day off, so it spent the whole day answering emails from my other AI assistant."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
