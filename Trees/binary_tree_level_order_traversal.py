from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            sub_res = []

            for i in range(len(q)):
                left = q.popleft()
                sub_res.append(left.val)
                if left.left:
                    q.append(left.left)
                if left.right:
                    q.append(left.right)

            res.append(sub_res)

        return res

    def levelOrder_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        def f(node):
            if not node:
                return []
            l = f(node.left)
            r = f(node.right)
            res = [[node.val]]
            self.bufferShorterList(l, r)
            for i in range(len(l)):
                zipped = l[i] + r[i]
                res.append(zipped)
            return res

        return f(root)

    def bufferShorterList(self, l1, l2):
        diff = len(l1) - len(l2)
        shorter = l2 if diff > 0 else l1
        diff = abs(diff)
        for i in range(diff):
            shorter.append([])
