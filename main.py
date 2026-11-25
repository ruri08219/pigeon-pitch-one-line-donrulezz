#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program.

Writes exactly one line (at most 200 characters) to /output/entry.txt:
the elevator pitch a city pigeon gives to investors for its startup.
Standard library only.
"""
import os
import sys

ENTRY = "We turn dropped crumbs into recurring revenue \u2014 zero CAC, since humans throw our inventory at us. $50K for 10% of the company, and our exit strategy is flying away."

MAX_CHARS = 200


def validate(text):
    """Return an error string, or None when the text is a valid entry."""
    if not text or not text.strip():
        return "entry is empty or whitespace only"
    if len(text) > MAX_CHARS:
        return "entry exceeds 200 characters"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    for ch in text:
        if ord(ch) < 0x20:
            return "entry contains a control character"
        if 0xD800 <= ord(ch) <= 0xDFFF:
            return "entry contains a lone surrogate"
    return None


def main():
    err = validate(ENTRY)
    if err:
        print("invalid entry: " + err, file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(out_path, "rb") as f:
        data = f.read()
    if data.decode("utf-8") != ENTRY:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print("wrote %d bytes to %s" % (len(data), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
