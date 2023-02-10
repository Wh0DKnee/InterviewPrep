class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0 for _ in range(n)] for _ in range(m)]
        ways[0] = [1] * n
        for r in range(m):
            ways[r][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                ways[r][c] = ways[r - 1][c] + ways[r][c - 1]

        return ways[m - 1][n - 1]
