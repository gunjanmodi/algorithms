"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O(n) | Space: O(1)
from collections import deque
def main(array, k):
    min_max_sum = 0
    min_queue = deque()
    max_queue = deque()
    for i in range(k):
        while min_queue and array[i] < array[min_queue[-1]]:
            min_queue.pop()

        while max_queue and array[i] > array[max_queue[-1]]:
            max_queue.pop()

        min_queue.append(i)
        max_queue.append(i)

    for window_end in range(k, len(array)):
        min_max_sum += array[min_queue[0]] + array[max_queue[0]]

        while (len(min_queue) > 0 and min_queue[0] <= window_end - k):
            min_queue.popleft()
        while (len(max_queue) > 0 and max_queue[0] <= window_end - k):
            max_queue.popleft()
        while min_queue and array[window_end] < array[min_queue[-1]]:
            min_queue.pop()

        while max_queue and array[window_end] > array[max_queue[-1]]:
            max_queue.pop()

        min_queue.append(window_end)
        max_queue.append(window_end)
    min_max_sum += array[min_queue[0]] + array[max_queue[0]]
    return min_max_sum


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([2, 5, -1, 7, -3, -1, -2], 3))