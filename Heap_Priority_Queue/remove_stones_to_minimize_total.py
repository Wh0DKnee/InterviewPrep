from typing import List
import heapq
from math import ceil


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)

        for i in range(k):
            largest = -heapq.heappop(piles)
            halved = ceil(largest/2)
            heapq.heappush(piles, -halved)

        return -sum(piles)
