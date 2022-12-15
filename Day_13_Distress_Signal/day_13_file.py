from typing import List, Union
from enum import Enum, auto


class OrderState(Enum):
    INCONCLUSIVE = auto()
    CORRECT = auto()
    WRONG = auto()


PuzzleInput = List[str]
SignalPacket = List[Union[List[str], str]]


def load_puzzle_input(case: str) -> PuzzleInput:
    if case == "puzzle":
        file_name = "Day_13_Distress_Signal/puzzle_input.txt"
    else:
        file_name = "Day_13_Distress_Signal/test_input.txt"
    with open(file_name) as f:
        signals = [eval(x.strip()) for x in f.readlines() if x.strip() != ""]
    return signals


def check_order(left: SignalPacket, right: SignalPacket) -> OrderState:
    while True:
        if len(left) == 0 and len(right) == 0:
            return OrderState.INCONCLUSIVE
        elif len(left) > 0 and len(right) == 0:
            return OrderState.WRONG
        elif len(left) == 0 and len(right) > 0:
            return OrderState.CORRECT

        left_item: SignalPacket = left[0]
        right_item: SignalPacket = right[0]

        if isinstance(left_item, list) and isinstance(right_item, list):
            element_comparison: OrderState = check_order(left_item, right_item)
            if element_comparison != OrderState.INCONCLUSIVE:
                return element_comparison
        elif isinstance(left_item, int) and isinstance(right_item, int):
            if left_item < right_item:
                return OrderState.CORRECT
            elif left_item > right_item:
                return OrderState.WRONG
        else:
            left_item: SignalPacket = (
                left_item if isinstance(left_item, list) else [left_item]
            )
            right_item: SignalPacket = (
                right_item if isinstance(right_item, list) else [right_item]
            )

            element_comparison: OrderState = check_order(left_item, right_item)
            if element_comparison != OrderState.INCONCLUSIVE:
                return element_comparison

        left, right = left[1:], right[1:]


def print_sum_integers(signals: PuzzleInput):
    index_counter: int = 0
    number_signals: int = len(signals) // 2
    for packet in range(number_signals):
        left, right = signals[2 * packet], signals[2 * packet + 1]
        if check_order(left, right) == OrderState.CORRECT:
            index_counter += packet + 1

    print(f"The index counter for correctly ordered packets is {index_counter}")


def partition(signals: PuzzleInput, low: int, high: int):
    """Standard partition for the quicksort algorithm,"""
    pivot: SignalPacket = signals[high]

    index: int = low - 1

    for j in range(low, high):
        if check_order(signals[j], pivot) == OrderState.CORRECT:
            index += 1
            signals[index], signals[j] = signals[j], signals[index]

    signals[index + 1], signals[high] = signals[high], signals[index + 1]
    return index + 1


def quick_sort(signals: PuzzleInput, low: int, high: int):
    if low < high:
        partition_index = partition(signals, low, high)
        quick_sort(signals, low, partition_index - 1)
        quick_sort(signals, partition_index + 1, high)


if __name__ == "__main__":
    signals = load_puzzle_input("puzzle")
    print_sum_integers(signals)

    signals += [[[2]], [[6]]]
    quick_sort(signals, 0, len(signals) - 1)

    index_list_2: int = signals.index([[2]]) + 1
    index_list_6: int = signals.index([[6]]) + 1

    print(f"The decoder key is {index_list_2 * index_list_6}")
