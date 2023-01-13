class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack = []
        close_stack = []

        for i in range(len(s)):
            if s[i] == ")":
                if open_stack:
                    open_stack.pop()
                else:
                    close_stack.append(i)
            elif s[i] == "(":
                open_stack.append(i)

        to_remove = set(open_stack)
        to_remove.update(close_stack)

        res = []
        for i in range(len(s)):
            if i in to_remove:
                continue
            res.append(s[i])

        return ''.join(res)
