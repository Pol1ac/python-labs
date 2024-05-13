import unittest
from src.cards_on_board import min_square_size


class TestLab2(unittest.TestCase):
     def test_case1(self):
        self.assertEqual(min_square_size(10, 2, 3),9)
     def test_case2(self):
        self.assertEqual(min_square_size(2, 1000000000, 999999999), 1999999998)
     def test_case3(self):
        self.assertEqual(min_square_size(4, 1, 1), 2)
    
if __name__ == "__main__":
    unittest.main()
