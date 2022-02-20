"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array, k):
    result = []
    window_start = 0
    negative_start = 0
    for window_end in range(len(array)):
        if window_end >= k - 1:
            for i in range(window_start, window_end+1):
                if array[i] < 0:
                    negative_start = array[i]
                    break
            result.append(negative_start)
            window_start += 1
            negative_start = 0
    return result

from collections import deque
def main(array, k):
    result = []
    queue = deque()
    for i in range(k):
        if array[i] < 0:
            queue.append(i)

    for i in range(k, len(array)):
        if not queue:
            result.append(0)
        else:
            result.append(array[queue[0]])

        while queue and queue[0] <= (i-k):
            queue.popleft()

        if array[i] < 0:
            queue.append(i)

    if not queue:
        result.append(0)
    else:
        result.append(array[queue[0]])
    return result





# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(main([-8, 2, 3, -6, 10], 2))