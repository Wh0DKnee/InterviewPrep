from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(start, combi):
            if len(combi) == k:
                res.append(combi[:])
                return
            if n - start + 1 + len(combi) < k:
                return

            for i in range(start, n + 1):
                combi.append(i)
                dfs(i + 1, combi)
                combi.pop()

        dfs(1, [])
        return res
