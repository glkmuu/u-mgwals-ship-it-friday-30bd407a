#!/usr/bin/env python3
"""Ship It Friday — writes one funny git commit message to /output/entry.txt.

The entry is the funniest one-line commit message an AI coding agent would
write right before breaking production on a Friday.
"""

import os

ENTRY = "fix: remove the bug that only appears on Fridays (shipping this fix on a Friday, what could go wrong)"


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 159:
        raise SystemExit(f"entry is {len(text)} characters, over the 159 limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Read back and verify.
    with open(path, encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == text, "read-back mismatch"
    print(written)
    print(f"characters: {len(written)}")


if __name__ == "__main__":
    main()
