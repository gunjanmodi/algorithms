"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(histogram):
    array = [-1] * len(histogram)
    min_so_far = float('inf')
    for i in range(1, len(histogram)):
        min_so_far = min(min_so_far, histogram[i])
        


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([6,2,5,4,5,1,6]))