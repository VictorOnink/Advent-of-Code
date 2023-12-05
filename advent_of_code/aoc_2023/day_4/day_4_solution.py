from collections import defaultdict
from typing import Dict, List

from parse import compile

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


def parse_scratch_cards(scratch_cards: PuzzleInput) -> Dict[int, Dict[str, List[str]]]:
    card_contents: Dict[int, Dict[int, List[str]]] = dict()

    scratch_card_schema = compile("Card {}: {} | {}")

    for card in scratch_cards:
        card_id, winning_numbers, card_numbers = scratch_card_schema.parse(card)
        winning_numbers = [num for num in winning_numbers.split(" ") if num]
        card_numbers = [num for num in card_numbers.split(" ") if num]
        card_contents[int(card_id)] = {"win": winning_numbers, "num": card_numbers}

    return card_contents


def get_card_point_totals(card_contents: Dict[int, Dict[str, List[str]]]):
    point_totals: List[int] = list()

    for _, contents in card_contents.items():
        number_of_winning_numbers = sum(x in contents["num"] for x in contents["win"])

        if number_of_winning_numbers == 0:
            point_totals.append(0)
        else:
            point_totals.append(2 ** (number_of_winning_numbers - 1))

    return point_totals


def get_number_of_cards(card_contents: Dict[int, Dict[str, List[str]]]):
    total_number_of_cards = defaultdict(lambda: 1)

    for card_id, contents in card_contents.items():
        number_of_card_instances = total_number_of_cards[card_id]

        number_matched_numbers = len(
            [win_num for win_num in contents["win"] if win_num in contents["num"]]
        )
        for next_cards in range(card_id + 1, card_id + 1 + number_matched_numbers):
            total_number_of_cards[next_cards] += number_of_card_instances

    return total_number_of_cards


def solution(case: str) -> None:
    scratch_cards: PuzzleInput = load_puzzle_input(Year(2023), Day(4), PuzzleCase(case))

    card_contents = parse_scratch_cards(scratch_cards)

    card_point_totals = get_card_point_totals(card_contents)

    print(f"The sum of point totals is {sum(card_point_totals)}")

    total_number_of_cards = get_number_of_cards(card_contents)

    total_cards = sum(x for x in total_number_of_cards.values())

    print(f"In the end we have ended up with {total_cards}")
