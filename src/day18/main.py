# Created by Tobias Bück at 2019-12-22 11:43:51.549549
# Solution of day 18 of advent of Code 2019
# 
# INPUTS
from typing import List, Dict, Union, Type, Optional

import utility  # helper methods
import abc


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}, {self.y}"


class MazeObject:
    @abc.abstractmethod
    def can_walk_through(self) -> bool:
        pass

    @abc.abstractmethod
    def __repr__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class Street(MazeObject):
    def can_walk_through(self) -> bool:
        return True

    def __repr__(self):
        return "."

    def __str__(self):
        return self.__repr__()


class Key(MazeObject):
    def __init__(self, identifier):
        self.identifier: str = identifier

    def can_walk_through(self) -> bool:
        return True

    def __repr__(self):
        return self.identifier

    def __str__(self):
        return self.__repr__()


class PlayerStartPosition(MazeObject):
    def can_walk_through(self) -> bool:
        return True

    def __repr__(self):
        return "@"

    def __str__(self):
        return self.__repr__()


class Door(MazeObject):
    def __init__(self, identifier):
        self.identifier: str = identifier
        self.is_open: bool = False

    def is_right_key(self, key: Key) -> bool:
        return key.identifier.capitalize() == self.identifier.capitalize()

    def open(self, key: Key) -> None:
        if self.is_right_key(key):
            self.is_open = True

    def can_walk_through(self) -> bool:
        return self.is_open

    def __repr__(self):
        return self.identifier

    def __str__(self):
        return self.__repr__()


class Wall(MazeObject):
    def can_walk_through(self) -> bool:
        return False

    def __repr__(self):
        return "#"

    def __str__(self):
        return self.__repr__()


class Player:
    def __init__(self, start_position: Position):
        self.keys: List[Key] = []
        self.start_position = start_position
        self.position: Position = start_position
        self.steps_taken = 0

    def move_to(self, position: Position):
        self.position = position

    def reset(self):
        self.position = self.start_position

    def __repr__(self):
        return f"Player is at {self.position}"

    def __str__(self):
        return self.__repr__()


class Maze:
    instance = None

    def __init__(self, matrix):
        self.start_matrix: List[List[MazeObject]] = matrix
        self.matrix: List[List[MazeObject]] = matrix
        if self.instance is None:
            self.instance = self

    def get_players_start_position(self) -> Optional[Position]:
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if type(self.matrix[y][x]) == PlayerStartPosition:
                    return Position(x, y)
        return None

    @classmethod
    def get_instance(cls):
        return cls.instance

    def reset(self):
        self.matrix = self.start_matrix.copy()

    def object_is_at(self, position: Position) -> MazeObject:
        return self.matrix[position.y][position.x]

    def can_be_walked(self, position: Position):
        return self.object_is_at(position).can_walk_through()

    def shortest_path(self, from_position: Position, to_position: Position) -> Optional[int]:
        pass

    def __repr__(self):
        string = ""

        for row in self.matrix:
            for el in row:
                string += el.__repr__()
            string += "\n"
        return string


def get_input_file():
    return open("../../input/2019/input18.txt")


def str_to_maze_object(string: str) -> MazeObject:  # POSITION ??????
    maze_objects_dict: Dict[str, Type[Union[Wall, PlayerStartPosition, Street]]] = \
        {
            "#": Wall,
            "@": PlayerStartPosition,
            ".": Street,
        }
    if string in maze_objects_dict:
        return maze_objects_dict[string]()

    else:
        if string.islower():
            return Key(string)
        else:
            return Door(string)


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)

    maze_matrix = []
    for y in range(len(lines_input_file)):
        row = []
        for element in lines_input_file[y]:
            row.append(str_to_maze_object(element))
        maze_matrix.append(row)

    maze = Maze(maze_matrix)
    player = maze.get_players_start_position()
    return maze, player


def part1():
    maze, player = get_clean_data()
    print(maze)
    print(player)


def part2():
    lines = get_clean_data()


def main():
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")


if __name__ == '__main__':
    main()
