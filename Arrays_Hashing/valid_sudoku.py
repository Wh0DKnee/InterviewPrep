from typing import List
from collections import defaultdict


class Solution:
    # O(3n) time and O(n) space complexity
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for i in range(len(board)):
            s.clear()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])

        for i in range(len(board)):
            s.clear()
            for j in range(len(board)):
                # print(i, j, board[i][j], s)
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])

        for i in range(3):
            for j in range(3):
                s.clear()
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] == ".":
                            continue
                        if board[i * 3 + k][j * 3 + l] in s:
                            return False
                        s.add(board[i * 3 + k][j * 3 + l])

        return True

    # O(n) time and O(3n) space complexity
    def isValidSudoku_alternative(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True