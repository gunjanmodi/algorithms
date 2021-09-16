def search_matrix(matrix, target):
    left = 0
    right = len(matrix[0]) - 1 if len(matrix[0]) > 1 else 0

    while left < len(matrix) and right >= 0:
        num = matrix[left][right]
        if num == target:
            return True
        elif num > target:
            right -= 1
        else:
            left += 1

    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_matrix(matrix, 1))
matrix = [[1]]
print(search_matrix(matrix, 2))
