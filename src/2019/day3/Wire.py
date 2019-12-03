from typing import List


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


class Wire:
    def __init__(self, commands):  # commands = R5,U8 ...
        self.commands = commands
        self.position = Point(0, 0)

    def move(self, x, y):
        self.position.x = x
        self.position.y = y

    def calculate_points(self) -> List[Point]:
        points = []
        for command in self.commands:
            dir_x, dir_y = command.get_direction()
            for step in range(command.steps):
                new_x = self.position.x + dir_x
                new_y = self.position.y + dir_y
                self.move(new_x, new_y)
                points.append(self.position)
        return points
