from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(lambda: 0)
        frequ = [[] for i in range(len(nums) + 1)]

        for i in nums:
            d[i] += 1

        for key, val in d.items():
            frequ[val].append(key)

        res = []
        for key in reversed(frequ):
            if key:
                res.extend(key)
            if len(res) >= k:
                break

        return res
