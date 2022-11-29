from collections import defaultdict


class Solution:
    # This problem is pretty tricky tbh, need to review it
    # to really understand the approach.
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, res = 0, 0

        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))

        return res


