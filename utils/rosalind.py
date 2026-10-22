"""Small standard-library helpers shared across Rosalind solutions."""

from __future__ import annotations

from typing import Iterable, TextIO


def read_text(stream: TextIO) -> str:
    """Read all text from a stream and remove surrounding whitespace."""
    return stream.read().strip()


def read_fasta(text: str) -> list[tuple[str, str]]:
    """Parse FASTA text into (record_id, sequence) pairs.

    Blank lines are ignored. Sequence lines are joined and whitespace removed.
    """
    records: list[tuple[str, str]] = []
    current_id: str | None = None
    sequence_parts: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_id is not None:
                records.append((current_id, "".join(sequence_parts)))
            current_id = line[1:].split(maxsplit=1)[0]
            sequence_parts = []
        else:
            if current_id is None:
                raise ValueError("Sequence data found before the first FASTA header.")
            sequence_parts.append("".join(line.split()))

    if current_id is not None:
        records.append((current_id, "".join(sequence_parts)))
    return records


def format_fasta(records: Iterable[tuple[str, str]], width: int = 60) -> str:
    """Format (record_id, sequence) pairs as FASTA text."""
    if width < 1:
        raise ValueError("width must be at least 1")

    lines: list[str] = []
    for record_id, sequence in records:
        lines.append(f">{record_id}")
        lines.extend(sequence[index : index + width] for index in range(0, len(sequence), width))
    return "\n".join(lines)
