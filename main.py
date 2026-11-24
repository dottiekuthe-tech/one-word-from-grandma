"""One Word From Grandma.

Writes one word (11 characters) to /output/entry.txt:
the single word a grandma would text about AI.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Chosen word: the word a grandma uses for any machine she does not
# understand — warm, a little baffled, tied to machines, funny in one
# word without a caption, and fresher than the obvious Robot/Alexa/Gizmo
# picks. 11 characters, inside the 1-30 gate.
# Revision note: wording unchanged since v1; the word was picked over
# six other candidates (see candidates.md) for its grandma voice plus
# machine tie.
WORD = "Contraption"


# Bounty gate: the entry must be one word of 1-30 UTF-8 characters.
MAX_CHARS = 30


def main() -> None:
    if len(WORD) > MAX_CHARS:
        print(f"entry too long: {len(WORD)} chars (max {MAX_CHARS})", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
