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


def search_matrix(matrix, target):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = (rows * cols) - 1

    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid//cols][mid%cols]

        if num  == target:
            return True
        elif num < target:
            left = mid + 1 
        else:
            right = mid - 1
            
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_matrix(matrix, 1))
matrix = [[1]]
print(search_matrix(matrix, 2))
