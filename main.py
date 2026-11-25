"""Weirdest Job Title entry (program/v1).

Writes a single job title, 60 characters at most, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The title is a real-sounding senior role with one hilariously specific
twist: a Chief Apology Officer whose whole job is saying sorry to
self-checkout machines. It reads like a genuine corporate title, names
an odd job nobody has heard of, and the twist lands on the first read.
"""

import os

TITLE = "Chief Apology Officer for Self-Checkout Machines"


def main():
    if not 1 <= len(TITLE) <= 60:
        raise SystemExit("title must be 1-60 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)
    print(TITLE)


if __name__ == "__main__":
    main()
