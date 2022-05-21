from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for num in nums:
            if num in lookup:
                return True
            lookup.add(num)
        return False
