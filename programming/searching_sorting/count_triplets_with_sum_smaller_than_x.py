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
    array.sort()
    count = 0
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum >= target:
                right -= 1
            else:
                count += (right-left)
                left += 1
    return count





# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 3, 4, 5, 7], 12))