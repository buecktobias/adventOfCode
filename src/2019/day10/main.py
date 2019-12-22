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

    def manhattan_distance(self, other):
        abs_x_diff = abs(self.x - other.x)
        abs_y_diff = abs(self.y - other.y)
        return abs_x_diff + abs_y_diff


class Asteroid:
    def __init__(self, x, y):
        self.vec = Vector(x, y)

    def asteroids_in_sight(self, asteroids):
        asteroids_copy = asteroids[:]
        asteroids_copy.remove(self)
        vectors = [ast.vec for ast in asteroids_copy]
        return len(set(list([self.vec.angle(vector) for vector in vectors])))

    def __repr__(self):
        return f"({self.vec.x} ,{self.vec.y})"

    def vaporize(self, asteroids):
        vaporized = []
        asteroids_copy = asteroids[:]
        asteroids_copy.remove(self)
        while len(asteroids_copy) > 0:
            angels_dict = {}
            for asteroid in asteroids_copy:
                angle = self.vec.angle(asteroid.vec)
                if angle in angels_dict:
                    angels_dict[angle].append(asteroid)
                else:
                    angels_dict[angle] = [asteroid]

            first_asteroids = []

            for key in angels_dict.keys():
                nearest = min(angels_dict[key], key=lambda ast: self.vec.manhattan_distance(ast.vec))
                first_asteroids.append(nearest)

            first_asteroids.sort(key=lambda ast: self.vec.angle(ast.vec))
            first_asteroids = list(reversed(first_asteroids))
            vaporized.extend(first_asteroids)
            for ast in first_asteroids:
                asteroids_copy.remove(ast)
        return vaporized


def get_input_file():
    return open("../../../input/2019/input10.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)

    [list(line) for line in lines_input_file]

    lines_input_file = list(filter(lambda l: len(l) > 0, lines_input_file))
    return lines_input_file


def part1():
    lines = get_clean_data()
    max_x = len(lines[0])  # amount xss
    asteroids = []

    for y in range(len(lines)):
        for x in range(max_x):
            if lines[y][x] == '#':
                asteroids.append(Asteroid(x, y))

    best = max(asteroids, key=lambda ast: ast.asteroids_in_sight(asteroids))

    vaporized = best.vaporize(asteroids)
    print(vaporized[200])
    x = vaporized[200].vec.x
    y = vaporized[200].vec.y
    print(100 * x + y)


def part2():
    lines = get_clean_data()


def main():
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    main()
