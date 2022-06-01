from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(options, remainder):
            if remainder == 0:
                res.append(subset.copy())
                return
            if remainder < 0:
                return
            if not options:
                return

            subset.append(options[0])
            dfs(options, remainder - options[0])
            subset.pop()
            dfs(options[1:], remainder)

        dfs(candidates, target)
        return res
