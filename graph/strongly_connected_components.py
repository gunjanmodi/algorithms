from collections import defaultdict
from heapq import heappop, heappush
from turtle import st


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_list = [[] for _ in range(self.nodes)]

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)


def dfs_helper(graph, node, visited, stack, is_topological):
    visited.add(node)
        

    for child in graph[node]:
        if child not in visited:
            dfs_helper(graph, child, visited, stack, is_topological)

    if is_topological:
        stack.append(node)

def kosurajus_algorithm(graph, vertices):
    # Step 1: Store vertices in Topological Sort order
    stack = []
    visited = set()

    for vertex in range(vertices):
        if vertex not in visited:
            dfs_helper(graph, vertex, visited, stack, True)


    # Step 2: Reverse all edges of the Graph
    reversed_graph = [[] for _ in range(vertices)]
    for u in range(len(graph)):        
        for v in graph[u]:
            reversed_graph[v].append(u)

    # Step 3: One by One pop elements from top of the stack and Count/Store and Mark the elements visited by current vertex
    count = 0
    visited = set()
    while stack:
        u = stack.pop()
        if u not in visited:
            dfs_helper(reversed_graph, u, visited, stack, False)
            count += 1
            print("-----")
    return count



if __name__ == '__main__':

    edges = [
        [0, 1], [1, 2], [2, 0], [1, 3], [3, 4]
    ]

    g = Graph(5)
    for edge in edges:
        if edge:
            g.add_edge(edge[0], edge[1])
    output = kosurajus_algorithm(g.adjacency_list, g.nodes)
    print(output)
