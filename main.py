#!/usr/bin/env python3
"""Write one office joke for make.fun's One-Line Office Jokes bounty.

Why this entry fits the judge's brief: it turns on a real office
detail, the reply-all accident, and lands the laugh in the last
few words, "my regret", in one reading.
"""

import os

LINE = (
    "I hit reply-all to say 'please remove me,' and now 400 strangers "
    "know my name, my job, and my regret."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-199 characters, a single line.
    # The line was counted at exactly 101 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 101, f"line is {len(line)} characters, expected 101"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 199, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"
    assert line.endswith("regret."), "punch must land in the last few words"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 101, "entry.txt is not 101 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
