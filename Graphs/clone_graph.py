

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        old_to_new = {}

        def dfs(n):
            if n in old_to_new:
                return
            old_to_new[n] = Node(n.val)

            for nei in n.neighbors:
                dfs(nei)
                # here, the neighbor already got cloned in the recursive call!
                old_to_new[n].neighbors.append(old_to_new[nei])

        dfs(node)

        return old_to_new[node]
