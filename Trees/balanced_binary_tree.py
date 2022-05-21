from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]

        def dfs(node):
            if not node:
                return -1

            hl = dfs(node.left)
            hr = dfs(node.right)

            if abs(hl - hr) > 1:
                res[0] = False
            return max(hl, hr) + 1

        dfs(root)
        return res[0]
