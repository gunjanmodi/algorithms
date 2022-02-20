def find_factorial(num):
    if num == 0:
        return 1
    num *= find_factorial(num-1)
    return num


print(find_factorial(3))