import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node, maximum):
            if not node:
                return
            if node.val >= maximum:
                res[0] += 1

            new_max = max(maximum, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, -math.inf)
        return res[0]
