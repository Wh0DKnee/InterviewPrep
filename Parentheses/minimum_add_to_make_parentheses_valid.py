class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                res += 1
                balance += 1

        return res + balance
