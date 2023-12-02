"""Main module for solving day 1"""
import sys

from aoc.common import parse_lines_from_file


def extract_digits(input_string: str) -> int:
    """Extracts the first and last digit from a string, concatenates them, and returns
    the resulting new number. i.e. '1abc2' becomes 12.

    Args:
        input_string (str): a string of characters

    Returns:
        int: the resulting number
    """
    digits = [char for char in input_string if char.isdecimal()]
    result = int(digits[0] + digits[-1])
    return result


def replace_words_with_numbers(input_string: str) -> str:
    """Replaces words representing numbers 1 thru 9 with a new string including the
    numeric representation of the word. This is done to preserve additional words
    created using overlapping characters. i.e. sevenine.

    Args:
        input_string (str): a string of characters

    Returns:
        str: a string of characters containing new digits inside spelled out numbers.
    """
    lookup = {
        "one": "o1e",
        "two": "t2o",
        "three": "thr3e",
        "four": "f4ur",
        "five": "f5ve",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ht",
        "nine": "n9ne",
    }
    result = input_string
    for word, replacement in lookup.items():
        result = result.replace(word, replacement)

    return result


def part_one(input_lines: list[str]) -> int:
    """Solves day 1.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    digits = [extract_digits(line) for line in input_lines]
    return sum(digits)


def part_two(input_lines: list[str]) -> int:
    """Solves day 2.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    digits = []
    for line in input_lines:
        replaced_line = replace_words_with_numbers(line)
        digit = extract_digits(replaced_line)
        digits.append(digit)
    return sum(digits)


def main() -> None:
    """The main function."""
    input_lines = parse_lines_from_file(sys.argv[1])
    day_one_result = part_one(input_lines)
    day_two_result = part_two(input_lines)
    print(f"Day One Result: {day_one_result}")
    print(f"Day Two Result: {day_two_result}")


if __name__ == "__main__":
    main()
