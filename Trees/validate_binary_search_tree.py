from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False

            return (valid(node.left, lower, node.val) and
                    valid(node.right, node.val, upper))

        return valid(root, -math.inf, math.inf)
