#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one fixed two-sentence horror story to entry.txt in
MAKEFUN_OUTPUT_DIR when set, otherwise /output/entry.txt.
Standard library only, deterministic, no network.
"""

import os

STORY = (
    "The dentist refused to use the plaster mold of my teeth because it "
    "no longer matched my mouth. It had grown a second row of molars, "
    "still warm, and one already bore the filling I was scheduled to get "
    "next month."
)


def entry_path(out_dir):
    return os.path.join(out_dir, "entry.txt")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = entry_path(out_dir)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
