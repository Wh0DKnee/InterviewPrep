# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]  # list because the environment for the nested function copies primitive values

        def dfs(node):
            if not node:
                return -1
            hl = dfs(node.left)
            hr = dfs(node.right)
            d = hl + hr + 2
            if d > result[0]:
                result[0] = d
            return max(hl, hr) + 1

        dfs(root)
        return result[0]
    