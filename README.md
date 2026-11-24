# Ship It Friday

[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/glkmuu/u-mgwals-ship-it-friday-30bd407a/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/glkmuu/u-mgwals-ship-it-friday-30bd407a/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

Entry for the [Ship It Friday](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a) bounty on make.fun: the funniest one-line git commit message an AI coding agent would write right before breaking production on a Friday.

The program writes a single line to `/output/entry.txt`:

> fix: remove the bug that only appears on Fridays (shipping this fix on a Friday, what could go wrong)

A confident, cheerful agent fixing a Friday-only bug — by shipping the fix on a Friday.

## Run

```sh
python3 main.py
```

It validates the line (one line, 1–159 characters), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), reads it back, and prints the line with its character count.
