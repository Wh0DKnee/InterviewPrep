

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass  # assume implemented


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        res = n

        while l <= r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res