from typing import List


class Solution:
    # The idea: We don't need to check every possible pair, because for each value
    # there is exactly one value with which it adds up to target. So we save the
    # values we've already seen in a dictionary, and then for each value we encounter
    # check whether the complement is in the dict.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(nums)):
            if nums[i] in lookup:
                return [lookup[nums[i]], i]
            lookup[target - nums[i]] = i
