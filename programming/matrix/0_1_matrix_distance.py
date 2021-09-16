def distance(matrix):
    if not matrix:
        return
    row_size = len(matrix)
    column_size = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                upper = matrix[i - 1][j] if i - 1 >= 0 else float('inf')
                right = matrix[i][j + 1] if j + 1 < column_size else float('inf')
                bottom = matrix[i + 1][j] if i + 1 < row_size else float('inf')
                left = matrix[i][j - 1] if j - 1 >= 0 else float('inf')
                if right == 0:
                    matrix[i][j] = 0
                matrix[i][j] = min(upper, bottom, left) + 1
    return matrix


# print(distance([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
# print(distance([
#     [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
#     [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
#     [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
#     [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
# ))

"""
[[1,0,1,1,0,0,1,0,0,1],
 [0,1,1,0,1,0,1,0,1,1],
 [0,0,1,0,1,0,0,1,0,0],
 [1,0,1,0,1,1,1,1,1,1],
 [0,1,0,1,1,0,0,0,0,1],
 [0,0,1,0,1,1,1,0,1,0]
 [0,1,0,1,0,1,0,0,1,1],
 [1,0,0,0,1,2,1,1,0,1],
 [2,1,1,1,1,2,1,0,1,0],
 [3,2,2,1,0,1,0,0,1,1]]
"""
print(distance(([[0,1,0,1,1],
                 [1,1,0,0,1],
                 [0,0,0,1,0],
                 [1,0,1,1,1],
                 [1,0,0,0,1]])))
# [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[2,0,0,0,1]]
