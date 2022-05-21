from recviz import recviz

v = []
n = 3


@recviz
def gen(k):
    if k == n+1:
        return v
    else:
        gen(k+1)
        v.append(k)
        gen(k+1)
        v.pop()


gen(1)
