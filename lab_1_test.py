import unittest
import lab_1


class TestLab1(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(lab_1.two_sum(nums = [2,7,11,15], target = 9),[0,1])
    def test_case2(self):
        self.assertEqual(lab_1.two_sum(nums = [3,2,4], target = 6 ),[1,2])
    def test_case3(self):
        self.assertEqual(lab_1.two_sum(nums = [3,3], target = 6 ),[0,1])
    def test_case4(self):
        self.assertEqual(lab_1.two_sum(nums = [3,5], target = 6), -1)
    
if __name__ == "__main__":
    unittest.main()