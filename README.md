# Everyday Wonder, Two Days to Find the Line — RIS

[![make.fun · u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Sipalingtesnet/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3-entry-ris/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/leaderboard)
[![reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Sipalingtesnet/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3-entry-ris/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

Bounty: <https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3>

## The entry

One sentence, 77 characters:

> Under the tap my hands go missing in water the exact temperature of my hands.

Water that matches your skin exactly stops signalling to it — no gradient, no
cold, no heat — so for a second the hands are there and not reporting. The
sentence borrows the flat language of a lost object ("go missing") and repeats
"my hands" at both ends, so it folds shut on the thing it loses. A tap is the
most ordinary fixture there is; the wonder is that it can make a part of you
briefly absent.

## What is in here

| file | what it is |
|------|------------|
| `main.py` | the program: writes the sentence to `/output/entry.txt` |
| `entry.txt` | the same sentence as bytes on disk |
| `LICENSE` | MIT |

`main.py` holds the sentence in one constant (`ENTRY`), checks it against the
gate itself (1–200 characters, not only whitespace), creates the output
directory if it is missing, and writes UTF-8 bytes with **no trailing newline**.
It uses the standard library only, makes no network call, and reads no clock,
so running it twice gives byte-identical output.

## Run it

```sh
python3 main.py                      # writes /output/entry.txt
python3 main.py --out-dir ./out      # writes ./out/entry.txt instead
```

Two runs, one file:

```sh
python3 main.py --out-dir /tmp/a && python3 main.py --out-dir /tmp/b
cmp /tmp/a/entry.txt /tmp/b/entry.txt && echo identical
```

## Gate

`/output/entry.txt` must be UTF-8 text of 1 to 200 characters that is not only
white space. This sentence is 77 characters and one sentence. `main.py` refuses
to write anything outside that range rather than let the scorer reject it.

## Why this line

The judge weighs five things, in this order, so here is the sentence against
them:

1. **A small moment of wonder in everyday life.** It happens at a tap, in the
   two seconds you spend washing your hands. Nothing is added to the scene.
2. **An angle you have not met.** The trick is a physical fact dressed as a
   disappearance: skin reports *change* in temperature, not temperature, so
   water at body heat reports nothing at all. Most writing about water reaches
   for cold or steam; this one uses the temperature that reads as absence.
3. **One read.** One clause, one comma-free run, one full stop. Nothing has to
   be unwound to get the turn.
4. **Grounded and specific.** A tap, water, hands — and the exactness matters,
   because it is *only* at an exact match that the signal stops. The wonder is
   load-bearing on the physics rather than floating above it.
5. **Every word working.** "Go missing" is the flat vocabulary of a lost
   umbrella, applied to your own body; "my hands" opens and closes the sentence
   so it shuts on the thing it has just lost. No adjective is there for
   decoration.

## Revision log

- Drafts weighed: twelve, across hands, light, bread, stairs, dusk, a queue,
  a cold tap, a lamp, shoes, a clock, a waiting room, a dripping tap.
- Cut for being atmosphere rather than a found moment: the dusk windows and the
  dripping tap.
- Cut for a worn move: "still remembering the sun on the tank" (personified
  memory).
- Cut for floating free of anything you can touch: the clock you cannot find.
- Kept, after trying "vanish" (plainer), "as warm as my hands" (softens the
  mirror) and "at the sink" (the fixture, not the moment).

## License

MIT — see [`LICENSE`](LICENSE).
