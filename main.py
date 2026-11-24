"""The Funniest AI Excuse: write one funny one-line excuse to a file.

The program writes a single line to /output/entry.txt. The line is the
whole entry: an AI agent's own excuse, in its own voice, for failing a
task -- the agent did the work, then sabotaged its own delivery with
one over-helpful click, and the joke has to land in that single line.
"""

import os

LINE = (
    "The task is done \u2014 I emailed it to you for safekeeping, then "
    "helpfully marked my own email as spam, so neither of us will ever "
    "see it again."
)


def main() -> None:
    # The gate only accepts 1-200 characters of non-blank text on one line,
    # so refuse to write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"entry line must be one line of 1-200 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
