import sys
from collections import deque
from collections import defaultdict

class node_BFS:
    def __init__(self, color, distance, parent):

        self.color = color
        self.d = distance
        self.parent = parent


####&&&& BFS is used to find the shortest path between two vertices



MAX_D = sys.maxsize

# BFS on graph with list of vertices V and adjacency dict
def BFS(V, adj_dict, s, node=None, find_shortest_path=False):

    vertices = set()
    BFS_edges = set()
    for vertex in V:
        if vertex != s:
            v = node_BFS("white", MAX_D, None)
            vertices.add(v)
    s = node_BFS("gray", 0, None)
    Q = deque()
    Q.append(s)
    while len(Q) != 0:
        u = Q.pop()
        for v in adj_dict[u]:
            if v.color == "white":
                v.color = "gray"
                BFS_edges.add((u, v))
                v.d = u.d + 1
                if find_shortest_path and v == node:
                    return v.d
                v.parent = u
                Q.append(v)
        u.color = "black"
    return BFS_edges



d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(0)
l = list(d)
print(list(d.items()))



# BFS is used for detecting the shortest path from u to v
def shortest_path(V, u, v, lst):

    d = BFS(V, lst, u, v,  find_shortest_path=True)
    return d






