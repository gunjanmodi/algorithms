def dfs(self, V, adj):
    result = []
    visited = set()
    self.dfs_helper(adj, visited, 0, result)
    return result
    
def dfs_helper(self, adj, visited, node, result):
    if node in visited:
        return
    
    result.append(node)
    visited.add(node)
    
    neighbours = adj[node]
    for neighbour in neighbours:
        self.dfs_helper(adj, visited, neighbour, result)