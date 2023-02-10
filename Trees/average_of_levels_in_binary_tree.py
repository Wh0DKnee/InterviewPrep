from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        avgs = []

        while q:
            total = 0
            n = len(q)
            for _ in range(n):
                cur = q.pop()
                total += cur.val
                if cur.left:
                    q.appendleft(cur.left)
                if cur.right:
                    q.appendleft(cur.right)
            avgs.append(total / n)

        return avgs
