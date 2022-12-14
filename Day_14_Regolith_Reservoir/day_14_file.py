from typing import List, Tuple, Set

PuzzleInput = List[str]
CaveCoordinate = Tuple[int, int]
RockPoints = Set[CaveCoordinate]
SandPoints = Set[CaveCoordinate]


def load_puzzle_input(case: str) -> PuzzleInput:
    if case == "puzzle":
        file_name = "Day_14_Regolith_Reservoir/puzzle_input.txt"
    else:
        file_name = "Day_14_Regolith_Reservoir/test_input.txt"
    with open(file_name) as f:
        lines = [x.strip().split(" -> ") for x in f.readlines()]
    return lines


def get_rock_face(rock_coordinates: PuzzleInput) -> RockPoints:
    rock_face: RockPoints = set()

    for ledge in rock_coordinates:
        ledge_coordinates = [eval(rock) for rock in ledge]

        for i in range(len(ledge) - 1):
            start, end = ledge_coordinates[i], ledge_coordinates[i + 1]

            # Get the coordinate differences
            x_diff, y_diff = end[0] - start[0], end[1] - start[1]

            # Get x coordinates:
            if x_diff == 0:
                x_range = [start[0]]
            elif x_diff < 0:
                x_range = [start[0] + x for x in range(x_diff, 1)]
            else:
                x_range = [start[0] + x for x in range(x_diff + 1)]

            # Get y coordinates:
            if y_diff == 0:
                y_range = [start[1]]
            elif y_diff < 0:
                y_range = [start[1] + y for y in range(y_diff, 1)]
            else:
                y_range = [start[1] + y for y in range(y_diff + 1)]

            # Add rock
            for coord in [(x, y) for x in x_range for y in y_range]:
                rock_face.add(coord)

    return rock_face


def get_floor_y(rock_face: RockPoints) -> int:
    return max(rock[1] for rock in rock_face) + 1


def sand_to_the_roof(rock_face: RockPoints, sand_entry: CaveCoordinate) -> None:
    all_sand: SandPoints = set()
    unit_counter: int = 0
    floor_y: int = get_floor_y(rock_face)
    while sand_entry not in all_sand:
        all_sand, _ = drop_sand(all_sand, rock_face, sand_entry, floor_y)
        unit_counter += 1
    print(f"The sand stops moving after {unit_counter} rounds.")


def sand_to_the_bottom(rock_face: RockPoints, sand_entry: CaveCoordinate) -> None:
    all_sand: SandPoints = set(sand_entry)
    unit_counter: int = 0
    max_y: int = sand_entry[1]
    floor_y: int = get_floor_y(rock_face)

    while max_y < floor_y:
        all_sand, sand_position = drop_sand(all_sand, rock_face, sand_entry, floor_y)
        max_y = sand_position[1]
        unit_counter += 1

    print(f"The sand stops moving after {unit_counter - 1} rounds.")


def drop_sand(
    all_sand: SandPoints,
    rock_face: RockPoints,
    sand_entry: CaveCoordinate,
    floor_y: int,
) -> Tuple[SandPoints, CaveCoordinate]:
    sand_position = sand_entry
    can_move = True
    while can_move:
        # Check above floor
        above_floor = sand_position[1] + 1 <= floor_y
        # Otherwise try moving down
        if (
            all(
                (sand_position[0], sand_position[1] + 1) not in x
                for x in [all_sand, rock_face]
            )
            and above_floor
        ):
            sand_position = (sand_position[0], sand_position[1] + 1)
        # Try moving down and left
        elif (
            all(
                (sand_position[0] - 1, sand_position[1] + 1) not in x
                for x in [all_sand, rock_face]
            )
            and above_floor
        ):
            sand_position = (sand_position[0] - 1, sand_position[1] + 1)
        # Try moving down and right
        elif (
            all(
                (sand_position[0] + 1, sand_position[1] + 1) not in x
                for x in [all_sand, rock_face]
            )
            and above_floor
        ):
            sand_position = (sand_position[0] + 1, sand_position[1] + 1)
        # Acceptance that the sand is actually stuck
        else:
            can_move = False
            all_sand.add(sand_position)
    return all_sand, sand_position


if __name__ == "__main__":
    rock_coordinates = load_puzzle_input("puzzle")

    sand_entry: CaveCoordinate = (500, 0)

    rock_face: RockPoints = get_rock_face(rock_coordinates)

    sand_to_the_bottom(rock_face, sand_entry)

    sand_to_the_roof(rock_face, sand_entry)
