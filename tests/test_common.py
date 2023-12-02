"""Tests for aoc common functions."""
from aoc.common import parse_lines_from_file


def test_parse_file():
    """Tests parse_file."""
    expected = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert parse_lines_from_file("tests/example.txt") == expected
