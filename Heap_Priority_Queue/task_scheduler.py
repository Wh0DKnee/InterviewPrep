from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        taskCounts = defaultdict(int)
        for task in tasks:
            taskCounts[task] += 1

        maxHeap = []
        for k, v in taskCounts.items():
            heapq.heappush(maxHeap, (-v, k))

        cooldownQ = deque()

        while maxHeap or cooldownQ:
            time += 1
            if cooldownQ:
                top = cooldownQ.pop()
                if top is not None:
                    heapq.heappush(maxHeap, top)
            if maxHeap:
                neg_count, task = heapq.heappop(maxHeap)
                neg_count += 1
                if neg_count < 0:
                    while len(cooldownQ) < n:
                        cooldownQ.appendleft(None)
                    cooldownQ.appendleft((neg_count, task))

        return time
