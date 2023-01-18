from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]

        for i in range(1, len(nums)):
            self.sums[i] = nums[i] + self.sums[i-1]

    def update(self, index: int, val: int) -> None:
        old = self.sums[index]
        self.sums[index] = val
        if index > 0:
            self.sums[index] += self.sums[index - 1]
        diff = self.sums[index] - old

        for i in range(index+1, len(self.sums)):
            self.sums[index] += diff

    def sumRange(self, left: int, right: int) -> int:
        print(self.sums)
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1, 3, 5])
numArray.sumRange(0, 2)
numArray.update(1, 2)
numArray.sumRange(0, 2)
