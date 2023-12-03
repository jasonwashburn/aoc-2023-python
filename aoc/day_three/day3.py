"""Main module for solving day X."""
import sys
from dataclasses import dataclass
from itertools import product

from aoc.common import parse_lines_from_file


@dataclass
class Number:
    """
    Represents a number with its value, column range, and adjacent coordinates.
    """

    value: int
    col_range: tuple[int, int]
    adjacent_coords: set | None = None


def decode_line(input_line: str) -> tuple[list[Number | None], list[int | None]]:
    """
    Decode a line of input and extract numbers and symbol indices.

    Args:
        input_line (str): The input line to decode.

    Returns:
        tuple[list[Number | None], list[int | None]]: A tuple containing two lists.
            The first list contains Number objects representing the extracted numbers.
            The second list contains tuples representing the symbol indices, where each tuple
            consists of an index and the corresponding symbol.

    """
    numbers = []
    symbol_indices: list[tuple[int, str] | None] = []
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
                symbol_indices.append((index, char))
    if in_number:
        numbers.append(
            Number(value=int(num_collector), col_range=(start_col, index + 1))
        )
    return numbers, symbol_indices


def calc_adjacent_positions(start, stop, row) -> set[tuple[int, int]]:
    """
    Calculate the adjacent positions given a start and stop position, and a row number.

    Args:
        start (int): The starting position.
        stop (int): The stopping position.
        row (int): The row number.

    Returns:
        set[tuple[int, int]]: A set of tuples representing the adjacent positions.
    """
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
        symbol_positions += [
            (row_index, symbol_index[0]) for symbol_index in symbol_indicies
        ]

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
    total = 0
    gear_positions = []
    numbers: list[Number | None] = []
    for row_index, input_line in enumerate(input_lines):
        new_numbers, symbol_indicies = decode_line(input_line)
        for number in new_numbers:
            number.adjacent_coords = calc_adjacent_positions(
                start=number.col_range[0], stop=number.col_range[1], row=row_index
            )
        numbers += new_numbers
        gear_positions += [
            (row_index, symbol_index[0])
            for symbol_index in symbol_indicies
            if symbol_index[1] == "*"
        ]

    gear_nums = {}
    for number in numbers:
        intersections = number.adjacent_coords.intersection(gear_positions)
        for coord in intersections:
            if gear_nums.get(coord):
                gear_nums[coord].append(number)
            else:
                gear_nums[coord] = [number]

    for numbers in gear_nums.values():
        if len(numbers) == 2:
            total += numbers[0].value * numbers[1].value

    return total


def main() -> None:
    """The main function."""
    input_lines = parse_lines_from_file(sys.argv[1])
    day_one_result = part_one(input_lines)
    day_two_result = part_two(input_lines)
    print(f"Day One Result: {day_one_result}")
    print(f"Day Two Result: {day_two_result}")


if __name__ == "__main__":
    main()
