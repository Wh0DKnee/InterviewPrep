from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(i, j, remainder):
            if not remainder:
                return True
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[0]):
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != remainder[0]:
                return False

            visited.add((i, j))
            remainder = remainder[1:]
            s1 = dfs(i + 1, j, remainder)
            s2 = dfs(i - 1, j, remainder)
            s3 = dfs(i, j - 1, remainder)
            s4 = dfs(i, j + 1, remainder)
            visited.remove((i, j))
            return s1 or s2 or s3 or s4

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.clear()
                if dfs(i, j, word):
                    return True
        return False


