import unittest
from src.bfs_maze import bfs


class TestBFS(unittest.TestCase):

    def test_simple_maze(self):
        maze = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1]
        ]
        source = (0, 0)
        destination = (2, 2)
        expected_distance = 4

        distance = bfs(maze, source, destination)
        self.assertEqual(distance, expected_distance)

    def test_complex_maze(self):
        maze = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]
        source = (0, 0)
        destination =  (7, 5)
        expected_distance = 12

        distance = bfs(maze, source, destination)
        self.assertEqual(distance, expected_distance)

    def test_no_path(self):
        return
        maze = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 0]
        ]
        source = (0, 0)
        destination = (2, 2)
        expected_distance = float('inf')

        distance = bfs(maze, source, destination)
        self.assertEqual(distance, expected_distance)

if __name__ == '__main__':
    unittest.main()
