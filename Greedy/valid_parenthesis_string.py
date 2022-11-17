from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_p = []
        wildcards = []

        for i, c in enumerate(s):
            if c == '*':
                wildcards.append(i)
            elif c == '(':
                open_p.append(i)
            elif c == ')':
                if not open_p and not wildcards:
                    return False
                if open_p:
                    open_p.pop()
                else:
                    wildcards.pop()

        while open_p and wildcards and wildcards[-1] > open_p[-1]:
            wildcards.pop()
            open_p.pop()

        return not open_p