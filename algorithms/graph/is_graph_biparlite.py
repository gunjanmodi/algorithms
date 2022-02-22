from collections import deque
def is_biparlite_bfs(graph):
    color = {}
    queue = deque()
    
    for i in range(len(graph)):
        if i not in color:
            color[i] = 1
            queue.append(i)
    
            while queue:
                current = queue.popleft()
                for neighbour in graph[current]:
                    if neighbour not in color:
                        color[neighbour] = -color[current]
                        queue.append(neighbour)
                    elif color[neighbour] == color[current]:
                        return False
    return True


def is_biparlite_dfs(graph):
    colors = {}
    for i in range(len(graph)):
        if i not in colors:
            colors[i] = 1
            if not dfs(graph, colors, i):
                return False
    return True


def dfs(graph, colors, current):
    for neighbour in graph[current]:
        if neighbour not in colors:
            colors[neighbour] = -colors[current]
            if not dfs(graph, colors, neighbour):
                return False
        elif colors[neighbour] == colors[current]:
            return False
    return True


if __name__ == '__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print(is_biparlite_bfs(graph))
    print(is_biparlite_dfs(graph))

    graph = [[1,3],[0,2],[1,3],[0,2]]
    print(is_biparlite_bfs(graph))
    print(is_biparlite_dfs(graph))