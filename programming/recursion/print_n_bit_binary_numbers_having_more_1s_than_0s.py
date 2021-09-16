"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(n):
    result = []
    recursive_helper(1, 0, ['1'], n - 1, result)
    return result


def recursive_helper(count_one, count_zero, output_string, n, result):
    if n == 0:
        result.append("".join(output_string))
        return
    output_string_copy = output_string[:]
    n -= 1
    output_string.append('1')
    recursive_helper(count_one + 1, count_zero, output_string, n, result)
    if count_one > count_zero:
        output_string_copy.append('0')
        recursive_helper(count_one, count_zero + 1, output_string_copy, n, result)




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main(2))
print(main(3))
print(main(4))
print(main(1))

# print(main(20))