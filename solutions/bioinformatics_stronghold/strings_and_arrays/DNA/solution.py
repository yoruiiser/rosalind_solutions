"""DNA: Counting DNA Nucleotides.

Counts A, C, G, and T in a DNA string read from standard input.
"""

import sys


def solve(sequence: str) -> str:
    sequence = "".join(sequence.split())
    return " ".join(str(sequence.count(base)) for base in "ACGT")


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
