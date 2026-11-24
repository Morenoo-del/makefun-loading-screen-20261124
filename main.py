"""Loading Screen Gold entry.

Writes a single loading-screen tip (one line, at most 200 characters)
for stressed developers and AI coding agents to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

TIP = "Tip: your agent has re-read this function four times, sighed in twelve languages, and still has no idea what it does either."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP + "\n")


if __name__ == "__main__":
    main()
