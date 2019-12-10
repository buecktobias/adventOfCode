# Created by Tobias Bück at 2019-12-08 10:08:02.334269
# Solution of day 8 of advent of Code 2019
# 
# INPUTS
from typing import List
import utility  # helper methods
from matplotlib import pyplot as plt

WIDTH = 25
HEIGHT = 6


TRANSPARENT = 2
BLACK = 0
WHITE = 1


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


def get_transparent_image():
    image = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(TRANSPARENT)
        image.append(row)
    return image


def layers_to_image(layers):
    transparent_image = get_transparent_image()

    for layer in layers:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if transparent_image[y][x] == TRANSPARENT and layer[y][x] != TRANSPARENT:
                    transparent_image[y][x] = layer[y][x]
    return transparent_image


def part1():

    digits = get_clean_data()
    layers = to_layers(WIDTH, HEIGHT, digits)
    layer_fewest_zeros = min(layers, key=fewest_zero)
    digits_fewest_zeros = get_digits_layer(layer_fewest_zeros)
    return digits_fewest_zeros.count(1) * digits_fewest_zeros.count(2)


def part2():
    digits = get_clean_data()
    layers = to_layers(WIDTH, HEIGHT, digits)
    image = layers_to_image(layers)
    plt.imshow(image, cmap='Greys', interpolation='nearest')
    plt.show()
    for r in image:
        for c in r:
            if c == BLACK:
                print('.', end='')
            if c == WHITE:
                print('#', end='')
        print()
    # zukcj
    return None


def main():
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    main()
