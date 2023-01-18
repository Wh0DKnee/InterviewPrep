from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = [True]

        def dfs(node1, node2):
            if not res[0] or (node1 is None and node2 is None):
                return
            if node1 is None or node2 is None or node1.val != node2.val:
                res[0] = False
                return
            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        dfs(p, q)
        return res[0]

    def isSameTree_rec(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
