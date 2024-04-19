class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class HeapBasedPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self._bubble_up(len(self.heap) - 1)

    def delete(self):
        if not self.heap:
            return None
        max_priority_node = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._bubble_down(0)
        return max_priority_node.value
м

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[parent_index].priority < self.heap[index].priority:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_priority_index = index
            if left_child_index < len(self.heap) and self.heap[largest_priority_index].priority < self.heap[left_child_index].priority:
                largest_priority_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[largest_priority_index].priority < self.heap[right_child_index].priority:
                largest_priority_index = right_child_index
            if largest_priority_index == index:
                break
            self.heap[largest_priority_index], self.heap[index] = self.heap[index], self.heap[largest_priority_index]
            index = largest_priority_index
