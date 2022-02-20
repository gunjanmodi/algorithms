def n_bit_binary(n):
    result = []
    recursive_helper(1, 0, ['1'], n - 1, result)
    return result
    
def recursive_helper(count_one, count_zero, output_string, n, result):
    if n == 0:
        if count_one >= count_zero:
            result.append("".join(output_string))
        return
    output_string_copy = output_string[:]
    n -= 1
    output_string.append('1')
    recursive_helper(count_one + 1, count_zero, output_string, n, result)
    if count_one > count_zero:
        output_string_copy.append('0')
        recursive_helper(count_one, count_zero + 1, output_string_copy, n, result)


print(n_bit_binary(3))
        
