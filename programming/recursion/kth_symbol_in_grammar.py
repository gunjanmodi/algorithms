"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

import math
# Time: O() | Space: O()
def solve(n, k):
    if n == 1 or k == 1:
        return 0
    mid = math.pow(2, n - 1) // 2
    if k <= mid:
        return solve(n-1, k)
    else:
        return int(not solve(n-1, k-mid))



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(solve(1, 1))
print(solve(2, 1))
print(solve(2, 2))
print(solve(3, 1))