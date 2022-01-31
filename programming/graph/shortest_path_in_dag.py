from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for v in range(self.vertices)]

    def add_edge(self, source, target, weight):
        self.adjacency_list[source].append((target, weight))


def shortest_path(graph, vertices, source):
    print(graph)
    topological_order = topological_sort(graph, vertices)
    distances = [float('inf')] * vertices
    distances[source] = 0
    for vertex in topological_order:
        for node, weight in graph[vertex]:
            if distances[node] > distances[vertex] + weight:
                distances[node] = distances[vertex] + weight
    return distances


def topological_sort(graph, nodes):
    result = []
    in_degrees = {}
    for i in range(nodes):
        in_degrees[i] = 0

    for i in range(len(graph)):
        for node, weight in graph[i]:
            in_degrees[node] += 1

    queue = deque()

    for key, value in in_degrees.items():
        if value == 0:
            queue.append(key)

    while queue:
        node = queue.popleft()
        result.append(node)
        for adjacent, weight in graph[node]:
            in_degrees[adjacent] -= 1
            if in_degrees[adjacent] == 0:
                queue.append(adjacent)

    return result


if __name__ == '__main__':
    edges = [[0, 1, 2], [0, 4, 1], [1, 2, 3], [2, 3, 6], [4, 2, 2], [4, 5, 4], [5, 3, 1]]
    g = Graph(6)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    output = shortest_path(g.adjacency_list, g.vertices, 0)
    print(output)

    edges = [[0, 1, 5], [0, 2, 3], [1, 3, 6], [1, 2, 2], [2, 4, 4], [2, 5, 2], [2, 3, 7], [3, 4, -1], [4, 5, -2]]
    g = Graph(6)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    output = shortest_path(g.adjacency_list, g.vertices, 0)
    print(output)