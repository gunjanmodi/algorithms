from heapq import heappop, heappush


def k_closest_numbers(array, x, k):
    min_heap = []
    for i, num in enumerate(array):
        item = (abs(num - x), num)
        heappush(min_heap, item)

    result = []
    j = 1
    # _ = heappop(min_heap)
    while j <= k:
        result.append(heappop(min_heap)[1])
        j += 1
    return result


if __name__ == '__main__':
    print(k_closest_numbers([5, 6, 7, 8, 9], 7, 3))
    print(k_closest_numbers([10, 2, 14, 4, 7, 6], 5, 3))
    print(k_closest_numbers([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 35, 4))
    print(k_closest_numbers([1, 2, 3, 6, 10], 4, 3))
