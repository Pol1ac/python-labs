import unittest
from src.boyer_moore import boyer_moore

class TestBoyerMoore(unittest.TestCase):
    def test_single_occurrence(self):
        haystack = "queue"
        needle = "ue"
        self.assertEqual(boyer_moore(haystack, needle), [1,3])

    def test_multiple_occurrences(self):
        haystack = "abracadabra"
        needle = "abra"
        self.assertEqual(boyer_moore(haystack, needle), [0, 7])

    def test_no_occurrence(self):
        haystack = "hello"
        needle = "world"
        self.assertEqual(boyer_moore(haystack, needle), [])

    def test_empty_needle(self):
        haystack = "abcdef"
        needle = ""
        self.assertEqual(boyer_moore(haystack, needle), [])

if __name__ == "__main__":
    unittest.main()
