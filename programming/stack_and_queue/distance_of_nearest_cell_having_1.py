"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(matrix):
    if not matrix:
        return
    rows = len(matrix)
    columns = len(matrix[0])




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([[0,1,1,0],[1,1,0,0],[0,0,1,1]]))