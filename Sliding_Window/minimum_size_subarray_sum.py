from typing import List
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = math.inf

        for r, num in enumerate(nums):
            total += num
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if res == math.inf else res
