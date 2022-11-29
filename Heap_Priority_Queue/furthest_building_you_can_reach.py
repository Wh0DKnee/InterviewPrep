from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []

        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                continue
            heapq.heappush(minHeap, diff)
            if len(minHeap) > ladders:
                bricks -= heapq.heappop(minHeap)
            if bricks < 0:
                return i - 1

        return len(heights) - 1

    # TLE
    def furthestBuilding_DP(self, heights, bricks, ladders):
        memo = {}

        # 5, 3, 5
        def dfs(index, bs, ls):
            if (index, bs, ls) in memo:
                return memo[(index, bs, ls)]
            if bs < 0 or ls < 0:
                return index - 1
            if index == len(heights) - 1:  # made it to the end
                return index

            if heights[index + 1] <= heights[index]:
                return dfs(index + 1, bs, ls)

            diff = heights[index + 1] - heights[index]
            memo[(index, bs, ls)] = max(dfs(index + 1, bs - diff, ls), dfs(index + 1, bs, ls - 1))
            return memo[(index, bs, ls)]

        return dfs(0, bricks, ladders)