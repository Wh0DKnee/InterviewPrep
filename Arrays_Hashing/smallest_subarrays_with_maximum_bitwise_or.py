from typing import List
import math


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        lookup = [-math.inf] * 30  # 10^9 is limit of input, and 10^9 in binary has 30 digits.
        res = []
        for i in range(len(nums) - 1, -1, -1):
            most_right = i
            for d in range(30):
                if nums[i] & (1 << d):
                    lookup[d] = i
                most_right = max(most_right, lookup[d])
            res.append(most_right - i + 1)

        res.reverse()
        return res
