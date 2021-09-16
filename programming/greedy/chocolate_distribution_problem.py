"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array, m):
    if m > len(array):
        return -1
    if m == 0 or len(array) == 0:
        return 0
    array.sort()
    min_diff = float('inf')
    window_start = 0
    for window_end in range(len(array)):
        if window_end >= m - 1:
            current_diff = array[window_end] - array[window_start]
            min_diff = min(min_diff, current_diff)
            window_start += 1
    return min_diff



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([3, 4, 1, 9, 56, 7, 9, 12], 5))
print(main([7, 3, 2, 4, 9, 12, 56], 3))
