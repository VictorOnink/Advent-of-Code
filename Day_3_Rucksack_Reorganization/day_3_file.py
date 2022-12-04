import string

def get_priority_score(Item: str) -> int:
    return string.ascii_letters.find(Item) + 1
    

def load_puzzle_input() -> list:
    with open("Day_3_Rucksack_Reorganization/puzzle_input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def split_bag_into_compartments(rucksack_contents: list) -> list:
    rucksack_compartments = []
    for rucksack in rucksack_contents:
        number_of_items = len(rucksack)
        rucksack_compartments.append(
            [rucksack[:(number_of_items // 2)], rucksack[(number_of_items // 2):]]
            )
    return rucksack_compartments

def get_priority_scores(rucksack_compartments: list) -> None:
    total_priority_score = 0

    for rucksack in rucksack_compartments:
        first_comp, second_comp = rucksack
        for Item in set(first_comp):
            if Item in second_comp:
                total_priority_score += get_priority_score(Item)
    
    print(f"The total priority score is {total_priority_score}")

def get_priority_scores_per_group_elves(rucksack_contents: list) -> None:
    elves_per_group = 3
    number_of_groups = len(rucksack_contents) // elves_per_group

    total_priority_score = 0

    for group_id in range(number_of_groups):
        elf_1 = rucksack_contents[group_id * elves_per_group]
        elf_2 = rucksack_contents[group_id * elves_per_group + 1]
        elf_3 = rucksack_contents[group_id * elves_per_group + 2]

        for Item in set(elf_1):
            if (Item in elf_2) & (Item in elf_3):
                total_priority_score += get_priority_score(Item)
                break
    
    print(f"The total priority score is {total_priority_score}")



if __name__ == "__main__":
    rucksack_contents = load_puzzle_input()

    rucksack_compartments = split_bag_into_compartments(rucksack_contents)

    get_priority_scores(rucksack_compartments)

    get_priority_scores_per_group_elves(rucksack_contents)
