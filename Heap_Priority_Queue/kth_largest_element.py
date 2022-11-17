from typing import List


class KthLargest:

    # Idea: We maintain a min heap with the k largest elements.
    # The k-th largest element will therefore always be at the root.
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k and val <= self.heap[0]:
            return self.heap[0]

        self.heap.append(val)
        self.heapify_up()

        if len(self.heap) > self.k:
            self.popMin()

        return self.heap[0]

    def heapify_up(self):
        index = len(self.heap) - 1
        # Bubble up
        while parent(index) >= 0 and self.heap[parent(index)] > self.heap[index]:
            self.heap[parent(index)], self.heap[index] = self.heap[index], self.heap[parent(index)]
            index = parent(index)

    def popMin(self):
        min_ = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return min_

    def heapify_down(self):
        # Bubble down
        index = 0
        heap_len = len(self.heap)
        while True:
            left_child = None if left(index) >= heap_len else self.heap[left(index)]
            right_child = None if right(index) >= heap_len else self.heap[right(index)]
            if right_child is None and left_child is None:
                break
            if right_child is None:
                smaller_index = left(index)
                smaller = left_child
            elif left_child is None:
                smaller_index = right(index)
                smaller = right_child
            else:
                smaller = left_child if left_child < right_child else right_child
                smaller_index = left(index) if left_child < right_child else right(index)

            if smaller < self.heap[index]:
                self.heap[index], self.heap[smaller_index] = self.heap[smaller_index], self.heap[index]
                index = smaller_index
            else:
                break


def left(index: int) -> int:
    return index * 2 + 1


def right(index: int) -> int:
    return index * 2 + 2


def parent(index: int) -> int:
    return (index - 1) // 2

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)