from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits, l, res = 0, 0, 0

        for r, num in enumerate(nums):
            while l < r and (num & used_bits) != 0:
                used_bits ^= nums[l]
                l += 1
            if l == r:
                used_bits = num
            else:
                used_bits ^= num
            # if/else can be replaced with used_bits |= num, but I think this is easier to understand
            res = max(res, r - l + 1)

        return res
