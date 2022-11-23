

class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __str__(self):
        return self.name


def has_cycle(v):
    visited = set()

    def dfs(node, parent):
        if node in visited:
            return True

        visited.add(node)
        for nei in node.neighbors:
            if nei != parent and dfs(nei, node):
                return True

        return False

    return dfs(v, None)


def has_cycle2(v):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in node.neighbors:
            if nei == parent:
                continue
            if node in visited:
                return True
            return dfs(nei, node)

        return False

    return dfs(v, None)


def find_cycle(v):
    cycle = {}

    def dfs(node, parent):
        if node in cycle:
            for key in list(cycle.keys()):
                if key == node:
                    return list(cycle.keys())
                del cycle[key]

        cycle[node] = None
        for nei in node.neighbors:
            if nei != parent and dfs(nei, node):
                return list(cycle.keys())

        del cycle[node]
        return []

    return dfs(v, None)


#            A
#          /-|\
#        /-  | -\
#       -    |   -
#      B     C   E
#    /-|     |   |
#  --  |     |   |
# D    F     G   |
#      -         |
#      +---------+
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
print("has_cycle2(D)")
print(has_cycle(D))
print("find_cycle(D)")
c = find_cycle(D)
for n in c:
    print(n)
