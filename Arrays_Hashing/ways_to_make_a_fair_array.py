from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        rightOdd, rightEven = 0, 0
        leftOdd, leftEven = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                rightEven += nums[i]
            else:
                rightOdd += nums[i]

        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                rightEven -= nums[i]
            else:
                rightOdd -= nums[i]

            if leftEven + rightOdd == leftOdd + rightEven:
                res += 1

            if i % 2 == 0:
                leftEven += nums[i]
            else:
                leftOdd += nums[i]

        return res
