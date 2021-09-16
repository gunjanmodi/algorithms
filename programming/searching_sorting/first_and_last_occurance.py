"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array, x):
    left = 0
    right = len(array) - 1
    element_index = None
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            element_index = mid
            break
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    if not element_index:
        return [-1, -1]
    first = element_index
    last = element_index
    while first - 1 >= 0 and array[first] == array[first - 1] :
        first -= 1
    while last + 1 < len(array) and array[last] == array[last + 1]:
        last += 1
    return [first, last]





# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 8], 8))
print(main([1, 3, 5, 5, 5, 5, 67, 123, 125], 65))
print(main([], 65))
print(main([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))
print(main([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))


