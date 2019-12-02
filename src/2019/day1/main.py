
# Created by Tobias Bück at 2019-12-01 06:00:15.774113
# Solution of day 1 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods
import inputGetter    # script for getting input file
import submitSolution   # script to submit uploading solution
from math import floor


# opens the input file
def get_input_file():
    return open("../../../input/2019/input1.txt")


def get_cleaned_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_as_ints(input_file)
    return lines_input_file


def part2_mass(mass):
    sum = 0
    while calculate_mass(mass) > 0:
        sum += calculate_mass(mass)
        mass = calculate_mass(mass)
    return sum


def calculate_mass(mass):
    return floor(mass / 3) - 2


def part1():
    lines_input_file = get_cleaned_data()
    return sum(map(calculate_mass, lines_input_file))


def part2():
    lines_input_file = get_cleaned_data()
    return sum(map(part2_mass, lines_input_file))


# solve days puzzle
def main():
    print(f"part1 {part1()}")
    print(f"part2 {part2()}")


if __name__ == '__main__':
    main()    
