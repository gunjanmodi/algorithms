
# Time: O(n), Space: O(n)
def prefix_to_postfix(string):
    stack = string.split(" ")[:-1]
    stack_ref = stack[::]

    operators = {"+", "-", "/", "*", "^"}
    sum = 0
    temp_stack = []
    for i in range(len(stack_ref)):
        character = stack_ref[i]
        if character in operators:
            expression = []
            expression.append(temp_stack.pop())
            expression.append(stack.pop(0))
            expression.append(temp_stack.pop())
            if int(float(expression[0])) < int(float(expression[-1])):
                expression[0], expression[-1] = expression[-1], expression[0]
            sum += eval("".join(expression))
            temp_stack.append(str(sum))
            sum = 0
        else:
            temp_stack.append(stack.pop(0))
    return int(float(temp_stack[0]))


output = prefix_to_postfix("31 4 50 + * ?")
print(output)
output = prefix_to_postfix("12 23 + 14 - ?")
print(output)
output = prefix_to_postfix("2 43 12 * + 12 + ?")
print(output)
output = prefix_to_postfix("12 3 + 12 3 + * 12 3 + / ?")
print(output)
output = prefix_to_postfix("32 34 12 * + 1 2 + * 1 1 + / 23 21 - * ?")
print(output)
output = prefix_to_postfix("12 10 * 12 / ?")
print(output)
