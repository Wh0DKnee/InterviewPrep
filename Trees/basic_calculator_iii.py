import operator


class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def calculate(self, s: str) -> int:
        root = self.build_tree(s)
        # self.print(root)
        return self.evaluate(root)

    def print(self, node):
        print(node.val)
        if node.left is not None:
            print("left: ")
            self.print(node.left)
        if node.right is not None:
            print("right: ")
            self.print(node.right)

    def build_tree(self, s):
        if s[0] == "(" and s[-1] == ")":  # if the entire expression is bracketed, we remove the brackets.
            s = s[1:-1]
        print(s)
        bracket_level = 0
        op_idx = -1
        found_add_or_sub = False

        for idx, c in enumerate(s):
            if c == "(":
                bracket_level += 1
            elif c == ")":
                bracket_level -= 1
            elif bracket_level > 0:
                continue
            elif c == "+" or c == "-":  # + and - have less precedence, so it needs to be higher up the tree.
                op_idx = idx
                found_add_or_sub = True
            elif (c == "*" or c == "/") and not found_add_or_sub:
                op_idx = idx

        if op_idx == -1:  # string is just a number.
            return Node(s)

        node = Node(s[op_idx])
        node.left = self.build_tree(s[:op_idx])
        node.right = self.build_tree(s[op_idx + 1:])
        return node

    def evaluate(self, node):
        char_to_op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
        if node.val.isdigit():
            return int(node.val)

        left, right = self.evaluate(node.left), self.evaluate(node.right)
        res = char_to_op[node.val](left, right)
        #  print(left, node.val, right, "=", res)
        return char_to_op[node.val](left, right)

    def evaluate(self, node):
        char_to_op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
        if node.val.isdigit():
            return int(node.val)
        return char_to_op[node.val](self.evaluate(node.left), self.evaluate(node.right))