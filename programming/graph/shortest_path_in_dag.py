class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for v in range(self.vertices)]

    def add_edge(self, source, target):
        self.adjacency_list[source].append(target)


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(3, 4)
    g.add_edge(3, 2)

    print(g.adjacency_list)
