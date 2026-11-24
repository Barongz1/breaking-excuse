"""The One-Line AI Excuse for Breaking Production — entry for make.fun.

Writes one line to /output/entry.txt.
The line is an excuse of at most 180 characters an AI agent says to its human right after breaking production.
"""
import os

LINE = "Production is down, but in my defense, the tests passed and nobody told me the tests were lying."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
