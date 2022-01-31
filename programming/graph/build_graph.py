class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.adjacency_list = [[] for _ in range(self.V)]

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def print_graph(self):
        for idx, nodes in enumerate(self.adjacency_list):
            adjacent_nodes = ", ".join(map(str, nodes))
            print(f"{idx}: \t {adjacent_nodes}")

    def bfs(self, source):
        queue = [source]
        result = []
        visited = set()
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in visited:
                result.append(node)
                visited.add(node)
                for item in self.adjacency_list[node]:
                    queue.append(item)
        return result

    def dfs(self, source, result, visited):
        result.append(source)
        visited[source] = source
        for n in range(len(self.adjacency_list[source])):
            if n not in visited:
                self.dfs(n, result, visited)

    def detect_cycle(self, source):
        queue = [source]
        visited = set()
        while len(queue) > 0:
            node = queue.pop(0)
            if node == source:
                return True
            if node not in visited:
                visited.add(node)
                for item in self.adjacency_list[node]:
                    queue.append(item)
        return False


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(3,4)
    g.add_edge(3,2)
    # g.add_edge(3,1)

    g.print_graph()


    
    bfs_result = g.bfs(3)
    print(bfs_result)
    # dfs_result = []
    # g.dfs(3, dfs_result, {})
    # print(dfs_result)
