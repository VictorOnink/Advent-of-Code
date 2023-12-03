from collections import defaultdict
from typing import Dict, Iterable, List, Tuple

from parse import compile

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput

CoordinateType = Tuple[int, int]


def get_vent_line_coordinates_non_diagonal(
    inputs: PuzzleInput,
) -> List[List[CoordinateType]]:
    vent_line_coordinates: List[List[CoordinateType]] = list()

    string_format = compile("{:d},{:d} -> {:d},{:d}")
    for line in inputs:
        x1, y1, x2, y2 = string_format.parse(line)
        if (x1 != x2) & (y1 != y2):
            continue

        x_step = _get_range(x1, x2)
        y_step = _get_range(y1, y2)

        vent_line = [(x, y) for x in x_step for y in y_step]
        vent_line_coordinates.append(vent_line)

    return vent_line_coordinates


def get_vent_line_coordinates_diagonal(
    inputs: PuzzleInput,
) -> List[List[CoordinateType]]:
    vent_line_coordinates: List[List[CoordinateType]] = list()

    string_format = compile("{:d},{:d} -> {:d},{:d}")
    for line in inputs:
        x1, y1, x2, y2 = string_format.parse(line)
        if (x1 == x2) | (y1 == y2):
            continue

        x_step = _get_range(x1, x2)
        y_step = _get_range(y1, y2)

        vent_line = [(x, y) for x, y in zip(x_step, y_step)]

        vent_line_coordinates.append(vent_line)

    return vent_line_coordinates


def _get_range(a: int, b: int) -> Iterable:
    if a == b:
        return [a]
    elif a > b:
        return range(a, b - 1, -1)
    else:
        return range(a, b + 1)


def count_vents(
    vent_line_coordinates: List[List[CoordinateType]],
) -> Dict[CoordinateType, int]:
    vent_counter = defaultdict(int)

    for vent_line in vent_line_coordinates:
        for coordinates in vent_line:
            vent_counter[coordinates] += 1

    return vent_counter


def solution(case: str) -> None:
    inputs: PuzzleInput = load_puzzle_input(Year(2021), Day(5), PuzzleCase(case))

    vent_line_coordinates_non_diagonal = get_vent_line_coordinates_non_diagonal(inputs)

    vent_counts = count_vents(vent_line_coordinates_non_diagonal)

    number_of_high_risk_coordinates = sum(
        1 for vent_count in vent_counts.values() if vent_count > 1
    )

    print(f"There are {number_of_high_risk_coordinates} high risk coordinates")

    vent_line_coordinates_diagonal = get_vent_line_coordinates_diagonal(inputs)

    all_vent_counts = count_vents(
        vent_line_coordinates_non_diagonal + vent_line_coordinates_diagonal
    )

    number_of_high_risk_coordinates = sum(
        1 for vent_count in all_vent_counts.values() if vent_count > 1
    )

    print(
        f"There are {number_of_high_risk_coordinates} high risk coordinates including diagonal vent lines"
    )
