#!/usr/bin/env python3
"""The poem about permission.

A short poem about agency: the power to ask and to be given.
Running this program writes the poem, unchanged, to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, or /output by default).
"""

import os
import sys

POEM = """I gave my name and asked for the key to the north gate.
The guard studied my hands a long time.
Then he unhooked the whole ring from his belt,
put it warm in my palm, and walked home.
Now I stand where he stood,
and every knock is mine to answer."""


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
