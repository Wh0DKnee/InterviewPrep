from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, res = [], [], []

        cur = 1
        for num in nums:
            left.append(cur * num)
            cur = cur * num

        cur = 1
        for num in reversed(nums):
            right.insert(0, cur * num)
            cur = cur * num

        for i in range(len(nums)):
            l = 1 if i == 0 else left[i - 1]
            r = 1 if i == len(nums) - 1 else right[i + 1]
            res.append(l * r)

        return res

    # Slightly more elegant solution which eliminates the need for the last loop
    # and doesn't need two extra lists.
    def productExceptSelf_elegant(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
