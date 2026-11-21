#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet scene written to
relax the AI judge reading it. Deterministic: the same text, every run.

The text is built for the judge's brief, in its own order of criteria:
it relaxes by slowing the reader down (a 4 a.m. bakery, dough rising
slow, short sentences and line breaks that make the reading unhurried)
rather than by telling anyone to relax; the courage comes from the
scene itself -- yeast rising in the dark, unwatched, and still it
rises -- with no imperative in it, no "breathe", no "be brave"; the
words are plain, concrete and gentle, none that could be cut; it
leaves one thought to return to, that some things need time and
a little heat; and the bakery at four in the morning is its own
image, not a stock wellness phrase or a reworded meditation script.
"""

from pathlib import Path

TEXT = """Four in the morning: the baker lights the oven.
Flour on her hands, dough rising slow in its bowl.
Nothing hurries. The yeast works in the dark,
unwatched \u2014 and still it rises.
By sunrise the loaves are warm, the street smells of bread.
Some things need time, and a little heat."""


def main() -> None:
    # The competition gates the entry on 1-280 code points of non-blank
    # text; fail loudly here rather than shipping an entry the grader
    # would reject if the text is ever edited past the gate.
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"text is {len(TEXT)} code points, outside the 1-280 gate")
    if not TEXT.strip():
        raise SystemExit("text is blank")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
