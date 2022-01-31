from collections import deque


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
            print(f"{idx}:  {adjacent_nodes}")


def shortest_path_unweighted(adj, source, nodes):
    print(adj)
    visited = set()
    queue = deque()
    result = [float('inf')] * nodes
    result[source] = 0
    visited.add(source)
    queue.append(source)
    while queue:
        node = queue.popleft()
        children = adj[node]
        for child in children:
            if child not in visited:
                result[child] = result[node] + 1
                queue.append(child)
                visited.add(child)
        
    return result
   

if __name__ == '__main__':
    edges = [[0, 1],[0, 2],[0, 4],[1, 3],[2, 3],[2, 4],[3, 5],[4, 5]]
    g = Graph(6)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    output = shortest_path_unweighted(g.adjacency_list, 0, g.V)
    print(output)