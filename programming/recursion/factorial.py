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
    if n == 1:
        return 1
    return n * main(n-1)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main(7))