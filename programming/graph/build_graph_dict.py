import collections


class Graph(object):
    def __init__(self, edges):
        self.edges = edges
        self.adj = Graph._build_adjacency_list(edges)

    @staticmethod
    def _build_adjacency_list(edges):
        adj = collections.defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
        return adj


if __name__ == "__main__":
    G = Graph([
        ('u', 'v'),
        ('u', 'x'),
        ('v', 'y'),
        ('w', 'y'),
        ('w', 'z'),
        ('x', 'v'),
        ('y', 'x'),
        ('z', 'z')])