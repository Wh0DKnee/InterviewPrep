from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] < prev[1]:  # overlap
                res += 1
                prev = prev if prev[1] < cur[1] else cur
            else:
                prev = cur

        return res
