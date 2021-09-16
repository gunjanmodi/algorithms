"""
Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the
numbers less than or equal to k together.
"""

def min_swap(arr, k):
    if not arr:
        return 0
    min_swap_count = 0

    for i in range(len(arr)):
        arr[i] -= k

    start = 1 if arr[0] < 0 else 0
    for i in range(start, len(arr)):
        if arr[i] <= 0:
            min_swap_count += 1

    return min_swap_count if not len(arr) == k else 0


print(min_swap([2, 1, 5, 6, 3], 3))  # Expected: 1
#              [-1, -2, 2, 3, 0]
print(min_swap([2, 7, 9, 5, 8, 7, 4], 6))  # Expected: 2
#              [-4, 1, 3, -1, 2, 1, -2]
print(min_swap([20, 12, 17], 6))  # Expected: 0
#             [-20, -12,-17]
print(min_swap([10, 12, 20, 20, 5, 19, 19, 12, 1, 20, 1], 1)) # Expected: 1
#              [9,  11, 19, 19, 4, 18, 18, 11, 0, 19, 0]