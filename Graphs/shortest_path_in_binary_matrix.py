from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        dr = [0, 0, 1, -1, -1, 1, -1, 1]
        dc = [1, -1, 0, 0, -1, 1, 1, -1]
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.pop()
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1:
                    continue
                if r == ROWS - 1 and c == COLS - 1:
                    return dist

                for i in range(8):
                    rr, cc = r + dr[i], c + dc[i]
                    if (rr, cc) not in visited:
                        q.appendleft((rr, cc))
                        visited.add((rr, cc))
            dist += 1

        return -1
