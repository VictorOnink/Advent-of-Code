from typing import List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


def depth_increase_counter(depths: PuzzleInput) -> None:
    increase_depth: int = 0

    for z in range(1, len(depths)):
        if depths[z] > depths[z - 1]:
            increase_depth += 1
    print(f"The depth has increased {increase_depth} times")


def calculate_sliding_window_depth_sum(
    depths: PuzzleInput, window_size: int = 3
) -> List[int]:
    sliding_depth_sum = [
        sum(depths[z : (z + window_size)])
        for z in range(0, len(depths) - window_size + 1)
    ]
    return sliding_depth_sum


def solution(case: str):
    depth_measurements: PuzzleInput = load_puzzle_input(
        Year(2021), Day(1), PuzzleCase(case)
    )

    depth_measurements = [int(z) for z in depth_measurements]

    depth_increase_counter(depth_measurements)

    sliding_depth = calculate_sliding_window_depth_sum(depth_measurements)

    depth_increase_counter(sliding_depth)
