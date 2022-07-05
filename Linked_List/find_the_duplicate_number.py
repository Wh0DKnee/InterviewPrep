from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # This "medium" problem is bullshit. You can't solve this unless you either
        # already know the solution or are an absolute fucking genius.

        # First, you need to see that it is equivalent to a linked list cycle problem,
        # which isn't intuitive at all, and then you have to find the start of the cycle,
        # which, again, if you don't happen to already know Floyd's algorithm by chance,
        # is impossible unless you've won a Turing award, in which case you're probably
        # not on leetcode grinding questions.

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
