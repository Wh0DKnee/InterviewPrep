from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, parent_sum):
            if not node:
                return parent_sum

            right_sum = dfs(node.right, parent_sum)
            cur_sum = right_sum + node.val
            node.val = cur_sum
            # the total sum of a tree is the greater value its most left child node
            # (all other nodes in the tree are greater)
            tree_total = dfs(node.left, cur_sum)
            return tree_total

        dfs(root, 0)
        return root

    def convertBST_sort(self, root):
        ordered_nodes = []

        def dfs(node):
            if node is None:
                return
            ordered_nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        ordered_nodes.sort(key=lambda n: n.val)
        total = 0
        for node in reversed(ordered_nodes):
            total += node.val
            node.val = total

        return root
