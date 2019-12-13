# Created by Tobias Bück at 2019-12-13 00:00:53.987793
# Solution of day 12 of advent of Code 2019
# 
# INPUTS 
import utility  # helper methods
import re


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def cords(self):
        return self.x, self.y, self.z

    def __abs__(self):
        return sum([abs(cord) for cord in self.cords])

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __iadd__(self, other):
        return self + other

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}"


class Moon:
    moons = []

    def __init__(self, name, x, y, z):
        self.name = name
        self.position = Vector(x, y, z)
        self.velocity = Vector(0, 0, 0)
        Moon.moons.append(self)

    def gravity_to_all(self):
        moons = Moon.moons[:]
        moons.remove(self)
        for moon in moons:
            self.gravity(moon)

    def gravity(self, other):
        if self.position.x > other.position.x:
            self.velocity.x -= 1
        elif self.position.x < other.position.x:
            self.velocity.x += 1

        if self.position.y > other.position.y:
            self.velocity.y -= 1
        elif self.position.y < other.position.y:
            self.velocity.y += 1

        if self.position.z > other.position.z:
            self.velocity.z -= 1
        elif self.position.z < other.position.z:
            self.velocity.z += 1

    def move(self):
        self.position += self.velocity

    @property
    def potential_energy(self):
        return abs(self.position)

    @property
    def kinetic_energy(self):
        return abs(self.velocity)

    @property
    def energy(self):
        return self.kinetic_energy * self.potential_energy

    def __repr__(self):
        return f"{self.name}({self.position})"


def get_input_file():
    return open("../../../input/2019/input12.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)

    lines = list((line.split(",") for line in lines_input_file))
    for i in range(len(lines)):
        lines[i] = (int(cord) for cord in lines[i])
    return lines


def time_step(moons):
    for moon in moons:
        moon.gravity_to_all()
    for moon in moons:
        moon.move()


def time_steps(n_steps, moons):
    for n in range(n_steps):
        time_step(moons)


def part1():
    lines = get_clean_data()
    moons = []
    for line in lines:
        moons.append(Moon(" ", *line))
    time_steps(1000, moons)
    result = sum([moon.energy for moon in moons])
    print(result)


def part2():
    lines = get_clean_data()


def main():
    part1()


if __name__ == '__main__':
    main()
