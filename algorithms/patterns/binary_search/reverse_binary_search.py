def reverse_binary_search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return -1



print(reverse_binary_search([9, 8, 7, 6, 5, 4, 3, 2, 1], 8))