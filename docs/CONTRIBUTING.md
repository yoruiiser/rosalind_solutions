# Solution workflow

This is a personal solutions repository, so "contributing" means adding or improving your own solutions. Preserve existing work and keep each problem easy to run on its own.

## Folder and file names

Use this pattern:

```text
solutions/<track>/<topic>/<PROBLEM_ID>/
├── solution.py
├── sample_input.txt
└── sample_output.txt
```

Use Rosalind's problem abbreviation for the final folder, such as `DNA`. Choose a short topic folder such as `strings_and_arrays`, `probability`, `dynamic_programming`, or `graph_algorithms`. If a problem does not fit an existing topic, add a descriptive topic folder.

## Start a solution

1. Copy `templates/problem.py`, `templates/sample_input.txt`, and `templates/sample_output.txt` into the problem folder.
2. Rename `problem.py` to `solution.py`.
3. Implement the answer in `solve(text)` or adapt the template to parse the input directly.
4. Keep the script runnable from the repository root and print only the answer to standard output.
5. Add the official example to the sample files and try the run command in the README.
6. Update `PROGRESS.md`.

## Style

- Use Python's standard library unless a problem benefits from a dependency.
- Keep the algorithm understandable; add a short explanation in a comment or docstring for non-obvious steps.
- Avoid hard-coding the sample answer. Read from standard input so the same solution works with Rosalind's dataset.
- Do not include personal credentials or private datasets in commits.

## Reviewing your own changes

Before committing, check that the files are in the expected folder and run the sample command from the README. A future optional test runner can be added if the collection grows.
