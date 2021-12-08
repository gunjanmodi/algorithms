from heapq import heapify, heappop, heappush

def merge_k_sorted_arrays(matrix, k):
    min_heap = []
    result = []
    for i in range(len(matrix)):
        row = matrix[i]
        heappush(min_heap, (row[0], i, 0))

    rows = k
    colums = len(matrix[0])
    n = rows * colums
    i = 0
    while i < n:
        smallest, r, c  = heappop(min_heap)
        result.append(smallest)
        if c + 1 < colums:
            heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        i += 1
    return result


print(merge_k_sorted_arrays([[1,2,3,4],[2,2,3,4], [5,5,6,6],[7,8,9,9]], 4))

    
