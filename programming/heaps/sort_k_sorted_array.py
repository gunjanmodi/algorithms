from heapq import heappop, heappush


def sort_k_sorted_array(array, k):
    min_heap = []
    result = []
    for i, num in enumerate(array):
        heappush(min_heap, num)
        if i >= k:
            sorted_candidate = heappop(min_heap)
            result.append(sorted_candidate)
    while len(min_heap) > 0:
        result.append(heappop(min_heap))
    return result


if __name__ == '__main__':
    print(sort_k_sorted_array([6, 5, 3, 2, 8, 10, 9], 3))