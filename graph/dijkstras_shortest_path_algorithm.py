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


def dijkstras_shortest_path(graph, vertices, source):
    distances = {}

    for vertex in range(len(graph)):
        distances[vertex] = float('inf')
    
    distances[source] = 0

    min_heap = [(0, source)]
    finalized = set()
        
    while min_heap:
        current_weight, current_node  = heappop(min_heap)
        
        if current_node in finalized:
            continue
            
        finalized.add(current_node)
        
        for neighbour, weight in graph[current_node]:
            if neighbour not in finalized:
                if distances[neighbour] > distances[current_node] + weight:
                    distances[neighbour] =  distances[current_node] + weight
                    
                    heappush(min_heap, (distances[neighbour], neighbour))
    
    return list(distances.values())


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
    output = dijkstras_shortest_path(g.graph, g.nodes, 0)
    print(output)

    # edges = [
    #     ['S', 'A', 15], ['S', 'B', 10],
    #     ['A', 'B', 2], ['A', 'C', 10],
    #     ['B', 'C', 5], ['B', 'D', 1],
    #     ['D', 'C', 3]
    # ]

    # g = Graph(5)
    # for edge in edges:
    #     g.add_edge(edge[0], edge[1], edge[2])
    # output = dijkstras_shortest_path(g.graph, g.nodes, 'S')
    # print(output)

    # edges = [['A', 'B', 4], ['A', 'C', 8], ['B', 'C', 11],
    #          ['B', 'D', 8], ['C', 'E', 7], ['C', 'F', 1],
    #          ['D', 'E', 2], ['D', 'H', 4], ['D', 'G', 7],
    #          ['E', 'F', 6], ['F', 'H', 2], ['G', 'H', 14],
    #          ['G', 'I', 9], ['H', 'I', 10]

    #          ]
    # g = Graph(9)
    # for edge in edges:
    #     g.add_edge(edge[0], edge[1], edge[2])
    # output = dijkstras_shortest_path(g.graph, g.nodes, 'A')
    # print(output)

    edges = [
        [0, 1, 4], [0, 7, 8], [1, 2, 8], [1, 7, 11],
        [2, 3, 7], [2, 8, 2], [2, 5, 4], [3, 4, 9],
        [3, 5, 14], [4, 5, 10], [5, 6, 2], [6, 7, 1],
        [6, 8, 6], [7, 8, 7]
    ]
    g = Graph(9)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    output = dijkstras_shortest_path(g.graph, g.nodes, 0)
    print(output)
