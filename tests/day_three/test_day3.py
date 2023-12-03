"""Tests for Day X."""
import pytest

from aoc.common import parse_lines_from_file
from aoc.day_three.day3 import (
    Number,
    calc_adjacent_positions,
    decode_line,
    part_one,
    part_two,
)


@pytest.mark.parametrize(
    "input_str, expected",
    [
        (
            "467..114..",
            (
                [
                    Number(value=467, col_range=(0, 3)),
                    Number(value=114, col_range=(5, 8)),
                ],
                [],
            ),
        ),
        (
            "...*......",
            (
                [],
                [(3, "*")],
            ),
        ),
        (
            "..35..633.",
            (
                [
                    Number(value=35, col_range=(2, 4)),
                    Number(value=633, col_range=(6, 9)),
                ],
                [],
            ),
        ),
        (
            "617*......",
            (
                [
                    Number(value=617, col_range=(0, 3)),
                ],
                [(3, "*")],
            ),
        ),
        (
            "...$.*..47",
            (
                [Number(value=47, col_range=(8, 10))],
                [(3, "$"), (5, "*")],
            ),
        ),
    ],
)
def test_decode_line(input_str, expected):
    """Test the decode_line function."""
    assert decode_line(input_str) == expected


@pytest.mark.parametrize(
    "start, stop, row, expected",
    [
        (
            1,
            2,
            1,
            {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)},
        ),
    ],
)
def test_calc_adjacent_positions(start, stop, row, expected) -> None:
    """Tests the calc_adjacent_positions function."""
    assert calc_adjacent_positions(start=start, stop=stop, row=row) == expected


def test_day_one():
    """Tests day one."""
    input_lines = parse_lines_from_file("aoc/day_three/example1.txt")
    assert part_one(input_lines) == 4361


def test_day_two() -> None:
    """Tests day two"""
    input_lines = parse_lines_from_file("aoc/day_three/example2.txt")
    assert part_two(input_lines) == 467835
