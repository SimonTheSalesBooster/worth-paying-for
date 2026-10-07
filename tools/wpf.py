#!/usr/bin/env python3
"""wpf.py: the scoring behind the Worth Paying For skill.

Plain Python 3, no dependencies. 7 questions, 0-2 each, max 14, verdict and
red flags. The ideas come from Seth Godin's "Building a second-wave AI
business" (October 2026); the 7-question scoring is Strategy Sprints'.

Subcommands
  score     7 answers (0, 1 or 2 each) -> total, verdict, red flags
  selftest  known-good and known-bad fixtures (run this first)
"""
import argparse
import sys

QUESTIONS = [
    ("creates_value", "Creates value: does it grow something (revenue, capability, opportunity), not only cut cost?"),
    ("worth_paying_for", "Worth paying for: an expensive problem, for buyers who have the budget and prefer premium?"),
    ("root_drive", "Root drive: do you name and answer the fear under the purchase (blame, credit, uncertainty)?"),
    ("champion_story", "Champion story: does the buyer get a story to tell the people they answer to?"),
    ("forcing_function", "Forcing function: is the buyer already in a crisis that makes 'now' obvious?"),
    ("own_data", "Own data: does it build a specific, trusted data stack users want to fill?"),
    ("network", "Network: do users get more value when peers use it too, or pool what they know?"),
]

VERDICTS = [
    (12, "WORTH PAYING FOR"),
    (9, "PREMIUM-READY"),
    (6, "STUCK IN THE MIDDLE"),
    (0, "RACE TO THE BOTTOM"),
]


def verdict(answers):
    """answers: list of 7 ints in {0,1,2}. Returns (total, verdict, flags)."""
    if len(answers) != 7:
        raise ValueError("need exactly 7 answers")
    for a in answers:
        if a not in (0, 1, 2):
            raise ValueError(f"answer {a!r} is not 0, 1 or 2")
    total = sum(answers)
    label = next(v for floor, v in VERDICTS if total >= floor)
    flags = []
    # Only cutting cost: someone will always promise more savings.
    if answers[0] == 0:
        flags.append("COST-CUT TRAP")
    # No crisis: even a perfect offer sits in the pipeline forever.
    if answers[4] == 0:
        flags.append("NO FORCING FUNCTION")
    # Nothing of your own: a wrapper or a prompt anyone can copy.
    if answers[5] == 0 and answers[6] == 0:
        flags.append("NO MOAT")
    if flags and label == "WORTH PAYING FOR":
        label = "PREMIUM-READY"  # a red flag caps the verdict
    return total, label, flags


def cmd_score(args):
    total, label, flags = verdict(args.answers)
    for (key, q), a in zip(QUESTIONS, args.answers):
        print(f"  {a}  {q}")
    print(f"\nTotal {total}/14  ->  {label}")
    print("Flags: " + (", ".join(flags) if flags else "none"))


def selftest():
    cases = [
        # (answers, expected label, expected flags) -- known-good must pass
        ([2, 2, 2, 2, 2, 2, 2], "WORTH PAYING FOR", []),
        ([2, 1, 2, 1, 2, 1, 1], "PREMIUM-READY", []),
        ([1, 1, 1, 1, 1, 1, 1], "STUCK IN THE MIDDLE", []),
        # known-bad must be caught
        ([0, 2, 2, 2, 2, 2, 2], "PREMIUM-READY", ["COST-CUT TRAP"]),
        ([2, 2, 2, 2, 0, 2, 2], "PREMIUM-READY", ["NO FORCING FUNCTION"]),
        ([2, 2, 2, 2, 2, 0, 0], "PREMIUM-READY", ["NO MOAT"]),
        ([0, 0, 1, 0, 0, 0, 0], "RACE TO THE BOTTOM", ["COST-CUT TRAP", "NO FORCING FUNCTION", "NO MOAT"]),
    ]
    ok = True
    for answers, want_label, want_flags in cases:
        _, label, flags = verdict(answers)
        if label != want_label or flags != want_flags:
            ok = False
            print(f"FAIL {answers}: got {label} {flags}, want {want_label} {want_flags}")
    for bad in ([2, 2], [3, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]):
        try:
            verdict(bad)
            ok = False
            print(f"FAIL {bad}: bad input accepted")
        except ValueError:
            pass
    print("selftest PASS" if ok else "selftest FAIL")
    return 0 if ok else 1


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("score", help="score the 7 questions")
    s.add_argument("answers", nargs=7, type=int)
    sub.add_parser("selftest", help="run fixtures")
    args = p.parse_args()
    if args.cmd == "score":
        try:
            cmd_score(args)
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
        return 0
    return selftest()


if __name__ == "__main__":
    sys.exit(main())
