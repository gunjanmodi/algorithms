from dis import dis
from turtle import distance


class Graph:
    def __init__(self, nodes, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(nodes)]

    def add_edge(self, node1, node2):
        self.adj[node1].append(node2)


def floyd_warshall_algorithm(adj_matrix):
    n = len(adj_matrix)
    path = [ [-1 for j in range(n)] for row in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                path[i][j] = 0
            elif adj_matrix[i][j] != float('inf'):
                path[i][j] = adj_matrix[i][j]
            else:
                path[i][j] = float('inf')


    for k in range(n):
        for i in range(n):
            for j in range(n):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])

    return path

if __name__ == '__main__':
    I = float('inf')
    adj_matrix = [
        [0, I, -2, I],
        [4, 0, 3, I],
        [I, I, 0, 2],
        [I, -1, I, 0]
    ]

    output = floyd_warshall_algorithm(adj_matrix)
    print(output)