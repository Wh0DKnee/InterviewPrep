from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # idea: max heap, pop twice, push new element
        heap = [-weight for weight in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1, s2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if s1 > s2:
                heapq.heappush(heap, -(s1 - s2))

        return 0 if not heap else -heap[0]