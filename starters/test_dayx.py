"""Tests for Day X."""
import pytest

from aoc.common import parse_lines_from_file
from aoc.day_two.day2 import part_one, part_two


@pytest.mark.skip("Not Implemented")
def test_part_one():
    """Tests day one."""
    input_lines = parse_lines_from_file("aoc/day_x/example1.txt")
    assert part_one(input_lines) == 13


@pytest.mark.skip("Not Implemented")
def test_part_two() -> None:
    """Tests day two"""
    input_lines = parse_lines_from_file("aoc/day_x/example2.txt")
    assert part_two(input_lines) == 467835
