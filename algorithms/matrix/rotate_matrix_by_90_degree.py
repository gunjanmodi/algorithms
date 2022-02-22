"""
Rotate a matrix by 90 degree in clockwise direction without using any extra space
"""


# def rotate_matrix(matrix):
#     new_matrix = [ [0 for _ in matrix] for _ in matrix ]
#     i = len(matrix) - 1
#     m, n = 0, 0
#     while i >= 0:
#         j = 0
#         while j < len(matrix[i]):
#             new_matrix[m][n] = matrix[i][j]
#             j += 1
#             m += 1
#         i -= 1
#         m = 0
#         n += 1
#     return new_matrix

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)
    row = 0
    while row < n:
        left = 0
        right = len(matrix[row]) - 1
        while left < right:
            matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
            left += 1
            right -= 1
        row += 1
    return matrix


print(rotate_matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))
# print(rotate_matrix([
#     [1,2,3, 4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13, 14, 15, 16],
# ]))