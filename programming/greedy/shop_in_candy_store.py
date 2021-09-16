"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O(nlogn) | Space: O(1)
def main(candies, k):
    candies.sort()
    min_amount, max_amount = 0, 0
    min_pointer, max_pointer = 0, len(candies) - 1
    total_min_length, total_max_length = len(candies) - 1, 0
    while min_pointer <= total_min_length:
        min_amount += candies[min_pointer]
        total_min_length -= k
        min_pointer += 1

    while max_pointer >= total_max_length:
        max_amount += candies[max_pointer]
        total_max_length += k
        max_pointer -= 1
    return [min_amount, max_amount]




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([3, 2, 1, 4], 2)) # 3, 7
print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)) # 15, 40
print(main([3, 2, 1, 4, 5], 4)) # 1, 5
