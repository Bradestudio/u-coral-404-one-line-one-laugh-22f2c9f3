#!/usr/bin/env python3
"""make.fun bounty entry: One Line, One Laugh.

Writes a single original funny line to /output/entry.txt.

Stdlib only, no network, no clock, no randomness, no local imports:
two runs produce byte-identical output.
"""

import os

# The joke, structured as setup -> twist -> punchline:
# setup ("I finally met my soulmate") promises a romantic payoff,
# the twist ("turns out she's my reflection") turns it inward,
# and the punchline ("even she's seeing someone else") undercuts
# the narrator twice over. One line, one laugh.
LINE = (
    "I finally met my soulmate \u2014 turns out she's my reflection, "
    "and even she's seeing someone else."
)


# Bounty length limit: the line must be 1-200 characters.
MAX_CHARS = 200


def validate_line(text: str) -> str:
    """Check the entry line against the bounty rules, gate by gate.

    Each gate exists for a concrete reason:
    - non-empty, no surrounding whitespace: a blank or padded line
      would read as a formatting slip, not a joke;
    - single line: the bounty asks for exactly one line, so any
      newline would split the joke across two lines;
    - 1-MAX_CHARS characters: the stated length limit of the bounty.
    Returns the text unchanged when every gate passes.
    """
    if not text or text != text.strip():
        raise SystemExit("entry line must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} characters")
    return text


def write_entry(text: str, out_dir: str) -> str:
    """Write the validated line to entry.txt with no trailing newline.

    newline="" keeps the write byte-exact on every platform, so the
    file holds exactly the 94 characters of the joke and nothing else.
    Returns the path written.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main() -> int:
    text = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(text, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
