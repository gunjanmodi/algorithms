def balanced_binary_string_count(string):
    if not len(string):
        return 0
    stack = []
    count = 0
    for token in string:
        if len(stack) and stack[-1] != token:
            stack.pop()
            if len(stack) == 0:
                count += 1
        else:
            stack.append(token)
    return count if count > 0 else -1




# print(balanced_binary_string_count("0100110101"))
# print(balanced_binary_string_count("0111100010"))
# print(balanced_binary_string_count("0000000000"))
# print(balanced_binary_string_count("1,0,0,1,0,1,1"))


def count_subarray_with_equal_zero_and_one(array):
    overall_count = 0
    for i in range(len(array)):
        zero_count = 1 if array[i] == 0 else 0
        one_count = 1 if array[i] == 1 else 0
        for j in range(i + 1, len(array)):
            if array[j] == 0:
                zero_count += 1
            else:
                one_count += 1
            if zero_count == one_count:
                overall_count += 1
    return overall_count


print(count_subarray_with_equal_zero_and_one([1, 0, 0, 1, 0, 1, 1]))
print(count_subarray_with_equal_zero_and_one([1,1,1,1,0]))


