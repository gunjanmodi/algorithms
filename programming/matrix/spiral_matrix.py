# def spiral_order(matrix):
#     # me = MatrixExplorer(matrix)
#     me.traverse()
#     return me.result


# class MatrixExplorer:
#     def __init__(self, matrix):
#         self.result = []
#         self.matrix = matrix
#         self.matrix_row_length = len(self.matrix)
#         self.matrix_column_length = len(self.matrix[0])
#
#
#     def traverse(self):
#         row = 0
#         column = 0
#         self.go_east(row, column)
#
#     def go_east(self, row, column):
#         while column < self.matrix_column_length:
#             self.result.append(self.matrix[row][column])
#             column += 1
#         self.go_south(row + 1, column - 1)
#
#     def go_south(self, row, column):
#         while row < self.matrix_row_length:
#             self.result.append(self.matrix[row][column])
#             row += 1
#         self.go_west(row - 1, column - 1)
#
#     def go_west(self, row, column):
#         while column >= 0:
#             self.result.append(self.matrix[row][column])
#             column -= 1
#         self.go_north(row - 1, column + 1)
#
#     def go_north(self, row, column):
#         while row > 0:
#             self.result.append(self.matrix[row][column])
#             row -= 1
#
#         self.matrix_row_length -= 1
#         self.matrix_column_length -= 1
#         self.go_east(row+1, column+1)


#
# class MatrixExplorer:
#     def __init__(self, matrix):
#         self.result = []
#         self.matrix = matrix
#         self.matrix_row_length = len(self.matrix)
#         self.matrix_column_length = len(self.matrix[0])


# def spiral_order(matrix):
#     result = []
#     matrix_row_length = len(matrix) - 1
#     matrix_column_length = len(matrix[0]) - 1
#     row = 0
#     column = 0
#     iteration_layer = 0
#
#     while row <= matrix_row_length and column <= matrix_column_length:
#
#         # Go east
#         while column <= matrix_column_length:
#             result.append(matrix[row][column])
#             column += 1
#         row += 1
#         column -= 1
#
#         # Go south
#         while row <= matrix_row_length:
#             result.append(matrix[row][column])
#             row += 1
#         row -= 1
#         column -= 1
#
#         # Go west
#         while column >= iteration_layer:
#             result.append(matrix[row][column])
#             column -= 1
#         row -= 1
#         column += 1
#
#         # Go north
#         while row > iteration_layer:
#             result.append(matrix[row][column])
#             row -= 1
#         row += 1
#         column += 1
#
#         matrix_row_length -= 1
#         matrix_column_length -= 1
#         if matrix_column_length > matrix_row_length:
#             matrix_column_length -= 1
#         if matrix_row_length > matrix_column_length:
#             matrix_row_length -= 1
#         iteration_layer += 1
#
#     return result


def spiral_order(matrix):
    start_row, end_row = 0, len(matrix) - 1
    start_col, end_col = 0, len(matrix[0]) - 1
    result = []

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col):
            result.append(matrix[start_row][i])

        for j in range(start_row, end_col):
            result.append(matrix[j][end_col])

        for k in reversed(range(start_col, end_col+1)):
            result.append(matrix[end_row][k])

        for l in reversed(range(start_row+1, end_row)):
            result.append(matrix[l][start_col])


        start_row += 1
        start_col += 1

        end_row -= 1
        end_col -= 1



    return result





output = spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]])
print(output)
output = spiral_order([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
print(output)
output = spiral_order([[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]])
print(output)