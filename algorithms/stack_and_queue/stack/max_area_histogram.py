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
    result = []
    idx, item = 0, 1
    for i in reversed(range(len(array))):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1][item] < array[i]:
            result.append(stack[-1][idx])
        elif len(stack) > 0 and stack[-1][item] > array[i]:
            while len(stack) > 0 and stack[-1][item] > array[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(n)
            else:
                result.append(stack[-1][idx])
        stack.append((i, array[i]))

    result.reverse()
    
    return result


def nearest_smaller_left(array):
    stack = []
    n = len(array) 
    result = []
    idx, item = 0, 1
    for i in range(len(array)):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1][item] < array[i]:
            result.append(stack[-1][idx])
        elif len(stack) > 0 and stack[-1][item] > array[i]:
            while len(stack) > 0 and stack[-1][item] > array[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1][idx])
        stack.append((i, array[i]))

    return result


print(max_area_histogram([6,2,5,4,5,1,6]))
print(max_area_histogram([1, 2, 3, 4, 5]))