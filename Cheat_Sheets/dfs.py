class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __str__(self):
        return self.name


# Checks if neighbor is already visited before recursive call.
def dfs1(node, visited):
    print(node)  # process visited node
    visited.add(node)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs1(neighbor, visited)


# Equivalent, but we delay the visited check until the next recursion
# level. This uses an extra stack frame (doesn't really matter), but IMO
# it's less clear because in dfs1, a recursive call means we are visiting
# the node that is passed, and we can just print it. In dfs2, we need to do
# the check first and then print it, otherwise we'll potentially get some
# nodes printed twice.
# In some cases, the code will be more elegant though: If we don't call the
# function recursively in a loop, but manually multiple times, we don't need
# to write the if statement multiple times - the if in the recursive call will
# handle it all.
def dfs2(node, visited):
    if node in visited:
        return
    print(node)  # process after the early out, otherwise we might process a node multiple times
    visited.add(node)
    for neighbor in node.neighbors:
        dfs2(neighbor, visited)


# IMO, this is quite hard to understand. What's confusing is the timing of
# setting and checking the seen status of a node.
def dfs_iterative(node):
    stack = [node]
    seen = set()
    while stack:
        cur = stack.pop()
        if cur not in seen:
            seen.add(cur)
            print(cur)
            for neighbor in reversed(cur.neighbors):
                # without reversed we also get a valid dfs, but a
                # different order than the recursive versions.
                stack.append(neighbor)


# This is equivalent to BFS, but instead of using a queue, we use a stack.
# It is a common misconception, that swapping the queue with a stack results
# in dfs: https://11011110.github.io/blog/2013/12/17/stack-based-graph-traversal.html
# The problem is that all neighbors of the start node are marked as seen, and only
# not-yet-seen nodes are pushed onto the stack. Imagine a simple graph:
# TODO: Think of minimal example that guarantees that the order is non-DFS conforming
def dfs_iterative_wrong(node):
    stack = [node]
    seen = {node}
    while stack:
        cur = stack.pop()
        print(cur)
        for neighbor in reversed(cur.neighbors):
            # without reversed we also get a valid dfs, but a
            # different order than the recursive versions.
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)


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
print("dfs1:")
dfs1(A, set())
print("dfs2:")
dfs2(A, set())
print("dfs_iterative:")
dfs_iterative(A)
print("dfs_iterative_wrong")
dfs_iterative_wrong(A)
