class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_list = [[] for _ in range(nodes)]
        self.in_degree = {k: 0 for k in range(nodes)}

    def add_edge(self, node1, node2, weight):
        self.adjacency_list[node1].append({"node": node2, "weight": weight})
        self.in_degree[node2] += 1

    def print_graph(self):
        for idx, nodes in enumerate(self.adjacency_list):
            adjacent_nodes = ", ".join(map(str, nodes))
            print(f"{idx}: \t {adjacent_nodes}")

    def topological_sort(self):
        queue = []
        sorted_order = []
        for node, count in self.in_degree.items():
            if count == 0:
                queue.append(node)

        while len(queue) > 0:
            parent = queue.pop(0)
            sorted_order.append(parent)
            for child in self.adjacency_list[parent]:
                child_node, child_weight = child['node'], child['weight']
                self.in_degree[child_node] -= 1
                if self.in_degree[child_node] == 0:
                    queue.append(child_node)
        return sorted_order

    def shortest_path(self, source):
        distances = [float('inf') for _ in range(self.nodes)]
        topological_order = self.topological_sort()
        distances[source] = 0
        for node in topological_order:
            for adjacent in self.adjacency_list[node]:
                child_node, weight = adjacent["node"], adjacent["weight"]
                if distances[child_node] > distances[node] + weight:
                    distances[child_node] = distances[node] + weight
        return distances


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 4, 1)
    g.add_edge(1, 2, 3)
    g.add_edge(4, 2, 2)
    g.add_edge(4, 5, 4)
    g.add_edge(2, 3, 6)
    g.add_edge(5, 3, 1)
    # g.print_graph()
    # print(g.in_degree)
    result = g.shortest_path(0)
    print(result)
