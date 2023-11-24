from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


def detect_marker(datastream: PuzzleInput, unique_for_marker: int) -> int:
    number_of_characters: int = len(datastream)

    for index in range(unique_for_marker, number_of_characters):
        if (
            len(set(datastream[(index - unique_for_marker) : index]))
            == unique_for_marker
        ):
            return index


def solution(case: str):
    datastream = load_puzzle_input(year=Year(2022), day=Day(6), case=PuzzleCase(case))[
        0
    ]

    marker_position = detect_marker(datastream, unique_for_marker=4)
    print(f"First marker after position {marker_position}")

    start_of_message_position = detect_marker(datastream, unique_for_marker=14)
    print(f"First start-of-message marker after position {start_of_message_position}")
