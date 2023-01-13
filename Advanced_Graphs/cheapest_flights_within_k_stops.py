from typing import List
from collections import defaultdict, deque
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # handle edge case so we don't need to worry about it
        if src == dst:
            return 0

        # build adjacency list
        adj_list = defaultdict(list)
        for i in range(len(flights)):
            start, to, price = flights[i]
            adj_list[start].append((to, price))

        # run optimized BFS (stop when #stops > k or when the cost exceeds the current best)
        # that allows visiting the same node multiple times if the cost is reduced
        q = deque()
        q.append((src, 0, 0))
        visited = defaultdict(int)
        visited[src] = 0
        res = math.inf

        while q:
            cur, stops, cost = q.pop()
            if stops > k or cost > res:
                continue

            for nei, price in adj_list[cur]:
                if nei == dst:
                    res = min(res, cost + price)
                    continue
                if nei not in visited or cost + price < visited[nei]:
                    visited[nei] = cost + price
                    q.appendleft((nei, stops + 1, cost + price))

        return -1 if res == math.inf else res
