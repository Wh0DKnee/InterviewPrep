from typing import List
from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        visited = set()

        def has_cycle(node, parent):
            if node in visited:
                return True
            visited.add(node)

            for nei in adj[node]:
                if nei != parent and has_cycle(nei, node):
                    return True

            return False

        return False if has_cycle(0, None) or len(visited) != n else True
