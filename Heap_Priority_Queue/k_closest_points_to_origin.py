from typing import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(math.sqrt(p[0] ** 2 + p[1] ** 2), p) for p in points]
        res = []
        heapq.heapify(dists)

        for i in range(k):
            _, p = heapq.heappop(dists)
            res.append(p)

        return res
