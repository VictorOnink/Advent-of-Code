import re

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput

CRATE_CONFIGURATION = {
    1: ["D", "H", "N", "Q", "T", "W", "V", "B"],
    2: ["D", "W", "B"],
    3: ["T", "S", "Q", "W", "J", "C"],
    4: ["F", "J", "R", "N", "Z", "T", "P"],
    5: ["G", "P", "V", "J", "M", "S", "T"],
    6: ["B", "W", "F", "T", "N"],
    7: ["B", "L", "D", "Q", "F", "H", "V", "N"],
    8: ["H", "P", "F", "R"],
    9: ["Z", "S", "M", "B", "L", "N", "P", "H"],
}


def carry_out_crate_moves(crate_moves: PuzzleInput, crate_mover: str):
    for move in crate_moves:
        print(move)
        parsed_move = [x.strip() for x in re.split("move |from |to ", move)]
        number_of_crates, target, destination = [int(x) for x in parsed_move[1:]]
        move_crates(number_of_crates, target, destination, crate_mover)

    for stack in CRATE_CONFIGURATION.keys():
        print(stack, CRATE_CONFIGURATION[stack])


def move_crates(number_of_crates: int, target: int, destination: int, crate_mover: str):
    # Moves one crate at a time, moving the top of the stack down
    if crate_mover == "crate_mover_9000":
        for _ in range(number_of_crates):
            crate_label: str = CRATE_CONFIGURATION[target].pop()
            CRATE_CONFIGURATION[destination].append(crate_label)
    # Moves multiple crates at once
    if crate_mover == "crate_mover_9001":
        crate_label: str = CRATE_CONFIGURATION[target][-number_of_crates:]
        CRATE_CONFIGURATION[destination] += crate_label
        CRATE_CONFIGURATION[target] = CRATE_CONFIGURATION[target][:-number_of_crates]


def solution(case: str):
    crate_moves = load_puzzle_input(year=Year(2022), day=Day(5), case=PuzzleCase(case))

    carry_out_crate_moves(crate_moves, "crate_mover_9000")

    carry_out_crate_moves(crate_moves, "crate_mover_9001")
