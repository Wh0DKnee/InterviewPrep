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
                coord = free_coords.pop()
                queen_positions.append(coord)
                x, y = coord
                new_free_coords = free_coords.copy()

                # remove up/down, left/right
                for i in range(n):
                    new_free_coords.discard((x, i))
                    new_free_coords.discard((i, y))

                # remove diagonals
                i, j = x, y
                # print("pos", x, y)
                while i > 0 and j > 0:
                    i -= 1
                    j -= 1

                while i < n and j < n:
                    # print("diag1", i, j)
                    new_free_coords.discard((i, j))
                    i += 1
                    j += 1

                i, j = x, y
                while i > 0 and j < n - 1:
                    i -= 1
                    j += 1

                while i < n and j >= 0:
                    # print("diag2", i, j)
                    new_free_coords.discard((i, j))
                    i += 1
                    j -= 1

                dfs(num_queens + 1, new_free_coords)
                queen_positions.remove(coord)

        initial_coords = set()
        for i in range(n):
            for j in range(n):
                initial_coords.add((i, j))

        dfs(0, initial_coords)
        res = []

        # convert res
        dots = ""
        for k in range(n):
            dots += "."

        for i in range(len(res_positions)):
            res.append([])
            for j in range(n):
                res[i].append(dots)
            for x, y in res_positions[i]:
                res[i][x] = res[i][x][:y] + "Q" + res[i][x][y + 1:]

        return res