from typing import Dict, List, Tuple

import numpy as np
from parse import compile

from advent_of_code.utils.data_loader import Day, PuzzleCase, Year, load_puzzle_input
from advent_of_code.utils.objects import PuzzleInput


class Seed:
    def __init__(
        self, seed_number: int, mappings: Dict[str, List[Tuple[int, int]]]
    ) -> None:
        self.seed_number = seed_number
        self.mappings = mappings

    def get_location(self) -> int:
        soil = self._convert_mapping(self.seed_number, "seed-to-soil")
        fertilizer = self._convert_mapping(soil, "soil-to-fertilizer")
        water = self._convert_mapping(fertilizer, "fertilizer-to-water")
        light = self._convert_mapping(water, "water-to-light")
        temperature = self._convert_mapping(light, "light-to-temperature")
        humidity = self._convert_mapping(temperature, "temperature-to-humidity")
        location = self._convert_mapping(humidity, "humidity-to-location")
        return location

    def _convert_mapping(self, value: int, mapping_name: str):
        ranges = self.mappings[mapping_name]
        for range_ind in range(1, len(ranges), 2):
            start_range, end_range = ranges[range_ind]

            if value >= start_range and value < end_range:
                map_start, _ = ranges[range_ind - 1]
                offset = map_start - start_range
                return value + offset
        return value


def get_mapping(map_type: str, raw_input: PuzzleInput) -> List[Tuple[int, int]]:
    mapping_list: List[Tuple[int, int]] = list()

    is_correct_mapping = False

    mapping_schema = compile("{:d} {:d} {:d}")
    for row in raw_input:
        if map_type in row:
            is_correct_mapping = True
            continue
        if is_correct_mapping and row:
            value_range_start, mapping_range_start, range_length = mapping_schema.parse(
                row
            )
            mapping_list.append((value_range_start, value_range_start + range_length))
            mapping_list.append(
                (mapping_range_start, mapping_range_start + range_length)
            )
        elif not row:
            is_correct_mapping = False
    return mapping_list


def converge_search(
    start_range: int,
    end_range: int,
    mappings: Dict[str, List[Tuple[int, int]]],
    step_sizer: int = 100,
    step_convergence: int = 10,
):
    """This convergence approach was inspired the solution posted by mmdoogie (github account)"""
    step_size = max(1, int(np.power(10, np.log10(end_range / step_sizer))))

    while step_size > 1:
        search_range = range(start_range, end_range, step_size)
        location_values = [
            Seed(seed_number, mappings).get_location() for seed_number in search_range
        ]
        min_location = min(location_values)
        start_range, end_range = (
            search_range[max(0, location_values.index(min_location) - 1)],
            search_range[
                min(location_values.index(min_location) + 1, len(location_values) - 1)
            ],
        )
        step_size = step_size // step_convergence

    search_range = range(start_range, end_range)
    if len(search_range) > 0:
        location_values = [
            Seed(seed_number, mappings).get_location() for seed_number in search_range
        ]
        min_location = min(location_values)
    else:
        min_location = Seed(start_range, mappings).get_location()
    return min_location


def solution(case: str) -> None:
    raw_input: PuzzleInput = load_puzzle_input(Year(2023), Day(5), PuzzleCase(case))
    seed_numbers: List[str] = [
        int(x) for x in raw_input[0].split(":")[1].strip().split(" ")
    ]

    mappings: Dict[str, List[Tuple[int, int]]] = {
        "seed-to-soil": get_mapping("seed-to-soil", raw_input),
        "soil-to-fertilizer": get_mapping("soil-to-fertilizer", raw_input),
        "fertilizer-to-water": get_mapping("fertilizer-to-water", raw_input),
        "water-to-light": get_mapping("water-to-light", raw_input),
        "light-to-temperature": get_mapping("light-to-temperature", raw_input),
        "temperature-to-humidity": get_mapping("temperature-to-humidity", raw_input),
        "humidity-to-location": get_mapping("humidity-to-location", raw_input),
    }

    seeds: List[Seed] = [Seed(seed_number, mappings) for seed_number in seed_numbers]

    locations: List[int] = [seed.get_location() for seed in seeds]

    print(f"The minimum location is {min(locations)}")

    min_location_per_range: List[int] = list()

    for ind in range(0, len(seed_numbers), 2):
        start_range = seed_numbers[ind]
        end_range = seed_numbers[ind] + seed_numbers[ind + 1]
        min_location_per_range.append(converge_search(start_range, end_range, mappings))

    print(f"The min location with rows is {min(min_location_per_range)}")
