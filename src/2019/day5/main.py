# Created by Tobias Bück at 2019-12-05 06:08:50.704489
# Solution of day 5 of advent of Code 2019
# 
# INPUTS
from typing import List, Dict, Any

import enum
import abc


class OptFunction(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def execute(params, input_parser, modes):
        pass


class Add(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        a = params[0]
        b = params[1]
        c = params[2]

        if modes[0] == Mode.POSITION_MODE:
            a = numbers[a]

        if modes[1] == Mode.POSITION_MODE:
            b = numbers[b]

        numbers[c] = a + b
        return numbers


class Multiply(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        a = params[0]
        b = params[1]
        c = params[2]

        if modes[0] == Mode.POSITION_MODE:
            a = numbers[a]

        if modes[1] == Mode.POSITION_MODE:
            b = numbers[b]
        numbers[c] = a * b
        return numbers


class Input(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        # TODO modes !
        a = params[0]
        numbers[a] = int(input())
        return numbers


class Output(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        # TODO modes !
        a = params[0]
        if modes[0] == Mode.POSITION_MODE:
            a = numbers[a]

        print(a)
        return numbers


class Halt(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        # TODO modes !
        raise ValueError("HALT")


class JumpTrue(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        a = params[0]
        b = params[1]
        if modes[0] == Mode.POSITION_MODE:
            a = numbers[a]

        if modes[1] == Mode.POSITION_MODE:
            b = numbers[b]

        if a != 0:
            input_parser.pointer = b

        return numbers


class JumpFalse(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        a = params[0]
        b = params[1]
        if modes[0] == Mode.POSITION_MODE:
            a = numbers[a]

        if modes[1] == Mode.POSITION_MODE:
            b = numbers[b]

        if a == 0:
            input_parser.pointer = b

        return numbers


class LessThan(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        a = params[0]
        b = params[1]
        c = params[2]

        if modes[0] == Mode.POSITION_MODE:
            a = numbers[a]

        if modes[1] == Mode.POSITION_MODE:
            b = numbers[b]

        if a < b:
            numbers[c] = 1
        else:
            numbers[c] = 0
        return numbers


class Equals(OptFunction):
    @staticmethod
    def execute(params, input_parser, modes):
        numbers = input_parser.numbers
        a = params[0]
        b = params[1]
        c = params[2]

        if modes[0] == Mode.POSITION_MODE:
            a = numbers[a]

        if modes[1] == Mode.POSITION_MODE:
            b = numbers[b]

        if a == b:
            numbers[c] = 1
        else:
            numbers[c] = 0
        return numbers



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
    JUMP_TRUE = (5, 2, JumpTrue)
    JUMP_FALSE = (6, 2, JumpFalse)
    LESS_THAN = (7, 3, LessThan)
    EQUALS = (8, 3, Equals)

    def execute(self, params: List[int], input_parser, modes):
        assert self.amount_parameters == len(params), "The opt code needs a different amount of parameters!"
        cls = self.cls
        return cls.execute(params, input_parser, modes)


class Mode(enum.Enum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1


class IntCode:
    def __init__(self, opt_code: OptCode, params: List[int], modes: List[Mode]):
        assert len(params) == opt_code.amount_parameters, "The opt code needs a different amount of parameters!"
        self.opt_code: OptCode = opt_code
        self._params: List[int] = params
        self.modes: List[Mode] = modes

    def execute(self, input_parser):
        return self.opt_code.execute(self._params, input_parser, self.modes)


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
        modes = list(reversed(list(map(lambda digit_mode: Mode(digit_mode), modes))))
        params = self.numbers[self.pointer + 1: self.pointer + 1 + opt_code.amount_parameters]
        return IntCode(opt_code, params, modes)

    def start(self):
        while True:
            int_code = self.get_int_code()
            pointer_before = int(self.pointer)
            int_code.execute(self)
            opt_code_params = int_code.opt_code.amount_parameters
            if pointer_before == self.pointer:
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
