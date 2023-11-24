from argparse import ArgumentParser

from advent_of_code.aoc_2022 import SOLUTIONS_2022
from advent_of_code.aoc_2021 import SOLUTIONS_2021

SOLUTIONS = {
    2022: SOLUTIONS_2022,
    2021: SOLUTIONS_2021
}

if __name__ == "__main__":
    parser = ArgumentParser(
                    prog='Advent of Code',
                    description='This code runs the requested solution for Advent of Code',
                    )
    parser.add_argument('--year', nargs="?", const=2022, type=int)
    parser.add_argument('--day', nargs="?", const=1, type=int)
    parser.add_argument('--case', nargs="?", const="test", type=str)

    args = parser.parse_args()

    solution = SOLUTIONS[args.year][args.day]

    solution(args.case)