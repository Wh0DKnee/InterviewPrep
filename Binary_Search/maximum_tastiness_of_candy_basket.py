from typing import List
import math


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        ideal_tastiness = math.floor((price[-1] - price[0]) / (k - 1))

        l, r = 0, ideal_tastiness
        res = 0

        while l <= r:
            m = l + ((r - l) // 2)

            if self.isTastinessPossible(price, k, m):
                res = m
                l = m + 1
            else:
                r = m - 1

        return res

    def isTastinessPossible(self, price, k, tastiness):
        next_min = 0

        for p in price:
            if k == 0:
                break
            if p >= next_min:
                k -= 1
                next_min = p + tastiness

        return k == 0
