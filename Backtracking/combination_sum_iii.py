from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(remain, options, combi):
            if remain == 0 and len(combi) == k:
                res.append(combi[:])
                return
            if remain <= 0 or len(options) == 0:
                return

            dfs(remain, options[1:], combi)
            combi.append(options[0])
            dfs(remain - options[0], options[1:], combi)
            combi.pop()

        dfs(n, [1, 2, 3, 4, 5, 6, 7, 8, 9], [])
        return res
