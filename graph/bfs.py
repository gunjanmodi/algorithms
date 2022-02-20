from collections import deque

def bfs(self, V, adj):
    if not adj:
        return
    result = []
    queue = deque()
    visited = set()
        
    queue.append(0)
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            neighbours = adj[node]
            for neighbour in neighbours:
                queue.append(neighbour)
        visited.add(node)
        
    return result