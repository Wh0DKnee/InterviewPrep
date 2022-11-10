from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
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
            dfs(options[1:], remainder - options[0])
            subset.pop()

            change = len(options)
            cur = options[0]
            for i in range(len(options)):
                if cur != options[i]:
                    change = i
                    break

            dfs(options[change:], remainder)

        dfs(candidates, target)
        return res
