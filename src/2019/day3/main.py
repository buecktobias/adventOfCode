# Created by Tobias Bück at 2019-12-02 12:57:39.185793
# Solution of day 3 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods


class Command:
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = steps

    def get_direction(self):
        if self.direction == "L":
            return -1, 0
        elif self.direction == "R":
            return 1, 0
        elif self.direction == "U":
            return 0, 1
        elif self.direction == "D":
            return 0, -1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        diff_x = abs(other.x - self.x)
        diff_y = abs(other.y - self.y)
        return diff_x + diff_y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))


class WirePoint:
    def __init__(self, point, steps):
        self.point = point
        self.steps = steps

    def __eq__(self, other):
        return self.point.x == other.point.x and self.point.y == other.point.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.point.x, self.point.y))


class Wire:
    def __init__(self, commands):  # commands = R5,U8 ...
        self.commands = commands
        self.position = Point(0, 0)
        self.steps = 0

    def move(self, x, y):
        self.position.x += x
        self.position.y += y
        self.steps += 1

    def calculate_points(self):
        points = set()
        for command in self.commands:
            direction = command.get_direction()
            for step in range(command.steps):
                self.move(*direction)
                points.add(Point(self.position.x, self.position.y))
        return points


def get_input_file():
    return open("../../../input/2019/input3.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)
    lines_input_file = list([line.split(",") for line in lines_input_file])
    return lines_input_file


def part1():
    lines = get_clean_data()
    wires = []
    for line in lines:
        commands = []
        for c in line:
            commands.append(Command(c[0], int(c[1:])))
        wires.append(Wire(commands))

    wire1_points = wires[0].calculate_points()
    wire2_points = wires[1].calculate_points()

    intersection_points = []

    for point1 in wire1_points:
        if point1 in wire2_points:
            intersection_points.append(point1)

    start_point = Point(0, 0)
    nearest_intersection = min(intersection_points, key=lambda point: point.distance(start_point))
    print(nearest_intersection.distance(start_point))   # solution part 1


def part2():
    lines = get_clean_data()   
    
        
def main():
    part1()
    part2()


if __name__ == '__main__':
    main()    
