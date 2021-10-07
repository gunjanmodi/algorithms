import heapq


def main(array):
    counts = {}
    for num in array:
        if num in counts:
            current_frequency = counts[num][0] * -1
            counts[num] = ((current_frequency + 1) * -1, num)
        else:
            counts[num] = (-1, num)

    max_heap = list(counts.values())
    heapq.heapify(max_heap)

    result = []
    while max_heap:
        element = heapq.heappop(max_heap)
        for i in range(element[0] * -1):
            result.append(element[1])
    print(*result)
    return result


if __name__ == '__main__':
    print(main([1, 1, 1, 3, 2, 2, 4]))