from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))

        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]

        dist = 1
        max_dist = -1

        while q:
            for _ in range(len(q)):
                r, c = q.pop()
                for i in range(4):
                    rr, cc = r + dr[i], c + dc[i]
                    if (0 <= rr < n and 0 <= cc < n
                            and (rr, cc) not in visited):
                        max_dist = dist
                        visited.add((rr, cc))
                        q.appendleft((rr, cc))

            dist += 1

        return max_dist
