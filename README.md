# Rosalind Solutions

A personal, beginner-friendly collection of solutions to [Rosalind](https://rosalind.info/) bioinformatics problems.

The repository is organized so each new problem has one home for its solution, sample input, and sample output. Existing solutions in `python_village/solutions/` are preserved.

## Repository map

```text
.
├── README.md
├── .gitignore
├── PROGRESS.md
├── docs/
│   └── CONTRIBUTING.md
├── templates/
│   ├── problem.py
│   ├── sample_input.txt
│   └── sample_output.txt
├── utils/
│   ├── __init__.py
│   └── rosalind.py
├── python_village/                 # Existing work; kept in its original layout
└── solutions/
    ├── bioinformatics_stronghold/
    │   └── strings_and_arrays/
    │       └── DNA/
    │           ├── solution.py
    │           ├── sample_input.txt
    │           └── sample_output.txt
    ├── bioinformatics_armory/
    ├── bioinformatics росalind/
    └── ...
```

Topic folders follow Rosalind's learning tracks. Create a problem folder named with its problem ID (for example, `DNA`, `RNA`, or `GC`). Put `solution.py`, `sample_input.txt`, and `sample_output.txt` together inside it. Keep the problem ID and folder names lowercase/uppercase exactly as Rosalind displays them.

## Add a solution

1. Choose the Rosalind track and topic that best fit the problem.
2. Copy the three files from `templates/` into `solutions/<track>/<topic>/<PROBLEM_ID>/`.
3. Rename `problem.py` to `solution.py`; implement the solution using standard input and standard output.
4. Save Rosalind's example input and expected output in the matching text files.
5. Run it from the repository root:

   ```bash
   python solutions/<track>/<topic>/<PROBLEM_ID>/solution.py < solutions/<track>/<topic>/<PROBLEM_ID>/sample_input.txt
   ```

6. Compare the printed result with `sample_output.txt`, then mark the problem complete in [PROGRESS.md](PROGRESS.md).

No third-party packages are required. Python 3.10 or newer is recommended.

## Reusable helpers

`utils/rosalind.py` includes small standard-library helpers for reading input and FASTA records. Import them from a solution when useful; each script should still work when run from the repository root. Use plain Python when a helper would make a beginner's solution harder to follow.

## Progress

Use [PROGRESS.md](PROGRESS.md) to record solved problem IDs. The list is intentionally manual: add a checkbox when you begin and mark it complete when your solution is ready. Add new Rosalind problems there as you work through them.

## Contributing to your own collection

- Keep each problem self-contained in its own folder.
- Include the official sample input and expected output when available.
- Prefer clear variable names and short comments that explain why, not every line.
- Do not commit private test data, credentials, or large generated files.
- See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for the folder convention and workflow.

## License and attribution

Problem statements and datasets belong to Rosalind and their respective authors. This repository contains personal solution code and learning notes. Follow Rosalind's terms when sharing problem text or data.
