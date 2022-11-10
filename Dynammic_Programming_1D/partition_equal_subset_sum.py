from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target / 2

        sum_set = set([0])
        for num in nums:
            next_sum_set = set()
            for s in sum_set:
                next_sum_set.add(s + num)
            sum_set.update(next_sum_set)
            if target in sum_set:
                return True

        return False

    def canPartition_memo(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target / 2
        memo = {}

        def dfs(cur_sum, rem_nums):
            if cur_sum == target:
                memo[(tuple(rem_nums), cur_sum)] = True
                return True
            if not rem_nums:
                memo[(tuple(rem_nums), cur_sum)] = False
                return False
            if tuple(rem_nums) in memo:
                return memo[tuple(rem_nums)]

            left = dfs(cur_sum + rem_nums[0], rem_nums[1:])
            right = dfs(cur_sum, rem_nums[1:])
            memo[(tuple(rem_nums), cur_sum)] = left or right
            return left or right

        return dfs(0, nums)