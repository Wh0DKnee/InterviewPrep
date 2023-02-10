from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        def dfs(node):
            # store right subtree for later
            tmp = node.right
            # make left subtree right subtree
            node.right = node.left
            # set left subtree to None
            node.left = None
            # recurse on right subtree (previous left subtree)
            # and store the last node that it got called on (in the example: 4)
            if node.right is None:
                last = node
            else:
                last = dfs(node.right)
            # re-attach right subtree that we saved earlier
            last.right = tmp
            # recurse on subtree
            if tmp is not None:
                last = dfs(tmp)
            return last

        dfs(root)
