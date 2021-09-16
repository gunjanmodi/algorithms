def find_happy_number(num):
    fast, slow = num, num
    while True:
        fast = find_happy_number_helper(find_happy_number_helper(fast))
        slow = find_happy_number_helper(slow)
        if fast == slow:
            break
    return slow == 1


def find_happy_number_helper(num):
    sum = 0
    for digit in str(num):
        digit = int(digit)
        sum += digit * digit
    return sum

if __name__ == '__main__':
    output = find_happy_number(12)
    print(output)
    output = find_happy_number(23)
    print(output)