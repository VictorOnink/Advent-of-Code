from typing import List

PuzzleInput = List[str]


def load_puzzle_input() -> PuzzleInput:
    with open("Day_6_Tuning_Trouble/puzzle_input.txt") as f:
        lines = [x.strip() for x in f.readlines()][0]
    return lines


def detect_marker(datastream: PuzzleInput, unique_for_marker: int) -> int:
    number_of_characters: int = len(datastream)

    for index in range(unique_for_marker, number_of_characters):
        if (
            len(set(datastream[(index - unique_for_marker) : index]))
            == unique_for_marker
        ):
            return index


if __name__ == "__main__":
    datastream = load_puzzle_input()

    marker_position = detect_marker(datastream, unique_for_marker=4)
    print(f"First marker after position {marker_position}")

    start_of_message_position = detect_marker(datastream, unique_for_marker=14)
    print(f"First start-of-message marker after position {start_of_message_position}")
