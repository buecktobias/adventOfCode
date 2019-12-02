
# Created by Tobias Bück at 2019-12-01 06:00:15.774113
# Solution of day 1 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods
from math import floor  # for rounding down


# opens the input file
def get_input_file():
    return open("../../../input/2019/input1.txt")


def get_cleaned_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_as_ints(input_file)
    return lines_input_file


def calculate_part2_fuels(mass):
    while calculate_fuel(mass) > 0:
        mass = calculate_fuel(mass)
        yield mass


def calculate_part2(mass):
    return sum(calculate_part2_fuels(mass))


def calculate_fuel(mass):
    return floor(mass / 3) - 2


def part1():
    lines_input_file = get_cleaned_data()
    return sum(map(calculate_fuel, lines_input_file))


def part2():
    lines_input_file = get_cleaned_data()
    return sum(map(calculate_part2, lines_input_file))


# solve days puzzle
def main():
    print(f"part1 {part1()}")
    print(f"part2 {part2()}")


if __name__ == '__main__':
    main()    
