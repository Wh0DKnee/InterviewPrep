class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1, 2: 2}
        return self.climb(n, memo)

    def climb(self, n, memo):
        if n in memo:
            return memo[n]

        memo[n] = self.climb(n - 1, memo) + self.climb(n - 2, memo)
        return memo[n]

