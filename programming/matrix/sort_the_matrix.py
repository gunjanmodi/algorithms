def sort_matrix(matrix):
    temp_array = [0] * (len(matrix) * len(matrix[0]))
    k = 0
    for row in matrix:
        for value in row:
            temp_array[k] = value
            k += 1
    temp_array.sort()

    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = temp_array[k]
            k += 1
    return matrix
print(sort_matrix([[5,4,7], [1,3,8], [2,9,6]]))