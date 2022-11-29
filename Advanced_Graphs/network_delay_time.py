import math
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman Ford
        dists = []
        for i in range(n):
            dists.append(math.inf)

        dists[k - 1] = 0
        for i in range(n):
            for a, b, cost in times:
                dists[b - 1] = min(dists[b - 1], dists[a - 1] + cost)

        res = max(dists)
        return -1 if res == math.inf else res

    def networkDelayTime_Dijkstra(self, times, n, k):
        adj = defaultdict(list)
        dists = {}
        for a, b, cost in times:
            adj[a].append((cost, b))

        for i in range(1, n + 1):
            dists[i] = math.inf

        visited = set()
        minH = [(0, k)]

        while minH:
            dist, cur = heapq.heappop(minH)
            if cur in visited:
                continue
            dists[cur] = min(dists[cur], dist)
            visited.add(cur)
            if len(visited) == n:
                # print(dists)
                return max(list(dists.values()))

            for w, nei in adj[cur]:
                heapq.heappush(minH, (dists[cur] + w, nei))

        return -1
