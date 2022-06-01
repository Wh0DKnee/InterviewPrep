

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        visited = set()
        clones = {}

        def dfs(v):
            visited.add(v)
            if v.val not in clones:
                clone = Node(v.val, [])
                clones[v.val] = clone
            for neighbor in v.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
                clones[v.val].neighbors.append(clones[neighbor.val])

        dfs(node)
        return clones[1]
