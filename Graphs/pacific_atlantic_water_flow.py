from typing import List


class Solution:
    # brute force idea: run a DFS from each cell, early out if both oceans have been reached,
    # if not, the cell cannot drain water to both oceans

    # better idea: run a DFS from each cell, but early out once we reach a cell for which we've already
    # finished DFS
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachable = {}
        visited = set()
        done = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                reachable[(i, j)] = set()
                if i == 0 or j == 0:
                    reachable[(i, j)].add('p')
                if j == len(heights[0]) - 1 or i == len(heights) - 1:
                    reachable[(i, j)].add('a')

        def dfs(start, v):
            visited.add(v)
            reachable[start].update(reachable[v])
            neighbors = [(v[0], v[1] - 1), (v[0], v[1] + 1), (v[0] + 1, v[1]), (v[0] - 1, v[1])]
            for nei in neighbors:
                if not self.validNeighbor(v, nei, heights):
                    continue
                if nei in done:
                    reachable[start].update(reachable[nei])
                elif nei not in visited:
                    dfs(start, nei)
            done.add(start)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited.clear()
                dfs((i, j), (i, j))

        res = []
        for key, value in reachable.items():
            if len(value) == 2:
                res.append(list(key))

        return res

    def validNeighbor(self, index_self, index_neighbor, heights):
        valid_index = 0 <= index_neighbor[0] < len(heights) and 0 <= index_neighbor[1] < len(heights[0])
        if not valid_index:
            return False
        return heights[index_neighbor[0]][index_neighbor[1]] <= heights[index_self[0]][index_self[1]]


sol = Solution()
h = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(sol.pacificAtlantic(h))
