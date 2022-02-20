def max_area_rectangle_binary(matrix):
    if not matrix:
        return
    max_area = 0
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            if row[j] == 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] += row[j]
        current_max = max_area_histogram(matrix[i])
        max_area = max(max_area, current_max)

    return max_area


def max_area_histogram(array):
    nsr = nearest_smaller_right(array)
    nsl = nearest_smaller_left(array)
    max_area = 0
    for i in range(len(array)):
        max_area = max(max_area, (nsr[i] - nsl[i] - 1) * array[i])
    return max_area

def nearest_smaller_right(array):
    stack = []
    n = len(array) 
    result = [n] * n
    idx, item = 0, 1
    for i in reversed(range(len(array))):
        if len(stack) == 0:
            result[i] = n
        elif len(stack) > 0 and stack[-1][item] < array[i]:
            result[i] = stack[-1][idx]
        else:
            while len(stack) > 0 and stack[-1][item] >= array[i]:
                stack.pop()
            if len(stack) == 0:
                result[i] = n
            else:
                result.append(stack[-1][idx])
        stack.append((i, array[i]))
    
    # result.reverse()
    
    return result


def nearest_smaller_left(array):
    stack = []
    n = len(array) 
    result = [-1] * n
    idx, item = 0, 1
    for i in range(len(array)):
        if len(stack) == 0:
            result[i] = -1
        elif len(stack) > 0 and stack[-1][item] < array[i]:
            result[i] = stack[-1][idx]
        else:
            while len(stack) > 0 and stack[-1][item] >= array[i]:
                stack.pop()
            if len(stack) == 0:
                result[i] = -1
            else:
                result[i] = stack[-1][idx]
        stack.append((i, array[i]))

    return result

print(max_area_rectangle_binary([[1, 1, 1, 1, 1],[0, 1, 0, 0, 0]]))
print(max_area_rectangle_binary([[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]])) 