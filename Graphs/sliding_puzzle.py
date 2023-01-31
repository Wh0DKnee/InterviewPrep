from typing import List
import copy
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        solved_board = [[1, 2, 3], [4, 5, 0]]
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]

        q = deque()
        q.append((board, 0))
        visited = set()
        visited.add(self.hashState(board))

        while q:
            state, moves = q.pop()
            if state == solved_board:
                return moves

            r, c = self.getEmptyCoords(state)

            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                if not self.coordsValid(rr, cc):
                    continue
                new_state = copy.deepcopy(state)
                new_state[r][c], new_state[rr][cc] = new_state[rr][cc], new_state[r][c]
                if self.hashState(new_state) in visited:
                    continue
                q.appendleft((new_state, moves + 1))
                visited.add(self.hashState(new_state))

        return -1

    def hashState(self, board):
        l = [str(x) for row in board for x in row]
        s = ''.join(l)
        return s

    def getEmptyCoords(self, board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 0:
                    return r, c

    def coordsValid(self, r, c):
        return 0 <= r < 2 and 0 <= c < 3
