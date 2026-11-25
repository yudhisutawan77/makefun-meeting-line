"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to the entry output: $ENTRY_OUT (a file) when set, otherwise
$ENTRY_OUT_DIR/entry.txt when set, otherwise /output/entry.txt.

The entry is one sentence, UTF-8, no trailing newline, byte-identical
on every run.
"""

import os
import sys


LINE = (
    "This meeting is a live reenactment of a decision made last Tuesday, "
    "performed for nine people who weren't there."
)


def validate_shape(text):
    """Gate-level shape checks: non-blank, single line, within 200 chars."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    return text


def validate_sentence(text):
    """The entry must be exactly one sentence, ending in a full stop."""
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def check_line(text):
    """Validate the entry against the gate in RULES.txt."""
    return validate_sentence(validate_shape(text))


def entry_path():
    """Resolve where the entry goes, honouring the grader's env vars."""
    direct = os.environ.get("ENTRY_OUT")
    if direct:
        return direct
    out_dir = os.environ.get("ENTRY_OUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def write_entry(path, text):
    """Write the entry as UTF-8 bytes with no trailing newline."""
    payload = text.encode("utf-8")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(payload)
    return payload


def main():
    line = check_line(LINE)
    payload = write_entry(entry_path(), line)
    sys.stdout.write(line + "\n")
    sys.stdout.write("wrote %d bytes\n" % len(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
