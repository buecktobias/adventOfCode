from unittest import TestCase
import unittest
from . import main

MAZE = """
#########
#b.A.@.a#
#########
"""


class TestMaze(TestCase):

    def setUp(self) -> None:
        self.maze = main.Maze()

    def test_get_instance(self):
        pass

    def test_reset(self):
        self.fail()

    def test_object_is_at(self):
        self.fail()

    def test_can_be_walked(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()


def test():
    unittest.main()

if __name__ == '__main__':
    test()