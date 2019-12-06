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
    def execute(params, numbers):
        pass


class Add(OptFunction):
    @staticmethod
    def execute(params, numbers):
        a = params[0]
        b = params[1]
        c = params[2]
        numbers[c] = a + b
        return numbers


class Multiply(OptFunction):
    @staticmethod
    def execute(params, numbers):
        a = params[0]
        b = params[1]
        c = params[2]
        numbers[c] = a * b
        return numbers


class Input(OptFunction):
    @staticmethod
    def execute(params, numbers):
        a = params[0]
        numbers[a] = int(input())
        return numbers


class Output(OptFunction):
    @staticmethod
    def execute(params, numbers):
        a = params[0]
        print(numbers[a])
        return numbers


class Halt(OptFunction):
    @staticmethod
    def execute(params, numbers):
        raise ValueError("HALT")


class OptCode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    HALT = 99

    @staticmethod
    def from_value(value):
        values = {
            1: OptCode.ADD,
            2: OptCode.MULTIPLY,
            3: OptCode.INPUT,
            4:  OptCode.OUTPUT,
            99: OptCode.HALT
        }
        return values.get(value)


    @property
    def amount_parameters(self):
        parameter_dict = {
            OptCode.ADD: 3,
            OptCode.MULTIPLY: 3,
            OptCode.HALT: 0,
            OptCode.INPUT: 1,
            OptCode.OUTPUT: 1
        }
        return parameter_dict.get(self)
    
    def execute(self, params: List[int], numbers: List[int]):
        assert self.amount_parameters == len(params), "The opt code needs a different amount of parameters!"
        functions_dict: Dict[OptCode, Any] = {
            OptCode.ADD:  Add,
            OptCode.HALT: Halt,
            OptCode.MULTIPLY: Multiply,
            OptCode.OUTPUT: Output,
            OptCode.INPUT: Input
        }

        cls = functions_dict.get(self)
        return cls.execute(params, numbers)


class Mode(enum.Enum):
    @staticmethod
    def from_value(value):
        values_dict = {
            0: Mode.POSITION_MODE,
            1: Mode.IMMEDIATE_MODE
        }
        return values_dict.get(value)

    POSITION_MODE = 0
    IMMEDIATE_MODE = 1




class IntCode:
    def __init__(self, opt_code: OptCode, params: List[int], modes):
        assert len(params) == opt_code.amount_parameters, "The opt code needs a different amount of parameters!"
        self.opt_code: OptCode = opt_code
        self.params: List[int] = params
        self.modes: List[Mode] = modes

    def _get_params(self, numbers):
        params = []
        for i in range(len(self.params)):
            if self.modes[i] == Mode.IMMEDIATE_MODE:
                params.append(self.params[i])
            else:
                params.append(numbers[self.params[i]])
        return params

    def execute(self, numbers):
        params = self.params
        return self.opt_code.execute(params, numbers)


class InputParser:
    def __init__(self, numbers):
        self.pointer = 0
        self.numbers = numbers

    def forward(self, steps):
        self.pointer += steps

    def get_int_code(self):
        code = list(str(self.numbers[self.pointer]))
        reversed_code = list(reversed(code))
        int_opt_code = int("".join(reversed_code)[:2])
        opt_code: OptCode = OptCode.from_value(int_opt_code)
        str_modes = reversed_code[2:]
        modes = []
        for i in range(3):
            if len(str_modes) > i and str_modes[i] == "1":
                modes.append(Mode.from_value(1))
            else:
                modes.append(Mode.from_value(0))
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
    print(str(int("1100")))
    main()    
