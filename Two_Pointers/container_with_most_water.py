from typing import List
import math


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = -math.inf

        while l < r:
            water = (r - l) * min(height[l], height[r])
            res = max(res, water)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res
