def ngl(array):
    stack = []
    result = []

    for i in range(len(array)):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1] > array[i]:
            result.append(stack[-1])
        elif len(stack) > 0 and stack[-1] < array[i]:
            while stack[-1] < array[i]:
                stack.pop()
                if len(stack) == 0:
                    stack.append(-1)
                    break
            result.append(stack[-1])
        stack.append(array[i])
        
    return result


print(ngl([1, 3, 2, 4]))
print(ngl([1, 2, 1]))
print(ngl([6, 2, 0, 1, 3])) 