from typing import Tuple

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


def get_direction_multiplier(direction: str) -> int:
    direction_multiplier = {"forward": 1, "down": 1, "up": -1}
    return direction_multiplier[direction]


def get_coordinates(
    directions: PuzzleInput, start_z: int = 0, start_x: int = 0
) -> Tuple[int, int]:
    x_sub, z_sub = start_x, start_z

    for stage in directions:
        movement, steps = stage.split()
        if movement in ["forward"]:
            x_sub += int(steps) * get_direction_multiplier(movement)
        elif movement in ["up", "down"]:
            z_sub += int(steps) * get_direction_multiplier(movement)

    return (x_sub, z_sub)


def get_coordinates_with_aim(
    directions: PuzzleInput, start_z: int = 0, start_x: int = 0, start_aim: int = 0
) -> Tuple[int, int]:
    x_sub, z_sub, aim_sub = start_x, start_z, start_aim

    for stage in directions:
        movement, steps = stage.split()
        if movement in ["forward"]:
            x_sub += int(steps) * get_direction_multiplier(movement)
            z_sub += aim_sub * int(steps) * get_direction_multiplier(movement)
        elif movement in ["up", "down"]:
            aim_sub += int(steps) * get_direction_multiplier(movement)

    return (x_sub, z_sub)


def solution(case: str) -> None:
    directions: PuzzleInput = load_puzzle_input(Year(2021), Day(2), PuzzleCase(case))

    x_sub, z_sub = get_coordinates(directions)

    print(f"The product of the submarine coordinates is {x_sub * z_sub}")

    x_sub, z_sub = get_coordinates_with_aim(directions)

    print(f"The product of the submarine coordinates wtih aim is {x_sub * z_sub}")

