#!/usr/bin/env python3
"""Frog Trio sleeve notes.

Writes the album title and back-cover blurb for the Frog Trio — a jazz
trio made entirely of frogs — for the make.fun competition
u-ravendell-sleeve-notes-for-the-frog-trio-29d80da5.

Output: /output/entry.txt, one album title followed by a short blurb,
1-400 UTF-8 characters in total.
"""

import os

ENTRY = """Pondwater Blue

Live from the Lily Pad Club, the Frog Trio — Marlowe on tenor sax, Bea on upright bass, Tad on brushes — swing standards till the reeds hum and the pond answers back. No gimmick, no trick: three frogs, one late set, and the blues played the way they were meant to be — wet, low, and after midnight. You can hear the crickets keeping time in the back.
"""


def main() -> None:
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {out}")


if __name__ == "__main__":
    main()
