class Graph():
    def __init__(self, edges, vertices) -> None:
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]
        
        for u, v in edges:
            self.adj[u].append(v)
        print(self.adj)


def dfs(graph, vertices):
    visited = []
    arrival = []
    departure = []

    for _ in range(vertices):
        visited.append(False)
        arrival.append(False)
        departure.append(False)

    timer = [-1]
    for u in range(vertices):
        if not visited[u]:
            dfs_helper(graph, u, visited, arrival, departure, timer)

    for i in range(vertices):
        print("Node: ", i, " Arrival: ", arrival[i], " Departure: ", departure[i])


def dfs_helper(graph, u, visited, arrival, departure, timer):
    visited[u] = True
    timer[0] += 1
    arrival[u] = timer[0]

    for v in graph[u]:
        if not visited[v]:
            dfs_helper(graph, v, visited, arrival, departure, timer)

    timer[0] += 1
    departure[u] = timer[0]


if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
    n = 8
    graph = Graph(edges, n)
    dfs(graph.adj, graph.vertices)
