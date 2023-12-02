from typing import Dict, List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput

SPELLED_MAPPING: Dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_numerical_char(input_string: str) -> str:
    for char in input_string:
        if char.isnumeric():
            return char


def find_calibration_values(document: PuzzleInput) -> List[str]:
    values: List[str] = list()

    for row in document:
        calibration_value = find_numerical_char(row) + find_numerical_char(row[::-1])
        values.append(calibration_value)

    return values


def get_all_numbers_from_row(row: str) -> List[str]:
    all_numbers: List[str] = list()
    for char_index in range(len(row)):
        if row[char_index].isnumeric():
            all_numbers.append(row[char_index])
        for spelled_digit, digit in SPELLED_MAPPING.items():
            try:
                if row[char_index:].index(spelled_digit) == 0:
                    all_numbers.append(digit)
            except ValueError:
                continue
    return all_numbers


def find_calibration_values_spelled(document: PuzzleInput) -> List[str]:
    values: List[str] = list()

    for row in document:
        all_numbers = get_all_numbers_from_row(row)

        values.append(all_numbers[0] + all_numbers[-1])

    return values


def solution(case: str) -> None:
    document: PuzzleInput = load_puzzle_input(Year(2023), Day(1), PuzzleCase(case))

    calibration_values = find_calibration_values(document)

    sum_calibration_values = sum(int(val) for val in calibration_values)

    print(f"The sum of calibration values is {sum_calibration_values}")

    if case == "test":
        document = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]

    spelled_calibration_values = find_calibration_values_spelled(document)

    sum_calibration_values = sum(int(val) for val in spelled_calibration_values)

    print(f"The sum of calibration values with spelling is {sum_calibration_values}")
