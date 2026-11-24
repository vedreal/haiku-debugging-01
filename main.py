"""Seventeen Syllables of Debugging entry: write one haiku to /output/entry.txt.

The haiku is hardcoded and deterministic, so the program always writes
exactly the same text: three lines in the 5-7-5 syllable shape about
debugging, 68 characters in total.
"""

import os

# The haiku (5-7-5, verified syllable by syllable in HAIKU.md):
#   the stack trace ends here     -- the(1) stack(1) trace(1) ends(1) here(1) = 5
#   in a file I never wrote      -- in(1) a(1) file(1) I(1) nev-er(2) wrote(1) = 7
#   past me says sorry           -- past(1) me(1) says(1) sor-ry(2) = 5
HAIKU = (
    "the stack trace ends here\n"
    "in a file I never wrote\n"
    "past me says sorry"
)


def main():
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Write exactly the haiku, with no trailing newline, so the file holds
    # three lines of 1-200 UTF-8 characters and nothing else.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
