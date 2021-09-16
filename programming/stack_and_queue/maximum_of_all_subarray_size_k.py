"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O(n) | Space: O(n)
from collections import deque
def main(array, k):
    result = []
    max_queue = deque()
    for i in range(len(array)):
        while max_queue and array[max_queue[-1]] < array[i]:
            max_queue.pop()
        max_queue.append(i)

        if max_queue[0] == i - k:
            max_queue.popleft()
        if i >= k - 1:
            result.append(array[max_queue[0]])
    return result


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1,3,1,2,0,5], 3))
print(main([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
print(main([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))