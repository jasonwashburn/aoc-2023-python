"""Main module for solving day 2"""
import sys

from aoc.common import parse_lines_from_file

POSSIBLE_COLORS = {"red": 12, "green": 13, "blue": 14}


def parse_grab(grab_str: str) -> dict[str, int]:
    """Parses a grab string into a dict of block color counts.

    Example: "3 blue, 4 red" -> {"red": 4, "green": 0, "blue": 3}

    Args:
        grab_str (str): a string representing color block counts

    Returns:
        dict[str, int]: a dict of color counts
    """
    result = {"red": 0, "green": 0, "blue": 0}
    color_counts = grab_str.strip().split(",")
    for color_count in color_counts:
        count, color = color_count.strip().split(" ")
        result[color] = int(count.strip())
    return result


def parse_game_line(input_line: str) -> list[dict[str, int]]:
    """Parses an input line into a list of cube grabs as dictionaries.

    Example: [
        {"red": 4, "green": 0, "blue": 3},
        {"red": 1, "green": 2, "blue": 6},
        {"red": 0, "green": 2, "blue": 0},
    ]

    Args:
        input_line (str): an input line string containing a single game of grabs

    Returns:
        list[dict[str, int]]: a list of dictionaries representing each grab counts
    """
    result = []
    _, grabs = input_line.strip().split(":")
    for grab in grabs.strip().split(";"):
        result.append(parse_grab(grab))
    return result


def is_possible_grab(grab: dict[str, int], max_colors: dict[str, int]):
    """
    Check if it is possible to grab the given colors based on the maximum allowed colors.

    Args:
        grab (dict[str, int]): A dictionary representing the colors to grab and their
            respective counts.
        max_colors (dict[str, int]): A dictionary representing the maximum allowed
            colors and their respective counts.

    Returns:
        bool: True if it is possible to grab the colors, False otherwise.
    """
    for color, count in grab.items():
        if count > max_colors[color]:
            return False
    return True


def find_min_cubes_required(grabs: list[dict[str, int]]) -> dict[str, int]:
    """
    Finds the minimum number of cubes required for each color based on the given grabs.

    Args:
        grabs (list[dict[str, int]]): A list of dictionaries representing the grabs made
            for each color. Each dictionary contains the color as the key and the count
            of cubes grabbed as the value.

    Returns:
        dict[str, int]: A dictionary containing the minimum number of cubes required for
            each color. The keys are the color names ("red", "green", "blue") and the
            values are the corresponding counts.
    """
    min_required = {"red": 0, "green": 0, "blue": 0}
    for grab in grabs:
        for color, count in grab.items():
            if count > min_required[color]:
                min_required[color] = count

    return min_required


def part_one(input_lines: list[str]) -> int:
    """Solves part 1.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    total = 0

    for index, line in enumerate(input_lines):
        game_num = index + 1
        possible_game = True
        game = parse_game_line(line)
        for grab in game:
            if not is_possible_grab(grab=grab, max_colors=POSSIBLE_COLORS):
                possible_game = False
                break
        if possible_game:
            total += game_num
    return total


def part_two(input_lines: list[str]) -> int:
    """Solves part 2.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """

    total = 0

    for line in input_lines:
        grabs = parse_game_line(line)
        min_cubes = find_min_cubes_required(grabs)
        game_power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        total += game_power
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
