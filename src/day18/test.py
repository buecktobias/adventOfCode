import unittest
from . import main
from . import test_maze


class MazeMain(unittest.TestCase):
    def test_something(self):
        lol = main.Maze([[0, 1]])
        self.assertEqual(type(lol), main.Maze.__class__)


if __name__ == '__main__':
    test_maze.test()
    unittest.main()


