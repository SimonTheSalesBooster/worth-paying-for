# Worth Paying For

**Stop selling cheaper. Win bigger deals at the price you want.**

Every AI pitch your buyer hears right now promises the same stale thing: fewer people, less time, lower cost. So sooner or later the question lands on your desk.. why do you cost more? 🐬

Cutting your price is a race nobody wins. Someone will always promise bigger savings than you. The bitter part? Once the savings are banked, there's nothing left to sell.

Buyers with real budgets don't pay to save. They pay to feel safe, to look good, and to stop worrying. In B2B, every purchase hides one question: "What will I tell my boss?" 🐯

Hand your buyer that answer before they need it, and you lead the sales conversation. No begging. No discount to close. Your price stops looking expensive and starts looking serious.

This free Claude Code skill coaches you there. It's built on Seth Godin's idea of the second-wave AI business.

One question at a time, like a coach across the table. 7 questions, 0 to 2 each. 🌴 Then you walk away with the story your buyer tells after they say yes, the crisis that makes them buy this month, and ONE move for this week.

🐬 We ran it on our own business first. 10 out of 14.

It caught our cheapest offers setting a low price anchor. It pushed us to write the story we want our buyer to tell: "I installed the sales process before I hired, so the new hire performs from week one."

Our one move that week: add days from first call to signature to every deal in our CRM ([our full scorecard](./examples/strategy-sprints.md)). 🐯

Free. No sign-up. Not for you if you want a template to copy: it asks, you answer, you find the gap. Install below, then type `/worth-paying-for`.

---

## The 7 questions

| # | Question | 2 looks like |
|---|---|---|
| Q1 | **Creates value:** what do they have after a year that they didn't before? | New revenue or capability, not just savings |
| Q2 | **Worth paying for:** expensive problem, real budget? | Premium price reads as serious |
| Q3 | **Root drive:** what's the buyer afraid of? | Blame, credit or uncertainty, named and answered |
| Q4 | **Champion story:** what do they tell their boss after buying? | A ready story that serves their career |
| Q5 | **Forcing function:** why this month, not next year? | A live crisis: competitor, technology, market |
| Q6 | **Own data:** what do you know after 100 clients that nobody can copy? | Specific, trusted data that compounds |
| Q7 | **Network:** do clients win more when their peers use you too? | Built in, or pooled knowledge |

12-14 **WORTH PAYING FOR** · 9-11 PREMIUM-READY · 6-8 STUCK IN THE MIDDLE · 0-5 RACE TO THE BOTTOM.
Three red flags cap the verdict however high the total: **COST-CUT TRAP** (Q1 = 0), **NO FORCING FUNCTION** (Q5 = 0), **NO MOAT** (Q6 and Q7 = 0).

## Modes

| You type | You get |
|---|---|
| `/worth-paying-for` | A coaching session. One question at a time, in your words, ending in your card and one move for this week |
| `/worth-paying-for card <your offer or URL>` | A fast audit: it researches what it can, scores, and lists what to ask you |
| `/worth-paying-for idea "<AI business idea>"` | Tests an idea before you build it, plus the 3 traps (naked AI, hidden prompts, selling one at a time) |
| `/worth-paying-for story` | The story your buyer tells their boss, a one-line opener naming their crisis, and 3 questions for your next sales call |

## Install

```bash
git clone https://github.com/SimonTheSalesBooster/worth-paying-for ~/worth-paying-for
cp ~/worth-paying-for/worth-paying-for.md ~/.claude/commands/
python3 ~/worth-paying-for/tools/wpf.py selftest
```

Plain Python, no dependencies. The self-test runs known-good scores that must pass and known-bad ones (cost-cut only, no crisis, no moat, bad inputs) that must be caught.

## What's in the repo

| File | What it is |
|---|---|
| `worth-paying-for.md` | The skill: coaching rules, 7 questions, the 3 layers, forcing function, moat check |
| `tools/wpf.py` | Scoring, verdict, red flags, self-test |
| `knowledge/MODEL.md` | The model in plain words |
| `templates/card.md` | Your one-page Worth Paying For Card |
| `examples/strategy-sprints.md` | Our own scorecard and what we changed |

The ideas come from Seth Godin's "Building a second-wave AI business" (October 2026): https://seths.blog/2026/10/but-is-it-a-business/ Everything here is paraphrased in our own words. The 7-question scoring, thresholds, red flags and coaching flow are ours. Read the original.

---

## Who made this

**[Strategy Sprints](https://www.strategysprints.com)**, Simon Severino. We help B2B founders take control of the sales conversation. 2,400+ founders have gone through our programs. 🌴

Want more skills like this, plus a community of owners to use them with? 🐬 Join the Sprint Club: https://www.strategysprints.com

Ready to accelerate now? Book a Discovery Call: https://calendly.com/strategysprint/discovery-call

Happy hunting.

Simon & The Sprinters 🐬⚡️🐆

---

*Unofficial. Not affiliated with or endorsed by Seth Godin.*

## License

[Apache-2.0](./LICENSE) for our code and text. The original article belongs to its author.
