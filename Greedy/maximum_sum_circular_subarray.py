from typing import List
import math


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, -math.inf, 0, math.inf, 0
        for num in nums:
            curMax += num
            maxSum = max(maxSum, curMax)
            curMax = max(curMax, 0)

            curMin += num
            minSum = min(minSum, curMin)
            curMin = min(curMin, 0)

            total += num
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
