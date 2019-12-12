# Created by Tobias Bück at 2019-12-10 06:06:11.675218
# Solution of day 10 of advent of Code 2019
# 
# INPUTS 
import utility  # helper methods
import sympy
import tkinter as tk
from math import atan2


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self, other):
        x_diff = other.x - self.x
        y_diff = other.y - self.y
        return atan2(x_diff, y_diff)


class Asteroid:
    def __init__(self, x, y):
        self.vec = Vector(x, y)

    def asteroids_in_sight(self, asteroids):
        asteroids_copy = asteroids[:]
        asteroids_copy.remove(self)
        vectors = [ast.vec for ast in asteroids_copy]
        return len(set(list([self.vec.angle(vector) for vector in vectors])))


def get_input_file():
    return open("../../../input/2019/input10.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)

    [list(line) for line in lines_input_file]

    lines_input_file = list(filter(lambda l: len(l) > 0, lines_input_file))
    print(lines_input_file)
    return lines_input_file


def part1():
    lines = get_clean_data()
    max_x = len(lines[0])  # amount xss
    max_y = len(lines)  # amount yss
    asteroids = []

    for y in range(len(lines)):
        for x in range(max_x):
            if lines[y][x] == '#':
                asteroids.append(Asteroid(x, y))

    best = max(asteroids, key=lambda ast: ast.asteroids_in_sight(asteroids))
    return best.asteroids_in_sight(asteroids)


def part2():
    lines = get_clean_data()


def main():
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    main()
