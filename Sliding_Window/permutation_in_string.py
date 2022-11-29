from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        search = defaultdict(int)
        found = defaultdict(int)
        for c in s1:
            search[c] += 1

        l = 0
        for r in range(len(s2)):
            found[s2[r]] += 1

            while found[s2[r]] > search[s2[r]]:
                found[s2[l]] -= 1
                l += 1

            if r - l + 1 == len(s1):
                return True

        return False
