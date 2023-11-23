from typing import List

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput



def print_screen(lines: PuzzleInput, signal_selection: List[int]):
    register: int = 1
    cycle: int = 1
    signal_strengths: List[str] = [register * cycle]

    screen_pixels: str = ""

    for line in lines:
        screen_pixels = print_pixel(screen_pixels, cycle, register)
        cycle += 1
        signal_strengths.append(register * cycle)

        if "addx" in line:
            screen_pixels = print_pixel(screen_pixels, cycle, register)
            cycle += 1
            register += int(line.split()[1])
            signal_strengths.append(register * cycle)

    sum_selected_signal_strengths = sum(signal_strengths[i] for i in signal_selection)

    print(f"We have {sum_selected_signal_strengths=}")

    print(screen_pixels)


def print_pixel(screen_pixels: str, cycle: int, register: int) -> str:
    if abs(((cycle - 1) % 40 - register)) <= 1:
        screen_pixels += "#"
    else:
        screen_pixels += "."
    if (cycle - 1) % 40 == 39:
        screen_pixels += "\n"
    return screen_pixels


def solution():
    lines = load_puzzle_input(year=Year(2022), day=Day(10), case=PuzzleCase("puzzle"))

    signal_selection = [19, 59, 99, 139, 179, 219]
    print_screen(lines, signal_selection)