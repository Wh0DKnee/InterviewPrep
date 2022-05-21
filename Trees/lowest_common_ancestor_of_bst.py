
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_smaller = p.val < root.val
        q_smaller = q.val < root.val
        p_bigger = p.val > root.val
        q_bigger = q.val > root.val

        if p_smaller and q_smaller:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_bigger and q_bigger:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def solution_for_any_binary_tree(self, root, p, q):
        res = [None]

        def dfs(node):
            if not node or res[0] is not None:
                return set()
            s = {node}
            l = dfs(node.left)
            r = dfs(node.right)
            s.update(l)
            s.update(r)
            if p in s and q in s and res[0] is None:
                res[0] = node
            return s

        dfs(root)
        return res[0]
