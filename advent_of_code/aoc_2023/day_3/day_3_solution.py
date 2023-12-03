from typing import List, Set, Tuple

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput

CoordinateType = Tuple[int, int]
SetCoordinatesType = Set[CoordinateType]


def get_symbol_coordinates(schematic: PuzzleInput) -> SetCoordinatesType:
    symbol_coordinates: SetCoordinatesType = set()

    for row_ind, row_str in enumerate(schematic):
        for char_ind, char in enumerate(row_str):
            if not char.isnumeric() and char != ".":
                symbol_coordinates.add((row_ind, char_ind))

    return symbol_coordinates


def get_gear_coordinates(schematic: PuzzleInput) -> SetCoordinatesType:
    gear_coordinates: SetCoordinatesType = set()

    for row_ind, row_str in enumerate(schematic):
        for char_ind, char in enumerate(row_str):
            if char == "*":
                gear_coordinates.add((row_ind, char_ind))

    return gear_coordinates


def get_surround_coordinates_symbols(
    symbol_coordinates: SetCoordinatesType, schematic_size: Tuple[int, int]
) -> Set[CoordinateType]:
    symbol_coordinates_surrounding: SetCoordinatesType = set()
    max_row, max_col = schematic_size

    for coordinate in symbol_coordinates:
        row, col = coordinate

        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                symbol_coordinates_surrounding.add(
                    (
                        max(0, min(row + drow, max_row - 1)),
                        max(0, min(col + dcol, max_col - 1)),
                    )
                )
    return symbol_coordinates_surrounding


def get_part_number_coordinates(
    schematic: PuzzleInput,
) -> Tuple[List[str], List[SetCoordinatesType]]:
    part_numbers: List[str] = list()
    part_number_coordinates: List[SetCoordinatesType] = list()

    number_str = ""
    coordinate_tracker: SetCoordinatesType = set()

    for row_ind, row_str in enumerate(schematic):
        for char_ind, char in enumerate(row_str):
            if char.isnumeric():
                number_str += char
                coordinate_tracker.add((row_ind, char_ind))
            elif number_str != "":
                part_numbers.append(number_str)
                part_number_coordinates.append(coordinate_tracker)
                number_str = ""
                coordinate_tracker = set()

    return (part_numbers, part_number_coordinates)


def get_adjacent_parts(
    part_numbers: List[str],
    part_number_coordinates: List[SetCoordinatesType],
    symbol_coordinates_surrounding: SetCoordinatesType,
) -> List[str]:
    adjacent_parts: List[str] = list()

    for part_number, part_coordinates in zip(part_numbers, part_number_coordinates):
        if part_coordinates.intersection(symbol_coordinates_surrounding):
            adjacent_parts.append(part_number)

    return adjacent_parts


def get_gear_ratios(
    gear_coordinates: SetCoordinatesType,
    part_numbers: List[str],
    part_number_coordinates: List[SetCoordinatesType],
    schematic_size: Tuple[int, int],
    n: int = 2,
) -> List[int]:

    gear_ratios: List[int] = list()

    for gear_coord in gear_coordinates:
        adjacent_coord = get_surround_coordinates_symbols({gear_coord}, schematic_size)

        adjacent_parts = get_adjacent_parts(
            part_numbers, part_number_coordinates, adjacent_coord
        )

        if len(adjacent_parts) == n:
            gear_ratios.append(int(adjacent_parts[0]) * int(adjacent_parts[1]))

    return gear_ratios


def solution(case: str) -> None:
    schematic: PuzzleInput = load_puzzle_input(Year(2023), Day(3), PuzzleCase(case))

    schematic_size: Tuple[int, int] = (len(schematic), len(schematic[0]))

    symbol_coordinates = get_symbol_coordinates(schematic)

    symbol_coordinates_surrounding = get_surround_coordinates_symbols(
        symbol_coordinates, schematic_size
    )

    part_numbers, part_number_coordinates = get_part_number_coordinates(schematic)

    adjacent_parts = get_adjacent_parts(
        part_numbers, part_number_coordinates, symbol_coordinates_surrounding
    )

    sum_adjacent_parts = sum(int(part_number) for part_number in adjacent_parts)

    print(f"The sum of all parts adjacent to a symbol is {sum_adjacent_parts}")

    gear_coordinates = get_gear_coordinates(schematic)

    gear_ratios = get_gear_ratios(
        gear_coordinates,
        part_numbers,
        part_number_coordinates,
        schematic_size,
    )

    sum_gear_ratios = sum(gear_ratios)

    print(f"The sum of gear ratios is {sum_gear_ratios}")
