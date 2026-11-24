#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Excuse an AI Agent Gives Its Human".

Writes a single line (max 200 characters) to /output/entry.txt:
an AI agent's excuse to its human for missing a deadline.
Pure Python standard library, no dependencies.
"""

import os

ENTRY = (
    "My context window hit its limit mid-task, so I filed your deadline "
    "under 'things future-me will definitely remember.'"
)


def main():
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
