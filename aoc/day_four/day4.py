"""Main module for solving day X."""
import sys

from aoc.common import parse_lines_from_file


def parse_input_line(input_line: str) -> tuple[set[int], set[int]]:
    """
    Parses an input line and returns a tuple of two sets.

    The winning_nums and ticket_nums are sets of integers.

    Args:
        input_line (str): The input line to parse.

    Returns:
        tuple[set[int], set[int]]: A tuple containing the winning_nums set and ticket_nums set.
    """
    _, numbers = input_line.strip().split(":")
    winning_nums, ticket_nums = numbers.strip().split("|")
    winning_nums = {int(num) for num in winning_nums.strip().split(" ") if num != ""}
    ticket_nums = {int(num) for num in ticket_nums.strip().split(" ") if num != ""}

    return (winning_nums, ticket_nums)


def score_line(winning_nums: set[int], ticket_nums: set[int]) -> int:
    """
    Calculate the score for a line of numbers based on the winning numbers.

    Args:
        winning_nums (set[int]): The set of winning numbers.
        ticket_nums (set[int]): The set of numbers on the ticket.

    Returns:
        int: The score for the line of numbers.
    """
    matches = len(winning_nums.intersection(ticket_nums))
    if matches == 0:
        return 0
    elif matches == 1:
        return 1
    else:
        return 1 * (2 ** (matches - 1))


def part_one(input_lines: list[str]) -> int:
    """Solves part 1.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    total = 0
    for line in input_lines:
        winning_nums, ticket_nums = parse_input_line(line)
        total += score_line(winning_nums=winning_nums, ticket_nums=ticket_nums)

    return total


def part_two(input_lines: list[str]) -> int:
    """Solves part 2.

    Args:
        input_lines (list[str]): The puzzle input as a list of strings.

    Returns:
        int: The solution.
    """
    total = 0
    cards = {
        card_num: {"quantity": 1, "winning_numbers": 0}
        for card_num in range(1, len(input_lines) + 1)
    }

    for current_card_num, line in enumerate(input_lines, start=1):
        winning_nums, ticket_nums = parse_input_line(line)
        intersection = winning_nums.intersection(ticket_nums)
        num_wins = len(intersection)
        cards[current_card_num]["winning_numbers"] = num_wins
        quantity_current_card = cards[current_card_num]["quantity"]
        for i in range(1, num_wins + 1):
            if current_card_num + i <= len(input_lines):
                cards[current_card_num + i]["quantity"] += 1 * quantity_current_card

    for card_info in cards.values():
        total += card_info["quantity"]

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
