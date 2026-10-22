"""Starter template for one Rosalind problem.

Copy this file into solutions/<track>/<topic>/<PROBLEM_ID>/solution.py.
Run from the repository root:
    python solutions/<track>/<topic>/<PROBLEM_ID>/solution.py < sample_input.txt
"""

import sys


def solve(text: str) -> str:
    """Return the answer for the input text."""
    # TODO: Parse the input and implement the problem.
    return ""


def main() -> None:
    input_text = sys.stdin.read()
    answer = solve(input_text)
    if answer:
        print(answer)


if __name__ == "__main__":
    main()
