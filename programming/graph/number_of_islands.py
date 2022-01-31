def dfs(grid, i, j, rows, cols, visited):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return

    if (i,j) in visited or grid[i][j] == '0':
        return

    visited.add((i, j))

    dfs(grid, i - 1, j, rows, cols, visited)
    dfs(grid, i + 1, j, rows, cols, visited)
    dfs(grid, i, j - 1, rows, cols, visited)
    dfs(grid, i, j + 1, rows, cols, visited)

def number_of_islands(grid):
    result = 0

    if not grid:
        return result

    rows = len(grid)
    cols = len(grid[0])
    
    visited = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(grid, i, j, rows, cols, visited)
                result += 1

    return result


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = number_of_islands(grid)
    print(result)

