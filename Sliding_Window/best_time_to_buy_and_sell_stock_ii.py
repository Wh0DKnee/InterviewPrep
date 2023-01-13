from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res, prev_r_price = 0, 0, -math.inf
        prices.append(-math.inf)

        for r in range(len(prices)):
            prev_win = prev_r_price - prices[l]

            if prices[r] < prices[l]:
                l = r
            if prev_r_price > prices[r] and prev_win > 0:
                res += prev_win
                l = r

            prev_r_price = prices[r]

        return res

    def maxProfitGeniusSolution(self, prices):
        # if tomorrow's price is higher than today's: buy
        # otherwise don't.
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
