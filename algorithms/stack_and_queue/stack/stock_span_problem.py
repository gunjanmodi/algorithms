# def stock_span(prices):
#     stack1 = []
#     stack2 = []
#     result = []
#     for i in range(len(prices)):
#         if len(stack1) == 0:
#             result.append(1)
#         elif len(stack1) > 0 and stack1[-1][1] > prices[i]:
#             result.append(1)
#         elif len(stack1) > 0 and stack1[-1][1] < prices[i]:
#             while stack1[-1][1] < prices[i]:
#                 stack2.append(stack1.pop())
#                 if len(stack1) == 0:
#                     break
#             if len(stack1) == 0:
#                 result.append(i+1)
#             else:
#                 result.append(i - stack1[-1][0])
                    
#             while len(stack2) > 0:
#                 stack1.append(stack2.pop())

#         stack1.append((i, prices[i]))
#     return result

def stock_span(array):
    stack = []
    result = []

    for i in range(len(array)):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1][1] > array[i]:
            result.append(stack[-1][0])
        elif len(stack) > 0 and stack[-1][1] <= array[i]:
            while len(stack) > 0 and stack[-1][1] <= array[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1][0])
        stack.append((i, array[i]))
    i = 0
    while i < len(result):
        result[i] = i - result[i]
        i += 1
    return result


print(stock_span([100, 80, 60, 70, 60, 75, 85]))
print(stock_span([10, 4, 5, 90, 120, 80]))