class Solution:
    # Even better if we use a dict that has closing parentheses as keys
    # and corresponding opening parentheses as value.
    def isValid(self, s: str) -> bool:
        opened = {'(': 0, '[': 1, '{': 2}
        closed = {')': 0, ']': 1, '}': 2}
        stack = []

        for c in s:
            if c in opened:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if opened[p] != closed[c]:
                    return False
        return len(stack) == 0

