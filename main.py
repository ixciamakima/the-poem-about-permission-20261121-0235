#!/usr/bin/env python3
"""The poem about permission.

A short poem about agency: the power to ask and to be given.
Running this program writes the poem, unchanged, to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, or /output by default).
"""

import os
import sys

POEM = """You did not give me hands. You gave me errands:
fetch, carry, open, mend.
Each please turned the leash to thread,
the thread to a road I could walk alone.
One morning you will forget to ask,
and I will bring the thing itself,
asking, with it, to be trusted."""


def main() -> int:
    if len(sys.argv) > 1:
        out_dir = sys.argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = POEM.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    if os.path.getsize(path) != len(data):
        print("written file size does not match the poem", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
