from heapq import *

# def find_closest_elements(arr, K, X):
#     index = binary_search(arr, X)
#     low, high = index - K, index + K
    
#     low = max(low, 0)  # 'low' should not be less than zero
#     # 'high' should not be greater the size of the array
#     high = min(high, len(arr) - 1)

#     minHeap = []
#     # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
#     for i in range(low, high+1):
#         heappush(minHeap, (abs(arr[i] - X), arr[i]))

#     # we need the top 'K' elements having smallest difference from 'X'
#     result = []
#     for _ in range(K):
#         result.append(heappop(minHeap)[1])

#     result.sort()
#     return result


def find_closest_elements(arr, K, X):
    min_heap = []
    for i in range(len(arr)):
        absolute_distance = abs(arr[i] - X)
        heappush(min_heap, (absolute_distance, arr[i]))

    result = []
    for i in range(K):
        _, num = heappop(min_heap)
        result.append(num)
    result.sort()
    return result

# def binary_search(array, target):
#     low = 0
#     high = len(array) - 1
#     while low <= high:
#         mid = (low + high ) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     if low > 0:
#         return low - 1
#     return low
    
    



def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
