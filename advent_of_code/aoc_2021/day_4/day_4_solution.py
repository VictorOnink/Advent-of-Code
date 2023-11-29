from typing import Dict, List, Set, Tuple

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


class BingoCard:
    def __init__(self, rows: List[str], bingo_dim: int = 5) -> None:
        self.rows = rows
        self.bingo_dim = bingo_dim
        self.latest_move = None

        self._initialize_bingo_card()

    def _initialize_bingo_card(self) -> None:
        self.card_number_set: Set[str] = set()
        self.bingo_card: Dict[Tuple[int, int], str] = {}
        self.masked_cells: Set[Tuple[int, int]] = set()

        for row in range(self.bingo_dim):
            filter_row = [x for x in self.rows[row].split(" ") if x]
            for col, value in enumerate(filter_row):
                self.card_number_set.add(value)
                self.bingo_card[(row, col)] = value

    def play_bingo_number(self, value: str) -> None:
        self.latest_move = value
        if value in self.card_number_set:
            card_position = self._get_card_position(value)
            self.masked_cells.add(card_position)

        return self

    def check_for_bingo(self) -> bool:
        if self._check_bingo_row() | self._check_bingo_column():
            return True
        return False

    def _get_card_position(self, value: str) -> Tuple[int, int]:
        for position, card_value in self.bingo_card.items():
            if card_value == value:
                return position

    def _check_bingo_row(self) -> bool:
        for row in range(self.bingo_dim):
            row_points = set((row, col) for col in range(self.bingo_dim))

            overlap_masked = row_points & self.masked_cells

            if len(overlap_masked) == self.bingo_dim:
                return True
        return False

    def _check_bingo_column(self) -> bool:
        for col in range(self.bingo_dim):
            col_points = set((row, col) for row in range(self.bingo_dim))

            overlap_masked = col_points & self.masked_cells

            if len(overlap_masked) == self.bingo_dim:
                return True
        return False

    def get_score(self) -> int:
        unmasked_sum: int = 0

        for position, position_value in self.bingo_card.items():
            if position not in self.masked_cells:
                unmasked_sum += int(position_value)

        score = int(self.latest_move) * unmasked_sum

        return score


def get_bingo_cards(inputs: PuzzleInput, bingo_dim: int = 5) -> List[BingoCard]:
    # discard the first two rows of inputs since these are the random
    # numbers and an empty row
    raw_bingo_cards = inputs[2:]

    bingo_cards: List[BingoCard] = []

    for ind in range(len(raw_bingo_cards) // (bingo_dim + 1) + 1):
        card_rows = raw_bingo_cards[
            ind * (bingo_dim + 1) : ind * (bingo_dim + 1) + bingo_dim
        ]
        bingo_cards.append(BingoCard(rows=card_rows))

    return bingo_cards


def run_clean_bingo_game(
    random_numbers: List[str], bingo_cards: List[BingoCard]
) -> BingoCard:
    number_index: int = 0

    we_have_a_bingo = False
    winning_card: BingoCard | None = None

    while not we_have_a_bingo:
        bingo_number = random_numbers[number_index]

        bingo_cards = [card.play_bingo_number(bingo_number) for card in bingo_cards]

        for card in bingo_cards:
            if card.check_for_bingo():
                we_have_a_bingo = True
                winning_card = card

        number_index += 1

    final_score = winning_card.get_score()

    print(f"The final score is {final_score}")


def run_rigged_bingo_game(
    random_numbers: List[str], bingo_cards: List[BingoCard]
) -> BingoCard:

    number_index: int = 0

    while len(bingo_cards) > 1:
        bingo_number = random_numbers[number_index]

        bingo_cards = [card.play_bingo_number(bingo_number) for card in bingo_cards]

        bingo_cards = [card for card in bingo_cards if not card.check_for_bingo()]

        number_index += 1

    we_have_a_bingo = False
    final_card: BingoCard = bingo_cards[0]

    while not we_have_a_bingo:
        bingo_number = random_numbers[number_index]
        final_card = final_card.play_bingo_number(bingo_number)

        if final_card.check_for_bingo():
            break
        number_index += 1

    final_score = final_card.get_score()

    print(f"The final score in the rigged game is {final_score}")


def solution(case: str) -> None:
    inputs: PuzzleInput = load_puzzle_input(Year(2021), Day(4), PuzzleCase(case))

    random_numbers: List[str] = [x for x in inputs[0].split(",")]

    bingo_cards = get_bingo_cards(inputs)

    run_clean_bingo_game(random_numbers, bingo_cards)

    run_rigged_bingo_game(random_numbers, bingo_cards)
