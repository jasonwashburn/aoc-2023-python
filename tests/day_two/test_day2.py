"""Tests for day 2."""
import pytest

from aoc.common import parse_lines_from_file
from aoc.day_two.day2 import (
    find_min_cubes_required,
    is_possible_grab,
    parse_game_line,
    parse_grab,
    part_one,
    part_two,
)


def test_parse_game_line() -> None:
    """Tests parse_game_line."""
    expected = [
        {"red": 4, "green": 0, "blue": 3},
        {"red": 1, "green": 2, "blue": 6},
        {"red": 0, "green": 2, "blue": 0},
    ]
    assert (
        parse_game_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        == expected
    )


@pytest.mark.parametrize(
    "grab, max_colors, expected",
    [
        ({"red": 1, "green": 2, "blue": 3}, {"red": 1, "green": 2, "blue": 3}, True),
        ({"red": 2, "green": 2, "blue": 3}, {"red": 1, "green": 2, "blue": 3}, False),
        ({"red": 1, "green": 3, "blue": 3}, {"red": 1, "green": 2, "blue": 3}, False),
    ],
)
def test_is_possible_grab(grab, max_colors, expected) -> None:
    """Tests is_possible_grab."""
    assert is_possible_grab(grab, max_colors) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("3 blue, 4 red", {"red": 4, "green": 0, "blue": 3}),
        ("3 red, 4 blue", {"red": 3, "green": 0, "blue": 4}),
        ("3 green, 4 red", {"red": 4, "green": 3, "blue": 0}),
    ],
)
def test_parse_grab(input_str, expected) -> None:
    """Tests parse grab."""
    assert parse_grab(input_str) == expected


@pytest.mark.parametrize(
    "grabs, expected",
    [
        (
            [
                {"red": 4, "green": 0, "blue": 3},
                {"red": 1, "green": 2, "blue": 6},
                {"red": 0, "green": 2, "blue": 0},
            ],
            {"red": 4, "green": 2, "blue": 6},
        )
    ],
)
def test_find_min_cubes_required(grabs, expected) -> None:
    """Tests find_min_cubes_required."""
    assert find_min_cubes_required(grabs) == expected


def test_part_one():
    """Tests part one."""
    example = parse_lines_from_file("aoc/day_two/example1.txt")
    assert part_one(example) == 8


def test_part_two() -> None:
    """Tests part two"""
    example = parse_lines_from_file("aoc/day_two/example2.txt")
    assert part_two(example) == 2286
