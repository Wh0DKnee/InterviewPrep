from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):  # returns true if dfs touches border
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 1:
                return False

            grid[row][col] = 1
            is_border = row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1
            r1 = dfs(row + 1, col)
            r2 = dfs(row - 1, col)
            r3 = dfs(row, col + 1)
            r4 = dfs(row, col - 1)
            return is_border or r1 or r2 or r3 or r4

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    continue
                if not dfs(r, c):
                    res += 1

        return res

