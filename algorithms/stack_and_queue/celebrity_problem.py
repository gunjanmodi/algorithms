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
    result = set()
    celebrities = []
    for i in range(len(matrix)):
        ks = []
        for j in range(len(matrix[i])):
            if i !=j and matrix[i][j] == 1:
                ks.append(j)
        celebrities.append(ks)
    for celebrity in celebrities:
        for c in celebrity:
            if len(celebrities[c]) == 0:
                return c
    return -1



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([[0, 1, 0], [0, 0, 0], [0, 1, 0]]))
print(main([[0, 1], [1, 0]]))
print(main([ [0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0]]))