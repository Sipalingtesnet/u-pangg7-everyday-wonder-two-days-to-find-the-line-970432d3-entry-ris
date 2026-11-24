#!/usr/bin/env python3
"""Entry for "Everyday Wonder, Two Days to Find the Line".

The whole entry is one sentence: a small everyday moment turned until it
looks new. This program does nothing but put that sentence on disk at
/output/entry.txt, byte for byte, with no trailing newline, so that two runs
of it produce identical files.

    python3 main.py                   # writes /output/entry.txt
    python3 main.py --out-dir /tmp/x  # writes /tmp/x/entry.txt (local checks)

Standard library only, no network, no randomness, no clock.
"""

from __future__ import annotations

import os
import sys

# --- the entry -------------------------------------------------------------
# One sentence, 77 characters. Water that matches the temperature of the skin
# stops reaching it, so the hands stop arriving at the mind; the sentence
# repeats "my hands" once so it folds shut on the thing it loses.
ENTRY = "Under the tap my hands go missing in water the exact temperature of my hands."
# ---------------------------------------------------------------------------

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"

USAGE = """usage: python3 main.py [--out-dir DIR]

Writes the entry sentence, as UTF-8 bytes with no trailing newline, to
DIR/entry.txt (default DIR: /output).
"""


def target_dir(argv: list[str]) -> str:
    """Return the directory to write into, honouring an optional --out-dir."""
    args = list(argv[1:])
    while args:
        arg = args.pop(0)
        if arg in ("-h", "--help"):
            sys.stdout.write(USAGE)
            raise SystemExit(0)
        if arg == "--out-dir":
            if not args:
                raise SystemExit("--out-dir needs a value")
            return args.pop(0)
        if arg.startswith("--out-dir="):
            return arg.split("=", 1)[1]
        raise SystemExit("unknown argument: " + arg + "\n" + USAGE)
    return OUTPUT_DIR


def checked(text: str) -> str:
    """Refuse anything the gate would reject, or that is not one clean line."""
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry is outside the gate: %d characters" % len(text))
    if not text.strip():
        raise SystemExit("entry is only white space")
    # The file must hold one sentence; a stray newline would break that, and a
    # trailing newline would make the bytes drift from entry.txt.
    if "\n" in text or "\r" in text or "\x00" in text:
        raise SystemExit("entry must be a single line with no control breaks")
    if text != text.strip():
        raise SystemExit("entry must not begin or end with white space")
    return text


def main(argv: list[str]) -> int:
    text = checked(ENTRY)

    directory = target_dir(argv)
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_NAME)

    # write bytes, nothing appended, so repeat runs match exactly
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))

    sys.stdout.write("wrote %s (%d characters)\n" % (path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
