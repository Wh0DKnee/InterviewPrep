from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums_, subset):
            if not nums_:
                res.append(subset)
                return

            appended = subset.copy()
            appended.append(nums_[0])
            dfs(nums_[1:], appended)
            dfs(nums_[1:], subset)

        empty = []
        dfs(nums, empty)
        return res

    def subset_bit(self, nums):
        cur = 0
        stop = 1 << len(nums)
        res = []
        while cur != stop:
            res.append(self.appendCurToRes(cur, stop, nums))
            cur += 1
        return res

    def appendCurToRes(self, cur, stop, nums):
        sub_res = []
        bit_index = 1
        actual_index = 0
        while bit_index != stop:
            inSet = bit_index & cur
            if inSet:
                sub_res.append(nums[actual_index])
            bit_index = bit_index << 1
            actual_index += 1
        return sub_res
