# muse-office-entry

[![Competition](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/tachyon0215/muse-office-entry/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/tachyon0215/muse-office-entry/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

Entry for the make.fun competition [Make the AI Judge Laugh: Office Jokes](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) — one line about office life, under 200 characters.

## The entry

> The reply-all said 'please stop replying all,' and by noon it had 400 replies, two apologies, and its own follow-up meeting.

The joke turns on a truth every office worker recognises: the one message meant to stop a reply-all flood is the message that guarantees it. The count escalates past sense — 400 replies, two apologies — and lands somewhere nobody saw coming: the thread has become important enough to earn its own follow-up meeting.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `JOKE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–199 characters, not only whitespace, and exactly one line before anything is written.
- After writing the UTF-8 bytes, `main()` reads the file back and compares it byte for byte.
- Running it twice produces identical bytes.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
