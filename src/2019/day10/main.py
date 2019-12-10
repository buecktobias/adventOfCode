# Created by Tobias Bück at 2019-12-10 06:06:11.675218
# Solution of day 10 of advent of Code 2019
# 
# INPUTS 
import utility  # helper methods
import sympy
import tkinter as tk

class Object:
    def show(self, canvas, scale):
        pass


class Vector(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, canvas, scale):
        x1 = self.x * scale
        y1 = self.y * scale

        size = scale / 2
        canvas.create_oval(x1-size, y1-size, x1+size, y1 + size)

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


class StraightLine(Object):
    def __init__(self, x, y, dir_x, dir_y):
        self.position_vector = Vector(x, y)
        self.direction_vector = Vector(dir_x, dir_y)

    def show(self, canvas, scale):
        x1 = self.position_vector.x
        y1 = self.position_vector.y
        x2 = self.position_vector.x + self.direction_vector.x
        y2 = self.position_vector.y + self.direction_vector.y

        x1 *= scale
        x2 *= scale
        y1 *= scale
        y2 *= scale
        canvas.create_line()

    def intersects(self, vec: Vector):
        t = sympy.symbols('t')
        eq_x = sympy.Eq(self.position_vector.x + self.direction_vector.x * t, vec.x)
        eq_y = sympy.Eq(self.position_vector.y + self.direction_vector.y * t, vec.y)
        system = [eq_x, eq_y]
        solution = sympy.solve(system, t)

        if len(solution) > 0:
            if solution[t] > 1:  # t must be greater than 1
                return True
        return False


class Asteroid(Object):
    def __init__(self, x, y):
        self.vec = Vector(x, y)

    def show(self, canvas, scale):
        self.vec.show(canvas, scale)

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
            x_diff = nearest.vec.x - self.vec.x
            y_diff = nearest.vec.y - self.vec.y
            new_straight_line = StraightLine(self.vec.x, self.vec.y, x_diff, y_diff)
            asteroids_copy = list(filter(lambda ast: not new_straight_line.intersects(ast.vec), asteroids_copy))
            pass
        return counter


class Application(tk.Canvas):
    def __init__(self, objects, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.objects = objects
        self.create_widgets()

    def create_widgets(self):
        scale = 20
        for object in self.objects:
            object.show(self, scale)


def get_input_file():
    return open("../../../input/2019/test10_2")


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
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    main()
