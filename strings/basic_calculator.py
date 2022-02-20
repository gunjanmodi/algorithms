# def operation_strategy(a, b, op):
#     if op == '+':
#         return a + b
#     if op == '-':
#         return a - b
#     if op == '*':
#         return a * b
#     if op == '/':
#         return a // b
#
#
# def perform_operation(stack, operators):
#     operand2 = stack.pop()
#     operand1 = stack.pop()
#     operator = operators.pop()
#     return operation_strategy(operand1, operand2, operator)
#
#
# def calculate(s: str) -> int:
#     stack = [c for c in s if c != ' ']
#     return calculate_helper(stack)
#
#
# def calculate_helper(stack, i=0):
#     precedence = {"-": 1, "+": 2, "*": 3, "/": 4}
#     operators = []
#     digits = []
#     while i < len(stack):
#         character = stack[i]
#         if character == "(":
#             # result, i = calculate_helper(stack, i+1)
#             # digits.append(result)
#             operators.append(character)
#         if character == ")":
#             digits.append(perform_operation(digits, operators))
#             operators.pop()
#         if character.isdigit():
#             target = ''
#             while i < len(stack) and stack[i].isdigit():
#                 target += stack[i]
#                 i += 1
#             digits.append(int(target))
#             i -= 1
#         if character in ["-", "+", "*", "/"]:
#             while len(operators) != 0 and precedence.get(operators[-1], 0) > precedence.get(character, 0):
#                 digits.append(perform_operation(digits, operators))
#             operators.append(character)
#
#         i += 1
#     while len(operators) != 0:
#         digits.append(perform_operation(digits, operators))
#
#     return digits[-1]

def perform_operation(digits, operators):
    operator = operators.pop()
    operand2 = digits.pop()
    operand1 = digits.pop()
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        try:
            return operand1 / operand2
        except ZeroDivisionError:
            return 0


def calculate(string):
    characters = [character for character in string if character != ' ']

    digits = []
    operators = []
    precedence = {"/": 2, "*": 2, "+": 1, "-": 1}

    i = 0

    while i < len(characters):
        character = characters[i]
        if character == "(":
            operators.append(character)
        elif character == ")":
            digits.append(perform_operation(digits, operators))
            operators.pop()
        elif character.isdigit():
            target = ''
            while i < len(characters) and characters[i].isdigit():
                target += characters[i]
                i += 1
            i -= 1
            digits.append(int(target))
        elif character in "+-*/":
            while len(operators) > 0 and precedence.get(operators[-1], 0) > precedence.get(character, 0):
                digits.append(perform_operation(digits, operators))
            operators.append(character)
        i += 1

    while len(operators) != 0:
        digits.append(perform_operation(digits, operators))

    return float(digits[-1])


print(calculate("((3 + (4 / 2)) * (5 + 6))"))
print(calculate("(5 + 6)"))
print(calculate("(((2 + 3) * (4 - 3)) / ((4 + 0) - (4 - 2)))"))
print(calculate("(1 + (2 / (3 - 3)))"))
print(calculate("((-2) + 3)"))

