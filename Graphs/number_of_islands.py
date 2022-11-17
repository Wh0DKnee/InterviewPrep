from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if (
                    r < 0 or c < 0
                    or r >= ROWS or c >= COLS
                    or grid[r][c] == "0"
                    or (r, c) in visited
            ):
                return

            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # either use dfs or bfs. dfs is more readable imo
        def bfs(r, c):
            q = deque()
            q.appendleft((r, c))
            visited.add((r, c,))

            while q:
                r, c = q.pop()
                if (
                        r < 0 or c < 0
                        or r >= ROWS or c >= COLS
                        or grid[r][c] == "0"
                ):
                    continue

                neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for n in neighbors:
                    if n in visited:
                        continue
                    visited.add(n)
                    q.appendleft(n)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    res += 1
                    dfs(r, c)  # or bfs(r,c)

        return res
