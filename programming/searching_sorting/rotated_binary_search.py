"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O(log n) | Space: O(1)
def main(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif array[left] <= array[mid]:
            if target < array[mid] and target >= array[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > array[mid] and target <= array[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([4,5,6,7,0,1,2], 0))
