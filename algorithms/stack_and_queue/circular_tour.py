"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

from queue import Queue
# Time: O() | Space: O()
def main(lis):
    start = 0
    s = 0
    d = 0
    for i in range(len(lis)):
        s += lis[i][0] - lis[i][1]
        if s < 0:
            start = i + 1
            d += s
            s = 0
    return start if s + d >= 0 else -1









# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([[4, 6], [6, 5], [7, 3], [4, 5]]))