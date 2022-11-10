from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {"": True}
        return self.dfs(s, wordDict, memo)

    def dfs(self, s, wDict, memo):
        if s in memo:
            return memo[s]

        res = False
        for word in wDict:
            if not s.startswith(word):
                continue
            res = res or self.dfs(s[len(word):], wDict, memo)

        memo[s] = res
        return res