"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

import heapq
# Time: O(n+m) | Space: O(n+m)
def main(array1, array2):
    output = []
    output_length = len(array1) + len(array2) - 1
    # heap1 = heapq.heapify(array1)
    i = 0
    p1 = 0
    p2 = 0
    while i < output_length and p1 < len(array1) and p2 < len(array2):
        if array1[p1] <= array2[p2]:
            output.append(array1[p1])
            p1 += 1
        else:
            output.append(array2[p2])
            p2 += 1
        i += 1

    while p1 < len(array1):
        output.append(array1[p1])
        p2 += 1

    while p2 < len(array2):
        output.append(array2[p2])
        p2 += 1
    return output


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 3, 5, 7], [0, 2, 6, 8, 9]))

