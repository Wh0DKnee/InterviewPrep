from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res_positions = []
        queen_positions = []

        def dfs(num_queens, free_coords):
            if num_queens == n:
                res_positions.append(queen_positions.copy())
                return

            if not free_coords:
                return

            while free_coords:
                coord = free_coords.pop()  # once we've checked a coord, we never need to check it again
                                           # because we've covered all combinations involving this coord
                queen_positions.append(coord)
                new_free_coords = self.remove_attacked_squares(free_coords, coord[0], coord[1], n)
                dfs(num_queens + 1, new_free_coords)
                queen_positions.remove(coord)

        initial_coords = set()
        for i in range(n):
            for j in range(n):
                initial_coords.add((i, j))

        dfs(0, initial_coords)
        res = []

        # convert res to proper format
        dots = ""
        for k in range(n):
            dots += "."

        for i in range(len(res_positions)):
            res.append([])
            for j in range(n):
                res[i].append(dots)
            for x, y in res_positions[i]:
                res[i][x] = res[i][x][:y] + 'Q' + res[i][x][y + 1:]

        return res

    def remove_attacked_squares(self, coords, x, y, n):
        new_coords = coords.copy()

        # remove up/down, left/right
        for i in range(n):
            new_coords.discard((x, i))
            new_coords.discard((i, y))

        # remove diagonals
        i, j = x, y
        while i > 0 and j > 0:
            i -= 1
            j -= 1

        while i < n and j < n:
            new_coords.discard((i, j))
            i += 1
            j += 1

        i, j = x, y
        while i > 0 and j < n - 1:
            i -= 1
            j += 1

        while i < n and j >= 0:
            new_coords.discard((i, j))
            i += 1
            j -= 1

        return new_coords
