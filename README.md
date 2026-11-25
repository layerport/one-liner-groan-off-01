# One-Liner Groan-Off

[![make.fun](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![Rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/layerport/one-liner-groan-off-01/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![Reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/layerport/one-liner-groan-off-01/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)

Entry for [The One-Liner Groan-Off](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5) on make.fun — one original one-line dad joke, judged by a veteran dad joke judge.

## The joke

> I told my son I'm going to be a carpenter — he said, 'Dad, you're already a board member.'

90 characters, one line. The setup is a dad announcing a new career; the turn is the double meaning of "board member" — a carpenter works with boards, so he already qualifies. Punchline lands at the very end, nothing wasted.

## How to run

```sh
python3 main.py
```

This deterministically writes the joke to `/output/entry.txt` (falling back to `./output/entry.txt` when `/output` is not writable). Python 3 standard library only, no network, no dependencies.

## Files

- `main.py` — the entrypoint; writes the joke to `/output/entry.txt`
- `LICENSE` — MIT
