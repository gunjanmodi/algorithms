from collections import defaultdict, deque
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)


def topological_sort_bfs(graph, nodes):
    result = []
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
        result.append(node)
        adjacents = graph[node]
        for adjacent in adjacents:
            in_degrees[adjacent] -= 1
            if in_degrees[adjacent] == 0:
                queue.append(adjacent)

    return result


def dfs_helper(u, graph, visited, stack):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs_helper(v, graph, visited, stack)
    stack.insert(0, u)


def topological_sort_dfs(graph, vertices):
    visited = set()
    stack = []
    for u in range(vertices):
        if u not in visited:
            dfs_helper(u, graph, visited, stack)
    return stack





if __name__ == '__main__':
    edges = [[0, 2], [0, 3], [1, 3], [1, 4]]
    g = Graph(5)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    output = topological_sort_bfs(g.graph, g.nodes)
    print("BFS: ", output)
    output = topological_sort_dfs(g.graph, g.nodes)
    print("DFS: ",output)


    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    g = Graph(5)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    output = topological_sort_bfs(g.graph, g.nodes)
    print("BFS: ", output)
    output = topological_sort_dfs(g.graph, g.nodes)
    print("DFS: ",output)



