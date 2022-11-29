from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(parts, rest):
            if parts and not self.isPalindrome(parts[-1]):
                return
            if not rest:
                res.append(parts)
                return

            for i in range(1, len(rest) + 1):
                new_parts = parts[:]
                new_parts.append(rest[:i])
                dfs(new_parts, rest[i:])

        dfs([], s)
        return res

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True
