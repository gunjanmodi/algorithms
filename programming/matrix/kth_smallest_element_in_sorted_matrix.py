import heapq


def kth_smallest(matrix, k):
    heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
    heapq.heapify(heap)
    ret = 0
    for _ in range(k):
        ret, i, j = heapq.heappop(heap)
        if j + 1 < len(matrix[0]):
            heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
    return ret
#     flattened_list = []
#     i = 0
#     for row in matrix:
#         for j in range(len(row)):
#             value = row[j]
#             flattened_list.append(value)
#             if value < flattened_list[i-1]:
#                 flattened_list[i - 1], flattened_list[i] = flattened_list[i], flattened_list[i - 1]
#             i += 1
#     return flattened_list[k-1]


output = kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
print(output)
