from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)

        while q:
            prev = None
            for _ in range(len(q)):
                cur = q.pop()
                cur.next = prev
                if cur.right:
                    q.appendleft(cur.right)
                if cur.left:
                    q.appendleft(cur.left)
                prev = cur
        return root

    def connect_rec(self, root):
        if not root:
            return root

        def dfs(left, right):
            if left:
                left.next = right
                dfs(left.left, left.right)
            if right:
                dfs(right.left, right.right)
            if left and right:
                dfs(left.right, right.left)

        dfs(root.left, root.right)
        return root

    # using previously established next pointers.
    def connect_genius(self, root):
        cur = root

        while cur:
            nxt = cur.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            cur = nxt

        return root
