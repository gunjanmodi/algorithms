"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array):
    total = sum(array)
    if total % 2 != 0:
        return False
    else:
        return subset_with_equal_sum(array, total//2)


def subset_with_equal_sum(array, target):
    t = []
    n = len(array)
    for i in range(n + 1):
        t.append([False for _ in range(target + 1)])

    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if array[i - 1] <= j:
                t[i][j] = t[i-1][j] or t[i-1][j-array[i-1]]
            else:
                t[i][j] = t[i-1][j]
    return t[-1][-1]




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 5, 11, 5]))
print(main([1, 3, 5]))
