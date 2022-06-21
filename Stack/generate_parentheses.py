from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, o, c):
            if o == c == n:
                res.append(s)
                return
            if o < n:
                dfs(s + "(", o + 1, c)
            if o > c:
                dfs(s + ")", o, c + 1)

        dfs("", 0, 0)
        return res
