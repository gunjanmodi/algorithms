"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def sort_array(array):
    sort_array_helper(array)
    return array


def sort_array_helper(array):
    if len(array) <= 1:
        return
    last = array.pop()
    sort_array_helper(array)
    insert(array, last)


def insert(array, element):
    if len(array) == 0 or array[-1] <= element:
        array.append(element)
        return
    last = array.pop()
    insert(array, element)
    array.append(last)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(sort_array([1, 0, 5, 2]))
print(sort_array([5, 4, 2, 3, 1]))
print(sort_array([]))
print(sort_array([1,2,3,4,5]))
print(sort_array([1,2,3,4,5, 98,78, 5, 90, 5, 12, 9, 56, 5, 0, 2, 4, 2,90, 189]))
