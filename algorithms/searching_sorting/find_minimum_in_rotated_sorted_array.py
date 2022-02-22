def main(array):
    left = 0
    right = len(array) - 1
    n = len(array)

    min_index = -1

    while left <= right:
        if array[left] < array[right]:
            return array[left]
        mid = (left + right) // 2

        next = (mid + 1) % n
        prev = (mid - 1 + n) % n

        if array[mid] <= array[prev] and array[mid] <= array[next]:
            return array[mid]
        elif array[left] <= array[mid]:
            left = mid + 1
        elif array[right] >= array[mid]:
            right = mid - 1


print(main([5, 1, 2, 3, 4]))
print(main([1, 2, 3, 4, 5]))
print(main([11, 12, 15, 18, 2, 5, 6, 8]))