from collections import deque


class Linked_list():

    def __init__(self):

        self.list = deque()

    def add(self, e):

        self.list.append(e)

    def remove(self):
        self.list.pop()

    def __sizeof__(self):
        self.list.__sizeof__()

    def is_empty(self):
        return self.list.__sizeof__() == 0



class node_DFS:
    def __init__(self, color, start_time, parent, final_time):

        self.color = color
        self.d = start_time
        self.f = final_time
        self.parent = parent




# DFS can remove the edges from both directed and undiredcted graph
tree_nodes = set()
# tree_edges is the resultant acyclic graph at the end
tree_edges = set()
finished_nodes = deque()
back_edges = set()


def DFS_visit(adj_lst, v, time):

    time += 1
    v.d = time
    v.color = "gray"
    tree_nodes.add(v)
    for u in adj_lst:
        if u.color == "white":
            u.parant = v
            tree_edges.add((v, u))
            DFS_visit(adj_lst, u, time)
        else:
            back_edges.add((u, v))


    v.color = "back"
    time += 1
    v.f = time
    finished_nodes.append(v)


def DFS(V, lst):

    for v in V:
        v.color = "white"
        v.parent = None

    time = 0
    for v in V:
        if v.color == "white":
            DFS_visit(lst, v, time)
    return finished_nodes






def topological_sort(V, lst):

    LL = Linked_list()
    dfs_tree = DFS(V, lst)
    # LL.add(dfs_tree.__iter__())
    LL = list(map(LL.add, dfs_tree.__iter__()))
    return LL

