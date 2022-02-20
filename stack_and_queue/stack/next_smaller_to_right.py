def next_smaller_right(array):
    stack = []
    result = []

    for i in reversed(range(len(array))):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1] < array[i]:
            result.append(stack[-1])
        elif len(stack) > 0 and stack[-1] > array[i]:
            while stack[-1] > array[i]:
                stack.pop()
                if len(stack) == 0:
                    stack.append(-1)
                    break
            result.append(stack[-1])
        stack.append(array[i])
    result.reverse()
    return result


print(next_smaller_right([1, 3, 2, 4]))
print(next_smaller_right([1, 2, 1]))
print(next_smaller_right([6, 2, 0, 1, 3]))