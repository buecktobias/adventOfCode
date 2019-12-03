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
        directions = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, 1),
            "D": (0, -1)
        }
        return directions.get(self.direction)


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


class WirePoint(Point):
    def __init__(self, x, y, steps):
        self.steps = steps
        super().__init__(x, y)


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
        points = {}
        for command in self.commands:
            direction = command.get_direction()
            for step in range(command.steps):
                self.move(*direction)
                points[Point(self.position.x, self.position.y)] = self.steps
        return points


def get_input_file():
    return open("../../../input/2019/input3.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)
    lines_input_file = list([line.split(",") for line in lines_input_file])
    return lines_input_file


def get_intersection_points():
    lines = get_clean_data()
    wires = []
    for line in lines:
        commands = []
        for c in line:
            commands.append(Command(c[0], int(c[1:])))
        wires.append(Wire(commands))

    wire1_points = wires[0].calculate_points()
    wire2_points = wires[1].calculate_points()

    intersection_points = set(wire1_points.keys()) & set(wire2_points.keys())
    intersection_points_steps = []

    for intersection_point in intersection_points:
        steps = wire1_points[intersection_point] + wire2_points[intersection_point]
        new_wire_point = WirePoint(intersection_point.x, intersection_point.y, steps)
        intersection_points_steps.append(new_wire_point)
    return intersection_points_steps


def part1(intersection_points, start_point):
    nearest_intersection = min(intersection_points, key=lambda point: point.distance(start_point))
    return nearest_intersection.distance(start_point)


def part2(intersection_points):
    fewest_steps = min(intersection_points, key=lambda point: point.steps)
    return fewest_steps.steps
    
        
def main():
    intersection_points = get_intersection_points()
    start_point = Point(0, 0)
    print(f"Part1 : {part1(intersection_points, start_point)}")
    print(f"Part2 : {part2(intersection_points)}")


if __name__ == '__main__':
    main()    
