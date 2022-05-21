from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            top = stack
            if not top:
                continue
            tmp = top.left
            top.left = top.right
            top.right = tmp
            stack.extend([top.left, top.right])

        return root

    def invertTree_rec(self, root):
        if not root:
            return root

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree_rec(root.left)
        self.invertTree_rec(root.right)