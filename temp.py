def remove_k_digits(num, k):
    stack = []
    for n in num:
        while stack and k and stack[-1] > n:
            stack.pop()
            k -= 1
        stack.append(n)
        
    while k:
        stack.pop()
        k -= 1

    return ''.join(stack).lstrip('0') or '0'


if __name__ == '__main__':
    # print(remove_k_digits("1432219", 3))
    # print(remove_k_digits("10200", 1))
    # print(remove_k_digits("10", 2))
    print(remove_k_digits("9", 1))
    