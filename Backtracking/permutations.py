from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(options):
            if not options:
                res.append(subset.copy())
                return

            for i in range(len(options)):
                subset.append(options[i])
                new_options = options[:i] + options[i+1:]  # copy list and remove element at index i
                dfs(new_options)
                subset.pop()

        dfs(nums)
        return res
