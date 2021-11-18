import heapq


def kth_smallest(matrix, k):
    result, heap = None, []
    heapq.heappush(heap, (matrix[0][0], 0, 0))
    while k > 0:
        result, i, j = heapq.heappop(heap)
        if i == 0 and j + 1 < len(matrix):
            heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        if i + 1 < len(matrix):
            heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
        k -= 1
    return result


def kth_smallest(matrix, k):
    max_heap = []
    for row in matrix:
        for value in row:
            max_heap.append(value)
    heapq.heapify(max_heap)

    for _ in range(k - 1):
        heapq.heappop(max_heap)
    result = heapq.heappop(max_heap)
    return result




print(kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(kth_smallest([ [16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94] ], 3))
