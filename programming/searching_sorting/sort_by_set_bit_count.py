"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O(n) | Space: O(n)
def main(array):
    for i in range(len(array)):
        array[i] = convert_decimal_to_binary(array[i])
    array.sort(key=lambda x: x[0])
    return [tp[1] for tp in array]


def convert_decimal_to_binary(num):
    num_copy = num
    set_count = 0
    while num != 0:
        if num % 2 == 1:
            set_count += 1
        num //= 2
    return -set_count, num_copy


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([5, 2, 3, 9, 4, 6, 7, 15, 32]))
print(main([1, 2, 3, 4, 5, 6]))
