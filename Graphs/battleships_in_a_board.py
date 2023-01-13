from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS, COLS, = len(board), len(board[0])
        dirs_row = [0, 0, 1, -1]
        dirs_col = [-1, 1, 0, 0]
        res = 0

        def dfs(r, c):
            if (
                    r < 0 or r >= ROWS or
                    c < 0 or c >= COLS or
                    board[r][c] == '.'
            ):
                return
            board[r][c] = '.'

            for i in range(4):
                rr = r + dirs_row[i]
                cc = c + dirs_col[i]
                dfs(rr, cc)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'X':
                    dfs(row, col)
                    res += 1

        return res
