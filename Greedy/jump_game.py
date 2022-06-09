from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_index = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            dist = cur_index - i
            if nums[i] >= dist:
                cur_index = i
        return cur_index == 0