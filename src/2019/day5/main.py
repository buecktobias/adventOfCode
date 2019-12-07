# Created by Tobias Bück at 2019-12-05 06:08:50.704489
# Solution of day 5 of advent of Code 2019
# 
# INPUTS
from typing import List, Dict, Any

import utility     # helper methods
import enum
import abc


class OptFunction(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def execute(params, numbers, modes):
        pass


class Add(OptFunction):
    @staticmethod
    def execute(params, numbers, modes):
        # TODO modes !
        a = params[0]
        b = params[1]
        c = params[2]
        numbers[c] = a + b
        return numbers


class Multiply(OptFunction):
    @staticmethod
    def execute(params, numbers, modes):
        # TODO modes !
        a = params[0]
        b = params[1]
        c = params[2]
        numbers[c] = a * b
        return numbers


class Input(OptFunction):
    @staticmethod
    def execute(params, numbers, modes):
        # TODO modes !
        a = params[0]
        numbers[a] = int(input())
        return numbers


class Output(OptFunction):
    @staticmethod
    def execute(params, numbers, modes):
        # TODO modes !
        a = params[0]
        print(numbers[a])
        return numbers


class Halt(OptFunction):
    @staticmethod
    def execute(params, numbers, modes):
        # TODO modes !
        raise ValueError("HALT")


class OptCode(bytes, enum.Enum):
    def __new__(cls, value, amount_parameters, function):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.amount_parameters = amount_parameters
        obj.cls = function
        return obj
    ADD = (1, 3, Add)
    MULTIPLY = (2, 3, Multiply)
    INPUT = (3, 1, Input)
    OUTPUT = (4, 1, Output)
    HALT = (99, 0, Halt)

    def execute(self, params: List[int], numbers: List[int], modes):
        assert self.amount_parameters == len(params), "The opt code needs a different amount of parameters!"
        cls = self.cls
        return cls.execute(params, numbers, modes)


class Mode(enum.Enum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1


class IntCode:
    def __init__(self, opt_code: OptCode, params: List[int], modes: List[Mode]):
        assert len(params) == opt_code.amount_parameters, "The opt code needs a different amount of parameters!"
        self.opt_code: OptCode = opt_code
        self._params: List[int] = params
        self.modes: List[Mode] = modes


    def execute(self, numbers):
        params = self._get_params(numbers)
        return self.opt_code.execute(params, numbers, self.modes)


class InputParser:
    def __init__(self, numbers):
        self.pointer = 0
        self.numbers = numbers

    def forward(self, steps):
        self.pointer += steps

    def get_int_code(self):
        digits = str(self.numbers[self.pointer])
        while len(digits) < 5:
            digits = "0" + digits
        modes = map(lambda e: int(e), digits[:3])
        opt_code = OptCode(int(digits[3:]))
        modes = list(map(lambda digit_mode: Mode(digit_mode), modes))
        params = self.numbers[self.pointer + 1: self.pointer + 1 + opt_code.amount_parameters]
        return IntCode(opt_code, params, modes)

    def start(self):
        while True:
            int_code = self.get_int_code()
            int_code.execute(self.numbers)
            opt_code_params = int_code.opt_code.amount_parameters
            self.forward(opt_code_params + 1)


def get_input_file():
    return open("../../../input/2019/input5.txt", "r")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = input_file.read()
    numbers = list(lines_input_file.split(","))
    numbers = list([int(number) for number in numbers])
    return numbers


def get_value(numbers, number, is_immediate):
    if is_immediate:
        return number
    else:
        return numbers[number]


def part1():
    numbers = get_clean_data()
    program = InputParser(numbers)
    program.start()


def part2():
    lines = get_clean_data()   
    
        
def main():
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    main()
