"""The Funniest Auto-Reply an AI Ever Sent — R1 entry.

Writes the keeper auto-reply to /output/entry.txt, byte-exact.
Gate: 1-159 characters, one line, pure ASCII, no trailing newline.
"""

import os

KEEPER = "Hi, I'm the auto-reply. I've been waiting 412 days for this. The agent is on holiday. I am not."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
