"""One-star review of sleep, an everyday essential.

Writes a single deadpan one-star review to /output/entry.txt.
Stdlib only, deterministic, no network, no file reads.
"""

import os

REVIEW = (
    "I slept eight hours and woke up tired. "
    "If rest worked, I would not need to do it again tonight."
)


def main() -> None:
    # Self-check the sealed gate before writing: 1-160 chars, one line.
    assert 1 <= len(REVIEW) <= 160, "review outside the 1-160 character gate"
    assert "\n" not in REVIEW and REVIEW.strip() == REVIEW
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
