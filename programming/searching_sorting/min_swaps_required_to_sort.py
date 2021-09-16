"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

import heapq
# Time: O(nlogn) | Space: O(n)
def main(nums):
    key_to_index = dict([(nums[i], i) for i in range(len(nums))])
    heap = nums[::]
    heapq.heapify(heap)
    swaps = 0
    for i in range(len(nums)):
        smallest = heapq.heappop(heap)
        if nums[i] != smallest:
            current = nums[i]
            nums[i], nums[key_to_index[smallest]] = nums[key_to_index[smallest]], nums[i]
            key_to_index[smallest], key_to_index[current] = key_to_index[current], key_to_index[smallest]
            swaps += 1
    return swaps



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([8, 3, 14, 17, 15, 1, 12]))
print(main([10, 19, 6, 3, 5]))
print(main([2, 8, 5, 4]))