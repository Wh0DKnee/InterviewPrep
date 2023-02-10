from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS
                    or (i, j) in visited
                    or grid[i][j] == 0
            ):
                return

            visited.add((i, j))
            nonlocal size
            size += 1
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                size = 0
                dfs(r, c)
                res = max(res, size)

        return res
