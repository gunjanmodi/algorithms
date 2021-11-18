def spiral_order(matrix):
    result = []
    if not matrix:
        return result

    row_start = 0
    row_end = len(matrix) - 1
    col_start = 0
    col_end = len(matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        for pointer in range(col_start, col_end + 1):
            result.append(matrix[row_start][pointer])
        row_start += 1

        for pointer in range(row_start, row_end + 1):
            result.append(matrix[pointer][col_end])
        col_end -= 1
        
        if row_start <= row_end:
            for pointer in reversed(range(col_start, col_end + 1)):
                result.append(matrix[row_end][pointer])
        row_end -= 1

        if col_start <= col_end:
            for pointer in reversed(range(row_start, row_end + 1)):
                result.append(matrix[pointer][col_start])
        col_start += 1

    return result


if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiral_traverse(matrix))



output = spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]])
print(output)
output = spiral_order([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
print(output)
output = spiral_order([[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]])
print(output)