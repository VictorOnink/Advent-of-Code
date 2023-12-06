from collections import defaultdict
from typing import Dict, List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


def get_winning_ways(
    times: List[int], distance: List[int], charge_speed: int = 1
) -> Dict[int, int]:
    winning_combos = defaultdict(int)

    for race_id in range(len(times)):
        for charge_time in range(times[race_id]):
            v_boat = charge_time * charge_speed
            remaining_time = times[race_id] - charge_time
            if distance[race_id] < v_boat * remaining_time:
                winning_combos[race_id] += 1

    return winning_combos


def solution(case: str) -> None:
    raw_input: PuzzleInput = load_puzzle_input(Year(2023), Day(6), PuzzleCase(case))

    times: List[int] = [int(t) for t in raw_input[0].split(":")[1].split(" ") if t]
    distance: List[int] = [int(x) for x in raw_input[1].split(":")[1].split(" ") if x]

    winning_combos = get_winning_ways(times, distance)

    multiple_ways = 1
    for combos in winning_combos.values():
        multiple_ways *= combos

    print(f"The product of ways to win the race is {multiple_ways}")

    times_p2: List[int] = [int(raw_input[0].split(":")[1].replace(" ", ""))]
    distance_p2: List[int] = [int(raw_input[1].split(":")[1].replace(" ", ""))]

    winning_combos_p2 = get_winning_ways(times_p2, distance_p2)

    multiple_ways_p2 = 1
    for combos in winning_combos_p2.values():
        multiple_ways_p2 *= combos

    print(f"The product of ways to win the race is {multiple_ways_p2}")
