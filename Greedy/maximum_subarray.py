import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        cur = -math.inf

        for num in nums:
            cur = max(num, num + cur)
            res = max(res, cur)

        return res
    