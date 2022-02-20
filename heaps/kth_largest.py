from heapq import heappop, heappush

def kth_largest(array, k):
    min_heap = []
    i = 0
    while i < k:
        heappush(min_heap, array[i])
        i += 1

    while i < len(array) and min_heap:
        heappush(min_heap, array[i])
        heappop(min_heap)
        i += 1
    
    kth_largest = heappop(min_heap)
    return kth_largest


def kth_smallest(array, k):
    max_heap = []
    i = 0
    while i < k:
        heappush(max_heap, -array[i])
        i += 1

    while i < len(array) and max_heap:
        heappush(max_heap, -array[i])
        heappop(max_heap)
        i += 1
    
    kth_smallest = heappop(max_heap)
    return kth_smallest * -1


print(kth_largest([7, 10, 4, 3, 20, 15], 3))
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))