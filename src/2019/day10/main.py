# Created by Tobias Bück at 2019-12-10 06:06:11.675218
# Solution of day 10 of advent of Code 2019
# 
# INPUTS 
import utility  # helper methods
from sympy import *


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_vec = Vector(self.x, self.y)
        new_vec.x += other.x
        new_vec.y += other.y
        return new_vec

    def __mul__(self, other: int):
        new_vec = Vector(self.x, self.y)
        new_vec.x = other * self.x
        new_vec.y = other * self.y
        return new_vec

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class StraightLine:
    def __init__(self, x, y, dir_x, dir_y):
        self.position_vector = Vector(x, y)
        self.direction_vector = Vector(dir_x, dir_y)

    def intersects(self, vector: Vector):
        t = sympy.symbols('t')
        print(sympy.solve([self.position_vector + t * self.direction_vector, vector]))


class Asteroid:
    def __init__(self, x, y):
        self.vec = Vector(x, y)

    def get_nearest_asteroid(self, asteroids):
        asteroids_copy = asteroids[:]
        nearest = min(asteroids_copy, key=lambda other: abs(self.vec.x - other.vec.x) + abs(self.vec.y -other.vec.y))
        return nearest

    def asteroids_in_sight(self, asteroids):
        asteroids_copy = asteroids[:]
        asteroids_copy.remove(self)
        # ich könnte eine heap verwenden lol
        # immer wieder nähesten nehmen und alle rauskicken die von diesem neuewn Asteroid raaufgekickt werdsn
        counter = 0
        while len(asteroids_copy) > 0:
            nearest = self.get_nearest_asteroid(asteroids_copy)
            asteroids_copy.remove(nearest)
            counter += 1
            # asteroids rausschmeissen

            asteroids_copy = list(filter(lambda ast: self.is_asteroid_in_sight(ast, x_diff, y_diff), asteroids_copy))
        return counter


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
    max_x = len(lines[0]) # amount xss
    max_y = len(lines) # amount yss
    asteroids = []

    for y in range(len(lines)):
        for x in range(max_x):
            if lines[y][x] == '#':
                asteroids.append(Asteroid(x, y))
    best = max(asteroids, key=lambda ast: ast.asteroids_in_sight(asteroids))
    print(best.asteroids_in_sight(asteroids))


def part2():
    lines = get_clean_data()


def main():

    """
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))
    """
if __name__ == '__main__':
    main()
