import random
# Created by Tobias Bück at 2019-12-02 06:05:30.339167
# Solution of day 2 of advent of Code 2019
# 
# INPUTS
from typing import List

import utility     # helper methods


# opens the input file
def get_input_file():
    return open("../../../input/2019/input2.txt")


def get_numbers():
    input_file = get_input_file()
    lines_input_file = utility.get_lines_of_file(input_file)
    numbers = "".join(lines_input_file)
    numbers = list(numbers.split(","))
    numbers = list([int(number) for number in numbers])
    input_file.close()
    return numbers


def multiply(a, b):
    return a * b


def add(a,b):
    return a +b


def calculate(numbers: List[int]):
    for i in range(0, len(numbers), 4):
        opt_code = numbers[i]
        if opt_code == 1:
            operator = add
        elif opt_code == 2:
            operator = multiply
        elif opt_code == 99:
            break
        else:
            raise ValueError(f"opt code must be 1, 2 or 99, but is {opt_code}")

        number1 = numbers[i + 1]
        number2 = numbers[i + 2]
        number3 = numbers[i + 3]
        a = numbers[number1]
        b = numbers[number2]
        numbers[number3] = operator(a, b)
    return numbers


def part1():
    numbers = get_numbers()
    numbers[1] = 12
    numbers[2] = 2
    numbers = calculate(numbers)
    return numbers[0]


def part2():
    for x in range(100):
        for y in range(100):
            numbers = get_numbers()
            numbers[1] = x
            numbers[2] = y
            numbers = calculate(numbers)
            if numbers[0] == 19690720:
                return 100 * x +y

def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()    
