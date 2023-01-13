class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0
        res = 0

        i = 0
        while i < len(s):
            if s[i] == "(":
                balance += 1
            elif s[i] == ")":
                if i < len(s) - 1 and s[i + 1] == ")":
                    balance -= 1
                    i += 1
                else:
                    balance -= 1
                    res += 1

            if balance < 0:
                res += 1
                balance += 1

            i += 1

        return res + (balance * 2)
