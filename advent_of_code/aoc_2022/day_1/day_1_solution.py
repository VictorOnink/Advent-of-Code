from typing import Dict, List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput

ElfPacks = Dict[int, Dict[str, List[int]]]


def split_lines_to_elves(calorie_list: PuzzleInput) -> ElfPacks:

    elf_pack: ElfPacks = {0: {"calories": [], "total": []}}
    elf_index: int = 0

    for calorie_item in calorie_list:
        if calorie_item != "\n":
            elf_pack[elf_index]["calories"].append(int(calorie_item.strip("\n")))
        else:
            elf_pack[elf_index]["total"] = sum(elf_pack[elf_index]["calories"])
            elf_index += 1
            elf_pack[elf_index] = {"calories": [], "total": []}

    # Making sure we get the sum for the last elf too
    elf_pack[elf_index]["total"] = sum(elf_pack[elf_index]["calories"])

    return elf_pack


def get_n_elves_with_largest_packs(N: int, elf_pack: ElfPacks) -> None:
    total_calories_per_pack: List[int] = []

    for elf_calories in elf_pack.values():
        total_calories_per_pack.append(elf_calories["total"])

    total_calories_per_pack.sort()

    print(f"The elves with the {N} highest calories carry:\n")
    for calories in total_calories_per_pack[-N:]:
        print(f"\t{calories} calories \n")
    print(
        f"In total, these {N} elves carry {sum(total_calories_per_pack[-N:])} calories"
    )


def solution() -> None:
    calorie_list: PuzzleInput = load_puzzle_input(
        year=Year(2022), day=Day(1), case=PuzzleCase("puzzle"), with_strip=False
    )

    elf_pack = split_lines_to_elves(calorie_list)

    get_n_elves_with_largest_packs(1, elf_pack)
    get_n_elves_with_largest_packs(3, elf_pack)
