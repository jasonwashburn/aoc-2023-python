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
    result = []
    _, grabs = input_line.strip().split(":")
    for grab in grabs.strip().split(";"):
        result.append(parse_grab(grab))
    return result


def sum_colors(color_counts: list[dict[str, int]]) -> dict[str, int]:
    result = {"red": 0, "green": 0, "blue": 0}
    for color_count in color_counts:
        for color, count in color_count.items():
            result[color] += count

    return result


def is_possible_grab(grab: dict[str, int], max_colors: dict[str, int]):
    for color, count in grab.items():
        if count > max_colors[color]:
            return False
    return True


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
