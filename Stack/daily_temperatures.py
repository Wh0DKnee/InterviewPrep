from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = []
        res = [0] * len(t)
        for i in range(len(t)):
            while stack and t[stack[-1]] < t[i]:
                top = stack.pop()
                res[top] = (i - top)
            stack.append(i)

        return res
