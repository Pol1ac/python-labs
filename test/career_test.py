import unittest
from src.career import dfs


class CareerPathTest(unittest.TestCase):

    def setUp(self):
        self.L = 3
        self.levels = [[10, 20, 30], [40, 50], [60]]
        self.max_experience = [0]

    def test_dfs_basic(self):
        """Tests DFS with a simple input."""
        dfs(0, 0, self.levels[0][0], self.max_experience)
        self.assertEqual(self.max_experience[0], 130) 
    def test_dfs_multiple_paths(self):
        """Tests DFS with multiple paths and different starting positions."""
        dfs(0, 1, self.levels[0][1], self.max_experience)  
        self.assertEqual(self.max_experience[0], 140)  

    def test_dfs_empty_level(self):
        """Tests DFS with an empty level."""
        self.levels.append([]) 
        with self.assertRaises(IndexError):
            dfs(0, 0, self.levels[0][0], self.max_experience) 

    def test_dfs_invalid_input(self):
        """Tests DFS with invalid input data."""
        with self.assertRaises(ValueError):
            self.L = -1  
            dfs(0, 0, self.levels[0][0], self.max_experience)

        with self.assertRaises(ValueError):
            self.levels = [[10], [20, "invalid"]]  
            dfs(0, 0, self.levels[0][0], self.max_experience)

if __name__ == '__main__':
    unittest.main()
