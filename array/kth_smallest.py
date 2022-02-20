"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
import heapq
def main(array, k):
    heapq.heapify(array)
    kth_smallest = None
    for i in range(k):
        kth_smallest = heapq.heappop(array)
    return kth_smallest


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([7, 10, 4, 3, 20, 15], 3))
