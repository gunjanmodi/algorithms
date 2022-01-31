def num_enclaves_dfs(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    def dfs(matrix, i, j):
        if (i < 0 or i >= rows or j < 0 or j >= cols):
            return
        
        if matrix[i][j] != 1:
            return

        matrix[i][j] = -1

        dfs(matrix, i-1, j)
        dfs(matrix, i, j-1)
        dfs(matrix, i+1, j)
        dfs(matrix, i, j +1)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                dfs(matrix, i, j)

    result = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                result += 1

    return result


from collections import deque
def num_enclaves_bfs(matrix):
    if not (matrix or matrix[0]):
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])

    queue = deque()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        
        if i < 0 or i >= rows or j < 0 or j >= cols:
            continue

        if matrix[i][j] != 1:
            continue
        
        matrix[i][j] = -1

        queue.append((i - 1, j))
        queue.append((i + 1, j))
        queue.append((i, j - 1))
        queue.append((i, j + 1))


    result = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                result += 1
    return result


if __name__ == '__main__':
    matrix = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    result = num_enclaves_dfs(matrix)
    print(result)

    matrix = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    result = num_enclaves_dfs(matrix)
    print(result)

    matrix = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    result = num_enclaves_bfs(matrix)
    print(result)

    matrix = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    result = num_enclaves_bfs(matrix)
    print(result)