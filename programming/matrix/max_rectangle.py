def max_rectangle_area(matrix):
    max_rectangle = {"width": 0, "height": 0}
    current_rectangle = {"width": 0, "height": 0}
    # for row in range(len(matrix)):
    #     for col in range(len(matrix[row])):
    row, col = 0, 0
    while row < len(matrix):
        while col < len(matrix[row][col]):
            value = matrix[row][col]
            if value == 1:
                expand_rectangle(matrix, row, col, current_rectangle, max_rectangle)
                max_rectangle['width'] = max(max_rectangle['width'], current_rectangle['width'])
            current_rectangle = {"width": 0, "height": 0}
            col += 1
        row += 1




def expand_rectangle(matrix, row, col, current_rectangle, max_rectangle):
    # go right
    while row < len(matrix) and col < len(matrix[row]):
        if matrix[row][col] == 1:
            current_rectangle["width"] += 1
            col += 1
        else:
            break
    # go left


# print(max_rectangle_area([[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]))
print(max_rectangle_area([[0, 1, 1, 1], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 1]]))
print(max_rectangle_area([[0, 1, 1, 0], [1, 1, 0, 0]]))

