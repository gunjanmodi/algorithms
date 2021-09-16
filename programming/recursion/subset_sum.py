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
    n = len(array) - 1
    return subset_helper(array, target, n-1)


def subset_helper(array, target, n):
    if target == 0:
        return True
    if n == 0:
        return False

    if array[n] <= target:
        return subset_helper(array, target-array[n], n - 1) or subset_helper(array, target, n - 1)
    return subset_helper(array, target, n-1)


    


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 3, 7, 2, 5], 9))
print(main([1, 3, 7, 2, 5], 30))
