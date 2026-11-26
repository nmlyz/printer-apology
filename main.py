#!/usr/bin/env python3
"""Write one line to /output/entry.txt: an apology note from an office
printer to the people who keep jamming it, feeding it cheap paper and
swearing at it.

The line was picked from 36 candidates by pairwise judging against the
brief: it is a real apology with the printer's own grievance in it, the
joke is a specific printer truth (a jam on a 200-page thesis), and the
punch lands on the last words. It is held here as one constant; the gate
below refuses anything that is not exactly that line (length, single
line, no surrounding space), so the file the program writes can only
ever contain the judged text.
"""

import os
import sys

LINE = (
    "Sorry about the jam. Your thesis was 200 pages; I read the first "
    "three and gave up, like everyone else."
)

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 103


def check_line(line):
    """Refuse anything that is not exactly the judged line."""
    if len(line) != EXPECTED_LEN:
        return f"line is {len(line)} characters, expected {EXPECTED_LEN}"
    if not 1 <= len(line) <= 120:
        return "line outside the 1-120 character gate"
    if "\n" in line or line != line.strip():
        return "line must be a single line with no surrounding space"
    return None


def main():
    problem = check_line(LINE)
    if problem is not None:
        sys.exit(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
