#!/usr/bin/env python3
"""make.fun bounty entry: One Line, One Laugh.

Writes a single original funny line to /output/entry.txt.

Stdlib only, no network, no clock, no randomness, no local imports:
two runs produce byte-identical output.
"""

import os

LINE = (
    "I finally met my soulmate \u2014 turns out she's my reflection, "
    "and even she's seeing someone else."
)


def main() -> int:
    text = LINE
    if not text or text != text.strip():
        raise SystemExit("entry line must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
