from collections import defaultdict
from heapq import heappop, heappush


class Graph(object):
    def __init__(self, edges):
        self.edges = edges
        self.adj = Graph._build_adjacency_list(edges)

    @staticmethod
    def _build_adjacency_list(edges):
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
        return adj


def articulation_points(graph, source):
    discovery = find_discovery(graph, source)
    print(discovery)
    low = find_low(graph)

def find_discovery(graph, source):
    count = [1]
    visited = set()
    discovery = defaultdict(int)
    low = defaultdict(list)
    parent = defaultdict(list)
    dfs_helper(graph, source, discovery, low, parent,  visited, count)
    return discovery


def find_low(graph):
    pass


def dfs_helper(graph, vertex, discovery, low, parent, visited, count):
    visited.add(vertex)
    discovery[vertex] = count[0]
    low[vertex] = count[0]
    count[0] += 1

    
    for adjacent in graph[vertex]:
        if adjacent not in visited:
            parent[adjacent] = vertex
            dfs_helper(graph, adjacent, discovery, low, parent, visited, count)
    

if __name__ == '__main__':
    # edges = [
    #     ['a', 'b'], ['a', 'c'],
    #     ['b', 'd'], ['c', 'd'],
    #     ['c', 'g'], ['c', 'h'],
    #     ['d', 'e'], ['d', 'f'],
    #     ['g', 'h'], ['e', 'f']
    # ]
    # g = Graph(edges)
    # output = articulation_points(g.adj)
    # print(output)

    edges = [
        [1, 4], [1, 2],
        [4, 3], [2, 3],
        [3, 5], [3, 6],
        [5, 6]
    ]
    g = Graph(edges)
    output = articulation_points(g.adj, 1)
    print(output)