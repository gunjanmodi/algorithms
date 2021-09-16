def reverse(x):
    result = []
    is_negative = True if x < 0 else False

    if is_negative:
        str_int = str(x)[1:]
    else:
        str_int = str(x)

    for char in reversed(range(len(str_int))):
        result.append(str_int[char])
    tentative_output = "".join(result)
    if int(tentative_output) > 2 ** 31:
        return 0
    else:
        return int("-"+tentative_output) if is_negative else int(tentative_output)


def reverse_new(x):
    result = []
    is_negative = True if x < 0 else False
    if is_negative:
        x = x * -1
    while x > 0:
        p = x % 10
        result.append(p)
        x = x // 10

    number = 0
    i = len(result) - 1
    multiplier = 0.1
    while i >= 0:
        multiplier *= 10
        number += result[i] * int(multiplier)
        i -= 1

    if is_negative:
        return number * -1
    return number


# output = reverse(-456)
output = reverse_new(-456)
print(output)