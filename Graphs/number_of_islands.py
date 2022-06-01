from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        unvisited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    unvisited.add((i, j))

        count = 0
        while unvisited:
            count += 1
            stack = [unvisited.pop()]
            seen.add(stack[0])
            while stack:
                v = stack.pop()
                neighbors = [(v[0], v[1] - 1), (v[0], v[1] + 1), (v[0] + 1, v[1]), (v[0] - 1, v[1])]
                for neighbor in neighbors:
                    if not self.validIndex(neighbor, grid) or grid[neighbor[0]][neighbor[1]] == "0":
                        continue
                    if neighbor not in seen:
                        stack.append(neighbor)
                        seen.add(neighbor)
                        unvisited.remove(neighbor)
        return count

    def validIndex(self, index, grid):
        return 0 <= index[0] < len(grid) and 0 <= index[1] < len(grid[0])