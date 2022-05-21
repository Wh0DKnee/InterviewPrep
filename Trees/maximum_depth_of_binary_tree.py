from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        max_depth = 0

        while q:
            top, depth = q.pop()
            if not top:
                continue
            max_depth = max(max_depth, depth)
            q.extend([(top.left, depth + 1), (top.right, depth + 1)])

        return max_depth

    def maxDepth_rec(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth_rec(root.left), self.maxDepth_rec(root.right))
