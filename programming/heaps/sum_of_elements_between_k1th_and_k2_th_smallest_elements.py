from heapq import heappop, heapify


def k1th_k2th_smallest_num_sum(array, k1, k2):
    min_heap = array[:]
    heapify(min_heap)

    i = 1
    while i < k1:
        heappop(min_heap)
        i += 1
    k1th_element = heappop(min_heap)

    while i < k2 - 1:
        heappop(min_heap)
        i += 1
    k2th_element = heappop(min_heap)

    total = 0
    for num in array:
        if k1th_element < num < k2th_element:
            total += num
    return total


if __name__ == '__main__':
    print(k1th_k2th_smallest_num_sum([20, 8, 22, 4, 12, 10, 14], 3, 6))
    print(k1th_k2th_smallest_num_sum([10, 2, 50, 12, 48, 13], 2, 6))
