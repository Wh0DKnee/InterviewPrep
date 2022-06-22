from typing import List


# works because the items are pushed onto the stack in decreasing order (if an item
# is larger, we pop from the stack instead, until we encounter an item that isn't)
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
