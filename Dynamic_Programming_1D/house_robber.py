from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            cur = max(rob1 + num, rob2)
            rob1, rob2 = rob2, cur

        return rob2

    # What I did here was to save for each memo entry, whether the result at each
    # position included the value at that position, so that we know whether we can
    # include the next value without cost or not. The point that I was missing is
    # as follows: If the value at position i is included, that automatically means
    # that the max at i is larger than the max at i-1, since otherwise, we would
    # have just chosen not to include the value at i and keep the max at i-1.
    #
    # In pseudo code, I did:
    # if i-1 not included:
    #     rob[i] = rob[i-1] + nums[i]
    # else (if i-1 is included):
    #     rob[i] = max(rob[i-2] + nums[i], rob[i-1])
    #
    # However, in the first case, rob[i-1] == rob[i-2] since i-1 is not included,
    # which means that in this case, the code in the else case is equivalent and
    # we can therefore omit the case distinction altogether!
    def rob_initial_solution(self, nums):
        if len(nums) == 1:
            return nums[0]

        memo = [(0, False) for x in range(len(nums))]
        memo[0], memo[1] = (nums[0], True), (nums[0], False) if nums[0] > nums[1] else (nums[1], True)

        for i in range(2, len(nums)):
            if memo[i - 1][1]:
                val_with, val_without = nums[i] + memo[i - 2][0], memo[i - 1][0]
                memo[i] = (val_with, True) if val_with > val_without else (val_without, False)
            else:
                memo[i] = (memo[i - 1][0] + nums[i], True)

        return memo[-1][0]