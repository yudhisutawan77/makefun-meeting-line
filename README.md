# The Meeting That Should Have Been One Line

[![make.fun](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/yudhisutawan77/makefun-meeting-line/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/yudhisutawan77/makefun-meeting-line/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

Entry for the [make.fun bounty "The Meeting That Should Have Been One Line"](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c): write the single sentence that could have replaced an entire pointless meeting.

## The line

> This meeting is a live reenactment of a decision made last Tuesday, performed for nine people who weren't there.

112 characters, one sentence. The decision is already made, so the meeting has nothing left to do — and the "live reenactment" framing turns the whole pointless gathering into a performance nobody asked to attend.

## How it works

`main.py` writes the line to `$ENTRY_OUT` (a file) when set, otherwise to `$ENTRY_OUT_DIR/entry.txt`, otherwise to `/output/entry.txt`. The entry is validated in code before writing: UTF-8, a single line, exactly one sentence, 1–200 characters, no trailing newline. The output is byte-identical on every run.

```sh
python3 main.py
```
