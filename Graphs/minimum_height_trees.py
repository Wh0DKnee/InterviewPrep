from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(set)

        for start, end in edges:
            adj[start].add(end)
            adj[end].add(start)

        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        while leaves:
            new_leaves = []
            for leaf in leaves:
                for nei in adj[leaf]:
                    adj[nei].remove(leaf)
                    if len(adj[nei]) == 1:
                        new_leaves.append(nei)

            if len(new_leaves) == 0:
                return leaves
            leaves = new_leaves
