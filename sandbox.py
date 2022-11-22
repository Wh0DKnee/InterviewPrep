from collections import deque


class Solution:
    def orangesRotting(self, grid) -> int:
        distance = [0]
        max_distance = [0]
        ROWS, COLS = len(grid), len(grid[0])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def bfs(r, c):
            visited = {(r, c)}
            q = deque()
            q.append((r, c))

            while q:
                cur = q.pop()
                max_distance[0] = max(max_distance[0], distance[0])

                for i in range(4):
                    nr, nc = cur[0] + dr[i], cur[1] + dc[i]
                    if (
                            0 <= nr < ROWS
                            and 0 <= nc < COLS
                            and grid[nr][nc] == 1
                    ):
                        q.appendleft((nr, nc))
                        visited.add((nr, nc))

                distance[0] += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    bfs(row, col)

        return max_distance[0]


sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))