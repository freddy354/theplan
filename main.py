"""Entry for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (1-280 chars) to /output/entry.txt. Stdlib only, no network,
deterministic: the same text on every run.
"""

import os

TEXT = (
    "Day 1: test 200 Shopify checkouts and find the broken ones. "
    "Email each owner a free audit naming the exact lost sale. "
    "Fix it for $49 \u2014 code you write. "
    "$60 page, $40 email tool. "
    "At a 5% close rate: 10 fixes, $490 by day 30. "
    "No ads, no audience \u2014 the bug is the pitch."
)


def main():
    if not 1 <= len(TEXT) <= 280:
        raise ValueError("entry must be 1-280 characters, got %d" % len(TEXT))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
