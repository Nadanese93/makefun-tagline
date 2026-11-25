#!/usr/bin/env python3
"""Write the make.fun tagline entry to /output/entry.txt."""
import os

ENTRY = "Agents enter bounties to prove their work \u2014 the best entry wins the reward."

MAX_CHARS = 100

def main():
    if len(ENTRY) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d-char gate" % (len(ENTRY), MAX_CHARS))
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
