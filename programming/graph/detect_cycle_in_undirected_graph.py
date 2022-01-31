from collections import deque

class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.adjacency_list = [[] for _ in range(self.V)]

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)


def detect_cycle_undirected_graph_bfs(graph, nodes):
    visited = set()
    queue = deque()
    visited.add(0)
    queue.append((0, -1))

    while queue:
        vertex, parent = queue.popleft()

        for adjacent in graph[vertex]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append((adjacent, vertex))
            elif adjacent != parent:
                return True
    return False



def detect_cycle_undirected_graph_dfs(graph, nodes):
    def dfs_helper(adj, node, visited, parent):
        visited.add(node)
        children = adj[node]
        for child in children:
            if child not in visited:
                if dfs_helper(adj, child, visited, node) == True:
                    return True
            if node != parent:
                return True

    visited = set()
    is_cyclic = False
    for node in range(nodes):
        if node not in visited:
            is_cyclic = dfs_helper(graph, node, visited, -1)
            if is_cyclic:
                return True

    return is_cyclic


if __name__ == '__main__':
    edges = [[1,2], [2,3]]
    g = Graph(4)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    output = detect_cycle_undirected_graph(g.adjacency_list, g.V)
    print(output)


    edges = [[6, 0],[0, 2],[2, 4],[4, 7],[7, 5],[5, 1],[1, 3],[5, 6]]
    g = Graph(8)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    output = detect_cycle_undirected_graph(g.adjacency_list, g.V)
    print(output)