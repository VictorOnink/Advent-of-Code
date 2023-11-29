from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput

from copy import deepcopy

def get_most_common_bit_diagnostic(diagnostic: PuzzleInput, number_of_bits: int) -> str:
    mcb_diagnostic = ""
    
    for bit_num in range(number_of_bits):
        mcb_diagnostic += str(most_common_bit(diagnostic, bit_num))

    return mcb_diagnostic

def most_common_bit(diagnostic: PuzzleInput, bit_index: int) -> int:
    number_rows_diagnostic = len(diagnostic)
    equal_to_1 = sum(int(row[bit_index]) for row in diagnostic)
    equal_to_0 = number_rows_diagnostic - equal_to_1
    return int(equal_to_1 >= equal_to_0)

def invert_bits(bit_string: str) -> str:
    map_dict = {"1": "0", "0": "1"}

    invert: str = "".join(map_dict[bit] for bit in bit_string)

    return invert

def binary_to_decimal(bit_string: str) -> int:
    number_of_bits = len(bit_string)
    decimal: int = 0

    for ind, bit in enumerate(bit_string):
        decimal += int(bit) * 2 ** (number_of_bits - 1 - ind)

    return decimal

def get_oxygen_generator_rating(diagnostic: PuzzleInput) -> str:
    diagnostic_selector = deepcopy(diagnostic)
    
    bit_index = 0

    while len(diagnostic_selector) > 1:
        mcb = most_common_bit(diagnostic_selector, bit_index)

        diagnostic_selector = [value for value in diagnostic_selector if value[bit_index] == str(mcb)]

        bit_index += 1

    return diagnostic_selector[0]

def get_co2_scrubber_rating(diagnostic: PuzzleInput) -> str:
    diagnostic_selector = deepcopy(diagnostic)
    
    bit_index = 0

    while len(diagnostic_selector) > 1:
        lcb = invert_bits(str(most_common_bit(diagnostic_selector, bit_index)))

        diagnostic_selector = [value for value in diagnostic_selector if value[bit_index] == lcb]

        bit_index += 1

    return diagnostic_selector[0]

def solution(case: str) -> None:
    diagnostic: PuzzleInput = load_puzzle_input(Year(2021), Day(3), PuzzleCase(case))

    number_of_bits = len(diagnostic[0])

    mcb_diagnostic = get_most_common_bit_diagnostic(diagnostic, number_of_bits)

    lcb_diagnostic = invert_bits(mcb_diagnostic)

    gamma_rate = binary_to_decimal(mcb_diagnostic)

    epsilon_rate = binary_to_decimal(lcb_diagnostic)

    print(f"power consumption is {gamma_rate * epsilon_rate}")

    oxygen_rating = binary_to_decimal(get_oxygen_generator_rating(diagnostic))

    co2_rating = binary_to_decimal(get_co2_scrubber_rating(diagnostic))

    print(f"life support rating is {co2_rating * oxygen_rating}")