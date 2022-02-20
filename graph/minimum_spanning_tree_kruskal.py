from collections import defaultdict, deque
from heapq import heappop, heappush

class Graph(object):
    def __init__(self, edges):
        self.edges = edges
        self.adj = Graph._build_adjacency_list(edges)

    @staticmethod
    def _build_adjacency_list(edges):
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        return adj

def find(u, parent):
    if parent[u] == -1:
        return u
    if parent[u] != -1:
        return find(parent[u], parent)


def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[y] < rank[x]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1


def minimum_spanning_tree(edges, vertices):
    # Step 1: sort all edges in increasing order using min heap
    edges.sort(key=lambda edge:edge[2])

    # Initialize MST and result

    # Step 2: Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
    parent = defaultdict(int)
    rank = defaultdict(int)
    for u, v, w in edges:
        parent[u] = -1
        parent[v] = -1
        rank[u] = 0
        rank[v] = 0

    mst = []
    i = 0

    while i < vertices - 1:
        edge = edges[i]
        x = find(edge[0], parent)
        y = find(edge[1], parent)
        if x != y:
            union(parent, rank, x, y)
            mst.append(edge)
            i += 1

    return mst
        


if __name__ == '__main__':
    edges = [
        ['a', 'b', 6], ['a', 'c', 5],
        ['b', 'c', 3], ['b', 'd', 8],
        ['c', 'd', 7], ['c', 'e', 12],
        ['d', 'e', 10]
    ]
    # g = Graph(edges)
    output = minimum_spanning_tree(edges, 5)
    print(output)
    # edges = [[0, 1, 5], [0, 2, 1], [1, 2, 3]]
    # g = Graph(3)
    # for edge in edges:
    #     g.add_edge(edge[0], edge[1], edge[2])
    # output = minimum_spanning_tree(g.adjacency_list, g.vertices)
    # print(output)

    # edges = [[0, 1, 2], [1, 2, 3], [0, 3, 6], [1, 4, 5]]
    # g = Graph(5)
    # for edge in edges:
    #     g.add_edge(edge[0], edge[1], edge[2])
    # output = minimum_spanning_tree(g.adjacency_list, g.vertices)
    # print(output)

    # edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7]]
    # g = Graph(5)
    # for edge in edges:
    #     g.add_edge(edge[0], edge[1], edge[2])
    # output = minimum_spanning_tree(g.adjacency_list, g.vertices)
    # print(output)
