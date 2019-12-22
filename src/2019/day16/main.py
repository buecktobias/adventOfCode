# Created by Tobias Bück at 2019-12-18 14:16:25.534081
# Solution of day 16 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods


def get_input_file():
    return open("../../../input/2019/input16.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = input_file.read()
    return lines_input_file


def create_pattern(length, phase_number):
    base_pattern = [0, 1, 0, -1]

    index = 0
    i = 0
    counter = 0
    while counter < length + 100:
        while i < phase_number:
            yield base_pattern[index]
            counter += 1
            i += 1
        i = 0
        index += 1
        if index >= len(base_pattern):
            index = 0


def phases(phase_input, amount_phases):
    for i in range(amount_phases):
        phase_input = one_phase(phase_input)
    return phase_input

def one_phase(phase_input):

    phase_output = []


    for i in range(len(phase_input)):
        pattern_0_1 = create_pattern(len(phase_input) + 1, i + 1)
        # shift left
        next(pattern_0_1)

        sum_ = 0
        for number in phase_input:
            number = int(number)
            next_pattern_0_1 = next(pattern_0_1)
            sum_ += number * next_pattern_0_1
            sum_ += 0

        last_digit = int(str(sum_)[-1])
        phase_output.append(last_digit)
    return phase_output


def part1():
    lines = get_clean_data()
    input_phase = lines
    print("".join([str(i) for i in phases(input_phase, 100)[:8]]))


def part2():
    lines = get_clean_data()   
    
        
def main():
    print(f"part1: {part1()}")


if __name__ == '__main__':
    main()    
