"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array1, array2, k):
    i = j = count = 0
    kth_element = None
    while count < k and i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            kth_element = array1[i]
            i += 1
        else:
            kth_element = array2[j]
            j += 1
        count += 1

    while count < k  and i < len(array1):
        kth_element = array1[i]
        i += 1
        count += 1

    while count < k  and j < len(array2):
        kth_element = array2[j]
        j += 1
        count += 1
    return kth_element






# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))
print(main([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7))