class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
A.neighbors.extend([B, C, E])
B.neighbors.extend([A, D, F])
C.neighbors.extend([A, G])
D.neighbors.extend([B])
E.neighbors.extend([A, F])
F.neighbors.extend([B, E])
G.neighbors.extend([C])


def dfs(node, visited):
    print(node.name)
    visited.add(node)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)


def dfs2(node, visited):
    print(node.name)
    if node in visited:
        return
    visited.add(node)
    for neighbor in node.neighbors:
        dfs(neighbor, visited)


dfs2(A, set())
