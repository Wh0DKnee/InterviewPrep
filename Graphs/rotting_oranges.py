from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_dist = 0
        ROWS, COLS = len(grid), len(grid[0])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        while q:
            cur_r, cur_c, cur_dist = q.pop()
            max_dist = max(max_dist, cur_dist)

            for i in range(4):
                nr, nc = cur_r + dr[i], cur_c + dc[i]
                if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                ):
                    q.appendleft((nr, nc, cur_dist + 1))
                    grid[nr][nc] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return max_dist
