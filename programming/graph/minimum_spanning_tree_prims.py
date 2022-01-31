# from collections import defaultdict, deque
from heapq import heappop, heappush

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for v in range(self.vertices)]

    def add_edge(self, source, target, weight):
        self.adjacency_list[source].append((target, weight))
        self.adjacency_list[target].append((source, weight))


def minimum_spanning_tree(graph, vertices):
    result = 0
    min_heap = []
    source = 0

    for adjacent in graph[source]:
        heappush(min_heap, (adjacent[1], adjacent[0]))
    
    visited = set()
    visited.add(source)

    while True:
        weight, current_node = heappop(min_heap)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        result += weight

        if len(visited) == vertices:
            break

        for child_node, child_weight  in graph[current_node]:
            if child_node not in visited:
                heappush(min_heap, (child_weight, child_node))
        
    return result

if __name__ == '__main__':
    edges = [[0, 1, 5], [0, 2, 1], [1, 2, 3]]
    g = Graph(3)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    output = minimum_spanning_tree(g.adjacency_list, g.vertices)
    print(output)

    edges = [[0, 1, 2], [1, 2, 3], [0, 3, 6], [1, 4, 5]]
    g = Graph(5)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    output = minimum_spanning_tree(g.adjacency_list, g.vertices)
    print(output)

    edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7]]
    g = Graph(5)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    output = minimum_spanning_tree(g.adjacency_list, g.vertices)
    print(output)
