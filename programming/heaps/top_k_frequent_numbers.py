import heapq
from heapq import heapify


def top_k_frequent_numbers(array, k):
    counts = {}
    for i, num in enumerate(array):
        if num in counts:
            new_count = (counts[num][0]) + 1
            counts[num] = (new_count, num)
        else:
            counts[num] = (1, num)

    min_heap = list(counts.values())
    heapify(min_heap)
    result = heapq.nlargest(k, min_heap)
    return [item[1] for item in result]


if __name__ == '__main__':
    print(top_k_frequent_numbers([1,1,1,2,2,3], 2))
    print(top_k_frequent_numbers([1,1,2,2,3,3,3,4], 2))
    print(top_k_frequent_numbers([3, 1, 4, 4, 5, 2, 6, 1], 2))
    print(top_k_frequent_numbers([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4))
