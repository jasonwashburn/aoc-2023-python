import pytest

from aoc.day_one.day1 import (
    extract_digits,
    part_one,
    part_two,
    replace_words_with_numbers,
)


@pytest.mark.parametrize(
    "input, expected",
    [("1abc2", 12), ("pqr3stu8vwx", 38), ("abc1def2gh3eg4", 14)],
)
def test_extract_digits(input, expected):
    assert extract_digits(input) == expected


def test_part_one():
    assert part_one(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142


@pytest.mark.parametrize(
    "input, expected",
    [
        ("two1nine", "t2o1n9ne"),
        ("eightwothree", "ei8ht2othr3e"),
        ("abcone2threexyz", "abco1e2thr3exyz"),
        ("xtwone3four", "xt2o1e3f4ur"),
        ("4nineeightseven2", "4n9neei8htse7en2"),
        ("zoneight234", "zo1ei8ht234"),
        ("7pqrstsixteen", "7pqrsts6xteen"),
    ],
)
def test_replace_words_with_numbers(input, expected) -> None:
    assert replace_words_with_numbers(input) == expected


def test_part_two() -> None:
    assert (
        part_two(
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )
        == 281
    )
