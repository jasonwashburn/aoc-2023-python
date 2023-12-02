"""Tests for Day X."""
import pytest

from aoc.day_two.day2 import part_one, part_two


@pytest.mark.parametrize(
    "input_lines, expected_output", [(["one", "two", "three"], 123)]
)
@pytest.mark.skip("Not Implemented")
def test_day_one(input_lines, expected_output):
    """Tests day one."""
    assert part_one(input_lines) == expected_output


@pytest.mark.parametrize(
    "input_lines, expected_output", [(["one", "two", "three"], 123)]
)
@pytest.mark.skip("Not Implemented")
def test_day_two(input_lines, expected_output) -> None:
    """Tests day two"""
    assert part_two(input_lines) == expected_output
