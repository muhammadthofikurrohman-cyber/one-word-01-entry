"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username, one word and nothing
else, to entry.txt for the judge.

The gate requires 1 to 30 UTF-8 characters, not only whitespace:
"thofix-05" is 9 characters, a single word with no spaces, no
padding and no gloss tacked on.
"""

import os

USERNAME = "thofix-05"


def output_dir():
    """Output directory from the grader, falling back to /output.

    An empty MAKEFUN_OUTPUT_DIR is treated as unset, so a blank
    value can never make the program write to a relative path.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"


def main():
    if not 1 <= len(USERNAME) <= 30 or USERNAME != USERNAME.strip():
        raise ValueError("username must be 1-30 characters, one word")
    os.makedirs(output_dir(), exist_ok=True)
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
