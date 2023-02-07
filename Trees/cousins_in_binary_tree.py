# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_d, x_p = self.find(root, x)
        y_d, y_p = self.find(root, y)
        return x_d == y_d and x_p != y_p

    def find(self, node, val, depth=0, parent=None):
        if node is None:
            return None, None
        if node.val == val:
            return depth, parent

        left_d, left_p = self.find(node.left, val, depth + 1, node.val)
        right_d, right_p = self.find(node.right, val, depth + 1, node.val)
        if left_d is None:
            return right_d, right_p
        return left_d, left_p
