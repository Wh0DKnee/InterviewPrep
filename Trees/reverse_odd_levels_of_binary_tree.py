from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_order = self.levelOrder(root)

        level = 1
        while True:
            start, stop = (2 ** level) - 1, (2 ** (level + 1)) - 1
            if start >= len(level_order):
                break
            sublist = level_order[start:stop]
            sublist.reverse()
            level_order[start:stop] = sublist
            level += 2

        return self.fromLevelOrder(level_order)

    def levelOrder(self, root: Optional[TreeNode]):
        res = []
        q = deque()

        if root:
            q.append(root)

        while q:
            q_size = len(q)
            for i in range(q_size):
                popped = q.popleft()
                res.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

        return res

    def fromLevelOrder(self, level_order, index=0):
        if index >= len(level_order):
            return None
        node = TreeNode(level_order[index])
        node.left = self.fromLevelOrder(level_order, index * 2 + 1)
        node.right = self.fromLevelOrder(level_order, index * 2 + 2)
        return node
