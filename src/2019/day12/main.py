# Created by Tobias Bück at 2019-12-13 00:00:53.987793
# Solution of day 12 of advent of Code 2019
# 
# INPUTS 
import utility  # helper methods
import re
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import juggle_axes


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def cords(self):
        return self.x, self.y, self.z

    @cords.setter
    def cords(self, new_cords):
        self.x = new_cords[0]
        self.y = new_cords[1]
        self.z = new_cords[2]

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
        for i in range(len(self.position.cords)):
            if self.position.cords[i] > other.position.cords[i]:
                vel = self.velocity.cords
                vel[i] += 1
                self.velocity.cords = vel

    def move(self):
        self.position += self.velocity

    @classmethod
    def get_energy(cls):
        return sum([moon.energy for moon in cls.moons])

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
        return f"{self.name} pos=({self.position}) vel=({self.velocity})"


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


class MoonAnimation:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = p3.Axes3D(self.fig)
        self.data = self.get_data()
        self.scat = None
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=40, interval=20, init_func=self.setup_plot, blit=True)
        self.colors = ['red', 'green', 'blue', 'yellow']

    def get_data(self):
        moons = Moon.moons
        while True:
            time_step(moons)
            yield moons_cords(moons)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        xs, ys, zs = next(self.data)
        self.scat = self.ax.scatter(xs, ys, zs,c =self.colors)
        return self.scat,

    def update(self, i):
        xs, ys, zs = next(self.data)
        self.scat._offsets3d = juggle_axes(xs, ys, zs, 'z')
        return self.scat,

    def show(self):
        plt.show()

    def save(self):
        writer = animation.FFMpegWriter(fps=2, codec='libx264')
        self.ani.save("3dmoons_animation.mp4", writer=writer)


def moons_cords(moons):
    xs = []
    ys = []
    zs = []
    for moon in moons:
        xs.append(moon.position.x)
        ys.append(moon.position.y)
        zs.append(moon.position.z)
    return xs, ys, zs


def part1():
    lines = get_clean_data()
    moons = []
    for line in lines:
        moons.append(Moon(" ", *line))
    time_steps(1000, moons)
    result = Moon.get_energy()
    print(result)


def energy_plot():
    amount_data = 10000
    xs = list(range(amount_data))
    ys = []
    for i in range(amount_data):
        ys.append(Moon.get_energy())
        time_step(Moon.moons)
    plt.plot(xs, ys)
    plt.show()


def _2d_positions_plot(cord: int):# 0 -> x, 1 -> y, 2-> z
    ys_moons = []
    amount_data = 1000
    for i in range(amount_data):
        ys = []
        for moon in Moon.moons:
            ys.append(moon.position.cords[cord])
        ys_moons.append(ys)
        time_step(Moon.moons)
    for i in range(len(Moon.moons)):
        xs = list(range(amount_data))
        ys = [_ys[i] for _ys in ys_moons]
        plt.plot(xs, ys)
    plt.show()


def part2():
    lines = get_clean_data()


def main():
    part1()
    lines = get_clean_data()
    moons = []
    for line in lines:
        moons.append(Moon(" ", *line))

    _2d_positions_plot(0)
    _2d_positions_plot(1)
    _2d_positions_plot(2)


if __name__ == '__main__':
    main()
