def load_puzzle_input() -> list:
    with open("Day_2_rock_paper_scissors/puzzle_input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

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
    move_opponent = move_set[0]
    move_player = move_set[2]

    if (move_player == "X") & (move_opponent == "A") | (move_player == "Y") & (move_opponent == "B") | (move_player == "Z") & (move_opponent == "C"):
        return 3
    elif ((move_player == "X") & (move_opponent == "C")) | ((move_player == "Y") & (move_opponent == "A")) | ((move_player == "Z") & (move_opponent == "B")):
        return 6
    else:
        return 0

def compute_move_scores(moves: list) -> None:
    move_scores = []
    for move_set in moves:
        move_scores.append(get_move_selection_score(move_set) + get_game_outcome_score(move_set))

    print(f"With these moves, we get a score of {sum(move_scores)}")
    print(len(move_scores))


if __name__ == "__main__":
    game_moves = load_puzzle_input()

    compute_move_scores(game_moves)

