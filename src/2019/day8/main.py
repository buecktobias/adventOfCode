# Created by Tobias Bück at 2019-12-08 10:08:02.334269
# Solution of day 8 of advent of Code 2019
# 
# INPUTS
from typing import List

import utility  # helper methods


def get_input_file():
    return open("../../../input/2019/input8.txt")


def get_clean_data():
    with get_input_file() as input_file:
        text = input_file.read().strip()
    digits = [int(s) for s in str(text)]
    return digits


def to_layers(width, height, digits) -> List[List[List[int]]]:
    layers = []
    while len(digits) > 0:
        layer = []
        for row in range(height):
            row_digits = []
            for n in range(width):
                row_digits.append(digits.pop(0))
            layer.append(row_digits)
        layers.append(layer)
    return layers


def get_digits_layer(layer):
    digits_in_layer = []
    for row in layer:
        digits_in_layer += row
    return digits_in_layer


def fewest_zero(layer):
    digits_in_layer = []
    for row in layer:
        digits_in_layer += row
    return digits_in_layer.count(0)


def part1():
    width = 25
    height = 6
    digits = get_clean_data()
    layers = to_layers(width, height, digits)
    layer_fewest_zeros = min(layers, key=fewest_zero)
    digits_fewest_zeros = get_digits_layer(layer_fewest_zeros)
    return digits_fewest_zeros.count(1) * digits_fewest_zeros.count(2)


def part2():
    lines = get_clean_data()


def main():
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    main()
