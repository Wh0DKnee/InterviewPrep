class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = -1
        l = 0
        lookup = set()

        for r in range(len(s)):
            while s[r] in lookup:
                lookup.remove(s[l])
                l += 1
            lookup.add(s[r])
            longest = max(longest, r - l + 1)
        return longest