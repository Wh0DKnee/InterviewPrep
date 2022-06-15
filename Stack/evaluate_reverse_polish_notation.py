from typing import List
import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        for token in tokens:
            if token in operators:
                right, left = stack.pop(), stack.pop()
                stack.append(int(operators[token](left, right)))
            else:
                stack.append(int(token))

        return stack[0]
