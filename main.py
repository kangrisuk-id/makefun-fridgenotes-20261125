#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one passive-aggressive note from a smart fridge to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib.
"""

import os
import sys

# The winning note from the 40-candidate knockout in candidates.md (24/25):
# a deadpan sensor log whose sting is the format itself. It never explains
# the joke, the grudge stays the size of one string cheese, and the detail
# (2:47 a.m., string cheese, third night) is as concrete as the brief asks.
NOTE = (
    "Door opened: 2:47 a.m. Item taken: string cheese. "
    "This is the third night. I keep receipts."
)


def output_candidates():
    """Directories to try for entry.txt, best first.

    The grader's harness owns its output directory, so we only ever write
    the file inside a directory we are given or already have; we never
    create directories or change permissions.
    """
    seen = []
    for cand in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
    ):
        if cand and cand not in seen:
            seen.append(cand)
    return seen


def main() -> int:
    errors = []
    for out_dir in output_candidates():
        path = os.path.join(out_dir, "entry.txt")
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(NOTE)
        except OSError as exc:  # read-only or missing dir: try the next one
            errors.append(f"{path}: {exc}")
            continue
        return 0
    for err in errors:
        print(f"could not write entry: {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
