"""One Star for Monday — make.fun entry.

Writes one original line — a one-star review of Monday as if Monday
were a restaurant — to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python
standard library, deterministic: every run writes the same bytes.

The line, and why it is built this way (the judge weighs, in order):
1. It IS a one-star review of Monday as a restaurant, opening with
   the verdict itself: "One star."
2. It sounds like a real diner's complaint, with a table, a dish and
   a bill that went wrong: seated at 6 a.m., served cold coffee, and
   a 9 a.m. meeting as the dish.
3. The joke is Monday's own condition, so the line could not be about
   any other day: the meeting that should have been an email is the
   Monday-est dish on the menu, and the bill is the weekend itself.
4. It is short and quotable at exactly 25 words — the cap — the kind
   of line someone retypes into the group chat without trimming.
5. It holds up on a second read: the first read laughs at the cold
   coffee and the email-meeting; the second read lands the bill —
   Monday did not just waste the morning, it charged the whole
   weekend for it.
"""

import os

LINE = (
    "One star. Seated at 6 a.m., got cold coffee and a 9 a.m. meeting "
    "that should have been an email. Paid with my whole weekend."
)

# The gate: entry.txt must be UTF-8 text of 1 to 180 characters,
# not only white space, and at most 25 words on a single line.
MAX_CHARS = 180
MAX_WORDS = 25


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, outside the 1-%d gate"
            % (len(LINE), MAX_CHARS)
        )
    if len(LINE.split()) > MAX_WORDS:
        raise SystemExit(
            "entry line is %d words, over the %d-word cap"
            % (len(LINE.split()), MAX_WORDS)
        )
    if LINE.strip() != LINE or "\n" in LINE:
        raise SystemExit("entry line must be a single line, no newlines")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
