"""Tests for day 2."""
import pytest

from aoc.day_two.day2 import part_one, part_two


@pytest.mark.parametrize(
    "input_lines, expected_output", [(["one", "two", "three"], 123)]
)
@pytest.mark.skip("Not Implemented")
def test_part_one(input_lines, expected_output):
    """Tests part one."""
    assert part_one(input_lines) == expected_output


@pytest.mark.parametrize(
    "input_lines, expected_output", [(["one", "two", "three"], 123)]
)
@pytest.mark.skip("Not Implemented")
def test_part_two(input_lines, expected_output) -> None:
    """Tests part two"""
    assert part_two(input_lines) == expected_output
