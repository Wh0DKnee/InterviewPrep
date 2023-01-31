from typing import List


class Solution:
    # Critical observation: even though subsequences maintain the original order of
    # the elements, order does not matter in this question, so we can use sorting.
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        start = nums[0]
        for i, num in enumerate(nums):
            if num - start > k:
                res += 1
                start = num

        return res
