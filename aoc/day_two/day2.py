"""Main module for solving day 2"""
import sys

from aoc.common import parse_lines_from_file


def part_one(input_lines: list[str]) -> int:
    """Solves part 1.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    ...


def part_two(input_lines: list[str]) -> int:
    """Solves part 2.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    ...


def main() -> None:
    """The main function."""
    input_lines = parse_lines_from_file(sys.argv[1])
    day_one_result = part_one(input_lines)
    day_two_result = part_two(input_lines)
    print(f"Day One Result: {day_one_result}")
    print(f"Day Two Result: {day_two_result}")


if __name__ == "__main__":
    main()
