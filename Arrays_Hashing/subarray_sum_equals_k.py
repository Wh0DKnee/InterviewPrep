from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = nums[:]
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        d = defaultdict(int)
        d[0] = 1
        res = 0
        for i in range(len(prefix)):
            needed = prefix[i] - k
            if needed in d:
                res += d[needed]
            d[prefix[i]] += 1

        return res
