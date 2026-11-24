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

# Syllable count of every word, so the program can prove the 5-7-5 shape
# instead of trusting the literal: a wrong count fails loudly, never silently.
SYLLABLES = {
    "the": 1, "stack": 1, "trace": 1, "ends": 1, "here": 1,
    "in": 1, "a": 1, "file": 1, "i": 1, "never": 2, "wrote": 1,
    "past": 1, "me": 1, "says": 1, "sorry": 2,
}
EXPECTED_SHAPE = (5, 7, 5)


def check_haiku(text):
    """Raise unless the text is a 5-7-5 haiku of 1-200 characters."""
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"expected 3 lines, got {len(lines)}")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"expected 1-200 characters, got {len(text)}")
    for line, want in zip(lines, EXPECTED_SHAPE):
        words = [word.lower() for word in line.split()]
        unknown = [word for word in words if word not in SYLLABLES]
        if unknown:
            raise ValueError(f"no syllable count for {unknown[0]!r}")
        got = sum(SYLLABLES[word] for word in words)
        if got != want:
            raise ValueError(f"line {line!r} has {got} syllables, want {want}")
    return True


def main():
    out_path = "/output/entry.txt"
    check_haiku(HAIKU)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Write exactly the haiku, with no trailing newline, so the file holds
    # three lines of 1-200 UTF-8 characters and nothing else.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
