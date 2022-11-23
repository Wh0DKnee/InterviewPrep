from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        dfs_order = []
        cycle_start = [-1]

        def dfs(v, parent):
            visited.add(v)
            dfs_order.append(v)

            for nei in adj[v]:
                if nei == parent:
                    continue
                if nei in visited:
                    cycle_start[0] = nei
                    dfs_order.append(nei)
                    return True
                cycle_found = dfs(nei, v)
                if cycle_found:
                    return True
            dfs_order.pop()

        dfs(edges[0][0], None)
        # [5, 1, 2, 3, 4, 1]
        cycle_start_index = dfs_order.index(cycle_start[0])
        cycle = dfs_order[cycle_start_index:]
        print(cycle)
        orderMap = {}
        for i, (a, b) in enumerate(edges):
            orderMap[(a, b)] = i

        last_edge = 0
        for i in range(len(cycle) - 1):
            smaller = cycle[i] if cycle[i] < cycle[i + 1] else cycle[i + 1]
            bigger = cycle[i] if cycle[i] > cycle[i + 1] else cycle[i + 1]
            last_edge = max(last_edge, orderMap[(smaller, bigger)])

        return edges[last_edge]



