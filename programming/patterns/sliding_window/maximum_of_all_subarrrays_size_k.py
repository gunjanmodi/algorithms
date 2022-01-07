from collections import deque
def maximum_of_all_subarrrays_size_k(array, k):
    i = 0
    queue = deque()
    result = []
    for j in range(len(array)):
        while len(queue) > 0 and queue[0] < array[j]:
            queue.popleft()
        queue.append(array[j])
        if j - i + 1 == k:
            result.append(queue[0])
            if queue[0] == array[i]:
                queue.popleft()
            i += 1
    return result

            


print(maximum_of_all_subarrrays_size_k([1, 3, -1, -3, 5, 3, 6, 7], 3))