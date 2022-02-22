import heapq


def min_cost_of_ropes(array):
    min_heap = array
    heapq.heapify(min_heap)
    total = 0
    while len(min_heap) > 1:
        num1 = heapq.heappop(min_heap)
        num2 = heapq.heappop(min_heap)
        temp_total = num1 + num2
        total += temp_total
        heapq.heappush(min_heap, temp_total)
    return total



if __name__ == '__main__':
    print(min_cost_of_ropes([4, 3, 2, 6]))