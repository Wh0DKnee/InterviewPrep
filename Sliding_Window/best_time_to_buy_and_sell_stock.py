class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0

        for r in range(len(prices)):
            while (prices[r] - prices[l] < 0):
                l += 1
            best = max(best, prices[r] - prices[l])

        return best
