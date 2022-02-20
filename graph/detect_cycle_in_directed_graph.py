from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_helper(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                return self.is_cyclic_helper(neighbour, visited, rec_stack)
            elif rec_stack[neighbour]:
                return True
            rec_stack[node] = False
            return False

    def is_cyclic(self):
        visited = [False for _ in range(self.V)]
        rec_stack = [False for _ in range(self.V)]

        for node in range(self.V):
            if not visited[node]:
                return self.is_cyclic_helper(node, visited, rec_stack)
        return False


if __name__ == '__main__':
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 0)
    graph.add_edge(3, 3)

    if graph.is_cyclic():
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")


