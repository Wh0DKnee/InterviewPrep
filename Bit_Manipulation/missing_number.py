from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n ** 2 + n) // 2

        actual_sum = 0
        for num in nums:
            actual_sum += num

        return total_sum - actual_sum
