def clumsy(n):
    expression = get_clumsy_expression(n)
    expression = evaluate_multiplication_and_division(expression)
    return evaluate_addition_and_subtration(expression)


def evaluate_multiplication_and_division(expression):
    operators = {"*", "/"}
    i = 0
    while i < len(expression):
        token = expression[i]
        if token in operators:
            a = expression[i-1]
            b = expression[i+1]
            result = perform_operation(token, a, b)
            expression[i-1] = 0
            expression[i] = 0
            expression[i+1] = result
            i += 1
        i += 1
    return [token for token in expression if token != 0]


def evaluate_addition_and_subtration(expression):
    i = 1
    while i < len(expression):
        token = expression[i]
        a = expression[i-1]
        b = expression[i+1]
        result = perform_operation(token, a, b)
        expression[i-1] = 0
        expression[i] = 0
        expression[i+1] = result
        i += 2
    return expression[-1]


def perform_operation(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b


def get_clumsy_expression(n):
    operators = ["*", "/", "+", "-"]
    result = []
    i = n
    j = 0
    while i > 0:
        result.append(i)
        if i > 1:
            result.append(operators[j])
            j += 1
            if j == 4:
                j = 0
        i -= 1
    return result


print(clumsy(4))
print(clumsy(10))
