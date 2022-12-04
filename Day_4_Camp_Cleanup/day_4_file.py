import re

def load_puzzle_input() -> list:
    with open("Day_4_Camp_Cleanup/puzzle_input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def check_full_section_overlap(section_pairs: list) -> None:
    overlap_counter = 0
    for section_pair in section_pairs:
        range_1_min, range_1_max, range_2_min, range_2_max = [int(x) for x in re.split(",|-", section_pair)]
        
        range_1 = range(range_1_min, range_1_max + 1)
        range_2 = range(range_2_min, range_2_max + 1)

        if (range_1_min in range_2) & (range_1_max in range_2):
            overlap_counter += 1
        elif (range_2_min in range_1) & (range_2_max in range_1):
            overlap_counter += 1
    print(f"We have {overlap_counter} ranges with complete overlap")


def check_some_section_overlap(section_pairs: list) -> None:
    overlap_counter = 0
    for section_pair in section_pairs:
        range_1_min, range_1_max, range_2_min, range_2_max = [int(x) for x in re.split(",|-", section_pair)]
        
        range_1 = range(range_1_min, range_1_max + 1)
        range_2 = range(range_2_min, range_2_max + 1)

        if (range_1_min in range_2) | (range_1_max in range_2):
            overlap_counter += 1
        elif (range_2_min in range_1) | (range_2_max in range_1):
            overlap_counter += 1
    print(f"We have {overlap_counter} ranges with some overlap")



if __name__ == "__main__":
    section_pairs = load_puzzle_input()

    check_full_section_overlap(section_pairs)

    check_some_section_overlap(section_pairs)
