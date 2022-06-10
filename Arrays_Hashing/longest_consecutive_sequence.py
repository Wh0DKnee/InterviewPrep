from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lookup = set(nums)
        best = 1
        for num in nums:
            count = 0
            if num-1 in lookup:
                continue
            cur = num
            while cur in lookup:
                count += 1
                cur = cur + 1
            best = max(best, count)
        return best
