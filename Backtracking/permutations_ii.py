from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(options, perm):
            if len(options) == 0:
                res.append(perm[:])
                return

            for idx, num in enumerate(options):
                if idx > 0 and num == options[idx - 1]:
                    continue
                perm.append(num)
                dfs(options[:idx] + options[idx + 1:], perm)
                perm.pop()

        dfs(nums, [])
        return res
