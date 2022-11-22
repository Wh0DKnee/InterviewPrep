from collections import deque


class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __str__(self):
        return self.name


def bfs(node):
    q = deque()
    q.append(node)
    visited = {node}

    while q:
        cur = q.pop()
        print(cur)
        for n in cur.neighbors:
            if n not in visited:
                q.appendleft(n)
                visited.add(n)


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
print("bfs")
bfs(A)
