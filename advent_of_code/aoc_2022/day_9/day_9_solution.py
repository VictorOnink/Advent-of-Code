from enum import Enum
from typing import Dict, List, Tuple

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput

Coordinate = Tuple[str]


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


def track_rope_N_knots(lines: List[str], N: int) -> None:
    knots: Dict[int, set] = {}
    for knot_number in range(N):
        knots[knot_number] = (0, 0)

    knot_paths: Dict[int, set] = {}
    for knot_number in range(N):
        knot_paths[knot_number] = set((0, 0))

    for line in lines:
        direction, steps = line.split()

        for _ in range(int(steps)):
            knots[0] = update_head(knots[0], Direction(direction))
            knot_paths[0].add(knots[0])

            for knot_number in range(1, N):
                if not check_proximity(knots[knot_number - 1], knots[knot_number]):
                    knots[knot_number] = update_tail(
                        knots[knot_number - 1], knots[knot_number]
                    )
                    knot_paths[knot_number].add(knots[knot_number])

    print(
        f"The number of unique positions visited by the tail with {N=} is {len(knot_paths[N - 1])}"
    )


def update_tail(head: Coordinate, tail: Coordinate) -> Coordinate:
    left_right: int = head[0] - tail[0]
    up_down: int = head[1] - tail[1]
    tail: Tuple[int] = (tail[0] + sign_value(left_right), tail[1] + sign_value(up_down))
    return tail


def sign_value(value: int) -> int:
    if value == 0:
        return 0
    elif value < 0:
        return -1
    else:
        return 1


def update_head(head: Coordinate, direction: Direction) -> Coordinate:
    if direction == Direction.UP:
        return (head[0], head[1] + 1)
    elif direction == Direction.DOWN:
        return (head[0], head[1] - 1)
    elif direction == Direction.RIGHT:
        return (head[0] + 1, head[1])
    else:
        return (head[0] - 1, head[1])


def check_proximity(head: Coordinate, tail: Coordinate) -> bool:
    prox_x: int = abs(head[0] - tail[0])
    prox_y: int = abs(abs(head[1] - tail[1]))
    return (prox_x <= 1) and (prox_y <= 1)


def check_diagonal(head: Coordinate, tail: Coordinate) -> bool:
    return (head[0] != tail[0]) and (head[1] != tail[1])


def solution():
    lines = load_puzzle_input(year=Year(2022), day=Day(9), case=PuzzleCase("puzzle"))

    track_rope_N_knots(lines, N=2)

    track_rope_N_knots(lines, N=10)
