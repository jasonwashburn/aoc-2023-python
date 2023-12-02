"""Common functions for AOC."""
from pathlib import Path


def parse_lines_from_file(path: str) -> list[str]:
    """Parses a file into a list of strings.

    Args:
        path (str): The path to a file.

    Returns:
        list[str]: A list of strings representing lines in the input file.
    """
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    return lines
