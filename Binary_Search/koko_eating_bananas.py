from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        best = int(1e9)
        while left <= right:
            middle = left + ((right - left) // 2)
            time = self.timeItTakes(middle, piles)
            if time <= h:
                best = middle
                right = middle - 1
            else:
                left = middle + 1

        return best

    def timeItTakes(self, speed, piles):
        time = 0
        for p in piles:
            time += int(math.ceil(p / speed))
        return time
