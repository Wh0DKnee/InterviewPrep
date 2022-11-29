import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = {}
        for c in t:
            needed[c] = needed.get(c, 0) + 1

        l = 0
        res = ""
        best_len = math.inf

        for r in range(len(s)):
            if l >= len(s):
                break

            if s[r] in needed:
                needed[s[r]] -= 1

            if s[l] not in needed:
                l += 1

            while self.allValuesZeroOrSmaller(needed):
                if r - l + 1 < best_len:
                    res = s[l:r + 1]
                    best_len = len(res)

                needed[s[l]] += 1
                l += 1
                while l < len(s) and (s[l] not in needed or needed[s[l]] < 0):
                    if s[l] in needed:
                        needed[s[l]] += 1
                    l += 1

        return res

    def allValuesZeroOrSmaller(self, d):
        for v in d.values():
            if v > 0:
                return False

        return True
