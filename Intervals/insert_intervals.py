from typing import List
import math


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res

    def insert_naive(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        first, last = math.inf, -1

        for i in range(len(intervals)):
            if self.overlaps(intervals[i], newInterval):
                first = min(first, i)
                last = i

        # no overlaps
        if last == -1:
            insert_index = len(intervals)
            for i in range(len(intervals)):
                if intervals[i][0] > newInterval[0]:
                    insert_index = i
                    break
            intervals.insert(insert_index, newInterval)
            return intervals

        res = []
        left, right = 0, 0
        for i in range(len(intervals)):
            if i < first or i > last:
                res.append(intervals[i])
            if i == first:
                left = min(newInterval[0], intervals[i][0])
            if i == last:
                right = max(newInterval[1], intervals[i][1])
                res.append([left, right])
        return res

    def overlaps(self, a, b):
        return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]