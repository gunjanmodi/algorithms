from collections import defaultdict, deque
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)


def topological_sort(graph, nodes):
    count = 0
    in_degrees = {}
    for i in range(nodes):
        in_degrees[i] = 0

    for i in range(len(graph)):
        children = graph[i]
        for child in children:
            in_degrees[child] += 1

    queue = deque()

    for key, value in in_degrees.items():
        if value == 0:
            queue.append(key)

    while queue:
        node = queue.popleft()
        count += 1

        adjacents = graph[node]
        for adjacent in adjacents:
            in_degrees[adjacent] -= 1
            if in_degrees[adjacent] == 0:
                queue.append(adjacent)

    return count != nodes


if __name__ == '__main__':
    edges = [[0, 2], [0, 3], [1, 3], [1, 4]]
    g = Graph(5)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    output = topological_sort(g.graph, g.nodes)
    print(output)


    edges = [[0, 1], [1, 2], [2, 3], [3, 1], [4, 1]]
    g = Graph(5)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    output = topological_sort(g.graph, g.nodes)
    print(output)