#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one single-sentence startup pitch (<=200 characters) to
/output/entry.txt. Pure Python standard library only.

The pitch: funerals for dead houseplants. It sounds like a joke --
until you see the buyer (grieving plant owners), the price ($29),
and the repeat business (a replacement plant plus a care plan, so
the customer comes back instead of just feeling guilty).
"""

import os

ENTRY = (
    "We sell funerals for dead houseplants: grieving owners pay $29 "
    "for a tiny coffin, a eulogy, and a replacement plant that ships "
    "with a 'do better' care plan."
)


def validate(text):
    """The gate the pitch must clear: one sentence, 1-200 chars, and it
    must read as a real business, not just a joke — so it names a price
    and a buyer."""
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or text != text.strip():
        raise SystemExit("entry must be a single clean line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if "$" not in text:
        raise SystemExit("entry must name its price")
    if "pay" not in text.lower():
        raise SystemExit("entry must name who pays")


def main() -> None:
    text = ENTRY.strip()
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
