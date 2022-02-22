class Graph:
    def __init__(self, nodes):
        self.adjacency_list = [[] for _ in range(nodes)]

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def print_graph(self):
        for idx, nodes in enumerate(self.adjacency_list):
            adjacent_nodes = ", ".join(map(str, nodes))
            print(f"{idx}: \t {adjacent_nodes}")


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class GraphLL:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node