class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        memo = {len(cost) - 1: cost[len(cost) - 1], len(cost) - 2: cost[len(cost) - 2]}
        return self.minCost(0, cost, memo)

    def minCost(self, n, cost, memo):
        if n in memo:
            return memo[n]

        memo[n] = cost[n] + min(self.minCost(n + 1, cost, memo), self.minCost(n + 2, cost, memo))
        return memo[n]

    # TODO: easier with tabulization
