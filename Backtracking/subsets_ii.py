from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(nums_, subset):
            if not nums_:
                res.append(subset)
                return

            appended = subset.copy()
            appended.append(nums_[0])
            dfs(nums_[1:], appended)

            # if we have a repeating number, skip all of them for one of the search branches to avoid duplicates.
            change_index = len(nums_)
            cur = nums_[0]
            for i in range(len(nums_)):
                if nums_[i] != cur:
                    change_index = i
                    break

            dfs(nums_[change_index:], subset)

        dfs(nums, [])
        return res
