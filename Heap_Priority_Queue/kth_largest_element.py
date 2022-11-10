import math


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.vals = [math.inf]
        for num in nums:
            self.insert(num)
        self.k = k

    def insert(self, num):

    def extract_max(self):
        res = self.vals[0]
        self.vals
        heapify_down(0)
        return res

    def heapify_down(index):
        if index >= self.

    def add(self, val: int) -> int:
        self.vals.append(val)
        self.vals.sort()
        return self.vals[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)