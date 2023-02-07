from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        l, res = 0, 0

        for r, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                left_fruit = fruits[l]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                l += 1
            res = max(res, r-l+1)

        return res
