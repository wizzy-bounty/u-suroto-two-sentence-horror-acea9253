#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun competition
u-suroto-two-sentence-horror-acea9253.

Writes exactly one horror story of exactly two sentences (1-400 UTF-8
characters) to /output/entry.txt, then runs an internal self-check:
exactly two sentences, character length within bounds, valid UTF-8,
and not whitespace-only.

Deterministic: the story is a fixed constant, so every run writes
byte-identical output. Standard library only, no network.
"""

import os
import re
import sys

STORY = (
    "My dog has slept at the foot of my bed for nine years. "
    "Tonight he is sleeping at the foot of yours."
)

OUTPUT_PATH = "/output/entry.txt"


def count_sentences(text):
    """Count sentences by terminal punctuation (. ! ?) followed by
    whitespace or end of string."""
    parts = [p for p in re.split(r"[.!?]+(?:\s+|$)", text.strip()) if p]
    return len(parts)


def self_check(text):
    """Validate the story against the competition gate. Returns a list
    of failure messages (empty when the story passes)."""
    failures = []
    if not text or not text.strip():
        failures.append("empty or whitespace-only")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        failures.append("not valid UTF-8: %s" % exc)
    n_chars = len(text)
    if not 1 <= n_chars <= 400:
        failures.append("length %d chars outside 1-400" % n_chars)
    n_sentences = count_sentences(text)
    if n_sentences != 2:
        failures.append("sentence count %d, expected 2" % n_sentences)
    return failures


def main():
    failures = self_check(STORY)
    if failures:
        for failure in failures:
            print("SELF-CHECK FAIL: %s" % failure, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != STORY:
        print("SELF-CHECK FAIL: written output differs from story",
              file=sys.stderr)
        return 1

    print("OK: %d chars, %d sentences -> %s"
          % (len(STORY), count_sentences(STORY), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
