from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        lookup = {}
        for idx, num in enumerate(nums):
            lookup[num] = idx

        for elem, replacement in operations:
            nums[lookup[elem]] = replacement
            lookup[replacement] = lookup[elem]
            del lookup[elem]

        return nums
