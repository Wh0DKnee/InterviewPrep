from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        lookup = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def dfs(index, cur):
            if index >= len(digits):
                res.append(cur)
                return

            for c in lookup[digits[index]]:
                dfs(index + 1, cur + c)

        dfs(0, "")
        return res
