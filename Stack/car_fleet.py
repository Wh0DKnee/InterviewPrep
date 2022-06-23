from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        dur_remaining = [(target - position[i]) / speed[i] for i in range(len(position))]
        tup = zip(position, dur_remaining)
        for _, r in sorted(tup, reverse=True):
            stack.append(r)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
