from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []
        deleted = set()

        for i in range(k - 1):
            heapq.heappush(maxHeap, (-nums[i], i))

        for i in range(k - 1, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            while maxHeap[0] in deleted:
                popped = heapq.heappop(maxHeap)
                deleted.remove(popped)
            res.append(-maxHeap[0][0])
            if i - (k - 1) >= 0:
                deleted.add((-nums[i - (k - 1)], i - (k - 1)))

        return res
