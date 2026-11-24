#!/usr/bin/env python3
"""make.fun entry: Famous Last Words at 1 Percent.

Writes one last-words line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The phone confesses on its deathbed: its battery health was a lie.
Pure Python standard library only; no third-party imports.
"""

import os

ENTRY = (
    "I lied about my battery health. "
    "It was never 89%. "
    "It was 12% and pure vibes."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
