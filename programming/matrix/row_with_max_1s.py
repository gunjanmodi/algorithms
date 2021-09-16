def row_with_max1s(matrix):
    max_row_count = 0
    resulting_row = -1
    for i in range(len(matrix)):
        current_row_count = 0
        for num in matrix[i]:
            if num == 1:
                current_row_count += 1
        if current_row_count > max_row_count:
            resulting_row = i
            max_row_count = current_row_count
    return resulting_row


print(row_with_max1s([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(row_with_max1s([[0, 0], [1, 1]]))
