"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array, target):
    subset = []
    n = len(array)
    for _ in range(n + 1):
        subset.append([False for _ in range(target + 1)])

    for i in range(n + 1):
        for j in range(target + 1):
            if j == 0:
                subset[i][j] = True
    
            if i == 0:
                subset[i][j] = False

    for i in range(n + 1):
        for j in range(target + 1):

            if j < array[i-1]:
                subset[i][j] = subset[i-1][j]
                
            if j >= array[i-1]:
                subset[i][j] = (subset[i-1][j] or
                            subset[i - 1][j-array[i-1]])

    return subset[-1][-1]


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([3, 34, 4, 12, 5, 2], 9))
print(main([3, 34, 4, 12, 5, 2], 30))