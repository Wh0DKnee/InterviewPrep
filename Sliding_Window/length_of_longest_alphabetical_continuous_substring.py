class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        l, res = 0, 1

        for r in range(1, len(s)):
            if ord(s[r]) != ord(s[r - 1]) + 1:
                l = r
            res = max(res, r - l + 1)

        return res
