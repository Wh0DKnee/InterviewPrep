from typing import List
import math


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = math.inf

        while l <= r:
            # possible optimization: return nums[l] if nums[l] < nums[r]
            m = l + ((r - l) // 2)
            if nums[l] <= nums[m]:
                minimum = min(minimum, nums[l])
                l = m + 1
            else:
                minimum = min(minimum, nums[m])
                r = m - 1
        return minimum
