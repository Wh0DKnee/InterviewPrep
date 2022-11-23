from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dist = self.manhattan(points[i], points[j])
                    adj[i].append((dist, j))

        res = 0
        visited = set()
        minH = [(0, 0)]

        while len(visited) < N:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue

            visited.add(node)
            res += cost
            for cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minH, (cost, nei))

        return res

    def manhattan(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
