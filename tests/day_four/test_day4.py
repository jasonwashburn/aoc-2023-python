"""Tests for Day X."""
from aoc.common import parse_lines_from_file
from aoc.day_four.day4 import parse_input_line, part_one, part_two, score_line


def test_parse_input_line() -> None:
    """Tests parse_input_line."""
    input_str = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    expected = ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
    assert parse_input_line(input_str) == expected


def test_score_line() -> None:
    """Tests score_line."""
    winning_nums = {41, 48, 83, 86, 17}
    ticket_nums = {83, 86, 6, 31, 17, 9, 48, 53}
    expected = 8

    assert score_line(winning_nums=winning_nums, ticket_nums=ticket_nums) == expected


def test_part_one():
    """Tests day one."""
    input_lines = parse_lines_from_file("aoc/day_four/example1.txt")
    assert part_one(input_lines) == 13


def test_part_two() -> None:
    """Tests day two"""
    input_lines = parse_lines_from_file("aoc/day_four/example2.txt")
    assert part_two(input_lines) == 30
