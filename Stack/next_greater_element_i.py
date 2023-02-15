from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        next_greater = [-1] * len(nums2)
        mono = []
        s = set(nums1)
        lookup = {}

        for idx, num in enumerate(nums2):
            if num in s:
                lookup[num] = idx

            while mono and num > nums2[mono[-1]]:
                next_greater[mono.pop()] = num
            mono.append(idx)

        for idx, num in enumerate(nums1):
            res[idx] = next_greater[lookup[num]]

        return res