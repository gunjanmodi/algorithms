from collections import deque

def steps_by_knight(source, target, N):
    
    i, j, distance = 0, 1, 2
    rows = [2, 2, -2, -2, 1, 1, -1, -1]
    cols = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = deque()
    visited = set()

    queue.append((source[0], source[1], 0))
    
    while queue:
        node = queue.popleft()

        if node[i] == target[0] and node[j] == target[1]:
            return node[distance]

        if node not in visited:
            visited.add(node)
            
            for k in range(8):
                x = node[i] + rows[k]
                y = node[j] + cols[k]
                child = (x, y, node[distance] + 1)
                if is_valid(child[i], child[j], N) and child not in visited:
                    queue.append(child)
    
    return -1

def is_valid(i, j, n):
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    return True
        
    
if __name__ == '__main__':
    print(steps_by_knight([0, 7], [7, 0], 8))
