from collections import deque
def main(array, k):
    i = 0
    queue = deque()
    result = []
    for j in range(len(array)):
        if array[j] < 0:
            queue.append(array[j])
            
        if j - i + 1 >= k:
            if queue:
                result.append(queue[0])
                if array[i] == queue[0]:
                    queue.popleft()
            else:
                result.append(0)
            i += 1
    return result


print(main([12, -1, -7, 8, -15, 30, 16, 28], 3))