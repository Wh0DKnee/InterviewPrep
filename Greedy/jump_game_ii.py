from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        goal = len(nums) - 1

        while goal > 0:
            for i in range(goal - 1, -1, -1):
                dist = goal - i
                if nums[i] >= dist:
                    new_goal = i
            goal = new_goal
            jumps += 1

        return jumps

# Linear solution possible by doing a BFS: https://youtu.be/dJ7sWiOoK7g
