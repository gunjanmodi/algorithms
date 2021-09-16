"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

from collections import Counter
# Time: O() | Space: O()
def main(array):
    counters = Counter(array)
    deciding_factor = len(array) // 2
    for key, value in counters.items():
        if value > deciding_factor:
            return key
    return -1


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([3, 1, 3, 3, 2]))
print(main([1, 2, 3]))