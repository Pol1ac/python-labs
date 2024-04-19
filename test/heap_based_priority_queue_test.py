import lab_4
import unittest

class TestHeapBasedPriorityQueue(unittest.TestCase):

    def test_insert_and_delete_max(self):
        pq = HeapBasedPriorityQueue()
        pq.insert(3, 3)
        pq.insert(1, 1)
        pq.insert(5, 5)
        pq.insert(2, 2)
        pq.insert(4, 4)
        self.assertEqual(pq.peek(), 5)
        pq.delete_max()
        self.assertEqual(pq.peek(), 4)
       
