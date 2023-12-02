import re
from typing import Dict, List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


class ReachGame:
    def __init__(self, game_id: int):
        self.game_id = game_id
        self.rounds: List[Dict[str, int]] = list()

    def add_game_turns(self, turn_string: str) -> None:
        reaches_in_turn = turn_string.split(",")

        turn_dict: Dict[str, int] = dict()

        for reaches in reaches_in_turn:
            number, color = reaches.split()
            turn_dict[color] = int(number)

        self.rounds.append(turn_dict)

    def check_game_valid(self, bag_reservoir: Dict[str, int]) -> bool:
        for round in self.rounds:
            for color, number in round.items():
                if number > bag_reservoir[color]:
                    return False
        return True

    def get_game_power(self) -> int:
        minimum_per_color: Dict[str, int] = {"red": 0, "green": 0, "blue": 0}
        for round in self.rounds:
            for color, number in round.items():
                if number > minimum_per_color[color]:
                    minimum_per_color[color] = number

        game_power = (
            minimum_per_color["red"]
            * minimum_per_color["green"]
            * minimum_per_color["blue"]
        )

        return game_power


def parse_moves(game_moves: PuzzleInput) -> List[ReachGame]:
    game_objects: List[ReachGame] = list()

    for game in game_moves:
        game_id = int(re.search("[0-9]+", game.split(":")[0]).group())

        game_object = ReachGame(game_id)

        all_game_turns = game.split(":")[1].split(";")
        for game_turn in all_game_turns:
            game_object.add_game_turns(game_turn)

        game_objects.append(game_object)

    return game_objects


def solution(case: str) -> None:
    game_moves: PuzzleInput = load_puzzle_input(Year(2023), Day(2), PuzzleCase(case))

    game_objects = parse_moves(game_moves)

    bag_reservoir = {"red": 12, "blue": 14, "green": 13}

    sum_valid_id = sum(
        game.game_id for game in game_objects if game.check_game_valid(bag_reservoir)
    )

    print(f"The sum of valid game IDs is {sum_valid_id}.")

    sum_game_power = sum(game.get_game_power() for game in game_objects)

    print(f"The sum of game power is {sum_game_power}")
