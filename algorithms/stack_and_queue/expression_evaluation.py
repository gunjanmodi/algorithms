"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(expression):
    digits = []
    for token in expression:
        if token.isdigit():
            digits.append(token)
        elif token in "+-*/":
            b = int(digits.pop())
            a = int(digits.pop())
            digits.append(calculate(a, b, token))
    return digits[-1]


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        try:
            return a // b
        except ZeroDivisionError:
            return 1



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("231*+9-"))
print(main("123+*8-"))