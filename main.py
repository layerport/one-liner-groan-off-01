"""One-Liner Groan-Off entry.

Writes a single original one-line dad joke to /output/entry.txt.
Python 3 standard library only; fully deterministic.
"""

import os

JOKE = "I told my son I'm going to be a carpenter \u2014 he said, 'Dad, you're already a board member.'"


def main() -> None:
    # The gate allows 1 to 140 characters; this line is 90, one line.
    # The joke is original: a carpenter works with boards, so the dad is
    # already a "board member" -- setup and pun land in the same line,
    # punchline ("board member") at the very end, nothing wasted.
    line = JOKE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
