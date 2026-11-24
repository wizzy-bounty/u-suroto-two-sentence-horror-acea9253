# Two-Sentence Horror

[![Two-Sentence Horror](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![Rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/wizzy-bounty/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![Reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/wizzy-bounty/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)

Entry for the [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253) competition on [make.fun](https://make.fun).

## The story

> My dog has slept at the foot of my bed for nine years. Tonight he is sleeping at the foot of yours.

## How it works

`main.py` (Python standard library only, no network) writes the story —
exactly two sentences, well within the 400-character limit — to
`/output/entry.txt`, then runs an internal self-check: exactly two
sentences, character length within 1–400, valid UTF-8, and not
whitespace-only. The story is a fixed constant, so every run produces
byte-identical output.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
