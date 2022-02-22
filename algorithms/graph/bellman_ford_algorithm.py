from collections import defaultdict
from heapq import heappop, heappush


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2,  weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append((node2, weight))


def bellman_ford_shortest_path(graph, vertices, source):
    distances = [float('inf')] * len(edges)
    distances[source] = 0
    
    for i in range(vertices):
        for j in range(len(edges)):
            u, v, w = edges[j]
            if distances[u] != float('inf') and distances[v] > distances[u] + w:
                distances[v] = distances[u] + w

    return distances


def is_negative_weight_cycle(self, n, edges):
    distances = [float('inf')] * n
    distances[0] = 0
    
    for i in range(n):
        for j in range(len(edges)):
            u, v, w = edges[j]
            if distances[u] != float('inf') and distances[v] > distances[u] + w:
                distances[v] = distances[u] + w

    # When there is a cycle with negative edge, Bellman ford algorithm will not work.
    # For example, if we run the above loop n + 1 times, and there is a cycle with negative edge,
    # answer will keep upating. So if we run the relacation one more time, and if the answer is
    # getting changed, there is a cycle with negative edge.
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return True
    return False


if __name__ == '__main__':

    edges = [
        [0, 1, 7],
        [1, 2, 6], [1, 3, 20],[1, 4, 3],
        [2, 3, 14],
        [3, 4, 2]
    ]

    g = Graph(6)
    for edge in edges:
        if edge:
            g.add_edge(edge[0], edge[1], edge[2])
    output = bellman_ford_shortest_path(g.graph, g.nodes, 0)
    print(output)

