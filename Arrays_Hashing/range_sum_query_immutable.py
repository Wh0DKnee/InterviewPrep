from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # calculate prefix sums
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]

        for i in range(1, len(nums)):
            self.sums[i] = nums[i] + self.sums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
