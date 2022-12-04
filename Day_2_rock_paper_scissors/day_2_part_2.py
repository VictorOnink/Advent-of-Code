from enum import Enum


class GameOutcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


class GameMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def load_puzzle_input() -> list:
    with open("Day_2_rock_paper_scissors/puzzle_input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines


def compute_move_scores(moves: list) -> None:
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


if __name__ == "__main__":
    game_moves = load_puzzle_input()

    compute_move_scores(game_moves)
