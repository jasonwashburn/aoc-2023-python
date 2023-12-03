"""Main module for solving day X."""
import sys
from dataclasses import dataclass
from itertools import product

from aoc.common import parse_lines_from_file


@dataclass
class Number:
    value: int
    col_range: tuple[int, int]
    adjacent_coords: set | None = None


def decode_line(input_line: str) -> tuple[list[Number | None], list[int | None]]:
    numbers = []
    symbol_indices = []
    in_number = False
    num_collector = ""
    index = 0
    for index, char in enumerate(input_line):
        if char.isdigit():
            if not in_number:
                start_col = index
                in_number = True
            num_collector += char

        else:
            if in_number:
                numbers.append(
                    Number(
                        value=int(num_collector),
                        col_range=(start_col, index),
                    )
                )
                in_number = False
                start_col = None
                num_collector = ""

            if char != ".":
                symbol_indices.append(index)
    if in_number:
        numbers.append(
            Number(value=int(num_collector), col_range=(start_col, index + 1))
        )
    return numbers, symbol_indices


def calc_adjacent_positions(start, stop, row) -> set[tuple[int, int]]:
    adjacent_coords = set(product(range(row - 1, row + 2), range(start - 1, stop + 1)))
    return adjacent_coords


def part_one(input_lines: list[str]) -> int:
    """Solves part 1.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    total = 0
    symbol_positions = []
    numbers: list[Number | None] = []
    for row_index, input_line in enumerate(input_lines):
        new_numbers, symbol_indicies = decode_line(input_line)
        for number in new_numbers:
            number.adjacent_coords = calc_adjacent_positions(
                start=number.col_range[0], stop=number.col_range[1], row=row_index
            )
        numbers += new_numbers
        symbol_positions += [(row_index, index) for index in symbol_indicies]

    for number in numbers:
        if number.adjacent_coords.isdisjoint(symbol_positions):
            continue

        total += number.value

    return total


def part_two(input_lines: list[str]) -> int:
    """Solves part 2.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    print(input_lines)
    return len(input_lines)


def main() -> None:
    """The main function."""
    input_lines = parse_lines_from_file(sys.argv[1])
    day_one_result = part_one(input_lines)
    day_two_result = part_two(input_lines)
    print(f"Day One Result: {day_one_result}")
    print(f"Day Two Result: {day_two_result}")


if __name__ == "__main__":
    main()
