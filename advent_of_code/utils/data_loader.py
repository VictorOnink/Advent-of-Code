# This module contains code for importing test and puzzle inputs
from enum import Enum
from pathlib import Path
from typing import List

DATA_DIREC = Path(__file__).parents[2].joinpath("data")


class Year(Enum):
    """Enum for puzzle years"""

    YEAR_2023: int = 2023
    YEAR_2022: int = 2022
    YEAR_2021: int = 2021
    YEAR_2020: int = 2020
    YEAR_2019: int = 2019
    YEAR_2018: int = 2018
    YEAR_2017: int = 2017
    YEAR_2016: int = 2016
    YEAR_2015: int = 2015


class Day(Enum):
    """Enum for puzzle days"""

    DAY_1: int = 1
    DAY_2: int = 2
    DAY_3: int = 3
    DAY_4: int = 4
    DAY_5: int = 5
    DAY_6: int = 6
    DAY_7: int = 7
    DAY_8: int = 8
    DAY_9: int = 9
    DAY_10: int = 10
    DAY_11: int = 11
    DAY_12: int = 12
    DAY_13: int = 13
    DAY_14: int = 14
    DAY_15: int = 15
    DAY_16: int = 16
    DAY_17: int = 17
    DAY_18: int = 18
    DAY_19: int = 19
    DAY_20: int = 20
    DAY_21: int = 21
    DAY_22: int = 22
    DAY_23: int = 23
    DAY_24: int = 24
    DAY_25: int = 25


class PuzzleCase(Enum):
    """Enum with the two cases for puzzles"""

    TEST: str = "test"
    PUZZLE: str = "puzzle"


def load_puzzle_input(
    year: Year, day: Day, case: PuzzleCase, with_strip: bool = True
) -> List[str]:
    """
    Util function for loading in puzzle input from text files.

    Args:
        year (Year): Year of the puzzle
        day (Day): Day of the puzzle for the given year
        case (PuzzleCase): Whether this is the puzzle or test input
        with_strip (Bool): if True, apply strip to the lines in the txt file

    Returns:
        PuzzleInput: puzzle input as a list of strings, where each string
                     corresponds to one line of the input
    """
    file_name = DATA_DIREC.joinpath(
        f"aoc_{year.value}/day_{day.value}/{case.value}_input.txt"
    )

    with open(file_name) as f:
        if with_strip:
            lines = [x.strip() for x in f.readlines()]
        else:
            lines = [x for x in f.readlines()]

    return lines
