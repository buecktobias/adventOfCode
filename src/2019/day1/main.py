
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


def part2_mass(mass):
    sum = 0
    while calculate_mass(mass) > 0:
        sum += calculate_mass(mass)
        mass = calculate_mass(mass)
        print(mass)
    return sum


def calculate_mass(mass):
    return floor(mass / 3) - 2

# solve days puzzle
def solve():
    solution = 0
    input_file = get_input_file()
    lines_input_file = utility.get_lines_of_file(input_file)

    for line in lines_input_file:
        if line != "":
            number = int(line)
            solution += part2_mass(number)
    
    input_file.close()
    print(solution)
    return solution
    
    
def main():
    print(part2_mass(1969))
    solution = solve()
    level = 1  # level of the day, part, every day has two parts
    #submitSolution.submit_solution_requests(2019, 1, level, solution)


if __name__ == '__main__':
    main()    
