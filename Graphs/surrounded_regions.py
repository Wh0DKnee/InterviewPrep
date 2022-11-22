from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        cur = []
        to_flip = []
        do_flip = True
        visited = set()

        def dfs(r, c):
            nonlocal do_flip
            if (
                    (r, c) in visited
                    or r >= ROWS or r < 0
                    or c >= COLS or c < 0
                    or board[r][c] == "X"
            ):
                return
            visited.add((r, c))
            cur.append((r, c))
            if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                do_flip = False
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and board[row][col] == "O":
                    do_flip = True
                    cur = []
                    dfs(row, col)
                    if do_flip:
                        to_flip.extend(cur)

        for (row, col) in to_flip:
            board[row][col] = "X"

