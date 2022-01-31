def flood_fill(image, sr, sc, newColor):
    if not (image or image[0]):
        return image
    
    rows = len(image)
    cols = len(image[0])
    oldColor = image[sr][sc]
    
    def dfs(matrix, i, j):
        if (i < 0 or i >= rows or j < 0 or j >= cols):
            return
        
        if matrix[i][j] != oldColor:
            return
        
        matrix[i][j] = newColor
        
        dfs(matrix, i-1, j)
        dfs(matrix, i+1, j)
        dfs(matrix, i, j-1)
        dfs(matrix, i, j+1)
    
    if newColor != oldColor:    
        dfs(image, sr, sc)
        
    return image



if __name__ == '__main__':
    matrix = [[1,1,1],[1,1,0],[1,0,1]]
    result = flood_fill(matrix, 1, 1, 2)
    print(result)

    matrix = [[0,0,0],[0,0,0]]
    result = flood_fill(matrix, 0, 0, 1)
    print(result)


    matrix = [[0,0,0],[0,1,1]]
    result = flood_fill(matrix, 1, 1, 1)
    print(result)