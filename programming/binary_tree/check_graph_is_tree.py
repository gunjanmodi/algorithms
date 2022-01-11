from collections import defaultdict


class Graph:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def is_cyclic_util(self, node, parent):
        self.visited[node] = True
        for edge in self.graph[node]:
            if self.visited[edge] == False:
                if self.is_cyclic_util(edge, node) == True:
                    return True
            elif edge != parent:
                return True
        return False
        

    def is_graph_cyclic(self):
        self.visited = [False] * self.nodes
        self.is_cyclic_util(0, -1)
        return False

    def is_graph_connected(self):
        for node in self.graph.keys():
            if not self.visited[node]:
                return False
        return True

    def is_binary_tree(self):
        return (not self.is_graph_cyclic()) and self.is_graph_connected()
    


if __name__ == '__main__':
    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)

    print(g1.is_binary_tree())
    
    g2 = Graph(5)
    g2.add_edge(1, 0)
    g2.add_edge(0, 2)
    g2.add_edge(2, 1)
    g2.add_edge(0, 3)
    g2.add_edge(3, 4)

    print(g2.is_binary_tree())