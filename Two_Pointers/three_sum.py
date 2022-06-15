from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if i > 0 and nums[i - 1] == val:
                continue  # don't want duplicates

            target = -val
            left, right = i + 1, len(nums) - 1
            while left < right:
                added = nums[left] + nums[right]
                if added < target:
                    left += 1
                elif added > target:
                    right -= 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
