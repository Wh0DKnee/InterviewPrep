from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l, res = 0, 0
        nums.sort()  # need sorting, because the most frequent elements don't need to be consecutive
        opsNeeded = 0

        for r in range(len(nums)):
            if r > 0:
                opsNeeded += (nums[r] - nums[r - 1]) * (r - l)

            while opsNeeded > k:
                opsNeeded -= nums[r] - nums[l]
                l += 1

            res = max(res, r - l + 1)

        return res
