from enum import Enum
from typing import Dict, List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


class GameOutcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


class GameMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_move_selection_score(move_set: str) -> int:
    move_player = move_set[2]
    return {"Y": 2, "X": 1, "Z": 3}[move_player]


def get_game_outcome_score(move_set: str) -> int:
    """
    Opponent:
        - rock = A
        - paper = B
        - scissors = C

    Player:
        - rock = X
        - paper = Y
        - scissors = Z
    """
    move_opponent: str = move_set[0]
    move_player: str = move_set[2]

    if (
        (move_player == "X") & (move_opponent == "A")
        | (move_player == "Y") & (move_opponent == "B")
        | (move_player == "Z") & (move_opponent == "C")
    ):
        return 3
    elif (
        ((move_player == "X") & (move_opponent == "C"))
        | ((move_player == "Y") & (move_opponent == "A"))
        | ((move_player == "Z") & (move_opponent == "B"))
    ):
        return 6
    else:
        return 0


def compute_move_scores_part_1(moves: PuzzleInput) -> None:
    move_scores: List[int] = []
    for move_set in moves:
        move_scores.append(
            get_move_selection_score(move_set) + get_game_outcome_score(move_set)
        )

    print(f"With these moves, we get a score of {sum(move_scores)}")


def compute_move_scores_part_2(moves: PuzzleInput) -> None:
    move_scores = []
    for move_set in moves:
        move_opponent = convert_symbol_to_move(move_set[0])
        desired_outcome = convert_symbol_to_outcome(move_set[2])
        player_move = get_move_from_outcome(move_opponent, desired_outcome)
        move_scores.append(desired_outcome.value + player_move.value)

    print(f"With these moves, we get a score of {sum(move_scores)}")


def convert_symbol_to_move(opponent_move: str) -> GameMove:
    return {"A": GameMove.ROCK, "B": GameMove.PAPER, "C": GameMove.SCISSORS}[
        opponent_move
    ]


def convert_symbol_to_outcome(needed_outcome: str) -> GameOutcome:
    return {"X": GameOutcome.LOSS, "Y": GameOutcome.DRAW, "Z": GameOutcome.WIN}[
        needed_outcome
    ]


def get_move_from_outcome(
    opponent_move: GameMove, needed_outcome: GameOutcome
) -> GameMove:
    if opponent_move == GameMove.ROCK:
        return move_against_opponent_rock(needed_outcome)
    elif opponent_move == GameMove.SCISSORS:
        return move_against_opponent_scissors(needed_outcome)
    elif opponent_move == GameMove.PAPER:
        return move_against_opponent_paper(needed_outcome)


def move_against_opponent_rock(needed_outcome: GameOutcome) -> GameMove:
    if needed_outcome == GameOutcome.DRAW:
        return GameMove.ROCK
    elif needed_outcome == GameOutcome.WIN:
        return GameMove.PAPER
    else:
        return GameMove.SCISSORS


def move_against_opponent_scissors(needed_outcome: GameOutcome) -> GameMove:
    if needed_outcome == GameOutcome.DRAW:
        return GameMove.SCISSORS
    elif needed_outcome == GameOutcome.WIN:
        return GameMove.ROCK
    else:
        return GameMove.PAPER


def move_against_opponent_paper(needed_outcome: GameOutcome) -> GameMove:
    if needed_outcome == GameOutcome.DRAW:
        return GameMove.PAPER
    elif needed_outcome == GameOutcome.WIN:
        return GameMove.SCISSORS
    else:
        return GameMove.ROCK


def solution() -> None:
    game_moves: PuzzleInput = load_puzzle_input(
        year=Year(2022), day=Day(2), case=PuzzleCase("puzzle")
    )

    compute_move_scores_part_1(game_moves)

    compute_move_scores_part_2(game_moves)
