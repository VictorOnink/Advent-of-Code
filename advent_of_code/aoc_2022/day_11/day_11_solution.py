import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

from advent_of_code.utils.data_loader import DATA_DIREC, Day, PuzzleCase, Year


@dataclass
class Monkey:
    id: int
    divisible_test: int
    true_target: int
    false_target: int
    operation_type: str
    operation_value: int
    worry_mod: int = 1

    def transfer_to_whom(self, item_value: int, case: int):
        if self.operation_type == "+":
            item_value += self.operation_value
        elif self.operation_type == "*":
            item_value *= self.operation_value
        elif self.operation_type == "old * old":
            item_value *= item_value

        if case == 1:
            item_value = item_value // 3
        elif case == 2:
            item_value %= self.worry_mod

        if item_value % self.divisible_test == 0:
            return self.true_target, item_value
        else:
            return self.false_target, item_value


MonkeyGroup = List[Monkey]
StolenItems = Dict[int, List[int]]


def load_input(
    year: Year, day: Day, case: PuzzleCase
) -> Tuple[MonkeyGroup, StolenItems]:
    file_name = DATA_DIREC.joinpath(
        f"aoc_{year.value}/day_{day.value}/{case.value}_input.txt"
    )
    with open(file_name) as f:
        lines = [x.strip() for x in f.readlines() if x.strip() != ""]

    number_of_monkeys: int = len(lines) // 6

    items_per_monkey: StolenItems = dict.fromkeys(range(number_of_monkeys))
    for monkey in items_per_monkey.keys():
        items_per_monkey[monkey] = []

    group_of_monkeys: MonkeyGroup = []

    for monkey in range(number_of_monkeys):
        monkey_id: int = int(lines[monkey * 6][7])

        starting_items: List[int] = [
            int(x) for x in lines[monkey * 6 + 1].split(":")[1].split(",")
        ]

        if "old * old" in lines[monkey * 6 + 2]:
            operation_type: str = "old * old"
            operation_value: int = None
        elif "*" in lines[monkey * 6 + 2]:
            operation_type: str = "*"
            operation_value: int = int(lines[monkey * 6 + 2].split("*")[1])
        else:
            operation_type: str = "+"
            operation_value: int = int(lines[monkey * 6 + 2].split("+")[1])

        divisible_test: int = int(lines[monkey * 6 + 3].split("divisible by")[1])
        true_target: int = int(lines[monkey * 6 + 4].split("to monkey")[1])
        false_target: int = int(lines[monkey * 6 + 5].split("to monkey")[1])

        items_per_monkey[monkey] += starting_items
        group_of_monkeys.append(
            Monkey(
                monkey_id,
                divisible_test,
                true_target,
                false_target,
                operation_type,
                operation_value,
            )
        )

    return group_of_monkeys, items_per_monkey


def level_of_monkey_business(
    group_of_monkeys: MonkeyGroup, items_per_monkey: StolenItems, rounds: int, case: int
):
    monkey_business: List[int] = [0] * len(group_of_monkeys)

    worry_mod: int = math.lcm(*[monkey.divisible_test for monkey in group_of_monkeys])
    for monkey in group_of_monkeys:
        monkey.worry_mod = worry_mod

    for _ in range(rounds):
        for monkey in group_of_monkeys:
            while len(items_per_monkey[monkey.id]) > 0:

                item_value: int = items_per_monkey[monkey.id].pop()

                target_monkey, new_value = monkey.transfer_to_whom(item_value, case)

                items_per_monkey[target_monkey].append(new_value)
                monkey_business[monkey.id] += 1

    monkey_business.sort()
    print(
        f"The monkey business of chasing the two worst monkeys is {monkey_business[-1] * monkey_business[-2]}"
    )


def solution(case: str):
    group_of_monkeys, items_per_monkey = load_input(
        year=Year(2022), day=Day(11), case=PuzzleCase(case)
    )
    level_of_monkey_business(group_of_monkeys, items_per_monkey, rounds=20, case=1)

    group_of_monkeys, items_per_monkey = load_input(
        year=Year(2022), day=Day(11), case=PuzzleCase(case)
    )
    level_of_monkey_business(group_of_monkeys, items_per_monkey, rounds=10_000, case=2)
