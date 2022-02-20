import heapq
import math


# Time: O(nlogn) | Space: O(n)
def main(points, k):
    max_heap = []
    x, y = 0, 1
    for point in points:
        distance = math.pow(point[x], 2) + math.pow(point[y], 2)
        item = (distance * -1, point)
        heapq.heappush(max_heap, item)

    i = len(points)
    while i > k:
        heapq.heappop(max_heap)
        i -= 1

    return [item[1] for item in max_heap]


if __name__ == '__main__':
    print(main([[3, 3], [5, -1], [-2, 4]], 2))
    print(main([[1, 3], [-2, 2]], 1))
