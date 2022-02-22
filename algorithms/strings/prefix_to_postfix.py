
# Time: O(n), Space: O(n)
def prefix_to_postfix(string):
    print(string)
    stack = []
    for character in string:
        if character != ' ':
            stack.append(character)

    operators = {"+", "-", "*", "/", "^"}
    temp_stack = []

    for i in reversed(range(len(stack))):
        character = stack[i]
        if character in operators:
            equation_fragment = list()
            equation_fragment.append(temp_stack.pop())
            equation_fragment.append(temp_stack.pop())
            equation_fragment.append(stack.pop())
            temp_stack.append("".join(equation_fragment))
        else:
            temp_stack.append(stack.pop())
    print(temp_stack[0])
    return temp_stack[0]


# prefix_to_postfix("*+AB-CD")
# prefix_to_postfix("*-A/BC-/AKL")
prefix_to_postfix("+ + A * B C D")
prefix_to_postfix("* + A B + C D")
