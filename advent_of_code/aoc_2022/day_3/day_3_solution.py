import string
from typing import List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


def get_priority_score(Item: str) -> int:
    return string.ascii_letters.find(Item) + 1


def split_bag_into_compartments(rucksack_contents: PuzzleInput) -> List[str]:
    rucksack_compartments = []
    for rucksack in rucksack_contents:
        number_of_items = len(rucksack)
        rucksack_compartments.append(
            [rucksack[: (number_of_items // 2)], rucksack[(number_of_items // 2) :]]
        )
    return rucksack_compartments


def get_priority_scores(rucksack_compartments: List[str]) -> None:
    total_priority_score: int = 0

    for rucksack in rucksack_compartments:
        first_comp, second_comp = rucksack
        for Item in set(first_comp):
            if Item in second_comp:
                total_priority_score += get_priority_score(Item)

    print(f"The total priority score is {total_priority_score}")


def get_priority_scores_per_group_elves(rucksack_contents: List[str]) -> None:
    elves_per_group: int = 3
    number_of_groups: int = len(rucksack_contents) // elves_per_group

    total_priority_score: int = 0

    for group_id in range(number_of_groups):
        elf_1: str = rucksack_contents[group_id * elves_per_group]
        elf_2: str = rucksack_contents[group_id * elves_per_group + 1]
        elf_3: str = rucksack_contents[group_id * elves_per_group + 2]

        for Item in set(elf_1):
            if (Item in elf_2) & (Item in elf_3):
                total_priority_score += get_priority_score(Item)
                break

    print(f"The total priority score is {total_priority_score}")


def solution(case: str):
    rucksack_contents = load_puzzle_input(
        year=Year(2022), day=Day(3), case=PuzzleCase(case)
    )

    rucksack_compartments = split_bag_into_compartments(rucksack_contents)

    get_priority_scores(rucksack_compartments)

    get_priority_scores_per_group_elves(rucksack_contents)
